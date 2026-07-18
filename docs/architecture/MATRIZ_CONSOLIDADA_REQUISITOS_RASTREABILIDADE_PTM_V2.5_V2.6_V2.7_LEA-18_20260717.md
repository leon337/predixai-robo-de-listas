# MATRIZ CONSOLIDADA DE REQUISITOS E RASTREABILIDADE

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_CONSOLIDATED_TRACEABILITY_REMEDIATED_FOR_RETEST_04
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
NEW_REQUIREMENT_IDS=0
IMPLEMENTATION_AUTHORIZED=NO
V2_7_STRUCTURAL_IDS_AUDITED=32/32
V2_7_FUNCTIONAL_IDS_AUDITED=52/52
```

Os identificadores `DOM-*` e `H-*` referenciam o mapa unificado da LEA-18. Eles não são requisitos adicionais.

## 2. Fontes canônicas

| Código | Fonte |
|---|---|
| V25 | `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md` |
| V25-M | `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md` |
| V25-RC | revisão final do PR `#33`, Linear `LEA-13` e recibo pós-merge `LEA-8` |
| V26 | `docs/architecture/PTM_V2.6_OBSERVACAO_ANALISE_SINAIS_LEA-14_20260716.md` |
| V26-M | `docs/architecture/PTM_V2.6_MATRIZ_RASTREABILIDADE_LEA-14_20260716.md` |
| V26-RC | `docs/history/reviews/REVISAO_CRITICA_PTM_V2.6_LEA-15_20260716.md` |
| V27 | `docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md` |
| V27-M | `docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md` |
| V27-A1 | `docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md` |
| V27-A2 | `docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md` |
| V27-S | `docs/architecture/PTM_V2.7_SUPLEMENTO_RASTREABILIDADE_RETESTE_02_LEA-17_20260717.md` |
| V27-RC | `docs/history/reviews/REVISAO_CRITICA_RETESTE_02_PTM_V2.7_LEA-17_20260717.md` |
| CAP | `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` e adendo transversal |
| DOM | `docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md` |

## 3. Reconciliação numérica

```text
V2_5_STRUCTURAL_REQUIREMENTS=29
V2_5_FUNCTIONAL_REQUIREMENTS=23
V2_5_ADDITIONAL_ACCEPTED_REQUIREMENTS=4
V2_5_TOTAL_REQUIREMENT_IDS=56
V2_6_STRUCTURAL_REQUIREMENTS=28
V2_6_FUNCTIONAL_REQUIREMENTS=50
V2_6_TOTAL_REQUIREMENT_IDS=78
V2_7_STRUCTURAL_REQUIREMENTS=32
V2_7_FUNCTIONAL_REQUIREMENTS=52
V2_7_TOTAL_REQUIREMENT_IDS=84
CROSS_VERSION_TOTAL_REQUIREMENT_IDS=218
CROSS_VERSION_DUPLICATE_IDS=0
NEW_IDS_CREATED_BY_CONSOLIDATION=0
```

## 4. PTM V2.5 — rastreabilidade consolidada

### 4.1 Estruturais — 29 IDs

| IDs cobertos | Qtde. | Domínio | Handoff | Decisão consolidada | Fonte final |
|---|---:|---|---|---|---|
| `PTM-V25-001` a `PTM-V25-006` | 6 | DOM-02, DOM-03 | — | servidor e persistência controlada substituem autoridade JSON e acoplamento do monólito | V25, V25-M, V25-RC |
| `PTM-V25-007` | 1 | DOM-04 | H-01 | listas independentes de observação, análise e execução | V25, V25-RC |
| `PTM-V25-008` a `PTM-V25-009` | 2 | DOM-05 | — | cliente pareado e revogável; servidor mantém autoridade global | V25, V25-RC |
| `PTM-V25-010`, `PTM-V25-011A` a `PTM-V25-011D` | 5 | DOM-06 | H-02 | perfis, ROIs, âncoras e alvos versionados; coordenada não autoriza | V25, V25-M, CAP |
| `PTM-V25-012` a `PTM-V25-013` | 2 | DOM-02, DOM-14 | — | dependências de plataforma isoladas por adaptadores | V25, V25-RC |
| `PTM-V25-014A` a `PTM-V25-014E` | 5 | DOM-03 | — | migração preserva origem, backup, reconciliação e rollback | V25, V25-M, V25-RC |
| `PTM-V25-015A` a `PTM-V25-015E` | 5 | DOM-16 | H-11 | logging, auditoria, métricas, diagnóstico e tracing separados | V25, V25-RC |
| `PTM-V25-016` | 1 | DOM-02, DOM-03 | — | configuração versionada substitui JSON como autoridade final | V25, V25-RC |
| `PTM-V25-017` | 1 | DOM-02, DOM-05, DOM-16 | — | rede local exige autenticação, revogação, limites e redaction | V25, V25-RC |
| `PTM-V25-018` | 1 | DOM-01, DOM-02, DOM-05 | — | servidor inicia em `SAFE_IDLE` | V25, V25-RC |

### 4.2 Funcionais — 23 IDs

| IDs cobertos | Qtde. | Domínio | Handoff | Decisão consolidada | Fonte final |
|---|---:|---|---|---|---|
| `V25-SRV-001` a `V25-SRV-004` | 4 | DOM-01, DOM-02, DOM-03, DOM-05 | — | lifecycle seguro e contratos mínimos versionados | V25, V25-RC |
| `V25-CFG-001` a `V25-CFG-004` | 4 | DOM-02 | — | resolução determinística, fail-closed e redaction | V25, V25-RC |
| `V25-DB-001` a `V25-DB-005` | 5 | DOM-03 | H-11 | integridade, migrations controladas, outbox e restore | V25, V25-RC |
| `V25-LIST-001` a `V25-LIST-004` | 4 | DOM-04 | H-01 | CRUD independente e importação sem execução | V25, V25-RC |
| `V25-LEG-001` a `V25-LEG-006` | 6 | DOM-03 | — | inventário, backup, transformação, reconciliação e rollback | V25, V25-RC |

### 4.3 Requisitos adicionais — 4 IDs

| ID | Domínio | Interpretação consolidada | Fonte final |
|---|---|---|---|
| `V25-SEC-001` | DOM-16 | prova de ausência de ação não declarada ou não controlada | V25-RC, CAP |
| `V25-QA-001` | DOM-16 | quality gate agregado obrigatório | V25-RC |
| `V25-QA-002` | DOM-04, DOM-14, DOM-16 | E2E seguro usa adaptador nulo, simulado ou harness controlado | V25-RC, CAP |
| `V25-DOC-001` | DOM-01 | versão, entrypoint, instalação, README e CHANGELOG coerentes | V25-RC |

```text
V2_5_TOTAL_COVERED=56/56
```

## 5. PTM V2.6 — rastreabilidade consolidada

### 5.1 Estruturais — 28 IDs

| IDs cobertos | Qtde. | Domínio | Handoff | Decisão consolidada | Fonte final |
|---|---:|---|---|---|---|
| `PTM-V26-001` | 1 | DOM-11, DOM-13 | H-08 | análise e execução separadas | V26, V26-RC, CAP |
| `PTM-V26-002` a `PTM-V26-003` | 2 | DOM-07 | H-02, H-03 | sessão e fonte visual autorizadas | V26, V26-RC |
| `PTM-V26-004` | 1 | DOM-08 | H-04 | frame com proveniência | V26, V26-RC |
| `PTM-V26-005` a `PTM-V26-006` | 2 | DOM-09 | H-05 | validação precede análise | V26, V26-RC |
| `PTM-V26-007` a `PTM-V26-008` | 2 | DOM-10 | H-06 | dados estimados versionados e rastreáveis | V26, V26-RC |
| `PTM-V26-009` a `PTM-V26-018` | 10 | DOM-11 | H-07 | motores A–H determinísticos, sem efeito físico | V26, V26-RC |
| `PTM-V26-019` a `PTM-V26-022` | 4 | DOM-12 | H-08 | estratégia, arbitragem e sinal auditáveis | V26, V26-RC |
| `PTM-V26-023`, `PTM-V26-027` | 2 | DOM-03 | — | contratos e entidades seguem existência progressiva | V26, V26-RC |
| `PTM-V26-024` a `PTM-V26-026`, `PTM-V26-028` | 4 | DOM-16 | H-11 | replay, observabilidade e segurança preservam análise→ação | V26, V26-RC, CAP |

### 5.2 Funcionais — 50 IDs

| IDs cobertos | Qtde. | Domínio | Handoff | Decisão consolidada | Fonte final |
|---|---:|---|---|---|---|
| `V26-OBS-001` a `V26-OBS-004` | 4 | DOM-07 | H-02, H-03 | lifecycle de sessão fail-closed | V26, V26-RC |
| `V26-CAP-001` a `V26-CAP-004` | 4 | DOM-08 | H-04 | hash, sequência, origem, ROI e retenção | V26, V26-RC |
| `V26-VAL-001` a `V26-VAL-006` | 6 | DOM-09 | H-05 | checks explícitos e `UNKNOWN` conservador | V26, V26-RC |
| `V26-MAP-001` a `V26-MAP-005` | 5 | DOM-10 | H-06 | extração e mappings versionados | V26, V26-RC |
| `V26-ANA-001` a `V26-ANA-011` | 11 | DOM-11 | H-07 | snapshot elegível, motores A–H e determinismo | V26, V26-RC |
| `V26-STR-001` a `V26-STR-004` | 4 | DOM-12 | H-08 | estratégia explicável e versionada | V26, V26-RC |
| `V26-SIG-001` a `V26-SIG-008` | 8 | DOM-12 | H-08 | sinal, expiração e invalidação sem estado físico | V26, V26-RC |
| `V26-RPL-001` a `V26-RPL-003` | 3 | DOM-16 | — | replay sanitizado e controlado | V26, V26-RC, CAP |
| `V26-API-001` a `V26-API-002` | 2 | DOM-03, DOM-16 | — | contratos versionados e trace | V26, V26-RC |
| `V26-SEC-001` a `V26-SEC-003` | 3 | DOM-16 | H-11 | redaction e prova contra ação não controlada | V26, V26-RC, CAP |

```text
V2_6_TOTAL_COVERED=78/78
```

## 6. PTM V2.7 — rastreabilidade consolidada

### 6.1 Estruturais — 32 IDs

| IDs cobertos | Qtde. | Domínio | Handoff | Decisão consolidada | Fonte final |
|---|---:|---|---|---|---|
| `PTM-V27-001` | 1 | DOM-13, DOM-15 | H-08 a H-10 | sinal, comando, autorização, tentativa, efeito e recibo separados | V27, V27-RC |
| `PTM-V27-002` | 1 | DOM-13 | H-08, H-09 | baseline financeiro simulado | V27, V27-A2, V27-S, V27-RC |
| `PTM-V27-003` | 1 | DOM-14 | H-09, H-10 | ausência, capacidade e fronteira do adaptador real | V27, V27-A2, V27-S, V27-RC |
| `PTM-V27-004` a `PTM-V27-007` | 4 | DOM-13 | H-08, H-09 | comando imutável, grant explícito, revalidação e policy engine | V27, V27-A2, V27-S, V27-RC |
| `PTM-V27-008` a `PTM-V27-009` | 2 | DOM-14 | H-09, H-10 | alvo lógico e adaptadores `NULL|SIMULATED|CONTROLLED_UI` | V27, V27-A2, V27-S, V27-RC |
| `PTM-V27-010` a `PTM-V27-018` | 9 | DOM-15 | H-10 | intent-before-effect, idempotência, retry, circuito e concorrência | V27, V27-A1, V27-A2, V27-RC |
| `PTM-V27-019` | 1 | DOM-16 | H-12 | kill switch domina fila, grant, retry e dispatch | V27, V27-RC |
| `PTM-V27-020` | 1 | DOM-05, DOM-13 | H-09 | presença e confirmação humana explícitas | V27, V27-RC |
| `PTM-V27-021` | 1 | DOM-14, DOM-15 | H-10 | dry-run, simulação e UI controlada usam adaptadores declarados | V27, V27-A2, V27-RC |
| `PTM-V27-022` a `PTM-V27-025` | 4 | DOM-15 | H-10, H-11 | recibo, reconciliação, compensação e `UNKNOWN_EFFECT` explícitos | V27, V27-A2, V27-S, V27-RC |
| `PTM-V27-026` a `PTM-V27-028` | 3 | DOM-16 | H-11 | auditoria, tracing, redaction e rejeição de segredos | V27, V27-RC |
| `PTM-V27-029` | 1 | DOM-03, DOM-15 | — | persistência de execução segue existência progressiva | V27, V27-RC |
| `PTM-V27-030` | 1 | DOM-15 | H-11 | recovery não reenvia automaticamente | V27, V27-RC |
| `PTM-V27-031` | 1 | DOM-16 | H-12 | prova contra bypass, efeito real, segredo e alvo não autorizado | V27, V27-A2, V27-S, V27-RC |
| `PTM-V27-032` | 1 | DOM-01 | H-12 | gate futuro separado para modo financeiro real | V27, V27-A2, V27-S, V27-RC |

### 6.2 Funcionais — 52 IDs

| IDs cobertos | Qtde. | Domínio primário | Handoff | Decisão consolidada | Fonte final |
|---|---:|---|---|---|---|
| `V27-PRE-001` a `V27-PRE-006` | 6 | DOM-13 | H-09 | lifecycle seguro, snapshot e revalidação | V27, V27-A1, V27-A2, V27-S |
| `V27-CMD-001` a `V27-CMD-006` | 6 | DOM-13 | H-08, H-09 | sinal elegível, comando imutável, IDs e terminalidade | V27, V27-A2, V27-S |
| `V27-AUT-001` a `V27-AUT-006` | 6 | DOM-13 | H-09 | ação humana, grant, revogação e autoridade do servidor | V27, V27-A2, V27-S |
| `V27-EXE-001`, `V27-EXE-002`, `V27-EXE-005` a `V27-EXE-007` | 5 | DOM-15 | H-10 | tentativa, dispatch, timeout, retry e circuito | V27, V27-A2, V27-S |
| `V27-EXE-003` a `V27-EXE-004` | 2 | DOM-14 | H-10 | capability e payload do adaptador | V27, V27-A2, V27-S |
| `V27-EXE-008` | 1 | DOM-16 | H-12 | kill switch e contenção do dispatch | V27, V27-A2, V27-S |
| `V27-SAF-001`, `V27-SAF-008` | 2 | DOM-13 | H-09, H-12 | arming, política e ampliação controlada de limites | V27, V27-A2, V27-S, CAP |
| `V27-SAF-002` a `V27-SAF-003` | 2 | DOM-15 | H-10, H-12 | serialização e fila de execução | V27, V27-A2, V27-S, CAP |
| `V27-SAF-006` | 1 | DOM-14 | H-10 | alvo versionado e fronteira do adaptador | V27, V27-A2, V27-S, CAP |
| `V27-SAF-004`, `V27-SAF-005`, `V27-SAF-007` | 3 | DOM-16 | H-10, H-12 | fronteira de UI, segredo e redaction | V27, V27-A2, V27-S, CAP |
| `V27-REC-001` a `V27-REC-006` | 6 | DOM-15 | H-11 | recibo, idempotência, reconciliação e compensação | V27, V27-A2, V27-S |
| `V27-OBS-001` a `V27-OBS-005` | 5 | DOM-16 | H-11 | trace, auditoria, logs, métricas e relatório | V27, V27-RC |
| `V27-QA-001` a `V27-QA-007` | 7 | DOM-16 | H-12 | testes, concorrência, crash/restart e provas negativas | V27, V27-A2, V27-S, V27-RC |

```text
V2_7_STRUCTURAL_COVERED=32/32
V2_7_FUNCTIONAL_COVERED=52/52
V2_7_TOTAL_COVERED=84/84
```

## 7. Interpretação normativa supersessora

- PTM V2.5: `PTM-V25-011C`, `V25-SEC-001`, `V25-QA-002`.
- PTM V2.6: `PTM-V26-001`, `PTM-V26-007`, `PTM-V26-024`, `PTM-V26-028`, `V26-RPL-003`, `V26-SEC-002`, `V26-SEC-003`.
- PTM V2.7 Reteste 02: 22 IDs listados no índice individual, com `execution_channel`, `financial_effect_mode`, `CONTROLLED_UI`, alvo/allowlist, `process_instance_id`, recibo multidimensional e recovery fail-closed.

## 8. Cobertura por handoff

| Handoff | Requisitos principais vinculados |
|---|---|
| H-01 | `PTM-V25-007`, `V25-LIST-*`, `V25-QA-002` |
| H-02 | `PTM-V25-010`, `PTM-V25-011A..D`, `PTM-V26-002`, `V26-OBS-001` |
| H-03 | `PTM-V26-003`, `V26-OBS-*`, `V26-CAP-*` |
| H-04 | `PTM-V26-004`, `V26-CAP-*`, `V26-VAL-*` |
| H-05 | `PTM-V26-005..006`, `V26-VAL-*`, `V26-MAP-*` |
| H-06 | `PTM-V26-007..009`, `V26-MAP-*`, `V26-ANA-001` |
| H-07 | `PTM-V26-010..018`, `V26-ANA-*`, `V26-STR-*` |
| H-08 | `PTM-V26-019..022`, `V26-SIG-*`, `PTM-V27-001`, `V27-CMD-001` |
| H-09 | `PTM-V27-004..008`, `V27-PRE-*`, `V27-CMD-*`, `V27-AUT-*` |
| H-10 | `PTM-V27-009..018`, `V27-EXE-*`, `V27-SAF-002..006` |
| H-11 | `PTM-V27-022..030`, `V27-REC-*`, `V27-OBS-*` |
| H-12 | `PTM-V27-016..020`, `PTM-V27-031..032`, `V27-SAF-*`, `V27-QA-*` |

## 9. Pendências deliberadas

```text
IMPLEMENTATION_EVIDENCE=NOT_CREATED
RUNTIME_TEST_EXECUTION=NOT_EXECUTED
PHYSICAL_SCHEMA=NOT_DEFINED
SQL_AND_MIGRATIONS=NOT_CREATED
FINAL_TEST_ID_BINDING=PENDING_DOCUMENT_MASTER_AND_IMPLEMENTATION_PLAN
NUMERIC_THRESHOLDS=PENDING_REPRODUCIBLE_BENCHMARK
TARGET_LOGICAL_ID_FULL_TAXONOMY=PENDING_ADR_OR_DOCUMENT_MASTER
KILL_SWITCH_TOPOLOGY=PENDING_ADR
```

Cobertura documental não equivale a requisito implementado ou runtime aprovado.

## 10. Resultado do builder — G4

```text
V2_5_TOTAL_COVERED=56/56
V2_6_TOTAL_COVERED=78/78
V2_7_TOTAL_COVERED=84/84
CROSS_VERSION_TOTAL_COVERED=218/218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
NEW_REQUIREMENT_IDS=0
DOM_13_PRIMARY_IDS=26
DOM_14_PRIMARY_IDS=7
DOM_15_PRIMARY_IDS=27
DOM_16_PRIMARY_IDS=38
DOMAIN_LINKAGE_COMPLETE=PASS_BUILDER_REMEDIATED_FOR_RETEST_04
HANDOFF_LINKAGE_COMPLETE=PASS_BUILDER
SUPERSEDED_ID_INTERPRETATION_LINKED=PASS_BUILDER
TRACEABILITY_COMPLETENESS=PASS_BUILDER_REMEDIATED_FOR_RETEST_04
TRACEABILITY_BLOCKERS=0
G4_REQUIREMENTS_TRACEABILITY_COMPLETE=PASS_BUILDER_REMEDIATED
INDEPENDENT_CRITICAL_REVIEW=RETEST_04_REQUIRED
```

## 11. Próxima ação

Executar Reteste 04 independente sobre o novo HEAD do PR `#40`, validando integralmente os `52/52` requisitos funcionais V2.7 e as contagens por domínio primário.
