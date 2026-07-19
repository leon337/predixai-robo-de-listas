"""Configuração tipada e fail-closed para a FND-001."""

from __future__ import annotations

import os

from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

from server.contracts import AdapterMode


class ServerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    host: str = "127.0.0.1"
    port: int = 8765
    mode: AdapterMode = AdapterMode.NULL
    audit_enabled: bool = True

    @field_validator("host")
    @classmethod
    def host_must_be_loopback(cls, value: str) -> str:
        if value not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("FND-001 aceita somente bind local")
        return value

    @field_validator("port")
    @classmethod
    def port_must_be_unprivileged(cls, value: int) -> int:
        if not 1024 <= value <= 65535:
            raise ValueError("porta deve estar entre 1024 e 65535")
        return value


def load_config(environ: dict[str, str] | None = None) -> ServerConfig:
    env = os.environ if environ is None else environ
    raw_mode = env.get("PREDIXAI_SERVER_MODE", "NULL").strip().upper()
    raw_audit = env.get("PREDIXAI_AUDIT_ENABLED", "true").strip().lower()

    if raw_mode != AdapterMode.NULL.value:
        raise ValueError("configuração bloqueada: somente NULL é permitido na FND-001")
    if raw_audit not in {"true", "false"}:
        raise ValueError("PREDIXAI_AUDIT_ENABLED deve ser true ou false")

    try:
        return ServerConfig(
            host=env.get("PREDIXAI_SERVER_HOST", "127.0.0.1"),
            port=int(env.get("PREDIXAI_SERVER_PORT", "8765")),
            mode=AdapterMode.NULL,
            audit_enabled=raw_audit == "true",
        )
    except (ValueError, ValidationError) as exc:
        raise ValueError(f"configuração fail-closed inválida: {exc}") from exc
