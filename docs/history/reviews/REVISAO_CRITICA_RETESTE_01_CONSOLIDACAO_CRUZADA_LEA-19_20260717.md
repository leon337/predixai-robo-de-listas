# REVISÃO CRÍTICA INDEPENDENTE — RETESTE 01

## Consolidação cruzada PTM V2.5 / V2.6 / V2.7 — LEA-19 / PR #40

## 1. Controle

```text
REVIEW_TYPE=INDEPENDENT_CRITICAL_RETEST_01
REVIEW_ISSUE=LEA-19
BUILDER_ISSUE=LEA-18
REVIEWED_PULL_REQUEST=40
FAILED_REVIEWED_HEAD=83e8b76f8f38b5037f63a2718ec34f63227169ec
REMEDIATION_BASE_HEAD=4b2d3c86cb45801032372494e3dc24a99fb4dbbb
REVIEWED_PR_HEAD=f6616ff5a936aaa3061b182a693f8ba1dafe3c6e
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

## 2. Escopo do reteste

O reteste confrontou:

1. o relatório independente anterior da `LEA-19`;
2. os commits de remediação `0c7c5904ed753765d4861341f7dd18d838d91ff9` e `f6616ff5a936aaa3061b182a693f8ba1dafe3c6e`;
3. `PROJECT_RUNTIME_STATE.yaml` contra o schema `1.0.3`;
4. a precedência do inventário contra o adendo normativo do Reteste 02;
5. `PROJECT_RUNTIME_STATE.yaml`, `PROJECT_STATE.md`, tronco multichat, GitHub e Linear;
6. o índice individual dos 218 requisitos contra a matriz V2.5 e o mapa unificado de domínios;
7. o estado das threads de revisão e dos workflows do HEAD informado.

## 3. Remediações anteriores

### MAJOR-01 — schema de `gate_status`

```text
EXPECTED=IN_PROGRESS|PASS|WARN|FAIL|BLOCKED|NOT_STARTED
FOUND=IN_PROGRESS
MAJOR_01_REMEDIATION=PASS
```

O valor agora pertence ao enum permitido pelo schema `1.0.3`.

### MAJOR-02 — compatibilidade `real_click_authorized`

```text
FIELD_PRESENT=YES
VALUE=false
MAJOR_02_REMEDIATION=PASS
```

O campo obrigatório foi restaurado sem ampliar autorização de clique ou efeito financeiro.

### MAJOR-03 — precedência normativa

```text
POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
> PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK
> ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA
> PTM_V2.7_ADENDO_REMEDIACAO_01
> DOCUMENTO_PAI
MAJOR_03_REMEDIATION=PASS
```

A ordem do inventário agora coincide com o adendo normativo final.

## 4. Evidências positivas

```text
REMEDIATION_COMMITS=2
REMEDIATION_FILES_CHANGED=2
APPLICATION_CODE_FILES_CHANGED_BY_REMEDIATION=0
TEST_CODE_FILES_CHANGED_BY_REMEDIATION=0
SQL_OR_MIGRATION_FILES_CHANGED_BY_REMEDIATION=0
SCHEMA_REQUIRED_GATE_STATUS=PASS
SCHEMA_REQUIRED_REAL_CLICK_FIELD=PASS
NORMATIVE_PRECEDENCE=PASS
PREVIOUS_P1_THREADS_RESOLVED=2/2
GITHUB_ACTIONS_SUCCESS=9/9
PR_OPEN=YES
PR_READY_FOR_REVIEW=YES
PR_MERGEABLE=YES
```

Os contratos de automação controlada e separação de efeito financeiro permanecem fail-closed. Nenhuma correção autorizou código, SQL, migration, ADR, merge ou efeito financeiro real.

## 5. Novos achados maiores

### MAJOR-04 — drift entre manifesto, visão humana e tronco

`PROJECT_RUNTIME_STATE.yaml` registra:

```text
active_stage=CROSS_CONSOLIDATION_INDEPENDENT_RETEST
transition_status=READY_FOR_INDEPENDENT_REVIEW
to_state=CROSS_CONSOLIDATION_AWAITING_INDEPENDENT_RETEST
independent_critical_review=RETEST_REQUESTED_LEA_19
previous_independent_review_status=FAIL
```

Porém `PROJECT_STATE.md` e `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` continuam registrando a etapa inicial:

```text
TRANSITION_STATUS=IN_PROGRESS
TO_STATE=CROSS_CONSOLIDATION_AWAITING_INDEPENDENT_REVIEW
G7_INDEPENDENT_CRITICAL_REVIEW=AWAITING_LEA_19
NEXT_ACTION=EXECUTE_LEA_19_INDEPENDENT_CRITICAL_REVIEW_ON_PR_40
```

Ao mesmo tempo, o manifesto declara:

```text
manifest_documentation_drift=false
github_sync_status=PASS
linear_sync_status=PASS
```

As instruções permanentes determinam que divergência entre manifesto e documentação produza `MANIFEST_DOCUMENTATION_DRIFT=YES`, `EXECUTION_STATUS=BLOCKED_BY_STATE_DRIFT` e proíba avanço automático.

**Impacto:** o bootstrap reconstrói fases diferentes conforme a fonte lida. O estado operacional não pode ser considerado sincronizado ou pronto para avanço.

**Remediação exigida:** sincronizar `PROJECT_STATE.md`, tronco e marcadores vivos derivados com o estado de reteste/reprovação; enquanto houver divergência, registrar drift e bloqueio conforme o protocolo.

```text
MAJOR_04_STATUS=OPEN
```

### MAJOR-05 — domínio primário incorreto no índice individual

O índice individual coloca `PTM-V25-003` em:

```text
DOM-02=CONFIGURACAO_IDENTIDADE_SEGREDOS
```

A matriz canônica V2.5 classifica o requisito como:

```text
DOMAIN=persistence
DECISION=single_writer_boundary_and_progressive_physical_schema
```

O mapa unificado atribui persistência e fronteira de escritor único a:

```text
DOM-03=PERSISTENCIA_EVENTOS_BACKUP_RECOVERY
AUTHORITY=SERVER_SINGLE_WRITE_BOUNDARY
```

**Impacto:** o apêndice afirma que cada requisito aparece sob seu domínio primário, mas ao menos um vínculo primário está incorreto. Isso torna inexata a rastreabilidade por requisito, a propriedade do domínio e as contagens derivadas usadas para ADRs.

**Remediação exigida:** mover `PTM-V25-003` para `DOM-03`, reconciliar as contagens e auditar todos os grupos consolidados que possuem múltiplos domínios para confirmar o domínio primário de cada ID individual.

```text
MAJOR_05_STATUS=OPEN
```

## 6. Achado menor residual

### MINOR-03 — documento consolidado ainda descreve a auto-revisão como próxima etapa

`CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md` ainda registra:

```text
DOCUMENT_STATUS=BUILDER_CROSS_CONSOLIDATION_READY_FOR_SELF_REVIEW
G6_CONSOLIDATED_DOCUMENT_READY=READY_FOR_BUILDER_SELF_REVIEW
INDEPENDENT_CRITICAL_REVIEW=PENDING
NEXT_ACTION=EXECUTAR_AUTO_REVISAO_PRELIMINAR
```

Esse marcador é histórico incorreto em um documento tratado como consolidado e deve ser atualizado para o estágio efetivo após a remediação.

```text
MINOR_03_STATUS=OPEN
```

O antigo `MINOR-02`, relacionado ao estado Draft, foi resolvido: o inventário agora descreve a transição Draft→ready e o PR estava pronto para revisão no momento do reteste.

## 7. Gates avaliados

```text
MAJOR_01_REMEDIATION=PASS
MAJOR_02_REMEDIATION=PASS
MAJOR_03_REMEDIATION=PASS
SCHEMA_COMPATIBILITY=PASS
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
GITHUB_LINEAR_ALIGNMENT=FAIL
```

## 8. Resultado final

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=FAIL
RETEST_SEQUENCE=01
REVIEWED_PR_HEAD=f6616ff5a936aaa3061b182a693f8ba1dafe3c6e
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=1
SOURCE_INVENTORY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=FAIL
TRACEABILITY_COMPLETENESS=FAIL
CONFLICT_SUPERSESSION_RESOLUTION=PASS
CONTROLLED_AUTOMATION_SECURITY=PASS
REAL_FINANCIAL_EFFECT_SEPARATION=PASS
GITHUB_LINEAR_ALIGNMENT=FAIL
DOCUMENTAL_READY_FOR_MERGE=NO
ADRS_READY_TO_START=NO
RETEST_REQUIRED=YES
MERGE_AUTHORIZED=NO
```

## 9. Decisão do Boss Gate

```text
G7_INDEPENDENT_CRITICAL_REVIEW=FAIL_RETEST_01
AUDITORIA_INDEPENDENTE_CONCLUIDA=YES
PREVIOUS_MAJOR_REMEDIATION=PASS_3_OF_3
NEW_MAJOR_FINDINGS=2
BUILDER_REMEDIATION_REQUIRED=YES
PR_RETURN_TO_DRAFT=YES
ADRS_START_BLOCKED=YES
```

As três remediações solicitadas foram efetivas, mas o HEAD não pode avançar porque as fontes vivas divergem e o índice individual contém vínculo primário incorreto. O builder deve corrigir os novos achados, atualizar o documento consolidado e solicitar novo reteste independente.

## 10. Próxima ação

Corrigir `MAJOR-04`, `MAJOR-05` e `MINOR-03`, publicar novo HEAD e reabrir a `LEA-19` para Reteste 02. Merge, ADRs, código, SQL, migrations e implementação permanecem proibidos.