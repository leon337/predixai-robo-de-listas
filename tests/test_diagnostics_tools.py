from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from app.diagnostics_tools import (
    collect_diagnostics,
    diagnostic_summary,
    export_diagnostic_report,
    read_version,
)


class DiagnosticsToolsTests(unittest.TestCase):
    def test_read_version(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("2.4.3\n", encoding="utf-8")
            self.assertEqual(read_version(root), "2.4.3")

    def test_collect_diagnostics_reports_missing_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("2.4.3\n", encoding="utf-8")
            items = collect_diagnostics(root)
            self.assertTrue(any(item.status == "FAIL" for item in items))
            self.assertIn("FAIL", diagnostic_summary(items))

    def test_export_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("2.4.3\n", encoding="utf-8")
            items = collect_diagnostics(root)
            report = export_diagnostic_report(root, items)
            self.assertTrue(report.is_file())
            content = report.read_text(encoding="utf-8")
            self.assertIn("DIAGNÓSTICO V2.4.3", content)
            self.assertIn("Resumo:", content)


if __name__ == "__main__":
    unittest.main()
