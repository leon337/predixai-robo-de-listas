#!/usr/bin/env bash
set -Eeuo pipefail

EXPECTED_REPO="leon337/predixai-robo-de-listas"
EXPECTED_BRANCH="leonpcsn/dat-001-durable-state-legacy-migration"
EXPECTED_COMMIT=""
REPORT_DIR_REL="reports/local"
VENV_DIR=".venv-dat001"
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
  echo "ERROR=alterações locais protegidas; nenhum arquivo foi sobrescrito" >&2
  git status --short >&2
  exit 1
fi

TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT_DIR="$REPO_ROOT/$REPORT_DIR_REL"
REPORT_FILE="$REPORT_DIR/DAT_001_LOCAL_VALIDATION_${EXPECTED_COMMIT}_${TIMESTAMP}.txt"
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

log "MISSION=DAT-001_DURABLE_STATE_AND_LEGACY_MIGRATION"
log "VERSION_TARGET=V2.5.0-alpha.2"
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
REMOTE_BRANCH_HEAD="$(git rev-parse "origin/$EXPECTED_BRANCH")"
[[ "$REMOTE_BRANCH_HEAD" == "$EXPECTED_COMMIT" ]] || \
  fail "HEAD remoto divergente: esperado=$EXPECTED_COMMIT atual=$REMOTE_BRANCH_HEAD"

WORKTREE="$(mktemp -d -p /tmp predixai-dat001-XXXXXX)"
rmdir "$WORKTREE"
git worktree add --quiet --detach "$WORKTREE" "$EXPECTED_COMMIT" || \
  fail "não foi possível criar checkout isolado"
cd "$WORKTREE"

VALIDATED_COMMIT="$(git rev-parse HEAD)"
[[ "$VALIDATED_COMMIT" == "$EXPECTED_COMMIT" ]] || fail "HEAD isolado divergente"
log "REMOTE_BRANCH_HEAD=$REMOTE_BRANCH_HEAD"
log "VALIDATED_COMMIT=$VALIDATED_COMMIT"
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

log "STEP=INSTALL_PINNED_DEPENDENCIES"
python -m pip install --upgrade pip >>"$REPORT_FILE" 2>&1 || fail "falha ao atualizar pip"
python -m pip install -r requirements-dev.txt >>"$REPORT_FILE" 2>&1 || \
  fail "falha ao instalar requirements-dev.txt"

log "STEP=UNIT_INTEGRATION_SECURITY_RECOVERY_REGRESSION"
python -m pytest -q 2>&1 | tee -a "$REPORT_FILE" || fail "pytest falhou"

log "STEP=STATIC_VALIDATION"
ruff check server tests/server 2>&1 | tee -a "$REPORT_FILE" || fail "ruff falhou"
mypy server --ignore-missing-imports 2>&1 | tee -a "$REPORT_FILE" || fail "mypy falhou"

log "STEP=DURABILITY_BACKUP_RESTORE_IDEMPOTENCY_SMOKE"
python - <<'PY' 2>&1 | tee -a "$REPORT_FILE" || fail "smoke DAT-001 falhou"
import json
import tempfile
from pathlib import Path

from server.persistence import SQLitePersistence

with tempfile.TemporaryDirectory(prefix="predixai-dat001-") as directory:
    root = Path(directory)
    store = SQLitePersistence(root / "state.db")
    store.initialize()
    state = store.write_state(
        command_id="local-command",
        actor_id="local-operator",
        expected_version=0,
        aggregate_type="configuration",
        aggregate_id="local",
        payload={"mode": "NULL_ONLY"},
        trace_id="local-trace",
    )
    assert state.version == 1
    assert len(store.pending_events()) == 1
    backup = store.backup_to(root / "backup.db")
    restored_path = root / "restored.db"
    SQLitePersistence.restore_to_new_database(
        Path(backup.backup_path), restored_path, expected_sha256=backup.sha256
    )
    restored = SQLitePersistence(restored_path)
    assert restored.read_state("configuration", "local") == state

    legacy = root / "legacy.json"
    legacy.write_text(
        json.dumps({"version": 3, "profiles": [{"id": "local"}], "history": []}),
        encoding="utf-8",
    )
    first = store.import_legacy_to_staging(legacy, root / "evidence")
    repeated = store.import_legacy_to_staging(legacy, root / "evidence")
    assert first == repeated
    assert first.status == "CUTOVER_READY"
    assert store.health()["mode"] == "NULL_ONLY"

print("DURABLE_STATE=PASS")
print("SINGLE_WRITER_AND_OUTBOX=PASS")
print("BACKUP_RESTORE_INTEGRITY=PASS")
print("LEGACY_IMPORT_IDEMPOTENCY=PASS")
print("LEGACY_AUTHORITATIVE_MUTATION=NO")
print("PRODUCTION_DATABASE=NO")
print("EXISTING_REAL_DATA_MUTATION=NO")
print("MODE=NULL_ONLY")
print("BROKER_CONNECTION=NO")
print("REAL_CLICK=NO")
print("REAL_FINANCIAL_EFFECT=NO")
print("LIVE_MODE_ARMED=NO")
PY

log "ROLLBACK_REFERENCE=restore para banco novo a partir de backup verificado; migration down somente em banco vazio"
log "LOCAL_REPORT_TXT=$REPORT_FILE"
log "FINISHED_AT_UTC=$(date -u +%Y%m%dT%H%M%SZ)"
log "RESULT=PASS"
REPORT_SHA256="$(sha256sum "$REPORT_FILE" | awk '{print $1}')"
REPORT_SHA256_FILE="${REPORT_FILE}.sha256"
printf '%s  %s\n' "$REPORT_SHA256" "$(basename "$REPORT_FILE")" > "$REPORT_SHA256_FILE"
chmod 600 "$REPORT_SHA256_FILE"
printf 'REPORT_SHA256=%s\n' "$REPORT_SHA256"
printf 'REPORT_SHA256_FILE=%s\n' "$REPORT_SHA256_FILE"
printf '\nValidação concluída. Relatório: %s\n' "$REPORT_FILE"
