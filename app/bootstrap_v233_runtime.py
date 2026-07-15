#!/usr/bin/env python3
"""Finalização de inicialização da V2.3.3."""
from __future__ import annotations

import main as app_main
from version_info import read_app_version

_PREVIOUS_INIT = None


def init_v233(self, root) -> None:
    _PREVIOUS_INIT(self, root)
    version = read_app_version(app_main.ROOT_DIR)
    self.root.title(f"PredixAI Robô de Listas — V{version}")


def install_patch() -> None:
    global _PREVIOUS_INIT
    cls = app_main.PredixAIRoboListas
    _PREVIOUS_INIT = cls.__init__
    cls.__init__ = init_v233
