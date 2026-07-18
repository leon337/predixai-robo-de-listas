# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README é projeção derivada. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-26 — ADRs P0 da Arquitetura V1.0
ÚLTIMA_REVISÃO=LEA-27 — RETESTE_03_PASS
MAIN_PULL_REQUEST=46
MAIN_PR_STATUS=MERGED
MAIN_PR_HEAD=d92a96163f2a81c2eb5202b90581a7f65f9a8272
MAIN_PR_MERGE_COMMIT=ff726709d13b8acca0961cc17160e38430c6d26f
POST_MERGE_RECEIPT_PR=47
POST_MERGE_RECEIPT_STATUS=OPEN_AWAITING_CI_AND_MERGE
FASE=POST_MERGE_CONFIRMATION
STATE_REVISION=12
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

## ✅ ADRs P0 integrados

```text
ADR_P0_CRITICAL_REVIEW=PASS_RETEST_03
ADR_COUNT=12/12
ADR_SET_STATUS=MERGED_REVIEWED_P0_BASE
REQUIREMENT_TRACEABILITY=218/218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
CANONICAL_DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
DEPENDS_ON_CYCLE_COUNT=0
FOUR_FSMS=PASS
DIVERGENT_IDEMPOTENCY_COLLISION=PASS_BLOCKED
```

O conjunto P0 revisado foi integrado como base documental da Arquitetura V1.0. Os ADRs não autorizam código, operação real ou início automático do Documento Mestre.

## 🗺️ Mapa da campanha

```text
AUDITORIA MESTRA
      ✅ concluída
      ↓
PTM V2.5 / V2.6 / V2.7
      ✅ aprovadas
      ↓
CONSOLIDAÇÃO CRUZADA
      ✅ concluída
      ↓
ADRs P0 — LEA-26 / LEA-27
      ✅ 12/12 ADRs
      ✅ Reteste 03 PASS
      ✅ PR #46 integrado
      🟧 PR #47 — recibo pós-merge
      ↓
ADRs P1/P2
      ⬜ decisão pendente
      ↓
DOCUMENTO MESTRE
      ⛔ não autorizado
      ↓
ARQUITETURA V1.0 CONGELADA
      ⬜ não iniciada
      ↓
PRONTIDÃO PARA IMPLEMENTAÇÃO
      ⬜ não iniciada
```

## 🧱 ADRs P0

| ADR | Decisão | Estado do conjunto |
|---|---|---|
| [ADR-0001](docs/architecture/adrs/ADR-0001-SERVIDOR-E-AUTORIDADE-DE-ESTADO.md) | servidor e autoridade global | integrado P0 |
| [ADR-0002](docs/architecture/adrs/ADR-0002-PERSISTENCIA-E-ESCRITOR-UNICO.md) | persistência e escritor único | integrado P0 |
| [ADR-0003](docs/architecture/adrs/ADR-0003-CONTRATOS-REST-EVENTOS-E-VERSIONAMENTO.md) | REST, eventos e versionamento | integrado P0 |
| [ADR-0004](docs/architecture/adrs/ADR-0004-IDENTIDADE-PAREAMENTO-E-CLIENTES.md) | identidade e pareamento | integrado P0 |
| [ADR-0005](docs/architecture/adrs/ADR-0005-PERFIS-ROIS-E-ALVO-LOGICO.md) | perfis, ROIs e alvo lógico | integrado P0 |
| [ADR-0006](docs/architecture/adrs/ADR-0006-MOTORES-A-H-E-ENVELOPE-DE-ANALISE.md) | motores A–H | integrado P0 |
| [ADR-0007](docs/architecture/adrs/ADR-0007-ESTRATEGIAS-E-LIFECYCLE-DE-SINAIS.md) | estratégias e sinais | integrado P0 |
| [ADR-0008](docs/architecture/adrs/ADR-0008-MAQUINA-DE-ESTADOS-DE-COMANDO-E-EXECUCAO.md) | quatro FSMs | integrado P0 remediado |
| [ADR-0009](docs/architecture/adrs/ADR-0009-ADAPTADORES-E-SEPARACAO-DOS-MODOS-A-B.md) | adaptadores e separação A/B | integrado P0 remediado |
| [ADR-0010](docs/architecture/adrs/ADR-0010-KILL-SWITCH-DOMINANTE.md) | kill switch dominante | integrado P0 remediado |
| [ADR-0011](docs/architecture/adrs/ADR-0011-RECIBO-E-RECONCILIACAO-MULTIDIMENSIONAL.md) | idempotência e reconciliação | integrado P0 remediado |
| [ADR-0012](docs/architecture/adrs/ADR-0012-OBSERVABILIDADE-AUDITORIA-E-REDACTION.md) | observabilidade e auditoria | integrado P0 |

## 🎛️ Política A+B

```text
MODE_A=CONTROLLED_OR_SIMULATED_ALLOWED
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
AUTO_ENABLE=PROHIBITED
LIVE_WITHOUT_ALL_GATES=BLOCKED
```

Nenhuma sessão LIVE, operação real ou implementação foi autorizada.

## 🧾 Evidências

- [Reteste 03 — PASS](docs/history/reviews/REVISAO_CRITICA_RETESTE_03_ADRS_P0_LEA-27_20260718.md)
- [Recibo pós-merge do PR #46](docs/history/receipts/RECIBO_POS_MERGE_LEA-26_LEA-27_PR-46_20260718.md)

## Próxima ação

```text
NEXT_ACTION=VALIDATE_AND_MERGE_RECEIPT_PR_47
DOCUMENT_MASTER_START_AUTHORIZED=NO
```
