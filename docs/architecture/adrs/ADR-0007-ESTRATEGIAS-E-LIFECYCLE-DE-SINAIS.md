# ADR-0007 — Estratégias versionadas e lifecycle de sinais

## Controle

```text
ADR_ID=ADR-0007
CANDIDATE_ID=ADR-CAND-009
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

Resultados de análise não são sinais prontos. Estratégias precisam aplicar regras versionadas, arbitrar candidatos, preservar evidências, controlar validade e impedir que um sinal se transforme automaticamente em comando.

## Decisão

Adotar um registro de estratégias imutáveis e versionadas. Cada avaliação vincula `strategy_id`, `strategy_version`, `analysis_snapshot_id`, configuração resolvida e contexto de agenda.

O fluxo normativo será:

```text
ANALYSIS_RESULTS -> STRATEGY_EVALUATION -> CANDIDATES -> ARBITRATION -> SIGNAL
```

Um sinal é um artefato imutável com fingerprint determinístico, direção, ativo/contexto, horizonte, validade, evidências, contradições, caps, reason codes e estado de lifecycle.

Estados canônicos:

```text
WAIT|CANDIDATE|ACTIVE|EXPIRED|INVALIDATED|SUPERSEDED|BLOCKED
```

Somente `ACTIVE`, não expirado, não supersedido e elegível pode ser apresentado ao DOM-13. Ainda assim, sinal não cria comando, grant, alvo ou dispatch.

## Regras normativas

```text
STRATEGY=VERSIONED_IMMUTABLE_DEFINITION
SIGNAL_FINGERPRINT=DETERMINISTIC
SIGNAL_TTL=REQUIRED
ARBITRATION=EXPLICIT
CONTRADICTIONS=PRESERVED
SUPERSESSION=RECORDED
SIGNAL!=COMMAND
SIGNAL_AUTOEXECUTION=PROHIBITED_BY_BOUNDARY
UNKNOWN_OR_DEGRADED=WAIT_OR_BLOCK
```

## Alternativas consideradas

### Regra de estratégia embutida nos motores

Rejeitada por misturar análise e decisão estratégica, dificultando versão e comparação.

### Sinal mutável atualizado no lugar

Rejeitado por destruir histórico e dificultar auditoria de expiração ou supersessão.

### Primeiro candidato elegível vence

Rejeitado por tornar arbitragem implícita e dependente da ordem de execução.

## Consequências

### Positivas

- comparação entre versões de estratégia;
- sinais reproduzíveis por fingerprint;
- expiração e supersessão explícitas;
- separação forte entre inteligência e execução.

### Negativas e custos

- múltiplos artefatos por avaliação;
- arbitragem precisa de regras documentadas;
- estratégias antigas devem permanecer identificáveis para replay.

## Segurança, recovery e falha segura

```text
EXPIRED_SIGNAL=NOT_COMMAND_ELIGIBLE
SUPERSEDED_SIGNAL=NOT_COMMAND_ELIGIBLE
MISSING_EVIDENCE=BLOCKED
QUALITY_CAP_BELOW_POLICY=WAIT_OR_BLOCKED
RESTART=SIGNAL_STATE_RELOADED_WITH_TTL_RECHECK
DIRECT_ADAPTER_CALL=BLOCK
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-12
SECONDARY_DOMAINS=DOM-04|DOM-09|DOM-11|DOM-13|DOM-16
HANDOFFS=H-07|H-08
REQUIREMENTS=PTM-V26-019..022|V26-STR-001..004|V26-SIG-001..008
DEPENDS_ON=ADR-0006
```

## Critérios de aceitação

```text
STRATEGY_VERSIONING=PASS
CANDIDATE_SIGNAL_SEPARATION=PASS
SIGNAL_FINGERPRINT_AND_TTL=PASS
ARBITRATION_EXPLICIT=PASS
SIGNAL_AUTOEXECUTION_BLOCKED=PASS
```

## Fora de escopo

- regras numéricas de entrada;
- promessa de rentabilidade;
- implementação dos motores;
- criação de comando;
- qualquer operação real.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.