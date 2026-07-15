from pathlib import Path


def test_main_exists() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "app" / "main.py").is_file()


def test_requirements_declares_pynput() -> None:
    root = Path(__file__).resolve().parents[1]
    content = (root / "requirements.txt").read_text(encoding="utf-8")
    assert "pynput" in content
