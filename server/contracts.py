"""Contratos versionados da fundação segura."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

API_VERSION = "v1"


class RuntimeState(StrEnum):
    BOOTING = "BOOTING"
    SAFE_IDLE = "SAFE_IDLE"
    DEGRADED = "DEGRADED"
    STOPPED = "STOPPED"


class AdapterMode(StrEnum):
    NULL = "NULL"


class ReasonCode(StrEnum):
    STARTUP_COMPLETE = "STARTUP_COMPLETE"
    CONFIG_FAIL_CLOSED = "CONFIG_FAIL_CLOSED"
    NULL_ADAPTER_ACTIVE = "NULL_ADAPTER_ACTIVE"
    STOP_REQUESTED = "STOP_REQUESTED"


class HealthResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    service: str = "predixai-safe-server"
    state: RuntimeState
    mode: AdapterMode
    reason_code: ReasonCode
    trace_id: str = Field(default_factory=lambda: uuid4().hex)
    timestamp_utc: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CapabilitySnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = API_VERSION
    mode: AdapterMode = AdapterMode.NULL
    external_effects: bool = False
    real_click: bool = False
    broker_connection: bool = False
    live_mode: bool = False
    database: bool = False
    signal_engine: bool = False
    supported_states: tuple[RuntimeState, ...] = tuple(RuntimeState)
