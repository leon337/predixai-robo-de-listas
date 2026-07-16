# Transições idempotentes

## Contrato

Toda mudança de missão ou gate usa um `transition_id` único e persistente até consolidação.

## Campos persistidos

```text
TRANSITION_ID
FROM_STATE
TO_STATE
BASELINE_MAIN_SHA
BASELINE_STATE_REVISION
BOUND_TRANSITION_ID
OBSERVED_PR_HEAD
GITHUB_UPDATE_STATUS
LINEAR_UPDATE_STATUS
PROJECT_STATE_UPDATE_STATUS
TRUNK_UPDATE_STATUS
HANDOFF_UPDATE_STATUS
TRANSITION_STATUS
TRANSITION_COMPLETE
```

Os campos persistidos registram baseline, vínculo e observação. Nenhum campo persistido usa o prefixo `EXPECTED_`.

## Campos efêmeros da sessão de escrita

```text
PRE_WRITE_EXPECTED_MAIN_SHA
PRE_WRITE_EXPECTED_PR_HEAD
PRE_WRITE_EXPECTED_STATE_REVISION
PRE_WRITE_EXPECTED_TRANSITION_ID
CURRENT_MAIN_SHA
CURRENT_PR_HEAD
CURRENT_STATE_REVISION
CURRENT_TRANSITION_ID
```

Todos os `PRE_WRITE_EXPECTED_*` existem somente na sessão executora. Eles não são persistidos para tentar prever o resultado de um commit futuro.

## State revision

`state_revision` é inteira e monotônica.

- inicia em zero na adoção do protocolo;
- incrementa uma única vez por transição consolidada;
- permanece inalterada durante retries e remediações da mesma transição;
- fica vinculada ao mesmo `transition_id` até conclusão;
- só muda depois da validação das pré-condições;
- não reinicia em migrações de schema.

## Fluxo

```text
PREPARED
→ IN_PROGRESS
→ PARTIAL | READY_FOR_INDEPENDENT_REVIEW | BLOCKED
→ APPROVED_FOR_MERGE
→ MERGED_PENDING_POST_MERGE_CONFIRMATION
→ COMPLETE
```

## Pré-condição de escrita

Antes de cada mutação, a sessão compara:

```text
PRE_WRITE_EXPECTED_MAIN_SHA == CURRENT_MAIN_SHA
PRE_WRITE_EXPECTED_PR_HEAD == CURRENT_PR_HEAD
PRE_WRITE_EXPECTED_STATE_REVISION == CURRENT_STATE_REVISION
PRE_WRITE_EXPECTED_TRANSITION_ID == CURRENT_TRANSITION_ID
```

Após commit válido, o executor consulta os valores atuais e renova somente os snapshots efêmeros da sessão.

## Sincronização parcial

```text
TRANSITION_STATUS=PARTIAL
GITHUB_UPDATE_STATUS=PASS
LINEAR_UPDATE_STATUS=FAIL
NEXT_ACTION=RETRY_LINEAR_SYNC
STATE_REVISION=UNCHANGED
TRANSITION_ID=UNCHANGED
```

O próximo chat conclui a mesma transição. É proibido criar nova missão ou incrementar a revisão.

## Prevenção de avanço duplicado

- arquivo já atualizado: não regravar sem necessidade;
- comentário Linear já publicado: não duplicar;
- issue já movida: confirmar, não mover novamente;
- PR já aberta: reutilizar;
- merge já ocorrido: iniciar transição pós-merge, não repetir merge;
- recibo já integrado: não criar outro para a mesma transição.

## Duas transições de fechamento

### Transição A — implementação documental

Produz documentos, manifesto preliminar, `PROJECT_STATE`, tronco, Linear e PR principal. Termina em:

```text
MAIN_PR_MERGED=PASS
TRANSITION_STATUS=MERGED_PENDING_POST_MERGE_CONFIRMATION
```

### Transição B — confirmação pós-merge

Somente após observar o merge real:

- confirmar `main` e merge commit;
- confirmar Linear;
- registrar `HANDOFF_ACTIVATED=PASS`;
- incrementar `state_revision` uma vez;
- encerrar o `transition_id` anterior;
- criar recibo em PR documental pequeno e separado.

A missão só fecha quando:

```text
POST_MERGE_TRANSITION_STARTED=PASS
POST_MERGE_RECEIPT_PR=<numero>
POST_MERGE_RECEIPT_MERGED=PASS
TRANSITION_COMPLETE=YES
```

## Falhas canônicas

```text
PARTIAL_SYNC_RECOVERY=RETRY_SAME_TRANSITION
DUPLICATE_ADVANCE=BLOCKED
UNKNOWN_TRANSITION=STATE_RECONSTRUCTION_REQUIRED
SCHEMA_INCOMPATIBLE=BLOCKED_BY_SCHEMA_MISMATCH
CONNECTOR_UNAVAILABLE=BLOCKED_BY_CONNECTOR_FAILURE
```

## Gates

```text
IDEMPOTENT_TRANSITION_PROTOCOL=PASS_REMEDIATED_SPECIFIED
PARTIAL_SYNC_RECOVERY=PASS_SPECIFIED
DUPLICATE_ADVANCE_PREVENTION=PASS_SPECIFIED
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```
