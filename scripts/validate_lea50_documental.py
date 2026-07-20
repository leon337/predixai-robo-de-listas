#!/usr/bin/env python3
"""Validador documental reproduzível da LEA-50; não executa o produto."""

from __future__ import annotations

import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "docs" / "architecture"
BASE_SHA = "0968ae86e92e7b640cbcc77941d49a9474839650"
MASTER_REL = "docs/architecture/DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md"
MASTER = ROOT / MASTER_REL
INDEX = ARCH / "APENDICE_INDICE_INDIVIDUAL_218_REQUISITOS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md"
MATRIX = ARCH / "ANEXO_NORMATIVO_MATRIZ_218_REQUISITOS_INCREMENTOS_LEA_50_20260720.md"
CATALOG = ARCH / "ANEXO_NORMATIVO_CATALOGO_INCREMENTOS_LEA_50_20260720.md"
GRAPH = ARCH / "ANEXO_NORMATIVO_GRAFO_PRECEDENCIA_INCREMENTOS_LEA_50_20260720.md"
POLICY = ARCH / "ANEXO_NORMATIVO_POLITICAS_EXECUCAO_INCREMENTAL_LEA_50_20260720.md"
RUNTIME_STATE = ROOT / "PROJECT_RUNTIME_STATE.yaml"
LAST_RETEST_HEAD = "8aebab96d7ca98b183e5973384df2cba28eabd83"

REQ_PATTERN = r"(?:PTM-V(?:25|26|27)-\d{3}[A-E]?|V(?:25|26|27)-[A-Z]{2,4}-\d{3})"
ADR_PATTERN = re.compile(r"ADR-\d{4}")
ANNEX_CONTRACT = (
    "DOCUMENT_TYPE=NORMATIVE_ANNEX",
    "PARENT_AUTHORITY=DOCUMENTO_MESTRE",
    "CAN_OVERRIDE_MASTER=NO",
    "REQUIRED_FOR_MASTER_VALIDITY=YES",
)
CATALOG_FIELDS = (
    "ID", "NOME", "OBJETIVO", "RESULTADO_TESTÁVEL", "ESCOPO", "FORA_DE_ESCOPO", "DEPENDE_DE",
    "DOMÍNIOS", "HANDOFFS", "REQUISITOS", "ADRS", "MODO_MÁXIMO", "SITUAÇÃO_ATUAL",
    "CRITÉRIOS_DE_ENTRADA", "ENTREGAS", "TESTES_UNITÁRIOS", "TESTES_DE_INTEGRAÇÃO",
    "TESTES_DE_REGRESSÃO", "TESTE_CUMULATIVO", "TESTE_LOCAL_DO_LEO", "COMANDO_ÚNICO_LOCAL",
    "EVIDÊNCIAS", "ROLLBACK", "RISCOS", "GATE_DE_SAÍDA", "VERSÃO_PREVISTA", "PRÓXIMO_INCREMENTO",
)
GATE_TOKENS = (
    "UNIT=PASS", "INTEGRATION=PASS", "REGRESSION=PASS", "CUMULATIVE=PASS",
    "SECURITY_NEGATIVE=PASS", "CI=PASS", "INDEPENDENT_REVIEW=PASS",
    "LOCAL_LINUX_MINT=PASS", "LOCAL_REPORT=PROVIDED", "TECHNICAL_DEBT=PASS",
)
ROLLBACK_CLAUSES = (
    "reverter PR do incremento", "restaurar tag/commit predecessor", "executar regressão cumulativa",
)
PROTECTED_ARCH_PATHS = (
    "docs/architecture/adrs",
    "docs/architecture/MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md",
    "docs/architecture/APENDICE_DOMINIOS_HANDOFFS_DOCUMENTO_MESTRE_LEA-34_20260718.md",
    "docs/architecture/APENDICE_INDICE_INDIVIDUAL_218_REQUISITOS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md",
    "docs/architecture/MATRIZ_RASTREABILIDADE_DOCUMENTO_MESTRE_LEA-34_20260718.md",
)


def fail(message: str) -> None:
    print(f"FAIL={message}")
    raise SystemExit(1)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode:
        fail(f"GIT:{' '.join(args)}:{result.stderr.strip()}")
    return result.stdout


def canonical_adr_list(value: str, context: str, accepted: set[str]) -> list[str]:
    refs = [item.strip() for item in value.split(",") if item.strip()]
    if not refs:
        fail(f"ADR_EMPTY:{context}")
    if len(refs) != len(set(refs)):
        fail(f"ADR_DUPLICATE:{context}:{value}")
    for ref in refs:
        if not ADR_PATTERN.fullmatch(ref):
            fail(f"ADR_FORMAT:{context}:{ref}")
        if ref not in accepted:
            fail(f"ADR_UNKNOWN:{context}:{ref}")
    return refs


for path in (MASTER, INDEX, MATRIX, CATALOG, GRAPH, POLICY, RUNTIME_STATE):
    if not path.is_file():
        fail(f"MISSING_FILE:{path.relative_to(ROOT)}")

for path in (MATRIX, CATALOG, GRAPH, POLICY):
    text = path.read_text()
    missing = [key for key in ANNEX_CONTRACT if key not in text]
    if missing:
        fail(f"ANNEX_CONTRACT:{path.name}:{','.join(missing)}")

accepted_adrs = {
    match.group(0)
    for path in (ARCH / "adrs").glob("ADR-[0-9][0-9][0-9][0-9]-*.md")
    if (match := ADR_PATTERN.match(path.name))
}
if accepted_adrs != {f"ADR-{number:04d}" for number in range(1, 19)}:
    fail(f"ACCEPTED_ADR_SET:{sorted(accepted_adrs)}")

index_text = INDEX.read_text()
domain_part = index_text.split("## 3. IDs com interpretação supersessora", 1)[0]
expected = set(re.findall(REQ_PATTERN, domain_part))
if len(expected) != 218:
    fail(f"EXPECTED_REQUIREMENTS:{len(expected)}")

matrix_rows: list[list[str]] = []
matrix_adr_refs: set[str] = set()
for line in MATRIX.read_text().splitlines():
    if re.match(r"\| (?:PTM-|V2[567]-)", line):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 12:
            fail(f"MATRIX_COLUMNS:{len(cells)}:{line[:80]}")
        matrix_adr_refs.update(canonical_adr_list(cells[4], f"MATRIX:{cells[0]}", accepted_adrs))
        matrix_rows.append(cells)

ids = [row[0] for row in matrix_rows]
if len(ids) != 218 or len(set(ids)) != 218:
    fail(f"MATRIX_CARDINALITY:rows={len(ids)}:unique={len(set(ids))}")
if set(ids) != expected:
    fail(f"MATRIX_SET:missing={sorted(expected-set(ids))}:unknown={sorted(set(ids)-expected)}")
sources = Counter(row[1] for row in matrix_rows)
if sources != Counter({"PTM_V2.5": 56, "PTM_V2.6": 78, "PTM_V2.7": 84}):
    fail(f"SOURCE_COUNTS:{dict(sources)}")
for row in matrix_rows:
    if any(not value for value in row):
        fail(f"EMPTY_MATRIX_FIELD:{row[0]}")
    if row[7] == "—":
        fail(f"MISSING_TEST_FAMILY:{row[0]}")
    if not row[10].endswith("_EXIT_PASS"):
        fail(f"MISSING_ACCEPTANCE_GATE:{row[0]}:{row[10]}")

catalog_text = CATALOG.read_text()
sections = re.split(r"(?=## \d{2}\. )", catalog_text)
increments: dict[str, dict[str, str]] = {}
catalog_adr_refs: set[str] = set()
for section in sections:
    title = re.match(r"## \d{2}\. ([A-Z]+(?:-[A-Z]+)*-?\d{3}|LIV-GATE-001) —", section)
    if not title:
        continue
    inc = title.group(1)
    values: dict[str, str] = {}
    for line in section.splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key] = value
    missing = [field for field in CATALOG_FIELDS if not values.get(field)]
    if missing:
        fail(f"CATALOG_FIELDS:{inc}:{','.join(missing)}")
    if values["ID"] != inc:
        fail(f"CATALOG_ID:{inc}:{values['ID']}")
    catalog_adr_refs.update(canonical_adr_list(values["ADRS"], f"CATALOG:{inc}", accepted_adrs))
    increments[inc] = values

mapped_increments = {row[6] for row in matrix_rows}
if len(increments) != 18 or set(increments) != mapped_increments:
    fail(f"INCREMENT_SET:catalog={sorted(increments)}:matrix={sorted(mapped_increments)}")
if matrix_adr_refs | catalog_adr_refs != accepted_adrs:
    fail("ADR_COVERAGE_NOT_18_OF_18")
requirements_per_increment = Counter(row[6] for row in matrix_rows)
if any(requirements_per_increment[inc] == 0 for inc in increments):
    fail("INCREMENT_WITHOUT_NORMATIVE_BASIS")

# Verifica as especificações; não simula scripts futuros nem executa o produto.
local_commands = {inc: values["COMANDO_ÚNICO_LOCAL"] for inc, values in increments.items()}
materialized: list[str] = []
for inc, command in local_commands.items():
    match = re.fullmatch(r"bash (scripts/[a-z0-9_]+\.sh) --expected-commit <CANDIDATE_HEAD>", command)
    if not match:
        fail(f"LOCAL_COMMAND_FORMAT:{inc}:{command}")
    script = ROOT / match.group(1)
    if script.is_file():
        syntax = subprocess.run(["bash", "-n", str(script)], cwd=ROOT, capture_output=True, text=True)
        if syntax.returncode:
            fail(f"LOCAL_SCRIPT_SYNTAX:{inc}:{syntax.stderr.strip()}")
        materialized.append(inc)
if materialized != ["FND-002"]:
    fail(f"LOCAL_SCRIPT_MATERIALIZATION_UNEXPECTED:{materialized}")

for inc, values in increments.items():
    rollback = values["ROLLBACK"]
    missing = [clause for clause in ROLLBACK_CLAUSES if clause not in rollback]
    if missing:
        fail(f"ROLLBACK_SPEC:{inc}:{','.join(missing)}")
    gate = values["GATE_DE_SAÍDA"]
    if not gate.startswith(f"{inc}_EXIT_PASS:"):
        fail(f"GATE_ID:{inc}:{gate}")
    missing_tokens = [token for token in GATE_TOKENS if token not in gate.split(":", 1)[1].split(";")]
    if missing_tokens:
        fail(f"GATE_OBJECTIVE_TOKENS:{inc}:{','.join(missing_tokens)}")

graph_text = GRAPH.read_text()
deps = {inc: [] for inc in increments}
for line in graph_text.splitlines():
    if not re.match(r"\| \d+ \| `", line):
        continue
    cells = [cell.strip().replace("`", "") for cell in line.strip("|").split("|")]
    inc, raw = cells[1], cells[2]
    if inc not in deps:
        fail(f"UNKNOWN_INCREMENT_REFERENCE:{inc}")
    deps[inc] = [] if raw == "Arquitetura V1.0" else [part.strip() for part in raw.split(",")]
for inc, predecessors in deps.items():
    for predecessor in predecessors:
        if predecessor not in increments:
            fail(f"MISSING_DEPENDENCY:{inc}:{predecessor}")
visiting: set[str] = set()
visited: set[str] = set()


def visit(node: str) -> None:
    if node in visiting:
        fail(f"DEPENDENCY_CYCLE:{node}")
    if node in visited:
        return
    visiting.add(node)
    for predecessor in deps[node]:
        visit(predecessor)
    visiting.remove(node)
    visited.add(node)


for item in deps:
    visit(item)

master_text = MASTER.read_text()
for number in range(24, 34):
    if f"## DM-{number}" not in master_text:
        fail(f"MASTER_SECTION_DM_{number}")
if "ROADMAP_AUTHORITY=DOCUMENTO_MESTRE" not in master_text:
    fail("MASTER_AUTHORITY")
if "NEXT_INCREMENT=FND-003" not in master_text:
    fail("AMBIGUOUS_NEXT_INCREMENT")

# Prova mecânica limitada: DM-01..DM-23 e fontes arquiteturais protegidas não mudaram.
baseline_master = git("show", f"{BASE_SHA}:{MASTER_REL}")
current_frozen_prefix = master_text.split("## DM-24", 1)[0]
if current_frozen_prefix.rstrip() != baseline_master.rstrip():
    fail("FROZEN_MASTER_PREFIX_DIFF")
protected_diff = git("diff", "--name-only", BASE_SHA, "--", *PROTECTED_ARCH_PATHS).splitlines()
if protected_diff:
    fail(f"PROTECTED_ARCHITECTURE_DIFF:{protected_diff}")

handoffs = set(re.findall(r"H-(?:0[1-9]|1[0-2])", MATRIX.read_text()))
domains = set(re.findall(r"DOM-(?:0[1-9]|1[0-6])", MATRIX.read_text()))
if len(handoffs) != 12 or len(domains) != 16:
    fail(f"CANONICAL_COUNTS:domains={len(domains)}:handoffs={len(handoffs)}")

changed_paths = git("diff", "--name-only", BASE_SHA, "--").splitlines()
product_prefixes = ("app/", "server/", "src/", "tests/", "android/", "database/")
product_changes = [path for path in changed_paths if path.startswith(product_prefixes)]
sql_migration_changes = [
    path for path in changed_paths
    if path.lower().endswith(".sql") or "/migrations/" in f"/{path.lower()}/"
]
if product_changes:
    fail(f"APPLICATION_PRODUCT_PATH_CHANGES:{product_changes}")
if sql_migration_changes:
    fail(f"SQL_MIGRATION_PATH_CHANGES:{sql_migration_changes}")

# F01: valida a projeção do último HEAD efetivamente retestado e o estado vivo do Linear.
runtime_text = RUNTIME_STATE.read_text()
runtime_expectations = (
    f'observed_pr_head: "{LAST_RETEST_HEAD}"',
    f'implementation_pr_head: "{LAST_RETEST_HEAD}"',
    f'last_independent_retest_head: "{LAST_RETEST_HEAD}"',
    'task_status_and_dependencies: "Linear LEA-50 In Progress; LEA-51 In Progress awaiting final independent retest"',
    'ready_for_independent_retest: true',
    'current_product_issue: "LEA-50"',
    'current_review_issue: "LEA-51"',
)
missing_state = [item for item in runtime_expectations if item not in runtime_text]
if missing_state:
    fail(f"F01_OPERATIONAL_STATE:{missing_state}")

print("VALIDATION=PASS")
print("VALIDATOR_SCOPE=DOCUMENT_STRUCTURE_AND_REPOSITORY_DIFF_ONLY")
print("REQUIREMENTS=218/218")
print("DOMAINS=16/16")
print("HANDOFFS=12/12")
print("ADRS_ACCEPTED_SET=18/18")
print("ADR_REFERENCES_CANONICAL=PASS")
print("ADR_REFERENCE_DUPLICATES=0")
print("INCREMENT_COUNT=18")
print("DEPENDENCY_CYCLES=0")
print("MISSING_DEPENDENCIES=0")
print("ORPHAN_REQUIREMENTS=0")
print("UNMAPPED_REQUIREMENTS=0")
print("DUPLICATE_REQUIREMENT_IDS=0")
print("UNKNOWN_INCREMENT_REFERENCES=0")
print("INCREMENTS_WITHOUT_NORMATIVE_BASIS=0")
print("INCREMENTS_WITHOUT_TEST_SPEC=0")
print("LOCAL_VALIDATION_SPECS=18/18")
print(f"LOCAL_VALIDATORS_MATERIALIZED={len(materialized)}/18")
print(f"LOCAL_VALIDATORS_PENDING_FUTURE_INCREMENT_MISSIONS={18-len(materialized)}")
print("LOCAL_VALIDATION_RUNTIME_EXECUTED=NO")
print("ROLLBACK_SPECS_STRUCTURED=18/18")
print("ROLLBACK_EXECUTION_PROOF=NOT_EXECUTED_DOCUMENTATION_ONLY")
print("OBJECTIVE_GATE_SPECS=18/18")
print("GATE_RESULTS_PROVEN_BY_THIS_RUN=0/18")
print("AMBIGUOUS_NEXT_INCREMENT=0")
print("FROZEN_MASTER_PREFIX_DIFF=0")
print("PROTECTED_ARCHITECTURE_ARTIFACT_DIFF=0")
print("ARCHITECTURE_DECISION_BASELINE_INFERENCE=UNCHANGED_WITHIN_MECHANICALLY_CHECKED_SCOPE")
print("APPLICATION_PRODUCT_PATH_CHANGES=0")
print("SQL_MIGRATION_PATH_CHANGES=0")
print("PRODUCT_RUNTIME_EXECUTED_BY_VALIDATOR=NO")
print("F01_OPERATIONAL_STATE_PROJECTION=PASS")
print(f"LAST_INDEPENDENT_RETEST_HEAD={LAST_RETEST_HEAD}")
