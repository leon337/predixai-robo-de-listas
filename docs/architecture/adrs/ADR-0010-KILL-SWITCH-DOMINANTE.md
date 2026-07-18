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
DEPENDS_ON=ADR-0001|ADR-0002
MUST_ALIGN_WITH=ADR-0008|ADR-0009|ADR-0011|ADR-0012
GOVERNS=ADR-0008|ADR-0009|ADR-0011
```

## Contexto

Qualquer ação controlada precisa poder ser interrompida antes do dispatch e durante o fluxo. O kill switch deve dominar arming, grants, filas, retries, dispatch, adaptadores e recovery, inclusive diante de conexão móvel perdida ou estado degradado.

## Decisão

Adotar kill switch global, servidor-autoritativo, persistido e associado a `kill_epoch` monotônico.

A ativação incrementa o epoch, muda o sistema para `KILLED`, invalida grants e comandos despacháveis, cancela filas sem efeito e exige reconciliação de tentativas abertas. Cada grant, tentativa e `adapter_request` carrega o epoch observado.

Dois caminhos independentes de ativação são obrigatórios:

1. comando autenticado no painel/servidor;
2. caminho local no host independente da sessão móvel.

Rearmar exige ação humana explícita, diagnóstico, reconciliação e novo epoch. Nunca ocorre automaticamente após restart.

## Semântica das relações

`ADR-0010 GOVERNS ADR-0008|ADR-0009|ADR-0011` significa que qualquer transição, dispatch ou reconciliação precisa respeitar o estado e o epoch do kill switch. Isso não cria dependência inversa em `DEPENDS_ON`.

```text
DEPENDS_ON_DAG_CYCLE_INTRODUCED=NO
KILL_GOVERNANCE_IS_NOT_DEPENDENCY_BACK_EDGE=YES
```

## Regras normativas

```text
KILL_SWITCH_AUTHORITY=SERVER
KILL_STATE=PERSISTED
KILL_EPOCH=MONOTONIC
KILL_DOMINATES=ARMING|GRANTS|QUEUE|RETRY|DISPATCH|ADAPTER|RECOVERY
ADAPTER_PRE_EFFECT_CHECK=REQUIRED
ACTIVATION_PATHS_MINIMUM=2
REARM=EXPLICIT_HUMAN_ACTION
RESTART_DEFAULT=SAFE_IDLE_OR_KILLED
KILL_EVENT=AUDIT_REQUIRED
GRANT_FROM_OLD_EPOCH=INVALIDATED_BY_KILL_EPOCH
```

## Alternativas consideradas

### Botão somente no celular

Rejeitado por depender de rede, bateria e sessão do cliente.

### Flag somente em memória

Rejeitada por perder estado em restart.

### Kill apenas no adaptador

Rejeitado porque não invalida grants, fila, retries e arming no servidor.

## Consequências

### Positivas

- contenção dominante em todos os modos;
- invalidação clara por epoch;
- ativação local independente;
- recovery auditável.

### Negativas e custos

- cada ponto de dispatch precisa verificar o epoch;
- rearm exige fluxo operacional próprio;
- kill não prova ausência de efeito em tentativa já iniciada.

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
HANDOFFS=H-10|H-11|H-12
REQUIREMENTS=V27-EXE-008|V27-SAF-004|V27-SAF-005|V27-SAF-007|PTM-V27-019|PTM-V27-026..028|V27-QA-001..007
TRACEABILITY_APPENDIX=APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md
```

## Critérios de aceitação

```text
GLOBAL_DOMINANT_KILL=PASS
PERSISTED_KILL_EPOCH=PASS
TWO_ACTIVATION_PATHS_REQUIRED=PASS
ADAPTER_PRE_EFFECT_CHECK=PASS
AUTOMATIC_REARM=NO
DEPENDENCY_AND_GOVERNANCE_SEPARATED=PASS
```

## Fora de escopo

- escolha da hotkey;
- hardware dedicado;
- código de sinalização;
- limite de latência numérico;
- acionamento real nesta missão.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.