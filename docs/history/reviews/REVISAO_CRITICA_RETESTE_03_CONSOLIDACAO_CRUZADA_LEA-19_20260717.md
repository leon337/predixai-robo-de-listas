# REVISÃO CRÍTICA — RETESTE 03 DA CONSOLIDAÇÃO CRUZADA

## LEA-19 / PR #40

## 1. Controle

```text
REVIEW_TYPE=INDEPENDENT_CRITICAL_RETEST_03
BUILDER_ISSUE=LEA-18
REVIEW_ISSUE=LEA-19
PULL_REQUEST=40
REVIEWED_PR_HEAD=daa23a5e6dc2ede3e48ae3bc867c6bcb73b91065
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
```

## 2. Resultado

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=FAIL
RETEST_SEQUENCE=03
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=1
SOURCE_INVENTORY_COMPLETENESS=PASS
AUTHORITY_BY_DOMAIN_CONSISTENCY=FAIL
DOMAIN_BOUNDARY_CONSISTENCY=FAIL
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS
TRACEABILITY_COMPLETENESS=FAIL
DUPLICATE_AND_ORPHAN_REQUIREMENT_CHECK=PASS
CONFLICT_SUPERSESSION_RESOLUTION=PASS
CONTROLLED_AUTOMATION_SECURITY=PASS
REAL_FINANCIAL_EFFECT_SEPARATION=PASS
RESTART_FAIL_CLOSED=PASS
DOCUMENTATION_RUNTIME_SEPARATION=PASS
GITHUB_LINEAR_ALIGNMENT=PASS
DOCUMENTAL_READY_FOR_MERGE=NO
ADRS_READY_TO_START=NO
RETEST_REQUIRED=YES
```

## 3. Remediações verificadas

```text
MAJOR_06_PTM_V27_031_PRIMARY_DOMAIN=PASS
PTM_V27_031_PRIMARY_DOMAIN=DOM-16
PTM_V27_032_PRIMARY_DOMAIN=DOM-01
PTM_V27_003_INDEX_PRIMARY_DOMAIN=PASS_DOM-14
LIVE_SOURCES_RETEST_03_STAGE=PASS
SCHEMA_1_0_3_COMPATIBILITY=PASS
CI_WORKFLOWS=9_OF_9_SUCCESS
OPEN_PREVIOUS_REVIEW_THREADS=0
```

A correção de `MAJOR-06` foi aplicada ao índice individual e às fontes vivas. O total continua `218`, sem duplicados ou órfãos.

## 4. Achados maiores

### MAJOR-07 — matriz consolidada não propaga PTM-V27-003 para DOM-14

A matriz consolidada ainda agrupa `PTM-V27-002` a `PTM-V27-007` exclusivamente em `DOM-13`.

O índice individual, o documento consolidado e a matriz canônica V2.7 reconhecem que `PTM-V27-003` governa ausência, capacidade e fronteira do adaptador real, cuja autoridade primária pertence ao `DOM-14`.

Correção obrigatória:

```text
PTM_V27_003_PRIMARY_DOMAIN=DOM-14
PTM_V27_002_004_005_006_007_PRIMARY_DOMAIN=DOM-13
STRUCTURAL_MATRIX_DOMAIN_LINKAGE=RECONCILED
```

A linha agrupada deve ser dividida para não preservar a classificação anterior nem declarar rastreabilidade completa com ligação contraditória.

### MAJOR-08 — domínio primário funcional incorreto em V27-EXE e V27-SAF

O índice individual coloca todos os oito `V27-EXE-*` em `DOM-14` e todos os oito `V27-SAF-*` em `DOM-13`.

Os critérios canônicos possuem autoridades diferentes:

```text
V27-EXE-001=DOM-15
V27-EXE-002=DOM-15
V27-EXE-003=DOM-14
V27-EXE-004=DOM-14
V27-EXE-005=DOM-15
V27-EXE-006=DOM-15
V27-EXE-007=DOM-15
V27-EXE-008=DOM-16

V27-SAF-001=DOM-13
V27-SAF-002=DOM-15
V27-SAF-003=DOM-15
V27-SAF-004=DOM-16
V27-SAF-005=DOM-16
V27-SAF-006=DOM-14
V27-SAF-007=DOM-16
V27-SAF-008=DOM-13
```

Requisitos de tentativa, dispatch, timeout, retry, circuito, fila e serialização pertencem ao `DOM-15`; capability e payload do adaptador pertencem ao `DOM-14`; kill switch, prova negativa, segredos e redaction pertencem ao `DOM-16`; arming, política e ampliação de limites permanecem no `DOM-13`.

Contagens derivadas esperadas após essas correções:

```text
DOM_13_PRIMARY_IDS=26
DOM_14_PRIMARY_IDS=7
DOM_15_PRIMARY_IDS=27
DOM_16_PRIMARY_IDS=38
TOTAL_IDS=218
UNIQUE_IDS=218
DUPLICATE_IDS=0
ORPHAN_IDS=0
```

A matriz consolidada também deve dividir os grupos funcionais e incluir `DOM-16` no grupo EXE e `DOM-15` no grupo SAF. Antes do Reteste 04, executar auditoria integral dos `52/52` IDs funcionais V2.7, não apenas dos grupos já apontados.

## 5. Achado menor

### MINOR-04 — reconciliação textual 29/30

O documento consolidado afirma que dois requisitos foram reclassificados e que os “outros 29” permaneceram inalterados. Como o conjunto estrutural possui 32 IDs, o valor correto é `30`.

```text
V2_7_STRUCTURAL_IDS_EXPECTED=32
V2_7_STRUCTURAL_IDS_RECLASSIFIED=2
V2_7_STRUCTURAL_IDS_CONFIRMED_WITHOUT_CHANGE=30
```

A inconsistência não altera o índice nem as contagens, mas deve ser corrigida antes do próximo reteste.

## 6. Gates preservados

- escopo exclusivamente documental;
- código, testes, workflows, SQL e migrations não alterados;
- 16 domínios e 12 handoffs preservados;
- conjuntos V2.5 `56/56`, V2.6 `78/78` e V2.7 `84/84` preservados;
- total `218`, sem duplicados ou órfãos;
- precedência normativa correta;
- separação análise, sinal, comando, autorização, alvo, dispatch, recibo e reconciliação preservada;
- efeito financeiro real permanece não autorizado;
- restart, timeout e `UNKNOWN_EFFECT` continuam fail-closed.

## 7. Decisão

O Reteste 03 não aprova o Boss Gate. O PR deve retornar a Draft até a correção de `MAJOR-07`, `MAJOR-08` e `MINOR-04`, sincronização das fontes vivas e execução do Reteste 04 independente.

```text
MERGE_AUTHORIZED=NO
ADRS_START_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
RETEST_04_REQUIRED=YES
```
