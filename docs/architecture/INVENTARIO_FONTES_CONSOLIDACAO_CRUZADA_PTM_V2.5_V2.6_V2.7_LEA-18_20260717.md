# INVENTÁRIO CANÔNICO DE FONTES — CONSOLIDAÇÃO CRUZADA

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=CANONICAL_SOURCE_INVENTORY_REMEDIATED_FOR_RETEST_04
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASELINE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
CURRENT_MAIN_OBSERVED=236bc5df7f675ca5cf56d80c5812bd911d224651
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
POLICY_A_B_ALIGNMENT=PASS_BUILDER
```

## 2. Objetivo

Definir quais fontes governam o presente, quais comprovam decisões históricas, quais cláusulas foram supersedidas e quais evidências devem ser preservadas sem serem tratadas como autoridade atual.

## 3. Autoridade por domínio

```text
CURRENT_OPERATIONAL_STATE=PROJECT_RUNTIME_STATE.yaml
CURRENT_HUMAN_STATE=PROJECT_STATE.md
CURRENT_ROADMAP=PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md
CONSOLIDATED_DOCUMENTATION=GitHub_main
UNMERGED_DOCUMENTATION=PR_40
TASK_STATUS=Linear_LEA_18_LEA_19
AUTOMATION_POLICY=docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
HISTORICAL_EVIDENCE=docs/history|docs/audits
```

Não existe precedência única para todos os domínios. Estado operacional, trabalho não integrado, tarefa, documentação consolidada e evidência histórica são resolvidos por suas autoridades próprias.

## 4. Precedência normativa A+B

Para conflitos sobre análise visual, captura, OCR, replay, ponteiro, teclado, preenchimento de campos, clique, autenticação, alvo controlado e efeito financeiro:

```text
1. docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
2. docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md
3. docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md
4. docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md
5. documentos-pai e matrizes para cláusulas não supersedidas
6. revisões, checkpoints e recibos históricos como evidência do estado anterior
```

Resultado vigente:

```text
MODE_A_CONTROLLED_AUTOMATION=AUTHORIZED
CONTROLLED_CHART_ANALYSIS=ALLOWED
CONTROLLED_CAPTURE_OCR_REPLAY=ALLOWED
CONTROLLED_POINTER_KEYBOARD_FIELDS_CLICK=ALLOWED
CONTROLLED_AUTHENTICATION=ALLOWED
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCKED_BY_DOMAIN_BOUNDARY
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_FINANCIAL_EFFECT=BLOCKED_UNTIL_ALL_LIVE_GATES_PASS
CONTROLLED_UI_ACTION_DOES_NOT_IMPLY_LIVE_AUTHORIZATION=TRUE
```

## 5. Fontes vivas da missão

| ID | Fonte | Papel | Autoridade atual | Tratamento |
|---|---|---|---|---|
| GOV-01 | `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md` | regras permanentes | normativa | aplicar integralmente |
| GOV-02 | `PROJECT_RUNTIME_STATE.yaml` no PR `#40` | estado operacional estruturado | canônica da transição ativa | manter sincronizado |
| GOV-03 | `PROJECT_STATE.md` no PR `#40` | visão humana do estado | derivada do manifesto | não divergir do GOV-02 |
| GOV-04 | `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` no PR `#40` | roadmap e continuidade | governante do fluxo | manter alinhado |
| GOV-05 | `docs/protocols/AUTORIDADE_POR_DOMINIO.md` | resolução de autoridade e drift | normativa | aplicar por domínio |
| GOV-06 | `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` | política A+B | normativa ativa de maior precedência no tema | prevalece sobre proibições genéricas antigas |
| GOV-07 | Linear `LEA-18` | tarefa, dependências, bloqueios e progresso | operacional | manter alinhado ao PR `#40` |
| GOV-08 | GitHub PR `#40` | trabalho documental não integrado | autoridade do conteúdo em construção | Draft até solicitação formal do Reteste 04 |
| GOV-09 | README da `main` | painel público | projeção derivada | sincronizar após mudança de estado público |

## 6. Fundação factual herdada

| ID | Fonte | Papel | Status | Uso na consolidação |
|---|---|---|---|---|
| AUD-01 | `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md` | snapshot factual inicial | histórico | usar fatos, não marcador antigo de estado |
| AUD-02 | `docs/audits/ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md` | correção de evidência e rastreabilidade | remediação concluída | governa a interpretação final |
| AUD-03 | `docs/audits/ANEXO_A_APENDICE_04_ARVORE_AST_DOCUMENTACAO_FINAL_PTP-GOV.6_20260716.md` | fechamento documental da árvore e AST | evidência final | sustenta inventário e contagens |
| AUD-04 | `docs/audits/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz.b64` | evidência bruta | verificável por hash | preservar |
| AUD-05 | `docs/history/reviews/REVISAO_CRITICA_AUDITORIA_MESTRA_PTP-GOV.6_20260716.md` | Boss Gate da Auditoria Mestra | PASS | sustenta as PTMs |
| AUD-06 | `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md` | contratos conceituais históricos | referência | não converter automaticamente em implementação |

## 7. PTM V2.5

| ID | Fonte | Papel | Autoridade na consolidação |
|---|---|---|---|
| V25-01 | `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md` | documento-pai | cláusulas não supersedidas |
| V25-02 | `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md` | rastreabilidade | base dos 56 IDs |
| V25-03 | revisão final do PR `#33`, review `4718668692` | Boss Gate | PASS |
| V25-04 | Linear `LEA-13` | controle operacional | Done/PASS |
| V25-05 | `docs/history/ptp/RECIBO_POS_MERGE_LEA-8_PTM_V2.5_20260716.md` | confirmação pós-merge | V2.5 definitiva |

```text
V25_STRUCTURAL_REQUIREMENTS=29
V25_FUNCTIONAL_REQUIREMENTS=23
V25_ADDITIONAL_REQUIREMENTS_ACCEPTED=4
V25_TOTAL_UNIQUE_REQUIREMENT_IDS=56
V25_CRITICAL_REVIEW=PASS
```

Frases históricas de exclusão de ponteiro e clique significam que a V2.5 não possui autoridade para produzir ação de UI. Elas não proíbem automação controlada pelo Modo A nem suporte arquitetural ao Modo B.

## 8. PTM V2.6

| ID | Fonte | Papel | Autoridade na consolidação |
|---|---|---|---|
| V26-01 | `docs/architecture/PTM_V2.6_OBSERVACAO_ANALISE_SINAIS_LEA-14_20260716.md` | documento-pai | cláusulas analíticas não supersedidas |
| V26-02 | `docs/architecture/PTM_V2.6_MATRIZ_RASTREABILIDADE_LEA-14_20260716.md` | rastreabilidade | base dos 78 IDs |
| V26-03 | `docs/history/reviews/REVISAO_CRITICA_PTM_V2.6_LEA-15_20260716.md` | Boss Gate | PASS |
| V26-04 | Linear `LEA-15` | controle operacional | Done/PASS |
| V26-05 | `docs/history/ptp/RECIBO_POS_MERGE_LEA-14_PTM_V2.6_20260716.md` | confirmação pós-merge | V2.6 definitiva |

```text
V26_STRUCTURAL_REQUIREMENTS=28
V26_FUNCTIONAL_REQUIREMENTS=50
V26_TOTAL_REQUIREMENT_IDS=78
V26_CRITICAL_REVIEW=PASS
```

`REAL_INPUT_AND_EXECUTION_EXCLUSION` significa ausência de acoplamento `ANALYSIS -> UNDECLARED_UI_ACTION`. Captura, OCR, replay e harness controlado permanecem permitidos.

## 9. Política transversal A+B

| ID | Fonte | Papel | Autoridade |
|---|---|---|---|
| CAP-00 | `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` | política normativa A+B | maior precedência |
| CAP-01 | `docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md` | correção de fronteira capacidade/etapa/efeito | complementar, quando não conflitar com CAP-00 |

```text
V2_5_OWNS_UI_AUTOMATION=NO
V2_6_ANALYSIS_DOMAIN_PRODUCES_UI_ACTION=NO
MODE_A_CONTROLLED_AUTOMATION=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_RUNTIME_ACTIVATION=DISABLED_UNTIL_ALL_GATES_PASS
```

## 10. PTM V2.7

| ID | Fonte | Papel | Autoridade na consolidação |
|---|---|---|---|
| V27-01 | `docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md` | documento-pai | cláusulas não supersedidas |
| V27-02 | `docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md` | matriz principal | base dos 84 IDs, complementada pelo suplemento |
| V27-03 | `docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md` | remediação inicial | aplicar onde não substituído |
| V27-04 | `docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md` | contrato CONTROLLED_UI e restart | normativo substituto |
| V27-05 | `docs/architecture/PTM_V2.7_SUPLEMENTO_RASTREABILIDADE_RETESTE_02_LEA-17_20260717.md` | interpretação dos IDs afetados | complementa a matriz |
| V27-06 | `docs/history/reviews/REVISAO_CRITICA_RETESTE_02_PTM_V2.7_LEA-17_20260717.md` | Boss Gate final | FINAL_PASS |
| V27-07 | Linear `LEA-17` | controle operacional | Done/PASS |
| V27-08 | `docs/history/ptp/RECIBO_POS_MERGE_LEA-16_PTM_V2.7_20260717.md` | recibo pós-merge | integrado |
| V27-09 | PR `#39`, merge `98bb1d33b9d8eca702fb4e52bdde02686021c766` | confirmação final | libera a consolidação |

```text
V27_STRUCTURAL_REQUIREMENTS=32
V27_FUNCTIONAL_REQUIREMENTS=52
V27_TOTAL_REQUIREMENT_IDS=84
V27_CRITICAL_REVIEW=PASS
V27_RETEST_02=PASS_AUTHORITY
```

## 11. Evidência da remediação do Reteste 03

| Fonte | Uso |
|---|---|
| `docs/history/reviews/REVISAO_CRITICA_RETESTE_03_CONSOLIDACAO_CRUZADA_LEA-19_20260717.md` | achados MAJOR-07, MAJOR-08 e MINOR-04 |
| `docs/history/reviews/REMEDIACAO_RETESTE_03_CONSOLIDACAO_CRUZADA_LEA-18_20260717.md` | síntese da remediação |
| `docs/history/reviews/REMEDIACAO_RETESTE_03_AUDITORIA_IDS_FUNCIONAIS_V2.7_LEA-18_20260718.md` | auditoria individual dos 52/52 IDs funcionais |

## 12. Fontes históricas sem autoridade atual

Permanecem consultáveis, mas não governam o presente:

- checkpoints anteriores aos recibos pós-merge;
- auto-revisões do builder;
- prompts de revisão;
- revisões `FAIL` supersedidas;
- cláusulas antigas de proibição global de capacidade de UI;
- marcadores antigos `DRAFT_PARTIAL`, `PENDING` ou `BLOCKED_BY_ENVIRONMENT`.

## 13. Ausências e decisões explícitas

O relatório Markdown final presumido da PTM V2.5 não existe. A autoridade composta é:

1. review final `4718668692` no PR `#33`;
2. Linear `LEA-13`;
3. recibo pós-merge `RECIBO_POS_MERGE_LEA-8_PTM_V2.5_20260716.md`.

```text
INVENTED_REPLACEMENT=NO
APPLICATION_IMPLEMENTED=NO_EVIDENCE_IN_THIS_MISSION
RUNTIME_VALIDATED=NO
SQL_OR_MIGRATIONS_AUTHORIZED=NO
```

## 14. Pendências arquiteturais carregadas

1. taxonomia integral de `target_logical_id`;
2. limites numéricos após benchmark reproduzível;
3. ADR da topologia do kill switch;
4. matriz integral de transições antes da implementação;
5. granularidade funcional por requisito da V2.6;
6. contratos físicos, produtores, consumidores e IDs finais de testes;
7. separação entre especificação e evidência runtime;
8. desenho completo do gate LIVE do Modo B.

## 15. Resultado

```text
CANONICAL_SOURCE_CATEGORIES=7
CURRENT_GOVERNING_SOURCES_IDENTIFIED=PASS
LEGACY_FACTUAL_AUTHORITY_IDENTIFIED=PASS
PTM_V2_5_FINAL_AUTHORITY_IDENTIFIED=PASS
PTM_V2_6_FINAL_AUTHORITY_IDENTIFIED=PASS
PTM_V2_7_FINAL_AUTHORITY_IDENTIFIED=PASS
POLICY_A_B_AUTHORITY_IDENTIFIED=PASS
SUPERSESSION_CHAIN_IDENTIFIED=PASS
MISSING_SOURCE_HANDLING=PASS
SOURCE_INVENTORY_BLOCKERS=0
G2_SOURCE_INVENTORY_COMPLETE=PASS_BUILDER_REMEDIATED
INDEPENDENT_CRITICAL_REVIEW=RETEST_04_REQUIRED
```

## 16. Próxima ação

Executar o Reteste 04 independente da LEA-19 no HEAD final do PR #40.