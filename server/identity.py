"""Identidade local, pareamento revogável e presença sem grant implícito."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
from enum import StrEnum
from hashlib import sha256
from secrets import token_hex, token_urlsafe
from threading import Lock
from typing import Callable

from pydantic import BaseModel, ConfigDict, Field

from server.contracts import API_VERSION, AdapterMode


class ClientRole(StrEnum):
    READ_ONLY = "READ_ONLY"
    CONTROLLED_OPERATOR = "CONTROLLED_OPERATOR"
    ADMIN = "ADMIN"


class PairingChallengeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    device_id: str = Field(pattern=r"^[a-zA-Z0-9][a-zA-Z0-9._-]{2,63}$")
    operator_id: str = Field(pattern=r"^[a-zA-Z0-9][a-zA-Z0-9._-]{2,63}$")


class PairingRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    challenge: str = Field(min_length=8, max_length=32)


class PairingChallengeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    challenge: str
    expires_at_utc: datetime
    device_id: str
    operator_id: str


class SessionResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    access_token: str
    token_type: str = "bearer"
    expires_at_utc: datetime
    device_id: str
    operator_id: str
    role: ClientRole
    authorization_grant: bool = False


class PresenceSnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    device_id: str
    operator_id: str
    sequence: int
    connected: bool = True
    authorization_grant: bool = False


class ClientCapabilitySnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    device_id: str
    operator_id: str
    role: ClientRole
    mode: AdapterMode = AdapterMode.NULL
    read_runtime: bool = True
    command_grant: bool = False
    external_effects: bool = False
    real_click: bool = False
    broker_connection: bool = False
    live_mode: bool = False


class RevocationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    device_id: str
    revoked: bool = True
    sessions_terminated: int


@dataclass(slots=True)
class _Challenge:
    digest: str
    expires_at: datetime
    device_id: str
    operator_id: str
    used: bool = False


@dataclass(slots=True)
class _Device:
    device_id: str
    operator_id: str
    role: ClientRole
    revocation_version: int = 0
    revoked: bool = False
    presence_sequence: int = 0


@dataclass(slots=True)
class _Session:
    token_digest: str
    device_id: str
    operator_id: str
    role: ClientRole
    revocation_version: int
    expires_at: datetime
    revoked: bool = False


class IdentityError(ValueError):
    """Erro seguro com reason code estável."""

    def __init__(self, reason_code: str) -> None:
        self.reason_code = reason_code
        super().__init__(reason_code)


class IdentityService:
    def __init__(
        self,
        *,
        pairing_ttl_seconds: int,
        session_ttl_seconds: int,
        clock: Callable[[], datetime] | None = None,
    ) -> None:
        self._pairing_ttl = timedelta(seconds=pairing_ttl_seconds)
        self._session_ttl = timedelta(seconds=session_ttl_seconds)
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self._challenges: dict[str, _Challenge] = {}
        self._devices: dict[str, _Device] = {}
        self._sessions: dict[str, _Session] = {}
        self._lock = Lock()

    @staticmethod
    def _digest(value: str) -> str:
        return sha256(value.encode("utf-8")).hexdigest()

    def create_challenge(
        self,
        request: PairingChallengeRequest,
    ) -> PairingChallengeResponse:
        raw = token_hex(8)
        digest = self._digest(raw)
        expires_at = self._clock() + self._pairing_ttl
        with self._lock:
            self._challenges[digest] = _Challenge(
                digest=digest,
                expires_at=expires_at,
                device_id=request.device_id,
                operator_id=request.operator_id,
            )
        return PairingChallengeResponse(
            challenge=raw,
            expires_at_utc=expires_at,
            device_id=request.device_id,
            operator_id=request.operator_id,
        )

    def pair(self, request: PairingRequest) -> SessionResponse:
        now = self._clock()
        digest = self._digest(request.challenge)
        with self._lock:
            challenge = self._challenges.get(digest)
            if challenge is None:
                raise IdentityError("PAIRING_CHALLENGE_UNKNOWN")
            if challenge.used:
                raise IdentityError("PAIRING_CODE_REUSE")
            if now >= challenge.expires_at:
                raise IdentityError("PAIRING_CHALLENGE_EXPIRED")
            existing = self._devices.get(challenge.device_id)
            if existing is not None and not existing.revoked:
                raise IdentityError("DEVICE_ALREADY_PAIRED")

            challenge.used = True
            device = _Device(
                device_id=challenge.device_id,
                operator_id=challenge.operator_id,
                role=ClientRole.READ_ONLY,
            )
            self._devices[challenge.device_id] = device
            return self._issue_session_locked(device, now)

    def authenticate(self, raw_token: str) -> _Session:
        now = self._clock()
        with self._lock:
            return replace(self._require_session_locked(raw_token, now))

    def renew(self, raw_token: str) -> SessionResponse:
        now = self._clock()
        with self._lock:
            session = self._require_session_locked(raw_token, now)
            session.revoked = True
            device = self._devices[session.device_id]
            return self._issue_session_locked(device, now)

    def presence(self, raw_token: str) -> PresenceSnapshot:
        now = self._clock()
        with self._lock:
            session = self._require_session_locked(raw_token, now)
            device = self._devices[session.device_id]
            device.presence_sequence += 1
            return PresenceSnapshot(
                device_id=device.device_id,
                operator_id=device.operator_id,
                sequence=device.presence_sequence,
            )

    def capabilities(self, raw_token: str) -> ClientCapabilitySnapshot:
        now = self._clock()
        with self._lock:
            session = self._require_session_locked(raw_token, now)
            return ClientCapabilitySnapshot(
                device_id=session.device_id,
                operator_id=session.operator_id,
                role=session.role,
            )

    def revoke_device(self, device_id: str) -> RevocationResponse:
        with self._lock:
            device = self._devices.get(device_id)
            if device is None:
                raise IdentityError("DEVICE_UNKNOWN")
            device.revoked = True
            device.revocation_version += 1
            count = 0
            for session in self._sessions.values():
                if session.device_id == device_id and not session.revoked:
                    session.revoked = True
                    count += 1
            return RevocationResponse(device_id=device_id, sessions_terminated=count)

    def _require_session_locked(self, raw_token: str, now: datetime) -> _Session:
        digest = self._digest(raw_token)
        session = self._sessions.get(digest)
        if session is None or session.revoked:
            raise IdentityError("SESSION_INVALID")
        device = self._devices.get(session.device_id)
        if device is None or device.revoked:
            raise IdentityError("DEVICE_REVOKED")
        if session.revocation_version != device.revocation_version:
            raise IdentityError("SESSION_REVOKED")
        if now >= session.expires_at:
            raise IdentityError("SESSION_EXPIRED")
        return session

    def _issue_session_locked(self, device: _Device, now: datetime) -> SessionResponse:
        raw_token = token_urlsafe(32)
        digest = self._digest(raw_token)
        expires_at = now + self._session_ttl
        self._sessions[digest] = _Session(
            token_digest=digest,
            device_id=device.device_id,
            operator_id=device.operator_id,
            role=device.role,
            revocation_version=device.revocation_version,
            expires_at=expires_at,
        )
        return SessionResponse(
            access_token=raw_token,
            expires_at_utc=expires_at,
            device_id=device.device_id,
            operator_id=device.operator_id,
            role=device.role,
        )
