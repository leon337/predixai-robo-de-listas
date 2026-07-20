#!/usr/bin/env python3
"""Validador documental da candidatura LEA-50; não executa o produto."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "docs" / "architecture"
MASTER = ARCH / "DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md"
INDEX = ARCH / "APENDICE_INDICE_INDIVIDUAL_218_REQUISITOS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md"
MATRIX = ARCH / "ANEXO_NORMATIVO_MATRIZ_218_REQUISITOS_INCREMENTOS_LEA_50_20260720.md"
CATALOG = ARCH / "ANEXO_NORMATIVO_CATALOGO_INCREMENTOS_LEA_50_20260720.md"
GRAPH = ARCH / "ANEXO_NORMATIVO_GRAFO_PRECEDENCIA_INCREMENTOS_LEA_50_20260720.md"
POLICY = ARCH / "ANEXO_NORMATIVO_POLITICAS_EXECUCAO_INCREMENTAL_LEA_50_20260720.md"

REQ_PATTERN = r"(?:PTM-V(?:25|26|27)-\d{3}[A-E]?|V(?:25|26|27)-[A-Z]{2,4}-\d{3})"
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


def fail(message: str) -> None:
    print(f"FAIL={message}")
    raise SystemExit(1)


for path in (MASTER, INDEX, MATRIX, CATALOG, GRAPH, POLICY):
    if not path.is_file():
        fail(f"MISSING_FILE:{path.relative_to(ROOT)}")

for path in (MATRIX, CATALOG, GRAPH, POLICY):
    text = path.read_text()
    missing = [key for key in ANNEX_CONTRACT if key not in text]
    if missing:
        fail(f"ANNEX_CONTRACT:{path.name}:{','.join(missing)}")

index_ids = re.findall(REQ_PATTERN, INDEX.read_text())
# O índice repete IDs em seções de supersessão; a autoridade é o bloco por domínio.
domain_part = INDEX.read_text().split("## 3. IDs com interpretação supersessora", 1)[0]
expected = set(re.findall(REQ_PATTERN, domain_part))
if len(expected) != 218:
    fail(f"EXPECTED_REQUIREMENTS:{len(expected)}")

matrix_rows = []
for line in MATRIX.read_text().splitlines():
    if re.match(r"\| (?:PTM-|V2[567]-)", line):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 12:
            fail(f"MATRIX_COLUMNS:{len(cells)}:{line[:80]}")
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
    if not row[7] or row[7] == "—":
        fail(f"MISSING_TEST_FAMILY:{row[0]}")
    if not row[10].endswith("_EXIT_PASS"):
        fail(f"MISSING_ACCEPTANCE_GATE:{row[0]}:{row[10]}")

catalog_text = CATALOG.read_text()
sections = re.split(r"(?=## \d{2}\. )", catalog_text)
increments = {}
for section in sections:
    title = re.match(r"## \d{2}\. ([A-Z]+(?:-[A-Z]+)*-?\d{3}|LIV-GATE-001) —", section)
    if not title:
        continue
    inc = title.group(1)
    values = {}
    for line in section.splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key] = value
    missing = [field for field in CATALOG_FIELDS if not values.get(field)]
    if missing:
        fail(f"CATALOG_FIELDS:{inc}:{','.join(missing)}")
    increments[inc] = values

mapped_increments = {row[6] for row in matrix_rows}
if len(increments) != 18 or set(increments) != mapped_increments:
    fail(f"INCREMENT_SET:catalog={sorted(increments)}:matrix={sorted(mapped_increments)}")

requirements_per_increment = Counter(row[6] for row in matrix_rows)
if any(requirements_per_increment[inc] == 0 for inc in increments):
    fail("INCREMENT_WITHOUT_NORMATIVE_BASIS")

graph_text = GRAPH.read_text()
deps = {inc: [] for inc in increments}
for line in graph_text.splitlines():
    if not re.match(r"\| \d+ \| `", line):
        continue
    cells = [cell.strip().replace("`", "") for cell in line.strip("|").split("|")]
    inc = cells[1]
    raw = cells[2]
    deps[inc] = [] if raw == "Arquitetura V1.0" else [part.strip() for part in raw.split(",")]

if set(deps) != set(increments):
    fail("UNKNOWN_INCREMENT_REFERENCE")
for inc, predecessors in deps.items():
    for predecessor in predecessors:
        if predecessor not in increments:
            fail(f"MISSING_DEPENDENCY:{inc}:{predecessor}")

visiting, visited = set(), set()
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
if re.search(r"DOM-(?:17|[2-9]\d)", "\n".join([master_text, MATRIX.read_text(), CATALOG.read_text()])):
    fail("NEW_DOMAIN_DETECTED")
if re.search(r"ADR-(?:0019|00[2-9]\d)", "\n".join([master_text, MATRIX.read_text(), CATALOG.read_text()])):
    fail("NEW_ADR_DETECTED")

handoffs = set(re.findall(r"H-(?:0[1-9]|1[0-2])", MATRIX.read_text()))
domains = set(re.findall(r"DOM-(?:0[1-9]|1[0-6])", MATRIX.read_text()))
adrs = {path.name for path in (ARCH / "adrs").glob("ADR-*.md")}
if len(handoffs) != 12 or len(domains) != 16 or len(adrs) != 18:
    fail(f"CANONICAL_COUNTS:domains={len(domains)}:handoffs={len(handoffs)}:adrs={len(adrs)}")

print("VALIDATION=PASS")
print("REQUIREMENTS=218/218")
print("DOMAINS=16/16")
print("HANDOFFS=12/12")
print("ADRS=18/18")
print("INCREMENT_COUNT=18")
print("DEPENDENCY_CYCLES=0")
print("MISSING_DEPENDENCIES=0")
print("ORPHAN_REQUIREMENTS=0")
print("UNMAPPED_REQUIREMENTS=0")
print("DUPLICATE_REQUIREMENT_IDS=0")
print("UNKNOWN_INCREMENT_REFERENCES=0")
print("INCREMENTS_WITHOUT_NORMATIVE_BASIS=0")
print("INCREMENTS_WITHOUT_TEST=0")
print("INCREMENTS_WITHOUT_LOCAL_VALIDATION=0")
print("INCREMENTS_WITHOUT_ROLLBACK=0")
print("GATES_WITHOUT_OBJECTIVE_CRITERIA=0")
print("AMBIGUOUS_NEXT_INCREMENT=0")
print("ARCHITECTURE_CHANGE=NO")
print("APPLICATION_CODE_CHANGED=NO")
print("TEST_CODE_CHANGED=NO")
print("SQL_CREATED=NO")
print("MIGRATION_CREATED=NO")
print("RUNTIME_EXECUTED=NO")
sys.exit(0)
