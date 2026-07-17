# Sincronização final da PTP-MEM.1 — schema 1.0.3

## Motivo

Após a integração da PR nº 31, o GitHub `main` e o Linear já indicavam a conclusão da PTP-MEM.1, mas os documentos vivos ainda representavam a Transição B em andamento.

## Estado confirmado

```text
MAIN_HEAD_CONFIRMED=6d37cee2e63fefb631b5b17b9d4717e54ebef93f
MAIN_PR_30_MERGED=PASS
POST_MERGE_RECEIPT_PR_31_MERGED=PASS
LEA_12=DONE
STATE_REVISION=1
TRANSITION_ID=PTP-MEM.1-T02
TRANSITION_COMPLETE=YES
```

## Migração do schema

```text
FROM_SCHEMA_VERSION=1.0.2
TO_SCHEMA_VERSION=1.0.3
MIGRATION_ID=PTP-MEM.1-FINAL-SYNC-001
BASELINE_STATE_REVISION=1
RESULTING_STATE_REVISION=1
BOUND_TRANSITION_ID=PTP-MEM.1-T02
BACKWARD_COMPATIBLE=YES
ROLLBACK_DEFINED=YES
MIGRATION_STATUS=COMPLETE
```

A migração substitui `main_head` por `observed_main_head` como snapshot informativo. O SHA atual para pré-condição de escrita continua sendo consultado ao vivo e comparado com `PRE_WRITE_EXPECTED_MAIN_SHA` efêmero.

Essa mudança impede que o próprio merge do PR de sincronização torne o manifesto imediatamente inconsistente por autorreferência.

## Resultado

```text
MANIFEST_DOCUMENTATION_DRIFT=NO
GITHUB_SYNC_STATUS=PASS
LINEAR_SYNC_STATUS=PASS
ACTIVE_MISSION=NONE
NEXT_ISSUE=LEA-8_TODO_NOT_STARTED
AUTOMATIC_ADVANCE=NO
RUNTIME_R8_R24=NOT_EXECUTED
SCHEMA_RUNTIME_VALIDATION=NOT_EXECUTED
APPLICATION_CODE_CHANGED=NO
```
