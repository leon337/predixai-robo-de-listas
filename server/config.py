"""Configuração resolvida, tipada e fail-closed do servidor seguro."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, SecretStr, ValidationError, field_validator

from server.contracts import AdapterMode


class ServerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    host: str = "127.0.0.1"
    port: int = 8765
    mode: AdapterMode = AdapterMode.NULL
    audit_enabled: bool = True
    identity_enabled: bool = True
    pairing_ttl_seconds: int = 120
    session_ttl_seconds: int = 300
    admin_secret: SecretStr | None = None

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

    @field_validator("pairing_ttl_seconds", "session_ttl_seconds")
    @classmethod
    def ttl_must_be_bounded(cls, value: int) -> int:
        if not 30 <= value <= 3600:
            raise ValueError("TTL deve estar entre 30 e 3600 segundos")
        return value

FILE_KEYS = {
    "host",
    "port",
    "mode",
    "audit_enabled",
    "identity_enabled",
    "pairing_ttl_seconds",
    "session_ttl_seconds",
}

ENV_KEYS = {
    "PREDIXAI_SERVER_HOST": "host",
    "PREDIXAI_SERVER_PORT": "port",
    "PREDIXAI_SERVER_MODE": "mode",
    "PREDIXAI_AUDIT_ENABLED": "audit_enabled",
    "PREDIXAI_IDENTITY_ENABLED": "identity_enabled",
    "PREDIXAI_PAIRING_TTL_SECONDS": "pairing_ttl_seconds",
    "PREDIXAI_SESSION_TTL_SECONDS": "session_ttl_seconds",
}


def _parse_bool(name: str, value: Any) -> bool:
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized not in {"true", "false"}:
        raise ValueError(f"{name} deve ser true ou false")
    return normalized == "true"


def _load_authorized_file(path: Path) -> dict[str, Any]:
    if path.suffix.lower() != ".json":
        raise ValueError("arquivo de configuração autorizado deve ser JSON")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"arquivo de configuração inválido: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("configuração deve ser um objeto JSON")
    unknown = set(payload) - FILE_KEYS
    if unknown:
        raise ValueError(f"campos não autorizados na configuração: {sorted(unknown)}")
    return payload


def load_config(
    environ: dict[str, str] | None = None,
    *,
    config_path: Path | None = None,
) -> ServerConfig:
    """Resolve defaults, arquivo explícito e ambiente, nesta precedência."""
    env = os.environ if environ is None else environ
    values: dict[str, Any] = {}

    selected_path = config_path
    if selected_path is None and env.get("PREDIXAI_CONFIG_FILE"):
        candidate = Path(env["PREDIXAI_CONFIG_FILE"]).expanduser().resolve()
        authorized_dir = (Path.cwd() / "config").resolve()
        if candidate.parent != authorized_dir:
            raise ValueError("PREDIXAI_CONFIG_FILE deve apontar para o diretório config/")
        selected_path = candidate
    if selected_path is not None:
        values.update(_load_authorized_file(selected_path))

    for env_key, field_name in ENV_KEYS.items():
        if env_key in env:
            values[field_name] = env[env_key]

    raw_mode = str(values.get("mode", "NULL")).strip().upper()

    if raw_mode != AdapterMode.NULL.value:
        raise ValueError("configuração bloqueada: somente NULL é permitido na FND-003")

    try:
        return ServerConfig(
            host=str(values.get("host", "127.0.0.1")),
            port=int(values.get("port", 8765)),
            mode=AdapterMode.NULL,
            audit_enabled=_parse_bool("audit_enabled", values.get("audit_enabled", True)),
            identity_enabled=_parse_bool("identity_enabled", values.get("identity_enabled", True)),
            pairing_ttl_seconds=int(values.get("pairing_ttl_seconds", 120)),
            session_ttl_seconds=int(values.get("session_ttl_seconds", 300)),
            admin_secret=SecretStr(env["PREDIXAI_ADMIN_SECRET"])
            if env.get("PREDIXAI_ADMIN_SECRET")
            else None,
        )
    except (ValueError, ValidationError) as exc:
        raise ValueError(f"configuração fail-closed inválida: {exc}") from exc
