import ast
from pathlib import Path


BANNED_IMPORTS = (
    "pynput",
    "sqlalchemy",
    "psycopg",
)

AUTHORIZED_SQLITE_MODULE = Path("server/persistence/store.py")

BANNED_RUNTIME_MARKERS = (
    "REAL_CLICK_AUTHORIZED=YES",
    "LIVE_MODE_ARMED=YES",
    "broker.connect",
)


def test_server_package_has_no_banned_imports_or_runtime_markers() -> None:
    root = Path("server")
    python_files = tuple(root.rglob("*.py"))
    contents = "\n".join(path.read_text(encoding="utf-8") for path in python_files).lower()

    for path in python_files:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        imports: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
        for banned in BANNED_IMPORTS:
            assert banned not in imports
        if path != AUTHORIZED_SQLITE_MODULE:
            assert "sqlite3" not in imports
    for banned in BANNED_RUNTIME_MARKERS:
        assert banned.lower() not in contents
