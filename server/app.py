"""Aplicação FastAPI da fundação segura."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query

from server.config import ServerConfig, load_config
from server.contracts import CapabilitySnapshot, HealthResponse
from server.read_model import (
    AuditEventPage,
    DiagnosticSnapshot,
    RuntimeSnapshot,
    SafeRuntimeReadModel,
)
from server.service import SafeServerService


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
        version="1.1.0-fnd.002",
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
