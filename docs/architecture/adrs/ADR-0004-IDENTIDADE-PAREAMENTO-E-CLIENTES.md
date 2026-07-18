# ADR-0004 — Identidade, pareamento e autoridade de clientes

## Controle

```text
ADR_ID=ADR-0004
CANDIDATE_ID=ADR-CAND-005
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

O painel móvel precisa operar de forma privada na rede autorizada, identificar dispositivo e operador, sobreviver a reconexões e permitir revogação. Presença do cliente não pode equivaler a autorização de comando ou sessão LIVE.

## Decisão

Adotar pareamento local explícito e revogável entre servidor e dispositivo.

O servidor gera desafio curto, de uso único e com expiração. O dispositivo apresenta o desafio por canal local autorizado e registra uma chave pública ou segredo de dispositivo derivado, nunca uma credencial de produção externa. Após o pareamento, sessões usam tokens curtos e renováveis vinculados a `device_id`, `operator_id`, escopo e versão de revogação.

O servidor mantém a autoridade de identidade, papéis, revogação e presença. O cliente mantém apenas credenciais locais mínimas e snapshots temporários.

## Regras normativas

```text
PAIRING=LOCAL_EXPLICIT_ONE_TIME_CHALLENGE
PAIRING_EXPIRATION=REQUIRED
DEVICE_IDENTITY=SERVER_REGISTERED_AND_REVOCABLE
OPERATOR_IDENTITY=SEPARATE_FROM_DEVICE
SESSION_TOKEN=SHORT_LIVED_SCOPED
REFRESH=ROTATABLE_AND_REVOCABLE
CLIENT_STATE=LOCAL_VIEW
PRESENCE!=AUTHORIZATION_GRANT
DISCONNECT=NO_AUTOMATIC_REARM
LOST_DEVICE=SERVER_REVOCATION_REQUIRED
```

Papéis iniciais devem distinguir ao menos leitura operacional, operação controlada e administração. A política de autorização final permanece no DOM-13.

## Alternativas consideradas

### Login único compartilhado

Rejeitado por eliminar rastreabilidade individual e revogação por dispositivo.

### Confiança automática por estar na mesma rede

Rejeitada porque localização de rede não prova identidade nem autorização.

### OAuth externo obrigatório

Não adotado na V1.0 por criar dependência de internet e serviço de terceiros. Pode ser integrado posteriormente sem alterar a autoridade local.

## Consequências

### Positivas

- operação privada e offline-capable;
- revogação por dispositivo e operador;
- auditoria de ações humanas;
- reconexão sem elevar autoridade do cliente.

### Negativas e custos

- fluxo de recuperação de dispositivo precisa ser definido;
- segredos locais exigem armazenamento seguro do navegador/sistema;
- expiração e rotação aumentam complexidade de sessão.

## Segurança, recovery e falha segura

```text
PAIRING_CODE_REUSE=REJECT
EXPIRED_CHALLENGE=REJECT
REVOKED_DEVICE=SESSION_TERMINATED
TOKEN_SCOPE_MISMATCH=REJECT
DEVICE_CLOCK=NOT_AUTHORITY
SERVER_RESTART=SESSION_REVALIDATION_REQUIRED
CLIENT_RECONNECT=SNAPSHOT_AND_SEQUENCE_RECONCILIATION
```

Nenhum token, cookie ou segredo será versionado no Git.

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-05
SECONDARY_DOMAINS=DOM-01|DOM-02|DOM-13|DOM-16
HANDOFFS=H-01|H-12
REQUIREMENTS=PTM-V25-008|PTM-V25-009|PTM-V27-020|V25-CFG-001..004|V27-AUT-001..006
DEPENDS_ON=ADR-0001|ADR-0003
```

## Critérios de aceitação

```text
DEVICE_AND_OPERATOR_SEPARATED=PASS
PAIRING_REVOCABLE=PASS
SESSION_SCOPED=PASS
CLIENT_NOT_GLOBAL_AUTHORITY=PASS
PRESENCE_NOT_GRANT=PASS
```

## Fora de escopo

- provedor OAuth;
- biometria;
- cadastro público;
- credenciais de corretora ou plataforma externa;
- código de autenticação.

## Estado da decisão

Status `ACCEPTED`. A decisão foi aprovada pela revisão crítica independente `LEA-27` no Reteste 03 e publicada no conjunto P0. A aceitação não autoriza código de autenticação, credenciais externas ou sessão LIVE.