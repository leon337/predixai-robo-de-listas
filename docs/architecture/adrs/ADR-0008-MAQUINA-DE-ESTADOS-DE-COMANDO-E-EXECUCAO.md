# ADR-0008 — Máquina de estados de comando e execução

## Controle

```text
ADR_ID=ADR-0008
CANDIDATE_ID=ADR-CAND-010
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

A PTM V2.7 separa sinal, comando, grant, resolução de alvo, tentativa, recibo e efeito confirmado. Essa cadeia precisa de estados persistidos e transições explícitas para sobreviver a concorrência, timeout e restart sem duplicar ação.

## Decisão

Adotar duas máquinas relacionadas e servidor-autoritativas:

1. **Command/Grant FSM**, responsável por elegibilidade, autorização e arming;
2. **Execution Attempt FSM**, responsável por tentativa, recibo, reconciliação e resultado.

Estados de comando:

```text
DRAFT|VALIDATING|AUTHORIZED|READY|CANCELLED|EXPIRED|KILLED|BLOCKED
```

Estados de arming da sessão:

```text
DISABLED|SAFE_IDLE|ARMED_DRY_RUN|ARMED_SIMULATED|ARMED_CONTROLLED_UI|ARMED_LIVE_GATED|KILLED
```

Estados da tentativa:

```text
CREATED|DISPATCHING|AWAITING_RECEIPT|RECONCILING|COMPLETED_NO_EFFECT|COMPLETED_SIMULATED|COMPLETED_CONTROLLED_UI|COMPLETED_LIVE_GATED|FAILED_NO_EFFECT|TIMED_OUT|UNKNOWN_EFFECT|KILLED
```

O comando e o grant são imutáveis após `AUTHORIZED`; qualquer alteração exige nova identidade. A tentativa é gravada antes do adaptador. Um restart invalida a despachabilidade de comandos anteriores e nunca retoma tentativa automaticamente.

## Regras normativas

```text
SIGNAL!=COMMAND
COMMAND!=GRANT
GRANT!=ATTEMPT
ATTEMPT!=EFFECT
STATE_TRANSITION=SERVER_VALIDATED_AND_PERSISTED
AUTHORIZED_COMMAND=IMMUTABLE
ATTEMPT_WRITE_BEFORE_EFFECT=REQUIRED
RESTART_INVALIDATES_DISPATCHABILITY=YES
TIMEOUT!=NO_EFFECT
UNKNOWN_EFFECT=NO_AUTOMATIC_RETRY
LIVE_ARMING=ALL_GATES_REQUIRED
```

## Alternativas consideradas

### Um único status genérico

Rejeitado por misturar autorização, tentativa e resultado, ocultando estados ambíguos.

### Estado mantido somente em memória

Rejeitado por tornar restart e auditoria inseguros.

### Retomar automaticamente após restart

Rejeitado por risco de duplicação e efeito desconhecido.

## Consequências

### Positivas

- transições auditáveis;
- recovery explícito;
- separação entre Modo A e Modo B;
- idempotência e kill switch integráveis.

### Negativas e custos

- mais estados e reason codes;
- interfaces precisam lidar com estados intermediários;
- mudanças na FSM exigem versionamento e compatibilidade.

## Segurança, recovery e falha segura

```text
INVALID_TRANSITION=REJECT_AND_AUDIT
STALE_AGGREGATE_VERSION=CONFLICT
RESTART=SAFE_IDLE_AND_RECONCILIATION_REQUIRED
KILL_SWITCH=DOMINANT_TERMINAL_TRANSITION
UNKNOWN_EFFECT=CORRELATED_TARGET_BLOCK
EXPIRED_GRANT=NO_DISPATCH
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-13|DOM-15
SECONDARY_DOMAINS=DOM-01|DOM-12|DOM-14|DOM-16
HANDOFFS=H-08|H-09|H-10|H-11|H-12
REQUIREMENTS=PTM-V27-001..007|V27-PRE-001..006|V27-CMD-001..006|V27-AUT-001..006|PTM-V27-010..018|PTM-V27-022..025|V27-REC-001..006
DEPENDS_ON=ADR-0001|ADR-0002|ADR-0007
```

## Critérios de aceitação

```text
COMMAND_GRANT_ATTEMPT_SEPARATION=PASS
PERSISTED_TRANSITIONS=PASS
RESTART_FAIL_CLOSED=PASS
TIMEOUT_UNKNOWN_EFFECT_SEPARATION=PASS
LIVE_STATE_GATED=PASS
```

## Fora de escopo

- código da FSM;
- biblioteca de state machine;
- tabelas físicas;
- thresholds de timeout;
- implementação de adaptador.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.