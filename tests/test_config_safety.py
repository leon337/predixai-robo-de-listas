from __future__ import annotations

import json
from pathlib import Path

from app.config_safety import ConfigSafetyManager


def test_atomic_write_creates_backup(tmp_path: Path) -> None:
    config = tmp_path / "config.json"
    backups = tmp_path / "backups"
    manager = ConfigSafetyManager(backups)

    config.write_text(json.dumps({"version": 1}), encoding="utf-8")
    backup = manager.write_json(config, {"version": 2})

    assert backup is not None
    assert json.loads(backup.read_text(encoding="utf-8"))["version"] == 1
    assert json.loads(config.read_text(encoding="utf-8"))["version"] == 2


def test_corrupt_config_recovers_latest_valid_backup(tmp_path: Path) -> None:
    config = tmp_path / "config.json"
    backups = tmp_path / "backups"
    manager = ConfigSafetyManager(backups)
    backups.mkdir()

    (backups / "config_20260101_000000_000001.json").write_text(
        json.dumps({"version": 3, "profiles": ["antigo"]}), encoding="utf-8"
    )
    (backups / "config_20260102_000000_000001.json").write_text(
        json.dumps({"version": 3, "profiles": ["recente"]}), encoding="utf-8"
    )
    config.write_text("{json quebrado", encoding="utf-8")

    recovered_from = manager.recover_if_needed(config)

    assert recovered_from is not None
    assert recovered_from.name == "config_20260102_000000_000001.json"
    assert json.loads(config.read_text(encoding="utf-8"))["profiles"] == ["recente"]
    assert list(backups.glob("corrompido_*.json"))


def test_invalid_config_without_backup_is_preserved_for_diagnostics(tmp_path: Path) -> None:
    config = tmp_path / "config.json"
    manager = ConfigSafetyManager(tmp_path / "backups")
    config.write_text("inválido", encoding="utf-8")

    recovered_from = manager.recover_if_needed(config)

    assert recovered_from is None
    assert config.read_text(encoding="utf-8") == "inválido"
    assert list((tmp_path / "backups").glob("corrompido_*.json"))


def test_backup_rotation_keeps_limit(tmp_path: Path) -> None:
    config = tmp_path / "config.json"
    manager = ConfigSafetyManager(tmp_path / "backups", max_backups=2)
    config.write_text(json.dumps({"value": 0}), encoding="utf-8")

    for value in range(4):
        manager.write_json(config, {"value": value + 1})

    assert len(list((tmp_path / "backups").glob("config_*.json"))) == 2
