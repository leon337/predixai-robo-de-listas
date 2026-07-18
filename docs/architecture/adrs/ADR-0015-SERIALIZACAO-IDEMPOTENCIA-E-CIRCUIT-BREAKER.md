# ADR-0015 — Serialização por alvo, idempotência de dispatch e circuit breaker

## Controle

```text
ADR_ID=ADR-0015
CANDIDATE_ID=ADR-CAND-013
PRIORITY=P1
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
DEPENDS_ON=ADR-0008|ADR-0009|ADR-0010|ADR-0011
MUST_ALIGN_WITH=ADR-0016|ADR-0018
```

## Contexto

O ADR-0011 define fingerprint e reconciliação, mas o executor ainda precisa de uma política explícita para impedir duas tentativas conflitantes no mesmo alvo, filas ilimitadas, retries ambíguos e falhas repetidas de adaptador.

## Decisão

Adotar **single-flight por chave de serialização de efeito**, deduplicação pelo contrato do ADR-0011, fila limitada e circuit breaker escopado por adaptador, alvo lógico e classe de ação.

```text
serialization_key=execution_channel|target_logical_id|target_identity_hash|action_conflict_class
breaker_key=adapter_id|adapter_version|target_logical_id|action_conflict_class
```

Somente uma tentativa capaz de produzir efeito pode permanecer em `DISPATCHING|AWAITING_RECEIPT|RECONCILING` por `serialization_key`. Ações comprovadamente não conflitantes exigem classificação versionada e teste específico.

## Circuit breaker

```text
CLOSED=opera dentro dos limites
OPEN=bloqueia novos dispatches
HALF_OPEN=permite somente probe explicitamente seguro e sem efeito ou validação controlada
KILLED=dominado pelo kill switch; não é estado recuperável automaticamente
```

A transição para `HALF_OPEN` não pode usar ação financeira real nem ação física ambígua como probe. Reabertura exige critérios, janela e contagens versionados; valores numéricos pertencem ao ADR-0017 e ao benchmark.

## Regras normativas

```text
EFFECT_CAPABLE_SINGLE_FLIGHT=REQUIRED
SERIALIZATION_KEY=VERSIONED_AND_AUDITABLE
QUEUE_BOUND=REQUIRED
QUEUE_OVERFLOW=BLOCK_WITH_REASON_CODE
IDEMPOTENCY_CONTRACT=ADR_0011
DIVERGENT_KEY_REUSE=BLOCK_AND_SECURITY_EVENT
RETRY_ELIGIBLE_RESULT=FAILED_NO_EFFECT_ONLY
TIMEOUT_RETRY=PROHIBITED
UNKNOWN_EFFECT_RETRY=PROHIBITED
OPEN_ATTEMPT_AFTER_RESTART=RECONCILE_NOT_REDISPATCH
CIRCUIT_BREAKER_SCOPE=ADAPTER|TARGET|ACTION_CONFLICT_CLASS
BREAKER_OPEN=NO_NEW_EFFECT_CAPABLE_DISPATCH
HALF_OPEN_EFFECTFUL_PROBE=PROHIBITED
KILL_SWITCH_DOMINATES_BREAKER_AND_QUEUE=YES
LIVE_REARM_AFTER_BREAKER=EXPLICIT_HUMAN_GATE_REQUIRED
```

## Concorrência

- aquisição da chave ocorre antes da tentativa ganhar despachabilidade;
- disputa usa versão do agregado e retorna conflito auditável;
- a chave não é liberada por timeout isolado;
- liberação ocorre após reconciliação terminal ou decisão explícita de recovery;
- `UNKNOWN_EFFECT` mantém bloqueio correlato até resolução.

## Alternativas consideradas

### Fila global única

Não adotada como única estratégia porque reduz paralelismo seguro entre alvos independentes, embora possa existir como fallback conservador.

### Paralelismo livre com dedupe posterior

Rejeitado porque deduplicação depois do efeito não impede conflito físico ou financeiro.

### Circuit breaker global

Rejeitado como padrão por bloquear todo o sistema devido a uma falha localizada. Kill switch permanece global e dominante.

### Retry automático após timeout

Rejeitado porque timeout não prova ausência de efeito.

## Consequências

### Positivas

- conflitos são bloqueados antes do efeito;
- falha repetida de adaptador reduz capacidade automaticamente;
- filas permanecem limitadas;
- retry exige prova explícita de nenhum efeito;
- kill switch continua dominante.

### Negativas e custos

- exige chave de conflito e classificação de ações;
- pode reduzir throughput;
- recovery de `UNKNOWN_EFFECT` pode demandar intervenção;
- circuit breaker precisa de métricas e testes de transição.

## Segurança, recovery e falha segura

```text
SERIALIZATION_KEY_UNKNOWN=USE_MORE_CONSERVATIVE_SCOPE_OR_BLOCK
LOCK_LOST=BLOCK_AND_RECONCILE
BREAKER_STATE_UNKNOWN=OPEN
QUEUE_STATE_CORRUPT=KILL_OR_SAFE_IDLE
ADAPTER_REPEATED_FAILURE=OPEN_CIRCUIT
TARGET_IDENTITY_CHANGE=INVALIDATE_QUEUE_AND_BLOCK
KILL_EPOCH_CHANGE=CANCEL_PENDING_AND_BLOCK
RESTART=SAFE_IDLE_AND_RECONCILIATION
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-15
SECONDARY_DOMAINS=DOM-13|DOM-14|DOM-16
HANDOFFS=H-10|H-11|H-12
DEFERRED_REQUIREMENTS_FROM_P0_APPENDIX=V27-SAF-002..003
DEFERRED_REQUIREMENT_COUNT=2
COMPLEMENTARY_REQUIREMENTS=PTM-V27-010..019|PTM-V27-022..025|PTM-V27-030..031|V27-EXE-001..002|V27-EXE-005..008|V27-REC-001..006|V27-QA-002..007
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
TRACEABILITY_APPENDIX=docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_ADRS_P1_P2_LEA-30_20260718.md
```

## Critérios de aceitação

```text
SINGLE_FLIGHT_BY_EFFECT_SCOPE=PASS_BUILDER
BOUNDED_QUEUE=PASS_BUILDER
FAILED_NO_EFFECT_ONLY_RETRY=PASS_BUILDER
TIMEOUT_AND_UNKNOWN_NO_RETRY=PASS_BUILDER
SCOPED_CIRCUIT_BREAKER=PASS_BUILDER
HALF_OPEN_EFFECTFUL_PROBE_BLOCKED=PASS_BUILDER
KILL_SWITCH_DOMINANCE=PASS_BUILDER
DEFERRED_REQUIREMENTS_RECONCILED=2/2
INDIVIDUAL_TRACEABILITY=PASS_BUILDER_REMEDIATED
NUMERIC_BREAKER_LIMITS_DEFINED=NO
```

## Fora de escopo

- implementação de lock ou fila;
- valores numéricos;
- biblioteca de circuit breaker;
- testes runtime;
- operação LIVE.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW` até `LEA-31=PASS`, autorização humana de merge e confirmação pós-merge.