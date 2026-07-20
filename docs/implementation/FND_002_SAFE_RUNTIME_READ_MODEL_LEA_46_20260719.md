# FND-002 — Safe Runtime Read Model

## Missão

```text
BUILDER_ISSUE=LEA-46
REVIEW_ISSUE=LEA-47
PULL_REQUEST=66
MODE=NULL_ONLY
MERGE_AUTHORIZED=NO
```

## Entregas

- `GET /api/v1/runtime` sem efeito colateral;
- `GET /api/v1/audit/events` com paginação, filtro exato e allowlist;
- `GET /api/v1/diagnostics` derivado do estado real;
- nenhum comando de mutação;
- nenhum banco, SQL, migration, Android, OCR, corretora, clique real ou LIVE.

## Remediações LEA-47

```text
LEA-47-F01=REMEDIATED
LEA-47-F02=REMEDIATED
LEA-47-F03=REMEDIATED
RETEST_REQUIRED=YES
```

### F01

O read model usa `SafeServerService.state_snapshot()`, que lê estado e razão sob lock sem registrar auditoria.

### F02

O diagnóstico é calculado pelo estado:

```text
SAFE_IDLE=SAFE
DEGRADED=DEGRADED
STOPPED=STOPPED
BOOTING/UNKNOWN=UNSAFE
```

### F03

Este documento, `PROJECT_STATE.md` e `PROJECT_RUNTIME_STATE.yaml` passam a registrar a FND-002 e seu reteste.

## Política de desenvolvimento local

Cada incremento deve seguir:

```text
PULL/ATUALIZAR REPOSITÓRIO LOCAL
→ INSTALAR DEPENDÊNCIAS ISOLADAS
→ EXECUTAR TESTES
→ EXECUTAR RUFF E MYPY
→ GERAR RELATÓRIO TXT
→ CORRIGIR FALHAS
→ VERSIONAR
→ PUBLICAR
```

Sem relatório de execução produzido no Linux Mint:

```text
⏳ AGUARDANDO EXECUÇÃO DO LEO
```

## Comandos previstos para validação local

```bash
git fetch origin
git checkout leonpcsn/lea-46-fnd-002-safe-runtime-read-model
git pull --ff-only
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q tests/server
ruff check server tests/server
mypy server --ignore-missing-imports
```

A execução local não foi presumida por este documento.
