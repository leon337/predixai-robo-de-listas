# Relatório de validação — DAT-001 / LEA-59

## Escopo

Persistência local V1, escritor único, eventos versionados, migrations reversíveis,
backup/restore e importação legada idempotente para staging, sob `NULL_ONLY`.

## Evidência do builder

```text
BASE_MAIN_SHA=f0faa79c157cbfeae75b620eddb9ccade6000a36
BRANCH=leonpcsn/dat-001-durable-state-legacy-migration
PYTHON_COMPILEALL=PASS
BASH_SYNTAX=PASS
GIT_DIFF_CHECK=PASS
PULL_REQUEST=72_DRAFT
VALIDATED_CODE_HEAD=390911d9bd7810c683a02337fe12722c9e0fc180
WORKFLOW_RUN_DAT_001=29796794825
PYTEST=PASS_77_TESTS_INCLUDING_PREVIOUS_53
RUFF=PASS
MYPY=PASS_12_SOURCE_FILES
CI=PASS_12_OF_12
BUILDER_VALIDATION=PASS_BY_GITHUB_ACTIONS
```

O ambiente isolado do builder não contém FastAPI, Pytest, Ruff ou Mypy e o download
do PyPI foi bloqueado. A execução completa foi comprovada pelo GitHub Actions no
HEAD indicado. A evidência Linux Mint continua obrigatória e não é inferida do CI.

## Provas previstas

- estado, recibo idempotente e outbox na mesma transação;
- concorrência resolve em uma escrita e um conflito de versão;
- checksum divergente da migration falha fechado;
- backup e restore verificam integridade e SHA-256;
- migration down é bloqueada quando há dados;
- repetição da fonte legada não duplica ledger ou staging;
- divergência bloqueia reconciliação e payload sensível é redigido;
- nenhuma importação cria estado autoritativo;
- toda capacidade externa permanece falsa.

## Limites da prova

```text
LOCAL_LINUX_MINT_TEST=⏳ AGUARDANDO EXECUÇÃO DO LEO
LOCAL_REPORT_TXT=⏳ AGUARDANDO EXECUÇÃO DO LEO
INDEPENDENT_REVIEW=NOT_EXECUTED_BY_BUILDER
MERGE=NOT_EXECUTED
LST_001_AUTHORIZED=NO
```
