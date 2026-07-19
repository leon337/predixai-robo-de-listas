from pathlib import Path


BANNED_IMPORTS = (
    "pynput",
    "sqlite3",
    "sqlalchemy",
    "psycopg",
)

BANNED_RUNTIME_MARKERS = (
    "REAL_CLICK_AUTHORIZED=YES",
    "LIVE_MODE_ARMED=YES",
    "broker.connect",
)


def test_server_package_has_no_banned_imports_or_runtime_markers() -> None:
    root = Path("server")
    contents = "\n".join(
        path.read_text(encoding="utf-8")
        for path in root.rglob("*.py")
    ).lower()

    for banned in BANNED_IMPORTS:
        assert banned.lower() not in contents
    for banned in BANNED_RUNTIME_MARKERS:
        assert banned.lower() not in contents
