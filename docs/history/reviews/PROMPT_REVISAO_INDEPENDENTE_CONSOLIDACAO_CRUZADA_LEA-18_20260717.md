# PACOTE PARA REVISÃO CRÍTICA INDEPENDENTE — CONSOLIDAÇÃO CRUZADA

## LEA-18 / PR #40

## 1. Papel do revisor

Atuar como revisor independente da consolidação cruzada das PTMs V2.5, V2.6 e V2.7. Não aceitar a auto-revisão do builder como Boss Gate e não alterar código, SQL, migrations ou escopo.

## 2. Controle

```text
REVIEW_PACKAGE_STATUS=READY
BUILDER_MISSION=LEA-18
REVIEWED_PULL_REQUEST=40
REVIEWED_PRODUCT_CONTENT_HEAD=99acfd6e014d5bc3c1beb03888f34b04e4aa457e
BUILDER_SELF_REVIEW_COMMIT=6a5fd591f507a8063f18136472c7ebd6e8c50480
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
MERGE_AUTHORIZED=NO
ADRS_AUTHORIZED=NO
```

## 3. Fontes obrigatórias do PR

1. `docs/architecture/INVENTARIO_FONTES_CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
2. `docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
3. `docs/architecture/MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
4. `docs/architecture/APENDICE_INDICE_INDIVIDUAL_218_REQUISITOS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
5. `docs/architecture/REGISTRO_CONFLITOS_SUPERSESSOES_PRECEDENCIA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
6. `docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
7. `docs/architecture/CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
8. `docs/history/reviews/AUTO_REVISAO_BUILDER_CONSOLIDACAO_CRUZADA_LEA-18_20260717.md` apenas como evidência preliminar;
9. `PROJECT_RUNTIME_STATE.yaml`, `PROJECT_STATE.md` e tronco multichat.

## 4. Fontes herdadas obrigatórias

- PTM V2.5 e matriz;
- revisão final do PR `#33`, Linear `LEA-13` e recibo pós-merge V2.5;
- PTM V2.6, matriz, revisão `LEA-15` e recibo pós-merge V2.6;
- PTM V2.7, matriz, adendos, suplemento do reteste 02, revisão `LEA-17` e recibo pós-merge V2.7;
- Auditoria Mestra V2.4.3-R1 e revisão crítica aprovada;
- `POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`;
- `ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md`;
- `AUTORIDADE_POR_DOMINIO.md`.

## 5. Verificações obrigatórias

### 5.1 Escopo e integridade

```text
DOCUMENTATION_ONLY_SCOPE
APPLICATION_CODE_UNCHANGED
TEST_CODE_UNCHANGED
WORKFLOWS_UNCHANGED
SQL_AND_MIGRATIONS_ABSENT
MAIN_BASE_UNCHANGED
PR_HEAD_BINDING
```

### 5.2 Fontes e autoridade

```text
SOURCE_INVENTORY_COMPLETENESS
AUTHORITY_BY_DOMAIN_CONSISTENCY
MAIN_VS_PR_SEPARATION
MANIFEST_PROJECT_STATE_TRUNK_ALIGNMENT
LINEAR_PR_ALIGNMENT
HISTORICAL_VS_CURRENT_AUTHORITY_SEPARATION
V2_5_COMPOSITE_REVIEW_EVIDENCE_VALIDITY
```

### 5.3 Domínios e fronteiras

```text
CANONICAL_DOMAIN_COUNT_16
MANDATORY_HANDOFF_COUNT_12
DOMAIN_AUTHORITY_INPUT_OUTPUT_STATE_BLOCKER_COMPLETENESS
V2_5_V2_6_V2_7_SCOPE_SEPARATION
ANALYSIS_EXECUTION_SEPARATION
SIGNAL_COMMAND_AUTHORIZATION_SEPARATION
COORDINATE_AUTHORIZATION_SEPARATION
RECEIPT_RECONCILIATION_SEPARATION
SERVER_CLIENT_AUTHORITY_SEPARATION
FORBIDDEN_BYPASS_COMPLETENESS
```

### 5.4 Requisitos e rastreabilidade

```text
V2_5_REQUIREMENTS=56/56
V2_6_REQUIREMENTS=78/78
V2_7_REQUIREMENTS=84/84
CROSS_VERSION_REQUIREMENTS=218/218
INDIVIDUAL_INDEX_ROWS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
NEW_REQUIREMENT_IDS=0
DOMAIN_LINKAGE_COMPLETENESS
HANDOFF_LINKAGE_COMPLETENESS
SUPERSEDED_INTERPRETATION_LINKAGE
```

O revisor deve verificar amostras e a reconciliação integral, não apenas aceitar contagens declaradas.

### 5.5 Conflitos e precedência

```text
CONFLICT_CLASSES_REVIEWED=24
UNRESOLVED_NORMATIVE_CONFLICTS=0_EXPECTED
CONTROLLED_AUTOMATION_POLICY_PRECEDENCE
V2_7_RETEST_02_PRECEDENCE
BUILDER_DRAFT_FINAL_REVIEW_RECEIPT_SEMANTICS
MERGEABILITY_VS_AUTHORIZATION_SEPARATION
DOCUMENTATION_VS_RUNTIME_SEPARATION
```

### 5.6 Segurança

```text
CONTROLLED_CAPTURE_OCR_REPLAY_ALLOWED
CONTROLLED_UI_BOUNDARY
ANALYSIS_DIRECT_UI_ACTION_BLOCKED
TARGET_AND_ACTION_ALLOWLIST_REQUIRED
AUTHORIZATION_AND_KILL_SWITCH_REQUIRED
REAL_FINANCIAL_EFFECT_BLOCKED_ALL_TARGET_CLASSES
PRODUCTION_SECRETS_BLOCKED
UNKNOWN_EFFECT_CONTAINMENT
RESTART_INVALIDATES_OLD_COMMAND
TIMEOUT_DOES_NOT_PROVE_NO_EFFECT
```

### 5.7 ADRs e próximos estágios

```text
ADR_CANDIDATE_COUNT=18
ADR_CREATED=NO
TECHNOLOGY_FINALIZED=NO
DOCUMENT_MASTER_CREATED=NO
ARCHITECTURE_V1_FROZEN=NO
IMPLEMENTATION_AUTHORIZED=NO
ROADMAP_SEQUENCE_PRESERVED
```

## 6. Perguntas críticas

1. Algum domínio possui duas autoridades globais incompatíveis?
2. Existe caminho que permita lista, análise ou sinal alcançar diretamente adaptador de UI?
3. Alguma redação permite interpretar coordenada como autorização?
4. `CONTROLLED_UI` pode ser confundido com efeito financeiro real?
5. Algum estado ou recibo confirma mais do que sua evidência permite?
6. Restart, timeout ou `UNKNOWN_EFFECT` permitem retry ou rearmamento inseguro?
7. Os 218 IDs estão realmente presentes, únicos e vinculados?
8. Alguma cláusula histórica superada ainda aparece como governante?
9. Algum ADR candidato já contém decisão tecnológica indevidamente fechada?
10. As fontes vivas e Linear refletem o mesmo estágio?

## 7. Severidades

```text
CRITICAL=risco de efeito financeiro real, bypass de autorização, segredo, perda de autoridade ou avanço indevido
MAJOR=contradição arquitetural, requisito órfão, fronteira incompleta, rastreabilidade materialmente incorreta ou precedência ambígua
MINOR=clareza, nomenclatura, referência ou consistência sem brecha arquitetural
```

## 8. Resultado exigido

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS|FAIL
REVIEWED_PR_HEAD=<sha>
CRITICAL_FINDINGS=<n>
MAJOR_FINDINGS=<n>
MINOR_FINDINGS=<n>
SOURCE_INVENTORY_COMPLETENESS=PASS|FAIL
DOMAIN_BOUNDARY_CONSISTENCY=PASS|FAIL
TRACEABILITY_COMPLETENESS=PASS|FAIL
CONFLICT_SUPERSESSION_RESOLUTION=PASS|FAIL
CONTROLLED_AUTOMATION_SECURITY=PASS|FAIL
REAL_FINANCIAL_EFFECT_SEPARATION=PASS|FAIL
GITHUB_LINEAR_ALIGNMENT=PASS|FAIL
DOCUMENTAL_READY_FOR_MERGE=YES|NO
ADRS_READY_TO_START=YES|NO
RETEST_REQUIRED=YES|NO
```

Condição mínima de `PASS`:

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
SOURCE_INVENTORY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=PASS
TRACEABILITY_COMPLETENESS=PASS
CONFLICT_SUPERSESSION_RESOLUTION=PASS
CONTROLLED_AUTOMATION_SECURITY=PASS
REAL_FINANCIAL_EFFECT_SEPARATION=PASS
GITHUB_LINEAR_ALIGNMENT=PASS
```

## 9. Restrições do revisor

- não aprovar com achado crítico ou maior aberto;
- não tratar mergeabilidade como autorização de merge;
- não alterar código, SQL ou migrations;
- não iniciar ADRs;
- não declarar runtime aprovado;
- não reescrever históricos;
- registrar relatório final em `docs/history/reviews/` e comentário no PR `#40`;
- manter a issue builder aberta até merge e confirmação pós-merge.

## 10. Próxima ação após a revisão

- `FAIL`: converter/manter PR Draft, registrar bloqueio e devolver ao builder;
- `PASS`: autorizar apenas a preparação operacional para merge, ainda dependente de autorização humana e confirmação do HEAD final.