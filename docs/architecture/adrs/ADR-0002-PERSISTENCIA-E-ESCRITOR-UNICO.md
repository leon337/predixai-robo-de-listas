# ADR-0002 — Persistência relacional local e fronteira de escritor único

## Controle

```text
ADR_ID=ADR-0002
CANDIDATE_ID=ADR-CAND-002
STATUS=ACCEPTED
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
ACCEPTED_AT=2026-07-18
ACCEPTANCE_EVIDENCE=docs/history/reviews/REVISAO_CRITICA_RETESTE_03_ADRS_P0_LEA-27_20260718.md
PUBLICATION_EVIDENCE=docs/architecture/adrs/README.md#indice-p0-publicado
IMPLEMENTATION_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
```

## Contexto

A V1.0 precisa preservar listas, perfis, sessões, evidências, sinais, comandos, grants, tentativas, recibos, auditoria e recovery em um servidor local. O hardware-alvo é limitado, a implantação deve funcionar sem custo recorrente e a autoridade global é única.

## Decisão

Adotar **SQLite como persistência relacional inicial da V1.0**, acessada exclusivamente por uma camada de persistência do servidor.

A fronteira será de escritor único lógico: clientes, handlers HTTP, motores, adaptadores e tarefas internas não escrevem diretamente no banco. Eles emitem comandos de domínio para serviços que executam transações curtas e explícitas.

A configuração futura deverá habilitar `foreign_keys`, modo WAL quando validado no filesystem-alvo, timeout de lock, backup consistente e migrations versionadas. O modelo conceitual permanece portável para PostgreSQL caso critérios objetivos de escala ou concorrência sejam atingidos.

## Regras normativas

```text
V1_DATABASE=SQLITE
WRITE_AUTHORITY=SERVER_PERSISTENCE_BOUNDARY
DIRECT_CLIENT_WRITE=PROHIBITED
DIRECT_HANDLER_WRITE=PROHIBITED
TRANSACTION_SCOPE=SHORT_DOMAIN_OPERATION
FOREIGN_KEYS=REQUIRED
WAL=REQUIRED_IF_FILESYSTEM_VALIDATED
OUTBOX_PATTERN=REQUIRED_FOR_DURABLE_EVENTS
RAW_LEGACY_SOURCE=PRESERVED_IMMUTABLY
MIGRATIONS=VERSIONED_AND_REVERSIBLE_WHEN_FEASIBLE
POSTGRESQL_MIGRATION_PATH=PRESERVED
```

Eventos que precisem sobreviver a restart serão gravados na mesma transação da mudança de estado por uma outbox. Publicação e consumo não podem anteceder o commit.

## Alternativas consideradas

### JSON como persistência principal

Rejeitada por integridade fraca, concorrência limitada, dificuldade de consulta, evolução e recovery.

### PostgreSQL desde a primeira versão

Não adotada como padrão inicial por exigir serviço adicional e maior carga operacional. Permanece destino previsto quando houver múltiplos escritores físicos, acesso remoto relevante ou volume incompatível com SQLite.

### Escrita direta por cada módulo

Rejeitada por quebrar invariantes, auditoria, ordem de eventos e rollback.

## Consequências

### Positivas

- implantação local simples;
- transações e integridade referencial;
- backup em arquivo controlado;
- baixo consumo de recursos;
- caminho explícito para evolução.

### Negativas e custos

- concorrência de escrita é serializada;
- operações longas devem ocorrer fora da transação;
- WAL e backup precisam ser testados no filesystem real;
- migração futura para PostgreSQL exigirá validação formal.

## Segurança, recovery e falha segura

```text
WRITE_LOCK_TIMEOUT=FAIL_WITH_REASON_CODE
PARTIAL_TRANSACTION=ROLLBACK
OUTBOX_PUBLISH_FAILURE=RETRY_WITHOUT_DUPLICATING_STATE
BACKUP_UNVERIFIED=NOT_RECOVERY_READY
RESTORE_REQUIRES_INTEGRITY_CHECK=YES
LEGACY_IMPORT=IDEMPOTENT_AND_RECONCILED
```

Nenhuma migration, SQL físico ou importação é criada por este ADR.

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-03
SECONDARY_DOMAINS=DOM-01|DOM-15|DOM-16
HANDOFFS=H-11
REQUIREMENTS=PTM-V25-003|PTM-V25-014A..014E|V25-DB-001..005|V25-LEG-001..006|PTM-V26-023|PTM-V26-027|V26-API-001..002|PTM-V27-029
DEPENDS_ON=ADR-0001
```

## Critérios de aceitação

```text
DATABASE_TECHNOLOGY_DECIDED=PASS
SINGLE_WRITER_BOUNDARY=PASS
TRANSACTION_AND_OUTBOX_CONTRACT=PASS
BACKUP_AND_RESTORE_EXPECTATION=PASS
POSTGRESQL_EXIT_CRITERIA_REQUIRED=YES
SQL_CREATED=NO
```

## Fora de escopo

- tabelas e colunas;
- migrations;
- ORM específico;
- tuning de produção;
- importação executável do legado.

## Estado da decisão

Status `ACCEPTED`. A decisão foi aprovada pela revisão crítica independente `LEA-27` no Reteste 03 e publicada no conjunto P0. A aceitação não cria SQL, migrations ou autorização de implementação.