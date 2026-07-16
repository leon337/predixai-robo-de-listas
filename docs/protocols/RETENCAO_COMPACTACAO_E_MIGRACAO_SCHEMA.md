# Retenção, Compactação e Migração de Schema

## Princípios

- documentos vivos devem permanecer curtos e atuais;
- históricos são imutáveis;
- correções históricas usam adendo;
- evidências grandes usam índice e ponteiro verificável;
- bootstrap não lê todo o histórico;
- mudança de schema exige migração explícita.

## Documentos vivos

Conjunto mínimo:

1. instruções permanentes;
2. `PROJECT_RUNTIME_STATE.yaml`;
3. `PROJECT_STATE.md`;
4. tronco multichat;
5. Skills e protocolo de memória;
6. documento da missão ativa.

## Histórico

- checkpoints, reviews, handoffs e testes concluídos vão para `docs/history/`;
- snapshots não são reescritos;
- divergência posterior gera adendo com referência ao documento original;
- um índice deve apontar para evidências canônicas.

## Compactação

Compactar quando:

- documento vivo repetir histórico;
- bootstrap exigir mais de seis fontes iniciais;
- roadmap resumido exceder sua função operacional;
- estado concluído permanecer em instrução permanente;
- múltiplos adendos puderem ser consolidados sem reescrever evidência.

A compactação deve preservar links, hashes, gates e decisões.

## Compatibilidade

O manifesto contém `schema_version`. Leitores devem:

1. validar versão suportada;
2. recusar avanço automático em versão desconhecida;
3. executar migração documentada;
4. preservar `transition_id` em migração parcial;
5. incrementar `state_revision` somente após consolidação.

## Migração de schema

Cada migração deve registrar:

```text
FROM_SCHEMA_VERSION=
TO_SCHEMA_VERSION=
MIGRATION_ID=
EXPECTED_STATE_REVISION=
RESULTING_STATE_REVISION=
BACKWARD_COMPATIBLE=YES|NO
ROLLBACK_DEFINED=YES|NO
MIGRATION_STATUS=PLANNED|IN_PROGRESS|PARTIAL|COMPLETE|FAILED
```

Schema incompatível bloqueia escrita:

```text
EXECUTION_STATUS=BLOCKED_BY_SCHEMA_MISMATCH
AUTOMATIC_ADVANCE=NO
```

## Gates

```text
BOOTSTRAP_MINIMAL_READ_SET=PASS
STATE_COMPACTION_POLICY=PASS
SCHEMA_MIGRATION_POLICY=PASS
FULL_HISTORY_READ_ON_START=NO
```