# ADR-0011 — Recibo e reconciliação multidimensional

## Controle

```text
ADR_ID=ADR-0011
CANDIDATE_ID=ADR-CAND-014
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

Uma tentativa pode produzir efeito de interface, efeito simulado, efeito financeiro, nenhum efeito ou efeito desconhecido. Um recibo do adaptador descreve observação local e não pode ser promovido a verdade global sem reconciliação.

## Decisão

Adotar registro de tentativa **antes do efeito** e reconciliação multidimensional no servidor.

A tentativa contém identidade idempotente, comando, grant, alvo, adaptador, deadline, process/boot ID, kill epoch e estado inicial. O adaptador retorna recibo com fatos observados e limitações.

A reconciliação mantém dimensões separadas:

```text
adapter_result
ui_result
simulation_result
financial_result
reconciliation_status
```

Cada dimensão usa `CONFIRMED|NO_EFFECT|UNKNOWN|NOT_APPLICABLE` e evidências próprias. `COMPLETED_*` só é emitido quando as dimensões obrigatórias para o modo estiverem reconciliadas.

`TIMEOUT` não significa ausência de efeito. `UNKNOWN_EFFECT` bloqueia retry e novas ações correlacionadas ao mesmo alvo até investigação ou reconciliação.

## Regras normativas

```text
ATTEMPT_WRITE_BEFORE_EFFECT=REQUIRED
ADAPTER_RECEIPT=LOCAL_EVIDENCE_NOT_GLOBAL_TRUTH
UI_RESULT!=FINANCIAL_RESULT
TIMEOUT!=NO_EFFECT
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
AUTOMATIC_RETRY=ONLY_AFTER_FAILED_NO_EFFECT
IDEMPOTENCY_KEY=REQUIRED
RECONCILIATION=SERVER_AUTHORITY
EVIDENCE_REFERENCE=REQUIRED_FOR_CONFIRMATION
```

## Alternativas consideradas

### Sucesso baseado apenas no retorno da biblioteca

Rejeitado por não demonstrar efeito real nem estado global.

### Um campo booleano `success`

Rejeitado por ocultar dimensões, ambiguidade e estados desconhecidos.

### Retry automático após timeout

Rejeitado pelo risco de duplicação quando o primeiro efeito ocorreu sem recibo.

## Consequências

### Positivas

- ambiguidade explícita;
- retry seguro somente com prova de ausência de efeito;
- auditoria separa UI, simulação e resultado financeiro;
- recovery após restart sem assumir resultado.

### Negativas e custos

- reconciliação pode exigir observação adicional;
- `UNKNOWN_EFFECT` pode bloquear operação até intervenção;
- mais estados e evidências precisam ser armazenados.

## Segurança, recovery e falha segura

```text
MISSING_RECEIPT=AWAIT_OR_UNKNOWN
CONTRADICTORY_EVIDENCE=UNKNOWN_EFFECT
RESTART_WITH_OPEN_ATTEMPT=RECONCILE_NOT_REDISPATCH
KILL_DURING_ATTEMPT=UNKNOWN_UNTIL_RECONCILED
DUPLICATE_IDEMPOTENCY_KEY=RETURN_EXISTING_ATTEMPT
FINANCIAL_RESULT_WITHOUT_LIVE_GATE=SECURITY_FAILURE
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-15
SECONDARY_DOMAINS=DOM-03|DOM-13|DOM-14|DOM-16
HANDOFFS=H-10|H-11|H-12
REQUIREMENTS=PTM-V27-010..018|PTM-V27-022..025|PTM-V27-030|V27-EXE-001|V27-EXE-002|V27-EXE-005..007|V27-REC-001..006
DEPENDS_ON=ADR-0002|ADR-0008|ADR-0009|ADR-0010
```

## Critérios de aceitação

```text
ATTEMPT_BEFORE_EFFECT=PASS
MULTIDIMENSIONAL_RESULTS=PASS
RECEIPT_NOT_GLOBAL_TRUTH=PASS
UNKNOWN_EFFECT_BLOCKS_RETRY=PASS
RESTART_RECONCILIATION=PASS
```

## Fora de escopo

- integração com extrato de plataforma;
- código de captura de evidência;
- regras numéricas de deadline;
- compensação financeira;
- operação real.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.