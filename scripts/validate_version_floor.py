#!/usr/bin/env python3
"""Valida uma versão SemVer estrita contra o piso histórico informado."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import TypeAlias

Identifier: TypeAlias = int | str
ParsedVersion: TypeAlias = tuple[tuple[int, int, int], tuple[Identifier, ...] | None]

_PRERELEASE_IDENTIFIER = (
    r"(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
)
_BUILD_IDENTIFIER = r"[0-9A-Za-z-]+"
_SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    rf"(?:-({_PRERELEASE_IDENTIFIER}(?:\.{_PRERELEASE_IDENTIFIER})*))?"
    rf"(?:\+{_BUILD_IDENTIFIER}(?:\.{_BUILD_IDENTIFIER})*)?$"
)


def parse_version(value: str) -> ParsedVersion:
    """Converte uma versão SemVer estrita em uma estrutura comparável."""
    match = _SEMVER.fullmatch(value.strip())
    if match is None:
        raise ValueError(f"versão SemVer inválida: {value!r}")

    core = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )
    prerelease_text = match.group(4)
    if prerelease_text is None:
        return core, None

    identifiers: list[Identifier] = []
    for part in prerelease_text.split("."):
        identifiers.append(int(part) if part.isdigit() else part)
    return core, tuple(identifiers)


def _compare_prerelease(
    left: tuple[Identifier, ...] | None,
    right: tuple[Identifier, ...] | None,
) -> int:
    if left is None and right is None:
        return 0
    if left is None:
        return 1
    if right is None:
        return -1

    for left_part, right_part in zip(left, right):
        if left_part == right_part:
            continue
        if isinstance(left_part, int) and isinstance(right_part, str):
            return -1
        if isinstance(left_part, str) and isinstance(right_part, int):
            return 1
        if isinstance(left_part, int) and isinstance(right_part, int):
            return 1 if left_part > right_part else -1
        if isinstance(left_part, str) and isinstance(right_part, str):
            return 1 if left_part > right_part else -1
        raise TypeError("identificador SemVer inesperado")

    if len(left) == len(right):
        return 0
    return 1 if len(left) > len(right) else -1


def compare_versions(left: str, right: str) -> int:
    """Retorna -1, 0 ou 1 conforme a precedência SemVer."""
    left_core, left_pre = parse_version(left)
    right_core, right_pre = parse_version(right)
    if left_core != right_core:
        return 1 if left_core > right_core else -1
    return _compare_prerelease(left_pre, right_pre)


def is_at_least(current: str, minimum: str) -> bool:
    return compare_versions(current, minimum) >= 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--minimum", required=True)
    parser.add_argument("--version-file", default="VERSION")
    args = parser.parse_args()

    current = Path(args.version_file).read_text(encoding="utf-8").strip()
    if not is_at_least(current, args.minimum):
        raise SystemExit(
            f"VERSION_FLOOR=FAIL current={current} minimum={args.minimum}"
        )
    print(f"VERSION_FLOOR=PASS current={current} minimum={args.minimum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
