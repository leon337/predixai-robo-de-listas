# Checkpoint DAT-001 — Remediação LEA-62-F01

## Identidade

```text
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=72
BASE_MAIN_SHA=f0faa79c157cbfeae75b620eddb9ccade6000a36
PREVIOUS_RETEST=LEA-62
PREVIOUS_RETEST_HEAD=b7260fe1ad06363db3f0d4de17cc998a2fbadf2c
PREVIOUS_DECISION=FAIL
BUILDER_ISSUE=LEA-59
REMEDIATION=LEA-62-F01
REMEDIATED_CODE_HEAD=6d9091ab7582f1efb71698fc4daf25c4ba3f1355
FINAL_RETEST=LEA-63
FINAL_RETEST_HEAD=READ_EXTERNALLY_FROM_PR_AND_LEA_63
MODE_MAX=NULL_ONLY
```

O SHA final não é embutido neste documento porque o commit documental não pode
referenciar o próprio hash. As autoridades externas são o PR #72 e a LEA-63.

## Correção

O backup não abre mais um caminho temporário previamente verificado. O snapshot
SQLite consistente é produzido em memória, validado, serializado e materializado
uma única vez no destino novo com criação exclusiva. A abertura usa
`O_CREAT | O_EXCL` e, quando disponível, `O_NOFOLLOW`.

A limpeza em caso de falha só remove o inode criado pelo próprio processo,
evitando excluir um arquivo que tenha substituído o caminho durante uma corrida.

## Evidência do builder

```text
PYTEST=PASS_82_INCLUDING_PREVIOUS_81
NEW_NEGATIVE_RACE_TEST=PASS
RUFF=PASS
MYPY=PASS_12_SOURCE_FILES
CI_AT_REMEDIATED_CODE_HEAD=PASS_12_OF_12
PRODUCTION_DATABASE=NO
EXISTING_REAL_DATA_MUTATION=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
LST_001_AUTHORIZED=NO
```

## Gate

O commit documental final deve receber os 12 workflows verdes e ser validado no
Linux Mint com TXT e `.sha256`. Depois, a LEA-63 executará um reteste
independente exclusivo. O PR permanece Draft; merge e LST-001 continuam
bloqueados.
