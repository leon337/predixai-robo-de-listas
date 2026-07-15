#!/usr/bin/env python3
"""Leitura segura da versão publicada do aplicativo."""
from __future__ import annotations

from pathlib import Path


def read_app_version(root_dir: Path) -> str:
    """Retorna a versão registrada em VERSION ou um fallback explícito."""
    try:
        value = (root_dir / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        return "desconhecida"
    return value or "desconhecida"
