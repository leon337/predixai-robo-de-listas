from __future__ import annotations

import importlib
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

from app.config_safety import ConfigSafetyManager


class DummyPredixAIRoboListas:
    def _load_config(self) -> None:
        pass

    def _save_config(self) -> None:
        pass


class DummyApp:
    def __init__(self) -> None:
        self.loaded = False
        self.saved = False


def load_bootstrap_module():
    app_dir = Path(__file__).resolve().parents[1] / "app"
    fake_main = types.ModuleType("main")
    fake_main.ROOT_DIR = app_dir.parent
    fake_main.CONFIG_PATH = app_dir.parent / "config" / "config_predixai_robo_listas.json"
    fake_main.PredixAIRoboListas = DummyPredixAIRoboListas

    sys.modules["main"] = fake_main
    sys.modules["config_safety"] = importlib.import_module("app.config_safety")
    sys.modules.pop("bootstrap_v242", None)
    sys.path.insert(0, str(app_dir))
    try:
        return importlib.import_module("bootstrap_v242")
    finally:
        sys.path.remove(str(app_dir))


bootstrap_v242 = load_bootstrap_module()


class V242PatchChainTests(unittest.TestCase):
    def test_safe_load_delegates_to_previous_loader(self) -> None:
        app = DummyApp()

        def previous_load(instance) -> None:
            instance.loaded = True

        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text(json.dumps({"version": 4, "lists": []}), encoding="utf-8")
            manager = ConfigSafetyManager(Path(temp_dir) / "backups")
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
            manager = ConfigSafetyManager(Path(temp_dir) / "backups")
            with patch.object(bootstrap_v242, "_PREVIOUS_SAVE", previous_save), patch.object(
                bootstrap_v242.app_main, "CONFIG_PATH", config
            ), patch.object(bootstrap_v242, "_MANAGER", manager):
                bootstrap_v242._safe_save(app)

        self.assertTrue(app.saved)


if __name__ == "__main__":
    unittest.main()
