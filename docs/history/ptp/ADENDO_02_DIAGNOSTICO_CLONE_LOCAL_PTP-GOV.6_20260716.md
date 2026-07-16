# ADENDO 02 — DIAGNÓSTICO DO CLONE LOCAL

## PTP-GOV.6 — Auditoria Mestra V2.4.3-R1

## 1. Controle

```text
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
EXPECTED_SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
LOCAL_BRANCH=main
LOCAL_HEAD=1c35534ee82d91ba34a6eab098eacf586a286b93
LOCAL_REPOSITORY_SHALLOW=false
CODE_CHANGED_BY_AUDIT=NO
APPLICATION_EXECUTED_BY_DIAGNOSTIC=NO
REAL_CLICK_EXECUTED_BY_DIAGNOSTIC=NO
```

## 2. Diagnóstico inicial

O diagnóstico local confirmou:

- diretório correto do repositório;
- branch local `main`;
- remote `origin` apontando para o repositório oficial;
- clone não superficial;
- `HEAD` e `origin/main` locais inicialmente em `1c35534ee82d91ba34a6eab098eacf586a286b93`;
- commit-base `0e2d7e98d863769be32a8bcb8b93684a61674aa3` inicialmente ausente no banco de objetos local.

O GitHub oficial continuava expondo o commit-base e o `PROJECT_STATE.md` correspondente à PTP-GOV.6. A causa foi classificada como objetos e referências remotas locais desatualizados, não ausência do commit no repositório oficial.

## 3. Estado pré-existente do worktree no diagnóstico

```text
MODIFIED=install.sh
MODIFIED=install_desktop.sh
MODIFIED=run.sh
UNTRACKED=.runtime/
UNTRACKED=backups/
UNTRACKED=reports/
```

Esses itens eram pré-existentes e não poderiam ser descartados, sobrescritos, limpos ou incluídos automaticamente na auditoria.

## 4. Fetch seguro executado

Em 2026-07-16, Leo executou somente `git fetch origin`, com captura do `HEAD` e do status antes e depois.

Resultado recebido:

```text
HEAD_BEFORE=1c35534ee82d91ba34a6eab098eacf586a286b93
HEAD_AFTER=1c35534ee82d91ba34a6eab098eacf586a286b93
ORIGIN_MAIN=0e2d7e98d863769be32a8bcb8b93684a61674aa3
EXPECTED_COMMIT_AVAILABLE=YES
LOCAL_HEAD_UNCHANGED=YES
WORKTREE_STATUS_PRESERVED=YES
```

Status registrado ao final da execução:

```text
MODIFIED=install.sh
MODIFIED=install_desktop.sh
MODIFIED=run.sh
UNTRACKED=backups/
UNTRACKED=reports/
```

A ausência de `.runtime/` no segundo status não é atribuída ao `fetch`, porque a comparação interna confirmou `WORKTREE_STATUS_PRESERVED=YES`. O diretório pode ter sido removido antes da execução pelo ciclo normal da aplicação. Nenhuma conclusão adicional é declarada sem evidência específica.

## 5. Classificação atualizada

```text
LOCAL_REMOTE_REF_STALE=RESOLVED_BY_FETCH
LOCAL_CODE_LOSS=NO_EVIDENCE
REMOTE_REPOSITORY_MISMATCH=NO
FETCH_EXECUTED=YES
FETCH_RESULT=PASS
EXPECTED_COMMIT_AVAILABLE=YES
PULL_EXECUTED=NO
CHECKOUT_EXECUTED=NO
RESET_EXECUTED=NO
RESTORE_EXECUTED=NO
CLEAN_EXECUTED=NO
LOCAL_HEAD_CHANGED=NO
WORKTREE_STATUS_CHANGED_BY_FETCH=NO
WORKTREE_PRESERVATION=PASS
```

## 6. Próxima coleta permitida

A evidência integral deve ser produzida diretamente do banco de objetos Git no commit-base, sem `checkout`, sem `worktree add` e sem executar a aplicação.

A coleta deve registrar:

1. árvore completa dos arquivos versionados;
2. totais por diretório e extensão;
3. índice AST de todos os arquivos Python no commit-base;
4. histórico completo alcançável pelo commit-base;
5. status local antes e depois;
6. confirmação de que o `HEAD` local não mudou.

## 7. Gate

```text
LOCAL_CLONE_DIAGNOSTIC=PASS
ROOT_CAUSE=STALE_LOCAL_REMOTE_OBJECTS_AND_REFS
FETCH_GATE=PASS
EXPECTED_COMMIT_GATE=PASS
OBJECT_DATABASE_AUDIT=AUTHORIZED_READ_ONLY
AUDIT_REPORT=READY_FOR_EXECUTION
AUDITORIA_MESTRA_DRAFT_COMPLETE=PENDING
LEA_10_START=BLOCKED
PTM_V2_5_ADVANCE=BLOCKED
```
