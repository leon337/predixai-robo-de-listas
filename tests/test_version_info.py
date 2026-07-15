from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest

APP_DIR = Path(__file__).resolve().parents[1] / "app"
sys.path.insert(0, str(APP_DIR))

from version_info import read_app_version


class VersionInfoTests(unittest.TestCase):
    def test_reads_version_file(self):
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "VERSION").write_text("2.3.3\n", encoding="utf-8")
            self.assertEqual(read_app_version(root), "2.3.3")

    def test_missing_version_file_uses_fallback(self):
        with TemporaryDirectory() as temp_dir:
            self.assertEqual(read_app_version(Path(temp_dir)), "desconhecida")

    def test_empty_version_file_uses_fallback(self):
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "VERSION").write_text("\n", encoding="utf-8")
            self.assertEqual(read_app_version(root), "desconhecida")


if __name__ == "__main__":
    unittest.main()
