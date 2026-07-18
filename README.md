# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README é projeção derivada. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-26 — ADRs P0 da Arquitetura V1.0
REVISÃO=LEA-27 — RETESTE_02_AUTHORIZED
PULL_REQUEST=46
PR_STATUS=DRAFT_DURING_FINAL_SYNC
SNAPSHOT_CONTENT_HEAD=6f1ac10005e7231e9efe88da9c7a27931038a989
SNAPSHOT_CONTENT_HEAD_SEMANTICS=COMMON_PERSISTED_SNAPSHOT_BEFORE_RETEST_02_SYNC
LIVE_PR_HEAD_SOURCE=GITHUB_API
FASE=MINOR_01_REMEDIATED_PRE_RETEST_02
GATE=A7_INDEPENDENT_CRITICAL_REVIEW_RETEST_02
ADR_GATES=6/7
STATE_REVISION=10
SNAPSHOT_AT=2026-07-18
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+TRONCO+README+PR_46+LINEAR
MERGE_AUTORIZADO=NO
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

O snapshot persistido é o mesmo nas quatro fontes oficiais. O HEAD vivo do PR é consultado pela API do GitHub e permanece separado para evitar autorreferência em arquivos versionados.

## 🚧 Revisões e remediações

```text
LEA_27_INITIAL_REVIEW=FAIL
INITIAL_REVIEWED_HEAD=2c9c2432058c5f119bd1802c3ba00e845c6a5ca0
INITIAL_CRITICAL_FINDINGS=0
INITIAL_MAJOR_FINDINGS=4
INITIAL_MINOR_FINDINGS=1

RETEST_01_RESULT=FAIL
RETEST_01_REVIEWED_HEAD=87d47ef5c4426d021a77dff2536946cfcd66eba8
RETEST_01_REPORT_COMMIT=6f1ac10005e7231e9efe88da9c7a27931038a989
RETEST_01_CRITICAL_FINDINGS=0
RETEST_01_MAJOR_FINDINGS=0
RETEST_01_MINOR_FINDINGS=1

MAJOR_01=PASS
MAJOR_02=PASS
MAJOR_03=PASS
MAJOR_04=PASS
MINOR_01=REMEDIATED_BY_BUILDER_PENDING_RETEST_02
OPEN_BUILDER_FINDINGS=0
```

## 🔄 Contrato comum do snapshot

```text
MANIFEST_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
MISSION_LOCK_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
PROJECT_STATE_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
TRONCO_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
README_SNAPSHOT=6f1ac10005e7231e9efe88da9c7a27931038a989
LIVE_PR_HEAD_SOURCE=GITHUB_API
COMMON_SNAPSHOT_ALIGNMENT=PASS_BUILDER
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
      ✅ rastreabilidade individual 218/218
      ✅ grafo DEPENDS_ON acíclico
      ✅ quatro FSMs completas
      ✅ idempotência divergente bloqueada
      ✅ Reteste 01 executado
      ✅ MINOR-01 remediado pelo builder
      🟧 Reteste 02 autorizado
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
A7_INDEPENDENT_CRITICAL_REVIEW=RETEST_02_AUTHORIZED
ADR_GATES=6/7
CURRENT_BLOCKER=INDEPENDENT_CRITICAL_RETEST_02_REQUIRED
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

Índice: [`docs/architecture/adrs/README.md`](docs/architecture/adrs/README.md).

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

- [Matriz resumida](docs/architecture/adrs/MATRIZ_RASTREABILIDADE_ADRS_P0_LEA-26_20260718.md)
- [Apêndice individual dos 218 requisitos](docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md)

## 🎛️ Política de automação — Modos A e B

```text
MODE_A=CONTROLLED_OR_SIMULATED_ALLOWED
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
AUTO_ENABLE=PROHIBITED
LIVE_WITHOUT_ALL_GATES=BLOCKED
```

Modo A permanece limitado a ambiente autorizado e sem efeito financeiro real. Modo B permanece apenas como capacidade arquitetural desligada e condicionada aos gates técnicos, humanos, comerciais, legais e de conformidade.

## 🧾 Evidências

- [Plano dos ADRs P0](docs/architecture/PLANO_MISSAO_ADRS_P0_LEA-26_20260718.md)
- [Apêndice 218/218](docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md)
- [Reteste 01 — FAIL](docs/history/reviews/REVISAO_CRITICA_RETESTE_01_ADRS_P0_LEA-27_20260718.md)
- [Remediação do MINOR-01](docs/history/reviews/REMEDIACAO_MINOR_01_SNAPSHOT_ADRS_P0_LEA-26_20260718.md)

## 🛣️ Próxima sequência

```text
1. responder e resolver a thread de sincronização
2. confirmar CI 9/9 no novo HEAD
3. marcar o PR pronto para revisão
4. executar LEA-27 Reteste 02
5. obter ADR_P0_CRITICAL_REVIEW=PASS
6. solicitar nova autorização humana de merge
```

```text
NEXT_ACTION=RESOLVE_THREAD_VALIDATE_CI_AND_EXECUTE_LEA_27_RETEST_02
```

## 🗃️ Legado executável disponível

A aplicação desktop legada permanece fonte histórica auditada. Sua existência não representa a arquitetura futura nem autoriza execução LIVE.

```text
ARQUIVO_DE_VERSÃO=2.4.3
VERSÃO_DOCUMENTAL_REAL=V2.4.3-R1
PLATAFORMA_LEGADA=Linux Mint / X11
```

```bash
sudo apt update
sudo apt install -y python3-venv python3-tk
git clone https://github.com/leon337/predixai-robo-de-listas.git
cd predixai-robo-de-listas
bash install.sh
bash run.sh
```