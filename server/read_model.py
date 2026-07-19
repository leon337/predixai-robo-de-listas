"""Camada somente leitura do runtime em modo NULL_ONLY."""

from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field

from server.audit import AuditEvent
from server.contracts import API_VERSION, AdapterMode, ReasonCode, RuntimeState
from server.service import SafeServerService

MAX_AUDIT_PAGE_SIZE = 100


class RuntimeSnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    state: RuntimeState
    mode: AdapterMode
    reason_code: ReasonCode
    audit_enabled: bool
    external_effects: bool = False
    timestamp_utc: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AuditEventView(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event: str
    reason_code: str
    trace_id: str
    timestamp_utc: str


class AuditEventPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    items: tuple[AuditEventView, ...]
    offset: int
    limit: int
    total: int
    has_more: bool


class DiagnosticSnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    status: str
    mode: AdapterMode
    state: RuntimeState
    audit_event_count: int
    external_effects: bool = False
    database: bool = False
    live_mode: bool = False


class SafeRuntimeReadModel:
    """Projeção defensiva sem comandos de mutação ou persistência."""

    def __init__(self, service: SafeServerService) -> None:
        self._service = service

    def runtime(self) -> RuntimeSnapshot:
        health = self._service.health()
        return RuntimeSnapshot(
            state=health.state,
            mode=health.mode,
            reason_code=health.reason_code,
            audit_enabled=self._service.config.audit_enabled,
        )

    def audit_events(
        self,
        *,
        offset: int = 0,
        limit: int = 20,
        event: str | None = None,
    ) -> AuditEventPage:
        safe_offset = max(offset, 0)
        safe_limit = min(max(limit, 1), MAX_AUDIT_PAGE_SIZE)
        events = self._service.audit.snapshot()
        filtered = tuple(item for item in events if event is None or item.event == event)
        page = filtered[safe_offset : safe_offset + safe_limit]
        return AuditEventPage(
            items=tuple(self._to_view(item) for item in page),
            offset=safe_offset,
            limit=safe_limit,
            total=len(filtered),
            has_more=safe_offset + len(page) < len(filtered),
        )

    def diagnostics(self) -> DiagnosticSnapshot:
        events = self._service.audit.snapshot()
        return DiagnosticSnapshot(
            status="SAFE",
            mode=self._service.config.mode,
            state=self._service.state,
            audit_event_count=len(events),
        )

    @staticmethod
    def _to_view(item: AuditEvent) -> AuditEventView:
        return AuditEventView(
            event=item.event,
            reason_code=item.reason_code,
            trace_id=item.trace_id,
            timestamp_utc=item.timestamp_utc,
        )
