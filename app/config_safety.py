#!/usr/bin/env python3
"""Backup, escrita atômica e recuperação da configuração."""
from __future__ import annotations

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any


class ConfigSafetyManager:
    def __init__(self, backup_dir: Path, max_backups: int = 10) -> None:
        self.backup_dir = backup_dir
        self.max_backups = max(1, max_backups)

    @staticmethod
    def is_valid_json(path: Path) -> bool:
        if not path.is_file():
            return False
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            return isinstance(payload, dict)
        except (OSError, UnicodeError, json.JSONDecodeError):
            return False

    def backup_current(self, config_path: Path) -> Path | None:
        if not self.is_valid_json(config_path):
            return None
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        destination = self.backup_dir / f"config_{stamp}.json"
        temporary = destination.with_suffix(".tmp")
        shutil.copy2(config_path, temporary)
        temporary.replace(destination)
        self._prune_backups()
        return destination

    def write_json(self, config_path: Path, payload: dict[str, Any]) -> Path | None:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        backup = self.backup_current(config_path)
        temporary = config_path.with_suffix(config_path.suffix + ".tmp")
        try:
            with temporary.open("w", encoding="utf-8") as stream:
                json.dump(payload, stream, ensure_ascii=False, indent=2)
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(config_path)
        finally:
            temporary.unlink(missing_ok=True)
        return backup

    def recover_if_needed(self, config_path: Path) -> Path | None:
        if not config_path.exists() or self.is_valid_json(config_path):
            return None

        self.backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        corrupt_copy = self.backup_dir / f"corrompido_{stamp}.json"
        shutil.copy2(config_path, corrupt_copy)

        for candidate in sorted(self.backup_dir.glob("config_*.json"), reverse=True):
            if not self.is_valid_json(candidate):
                continue
            temporary = config_path.with_suffix(config_path.suffix + ".recovery.tmp")
            try:
                shutil.copy2(candidate, temporary)
                temporary.replace(config_path)
            finally:
                temporary.unlink(missing_ok=True)
            return candidate
        return None

    def _prune_backups(self) -> None:
        backups = sorted(self.backup_dir.glob("config_*.json"), reverse=True)
        for obsolete in backups[self.max_backups :]:
            obsolete.unlink(missing_ok=True)
