# REVISÃO CRÍTICA INDEPENDENTE — CONSOLIDAÇÃO CRUZADA

## LEA-19 / PR #40

## 1. Controle

```text
REVIEW_TYPE=INDEPENDENT_CRITICAL_REVIEW
REVIEW_ISSUE=LEA-19
BUILDER_ISSUE=LEA-18
REVIEWED_PULL_REQUEST=40
REVIEWED_PR_HEAD=83e8b76f8f38b5037f63a2718ec34f63227169ec
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_OR_MIGRATIONS_CREATED=NO
RUNTIME_EXECUTED=NO
MERGE_AUTHORIZED=NO
ADRS_START_AUTHORIZED=NO
```

## 2. Escopo auditado

Foram confrontados:

1. os 13 arquivos alterados no PR `#40`;
2. `PROJECT_RUNTIME_STATE.yaml` contra `docs/protocols/PROJECT_RUNTIME_STATE_SCHEMA.yaml` versão `1.0.3`;
3. inventário canônico, mapa de 16 domínios e 12 handoffs;
4. matriz consolidada e índice individual dos 218 requisitos;
5. matrizes canônicas das PTMs V2.5, V2.6 e V2.7;
6. política de automação controlada, adendo transversal e adendo normativo do Reteste 02;
7. registro de conflitos, catálogo de ADRs e documento consolidado;
8. estado do PR, GitHub Actions, Linear `LEA-18` e `LEA-19`.

## 3. Evidências positivas

```text
CHANGED_FILE_COUNT=13
APPLICATION_CODE_FILES_CHANGED=0
TEST_CODE_FILES_CHANGED=0
WORKFLOW_FILES_CHANGED=0
SQL_FILES_CHANGED=0
MIGRATION_FILES_CHANGED=0
DOCUMENTATION_ONLY_SCOPE=PASS
GITHUB_ACTIONS_RUNS_CHECKED=9
GITHUB_ACTIONS_SUCCESS=9/9
CANONICAL_DOMAIN_COUNT=16
MANDATORY_HANDOFF_COUNT=12
V2_5_REQUIREMENTS=56/56
V2_6_REQUIREMENTS=78/78
V2_7_REQUIREMENTS=84/84
CROSS_VERSION_REQUIREMENTS=218/218
INDIVIDUAL_INDEX_ROWS=218
DOMAIN_COUNT_SUM=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
NEW_REQUIREMENT_IDS=0
ADR_CANDIDATE_COUNT=18
ADR_CREATED=NO
```

A reconciliação dos requisitos foi confrontada com as matrizes canônicas:

- V2.5: `29 estruturais + 23 funcionais + 4 adicionais = 56`;
- V2.6: `28 estruturais + 50 funcionais = 78`;
- V2.7: `32 estruturais + 52 funcionais = 84`;
- soma por domínio no índice individual: `218`.

Não foi encontrado caminho arquitetural que permita lista, análise ou sinal chamar diretamente o adaptador de UI. Coordenada permanece geometria, não autorização. Recibo permanece evidência, não verdade global. `CONTROLLED_UI` não autoriza efeito financeiro real. Restart invalida comando anterior e `UNKNOWN_EFFECT` bloqueia retry correlato.

## 4. Achados maiores

### MAJOR-01 — `gate_status` viola o schema operacional 1.0.3

**Arquivo:** `PROJECT_RUNTIME_STATE.yaml`

**Estado encontrado:**

```text
gate_status=AWAITING_INDEPENDENT_REVIEW
```

**Contrato vigente:** `docs/protocols/PROJECT_RUNTIME_STATE_SCHEMA.yaml` permite somente:

```text
NOT_STARTED|IN_PROGRESS|PASS|WARN|FAIL|BLOCKED
```

`AWAITING_INDEPENDENT_REVIEW` é valor permitido para `safety.execution_status`, não para `gate_status`.

**Impacto:** consumidor estrito do manifesto deve rejeitar o estado e reconstruir a continuidade como `BLOCKED_BY_SCHEMA_MISMATCH`. O manifesto canônico não pode declarar sincronização `PASS` enquanto viola o próprio contrato.

**Remediação exigida:** usar valor compatível, por exemplo `IN_PROGRESS` durante a revisão ou `FAIL/BLOCKED` após reprovação; alternativa exige migração formal e retrocompatível do schema.

```text
MAJOR_01_STATUS=OPEN
```

### MAJOR-02 — campo obrigatório `real_click_authorized` removido sem migração do schema

**Arquivo:** `PROJECT_RUNTIME_STATE.yaml`

O schema `1.0.3` exige `real_click_authorized` como propriedade booleana. O manifesto substituiu a semântica por campos novos, mas manteve `schema_version: 1.0.3` e não publicou migração retrocompatível.

**Impacto:** leitores estritos não conseguem validar ou reconstruir o estado operacional. A ampliação de campos pode coexistir, mas não pode remover propriedade obrigatória sem versão e migração.

**Remediação exigida:** restaurar o campo de compatibilidade com valor coerente ao escopo da missão ou versionar/migrar formalmente o contrato conforme `schema_migration`.

```text
MAJOR_02_STATUS=OPEN
```

### MAJOR-03 — precedência normativa contraditória entre fontes vivas

**Arquivo principal:** `docs/architecture/INVENTARIO_FONTES_CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`

O inventário registra:

```text
POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
> ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA
> PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK
```

Porém o próprio adendo normativo do Reteste 02, posterior e específico, registra:

```text
POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
> THIS_RETEST_02_ADDENDUM
> ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA
```

O registro de conflitos usa a segunda ordem. Portanto, o inventário canônico e o registro de conflitos não apresentam a mesma cadeia de autoridade.

**Impacto:** `AUTHORITY_BY_DOMAIN_CONSISTENCY` e `CONFLICT_SUPERSESSION_RESOLUTION` não podem passar enquanto a precedência estiver ambígua. A divergência afeta contratos finais de `CONTROLLED_UI`, estados, recibos e recovery temporal.

**Remediação exigida:** corrigir o inventário para refletir a ordem normativa final do Reteste 02 e revisar todas as referências derivadas.

```text
MAJOR_03_STATUS=OPEN
```

## 5. Achados menores

### MINOR-01 — documento consolidado preserva estágio anterior à auto-revisão

`CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md` ainda declara documento pronto para auto-revisão, revisão independente pendente e próxima ação de executar a auto-revisão, embora o PR já contenha auto-revisão concluída e pacote independente.

**Remediação:** atualizar somente os marcadores vivos do documento para o estágio efetivo de handoff independente.

```text
MINOR_01_STATUS=OPEN
```

### MINOR-02 — estado Draft contradiz o estado real do PR

O inventário e o registro de conflitos afirmam que o PR `#40` deve permanecer ou permanece Draft. O GitHub mostra o PR marcado como pronto para revisão. O `PROJECT_STATE.md` e o comentário de handoff também registram pronto para revisão.

**Impacto:** inconsistência operacional sem brecha financeira ou autorização de merge, pois `MERGE_AUTHORIZED=NO` permanece explícito.

**Remediação:** uniformizar a redação. Em resultado `FAIL`, converter o PR novamente para Draft.

```text
MINOR_02_STATUS=OPEN
```

## 6. Gates avaliados

```text
SOURCE_INVENTORY_COMPLETENESS=FAIL
AUTHORITY_BY_DOMAIN_CONSISTENCY=FAIL
DOMAIN_BOUNDARY_CONSISTENCY=PASS
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS
TRACEABILITY_COMPLETENESS=PASS
DUPLICATE_AND_ORPHAN_REQUIREMENT_CHECK=PASS
CONFLICT_SUPERSESSION_RESOLUTION=FAIL
CONTROLLED_AUTOMATION_SECURITY=PASS
REAL_FINANCIAL_EFFECT_SEPARATION=PASS
RESTART_FAIL_CLOSED=PASS
DOCUMENTATION_RUNTIME_SEPARATION=PASS
GITHUB_LINEAR_ALIGNMENT=FAIL
```

`GITHUB_LINEAR_ALIGNMENT=FAIL` decorre do manifesto operacional inválido e da impossibilidade de considerar `github_sync_status=PASS` e `linear_sync_status=PASS` enquanto o contrato canônico não valida.

## 7. Resultado final

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=FAIL
REVIEWED_PR_HEAD=83e8b76f8f38b5037f63a2718ec34f63227169ec
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=3
MINOR_FINDINGS=2
SOURCE_INVENTORY_COMPLETENESS=FAIL
DOMAIN_BOUNDARY_CONSISTENCY=PASS
TRACEABILITY_COMPLETENESS=PASS
CONFLICT_SUPERSESSION_RESOLUTION=FAIL
CONTROLLED_AUTOMATION_SECURITY=PASS
REAL_FINANCIAL_EFFECT_SEPARATION=PASS
GITHUB_LINEAR_ALIGNMENT=FAIL
DOCUMENTAL_READY_FOR_MERGE=NO
ADRS_READY_TO_START=NO
RETEST_REQUIRED=YES
MERGE_AUTHORIZED=NO
```

## 8. Decisão do Boss Gate

```text
G7_INDEPENDENT_CRITICAL_REVIEW=FAIL
AUDITORIA_INDEPENDENTE_CONCLUIDA=YES
BUILDER_REMEDIATION_REQUIRED=YES
PR_RETURN_TO_DRAFT=YES
ADRS_START_BLOCKED=YES
```

A arquitetura consolidada apresenta boa separação de domínios, rastreabilidade integral e contenção financeira adequada. O avanço é bloqueado exclusivamente pelos três achados maiores de governança, schema e precedência normativa.

## 9. Próxima ação

O builder deve corrigir os três achados maiores e os dois menores, publicar novo HEAD e solicitar reteste independente da `LEA-19`. Merge e ADRs permanecem proibidos.