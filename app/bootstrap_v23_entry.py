#!/usr/bin/env python3
"""Entrada final da V2.3.3."""
from __future__ import annotations

import main as app_main
import bootstrap_v22_entry
import bootstrap_v23
import bootstrap_v231
import bootstrap_v232
import bootstrap_v233


def install() -> None:
    bootstrap_v22_entry.install()
    bootstrap_v23.install_patch()
    bootstrap_v231.install_patch()
    bootstrap_v232.install_patch()
    bootstrap_v233.install_patch()


if __name__ == "__main__":
    install()
    app_main.main()
