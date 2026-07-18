# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README é projeção derivada. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-26 — ADRs P0 da Arquitetura V1.0
ÚLTIMA_REVISÃO=LEA-27 — RETESTE_02_PASS
PULL_REQUEST=46
PR_STATUS=READY_FOR_MERGE_NOT_AUTHORIZED
SNAPSHOT_CONTENT_HEAD=6f1ac10005e7231e9efe88da9c7a27931038a989
LIVE_PR_HEAD_SOURCE=GITHUB_API
RETEST_02_REVIEWED_HEAD=c4bfc336027f8e8aa76c686f460431a531a8dc69
RETEST_02_REPORT_COMMIT=216c8d2b485aed72c77e05b401fe06ecaa1eb6c9
FASE=ADR_P0_REVIEW_PASS_AWAITING_MERGE_AUTHORIZATION
GATE=A7_INDEPENDENT_CRITICAL_REVIEW_PASS_RETEST_02
ADR_GATES=7/7
STATE_REVISION=11
SNAPSHOT_AT=2026-07-18
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+TRONCO+README+PR_46+LINEAR
MERGE_AUTORIZADO=NO
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

O snapshot persistido permanece comum às fontes oficiais. O HEAD vivo é consultado pela API do GitHub e não é tratado como campo autorreferencial dos arquivos versionados.

## ✅ Resultado do Reteste 02

```text
ADR_P0_CRITICAL_REVIEW=PASS
RETEST_SEQUENCE=02
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
OPEN_FINDINGS=0
DOCUMENTAL_READY_FOR_MERGE=YES
DOCUMENT_MASTER_READY_TO_START=NO
RETEST_REQUIRED=NO
```

O Documento Mestre continua bloqueado até autorização humana de merge, integração do PR #46, recibo pós-merge e sincronização final.

## 🔍 Validações aprovadas

```text
MAJOR_01_TRACEABILITY_218=PASS
MAJOR_02_DEPENDENCY_DAG=PASS
MAJOR_03_FOUR_FSMS=PASS
MAJOR_04_IDEMPOTENCY_COLLISION=PASS
MINOR_01_COMMON_SNAPSHOT=PASS
MANIFEST_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
MISSION_LOCK_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
PROJECT_STATE_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
TRONCO_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
README_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
OPEN_REVIEW_THREADS=0
CI_WORKFLOWS=9_OF_9_SUCCESS
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
      ✅ concluída e publicada
      ↓
ADRs P0 — LEA-26 / LEA-27
      ✅ 12/12 ADRs propostos
      ✅ rastreabilidade 218/218
      ✅ grafo DEPENDS_ON acíclico
      ✅ quatro FSMs completas
      ✅ idempotência divergente bloqueada
      ✅ snapshot comum sincronizado
      ✅ LEA-27 Reteste 02 PASS
      🟧 autorização humana de merge
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

## 📊 Progresso auditável

```text
README_PROGRESS_SOURCE=LEA_26_REAL_GATES
ARBITRARY_PROGRESS=NO
A1_PRECONDITIONS=PASS
A2_TEMPLATE_AND_INDEX=PASS
A3_P0_ADRS=12/12
A4_TRACEABILITY=PASS
A5_CROSS_ADR_CONSISTENCY=PASS
A6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY
A7_INDEPENDENT_CRITICAL_REVIEW=PASS_RETEST_02
ADR_GATES=7/7
CURRENT_BLOCKER=NEW_HUMAN_MERGE_AUTHORIZATION_REQUIRED
```

## 🧱 ADRs P0 propostos

| ADR | Decisão | Estado |
|---|---|---|
| [ADR-0001](docs/architecture/adrs/ADR-0001-SERVIDOR-E-AUTORIDADE-DE-ESTADO.md) | servidor e autoridade global | proposto |
| [ADR-0002](docs/architecture/adrs/ADR-0002-PERSISTENCIA-E-ESCRITOR-UNICO.md) | SQLite V1 e escritor único | proposto |
| [ADR-0003](docs/architecture/adrs/ADR-0003-CONTRATOS-REST-EVENTOS-E-VERSIONAMENTO.md) | REST JSON v1, SSE e snapshot | proposto |
| [ADR-0004](docs/architecture/adrs/ADR-0004-IDENTIDADE-PAREAMENTO-E-CLIENTES.md) | identidade e pareamento local | proposto |
| [ADR-0005](docs/architecture/adrs/ADR-0005-PERFIS-ROIS-E-ALVO-LOGICO.md) | perfis, ROIs e alvo lógico | proposto |
| [ADR-0006](docs/architecture/adrs/ADR-0006-MOTORES-A-H-E-ENVELOPE-DE-ANALISE.md) | motores A–H e snapshot imutável | proposto |
| [ADR-0007](docs/architecture/adrs/ADR-0007-ESTRATEGIAS-E-LIFECYCLE-DE-SINAIS.md) | estratégias e lifecycle de sinais | proposto |
| [ADR-0008](docs/architecture/adrs/ADR-0008-MAQUINA-DE-ESTADOS-DE-COMANDO-E-EXECUCAO.md) | quatro FSMs explícitas | proposto remediado |
| [ADR-0009](docs/architecture/adrs/ADR-0009-ADAPTADORES-E-SEPARACAO-DOS-MODOS-A-B.md) | adaptadores e separação A/B | proposto remediado |
| [ADR-0010](docs/architecture/adrs/ADR-0010-KILL-SWITCH-DOMINANTE.md) | kill switch dominante | proposto remediado |
| [ADR-0011](docs/architecture/adrs/ADR-0011-RECIBO-E-RECONCILIACAO-MULTIDIMENSIONAL.md) | idempotência, recibo e reconciliação | proposto remediado |
| [ADR-0012](docs/architecture/adrs/ADR-0012-OBSERVABILIDADE-AUDITORIA-E-REDACTION.md) | observabilidade, auditoria e redaction | proposto |

## 🔗 Rastreabilidade e invariantes

```text
REQUIREMENT_ROWS=218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
UNJUSTIFIED_NO_P0_MAPPING=0
CANONICAL_DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
DEPENDS_ON_NODE_COUNT=12
DEPENDS_ON_CYCLE_COUNT=0
COMMAND_FSM=DEFINED
AUTHORIZATION_GRANT_FSM=DEFINED
SESSION_ARMING_FSM=DEFINED
EXECUTION_ATTEMPT_FSM=DEFINED
SAME_KEY_AND_DIFFERENT_CANONICAL_FINGERPRINT=BLOCK_CONFLICT_AND_AUDIT
```

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

- [Reteste 01 — FAIL](docs/history/reviews/REVISAO_CRITICA_RETESTE_01_ADRS_P0_LEA-27_20260718.md)
- [Remediação do MINOR-01](docs/history/reviews/REMEDIACAO_MINOR_01_SNAPSHOT_ADRS_P0_LEA-26_20260718.md)
- [Reteste 02 — PASS](docs/history/reviews/REVISAO_CRITICA_RETESTE_02_ADRS_P0_LEA-27_20260718.md)

## 🛣️ Próxima sequência

```text
1. aguardar autorização humana de merge
2. integrar o PR #46 com proteção do HEAD
3. publicar recibo pós-merge
4. sincronizar GitHub e Linear
5. decidir ADRs P1/P2 e autorização do Documento Mestre
```

```text
NEXT_ACTION=AWAIT_NEW_HUMAN_AUTHORIZATION_TO_MERGE_PR_46
```

## 🗃️ Legado executável disponível

A aplicação desktop legada permanece fonte histórica auditada. Sua existência não representa a arquitetura futura nem autoriza execução LIVE.

```text
ARQUIVO_DE_VERSÃO=2.4.3
VERSÃO_DOCUMENTAL_REAL=V2.4.3-R1
PLATAFORMA_LEGADA=Linux Mint / X11
```