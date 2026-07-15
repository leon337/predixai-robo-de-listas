from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app import bootstrap_v242


class DummyApp:
    def __init__(self) -> None:
        self.loaded = False
        self.saved = False


class V242PatchChainTests(unittest.TestCase):
    def test_safe_load_delegates_to_previous_loader(self) -> None:
        app = DummyApp()

        def previous_load(instance) -> None:
            instance.loaded = True

        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text(json.dumps({"version": 4, "lists": []}), encoding="utf-8")
            manager = bootstrap_v242.ConfigSafetyManager(Path(temp_dir) / "backups")
            with patch.object(bootstrap_v242, "_PREVIOUS_LOAD", previous_load), patch.object(
                bootstrap_v242.app_main, "CONFIG_PATH", config
            ), patch.object(bootstrap_v242, "_MANAGER", manager):
                bootstrap_v242._safe_load(app)

        self.assertTrue(app.loaded)

    def test_safe_save_preserves_previous_serializer(self) -> None:
        app = DummyApp()

        def previous_save(instance) -> None:
            instance.saved = True

        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text(json.dumps({"version": 4, "lists": ["preservar"]}), encoding="utf-8")
            manager = bootstrap_v242.ConfigSafetyManager(Path(temp_dir) / "backups")
            with patch.object(bootstrap_v242, "_PREVIOUS_SAVE", previous_save), patch.object(
                bootstrap_v242.app_main, "CONFIG_PATH", config
            ), patch.object(bootstrap_v242, "_MANAGER", manager):
                bootstrap_v242._safe_save(app)

        self.assertTrue(app.saved)


if __name__ == "__main__":
    unittest.main()
