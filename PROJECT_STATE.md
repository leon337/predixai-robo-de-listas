# PROJECT_STATE — PredixAI Robô de Listas

## Estado oficial

```text
REPOSITORY=leon337/predixai-robo-de-listas
MAIN_HEAD=f0faa79c157cbfeae75b620eddb9ccade6000a36
INSTALLED_VERSION=V2.4.3-R1
DAT_001_VERSION_TARGET=V2.5.0-alpha.2
STATE_REVISION=36
ACTIVE_MISSION=LEA-59
INDEPENDENT_REVIEW=LEA-60_TODO_BLOCKED
CURRENT_GATE=BUILDER_VALIDATION_DAT_001
```

A FND-003 foi aprovada, integrada no PR #71 e sincronizada localmente. A decisão
humana seguinte autorizou exclusivamente a DAT-001 em `NULL_ONLY`.

## Entrega em construção

- persistência local SQLite V1 e boundary único de escrita;
- controle otimista de versão, idempotência de comandos e outbox atômico;
- migrations SQL `up` e `down`, com checksum e rollback limitado a banco vazio;
- backup consistente, hash SHA-256, `integrity_check` e restore para destino novo;
- inventário e importação legada para staging, com ledger e reconciliação;
- fonte legada preservada e nenhuma lista autoritativa criada;
- executor Linux Mint isolado e CI cumulativo preparados.

## Validação

```text
PYTHON_COMPILEALL=PASS
GIT_DIFF_CHECK=PASS
BASH_SYNTAX=PASS
PYTEST=PENDING_DEPENDENCY_INSTALL
RUFF=PENDING_DEPENDENCY_INSTALL
MYPY=PENDING_DEPENDENCY_INSTALL
CI=PENDING_DRAFT_PR
LOCAL_LINUX_MINT_TEST=⏳ AGUARDANDO EXECUÇÃO DO LEO
LOCAL_REPORT_TXT=⏳ AGUARDANDO EXECUÇÃO DO LEO
```

Comando único após o HEAD candidato ser publicado:

```bash
./scripts/local_validate_dat_001.sh --expected-commit <HEAD_EXATO_DO_PR_DRAFT>
```

## Limites preservados

```text
MODE_MAX=NULL_ONLY
PRODUCTION_DATABASE=NO
EXISTING_REAL_DATA_MUTATION=NO
IRREVERSIBLE_MIGRATION=NO
DESTRUCTIVE_MIGRATION=NO
LEGACY_CUTOVER=NO
LST_001_AUTHORIZED=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

## Próximo gate

Concluir a validação do builder, publicar PR Draft, fixar externamente seu HEAD na
LEA-60, executar o teste Linux Mint e só então iniciar a revisão independente.
