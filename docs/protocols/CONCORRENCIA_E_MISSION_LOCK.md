# Concorrência e Mission Lock

## Modelo

```text
LOCK_ENFORCEMENT=ADVISORY
CONCURRENCY_MODEL=OPTIMISTIC
STALE_WRITE_PROTECTION=SHA_AND_STATE_REVISION
```

O mission lock informa posse lógica e intenção de escrita. Ele não impede tecnicamente outro chat ou usuário de alterar GitHub ou Linear.

## Campos

```text
MISSION_LOCKED=YES|NO
LOCK_OWNER
LOCK_SESSION_ID
LOCK_BASE_SHA
LOCK_PR_HEAD
LOCK_STARTED_AT
LOCK_EXPIRES_AT
LOCK_HEARTBEAT_AT
EXPECTED_STATE_REVISION
EXPECTED_TRANSITION_ID
```

## Pré-condições obrigatórias antes de escrita

```text
EXPECTED_MAIN_SHA == CURRENT_MAIN_SHA
EXPECTED_PR_HEAD == CURRENT_PR_HEAD
EXPECTED_STATE_REVISION == CURRENT_STATE_REVISION
EXPECTED_TRANSITION_ID == CURRENT_TRANSITION_ID
```

Se qualquer igualdade falhar:

```text
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
WRITE_OPERATION=PROHIBITED
STATE_RECONSTRUCTION_REQUIRED=YES
```

## Aquisição lógica

1. reconstruir GitHub, PR, manifesto e Linear;
2. confirmar ausência de lock válido incompatível;
3. registrar owner, session, SHA, revision e transition;
4. registrar heartbeat;
5. só então iniciar escrita documental.

## Heartbeat

O heartbeat é atualizado em marcos documentais significativos, não a cada resposta. Ausência de heartbeat não prova abandono; exige reconstrução.

## Expiração

Um lock pode ter `expires_at_utc`. Após expiração:

1. não assumir automaticamente a missão;
2. verificar branch, PR, commits, manifesto e Linear;
3. confirmar que não houve avanço;
4. registrar recuperação do lock;
5. manter o mesmo `transition_id` quando a transição estiver incompleta.

## Transferência

A transferência de missão deve registrar:

```text
PREVIOUS_LOCK_OWNER
NEW_LOCK_OWNER
TRANSFER_REASON
BASE_SHA_CONFIRMED
PR_HEAD_CONFIRMED
STATE_REVISION_CONFIRMED
TRANSITION_ID_PRESERVED
```

## Encerramento

O lock só é encerrado após:

- transição concluída ou formalmente pausada;
- estado sincronizado;
- próxima ação registrada;
- nenhum write pendente.

## Trabalho concorrente detectado

Quando outro chat avançou:

```text
CONCURRENT_WORK_DETECTED=YES
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
```

O chat deve parar, reconstruir, comparar e adaptar a base. Nunca sobrescrever trabalho mais recente.

## Falha de conectores

- GitHub indisponível: nenhuma escrita externa é autorizada.
- Linear indisponível: alterações GitHub podem permanecer em transição parcial, sem conclusão.
- ambos indisponíveis: somente análise local e nenhuma declaração de estado atual.

## Gates

```text
CONCURRENT_CHAT_CONTROL=PASS_SPECIFIED
STALE_WRITE_PROTECTION=PASS_SPECIFIED
ABANDONED_LOCK_RECOVERY=PASS_SPECIFIED
```

Esses resultados são de especificação. Runtime permanece `NOT_EXECUTED` até testes independentes.
