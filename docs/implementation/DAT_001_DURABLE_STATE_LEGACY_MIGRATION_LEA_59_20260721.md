# DAT-001 — Durable State and Legacy Migration

## Autoridade

```text
BUILDER_ISSUE=LEA-59
REVIEW_ISSUE=LEA-60
BASE_MAIN_SHA=f0faa79c157cbfeae75b620eddb9ccade6000a36
BRANCH=leonpcsn/dat-001-durable-state-legacy-migration
VERSION_TARGET=V2.5.0-alpha.2
MODE_MAX=NULL_ONLY
MERGE_AUTHORIZED=NO
```

Fundamento normativo: DOM-03; H-11; PTM-V25-003, PTM-V25-014A..014E,
PTM-V26-023, PTM-V26-027, PTM-V27-029, V25-DB-001..005 e
V25-LEG-001..006; ADR-0001, ADR-0002, ADR-0003 e ADR-0013.

## Modelo durável V1

`SQLitePersistence` é a única fronteira lógica de escrita. Cada mutação exige
`command_id`, `actor_id`, `expected_version`, agregado e `trace_id`. A operação usa
`BEGIN IMMEDIATE`, compara a versão, grava estado, recibo idempotente e evento de
outbox na mesma transação. Conflito de versão ou idempotência causa rollback.

Tabelas do schema V1:

- `aggregate_state`: estado versionado por agregado;
- `command_results`: recibos idempotentes de comandos;
- `outbox_events`: envelopes `v1` ordenados e publicáveis;
- `migration_runs`: ledger imutável de cada importação;
- `legacy_staging`: inventário aceito ou rejeitado sem autoridade de domínio;
- `schema_migrations`: versão e checksum do SQL aplicado.

SQLite habilita `foreign_keys`, timeout limitado e WAL quando configurado. O banco
é opcional: sem caminho configurado o servidor mantém a compatibilidade anterior e
o endpoint de saúde da persistência falha fechado.

## Migration e rollback

```text
UP=server/persistence/migrations/0001_initial.up.sql
DOWN=server/persistence/migrations/0001_initial.down.sql
CHECKSUM_DRIFT=FAIL_CLOSED
DOWN_ALLOWED_ONLY_IF_ALL_DOMAIN_TABLES_EMPTY=YES
IRREVERSIBLE_MIGRATION=NO
DESTRUCTIVE_MIGRATION_ON_EXISTING_DATA=NO
```

Rollback de dados não sobrescreve um banco existente. O restore exige backup
íntegro, SHA-256 esperado, schema conhecido e destino novo.

## Backup e restore

O backup usa a API consistente do SQLite sob lock do escritor, executa
`PRAGMA integrity_check`, calcula SHA-256 e aplica permissão local `0600`. O restore
valida hash, integridade e schema antes de copiar para um caminho ainda inexistente.
Uma falha remove somente o destino temporário que a própria operação criou.

## Legado

A fonte JSON V3/V4 é lida sem alteração, inventariada e copiada para evidência com
hash. A chave de idempotência combina hash da fonte, versão do importador e versão
do schema. Uma repetição retorna o mesmo run sem duplicar staging.

Itens válidos recebem `ACCEPTED`; duplicatas, perfis sem ID e campos sensíveis são
redigidos e recebem `REJECTED`. Qualquer divergência produz
`BLOCKED_RECONCILIATION`. Mesmo sem divergências o máximo é `CUTOVER_READY`:

```text
LEGACY_AUTHORITATIVE_COUNT=0
LEGACY_CUTOVER=NOT_AUTHORIZED
LST_001_AUTHORIZED=NO
EXISTING_REAL_DATA_MUTATION=NO
```

## Testes

As novas famílias cobrem schema/WAL/FK, atomicidade, idempotência, conflito de
versão, concorrência entre escritores, outbox, checksum, backup, hash, restore,
rollback vazio/não vazio, importação repetida, divergência, redaction, fonte
inválida e preservação integral de `NULL_ONLY`.

O CI executa toda a suíte, preservando os 53 testes anteriores, Ruff e Mypy. O
executor Linux Mint reproduz isso em worktree destacado, banco temporário e venv
isolada:

```bash
./scripts/local_validate_dat_001.sh --expected-commit <HEAD_EXATO_DO_PR_DRAFT>
```

O relatório fica em `reports/local/DAT_001_LOCAL_VALIDATION_*.txt`, ignorado pelo
Git. Sem evidência real do Leo:

```text
LOCAL_LINUX_MINT_TEST=⏳ AGUARDANDO EXECUÇÃO DO LEO
LOCAL_REPORT_TXT=⏳ AGUARDANDO EXECUÇÃO DO LEO
```

## Gates

```text
NEXT_GATE=LEA_60_INDEPENDENT_CRITICAL_REVIEW
NEXT_INCREMENT=LST-001
NEXT_INCREMENT_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
```
