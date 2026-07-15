#!/usr/bin/env python3
"""Proteções de runtime da V2.4.1.

Mantém uma única instância da aplicação, configura logs rotativos e executa
checagens mínimas antes da interface ser aberta.
"""
from __future__ import annotations

import fcntl
import logging
import os
import sys
from dataclasses import dataclass
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import TextIO


@dataclass(frozen=True)
class DiagnosticResult:
    ok: bool
    messages: tuple[str, ...]


class SingleInstanceLock:
    """Lock não bloqueante mantido enquanto o processo estiver ativo."""

    def __init__(self, lock_path: Path) -> None:
        self.lock_path = lock_path
        self._handle: TextIO | None = None

    def acquire(self) -> bool:
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        handle = self.lock_path.open("a+", encoding="utf-8")
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            handle.close()
            return False

        handle.seek(0)
        handle.truncate()
        handle.write(str(os.getpid()))
        handle.flush()
        self._handle = handle
        return True

    def release(self) -> None:
        if self._handle is None:
            return
        try:
            fcntl.flock(self._handle.fileno(), fcntl.LOCK_UN)
        finally:
            self._handle.close()
            self._handle = None
            try:
                self.lock_path.unlink(missing_ok=True)
            except OSError:
                pass

    def __enter__(self) -> "SingleInstanceLock":
        if not self.acquire():
            raise RuntimeError("Outra instância do PredixAI Robô de Listas já está aberta.")
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.release()


def configure_logging(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("predixai_robo_listas")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = RotatingFileHandler(
            log_dir / "predixai_robo_listas.log",
            maxBytes=1_000_000,
            backupCount=5,
            encoding="utf-8",
        )
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        logger.addHandler(handler)

    return logger


def run_startup_diagnostics(root_dir: Path) -> DiagnosticResult:
    messages: list[str] = []

    if sys.version_info < (3, 10):
        messages.append("Python 3.10 ou superior é obrigatório.")

    required_paths = (
        root_dir / "VERSION",
        root_dir / "config",
        root_dir / "app" / "main.py",
    )
    for path in required_paths:
        if not path.exists():
            messages.append(f"Caminho obrigatório ausente: {path}")

    config_dir = root_dir / "config"
    if config_dir.exists() and not os.access(config_dir, os.W_OK):
        messages.append(f"Sem permissão de escrita: {config_dir}")

    return DiagnosticResult(ok=not messages, messages=tuple(messages))
