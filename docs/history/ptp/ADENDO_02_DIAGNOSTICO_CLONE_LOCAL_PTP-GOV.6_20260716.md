# ADENDO 02 — DIAGNÓSTICO DO CLONE LOCAL

## PTP-GOV.6 — Auditoria Mestra V2.4.3-R1

## 1. Controle

```text
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
EXPECTED_SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
LOCAL_BRANCH=main
LOCAL_HEAD=1c35534ee82d91ba34a6eab098eacf586a286b93
LOCAL_ORIGIN_MAIN=1c35534ee82d91ba34a6eab098eacf586a286b93
LOCAL_REPOSITORY_SHALLOW=false
LOCAL_EXPECTED_COMMIT_AVAILABLE=NO
CODE_CHANGED_BY_AUDIT=NO
APPLICATION_EXECUTED_BY_DIAGNOSTIC=NO
REAL_CLICK_EXECUTED_BY_DIAGNOSTIC=NO
```

## 2. Evidência recebida

O diagnóstico local confirmou:

- diretório correto do repositório;
- branch local `main`;
- remote `origin` apontando para o repositório oficial;
- clone não superficial;
- `HEAD` e `origin/main` locais em `1c35534ee82d91ba34a6eab098eacf586a286b93`;
- commit-base `0e2d7e98d863769be32a8bcb8b93684a61674aa3` ausente no banco de objetos local.

O GitHub oficial continua expondo o commit-base e o `PROJECT_STATE.md` correspondente à PTP-GOV.6. Portanto, a causa é referência/objetos remotos locais desatualizados, não ausência do commit no repositório oficial.

## 3. Estado pré-existente do worktree

```text
MODIFIED=install.sh
MODIFIED=install_desktop.sh
MODIFIED=run.sh
UNTRACKED=.runtime/
UNTRACKED=backups/
UNTRACKED=reports/
```

Esses itens são pré-existentes e não podem ser descartados, sobrescritos, limpos ou incluídos automaticamente na auditoria.

## 4. Classificação

```text
LOCAL_REMOTE_REF_STALE=CONFIRMED
LOCAL_CODE_LOSS=NO_EVIDENCE
REMOTE_REPOSITORY_MISMATCH=NO
FETCH_REQUIRED=YES
PULL_REQUIRED=NO
CHECKOUT_REQUIRED=NO
RESET_REQUIRED=NO
CLEAN_REQUIRED=NO
WORKTREE_PRESERVATION=MANDATORY
```

## 5. Próxima operação permitida

Apenas atualizar os objetos e referências remotas:

```text
git fetch --prune origin
```

A operação não deve ser acompanhada por `pull`, `merge`, `rebase`, `checkout`, `reset`, `restore` ou `clean`.

Após o fetch, confirmar:

```text
EXPECTED_COMMIT_AVAILABLE=YES
LOCAL_HEAD_UNCHANGED=1c35534ee82d91ba34a6eab098eacf586a286b93
WORKTREE_PREEXISTING_CHANGES_PRESERVED=YES
```

Somente então o relatório integral deve ser executado em worktree temporário destacado no commit-base.

## 6. Gate

```text
LOCAL_CLONE_DIAGNOSTIC=PASS
ROOT_CAUSE=STALE_LOCAL_REMOTE_OBJECTS_AND_REFS
AUDIT_REPORT=NOT_STARTED
AUDITORIA_MESTRA_DRAFT_COMPLETE=PENDING
LEA_10_START=BLOCKED
PTM_V2_5_ADVANCE=BLOCKED
```
