# PTM V2.7 — SUPLEMENTO DE RASTREABILIDADE DO RETESTE 02

## LEA-17 / PR #37

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_TRACEABILITY_SUPPLEMENT_READY_FOR_RETEST
PARENT_MATRIX=docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md
NORMATIVE_ADDENDUM=docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md
POLICY=docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
NEW_REQUIREMENT_IDS=0
STRUCTURAL_COUNT_UNCHANGED=32
FUNCTIONAL_COUNT_UNCHANGED=52
TOTAL_COUNT_UNCHANGED=84
```

Este suplemento não cria IDs. Ele registra a interpretação normativa final dos requisitos afetados pelos achados do segundo ciclo de revisão.

## 2. Requisitos estruturais afetados

| ID | Interpretação normativa | Fonte | Gate |
|---|---|---|---|
| `PTM-V27-002` | Canal de UI e dimensão monetária são independentes: `CONTROLLED_UI` é permitido; resultado monetário real permanece não autorizado em qualquer classe de alvo. | Política §5; Adendo 02 §2 | `FINANCIAL_EFFECT_INDEPENDENT_DIMENSION` |
| `PTM-V27-003` | Adaptador financeiro externo continua ausente; adaptador de UI controlada não é adaptador financeiro. | Adendo 02 §§2,6 | `REAL_FINANCIAL_ADAPTER_ABSENT` |
| `PTM-V27-009` | Contrato comum aceita `NULL`, `SIMULATED` e `CONTROLLED_UI`, com capacidades explícitas e fail-closed. | Adendo 02 §6 | `CONTROLLED_UI_ADAPTER_CONTRACT` |
| `PTM-V27-014` | Qualquer restart invalida a despachabilidade de comando anterior pela mudança de `process_instance_id`; relógio monotônico só vale na mesma instância. | Adendo 02 §9 | `RESTART_INVALIDATES_DISPATCHABILITY` |
| `PTM-V27-025` | Efeito de UI desconhecido e dimensão monetária desconhecida são reconciliados separadamente e bloqueiam correlatos. | Adendo 02 §7 | `UNKNOWN_EFFECT_CONTAINMENT` |
| `PTM-V27-031` | Prova negativa busca bypass, alvo não autorizado, segredo e resultado monetário real; não exige ausência das bibliotecas de UI. | Política; Adendo transversal; Adendo 02 §8 | `UNCONTROLLED_ACTION_NEGATIVE_PROOF` |
| `PTM-V27-032` | Qualquer resultado monetário real exige gate próprio em toda classe de alvo. | Política §5 | `REAL_FINANCIAL_EFFECT_SEPARATE_GATE` |

## 3. Requisitos funcionais afetados

| ID | Critério final | Evidência futura |
|---|---|---|
| `V27-PRE-002` | Validar alvo, canal, dimensão monetária, boot, instância de processo e fonte temporal. | lifecycle e restart tests |
| `V27-CMD-002` | Comando declara `execution_channel`, `financial_effect_mode`, identidade do alvo e `process_instance_id_at_creation`. | contract tests |
| `V27-AUT-002` | Grant vincula canal, dimensão monetária, alvo e versão da allowlist. | auth mutation tests |
| `V27-AUT-004` | Mudança de canal, alvo, ação ou dimensão monetária exige novo grant. | reauthorization tests |
| `V27-EXE-001` | Dispatch somente no `ARMED_*` compatível com o canal autorizado. | state transition tests |
| `V27-EXE-003` | Adaptador declara `NULL`, `SIMULATED` ou `CONTROLLED_UI`; desconhecido bloqueia. | adapter contract tests |
| `V27-EXE-004` | `CONTROLLED_UI` recebe ação e alvo allowlisted, sem segredo de produção e sem capacidade monetária real. | payload negative tests |
| `V27-EXE-005` | Restart invalida comando anterior; timeout ou ambiguidade nunca presumem sucesso. | crash/restart tests |
| `V27-SAF-004` | Biblioteca de UI só pode ser alcançada pelo adaptador controlado, nunca por bypass. | AST/import graph tests |
| `V27-SAF-005` | Segredo de produção é rejeitado em qualquer canal. | secret scans |
| `V27-SAF-006` | Coordenada integra alvo versionado; coordenada isolada não autoriza ação. | target compatibility tests |
| `V27-REC-001` | Recibo separa `ui_result` e `financial_result`. | receipt contract tests |
| `V27-REC-003` | Reconciliação compara as duas dimensões sem inferência cruzada. | reconciliation tests |
| `V27-QA-005` | Restart no mesmo boot e em boot diferente prova ausência de redespacho e exige novo comando. | crash/recovery suite |
| `V27-QA-006` | Prova negativa cobre bypass, alvo externo não autorizado, segredo e resultado monetário real. | static, contract e runtime-negative tests |

## 4. Casos de contradição obrigatórios

```text
CONTROLLED_UI_WITH_REAL_FINANCIAL_EFFECT=BLOCK
CONTROLLED_UI_WITH_PRODUCTION_CREDENTIAL=BLOCK
CONTROLLED_UI_WITH_UNLISTED_TARGET=BLOCK
PRE_RESTART_COMMAND_REARM=BLOCK
PRE_RESTART_COMMAND_REDISPATCH=BLOCK
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCK
CONTROLLED_UI_EFFECT_IMPLIES_FINANCIAL_EFFECT=FALSE
```

## 5. Resultado do builder

```text
CONTROLLED_UI_NORMATIVE_TRACEABILITY=PASS_BUILDER
FINANCIAL_EFFECT_ALL_TARGET_CLASSES=PASS_BUILDER
SAME_BOOT_RESTART_FAIL_CLOSED=PASS_BUILDER
REQUIREMENT_COUNT_RECONCILIATION=PASS
INDEPENDENT_RETEST_REQUIRED=YES
```
