# REMEDIAÇÃO DE SCHEMA E FONTES — LEA-26

## Preparação do LEA-27 Reteste 03

## Controle

```text
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
PULL_REQUEST=46
PREVIOUS_AUTHORIZED_HEAD=decb578bd9b4c4bbe9d62947359eb59569d89020
MERGE_EXECUTED=NO
RETEST_SEQUENCE=03
DOCUMENTATION_ONLY=YES
MERGE_AUTHORIZED=NO
DOCUMENT_MASTER_START_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
```

## Origem

A verificação imediatamente anterior ao merge encontrou duas threads novas depois do Reteste 02:

```text
FINDING_01=PROJECT_RUNTIME_STATE_SCHEMA_1_0_3_INCOMPATIBILITY
FINDING_02=STALE_OPERATIONAL_RETEST_REFERENCES_IN_ADR_SOURCES
```

A autorização anterior estava vinculada ao HEAD indicado acima. Como a correção altera o PR, ela não autoriza o novo HEAD.

## Correção 01 — compatibilidade com o schema 1.0.3

O manifesto voltou a cumprir `docs/protocols/PROJECT_RUNTIME_STATE_SCHEMA.yaml`:

```text
TOP_LEVEL_OBSERVED_PR_HEAD=RESTORED
MISSION_LOCK_OBSERVED_PR_HEAD=RESTORED
OBSERVED_PR_HEAD_SEMANTICS=INFORMATIONAL_SNAPSHOT
LIVE_PR_HEAD_SOURCE=GITHUB_API
TRANSITION_STATUS=READY_FOR_INDEPENDENT_REVIEW
GITHUB_SYNC_STATUS=IN_PROGRESS
LINEAR_SYNC_STATUS=PASS
GATE_STATUS=IN_PROGRESS
EXECUTION_STATUS=AWAITING_INDEPENDENT_REVIEW
STATE_REVISION=11_PRESERVED_DURING_PARTIAL_RETRY
```

Os valores de enumeração usados pertencem aos conjuntos permitidos pelo schema 1.0.3. `snapshot_content_head` permanece metadado adicional, sem substituir o campo obrigatório `observed_pr_head`.

## Correção 02 — autoridade das fontes

Plano, índice e matriz foram atualizados para indicar `LEA-27 Reteste 03`. O manifesto deixou de tratá-los como fontes do gate operacional e passou a separá-los como evidência de conteúdo arquitetural.

```text
OPERATIONAL_GATE_SOURCES=
PROJECT_RUNTIME_STATE.yaml|
PROJECT_STATE.md|
PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md|
README.md|
PR_46_LIVE|
LINEAR_LEA_26_LEA_27

ARCHITECTURE_CONTENT_EVIDENCE=
PLANO_MISSAO|
ADR_INDEX|
TRACEABILITY_MATRIX|
TRACEABILITY_APPENDIX
```

O apêndice `218/218` preserva a tabela factual. Qualquer status de reteste embutido em seu snapshot histórico é superado explicitamente pelas fontes operacionais atuais e não pode controlar handoff, revisão ou merge.

## Validações do builder

```text
SCHEMA_REQUIRED_TOP_LEVEL_FIELDS=PASS_BUILDER
MISSION_LOCK_REQUIRED_FIELDS=PASS_BUILDER
TRANSITION_STATUS_ENUM=PASS_BUILDER
SYNC_STATUS_ENUM=PASS_BUILDER
GATE_STATUS_ENUM=PASS_BUILDER
EXECUTION_STATUS_ENUM=PASS_BUILDER
SOURCE_AUTHORITY_CURRENT=PASS_BUILDER
PLAN_RETEST_REFERENCE=03
ADR_INDEX_RETEST_REFERENCE=03
TRACEABILITY_MATRIX_RETEST_REFERENCE=03
MERGE_EXECUTED=NO
```

## Condição para avanço

```text
THREADS_MUST_BE_RESOLVED=YES
CI_MUST_PASS=9_OF_9
LEA_27_RETEST_03=PASS_REQUIRED
NEW_HUMAN_MERGE_AUTHORIZATION=REQUIRED_FOR_NEW_HEAD
```

O builder não emite o Boss Gate final.