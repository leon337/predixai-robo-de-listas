"""Aplicação FastAPI da fundação segura."""

from __future__ import annotations

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI

from server.config import ServerConfig, load_config
from server.contracts import CapabilitySnapshot, HealthResponse
from server.service import SafeServerService


def create_app(config: ServerConfig | None = None) -> FastAPI:
    resolved_config = config or load_config()
    service = SafeServerService(resolved_config)

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        service.start()
        yield
        service.stop()

    app = FastAPI(
        title="PredixAI Safe Server",
        version="1.0.0-fnd.001",
        lifespan=lifespan,
    )
    app.state.service = service

    @app.get("/api/v1/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return service.health()

    @app.get("/api/v1/capabilities", response_model=CapabilitySnapshot)
    def capabilities() -> CapabilitySnapshot:
        return service.capabilities()

    return app


app = create_app()
