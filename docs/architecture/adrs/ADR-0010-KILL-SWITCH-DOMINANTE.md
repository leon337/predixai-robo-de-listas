# ADR-0010 — Kill switch dominante e fail-closed

## Controle

```text
ADR_ID=ADR-0010
CANDIDATE_ID=ADR-CAND-012
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

Qualquer ação controlada precisa poder ser interrompida antes do dispatch e durante o fluxo. O kill switch deve dominar fila, grants, retries e adaptadores, inclusive diante de conexão móvel perdida ou estado parcialmente degradado.

## Decisão

Adotar kill switch global, servidor-autoritativo, persistido e com **epoch de segurança**.

A ativação incrementa o `kill_epoch`, muda o sistema para `KILLED`, invalida grants e comandos despacháveis e cancela filas ainda sem efeito. Cada tentativa e `adapter_request` carrega o epoch observado; o adaptador verifica o estado imediatamente antes do efeito.

Serão previstos dois caminhos independentes de ativação:

1. comando autenticado no painel/servidor;
2. caminho local no host, independente da sessão móvel, como hotkey, sinal do processo ou controle equivalente definido na implementação.

Rearmar exige ação humana explícita, diagnóstico, reconciliação de tentativas pendentes e novo epoch. Nunca ocorre automaticamente após restart.

## Regras normativas

```text
KILL_SWITCH_AUTHORITY=SERVER
KILL_STATE=PERSISTED
KILL_EPOCH=MONOTONIC
KILL_DOMINATES=ARMING|GRANTS|QUEUE|RETRY|DISPATCH|ADAPTER
ADAPTER_PRE_EFFECT_CHECK=REQUIRED
ACTIVATION_PATHS_MINIMUM=2
REARM=EXPLICIT_HUMAN_ACTION
RESTART_DEFAULT=SAFE_IDLE_OR_KILLED
KILL_EVENT=AUDIT_REQUIRED
```

## Alternativas consideradas

### Botão somente no celular

Rejeitado por depender de rede, bateria e sessão do cliente.

### Flag somente em memória

Rejeitada por perder estado em restart e permitir inconsistência com filas persistidas.

### Kill apenas no adaptador

Rejeitado porque não invalida grants, filas e retries no servidor.

## Consequências

### Positivas

- contenção dominante em todos os modos;
- invalidação clara por epoch;
- ativação local mesmo sem celular;
- recovery auditável.

### Negativas e custos

- todos os pontos de dispatch precisam verificar o epoch;
- rearm exige fluxo operacional próprio;
- cancelamento não confirma ausência de efeito para tentativa já iniciada.

## Segurança, recovery e falha segura

```text
KILL_STATE_UNKNOWN=TREAT_AS_KILLED
KILL_CHECK_FAILURE=NO_EFFECT
ACTIVE_ATTEMPT_ON_KILL=RECONCILIATION_REQUIRED
PENDING_QUEUE_ON_KILL=CANCEL
GRANT_FROM_OLD_EPOCH=INVALID
RESTART=NO_REARM
KILL_SWITCH_FAILURE=CRITICAL_BLOCKER
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-16
SECONDARY_DOMAINS=DOM-01|DOM-13|DOM-14|DOM-15
HANDOFFS=H-12|H-10|H-11
REQUIREMENTS=V27-EXE-008|V27-SAF-004|V27-SAF-005|V27-SAF-007|PTM-V27-019|PTM-V27-026..028|V27-QA-001..007
DEPENDS_ON=ADR-0001|ADR-0002
```

## Critérios de aceitação

```text
GLOBAL_DOMINANT_KILL=PASS
PERSISTED_KILL_EPOCH=PASS
TWO_ACTIVATION_PATHS_REQUIRED=PASS
ADAPTER_PRE_EFFECT_CHECK=PASS
AUTOMATIC_REARM=NO
```

## Fora de escopo

- escolha da hotkey;
- hardware dedicado;
- código de sinalização;
- limite de latência numérico;
- acionamento real nesta missão.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.