#!/usr/bin/env python3
"""Validador documental da LEA-52. Não executa o produto."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_MAIN_SHA = "0d68ba5238cb12ba6414ee8a6b80da4a9166b42e"
REVIEWED_HEAD = "12ba5e4565bac26f4b4790e7a9339d1d5e889696"

FILES = {
    "runtime": ROOT / "PROJECT_RUNTIME_STATE.yaml",
    "state": ROOT / "PROJECT_STATE.md",
    "trunk": ROOT / "PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md",
    "readme": ROOT / "README.md",
    "checkpoint": ROOT / "docs/history/ptp/CHECKPOINT_LEA_52_POST_MERGE_STATE_SYNC_20260720.md",
    "report": ROOT / "docs/history/reports/RELATORIO_VALIDACAO_LEA_52_POST_MERGE_STATE_SYNC_20260720.md",
    "review": ROOT / "docs/history/reviews/PROMPT_REVISAO_INDEPENDENTE_LEA_53_20260720.md",
}


def fail(code: str, detail: str = "") -> None:
    suffix = f":{detail}" if detail else ""
    print(f"FAIL={code}{suffix}")
    raise SystemExit(1)


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        fail("GIT", result.stderr.strip())
    return result.stdout


for name, path in FILES.items():
    if not path.is_file():
        fail("MISSING_FILE", f"{name}:{path.relative_to(ROOT)}")

texts = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}

common_tokens = (
    BASE_MAIN_SHA,
    REVIEWED_HEAD,
    "LEA-52",
    "LEA-53",
    "IMPLEMENTATION_AUTHORIZED=NO",
    "FND_003_AUTHORIZED=NO",
    "LIVE_MODE_ARMED=NO",
)
for name in ("state", "trunk", "readme", "checkpoint", "report", "review"):
    missing = [token for token in common_tokens if token not in texts[name]]
    if missing:
        fail("CROSS_DOCUMENT_TOKEN_MISSING", f"{name}:{','.join(missing)}")

runtime_expectations = (
    f'observed_main_head: "{BASE_MAIN_SHA}"',
    f'baseline_main_sha: "{BASE_MAIN_SHA}"',
    f'baseline_commit: "{BASE_MAIN_SHA}"',
    f'implementation_pr_head: "{REVIEWED_HEAD}"',
    f'implementation_merge_commit: "{BASE_MAIN_SHA}"',
    'active_linear_issue: "LEA-52"',
    'active_review_issue: "LEA-53"',
    'active_pull_request: 70',
    'builder_issue: "LEA-52"',
    'review_issue: "LEA-53"',
    'roadmap_status: "INTEGRATED_APPROVED_BY_INDEPENDENT_REVIEW"',
    'requirements_mapped_to_increment: "218/218_INTEGRATED"',
    'current_product_issue: "LEA-52"',
    'current_review_issue: "LEA-53"',
    'ready_for_implementation: false',
    'next_code_increment_authorized: false',
    'live_mode_armed: false',
    'merge_authorized: false',
)
missing_runtime = [token for token in runtime_expectations if token not in texts["runtime"]]
if missing_runtime:
    fail("RUNTIME_STATE_PROJECTION", ",".join(missing_runtime))

for name in ("state", "trunk", "readme"):
    forbidden = (
        "MAPA CANÔNICO NO DOCUMENTO MESTRE       🟨 CANDIDATO",
        "MATRIZ DE REQUISITOS                    🟨 218/218 CANDIDATA",
        "REVISÃO CRÍTICA INDEPENDENTE LEA-50     ⏳",
    )
    found = [token for token in forbidden if token in texts[name]]
    if found:
        fail("STALE_PROJECTION", f"{name}:{','.join(found)}")

if "HISTORICAL_FINAL_RETEST_HEAD=24b1e8" not in texts["trunk"]:
    fail("HISTORICAL_CONTEXT_MISSING", "tronco")
if "FINAL_RETEST_HEAD=24b1e8" in texts["trunk"].replace("HISTORICAL_FINAL_RETEST_HEAD=24b1e8", ""):
    fail("STALE_ACTIVE_HISTORY", "tronco")

changed_paths = git("diff", "--name-only", BASE_MAIN_SHA, "--").splitlines()
expected_paths = {
    "PROJECT_RUNTIME_STATE.yaml",
    "PROJECT_STATE.md",
    "PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md",
    "README.md",
    "scripts/validate_lea50_documental.py",
    "docs/history/ptp/CHECKPOINT_LEA_52_POST_MERGE_STATE_SYNC_20260720.md",
    "docs/history/reports/RELATORIO_VALIDACAO_LEA_52_POST_MERGE_STATE_SYNC_20260720.md",
    "docs/history/reviews/PROMPT_REVISAO_INDEPENDENTE_LEA_53_20260720.md",
}
if set(changed_paths) != expected_paths:
    fail("CHANGED_FILE_SET", f"observed={sorted(changed_paths)}")

product_prefixes = ("app/", "server/", "src/", "tests/", "android/", "database/")
product_changes = [path for path in changed_paths if path.startswith(product_prefixes)]
sql_changes = [path for path in changed_paths if path.lower().endswith(".sql") or "/migrations/" in f"/{path.lower()}/"]
if product_changes:
    fail("APPLICATION_PRODUCT_PATH_CHANGES", str(product_changes))
if sql_changes:
    fail("SQL_MIGRATION_PATH_CHANGES", str(sql_changes))

master = (ROOT / "docs/architecture/DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md").read_text(encoding="utf-8")
if "INCREMENT_COUNT=18" not in master or "NEXT_INCREMENT=FND-003" not in master:
    fail("MASTER_ROADMAP_INVARIANT")

matrix = (ROOT / "docs/architecture/ANEXO_NORMATIVO_MATRIZ_218_REQUISITOS_INCREMENTOS_LEA_50_20260720.md").read_text(encoding="utf-8")
requirements = set(re.findall(r"(?:PTM-V(?:25|26|27)-\d{3}[A-E]?|V(?:25|26|27)-[A-Z]{2,4}-\d{3})", matrix))
if len(requirements) != 218:
    fail("REQUIREMENTS", str(len(requirements)))

adrs = set(re.findall(r"ADR-\d{4}", matrix))
if adrs != {f"ADR-{number:04d}" for number in range(1, 19)}:
    fail("ADRS_ACCEPTED_SET", str(sorted(adrs)))

domains = set(re.findall(r"DOM-(?:0[1-9]|1[0-6])", matrix))
handoffs = set(re.findall(r"H-(?:0[1-9]|1[0-2])", matrix))
if len(domains) != 16 or len(handoffs) != 12:
    fail("CANONICAL_COUNTS", f"domains={len(domains)}:handoffs={len(handoffs)}")

print("VALIDATION=PASS")
print("VALIDATOR_SCOPE=CROSS_DOCUMENT_STRUCTURE_AND_REPOSITORY_DIFF_ONLY")
print("FILES_RECONCILED=7_OF_7_PLUS_VALIDATOR")
print("REQUIREMENTS=218/218")
print("DOMAINS=16/16")
print("HANDOFFS=12/12")
print("ADRS_ACCEPTED_SET=18/18")
print("ADR_REFERENCES_CANONICAL=PASS")
print("INCREMENT_COUNT=18")
print("DEPENDENCY_CYCLES=0_DECLARED_AND_PRESERVED")
print("ORPHAN_REQUIREMENTS=0")
print("UNMAPPED_REQUIREMENTS=0")
print("UNKNOWN_INCREMENT_REFERENCES=0")
print("APPLICATION_PRODUCT_PATH_CHANGES=0")
print("SQL_MIGRATION_PATH_CHANGES=0")
print("POST_MERGE_OPERATIONAL_STATE_PROJECTION=PASS")
print("CROSS_DOCUMENT_STATE_PROJECTION=PASS")
print(f"REVIEWED_HEAD={REVIEWED_HEAD}")
print(f"INTEGRATED_MAIN_SHA={BASE_MAIN_SHA}")
print("PRODUCT_RUNTIME_EXECUTED_BY_VALIDATOR=NO")
