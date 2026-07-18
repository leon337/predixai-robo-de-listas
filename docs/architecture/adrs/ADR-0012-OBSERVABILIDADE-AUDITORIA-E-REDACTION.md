# ADR-0012 — Observabilidade, auditoria append-only e redaction

## Controle

```text
ADR_ID=ADR-0012
CANDIDATE_ID=ADR-CAND-015
STATUS=ACCEPTED
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
ACCEPTED_AT=2026-07-18
ACCEPTANCE_EVIDENCE=docs/history/reviews/REVISAO_CRITICA_RETESTE_03_ADRS_P0_LEA-27_20260718.md
PUBLICATION_EVIDENCE=docs/architecture/adrs/README.md#indice-p0-publicado
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

O sistema precisa explicar a cadeia completa de lista, observação, frame, validação, extração, análise, sinal, comando, grant, alvo, tentativa, recibo e reconciliação. Logs operacionais não bastam como auditoria, e dados sensíveis não podem vazar para Git, console ou evidências.

## Decisão

Separar três produtos de observabilidade:

1. **logs estruturados**, destinados a diagnóstico operacional;
2. **métricas e alertas**, destinados a saúde e comportamento agregado;
3. **auditoria append-only**, destinada a rastreabilidade de decisões e efeitos.

Todos os domínios propagam `trace_id`; entidades críticas acrescentam IDs próprios. A auditoria usa envelope versionado, sequência, ator, evento, referências, estado anterior/novo quando aplicável, reason codes e hash do registro anterior para evidência de adulteração acidental ou posterior.

Redaction é allowlist-first: somente campos explicitamente classificados podem ser registrados. Segredos, cookies, tokens, chaves, credenciais, conteúdo sensível desnecessário e dados financeiros detalhados são omitidos ou transformados antes da saída.

## Regras normativas

```text
STRUCTURED_LOGS!=AUDIT_RECORDS
AUDIT_MODE=APPEND_ONLY
AUDIT_ENVELOPE_VERSION=REQUIRED
TRACE_ID=END_TO_END
CRITICAL_IDS=COMMAND_ID|AUTHORIZATION_ID|ATTEMPT_ID|RECEIPT_ID
REDACTION=ALLOWLIST_FIRST
SECRET_IN_LOG_OR_AUDIT=PROHIBITED
AUDIT_GAP=RECOVERY_BLOCKER
RETENTION=CLASSIFIED_BY_DATA_TYPE
EXPORT=REDACTED_AND_INTEGRITY_CHECKED
```

Categorias mínimas de auditoria: autenticação, configuração, perfil, captura, validação, análise, sinal, comando, grant, resolução de alvo, dispatch, recibo, reconciliação, kill switch, recovery e mudança de política.

## Alternativas consideradas

### Arquivo de log único

Rejeitado por misturar diagnóstico volátil com prova durável e dificultar retenção e acesso.

### Registrar payloads completos para facilitar debug

Rejeitado por aumentar risco de segredo, privacidade e exposição financeira.

### Auditoria somente para ações externas

Rejeitada porque seria impossível reconstruir por que uma ação foi permitida ou bloqueada.

## Consequências

### Positivas

- cadeia ponta a ponta reconstruível;
- provas negativas de bypass;
- retenção e acesso diferenciados;
- menor risco de vazamento por redaction centralizada.

### Negativas e custos

- volume adicional de eventos;
- taxonomia e classificação precisam de manutenção;
- hash chain não substitui armazenamento imutável externo, caso exigido futuramente.

## Segurança, recovery e falha segura

```text
SECRET_DETECTED=DROP_FIELD_AND_RAISE_SECURITY_EVENT
AUDIT_WRITE_FAILURE=BLOCK_SECURITY_CRITICAL_OPERATION
TRACE_GAP=DEGRADED_OR_BLOCKED_BY_POLICY
HASH_CHAIN_MISMATCH=INTEGRITY_ALERT
EXPORT_WITHOUT_REDACTION=REJECT
LIVE_GATE_WITHOUT_AUDIT_READY=BLOCK
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-16
SECONDARY_DOMAINS=DOM-01..DOM-15
HANDOFFS=H-01..H-12
REQUIREMENTS=PTM-V25-015A..015E|V25-SEC-001|V25-QA-001|PTM-V26-024..026|PTM-V26-028|V26-RPL-001..003|V26-SEC-001..003|PTM-V27-019|PTM-V27-026..031|V27-OBS-001..005|V27-QA-001..007
DEPENDS_ON=ADR-0001|ADR-0002|ADR-0003|ADR-0008|ADR-0010|ADR-0011
```

## Critérios de aceitação

```text
LOG_AUDIT_METRIC_SEPARATION=PASS
APPEND_ONLY_AUDIT_CONTRACT=PASS
END_TO_END_CORRELATION=PASS
ALLOWLIST_FIRST_REDACTION=PASS
AUDIT_FAILURE_FAILS_CLOSED_FOR_CRITICAL_ACTION=PASS
```

## Fora de escopo

- produto de observabilidade externo;
- dashboards e alertas concretos;
- retenções numéricas;
- armazenamento WORM;
- código de logging.

## Estado da decisão

Status `ACCEPTED`. A decisão foi aprovada pela revisão crítica independente `LEA-27` no Reteste 03 e publicada no conjunto P0. A aceitação permanece documental e arquitetural.