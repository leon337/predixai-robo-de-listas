# ADR-0013 — Migrations, compatibilidade e importação idempotente do legado

## Controle

```text
ADR_ID=ADR-0013
CANDIDATE_ID=ADR-CAND-003
PRIORITY=P1
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
DEPENDS_ON=ADR-0002
MUST_ALIGN_WITH=ADR-0001|ADR-0003|ADR-0012
```

## Contexto

O legado preserva dados em JSON sem integridade relacional suficiente para se tornar a autoridade final. A V1.0 adotou SQLite e escritor único, mas ainda precisa decidir como transformar, validar, reconciliar e cortar para o novo modelo sem perder a origem, duplicar registros ou impedir rollback.

## Decisão

Adotar um **pipeline versionado, idempotente e auditável de migração**, separado do runtime normal e executado somente por missão futura autorizada.

Cada execução terá `migration_run_id`, hash da fonte, versão do importador, versão do schema de destino, estado, contagens, divergências e referências de backup. A origem bruta será preservada imutavelmente.

```text
INVENTORY
-> SOURCE_BACKUP_VERIFIED
-> STAGING_TRANSFORM
-> VALIDATE
-> RECONCILE
-> CUTOVER_READY
-> CUTOVER
-> OBSERVE
-> COMPLETE
```

Qualquer falha antes do cutover retorna para estado bloqueado sem promover dados. Falha após cutover aciona rollback ou restauração conforme o plano validado para a migration específica.

## Regras normativas

```text
LEGACY_SOURCE=IMMUTABLE_EVIDENCE
MIGRATION_EXECUTION=SEPARATE_AUTHORIZED_MISSION
MIGRATION_LEDGER=REQUIRED
IMPORT_IDEMPOTENCY_KEY=SOURCE_HASH|IMPORTER_VERSION|TARGET_SCHEMA_VERSION
SAME_KEY_SAME_INPUT=RETURN_EXISTING_RESULT
SAME_KEY_DIVERGENT_INPUT=BLOCK_AND_AUDIT
STAGING_BEFORE_AUTHORITY=REQUIRED
RECONCILIATION_BEFORE_CUTOVER=REQUIRED
BACKUP_AND_RESTORE_TEST_BEFORE_CUTOVER=REQUIRED
CUTOVER_AUTHORITY=SERVER_SINGLE_WRITER
PARTIAL_IMPORT=NOT_AUTHORITATIVE
SCHEMA_COMPATIBILITY=EXPLICIT_AND_VERSIONED
EXPAND_MIGRATE_CONTRACT=DEFAULT_EVOLUTION_PATTERN
DESTRUCTIVE_CHANGE=SEPARATE_GATE
ROLLBACK_OR_FORWARD_REPAIR_PLAN=REQUIRED
```

O cutover deve registrar qual fonte, importador, schema e relatório foram aprovados. Reexecução não pode duplicar entidades nem apagar divergências anteriores.

## Compatibilidade

- leitores e escritores declaram versão de schema suportada;
- mudanças aditivas precedem remoções;
- dados antigos são transformados em staging antes de ganhar autoridade;
- incompatibilidade desconhecida bloqueia a promoção;
- remoção de campo exige prova de ausência de consumidor ou migração concluída.

## Alternativas consideradas

### Importar diretamente durante a inicialização

Rejeitada porque mistura boot, transformação, recuperação e autoridade, dificultando rollback e diagnóstico.

### Converter o JSON uma única vez sem ledger

Rejeitada porque não prova idempotência, versão, contagens ou reconciliação.

### Manter JSON e SQLite como autoridades concorrentes

Rejeitada por criar split-brain documental e múltiplos escritores lógicos.

## Consequências

### Positivas

- origem preservada e auditável;
- importação repetível sem duplicação;
- cutover condicionado a backup, restore e reconciliação;
- compatibilidade explícita entre versões;
- rollback ou reparo com evidência.

### Negativas e custos

- exige staging, ledger e relatórios;
- aumenta o trabalho de testes de restore;
- mudanças destrutivas ficam mais lentas;
- cada importador precisa de versão estável.

## Segurança, recovery e falha segura

```text
SOURCE_HASH_MISMATCH=BLOCK
BACKUP_UNVERIFIED=BLOCK_CUTOVER
RESTORE_TEST_FAILED=BLOCK_CUTOVER
RECONCILIATION_MISMATCH=BLOCK_CUTOVER
UNKNOWN_SCHEMA_VERSION=BLOCK
PARTIAL_WRITE=ROLLBACK_TRANSACTION
POST_CUTOVER_FAILURE=FOLLOW_APPROVED_ROLLBACK_OR_FORWARD_REPAIR
MIGRATION_LOG_WITH_SECRET=REDACT_AND_FAIL_GATE
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-03
SECONDARY_DOMAINS=DOM-01|DOM-16
HANDOFFS=H-11
REQUIREMENTS=PTM-V25-001..006|PTM-V25-014A..014E|PTM-V25-016|V25-DB-001..005|V25-LEG-001..006|PTM-V26-023|PTM-V26-027|PTM-V27-029
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
```

## Critérios de aceitação

```text
IMMUTABLE_SOURCE_PRESERVATION=PASS_BUILDER
IDEMPOTENT_IMPORT_CONTRACT=PASS_BUILDER
MIGRATION_LEDGER=PASS_BUILDER
STAGING_AND_RECONCILIATION=PASS_BUILDER
BACKUP_RESTORE_BEFORE_CUTOVER=PASS_BUILDER
COMPATIBILITY_STRATEGY=PASS_BUILDER
SQL_CREATED=NO
MIGRATION_EXECUTED=NO
```

## Fora de escopo

- SQL, tabelas e colunas;
- código de importação;
- execução de backup ou restore;
- volume final e janela de corte;
- migration física.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW` até `LEA-31=PASS`, autorização humana de merge e confirmação pós-merge.