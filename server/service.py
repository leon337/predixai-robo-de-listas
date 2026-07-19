"""Serviço de autoridade local da FND-001."""

from __future__ import annotations

from threading import Lock
from uuid import uuid4

from server.adapters import NullAdapter
from server.audit import InMemoryAuditSink
from server.config import ServerConfig
from server.contracts import (
    CapabilitySnapshot,
    HealthResponse,
    ReasonCode,
    RuntimeState,
)


class SafeServerService:
    def __init__(self, config: ServerConfig) -> None:
        self.config = config
        self.adapter = NullAdapter()
        self.audit = InMemoryAuditSink(enabled=config.audit_enabled)
        self._state = RuntimeState.BOOTING
        self._reason = ReasonCode.CONFIG_FAIL_CLOSED
        self._lock = Lock()

    @property
    def state(self) -> RuntimeState:
        with self._lock:
            return self._state

    def start(self) -> None:
        with self._lock:
            self._state = RuntimeState.SAFE_IDLE
            self._reason = ReasonCode.STARTUP_COMPLETE
        self.audit.record("server_started", self._reason.value)

    def degrade(self) -> None:
        with self._lock:
            self._state = RuntimeState.DEGRADED
            self._reason = ReasonCode.CONFIG_FAIL_CLOSED
        self.audit.record("server_degraded", self._reason.value)

    def stop(self) -> None:
        with self._lock:
            self._state = RuntimeState.STOPPED
            self._reason = ReasonCode.STOP_REQUESTED
        self.audit.record("server_stopped", self._reason.value)

    def health(self) -> HealthResponse:
        with self._lock:
            state = self._state
            reason = self._reason
        trace_id = uuid4().hex
        response = HealthResponse(
            state=state,
            mode=self.config.mode,
            reason_code=reason,
            trace_id=trace_id,
        )
        self.audit.record(
            "health_snapshot_returned",
            reason.value,
            trace_id=trace_id,
        )
        return response

    def capabilities(self) -> CapabilitySnapshot:
        return CapabilitySnapshot(mode=self.config.mode)
