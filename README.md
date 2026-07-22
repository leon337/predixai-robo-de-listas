# PredixAI Robô de Listas

> Painel operacional. A autoridade estruturada permanece em `PROJECT_RUNTIME_STATE.yaml`; o estado humano oficial permanece em `PROJECT_STATE.md`.

## Estado atual

```text
MAIN_HEAD=40aca6ff9c470e44ea37e2d066092bc1349564fc
MAIN_INSTALLED_VERSION=V2.5.0-alpha.2
MISSÃO_ATIVA=LEA-146 — evidência local e reconciliação pós-merge
LEA_101=DONE
LEA_102=DONE_FAIL
LEA_124=DONE_PASS
PR_73=MERGED
PR_73_MERGE_COMMIT=40aca6ff9c470e44ea37e2d066092bc1349564fc
STATE_REVISION=42
GATE=DOCUMENTATION_RECONCILIATION_REVIEW
ARQUITETURA_V1_CONGELADA=YES
STATE_SOURCE=PROJECT_RUNTIME_STATE.yaml
```

## Campanha

| Entrega ou gate | Estado |
|---|---|
| Documento Mestre e mapa canônico | ✅ integrados |
| Requisitos, domínios, handoffs e ADRs | ✅ `218/218`, `16/16`, `12/12`, `18/18` |
| FND-001, FND-002 e FND-003 | ✅ integradas |
| DAT-001 — estado durável e migração legada | ✅ integrada |
| V2.5.0-alpha.2 | ✅ promovida no PR #73 |
| LEA-124 — reteste independente | ✅ `DONE/PASS` |
| Validação local Linux Mint | ✅ versão, launcher e perfil confirmados |
| LEA-146 — reconciliação documental | 🟨 em revisão |
| LST-001 — Lists and Scheduling | ⏳ candidata; não autorizada |

## Evidência local

```text
LOCAL_MAIN_UPDATE=PASS
LOCAL_VERSION_DISPLAY=PASS
DESKTOP_LAUNCHER=PASS
LOCAL_SCREEN=1366x768_100_PERCENT
LOCAL_PROFILE=RECALIBRAGEM_1366X768
LOCAL_APPLICATION_LABEL=TESTE_CORRETOR_FICTICIA
COORDINATE_CAPTURE=PASS
CONTROLLED_CLICK_TEST_IN_FICTITIOUS_OR_DEMO_ENVIRONMENT=PASS_REPORTED_BY_LEO
PROFILE_COMPATIBILITY=PERFIL_PRONTO
```

Relatório: `docs/history/reports/RELATORIO_EVIDENCIA_LOCAL_V250_ALPHA2_LEA_146_20260722.md`.

## Versão integrada

```text
VERSION=2.5.0-alpha.2
ENTRYPOINT=app/bootstrap_v250_alpha2_entry.py
STABLE_RUNTIME_DELEGATE=bootstrap_v23_entry.run
BEHAVIORAL_RUNTIME_CHANGE=NO
GITHUB_ACTIONS=PASS_12_OF_12
```

## Próxima missão candidata

```text
ID=LST-001
NOME=Lists and Scheduling
OBJETIVO=Implementar listas, itens, revisões e agendamentos independentes de análise e execução.
RESULTADO_TESTÁVEL=CRUD e importação preservam revisão e nunca iniciam observação automaticamente.
DEPENDE_DE=DAT-001
MODO_MÁXIMO=NULL_ONLY
VERSÃO_PREVISTA=V2.5.0-alpha.3
AUTORIZAÇÃO=NO
```

## Limites

```text
MODE_MAX=NULL_ONLY
LST_001_AUTHORIZED=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
LIVE_MODE_ARMED=NO
NEXT_CODE_INCREMENT_AUTHORIZED=NO
```

## Próxima ação

Revisar e integrar a reconciliação documental da LEA-146. Depois, submeter a LST-001 à autorização humana explícita sobre o HEAD confirmado da `main`.
