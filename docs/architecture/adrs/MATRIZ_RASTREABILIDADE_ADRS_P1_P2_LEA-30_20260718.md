# MATRIZ DE RASTREABILIDADE — ADRs P1/P2

## LEA-30 — Remediação pós-LEA-31

## 1. Controle

```text
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
BASE_MAIN_SHA=dff0c0f0c26e820756804af92dd7b3641121d51b
REVIEWED_PR_HEAD=8ca08eaee367140a67ede7082e315b2844beab06
TRANSITION_ID=LEA-30-T01
ADR_COUNT=6
P1_COUNT=5
P2_COUNT=1
DOCUMENTATION_ONLY=YES
REMEDIATION_OF=LEA-31_MAJOR_01
```

## 2. Mapeamento candidato → ADR

| ADR | Candidato | Prioridade | Decisão | Domínios primários | Handoffs |
|---|---|---|---|---|---|
| ADR-0013 | ADR-CAND-003 | P1 | migrations, compatibilidade e importação do legado | DOM-03 | H-11 |
| ADR-0014 | ADR-CAND-007 | P1 | retenção de frames e evidências visuais | DOM-08 | H-03, H-04, H-05 |
| ADR-0015 | ADR-CAND-013 | P1 | serialização, dedupe e circuit breaker | DOM-15 | H-10, H-11, H-12 |
| ADR-0016 | ADR-CAND-016 | P1 | relógios, deadlines e identidade de processo | DOM-13, DOM-15 | H-09, H-10, H-12 |
| ADR-0017 | ADR-CAND-017 | P2 | thresholds e limites numéricos | DOM-09, DOM-11, DOM-12 | H-05, H-06, H-07, H-08, H-12 |
| ADR-0018 | ADR-CAND-018 | P1 | testes e evidência por camada | DOM-16 | H-04, H-05, H-07, H-09, H-10, H-11, H-12 |

```text
CANDIDATE_MAPPING=6/6
DUPLICATE_CANDIDATE_IDS=0
DUPLICATE_ADR_IDS=0
P1_CANDIDATES=5/5
P2_CANDIDATES=1/1
```

## 3. Reconciliação dos requisitos diferidos P1/P2

A fonte canônica é o apêndice individual 218/218 dos ADRs P0. Somente linhas marcadas como `F=DEFERRED_WITH_REASON` são contabilizadas nesta seção.

| ADR | Candidato | Requisitos diferidos canônicos | Quantidade |
|---|---|---|---:|
| ADR-0013 | ADR-CAND-003 | nenhum; decisão complementar a requisitos já decididos pelo ADR-0002 | 0 |
| ADR-0014 | ADR-CAND-007 | `PTM-V26-002..008`, `V26-OBS-001..004`, `V26-CAP-001..004`, `V26-VAL-001..006`, `V26-MAP-001..005` | 26 |
| ADR-0015 | ADR-CAND-013 | `V27-SAF-002..003` | 2 |
| ADR-0016 | ADR-CAND-016 | `V27-SAF-008` | 1 |
| ADR-0017 | ADR-CAND-017 | `V27-SAF-001` | 1 |
| ADR-0018 | ADR-CAND-018 | `V25-QA-002` | 1 |

```text
P1_P2_DEFERRED_REQUIREMENT_ROWS=31
P1_P2_DEFERRED_UNIQUE_IDS=31
P1_P2_DEFERRED_DUPLICATE_IDS=0
P1_P2_DEFERRED_UNMAPPED_IDS=0
P1_P2_DEFERRED_MISASSIGNED_IDS=0
INDIVIDUAL_TRACEABILITY=PASS_BUILDER_REMEDIATED
TRACEABILITY_APPENDIX=docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_ADRS_P1_P2_LEA-30_20260718.md
```

## 4. Requisitos complementares

Os grupos abaixo reforçam requisitos já decididos pelos ADRs P0. Eles não alteram a contagem canônica de 218 requisitos e não são apresentados como novos diferimentos.

| ADR | Requisitos complementares |
|---|---|
| ADR-0013 | `PTM-V25-001..006`, `PTM-V25-014A..014E`, `PTM-V25-016`, `V25-DB-001..005`, `V25-LEG-001..006`, `PTM-V26-023`, `PTM-V26-027`, `PTM-V27-029` |
| ADR-0014 | `PTM-V26-024..026`, `V26-RPL-001..003`, `V26-SEC-001..003` |
| ADR-0015 | `PTM-V27-010..019`, `PTM-V27-022..025`, `PTM-V27-030..031`, `V27-EXE-001..002`, `V27-EXE-005..008`, `V27-REC-001..006`, `V27-QA-002..007` |
| ADR-0016 | `PTM-V27-004..007`, `PTM-V27-010..018`, `PTM-V27-030..031`, `V27-PRE-001..006`, `V27-CMD-001..006`, `V27-AUT-001..006`, `V27-EXE-005..007`, `V27-QA-003..007` |
| ADR-0017 | `PTM-V26-005..006`, `PTM-V26-009..022`, `V26-VAL-003..006`, `V26-ANA-001..011`, `V26-STR-001..004`, `V26-SIG-001..008`, `V27-QA-001..007` |
| ADR-0018 | `V25-QA-001`, `V25-SEC-001`, `PTM-V26-024..028`, `V26-RPL-001..003`, `V26-API-001..002`, `V26-SEC-001..003`, `PTM-V27-010..019`, `PTM-V27-026..032`, `V27-EXE-001..008`, `V27-SAF-001..008`, `V27-REC-001..006`, `V27-OBS-001..005`, `V27-QA-001..007` |

```text
NEW_REQUIREMENT_IDS=0
CANONICAL_REQUIREMENT_TOTAL_PRESERVED=218
P0_DECISION_AUTHORITY_PRESERVED=YES
```

## 5. Dependências

```text
ADR-0013=ADR-0002
ADR-0014=ADR-0005|ADR-0012
ADR-0015=ADR-0008|ADR-0009|ADR-0010|ADR-0011
ADR-0016=ADR-0008|ADR-0010|ADR-0011
ADR-0017=ADR-0005|ADR-0006|ADR-0007|ADR-0012
ADR-0018=ADR-0003|ADR-0008|ADR-0009|ADR-0010|ADR-0011|ADR-0012|ADR-0013|ADR-0014|ADR-0015|ADR-0016|ADR-0017
```

```text
P1_P2_DEPENDS_ON_NODE_COUNT=6
P1_P2_DEPENDS_ON_CYCLE_COUNT=0
P1_P2_DEPENDS_ON_DAG=PASS_BUILDER
```

## 6. Cobertura de riscos

| Risco | ADR controlador |
|---|---|
| perda ou duplicação na importação | ADR-0013 |
| exposição de imagem sensível | ADR-0014 |
| dispatch concorrente ou retry ambíguo | ADR-0015 |
| validade ampliada por relógio ou restart | ADR-0016 |
| confiança artificial por valor arbitrário | ADR-0017 |
| declaração de PASS sem execução ou evidência | ADR-0018 |

## 7. Resultado do builder remediado

```text
P1_P2_ADR_COUNT=6/6
CANDIDATE_MAPPING=PASS_BUILDER
DOMAIN_LINKAGE=PASS_BUILDER
HANDOFF_LINKAGE=PASS_BUILDER
DEFERRED_REQUIREMENT_LINKAGE=PASS_BUILDER_REMEDIATED
COMPLEMENTARY_REQUIREMENT_LINKAGE=PASS_BUILDER_REMEDIATED
DEPENDENCY_DAG=PASS_BUILDER
NEW_REQUIREMENT_IDS=0
CANONICAL_REQUIREMENT_TOTAL_PRESERVED=218
LEA_31_MAJOR_01=REMEDIATED_BUILDER
INDEPENDENT_RETEST=REQUIRED
```

## 8. Limite

Esta matriz prova rastreabilidade documental e separa requisitos diferidos de vínculos complementares. Não prova implementação, execução de migration, captura, benchmark, teste runtime ou efeito financeiro.