# MATRIZ DE RASTREABILIDADE DO DOCUMENTO MESTRE

## LEA-34 — Arquitetura V1.0

## 1. Controle

```text
MISSION=LEA-34
BASE_MAIN_SHA=65b18341c06a391ea48ae5029102ad7a095c3340
SOURCE_MATRIX=docs/architecture/MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
DOCUMENT_MASTER=docs/architecture/DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md
V2_5_REQUIREMENTS=56
V2_6_REQUIREMENTS=78
V2_7_REQUIREMENTS=84
TOTAL_REQUIREMENTS=218
NEW_REQUIREMENT_IDS=0
TEST_RUNTIME_EXECUTED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

## 2. Contrato de rastreabilidade

```text
REQUIREMENT_ID_OR_RANGE
→ PTM_SOURCE
→ PRIMARY_DOMAIN
→ HANDOFFS
→ ADR_IDS
→ DOCUMENT_MASTER_SECTION
→ FUTURE_TEST_FAMILY
```

Faixas e curingas representam todos os IDs individuais abrangidos pela matriz consolidada. `DM-*`, `DOM-*`, `H-*` e `T-*` são referências arquiteturais e de teste futuro; não são novos requisitos PTM.

## 3. PTM V2.5 — 56/56

### 3.1 Estruturais — 29/29

| IDs | Qtde. | Domínio | Handoff | ADRs | Seção DM | Teste futuro |
|---|---:|---|---|---|---|---|
| `PTM-V25-001..006` | 6 | DOM-02, DOM-03 | — | ADR-0001, 0002, 0003 | DM-06, DM-07, DM-18 | `T-CFG-*`, `T-DB-*` |
| `PTM-V25-007` | 1 | DOM-04 | H-01 | ADR-0001, 0002 | DM-08 | `T-LIST-*`, `T-E2E-*` |
| `PTM-V25-008..009` | 2 | DOM-05 | — | ADR-0004 | DM-09 | `T-CFG-*`, `T-E2E-*` |
| `PTM-V25-010`, `011A..011D` | 5 | DOM-06 | H-02 | ADR-0005 | DM-10, DM-15 | `T-CFG-*`, `T-ADP-*` |
| `PTM-V25-012..013` | 2 | DOM-02, DOM-14 | — | ADR-0001, 0003, 0009 | DM-06, DM-15, DM-18 | `T-CFG-*`, `T-ADP-*` |
| `PTM-V25-014A..014E` | 5 | DOM-03 | — | ADR-0002, 0013 | DM-07, DM-19 | `T-DB-*`, `T-REC-*` |
| `PTM-V25-015A..015E` | 5 | DOM-16 | H-11 | ADR-0012 | DM-17 | `T-SEC-*` |
| `PTM-V25-016` | 1 | DOM-02, DOM-03 | — | ADR-0002 | DM-06, DM-07 | `T-CFG-*`, `T-DB-*` |
| `PTM-V25-017` | 1 | DOM-02, DOM-05, DOM-16 | — | ADR-0004, 0012 | DM-06, DM-09, DM-17 | `T-CFG-*`, `T-SEC-*` |
| `PTM-V25-018` | 1 | DOM-01, DOM-02, DOM-05 | — | ADR-0001, 0010 | DM-05, DM-06, DM-09 | `T-GOV-*`, `T-CFG-*` |

### 3.2 Funcionais — 23/23

| IDs | Qtde. | Domínio | Handoff | ADRs | Seção DM | Teste futuro |
|---|---:|---|---|---|---|---|
| `V25-SRV-001..004` | 4 | DOM-01, DOM-02, DOM-03, DOM-05 | — | ADR-0001, 0003, 0004 | DM-05..DM-09, DM-18 | `T-GOV-*`, `T-E2E-*` |
| `V25-CFG-001..004` | 4 | DOM-02 | — | ADR-0012 | DM-06, DM-17 | `T-CFG-*`, `T-SEC-*` |
| `V25-DB-001..005` | 5 | DOM-03 | H-11 | ADR-0002, 0003, 0013 | DM-07, DM-18, DM-19 | `T-DB-*`, `T-REC-*` |
| `V25-LIST-001..004` | 4 | DOM-04 | H-01 | ADR-0001, 0002 | DM-08 | `T-LIST-*`, `T-E2E-*` |
| `V25-LEG-001..006` | 6 | DOM-03 | — | ADR-0002, 0013 | DM-07, DM-19 | `T-DB-*`, `T-REC-*` |

### 3.3 Adicionais aceitos — 4/4

| ID | Domínio | ADRs | Seção DM | Teste futuro |
|---|---|---|---|---|
| `V25-SEC-001` | DOM-16 | ADR-0009, 0010, 0012 | DM-15, DM-17 | `T-SEC-*` |
| `V25-QA-001` | DOM-16 | ADR-0018 | DM-20 | `T-SEC-*`, `T-E2E-*` |
| `V25-QA-002` | DOM-04, DOM-14, DOM-16 | ADR-0009, 0018 | DM-08, DM-15, DM-20 | `T-E2E-*` |
| `V25-DOC-001` | DOM-01 | ADR-0018 | DM-05, DM-23 | `T-GOV-*` |

```text
V2_5_TRACEABILITY=56/56
```

## 4. PTM V2.6 — 78/78

### 4.1 Estruturais — 28/28

| IDs | Qtde. | Domínio | Handoff | ADRs | Seção DM | Teste futuro |
|---|---:|---|---|---|---|---|
| `PTM-V26-001` | 1 | DOM-11, DOM-13 | H-08 | ADR-0008, 0009 | DM-13, DM-14 | `T-ANA-*`, `T-CMD-*` |
| `PTM-V26-002..003` | 2 | DOM-07 | H-02, H-03 | ADR-0005, 0014 | DM-10, DM-11 | `T-OBS-*` |
| `PTM-V26-004` | 1 | DOM-08 | H-04 | ADR-0014 | DM-11 | `T-CAP-*` |
| `PTM-V26-005..006` | 2 | DOM-09 | H-05 | ADR-0014, 0017 | DM-12 | `T-VAL-*` |
| `PTM-V26-007..008` | 2 | DOM-10 | H-06 | ADR-0017 | DM-12 | `T-MAP-*` |
| `PTM-V26-009..018` | 10 | DOM-11 | H-07 | ADR-0006, 0017 | DM-13 | `T-ANA-*` |
| `PTM-V26-019..022` | 4 | DOM-12 | H-08 | ADR-0007 | DM-13 | `T-SIG-*` |
| `PTM-V26-023`, `027` | 2 | DOM-03 | — | ADR-0002, 0003 | DM-07, DM-18 | `T-DB-*` |
| `PTM-V26-024..026`, `028` | 4 | DOM-16 | H-11 | ADR-0012, 0014, 0018 | DM-17, DM-20 | `T-SEC-*`, `T-E2E-*` |

### 4.2 Funcionais — 50/50

| IDs | Qtde. | Domínio | Handoff | ADRs | Seção DM | Teste futuro |
|---|---:|---|---|---|---|---|
| `V26-OBS-001..004` | 4 | DOM-07 | H-02, H-03 | ADR-0005, 0014 | DM-10, DM-11 | `T-OBS-*` |
| `V26-CAP-001..004` | 4 | DOM-08 | H-04 | ADR-0014 | DM-11 | `T-CAP-*` |
| `V26-VAL-001..006` | 6 | DOM-09 | H-05 | ADR-0014, 0017 | DM-12 | `T-VAL-*` |
| `V26-MAP-001..005` | 5 | DOM-10 | H-06 | ADR-0017 | DM-12 | `T-MAP-*` |
| `V26-ANA-001..011` | 11 | DOM-11 | H-07 | ADR-0006, 0017 | DM-13 | `T-ANA-*` |
| `V26-STR-001..004` | 4 | DOM-12 | H-08 | ADR-0007 | DM-13 | `T-SIG-*` |
| `V26-SIG-001..008` | 8 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | `T-SIG-*`, `T-CMD-*` |
| `V26-RPL-001..003` | 3 | DOM-16 | — | ADR-0012, 0014, 0018 | DM-17, DM-20 | `T-E2E-*`, `T-SEC-*` |
| `V26-API-001..002` | 2 | DOM-03, DOM-16 | — | ADR-0003, 0012 | DM-07, DM-17, DM-18 | `T-DB-*`, `T-SEC-*` |
| `V26-SEC-001..003` | 3 | DOM-16 | H-11 | ADR-0009, 0010, 0012 | DM-15, DM-17 | `T-SEC-*` |

```text
V2_6_TRACEABILITY=78/78
```

## 5. PTM V2.7 — 84/84

### 5.1 Estruturais — 32/32

| IDs | Qtde. | Domínio | Handoff | ADRs | Seção DM | Teste futuro |
|---|---:|---|---|---|---|---|
| `PTM-V27-001` | 1 | DOM-13, DOM-15 | H-08..H-10 | ADR-0008, 0011 | DM-14, DM-16 | `T-CMD-*`, `T-EXE-*` |
| `PTM-V27-002` | 1 | DOM-13 | H-08, H-09 | ADR-0008, 0009 | DM-14, DM-15 | `T-CMD-*` |
| `PTM-V27-003` | 1 | DOM-14 | H-09, H-10 | ADR-0009 | DM-15 | `T-ADP-*` |
| `PTM-V27-004..007` | 4 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | `T-CMD-*` |
| `PTM-V27-008..009` | 2 | DOM-14 | H-09, H-10 | ADR-0005, 0009 | DM-10, DM-15 | `T-ADP-*` |
| `PTM-V27-010..018` | 9 | DOM-15 | H-10 | ADR-0011, 0015, 0016 | DM-16 | `T-EXE-*`, `T-REC-*` |
| `PTM-V27-019` | 1 | DOM-16 | H-12 | ADR-0010 | DM-17 | `T-SEC-*` |
| `PTM-V27-020` | 1 | DOM-05, DOM-13 | H-09 | ADR-0004, 0008 | DM-09, DM-14 | `T-CMD-*` |
| `PTM-V27-021` | 1 | DOM-14, DOM-15 | H-10 | ADR-0009 | DM-15, DM-16 | `T-ADP-*`, `T-EXE-*` |
| `PTM-V27-022..025` | 4 | DOM-15 | H-10, H-11 | ADR-0011 | DM-16 | `T-REC-*` |
| `PTM-V27-026..028` | 3 | DOM-16 | H-11 | ADR-0012 | DM-17 | `T-SEC-*` |
| `PTM-V27-029` | 1 | DOM-03, DOM-15 | — | ADR-0002, 0013 | DM-07, DM-16, DM-19 | `T-DB-*`, `T-REC-*` |
| `PTM-V27-030` | 1 | DOM-15 | H-11 | ADR-0016 | DM-16 | `T-REC-*` |
| `PTM-V27-031` | 1 | DOM-16 | H-12 | ADR-0010, 0012, 0018 | DM-17, DM-20 | `T-SEC-*` |
| `PTM-V27-032` | 1 | DOM-01 | H-12 | ADR-0009, 0010 | DM-05, DM-14, DM-17, DM-22 | `T-GOV-*`, `T-SEC-*` |

### 5.2 Funcionais — 52/52

| IDs | Qtde. | Domínio | Handoff | ADRs | Seção DM | Teste futuro |
|---|---:|---|---|---|---|---|
| `V27-PRE-001..006` | 6 | DOM-13 | H-09 | ADR-0008, 0016 | DM-14, DM-18 | `T-CMD-*` |
| `V27-CMD-001..006` | 6 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | `T-CMD-*` |
| `V27-AUT-001..006` | 6 | DOM-13 | H-09 | ADR-0004, 0008, 0009 | DM-09, DM-14, DM-15 | `T-CMD-*` |
| `V27-EXE-001`, `002`, `005..007` | 5 | DOM-15 | H-10 | ADR-0011, 0015, 0016 | DM-16 | `T-EXE-*`, `T-REC-*` |
| `V27-EXE-003..004` | 2 | DOM-14 | H-10 | ADR-0009 | DM-15 | `T-ADP-*` |
| `V27-EXE-008` | 1 | DOM-16 | H-12 | ADR-0010 | DM-17 | `T-SEC-*` |
| `V27-SAF-001`, `008` | 2 | DOM-13 | H-09, H-12 | ADR-0008, 0009, 0010 | DM-14, DM-17 | `T-CMD-*`, `T-SEC-*` |
| `V27-SAF-002..003` | 2 | DOM-15 | H-10, H-12 | ADR-0015 | DM-16, DM-17 | `T-EXE-*`, `T-SEC-*` |
| `V27-SAF-006` | 1 | DOM-14 | H-10 | ADR-0005, 0009 | DM-10, DM-15 | `T-ADP-*` |
| `V27-SAF-004`, `005`, `007` | 3 | DOM-16 | H-10, H-12 | ADR-0009, 0010, 0012 | DM-15, DM-17 | `T-SEC-*` |
| `V27-REC-001..006` | 6 | DOM-15 | H-11 | ADR-0011, 0016 | DM-16 | `T-REC-*` |
| `V27-OBS-001..005` | 5 | DOM-16 | H-11 | ADR-0012 | DM-17 | `T-SEC-*` |
| `V27-QA-001..007` | 7 | DOM-16 | H-12 | ADR-0010, 0018 | DM-17, DM-20 | `T-SEC-*`, `T-E2E-*` |

```text
V2_7_TRACEABILITY=84/84
```

## 6. Cobertura dos handoffs — 12/12

| Handoff | Seções DM | Famílias de teste futuras |
|---|---|---|
| H-01 DOM-04 → DOM-07 | DM-08 → DM-11 | `T-LIST-*`, `T-OBS-*`, `T-E2E-*` |
| H-02 DOM-06 → DOM-07 | DM-10 → DM-11 | `T-CFG-*`, `T-OBS-*` |
| H-03 DOM-07 → DOM-08 | DM-11 | `T-OBS-*`, `T-CAP-*` |
| H-04 DOM-08 → DOM-09 | DM-11 → DM-12 | `T-CAP-*`, `T-VAL-*` |
| H-05 DOM-09 → DOM-10 | DM-12 | `T-VAL-*`, `T-MAP-*` |
| H-06 DOM-10 → DOM-11 | DM-12 → DM-13 | `T-MAP-*`, `T-ANA-*` |
| H-07 DOM-11 → DOM-12 | DM-13 | `T-ANA-*`, `T-SIG-*` |
| H-08 DOM-12 → DOM-13 | DM-13 → DM-14 | `T-SIG-*`, `T-CMD-*` |
| H-09 DOM-13 → DOM-14 | DM-14 → DM-15 | `T-CMD-*`, `T-ADP-*` |
| H-10 DOM-14 → DOM-15 | DM-15 → DM-16 | `T-ADP-*`, `T-EXE-*` |
| H-11 DOM-15 → DOM-16 | DM-16 → DM-17 | `T-REC-*`, `T-SEC-*` |
| H-12 DOM-16 → DOM-13/15 | DM-17 → DM-14/DM-16 | `T-SEC-*`, `T-E2E-*` |

## 7. Cobertura dos ADRs — 18/18

```text
ADR-0001=DM-04|DM-05
ADR-0002=DM-07
ADR-0003=DM-18
ADR-0004=DM-09
ADR-0005=DM-10|DM-15
ADR-0006=DM-13
ADR-0007=DM-13
ADR-0008=DM-14|DM-16|DM-18
ADR-0009=DM-15
ADR-0010=DM-17
ADR-0011=DM-16
ADR-0012=DM-17
ADR-0013=DM-19
ADR-0014=DM-11|DM-17
ADR-0015=DM-16|DM-17
ADR-0016=DM-16|DM-18
ADR-0017=DM-12|DM-13
ADR-0018=DM-20
```

## 8. Resultado do builder

```text
V2_5_TRACEABILITY=56/56
V2_6_TRACEABILITY=78/78
V2_7_TRACEABILITY=84/84
TOTAL_TRACEABILITY=218/218
DUPLICATE_REQUIREMENT_IDS=0_INHERITED_FROM_CANONICAL_MATRIX
ORPHAN_REQUIREMENT_IDS=0_INHERITED_FROM_CANONICAL_MATRIX
CANONICAL_DOMAINS_COVERED=16/16
MANDATORY_HANDOFFS_COVERED=12/12
ADRS_REFERENCED=18/18
FUTURE_TEST_FAMILIES_DEFINED=16
TEST_SPEC_CREATED=PASS_ARCHITECTURAL_FAMILIES
TEST_RUNTIME_EXECUTED=NO
IMPLEMENTATION_EVIDENCE=NOT_CREATED
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
```

A validação final dessas contagens pertence à revisão crítica independente da missão do Documento Mestre.