# PROJECT_STATE — PredixAI Robô de Listas

## Estado oficial

```text
REPOSITORY=leon337/predixai-robo-de-listas
MAIN_HEAD=f0faa79c157cbfeae75b620eddb9ccade6000a36
INSTALLED_VERSION=V2.4.3-R1
DAT_001_VERSION_TARGET=V2.5.0-alpha.2
STATE_REVISION=37
ACTIVE_MISSION=LEA-59_REMEDIATION
PREVIOUS_REVIEW=LEA-60_FAIL
FINAL_RETEST=LEA-62_TODO_BLOCKED
PR_DRAFT=72
REMEDIATED_CODE_HEAD=372aebc2ed3541ea0c778f5da9ab094bb9c02728
FINAL_RETEST_HEAD=READ_EXTERNALLY_FROM_PR_AND_LEA_62
CURRENT_GATE=LOCAL_LINUX_MINT_REVALIDATION_AND_FINAL_RETEST_LEA_62
```

A FND-003 permanece integrada na `main`. A DAT-001 foi revisada na LEA-60 sobre
`541a68887e7d81245e3268c85d43fdefd6167c11` e recebeu `FAIL` pelos achados
F01, F02 e F03. A remediação autorizada foi aplicada na mesma branch e no mesmo
PR Draft, sem alterar a `main`.

## Remediação LEA-60

- F01: restore usa criação exclusiva e preserva temporário preexistente;
- F02: backup/restore rejeitam symlink no destino e em componentes ancestrais;
- F03: validador exige igualdade com o HEAD remoto, inclui o commit no relatório
  e gera arquivo lateral SHA-256;
- quatro testes negativos foram adicionados;
- nenhum cutover, lista autoritativa, conexão externa ou efeito financeiro foi criado.

## Validação do builder

```text
PYTEST=PASS_81_TESTS_INCLUDING_PREVIOUS_53
RUFF=PASS
MYPY=PASS_12_SOURCE_FILES
CI=PASS_12_OF_12_AT_REMEDIATED_CODE_HEAD
LOCAL_LINUX_MINT_PREVIOUS_HEAD=PASS_77_AT_541a68887e7d81245e3268c85d43fdefd6167c11
LOCAL_LINUX_MINT_REMEDIATED_HEAD=AWAITING_LEO
LOCAL_REPORT_SHA256=AWAITING_REMEDIATED_HEAD_EXECUTION
INDEPENDENT_FINAL_RETEST=LEA-62_TODO_BLOCKED
```

Comando único após o HEAD final ser fixado externamente:

```bash
./scripts/local_validate_dat_001.sh --expected-commit <FINAL_RETEST_HEAD>
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

Fixar externamente o HEAD final após o CI documental, executar novamente o
validador Linux Mint, preservar o TXT e o arquivo `.sha256`, e então executar
um único reteste final independente na LEA-62. Nenhum merge está autorizado.
