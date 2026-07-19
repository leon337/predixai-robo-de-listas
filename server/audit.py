"""Auditoria local em memória, sem persistência externa."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import Lock
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class AuditEvent:
    event: str
    reason_code: str
    trace_id: str = field(default_factory=lambda: uuid4().hex)
    timestamp_utc: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class InMemoryAuditSink:
    """Coletor thread-safe e sem efeitos externos."""

    def __init__(self, enabled: bool = True) -> None:
        self._enabled = enabled
        self._events: list[AuditEvent] = []
        self._lock = Lock()

    def record(self, event: str, reason_code: str) -> AuditEvent | None:
        if not self._enabled:
            return None
        item = AuditEvent(event=event, reason_code=reason_code)
        with self._lock:
            self._events.append(item)
        return item

    def snapshot(self) -> tuple[AuditEvent, ...]:
        with self._lock:
            return tuple(self._events)
