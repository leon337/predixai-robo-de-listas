#!/usr/bin/env bash
set -Eeuo pipefail

EXPECTED_REPO="leon337/predixai-robo-de-listas"
EXPECTED_BRANCH="leonpcsn/lea-46-fnd-002-safe-runtime-read-model"
EXPECTED_HEAD="${FND002_EXPECTED_HEAD:-}"
REPORT_DIR="reports/local"
TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT_FILE="${REPORT_DIR}/FND_002_LOCAL_VALIDATION_${TIMESTAMP}.txt"
VENV_DIR=".venv-fnd002"

command -v git >/dev/null 2>&1 || { echo "git não encontrado" >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "python3 não encontrado" >&2; exit 1; }

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "Execute dentro do repositório local." >&2
  exit 1
}
cd "$REPO_ROOT"

# A árvore precisa ser validada antes de o próprio executor criar relatório ou venv.
if [[ -n "$(git status --porcelain)" ]]; then
  echo "RESULT=FAIL" >&2
  echo "ERROR=árvore de trabalho contém alterações locais; faça commit, stash ou descarte antes de validar" >&2
  git status --short >&2
  exit 1
fi

mkdir -p "$REPORT_DIR"
: > "$REPORT_FILE"

log() {
  printf '%s\n' "$*" | tee -a "$REPORT_FILE"
}

fail() {
  log "RESULT=FAIL"
  log "ERROR=$*"
  exit 1
}

log "MISSION=FND-002_SAFE_RUNTIME_READ_MODEL"
log "MODE=NULL_ONLY"
log "STARTED_AT_UTC=$TIMESTAMP"
log "REPOSITORY_ROOT=$REPO_ROOT"
log "EXPECTED_REPOSITORY=$EXPECTED_REPO"
log "EXPECTED_BRANCH=$EXPECTED_BRANCH"
log "EXPECTED_HEAD=$EXPECTED_HEAD"

[[ -n "$EXPECTED_HEAD" ]] || fail "defina FND002_EXPECTED_HEAD com o HEAD fornecido no handoff"
[[ "$EXPECTED_HEAD" =~ ^[0-9a-f]{40}$ ]] || fail "FND002_EXPECTED_HEAD deve ser um SHA Git completo de 40 caracteres"

REMOTE_URL="$(git remote get-url origin 2>/dev/null || true)"
log "ORIGIN_URL=$REMOTE_URL"
case "$REMOTE_URL" in
  *github.com/leon337/predixai-robo-de-listas* ) ;;
  * ) fail "origin não corresponde ao repositório oficial" ;;
esac

CURRENT_HEAD="$(git rev-parse HEAD)"
CURRENT_BRANCH="$(git branch --show-current)"
log "CURRENT_HEAD=$CURRENT_HEAD"
log "CURRENT_BRANCH=$CURRENT_BRANCH"

[[ "$CURRENT_HEAD" == "$EXPECTED_HEAD" ]] || fail "HEAD divergente; esperado $EXPECTED_HEAD"
[[ "$CURRENT_BRANCH" == "$EXPECTED_BRANCH" ]] || fail "branch divergente; esperada $EXPECTED_BRANCH"

PYTHON_VERSION="$(python3 --version 2>&1)"
log "PYTHON_VERSION=$PYTHON_VERSION"
python3 - <<'PY' || fail "Python 3.11 ou superior é necessário"
import sys
if sys.version_info < (3, 11):
    raise SystemExit(1)
PY

log "STEP=CREATE_VENV"
python3 -m venv "$VENV_DIR" || fail "não foi possível criar o ambiente virtual"
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

log "STEP=INSTALL_DEPENDENCIES"
python -m pip install --upgrade pip >>"$REPORT_FILE" 2>&1 || fail "falha ao atualizar pip"
python -m pip install -r requirements-dev.txt >>"$REPORT_FILE" 2>&1 || fail "falha ao instalar requirements-dev.txt"

log "STEP=PYTEST"
python -m pytest -q tests/server 2>&1 | tee -a "$REPORT_FILE"

log "STEP=RUFF"
ruff check server tests/server 2>&1 | tee -a "$REPORT_FILE"

log "STEP=MYPY"
mypy server --ignore-missing-imports 2>&1 | tee -a "$REPORT_FILE"

log "STEP=READ_ONLY_SMOKE_TEST"
python - <<'PY' 2>&1 | tee -a "$REPORT_FILE"
from fastapi.testclient import TestClient
from server.app import create_app
from server.config import ServerConfig

app = create_app(ServerConfig())
with TestClient(app) as client:
    service = app.state.service
    before = len(service.audit.snapshot())
    expected = {
        "/api/v1/runtime": 200,
        "/api/v1/audit/events": 200,
        "/api/v1/diagnostics": 200,
    }
    for path, status in expected.items():
        response = client.get(path)
        assert response.status_code == status, (path, response.status_code, response.text)
    after = len(service.audit.snapshot())
    assert after == before, (before, after)

    assert client.post("/api/v1/runtime").status_code == 405
    assert client.put("/api/v1/audit/events").status_code == 405
    assert client.delete("/api/v1/diagnostics").status_code == 405

print("READ_ONLY_ENDPOINTS=PASS")
print("AUDIT_COUNT_UNCHANGED=PASS")
print("MUTATION_METHODS_BLOCKED=PASS")
print("REAL_CLICK_EXECUTED=NO")
print("BROKER_CONNECTED=NO")
print("LIVE_MODE_ARMED=NO")
PY

FINISHED_AT="$(date -u +%Y%m%dT%H%M%SZ)"
log "FINISHED_AT_UTC=$FINISHED_AT"
log "RESULT=PASS"
log "REPORT_FILE=$REPORT_FILE"
printf '\nValidação concluída. Relatório: %s\n' "$REPORT_FILE"
