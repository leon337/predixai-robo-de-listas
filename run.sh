#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [[ ! -x .venv/bin/python ]]; then
  echo "Ambiente virtual ausente. Execute ./install.sh primeiro." >&2
  exit 1
fi

source .venv/bin/activate
exec python app/bootstrap_v250_alpha2_entry.py
