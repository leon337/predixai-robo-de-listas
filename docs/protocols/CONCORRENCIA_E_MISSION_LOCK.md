# Concorrência e Mission Lock

## Modelo

```text
LOCK_ENFORCEMENT=ADVISORY
CONCURRENCY_MODEL=OPTIMISTIC
STALE_WRITE_PROTECTION=SESSION_PRE_WRITE_SNAPSHOT_PLUS_SHA_AND_STATE_REVISION
```

O mission lock informa posse lógica e intenção de escrita. Ele não impede tecnicamente outro chat ou usuário de alterar GitHub ou Linear.

## Separação dos heads

```text
OBSERVED_PR_HEAD
PRE_WRITE_EXPECTED_PR_HEAD
CURRENT_PR_HEAD
```

- `OBSERVED_PR_HEAD`: snapshot informativo persistido no manifesto;
- `PRE_WRITE_EXPECTED_PR_HEAD`: valor capturado externamente pela sessão antes da escrita;
- `CURRENT_PR_HEAD`: valor consultado no GitHub imediatamente antes da escrita.

É proibido persistir na própria branch um `expected_pr_head` que tente representar o SHA do commit que ainda será criado. Isso produziria uma expectativa autorreferente e imediatamente obsoleta.

## Campos do lock

```text
MISSION_LOCKED=YES|NO
LOCK_OWNER
LOCK_SESSION_ID
LOCK_BASE_SHA
LOCK_OBSERVED_PR_HEAD
LOCK_STARTED_AT
LOCK_EXPIRES_AT
LOCK_HEARTBEAT_AT
EXPECTED_STATE_REVISION
EXPECTED_TRANSITION_ID
```

## Pré-condições antes de cada escrita

A sessão deve capturar os valores esperados e, imediatamente antes da mutação, consultar os valores atuais:

```text
PRE_WRITE_EXPECTED_MAIN_SHA == CURRENT_MAIN_SHA
PRE_WRITE_EXPECTED_PR_HEAD == CURRENT_PR_HEAD
PRE_WRITE_EXPECTED_STATE_REVISION == CURRENT_STATE_REVISION
PRE_WRITE_EXPECTED_TRANSITION_ID == CURRENT_TRANSITION_ID
```

O valor esperado do PR head é memória efêmera da sessão, não campo autoritativo persistido na branch.

Se qualquer igualdade falhar:

```text
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
WRITE_OPERATION=PROHIBITED
STATE_RECONSTRUCTION_REQUIRED=YES
```

## Escritas sequenciais da mesma sessão

Após cada commit confirmado:

1. consultar o novo `CURRENT_PR_HEAD`;
2. atualizar o snapshot efêmero da sessão;
3. não reescrever o manifesto somente para tentar armazenar o SHA do próprio commit;
4. atualizar `OBSERVED_PR_HEAD` apenas em marcos de sincronização úteis;
5. confirmar novamente main, revisão e transição antes da próxima escrita.

## Aquisição lógica

1. reconstruir GitHub, PR, manifesto e Linear;
2. confirmar ausência de lock válido incompatível;
3. capturar main SHA, PR head, state revision e transition id;
4. registrar owner, session e snapshot informativo;
5. só então iniciar escrita documental.

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
