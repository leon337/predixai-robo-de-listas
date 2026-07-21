from datetime import datetime, timedelta, timezone

import pytest

from server.identity import (
    ClientRole,
    IdentityError,
    IdentityService,
    PairingChallengeRequest,
    PairingRequest,
)


class Clock:
    def __init__(self) -> None:
        self.now = datetime(2026, 7, 21, tzinfo=timezone.utc)

    def __call__(self) -> datetime:
        return self.now

    def advance(self, seconds: int) -> None:
        self.now += timedelta(seconds=seconds)


def service(clock: Clock) -> IdentityService:
    return IdentityService(
        pairing_ttl_seconds=60,
        session_ttl_seconds=120,
        clock=clock,
    )


def pair_client(identity: IdentityService) -> tuple[str, str]:
    challenge = identity.create_challenge(
        PairingChallengeRequest(
            device_id="device-001",
            operator_id="operator-001",
        )
    )
    session = identity.pair(
        PairingRequest(
            challenge=challenge.challenge,
        )
    )
    return challenge.challenge, session.access_token


def test_pairing_is_one_time_scoped_and_has_no_implicit_grant() -> None:
    clock = Clock()
    identity = service(clock)
    challenge, token = pair_client(identity)

    capabilities = identity.capabilities(token)
    assert capabilities.device_id == "device-001"
    assert capabilities.role is ClientRole.READ_ONLY
    assert capabilities.mode.value == "NULL"
    assert capabilities.command_grant is False
    assert capabilities.external_effects is False

    with pytest.raises(IdentityError, match="PAIRING_CODE_REUSE"):
        identity.pair(
            PairingRequest(
                challenge=challenge,
            )
        )


def test_expired_pairing_challenge_fails_closed() -> None:
    clock = Clock()
    identity = service(clock)
    challenge = identity.create_challenge(
        PairingChallengeRequest(
            device_id="device-001",
            operator_id="operator-001",
        )
    )
    clock.advance(61)

    with pytest.raises(IdentityError, match="PAIRING_CHALLENGE_EXPIRED"):
        identity.pair(
            PairingRequest(
                challenge=challenge.challenge,
            )
        )


def test_session_rotation_revokes_previous_token() -> None:
    clock = Clock()
    identity = service(clock)
    _challenge, token = pair_client(identity)

    renewed = identity.renew(token)
    assert renewed.access_token != token
    with pytest.raises(IdentityError, match="SESSION_INVALID"):
        identity.authenticate(token)
    assert identity.authenticate(renewed.access_token).device_id == "device-001"


def test_expired_session_fails_closed() -> None:
    clock = Clock()
    identity = service(clock)
    _challenge, token = pair_client(identity)
    clock.advance(121)

    with pytest.raises(IdentityError, match="SESSION_EXPIRED"):
        identity.authenticate(token)


def test_device_revocation_terminates_sessions() -> None:
    clock = Clock()
    identity = service(clock)
    _challenge, token = pair_client(identity)

    result = identity.revoke_device("device-001")
    assert result.sessions_terminated == 1
    with pytest.raises(IdentityError, match="SESSION_INVALID|DEVICE_REVOKED"):
        identity.authenticate(token)


def test_presence_sequence_never_becomes_authorization() -> None:
    clock = Clock()
    identity = service(clock)
    _challenge, token = pair_client(identity)

    first = identity.presence(token)
    second = identity.presence(token)
    assert (first.sequence, second.sequence) == (1, 2)
    assert first.authorization_grant is False
    assert second.authorization_grant is False
