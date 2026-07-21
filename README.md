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
RETESTE_PRÉ_MERGE=LEA-66 — PENDENTE
BRANCH=leonpcsn/dat-001-durable-state-legacy-migration
PR=72
PR_MODE=DRAFT
REMEDIATION_CODE_HEAD=508748322205bae8c1372a3e6af7504bbffec703
FINAL_RETEST_HEAD=EXTERNAL_GITHUB_PR_AND_LINEAR_LEA_66
STATE_REVISION=38
FASE=PREMERGE_REMEDIATION
GATE=AWAITING_LOCAL_REVALIDATION_THEN_LEA_66
ARQUITETURA_V1_CONGELADA=YES
MERGE_AUTORIZADO=NO
SNAPSHOT_AT=2026-07-21T08:57:00Z
STATE_SOURCE=PROJECT_RUNTIME_STATE.yaml
```

## Campanha

| Entrega ou gate | Estado |
|---|---|
| Documento Mestre e mapa canônico | ✅ integrados |
| Requisitos, domínios, handoffs e ADRs | ✅ `218/218`, `16/16`, `12/12`, `18/18` |
| FND-001, FND-002 e FND-003 | ✅ integradas |
| DAT-001 — estado durável e migração legada | 🟨 remediação: 85 testes, CI `12/12` |
| LEA-63 — reteste independente final | ✅ `PASS` |
| LEA-66 — reteste pré-merge | ⏳ validação local e revisão pendentes |
| PR #72 | ⏳ Draft; merge bloqueado |
| LST-001 | ⛔ não autorizado |

## Evidência DAT-001

```text
LOCAL_LINUX_MINT=PENDING_FOR_FINAL_RETEST_HEAD
CI_REMEDIATION_CODE_HEAD=PASS_12_OF_12
PYTEST=PASS_85
RUFF=PASS
MYPY=PASS_12_SOURCE_FILES
PR72_PREMERGE_F01=REMEDIATED_AWAITING_LEA_66
PR72_PREMERGE_F02=REMEDIATED_AWAITING_LEA_66
INDEPENDENT_DECISION=PENDING
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

Validar o HEAD documental final no Linux Mint e anexar o TXT e o sidecar SHA-256.
Depois, executar a LEA-66. O PR permanece Draft, sem autorização de merge.
