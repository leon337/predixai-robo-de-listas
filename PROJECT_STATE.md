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
PR_DRAFT=72
VALIDATED_CODE_HEAD=390911d9bd7810c683a02337fe12722c9e0fc180
CURRENT_GATE=LOCAL_LINUX_MINT_AND_INDEPENDENT_REVIEW_LEA_60
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
PYTEST=PASS_77_TESTS_INCLUDING_PREVIOUS_53
RUFF=PASS
MYPY=PASS_12_SOURCE_FILES
CI=PASS_12_OF_12_AT_VALIDATED_CODE_HEAD
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

Executar o comando Linux Mint com o HEAD final fixado externamente, anexar o
relatório TXT e então executar uma única revisão independente na LEA-60.
