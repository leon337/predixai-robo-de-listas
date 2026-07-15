#!/usr/bin/env python3
"""Integra backup e recuperação preservando a cadeia de patches existente."""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable

try:
    import main as app_main
    from config_safety import ConfigSafetyManager
except ModuleNotFoundError:
    from app import main as app_main
    from app.config_safety import ConfigSafetyManager

ROOT_DIR = Path(__file__).resolve().parents[1]
BACKUP_DIR = ROOT_DIR / "backups" / "config"
_MANAGER = ConfigSafetyManager(BACKUP_DIR, max_backups=10)
_INSTALLED = False
_PREVIOUS_LOAD: Callable | None = None
_PREVIOUS_SAVE: Callable | None = None


def _safe_save(self: app_main.PredixAIRoboListas) -> None:
    """Cria backup e delega ao salvamento vigente, preservando o schema V4."""
    if _PREVIOUS_SAVE is None:
        raise RuntimeError("Patch de salvamento seguro não inicializado")
    backup = _MANAGER.backup_current(app_main.CONFIG_PATH)
    _PREVIOUS_SAVE(self)
    if backup:
        logging.getLogger("predixai.runtime").info(
            "Backup de configuração criado: %s", backup
        )


def _safe_load(self: app_main.PredixAIRoboListas) -> None:
    """Recupera JSON inválido e delega ao carregamento vigente."""
    if _PREVIOUS_LOAD is None:
        raise RuntimeError("Patch de carregamento seguro não inicializado")

    config_exists = app_main.CONFIG_PATH.exists()
    config_was_valid = _MANAGER.is_valid_json(app_main.CONFIG_PATH) if config_exists else True
    recovered_from = _MANAGER.recover_if_needed(app_main.CONFIG_PATH)
    logger = logging.getLogger("predixai.runtime")

    if recovered_from:
        logger.warning("Configuração corrompida recuperada de: %s", recovered_from)
    elif config_exists and not config_was_valid:
        logger.error("Configuração corrompida sem backup válido; carregamento legado decidirá o fallback.")

    _PREVIOUS_LOAD(self)


def install_patch() -> None:
    global _INSTALLED, _PREVIOUS_LOAD, _PREVIOUS_SAVE
    if _INSTALLED:
        return

    cls = app_main.PredixAIRoboListas
    _PREVIOUS_LOAD = cls._load_config
    _PREVIOUS_SAVE = cls._save_config
    cls._save_config = _safe_save
    cls._load_config = _safe_load
    _INSTALLED = True
