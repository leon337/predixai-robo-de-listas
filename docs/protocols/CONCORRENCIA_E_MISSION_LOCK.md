# Concorrência e Mission Lock

## Modelo

```text
LOCK_ENFORCEMENT=ADVISORY
CONCURRENCY_MODEL=OPTIMISTIC
STALE_WRITE_PROTECTION=SESSION_PRE_WRITE_SNAPSHOT_PLUS_SHA_AND_STATE_REVISION
```

O mission lock informa posse lógica e intenção de escrita. Ele não impede tecnicamente outro chat ou usuário de alterar GitHub ou Linear.

## Semântica canônica

```text
OBSERVED_PR_HEAD=PERSISTED_INFORMATIONAL_SNAPSHOT
PRE_WRITE_EXPECTED_PR_HEAD=EPHEMERAL_SESSION_VALUE
CURRENT_PR_HEAD=LIVE_GITHUB_QUERY
SELF_REFERENTIAL_EXPECTED_HEAD=PROHIBITED
```

- `OBSERVED_PR_HEAD`: snapshot informativo persistido;
- `PRE_WRITE_EXPECTED_*`: valores efêmeros capturados pela sessão imediatamente antes da escrita;
- `CURRENT_*`: valores consultados nas fontes vivas imediatamente antes da mutação.

Nenhum campo persistido pode usar o prefixo `EXPECTED_` para representar uma expectativa de pré-escrita.

## Campos persistidos do lock

```text
MISSION_LOCKED=YES|NO
LOCK_OWNER
LOCK_SESSION_ID
LOCK_BASE_SHA
LOCK_OBSERVED_PR_HEAD
LOCK_STATE_REVISION_SNAPSHOT
LOCK_TRANSITION_ID_SNAPSHOT
LOCK_STARTED_AT
LOCK_EXPIRES_AT
LOCK_HEARTBEAT_AT
```

Os campos `LOCK_STATE_REVISION_SNAPSHOT` e `LOCK_TRANSITION_ID_SNAPSHOT` são informativos. Não substituem as expectativas efêmeras da sessão.

## Pré-condições antes de cada escrita

A sessão captura os valores esperados e consulta os valores atuais imediatamente antes da mutação:

```text
PRE_WRITE_EXPECTED_MAIN_SHA == CURRENT_MAIN_SHA
PRE_WRITE_EXPECTED_PR_HEAD == CURRENT_PR_HEAD
PRE_WRITE_EXPECTED_STATE_REVISION == CURRENT_STATE_REVISION
PRE_WRITE_EXPECTED_TRANSITION_ID == CURRENT_TRANSITION_ID
```

Se qualquer igualdade falhar:

```text
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
WRITE_OPERATION=PROHIBITED
STATE_RECONSTRUCTION_REQUIRED=YES
```

## Escritas sequenciais da mesma sessão

Após cada commit confirmado:

1. consultar o novo `CURRENT_PR_HEAD`;
2. renovar `PRE_WRITE_EXPECTED_PR_HEAD` apenas na memória efêmera da sessão;
3. não reescrever o manifesto para armazenar o SHA do próprio commit;
4. atualizar `OBSERVED_PR_HEAD` somente em marcos úteis de sincronização;
5. confirmar novamente main, revisão e transição antes da próxima escrita.

## Aquisição lógica

1. reconstruir GitHub, PR, manifesto e Linear;
2. confirmar ausência de lock consultivo incompatível;
3. capturar os quatro valores `PRE_WRITE_EXPECTED_*`;
4. registrar apenas snapshots informativos do lock;
5. executar a escrita somente após validar as quatro invariantes.

## Heartbeat

O heartbeat é atualizado em marcos documentais significativos, não a cada resposta. Ausência de heartbeat não prova abandono; exige reconstrução.

## Expiração e recuperação

Após expiração:

1. não assumir automaticamente a missão;
2. verificar branch, PR, commits, manifesto e Linear;
3. confirmar se houve avanço;
4. registrar recuperação do lock;
5. preservar `transition_id` e `state_revision` quando a transição estiver incompleta.

## Transferência

```text
PREVIOUS_LOCK_OWNER
NEW_LOCK_OWNER
TRANSFER_REASON
BASE_SHA_CONFIRMED
OBSERVED_PR_HEAD_CONFIRMED
STATE_REVISION_CONFIRMED
TRANSITION_ID_PRESERVED
```

## Encerramento

O lock só é encerrado após transição concluída ou formalmente pausada, estado sincronizado, próxima ação registrada e ausência de escrita pendente.

## Falha de conectores

```text
BLOCKED_BY_CONNECTOR_FAILURE
```

- GitHub indisponível: nenhuma escrita externa é autorizada;
- Linear indisponível: GitHub pode permanecer em sincronização parcial sem conclusão;
- ambos indisponíveis: somente análise sem declaração de estado atual.

## Gates

```text
CONCURRENT_CHAT_CONTROL=PASS_SPECIFIED
STALE_WRITE_PROTECTION=PASS_REMEDIATED_SPECIFIED
ABANDONED_LOCK_RECOVERY=PASS_SPECIFIED
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```
