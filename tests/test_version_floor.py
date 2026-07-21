from __future__ import annotations

import pytest

from scripts.validate_version_floor import compare_versions, is_at_least, parse_version


def test_alpha_target_is_above_previous_stable_floor() -> None:
    assert is_at_least("2.5.0-alpha.2", "2.4.3")


def test_alpha_sequence_uses_semver_precedence() -> None:
    assert is_at_least("2.5.0-alpha.2", "2.5.0-alpha.1")


def test_prerelease_is_below_same_core_release() -> None:
    assert compare_versions("2.5.0-alpha.2", "2.5.0") < 0


def test_release_is_above_same_core_prerelease() -> None:
    assert compare_versions("2.5.0", "2.5.0-alpha.2") > 0


def test_invalid_version_is_rejected() -> None:
    with pytest.raises(ValueError):
        parse_version("2.5")
