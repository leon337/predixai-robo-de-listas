from __future__ import annotations

import logging
from pathlib import Path

from app.runtime_guard import SingleInstanceLock, configure_logging, run_startup_diagnostics


def test_single_instance_lock_blocks_second_instance(tmp_path: Path) -> None:
    lock_path = tmp_path / "app.lock"
    first = SingleInstanceLock(lock_path)
    second = SingleInstanceLock(lock_path)

    assert first.acquire() is True
    assert second.acquire() is False

    first.release()
    assert second.acquire() is True
    second.release()


def test_configure_logging_creates_rotating_log(tmp_path: Path) -> None:
    logger = configure_logging(tmp_path)
    logger.info("runtime guard test")

    for handler in logger.handlers:
        handler.flush()

    assert (tmp_path / "predixai_robo_listas.log").exists()

    for handler in list(logger.handlers):
        handler.close()
        logger.removeHandler(handler)
    logging.shutdown()


def test_startup_diagnostics_passes_with_required_structure(tmp_path: Path) -> None:
    (tmp_path / "VERSION").write_text("2.3.3\n", encoding="utf-8")
    (tmp_path / "config").mkdir()
    (tmp_path / "app").mkdir()
    (tmp_path / "app" / "main.py").write_text("", encoding="utf-8")

    result = run_startup_diagnostics(tmp_path)

    assert result.ok is True
    assert result.messages == ()


def test_startup_diagnostics_reports_missing_paths(tmp_path: Path) -> None:
    result = run_startup_diagnostics(tmp_path)

    assert result.ok is False
    assert len(result.messages) == 3
