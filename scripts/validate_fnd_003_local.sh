#!/usr/bin/env bash
set -Eeuo pipefail

EXPECTED_REPO="leon337/predixai-robo-de-listas"
EXPECTED_BRANCH="leonpcsn/fnd-003-identity-configuration-client-trust"
EXPECTED_COMMIT=""
REPORT_DIR_REL="reports/local"
VENV_DIR=".venv-fnd003"
WORKTREE=""

usage() {
  printf 'Uso: %s --expected-commit <SHA-40>\n' "$0"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --expected-commit)
      [[ $# -ge 2 ]] || { usage >&2; exit 2; }
      EXPECTED_COMMIT="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
done

[[ "$EXPECTED_COMMIT" =~ ^[0-9a-f]{40}$ ]] || {
  echo "ERROR=--expected-commit exige SHA Git completo" >&2
  exit 2
}

command -v git >/dev/null 2>&1 || { echo "git não encontrado" >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "python3 não encontrado" >&2; exit 1; }

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "Execute dentro do repositório local." >&2
  exit 1
}
cd "$REPO_ROOT"

if [[ -n "$(git status --porcelain)" ]]; then
  echo "RESULT=FAIL" >&2
  echo "ERROR=alterações locais protegidas; a validação não modificou o checkout" >&2
  git status --short >&2
  exit 1
fi

TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT_DIR="$REPO_ROOT/$REPORT_DIR_REL"
REPORT_FILE="$REPORT_DIR/FND_003_LOCAL_VALIDATION_${TIMESTAMP}.txt"
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

cleanup() {
  if [[ -n "$WORKTREE" && -d "$WORKTREE" ]]; then
    git -C "$REPO_ROOT" worktree remove --force "$WORKTREE" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

log "MISSION=FND-003_IDENTITY_CONFIGURATION_CLIENT_TRUST"
log "MODE=NULL_ONLY"
log "STARTED_AT_UTC=$TIMESTAMP"
log "EXPECTED_REPOSITORY=$EXPECTED_REPO"
log "EXPECTED_BRANCH=$EXPECTED_BRANCH"
log "EXPECTED_COMMIT=$EXPECTED_COMMIT"

REMOTE_URL="$(git remote get-url origin 2>/dev/null || true)"
log "ORIGIN_URL=$REMOTE_URL"
case "$REMOTE_URL" in
  *github.com/leon337/predixai-robo-de-listas* ) ;;
  * ) fail "origin não corresponde ao repositório oficial" ;;
esac

log "STEP=FETCH_CANDIDATE"
git fetch --quiet origin \
  "refs/heads/$EXPECTED_BRANCH:refs/remotes/origin/$EXPECTED_BRANCH" || \
  fail "não foi possível atualizar a branch candidata"
git cat-file -e "${EXPECTED_COMMIT}^{commit}" || fail "commit candidato inexistente"
git merge-base --is-ancestor "$EXPECTED_COMMIT" "origin/$EXPECTED_BRANCH" || \
  fail "commit candidato não pertence à branch autorizada"

WORKTREE="$(mktemp -d -p /tmp predixai-fnd003-XXXXXX)"
rmdir "$WORKTREE"
git worktree add --quiet --detach "$WORKTREE" "$EXPECTED_COMMIT" || \
  fail "não foi possível criar checkout isolado"
cd "$WORKTREE"

[[ "$(git rev-parse HEAD)" == "$EXPECTED_COMMIT" ]] || fail "HEAD isolado divergente"
[[ -z "$(git status --porcelain)" ]] || fail "checkout isolado não está limpo"

python3 - <<'PY' || fail "Python 3.11 ou superior é necessário"
import sys
if sys.version_info < (3, 11):
    raise SystemExit(1)
PY

log "STEP=CREATE_ISOLATED_ENVIRONMENT"
python3 -m venv "$VENV_DIR" || fail "não foi possível criar o ambiente virtual"
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

log "STEP=INSTALL_DEPENDENCIES"
python -m pip install --upgrade pip >>"$REPORT_FILE" 2>&1 || fail "falha ao atualizar pip"
python -m pip install -r requirements-dev.txt >>"$REPORT_FILE" 2>&1 || \
  fail "falha ao instalar requirements-dev.txt"

log "STEP=UNIT_INTEGRATION_REGRESSION_CUMULATIVE_TESTS"
python -m pytest -q 2>&1 | tee -a "$REPORT_FILE" || fail "pytest falhou"

log "STEP=STATIC_VALIDATION"
ruff check server tests 2>&1 | tee -a "$REPORT_FILE" || fail "ruff falhou"
mypy server --ignore-missing-imports 2>&1 | tee -a "$REPORT_FILE" || fail "mypy falhou"

log "STEP=NULL_ONLY_IDENTITY_SMOKE"
python - <<'PY' 2>&1 | tee -a "$REPORT_FILE" || fail "smoke FND-003 falhou"
from fastapi.testclient import TestClient
from pydantic import SecretStr

from server.app import create_app
from server.config import ServerConfig

app = create_app(ServerConfig(admin_secret=SecretStr("ephemeral-local-validation")))
admin = {"X-PredixAI-Admin-Secret": "ephemeral-local-validation"}
with TestClient(app) as client:
    challenge = client.post(
        "/api/v1/identity/pairing/challenges",
        headers=admin,
        json={"device_id": "local-device", "operator_id": "local-operator"},
    )
    assert challenge.status_code == 200
    paired = client.post(
        "/api/v1/identity/pair",
        json={
            "challenge": challenge.json()["challenge"],
        },
    )
    assert paired.status_code == 200
    token = paired.json()["access_token"]
    bearer = {"Authorization": f"Bearer {token}"}
    capabilities = client.get("/api/v1/identity/capabilities", headers=bearer).json()
    assert capabilities["mode"] == "NULL"
    assert capabilities["role"] == "READ_ONLY"
    assert capabilities["command_grant"] is False
    assert capabilities["external_effects"] is False
    assert capabilities["broker_connection"] is False
    assert capabilities["real_click"] is False
    assert capabilities["live_mode"] is False
    assert client.post("/api/v1/identity/presence", headers=bearer).json()[
        "authorization_grant"
    ] is False
    assert client.post(
        "/api/v1/identity/devices/local-device/revoke", headers=admin
    ).status_code == 200
    assert client.get("/api/v1/identity/capabilities", headers=bearer).status_code == 401

print("IDENTITY_PAIRING=PASS")
print("SESSION_REVOCATION=PASS")
print("PRESENCE_WITHOUT_GRANT=PASS")
print("MODE=NULL_ONLY")
print("BROKER_CONNECTION=NO")
print("REAL_CLICK=NO")
print("REAL_FINANCIAL_EFFECT=NO")
print("LIVE_MODE_ARMED=NO")
PY

log "ROLLBACK_REFERENCE=remove isolated worktree; original checkout remained unchanged"
log "LOCAL_REPORT_TXT=$REPORT_FILE"
log "FINISHED_AT_UTC=$(date -u +%Y%m%dT%H%M%SZ)"
log "RESULT=PASS"
printf '\nValidação concluída. Relatório: %s\n' "$REPORT_FILE"
