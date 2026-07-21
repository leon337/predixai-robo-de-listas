from __future__ import annotations

import ast
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "2.5.0-alpha.2"
ENTRYPOINT = "app/bootstrap_v250_alpha2_entry.py"


def test_version_file_is_promoted() -> None:
    assert (ROOT_DIR / "VERSION").read_text(encoding="utf-8").strip() == EXPECTED_VERSION


def test_run_script_uses_promoted_entrypoint() -> None:
    launcher = (ROOT_DIR / "run.sh").read_text(encoding="utf-8")
    assert ENTRYPOINT in launcher
    assert "app/bootstrap_v23_entry.py" not in launcher


def test_promoted_entrypoint_is_valid_and_delegates_to_stable_runtime() -> None:
    source = (ROOT_DIR / ENTRYPOINT).read_text(encoding="utf-8")
    ast.parse(source)
    assert "from bootstrap_v23_entry import run" in source
    assert "raise SystemExit(run())" in source
