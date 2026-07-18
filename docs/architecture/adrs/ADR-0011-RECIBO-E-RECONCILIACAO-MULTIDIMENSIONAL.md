# ADR-0011 — Recibo, idempotência e reconciliação multidimensional

## Controle

```text
ADR_ID=ADR-0011
CANDIDATE_ID=ADR-CAND-014
STATUS=ACCEPTED
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
ACCEPTED_AT=2026-07-18
ACCEPTANCE_EVIDENCE=docs/history/reviews/REVISAO_CRITICA_RETESTE_03_ADRS_P0_LEA-27_20260718.md
PUBLICATION_EVIDENCE=docs/architecture/adrs/README.md#indice-p0-publicado
IMPLEMENTATION_AUTHORIZED=NO
DEPENDS_ON=ADR-0002|ADR-0008|ADR-0009|ADR-0010
MUST_ALIGN_WITH=ADR-0008|ADR-0009|ADR-0010|ADR-0012
GOVERNS=ADR-0012
INDEPENDENT_REVIEW_GATE=LEA-27_CURRENT_VALID_RETEST
```

## Contexto

Uma tentativa pode produzir efeito nulo, simulado, de interface controlada, LIVE gated, nenhum efeito ou efeito desconhecido. Um recibo do adaptador é evidência local e não pode virar verdade global sem reconciliação. A idempotência precisa distinguir repetição exata de colisão divergente.

## Decisão

Registrar a tentativa antes de qualquer efeito e reconciliar dimensões separadas no servidor.

```text
adapter_result
ui_result
simulation_result
financial_result
reconciliation_status
```

Cada dimensão usa `CONFIRMED|NO_EFFECT|UNKNOWN|NOT_APPLICABLE` com evidência própria. `COMPLETED_*` só é emitido quando as dimensões obrigatórias do modo estiverem reconciliadas.

## Fingerprint canônico de idempotência

A `idempotency_key` é associada a um fingerprint canônico imutável calculado, no mínimo, sobre:

```text
command_id
command_hash
authorization_id
grant_hash
mode
target_logical_id
profile_id
profile_version
adapter_id
adapter_version
action_type
sanitized_payload_hash
context_snapshot_hash
policy_version
kill_epoch
```

Normalização, ordenação dos campos, codificação e algoritmo de hash devem ser versionados.

## Regras normativas

```text
ATTEMPT_WRITE_BEFORE_EFFECT=REQUIRED
IDEMPOTENCY_KEY=REQUIRED
CANONICAL_FINGERPRINT=REQUIRED_AND_VERSIONED
SAME_KEY_AND_SAME_CANONICAL_FINGERPRINT=RETURN_EXISTING_ATTEMPT
SAME_KEY_AND_DIFFERENT_CANONICAL_FINGERPRINT=BLOCK_CONFLICT_AND_AUDIT
DIVERGENT_KEY_REUSE=SECURITY_INTEGRITY_INCIDENT
ADAPTER_RECEIPT=LOCAL_EVIDENCE_NOT_GLOBAL_TRUTH
UI_RESULT!=FINANCIAL_RESULT
TIMEOUT!=NO_EFFECT
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
AUTOMATIC_RETRY=ONLY_AFTER_FAILED_NO_EFFECT
RECONCILIATION=SERVER_AUTHORITY
EVIDENCE_REFERENCE=REQUIRED_FOR_CONFIRMATION
```

O retorno de tentativa existente só é permitido quando chave **e** fingerprint canônico são idênticos. A mesma chave com conteúdo divergente nunca é tratada como repetição válida.

## Fluxo de deduplicação

```text
1. NORMALIZE_REQUEST
2. COMPUTE_CANONICAL_FINGERPRINT
3. LOOKUP_IDEMPOTENCY_KEY
4A. KEY_ABSENT -> CREATE_ATTEMPT_BEFORE_EFFECT
4B. KEY_PRESENT_AND_FINGERPRINT_EQUAL -> RETURN_EXISTING_ATTEMPT
4C. KEY_PRESENT_AND_FINGERPRINT_DIFFERENT -> BLOCK_CONFLICT_AND_AUDIT
```

A colisão divergente não cria nova tentativa, não chama adaptador e não modifica a tentativa anterior.

## Alternativas consideradas

### Retornar tentativa por chave sem comparar conteúdo

Rejeitada porque pode ocultar mudança de comando, grant, alvo, modo, adaptador ou payload.

### Booleano `success`

Rejeitado por ocultar dimensões e estados desconhecidos.

### Retry automático após timeout

Rejeitado pelo risco de duplicidade quando o primeiro efeito ocorreu sem recibo.

## Consequências

### Positivas

- repetição idêntica é segura e reproduzível;
- colisão divergente é bloqueada antes do efeito;
- recibo permanece evidência local;
- `UNKNOWN_EFFECT` impede duplicidade correlata;
- recovery não assume resultado.

### Negativas e custos

- fingerprint e normalização precisam de versão;
- mudanças de contrato exigem compatibilidade explícita;
- reconciliação pode exigir observação adicional.

## Segurança, recovery e falha segura

```text
MISSING_RECEIPT=AWAIT_OR_UNKNOWN
CONTRADICTORY_EVIDENCE=UNKNOWN_EFFECT
RESTART_WITH_OPEN_ATTEMPT=RECONCILE_NOT_REDISPATCH
KILL_DURING_ATTEMPT=UNKNOWN_UNTIL_RECONCILED
SAME_KEY_DIFFERENT_FINGERPRINT=BLOCK_AND_SECURITY_EVENT
FINGERPRINT_VERSION_UNKNOWN=BLOCK
FINANCIAL_RESULT_WITHOUT_LIVE_GATE=SECURITY_FAILURE
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-15
SECONDARY_DOMAINS=DOM-03|DOM-13|DOM-14|DOM-16
HANDOFFS=H-10|H-11|H-12
REQUIREMENTS=PTM-V27-010..018|PTM-V27-022..025|PTM-V27-030|V27-EXE-001|V27-EXE-002|V27-EXE-005..007|V27-REC-001..006
TRACEABILITY_APPENDIX=APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md
```

## Critérios de aceitação

```text
ATTEMPT_BEFORE_EFFECT=PASS
MULTIDIMENSIONAL_RESULTS=PASS
RECEIPT_NOT_GLOBAL_TRUTH=PASS
SAME_KEY_SAME_FINGERPRINT_RETURNS_EXISTING=PASS
SAME_KEY_DIFFERENT_FINGERPRINT_BLOCKS=PASS
DIVERGENT_REUSE_AUDITED=PASS
UNKNOWN_EFFECT_BLOCKS_RETRY=PASS
RESTART_RECONCILIATION=PASS
MAJOR_04_REMEDIATION=PASS_BUILDER
```

## Fora de escopo

- algoritmo físico de hash;
- schema de tabela;
- integração com extrato de plataforma;
- regras numéricas de deadline;
- operação real.

## Estado da decisão

Status `ACCEPTED`. A decisão foi aprovada pela revisão crítica independente `LEA-27` no Reteste 03 e publicada no conjunto P0. A aceitação é exclusivamente documental e arquitetural.