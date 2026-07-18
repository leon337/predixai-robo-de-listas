# ADR-0003 — Contratos REST, eventos e versionamento

## Controle

```text
ADR_ID=ADR-0003
CANDIDATE_ID=ADR-CAND-004
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

O celular será painel operacional e o servidor manterá autoridade global. O sistema precisa transportar comandos, consultas, snapshots, mudanças de estado e alertas sem transformar conexão de cliente em autoridade ou depender de canal bidirecional permanente.

## Decisão

Adotar contratos HTTP JSON versionados em `/api/v1` para comandos e consultas, combinados com **Server-Sent Events (SSE)** para eventos servidor→cliente e snapshot REST como fallback de reconexão.

Comandos usam `POST` com identificador idempotente, ator, versão esperada e `trace_id`. Consultas usam `GET`. Atualizações integrais ou parciais usam semântica explícita, sem inferência por ausência de campo.

Eventos usam envelope canônico versionado, sequência monotônica por stream, identidade de processo e referência ao estado persistido. O cliente reconecta informando a última sequência; lacuna, retenção expirada ou mudança de processo exige snapshot.

## Regras normativas

```text
API_STYLE=REST_JSON
API_MAJOR_VERSION=/api/v1
SERVER_EVENT_CHANNEL=SSE
RECONNECT_FALLBACK=AUTHORITATIVE_SNAPSHOT
COMMAND_IDEMPOTENCY_KEY=REQUIRED
OPTIMISTIC_VERSION=REQUIRED_FOR_MUTATION
EVENT_ENVELOPE_VERSION=REQUIRED
EVENT_SEQUENCE=MONOTONIC_PER_STREAM
EVENT_AFTER_COMMIT=REQUIRED
CLIENT_ACK=NOT_GLOBAL_STATE_AUTHORITY
BREAKING_CHANGE=NEW_MAJOR_VERSION
```

Envelope mínimo de evento:

```text
event_id|event_type|event_version|occurred_at_utc|sequence|process_id|trace_id|aggregate_id|aggregate_version|payload
```

## Alternativas consideradas

### WebSocket para tudo

Não adotado como padrão por aumentar estado de conexão e complexidade de recovery. Pode ser reconsiderado por ADR futuro para casos comprovadamente bidirecionais e de baixa latência.

### Polling periódico como canal principal

Rejeitado por latência, consumo e dificuldade de representar sequência. Mantido apenas como fallback operacional simples.

### Eventos sem persistência/outbox

Rejeitados por permitir evento visível antes do commit ou perda após restart.

## Consequências

### Positivas

- protocolo simples para navegador e celular;
- comandos continuam auditáveis por HTTP;
- reconexão determinística por sequência e snapshot;
- separação clara entre mutação e notificação.

### Negativas e custos

- SSE é unidirecional;
- retenção de eventos e snapshot precisam ser coordenados;
- versões antigas exigem política explícita de compatibilidade.

## Segurança, recovery e falha segura

```text
MISSING_IDEMPOTENCY_KEY=MUTATION_REJECTED
STALE_EXPECTED_VERSION=CONFLICT
EVENT_GAP=SNAPSHOT_REQUIRED
PROCESS_ID_CHANGED=PREVIOUS_STREAM_INVALIDATED
UNAUTHORIZED_CLIENT=NO_EVENT_STREAM
SENSITIVE_FIELD=REDACT_OR_OMIT
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-01|DOM-03
SECONDARY_DOMAINS=DOM-05|DOM-16
HANDOFFS=H-01..H-12
REQUIREMENTS=V25-SRV-001..004|PTM-V26-023|PTM-V26-027|V26-API-001..002|V27-OBS-001..005
DEPENDS_ON=ADR-0001|ADR-0002
```

## Critérios de aceitação

```text
COMMAND_QUERY_SEPARATION=PASS
EVENT_AFTER_COMMIT=PASS
RECONNECT_AND_SNAPSHOT_CONTRACT=PASS
VERSIONING_POLICY=PASS
CLIENT_NOT_AUTHORITY=PASS
```

## Fora de escopo

- framework HTTP;
- código de endpoints;
- OpenAPI final;
- limites numéricos de retenção;
- infraestrutura de mensageria externa.

## Estado da decisão

Status `ACCEPTED`. A decisão foi aprovada pela revisão crítica independente `LEA-27` no Reteste 03 e publicada no conjunto P0. A aceitação é arquitetural e não autoriza implementação de endpoints ou runtime.