"""Aplicação FastAPI da fundação segura."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from hmac import compare_digest
from typing import Callable, TypeVar

from fastapi import FastAPI, Header, HTTPException, Query, status

from server.config import ServerConfig, load_config
from server.contracts import CapabilitySnapshot, HealthResponse
from server.read_model import (
    AuditEventPage,
    DiagnosticSnapshot,
    RuntimeSnapshot,
    SafeRuntimeReadModel,
)
from server.service import SafeServerService
from server.identity import (
    ClientCapabilitySnapshot,
    IdentityError,
    PairingChallengeRequest,
    PairingChallengeResponse,
    PairingRequest,
    PresenceSnapshot,
    RevocationResponse,
    SessionResponse,
)

T = TypeVar("T")


def create_app(config: ServerConfig | None = None) -> FastAPI:
    resolved_config = config or load_config()
    service = SafeServerService(resolved_config)
    read_model = SafeRuntimeReadModel(service)

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        service.start()
        yield
        service.stop()

    app = FastAPI(
        title="PredixAI Safe Server",
        version="2.5.0-alpha.2",
        lifespan=lifespan,
    )
    app.state.service = service
    app.state.read_model = read_model

    @app.get("/api/v1/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return service.health()

    @app.get("/api/v1/capabilities", response_model=CapabilitySnapshot)
    def capabilities() -> CapabilitySnapshot:
        return service.capabilities()

    @app.get("/api/v1/persistence/health")
    def persistence_health() -> dict[str, object]:
        if service.persistence is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="PERSISTENCE_DISABLED",
            )
        return service.persistence.health()

    def require_identity_enabled() -> None:
        if not resolved_config.identity_enabled:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="IDENTITY_DISABLED",
            )

    def require_admin(x_predixai_admin_secret: str | None = Header(default=None)) -> None:
        require_identity_enabled()
        configured = resolved_config.admin_secret
        if configured is None or x_predixai_admin_secret is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="ADMIN_REQUIRED")
        if not compare_digest(configured.get_secret_value(), x_predixai_admin_secret):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="ADMIN_REQUIRED")

    def bearer_token(authorization: str | None = Header(default=None)) -> str:
        require_identity_enabled()
        if authorization is None or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="SESSION_REQUIRED")
        token = authorization.removeprefix("Bearer ").strip()
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="SESSION_REQUIRED")
        return token

    def identity_call(operation: str, call: Callable[[], T]) -> T:
        try:
            result = call()
        except IdentityError as exc:
            service.audit.record(f"identity_{operation}_rejected", exc.reason_code)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=exc.reason_code) from exc
        service.audit.record(f"identity_{operation}_completed", f"{operation.upper()}_COMPLETE")
        return result

    @app.post(
        "/api/v1/identity/pairing/challenges",
        response_model=PairingChallengeResponse,
    )
    def create_pairing_challenge(
        request: PairingChallengeRequest,
        x_predixai_admin_secret: str | None = Header(default=None),
    ) -> PairingChallengeResponse:
        require_admin(x_predixai_admin_secret)
        return identity_call(
            "challenge",
            lambda: service.identity.create_challenge(request),
        )

    @app.post("/api/v1/identity/pair", response_model=SessionResponse)
    def pair(request: PairingRequest) -> SessionResponse:
        require_identity_enabled()
        return identity_call("pairing", lambda: service.identity.pair(request))

    @app.post("/api/v1/identity/sessions/renew", response_model=SessionResponse)
    def renew_session(authorization: str | None = Header(default=None)) -> SessionResponse:
        token = bearer_token(authorization)
        return identity_call("session_renewal", lambda: service.identity.renew(token))

    @app.post("/api/v1/identity/presence", response_model=PresenceSnapshot)
    def presence(authorization: str | None = Header(default=None)) -> PresenceSnapshot:
        token = bearer_token(authorization)
        return identity_call("presence", lambda: service.identity.presence(token))

    @app.get("/api/v1/identity/capabilities", response_model=ClientCapabilitySnapshot)
    def client_capabilities(
        authorization: str | None = Header(default=None),
    ) -> ClientCapabilitySnapshot:
        token = bearer_token(authorization)
        return identity_call("capabilities", lambda: service.identity.capabilities(token))

    @app.post(
        "/api/v1/identity/devices/{device_id}/revoke",
        response_model=RevocationResponse,
    )
    def revoke_device(
        device_id: str,
        x_predixai_admin_secret: str | None = Header(default=None),
    ) -> RevocationResponse:
        require_admin(x_predixai_admin_secret)
        return identity_call("revocation", lambda: service.identity.revoke_device(device_id))

    @app.get("/api/v1/runtime", response_model=RuntimeSnapshot)
    def runtime() -> RuntimeSnapshot:
        return read_model.runtime()

    @app.get("/api/v1/audit/events", response_model=AuditEventPage)
    def audit_events(
        offset: int = Query(default=0, ge=0),
        limit: int = Query(default=20, ge=1, le=100),
        event: str | None = Query(default=None, max_length=64),
    ) -> AuditEventPage:
        return read_model.audit_events(offset=offset, limit=limit, event=event)

    @app.get("/api/v1/diagnostics", response_model=DiagnosticSnapshot)
    def diagnostics() -> DiagnosticSnapshot:
        return read_model.diagnostics()

    return app


app = create_app()
