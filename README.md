# PredixAI Robô de Listas

> Painel operacional. A autoridade estruturada permanece em
> `PROJECT_RUNTIME_STATE.yaml`; o mapa de desenvolvimento permanece no Documento
> Mestre da Arquitetura V1.0.

## Estado atual

```text
VERSÃO_INSTALADA=V2.4.3-R1
DAT_001_VERSION_TARGET=V2.5.0-alpha.2
MAIN_HEAD=f0faa79c157cbfeae75b620eddb9ccade6000a36
MISSÃO_ATIVA=LEA-59 — DAT-001
RETESTE_PRÉ_MERGE=LEA-66 — DONE/PASS
BRANCH=leonpcsn/dat-001-durable-state-legacy-migration
PR=72
PR_MODE=DRAFT
FINAL_RETEST_HEAD=4798cea7e66ac0dd250cfd07465cdcea27430357
STATE_REVISION=39
FASE=PREMERGE_DOCUMENTATION_SYNC
GATE=AWAITING_DOCUMENTATION_SYNC_CI_THEN_MERGE_DECISION
ARQUITETURA_V1_CONGELADA=YES
MERGE_AUTORIZADO=NO
STATE_SOURCE=PROJECT_RUNTIME_STATE.yaml
```

## Campanha

| Entrega ou gate | Estado |
|---|---|
| Documento Mestre e mapa canônico | ✅ integrados |
| Requisitos, domínios, handoffs e ADRs | ✅ `218/218`, `16/16`, `12/12`, `18/18` |
| FND-001, FND-002 e FND-003 | ✅ integradas |
| DAT-001 — estado durável e migração legada | ✅ reteste pré-merge aprovado |
| LEA-66 — reteste pré-merge | ✅ `DONE/PASS` |
| PR #72 | ⏳ Draft; aguardando sincronização/CI e decisão humana |
| LST-001 | ⛔ não autorizado |

## Evidência DAT-001

```text
LOCAL_LINUX_MINT=PASS_85
CI_FINAL_HEAD=PASS_12_OF_12
INDEPENDENT_PYTEST=PASS_85
RUFF=PASS
MYPY=PASS_12_SOURCE_FILES
PR72_PREMERGE_F01=PASS
PR72_PREMERGE_F02=PASS
INDEPENDENT_DECISION=PASS
REPORT_SHA256=21bb35057bbd845370152d1a28a6c3a0db7194d7217dead9cc1af240bf6821f2
SIDECAR_MATCH=YES
NULL_ONLY=PRESERVED
```

A entrega introduz persistência SQLite local V1, escritor único, versão otimista,
comandos idempotentes, outbox atômico, migrations reversíveis, backup/restore
verificável e importação legada para staging. A remediação pré-merge rejeita
fontes simbólicas antes da normalização e serializa retries concorrentes da mesma
fonte sem duplicar staging ou ledger.

## Limites

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

## Próxima ação

Concluir a sincronização documental, confirmar o CI do novo HEAD documental e
preparar a decisão humana de merge. O PR permanece Draft e sem autorização de
merge.