# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README é projeção derivada. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-30 — ADRs P1/P2 da Arquitetura V1.0
REVISÃO_ATIVA=LEA-31 — pendente
PULL_REQUEST_ATIVO=49_DRAFT
BRANCH=leonpcsn/lea-30-adrs-p1-p2-arquitetura-v1
BASE_MAIN_SHA=dff0c0f0c26e820756804af92dd7b3641121d51b
PR_HEAD_SNAPSHOT=ef592068c45a53c0efc808545b9dfedb71adbfb1
FASE=ADR_P1_P2_READY_FOR_INDEPENDENT_REVIEW
GATE=INDEPENDENT_CRITICAL_REVIEW_IN_PROGRESS
STATE_REVISION=13
TRANSITION_ID=LEA-30-T01
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
MERGE_AUTORIZADO=NO
LIVE_MODE_ARMED=NO
SNAPSHOT_AT_UTC=2026-07-18T17:51:00Z
STATE_SOURCE=PROJECT_RUNTIME_STATE.yaml
```

## 🟧 ADRs P1/P2 propostos

```text
ADR_COUNT=6/6
P1_COUNT=5/5
P2_COUNT=1/1
CANDIDATE_MAPPING=6/6
DEPENDENCY_DAG=PASS_BUILDER
DEPENDS_ON_CYCLE_COUNT=0
NEW_REQUIREMENT_IDS=0
CANONICAL_REQUIREMENT_TOTAL=218
BUILDER_SELF_REVIEW=PASS_PRELIMINARY
MISSION_GATES=6/7
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
```

| ADR | Prioridade | Decisão | Estado |
|---|---|---|---|
| [ADR-0013](docs/architecture/adrs/ADR-0013-MIGRATIONS-COMPATIBILIDADE-E-IMPORTACAO-DO-LEGADO.md) | P1 | migrations e importação idempotente | proposto |
| [ADR-0014](docs/architecture/adrs/ADR-0014-RETENCAO-DE-FRAMES-E-EVIDENCIAS-VISUAIS.md) | P1 | retenção visual mínima | proposto |
| [ADR-0015](docs/architecture/adrs/ADR-0015-SERIALIZACAO-IDEMPOTENCIA-E-CIRCUIT-BREAKER.md) | P1 | serialização e circuit breaker | proposto |
| [ADR-0016](docs/architecture/adrs/ADR-0016-RELOGIOS-DEADLINES-E-IDENTIDADE-DE-PROCESSO.md) | P1 | relógios e identidade de processo | proposto |
| [ADR-0017](docs/architecture/adrs/ADR-0017-THRESHOLDS-E-LIMITES-NUMERICOS.md) | P2 | thresholds versionados | proposto |
| [ADR-0018](docs/architecture/adrs/ADR-0018-ESTRATEGIA-DE-TESTES-E-EVIDENCIA-POR-CAMADA.md) | P1 | testes e evidência por camada | proposto |

Nenhum ADR P1/P2 está aprovado. O conjunto depende da revisão crítica independente `LEA-31`, autorização humana de merge e confirmação pós-merge.

## ✅ Base P0 preservada

```text
LAST_COMPLETED_MISSION=LEA-26
LAST_COMPLETED_REVIEW=LEA-27_RETEST_03_PASS
P0_ADR_COUNT=12/12
P0_ADR_SET_STATUS=PUBLISHED_REVIEWED_P0_BASE
P0_MAIN_PR=46
P0_RECEIPT_PR=47
P0_FINAL_CONFIRMATION_PR=48
```

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
      ✅ publicados e revisados
      ↓
ADRs P1/P2 — LEA-30 / LEA-31
      ✅ 6/6 propostas produzidas
      ✅ rastreabilidade e DAG
      ✅ auto-revisão preliminar
      ⏳ revisão crítica independente
      ⛔ merge não autorizado
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

## 🎛️ Política A+B

```text
MODE_A=CONTROLLED_OR_SIMULATED_ALLOWED_BY_AUTHORIZED_MISSION
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
AUTO_ENABLE=PROHIBITED
LIVE_WITHOUT_ALL_GATES=BLOCKED
```

Nenhuma sessão LIVE, operação real ou implementação foi autorizada.

## 🧾 Evidências da missão

- [Plano LEA-30](docs/architecture/PLANO_MISSAO_ADRS_P1_P2_LEA-30_20260718.md)
- [Índice dos ADRs](docs/architecture/adrs/README.md)
- [Matriz P1/P2](docs/architecture/adrs/MATRIZ_RASTREABILIDADE_ADRS_P1_P2_LEA-30_20260718.md)
- [Auto-revisão preliminar](docs/history/reviews/AUTO_REVISAO_BUILDER_ADRS_P1_P2_LEA-30_20260718.md)
- [Roteiro da revisão LEA-31](docs/history/reviews/PROMPT_REVISAO_INDEPENDENTE_ADRS_P1_P2_LEA-31_20260718.md)

## Limites ativos

```text
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_CREATED=NO
MIGRATION_CREATED=NO
RUNTIME_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
BENCHMARK_EXECUTED=NO
TEST_RUNTIME_EXECUTED=NO
MERGE_AUTHORIZED=NO
DOCUMENT_MASTER_START_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

## Próxima ação

```text
NEXT_ACTION=EXECUTE_LEA_31_INDEPENDENT_CRITICAL_REVIEW_ON_PR_49_LIVE_HEAD
```