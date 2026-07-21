import json
from pathlib import Path

import pytest

from server.config import load_config
from server.contracts import AdapterMode


def test_default_config_is_local_and_null_only() -> None:
    config = load_config({})
    assert config.host == "127.0.0.1"
    assert config.mode is AdapterMode.NULL


def test_non_null_mode_is_rejected() -> None:
    with pytest.raises(ValueError, match="somente NULL"):
        load_config({"PREDIXAI_SERVER_MODE": "SIMULATED"})


def test_non_loopback_host_is_rejected() -> None:
    with pytest.raises(ValueError, match="fail-closed"):
        load_config({"PREDIXAI_SERVER_HOST": "0.0.0.0"})


def test_privileged_port_is_rejected() -> None:
    with pytest.raises(ValueError, match="fail-closed"):
        load_config({"PREDIXAI_SERVER_PORT": "80"})


def test_configuration_resolution_is_defaults_file_then_environment(tmp_path: Path) -> None:
    config_file = tmp_path / "server.json"
    config_file.write_text(
        json.dumps({"port": 9000, "audit_enabled": False, "session_ttl_seconds": 600}),
        encoding="utf-8",
    )

    config = load_config(
        {
            "PREDIXAI_SERVER_PORT": "9100",
            "PREDIXAI_AUDIT_ENABLED": "true",
            "PREDIXAI_ADMIN_SECRET": "local-test-secret",
        },
        config_path=config_file,
    )

    assert config.port == 9100
    assert config.audit_enabled is True
    assert config.session_ttl_seconds == 600
    assert config.admin_secret is not None
    assert "local-test-secret" not in repr(config)


def test_configuration_file_cannot_contain_secrets(tmp_path: Path) -> None:
    config_file = tmp_path / "server.json"
    config_file.write_text('{"admin_secret": "must-not-load"}', encoding="utf-8")

    with pytest.raises(ValueError, match="campos não autorizados"):
        load_config({}, config_path=config_file)


def test_identity_feature_flag_is_fail_closed() -> None:
    config = load_config({"PREDIXAI_IDENTITY_ENABLED": "false"})
    assert config.identity_enabled is False


def test_database_configuration_is_local_typed_and_null_only(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    config = load_config(
        {
            "PREDIXAI_DATABASE_PATH": "data/runtime.sqlite3",
            "PREDIXAI_DATABASE_BUSY_TIMEOUT_MS": "2000",
            "PREDIXAI_DATABASE_WAL_ENABLED": "false",
        }
    )

    assert config.database_path == (tmp_path / "data/runtime.sqlite3").resolve()
    assert config.database_busy_timeout_ms == 2000
    assert config.database_wal_enabled is False
    assert config.mode is AdapterMode.NULL


def test_database_configuration_rejects_path_outside_data(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    with pytest.raises(ValueError, match="diretório data"):
        load_config({"PREDIXAI_DATABASE_PATH": "../outside.db"})
