#!/usr/bin/env python3
"""Entrada explícita da aplicação para V2.5.0-alpha.2.

A promoção preserva integralmente o runtime V2.4.3 já validado e altera somente a
identidade pública da versão após a integração da DAT-001.
"""
from __future__ import annotations

from bootstrap_v23_entry import run


if __name__ == "__main__":
    raise SystemExit(run())
