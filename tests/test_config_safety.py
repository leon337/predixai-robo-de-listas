from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from app.config_safety import ConfigSafetyManager


class ConfigSafetyTests(unittest.TestCase):
    def test_atomic_write_creates_backup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / "config.json"
            backups = root / "backups"
            manager = ConfigSafetyManager(backups)

            config.write_text(json.dumps({"version": 1}), encoding="utf-8")
            backup = manager.write_json(config, {"version": 2})

            self.assertIsNotNone(backup)
            assert backup is not None
            self.assertEqual(json.loads(backup.read_text(encoding="utf-8"))["version"], 1)
            self.assertEqual(json.loads(config.read_text(encoding="utf-8"))["version"], 2)

    def test_corrupt_config_recovers_latest_valid_backup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / "config.json"
            backups = root / "backups"
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

            self.assertIsNotNone(recovered_from)
            assert recovered_from is not None
            self.assertEqual(recovered_from.name, "config_20260102_000000_000001.json")
            self.assertEqual(json.loads(config.read_text(encoding="utf-8"))["profiles"], ["recente"])
            self.assertTrue(list(backups.glob("corrompido_*.json")))

    def test_invalid_config_without_backup_is_preserved_for_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / "config.json"
            manager = ConfigSafetyManager(root / "backups")
            config.write_text("inválido", encoding="utf-8")

            recovered_from = manager.recover_if_needed(config)

            self.assertIsNone(recovered_from)
            self.assertEqual(config.read_text(encoding="utf-8"), "inválido")
            self.assertTrue(list((root / "backups").glob("corrompido_*.json")))

    def test_backup_rotation_keeps_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / "config.json"
            manager = ConfigSafetyManager(root / "backups", max_backups=2)
            config.write_text(json.dumps({"value": 0}), encoding="utf-8")

            for value in range(4):
                manager.write_json(config, {"value": value + 1})

            self.assertEqual(len(list((root / "backups").glob("config_*.json"))), 2)


if __name__ == "__main__":
    unittest.main()
