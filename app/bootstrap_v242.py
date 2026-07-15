#!/usr/bin/env python3
"""Integra backup e recuperação de configuração da V2.4.2."""
from __future__ import annotations

import logging
from dataclasses import asdict
from pathlib import Path

import main as app_main
from config_safety import ConfigSafetyManager

ROOT_DIR = Path(__file__).resolve().parents[1]
BACKUP_DIR = ROOT_DIR / "backups" / "config"
_MANAGER = ConfigSafetyManager(BACKUP_DIR, max_backups=10)
_INSTALLED = False
_ORIGINAL_LOAD = app_main.PredixAIRoboListas._load_config


def _safe_save(self: app_main.PredixAIRoboListas) -> None:
    payload = {
        "version": 3,
        "active_profile_id": self.active_profile_id,
        "active_list_id": self.active_list_id,
        "profiles": [asdict(profile) for profile in self.profiles],
        "history": self.history[-1000:],
    }
    backup = _MANAGER.write_json(app_main.CONFIG_PATH, payload)
    if backup:
        logging.getLogger("predixai.runtime").info("Backup de configuração criado: %s", backup)


def _safe_load(self: app_main.PredixAIRoboListas) -> None:
    config_exists = app_main.CONFIG_PATH.exists()
    config_was_valid = _MANAGER.is_valid_json(app_main.CONFIG_PATH) if config_exists else True
    recovered_from = _MANAGER.recover_if_needed(app_main.CONFIG_PATH)
    logger = logging.getLogger("predixai.runtime")

    if recovered_from:
        logger.warning("Configuração corrompida recuperada de: %s", recovered_from)
    elif config_exists and not config_was_valid:
        logger.error("Configuração corrompida sem backup válido; inicialização segura vazia.")

    _ORIGINAL_LOAD(self)


def install_patch() -> None:
    global _INSTALLED
    if _INSTALLED:
        return
    app_main.PredixAIRoboListas._save_config = _safe_save
    app_main.PredixAIRoboListas._load_config = _safe_load
    _INSTALLED = True
