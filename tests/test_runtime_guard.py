from __future__ import annotations

import logging
import tempfile
import unittest
from pathlib import Path

from app.runtime_guard import SingleInstanceLock, configure_logging, run_startup_diagnostics


class RuntimeGuardTests(unittest.TestCase):
    def test_single_instance_lock_blocks_second_instance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            lock_path = Path(directory) / "app.lock"
            first = SingleInstanceLock(lock_path)
            second = SingleInstanceLock(lock_path)

            self.assertTrue(first.acquire())
            self.assertFalse(second.acquire())

            first.release()
            self.assertTrue(second.acquire())
            second.release()

    def test_configure_logging_creates_rotating_log(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            log_dir = Path(directory)
            logger = configure_logging(log_dir)
            logger.info("runtime guard test")

            for handler in logger.handlers:
                handler.flush()

            self.assertTrue((log_dir / "predixai_robo_listas.log").exists())

            for handler in list(logger.handlers):
                handler.close()
                logger.removeHandler(handler)
            logging.shutdown()

    def test_startup_diagnostics_passes_with_required_structure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("2.3.3\n", encoding="utf-8")
            (root / "config").mkdir()
            (root / "app").mkdir()
            (root / "app" / "main.py").write_text("", encoding="utf-8")

            result = run_startup_diagnostics(root)

            self.assertTrue(result.ok)
            self.assertEqual(result.messages, ())

    def test_startup_diagnostics_reports_missing_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = run_startup_diagnostics(Path(directory))

            self.assertFalse(result.ok)
            self.assertEqual(len(result.messages), 3)


if __name__ == "__main__":
    unittest.main()
