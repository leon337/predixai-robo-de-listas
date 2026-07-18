# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README é projeção derivada. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-26 — ADRs P0 da Arquitetura V1.0
REVISÃO=LEA-27 — RETESTE_01_PENDING
PULL_REQUEST=46
PR_STATUS=DRAFT_PENDING_FINAL_SYNC
ACTIVE_PR_HEAD=c1c694f70d036104fee7b91addf7b68cc5d5ba58
ACTIVE_PR_HEAD_SEMANTICS=LAST_CONFIRMED_REMEDIATION_CONTENT_SNAPSHOT
CURRENT_PR_HEAD_SOURCE=LIVE_GITHUB_QUERY_AT_RETEST_START
FASE=ADR_P0_REMEDIATED_READY_FOR_RETEST_01
GATE=A7_INDEPENDENT_CRITICAL_REVIEW_RETEST_01
ADR_GATES=6/7
STATE_REVISION=9
SNAPSHOT_AT=2026-07-18
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+TRONCO+PR_46+LINEAR
MERGE_AUTORIZADO=NO
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

O HEAD exato do Reteste 01 deve ser confirmado na página viva do PR #46. Um arquivo versionado não pode conter o SHA do próprio commit que o cria; por isso o campo acima registra o último snapshot de conteúdo confirmado e declara a fonte viva do HEAD final.

## 🚧 Revisão inicial e remediação

```text
LEA_27_INITIAL_REVIEW=FAIL
INITIAL_REVIEWED_HEAD=2c9c2432058c5f119bd1802c3ba00e845c6a5ca0
CRITICAL_FINDINGS_INITIAL=0
MAJOR_FINDINGS_INITIAL=4
MINOR_FINDINGS_INITIAL=1

MAJOR_FINDINGS_REMEDIATED_BY_BUILDER=4/4
MINOR_FINDINGS_REMEDIATED_BY_BUILDER=1/1
OPEN_BUILDER_CRITICAL_FINDINGS=0
OPEN_BUILDER_MAJOR_FINDINGS=0
OPEN_BUILDER_MINOR_FINDINGS=0
INDEPENDENT_CLEARANCE=PENDING_RETEST_01
```

Os cinco achados permanecem pendentes de baixa independente até a LEA-27 executar o Reteste 01.

## 🗺️ Mapa da campanha

```text
AUDITORIA MESTRA
      ✅ concluída
      ↓
PTM V2.5 — Fundação
      ✅ aprovada
      ↓
PTM V2.6 — Observação, análise e sinais
      ✅ aprovada
      ↓
PTM V2.7 — Execução controlada e segurança
      ✅ aprovada
      ↓
CONSOLIDAÇÃO CRUZADA
      ✅ 7/7 gates
      ✅ PR #40, recibo #44 e fechamento #45 integrados
      ↓
ADRs P0 — LEA-26 / LEA-27
      ✅ 12/12 ADRs propostos
      ✅ rastreabilidade individual 218/218
      ✅ grafo DEPENDS_ON acíclico
      ✅ quatro FSMs completas
      ✅ idempotência divergente bloqueada
      ✅ auto-revisão pós-remediação
      🟧 LEA-27 Reteste 01
      ↓
DOCUMENTO MESTRE
      ⛔ não autorizado
      ↓
REVISÃO CRÍTICA DO DOCUMENTO MESTRE
      ⬜ não iniciada
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
A4_TRACEABILITY=PASS_BUILDER_AFTER_MAJOR_01
A5_CROSS_ADR_CONSISTENCY=PASS_BUILDER_AFTER_MAJOR_02_03_04
A6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY_AFTER_REMEDIATION
A7_INDEPENDENT_CRITICAL_REVIEW=RETEST_01_REQUIRED

ADR_GATES=6/7
CURRENT_BLOCKER=INDEPENDENT_CRITICAL_RETEST_01_REQUIRED
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

## 🔗 Rastreabilidade 218/218

```text
REQUIREMENT_ROWS=218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
UNJUSTIFIED_NO_P0_MAPPING=0
CANONICAL_DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
NEW_REQUIREMENT_IDS=0
```

- [Matriz resumida dos ADRs](docs/architecture/adrs/MATRIZ_RASTREABILIDADE_ADRS_P0_LEA-26_20260718.md)
- [Apêndice individual dos 218 requisitos](docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md)

## 🧭 Dependências e governança

```text
DEPENDS_ON=PRE_REQUISITO_ACICLICO
MUST_ALIGN_WITH=COERENCIA_BIDIRECIONAL_SEM_ORDEM
GOVERNS=DECISAO_QUE_RESTRINGE_OUTRA
DEPENDS_ON_NODE_COUNT=12
DEPENDS_ON_CYCLE_COUNT=0
DEPENDS_ON_DAG=PASS_BUILDER
```

A dominância do kill switch é relação `GOVERNS`; não cria ciclo inverso no grafo de pré-requisitos.

## 🔄 FSMs e idempotência

```text
COMMAND_FSM=DEFINED
AUTHORIZATION_GRANT_FSM=DEFINED
SESSION_ARMING_FSM=DEFINED
EXECUTION_ATTEMPT_FSM=DEFINED
SUPERSEDED=DEFINED
GRANT_REVOCATION_EXPIRATION_CONSUMPTION=DEFINED
KILL_EPOCH_INVALIDATION=DEFINED
RESTART_NO_REARM_OR_REDISPATCH=PASS

SAME_KEY_AND_SAME_CANONICAL_FINGERPRINT=RETURN_EXISTING_ATTEMPT
SAME_KEY_AND_DIFFERENT_CANONICAL_FINGERPRINT=BLOCK_CONFLICT_AND_AUDIT
```

## 🎛️ Política de automação — Modos A e B

```text
MODE_A=CONTROLLED_OR_SIMULATED_ALLOWED
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
AUTO_ENABLE=PROHIBITED
LIVE_WITHOUT_ALL_GATES=BLOCKED
```

Modo A permite análise, captura, OCR, replay, ponteiro, teclado, preenchimento, clique, autenticação controlada, E2E e ordem simulada em alvo autorizado e sem efeito financeiro real.

Modo B permanece apenas como capacidade arquitetural condicionada. Exige decisão comercial/legal, termos e jurisdição, elegibilidade, allowlists, limites, kill switch, auditoria, isolamento de segredos, arming humano e confirmação explícita da sessão.

Política normativa: [`docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`](docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md).

## 🧾 Evidências

- [Plano remediado](docs/architecture/PLANO_MISSAO_ADRS_P0_LEA-26_20260718.md)
- [Auto-revisão do builder](docs/history/reviews/AUTO_REVISAO_BUILDER_ADRS_P0_LEA-26_20260718.md)
- [Relatório de remediação](docs/history/reviews/REMEDIACAO_ADRS_P0_LEA-26_POS_LEA-27_20260718.md)
- [Revisão crítica inicial FAIL](docs/history/reviews/REVISAO_CRITICA_ADRS_P0_LEA-27_20260718.md)

## 🛣️ Próxima sequência

```text
1. sincronizar o HEAD final do PR #46
2. marcar o PR pronto para revisão
3. reabrir a LEA-27
4. solicitar Reteste 01
5. validar CI e threads
6. obter ADR_P0_CRITICAL_REVIEW=PASS
7. solicitar nova autorização humana de merge
8. publicar recibo pós-merge
9. decidir ADRs P1/P2 ou Documento Mestre
```

```text
NEXT_ACTION=EXECUTE_LEA_27_RETEST_01_ON_FINAL_LIVE_PR_46_HEAD
```

## 🗃️ Legado executável disponível

A aplicação desktop legada permanece como fonte histórica auditada. Sua existência não representa a arquitetura futura nem autoriza execução LIVE.

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
