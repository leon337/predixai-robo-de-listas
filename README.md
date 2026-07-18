# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README projeta as fontes vivas para leitura rápida. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-26 — ADRs P0 da Arquitetura V1.0
REVISÃO=LEA-27 — revisão crítica independente
PULL_REQUEST=46
PR_STATUS=READY_FOR_REVIEW
FASE=ADR_P0_INDEPENDENT_CRITICAL_REVIEW
GATE=A7_INDEPENDENT_CRITICAL_REVIEW
ADR_GATES=6/7
ADR_P0=12/12_PROPOSED_FOR_REVIEW
CRITICAL_FINDINGS=0_BUILDER
MAJOR_FINDINGS=0_BUILDER
MINOR_FINDINGS=0_BUILDER
STATE_REVISION=9
SNAPSHOT_AT=2026-07-18
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+TRONCO+PR_46+LINEAR
MERGE_AUTORIZADO=NO
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

Os 12 ADRs P0 foram produzidos e estão no PR #46. Eles permanecem **propostos**, não definitivos, até a revisão independente da LEA-27, autorização humana de merge e confirmação pós-merge.

## 🗺️ Mapa da campanha

```text
AUDITORIA MESTRA
      ✅ concluída
      ↓
PTM V2.5 — Fundação
      ✅ revisada e aprovada
      ↓
PTM V2.6 — Observação, análise e sinais
      ✅ revisada e aprovada
      ↓
PTM V2.7 — Execução controlada e segurança
      ✅ revisada e aprovada
      ↓
CONSOLIDAÇÃO CRUZADA
      ✅ 7/7 gates
      ✅ Reteste 05 PASS
      ✅ PR #40, recibo #44 e fechamento #45 integrados
      ↓
ADRs P0 — LEA-26 / LEA-27
      ✅ plano, template e índice
      ✅ ADR-0001 a ADR-0012
      ✅ matriz de rastreabilidade
      ✅ auto-revisão preliminar
      🟧 revisão crítica independente
      ↓
DOCUMENTO MESTRE
      ⬜ não autorizado
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

## 📊 Progresso auditável da missão

```text
README_PROGRESS_SOURCE=LEA_26_REAL_GATES
ARBITRARY_PROGRESS=NO

A1_PRECONDITIONS=PASS
A2_TEMPLATE_AND_INDEX=PASS
A3_P0_ADRS=12/12
A4_TRACEABILITY=PASS_BUILDER
A5_CROSS_ADR_CONSISTENCY=PASS_BUILDER
A6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY
A7_INDEPENDENT_CRITICAL_REVIEW=PENDING_LEA_27

ADR_GATES=6/7
CURRENT_BLOCKER=INDEPENDENT_CRITICAL_REVIEW_REQUIRED
```

---

# 🧱 ADRs P0 propostos

| ADR | Decisão principal | Estado |
|---|---|---|
| [ADR-0001](docs/architecture/adrs/ADR-0001-SERVIDOR-E-AUTORIDADE-DE-ESTADO.md) | servidor como autoridade global e monólito modular local | proposto |
| [ADR-0002](docs/architecture/adrs/ADR-0002-PERSISTENCIA-E-ESCRITOR-UNICO.md) | SQLite V1 e fronteira de escritor único | proposto |
| [ADR-0003](docs/architecture/adrs/ADR-0003-CONTRATOS-REST-EVENTOS-E-VERSIONAMENTO.md) | REST JSON v1, SSE e snapshot de reconexão | proposto |
| [ADR-0004](docs/architecture/adrs/ADR-0004-IDENTIDADE-PAREAMENTO-E-CLIENTES.md) | pareamento local, identidade e revogação | proposto |
| [ADR-0005](docs/architecture/adrs/ADR-0005-PERFIS-ROIS-E-ALVO-LOGICO.md) | perfis versionados, ROIs e `target_logical_id` | proposto |
| [ADR-0006](docs/architecture/adrs/ADR-0006-MOTORES-A-H-E-ENVELOPE-DE-ANALISE.md) | motores A–H determinísticos e snapshot imutável | proposto |
| [ADR-0007](docs/architecture/adrs/ADR-0007-ESTRATEGIAS-E-LIFECYCLE-DE-SINAIS.md) | estratégias versionadas e lifecycle de sinais | proposto |
| [ADR-0008](docs/architecture/adrs/ADR-0008-MAQUINA-DE-ESTADOS-DE-COMANDO-E-EXECUCAO.md) | máquinas de estado de comando, grant e tentativa | proposto |
| [ADR-0009](docs/architecture/adrs/ADR-0009-ADAPTADORES-E-SEPARACAO-DOS-MODOS-A-B.md) | adaptadores isolados e separação A/B | proposto |
| [ADR-0010](docs/architecture/adrs/ADR-0010-KILL-SWITCH-DOMINANTE.md) | kill switch dominante por epoch | proposto |
| [ADR-0011](docs/architecture/adrs/ADR-0011-RECIBO-E-RECONCILIACAO-MULTIDIMENSIONAL.md) | recibo e reconciliação multidimensional | proposto |
| [ADR-0012](docs/architecture/adrs/ADR-0012-OBSERVABILIDADE-AUDITORIA-E-REDACTION.md) | logs, métricas, auditoria append-only e redaction | proposto |

Índice: [`docs/architecture/adrs/README.md`](docs/architecture/adrs/README.md).

## 🔗 Cobertura

```text
P0_CANDIDATES=12
P0_ADRS_PROPOSED=12
P1_CANDIDATES_REMAINING=5
P2_CANDIDATES_REMAINING=1
CANONICAL_DOMAINS=16/16
MANDATORY_HANDOFFS=12/12
CROSS_VERSION_REQUIREMENTS=218/218
NEW_REQUIREMENT_IDS=0
```

Matriz: [`docs/architecture/adrs/MATRIZ_RASTREABILIDADE_ADRS_P0_LEA-26_20260718.md`](docs/architecture/adrs/MATRIZ_RASTREABILIDADE_ADRS_P0_LEA-26_20260718.md).

## 🧭 Decisões estruturantes propostas

```text
SERVER_STATE=GLOBAL_AUTHORITY
CLIENT_STATE=LOCAL_VIEW
V1_TOPOLOGY=LOCAL_MODULAR_MONOLITH
V1_DATABASE=SQLITE
WRITE_AUTHORITY=SERVER_SINGLE_WRITER
API=REST_JSON_V1
SERVER_EVENTS=SSE
TARGET_IDENTITY=TARGET_LOGICAL_ID
ANALYSIS=IMMUTABLE_SNAPSHOT_AND_ENGINE_DAG
SIGNAL!=COMMAND
COMMAND!=GRANT
GRANT!=ATTEMPT
ATTEMPT!=CONFIRMED_EFFECT
ADAPTER_TYPES=NULL|SIMULATED|CONTROLLED_UI|LIVE_GATED
KILL_SWITCH=DOMINANT_PERSISTED_EPOCH
TIMEOUT!=NO_EFFECT
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
AUDIT=APPEND_ONLY_WITH_REDACTION
```

---

# 🧩 Base já concluída

```text
✅ Auditoria Mestra
✅ PTM V2.5 — 56/56
✅ PTM V2.6 — 78/78
✅ PTM V2.7 — 84/84
✅ consolidação — 218/218
✅ domínios — 16
✅ handoffs — 12
✅ auditoria V2.7 estrutural — 32/32
✅ auditoria V2.7 funcional — 52/52
✅ duplicados — 0
✅ órfãos — 0
✅ conflitos normativos abertos — 0
```

## 🛣️ Próxima sequência

```text
1. 🟧 executar LEA-27 sobre o HEAD final do PR #46
2. ⬜ corrigir achados, caso existam
3. ⬜ obter ADR_P0_CRITICAL_REVIEW=PASS
4. ⬜ receber autorização humana de merge
5. ⬜ integrar PR #46
6. ⬜ publicar recibo e sincronização pós-merge
7. ⬜ decidir missão de ADRs P1/P2 ou Documento Mestre
```

```text
NEXT_ACTION=EXECUTE_LEA_27_INDEPENDENT_CRITICAL_REVIEW_ON_PR_46
```

---

# 🎛️ Política de automação — modos A e B

Automação de interface é uma capacidade legítima. O efeito permitido depende do modo, alvo, grant e gates da sessão.

## Modo A — aplicação própria, simulação ou ambiente controlado

```text
ANÁLISE_DE_GRÁFICO=AUTORIZADA
CAPTURA_DE_TELA=AUTORIZADA
OCR=AUTORIZADO
REPLAY=AUTORIZADO
MOVIMENTO_DE_PONTEIRO=AUTORIZADO
PREENCHIMENTO_DE_CAMPOS=AUTORIZADO
DIGITAÇÃO=AUTORIZADA
CLIQUE=AUTORIZADO
AUTENTICAÇÃO_CONTROLADA=AUTORIZADA
TESTE_E2E=AUTORIZADO
ORDEM_SIMULADA=AUTORIZADA
```

## Modo B — possível efeito financeiro real

```text
REAL_FINANCIAL_MODE=SUPPORTED_BY_SEPARATE_GATE
DEFAULT_STATE=DISABLED
AUTO_ENABLE=PROHIBITED
HUMAN_ARMING_REQUIRED=YES
AUTHORIZED_ACCOUNT_ALLOWLIST_REQUIRED=YES
AUTHORIZED_PLATFORM_ALLOWLIST_REQUIRED=YES
SESSION_LIMITS_REQUIRED=YES
MAX_OPERATION_LIMIT_REQUIRED=YES
LOSS_AND_EXPOSURE_LIMITS_REQUIRED=YES
KILL_SWITCH_REQUIRED=YES
AUDIT_RECEIPT_REQUIRED=YES
SECRET_ISOLATION_REQUIRED=YES
TARGET_IDENTITY_VALIDATION_REQUIRED=YES
COMMERCIAL_AND_LEGAL_DECISION_RECORDED_REQUIRED=YES
PLATFORM_TERMS_AND_JURISDICTION_VALIDATION_REQUIRED=YES
ACCOUNT_HOLDER_ELIGIBILITY_VALIDATION_REQUIRED=YES
EXPLICIT_LIVE_SCOPE_AND_AUTHORIZATION_REQUIRED=YES
EXPLICIT_LIVE_SESSION_CONFIRMATION_REQUIRED=YES
```

Sem todos os gates, o Modo B permanece desativado e qualquer efeito financeiro fica bloqueado.

Política normativa: [`docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`](docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md).

---

# 🔄 Sincronização do painel

```text
README_OPERATIONAL_DASHBOARD=PASS_IN_PR_46
README_VERSION_SYNC=PASS
README_MISSION_SYNC=PASS
README_PHASE_SYNC=PASS
README_GATE_SYNC=PASS
README_PROGRESS_SYNC=PASS
README_BLOCKERS_SYNC=PASS
README_NEXT_ACTION_SYNC=PASS
README_SNAPSHOT_METADATA=PASS
README_AUTOMATION_POLICY_SYNC=PASS
```

Fontes oficiais:

- [`PROJECT_RUNTIME_STATE.yaml`](PROJECT_RUNTIME_STATE.yaml);
- [`PROJECT_STATE.md`](PROJECT_STATE.md);
- [`PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`](PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md);
- [PR #46](https://github.com/leon337/predixai-robo-de-listas/pull/46);
- Linear `LEA-26` e `LEA-27`.

---

# 🗃️ Legado executável disponível

A aplicação desktop legada permanece no repositório como fonte auditada e executável histórica.

```text
ARQUIVO_DE_VERSÃO=2.4.3
VERSÃO_DOCUMENTAL_REAL=V2.4.3-R1
PLATAFORMA_LEGADA=Linux Mint / X11
```

Recursos do legado:

- janela sempre acima;
- calibração de dois pontos globais;
- agenda dinâmica de até cinco sinais;
- direções `PARA_CIMA` e `PARA_BAIXO`;
- execução por relógio local;
- movimento e clique local;
- painel e histórico da sessão;
- persistência local da agenda e das coordenadas.

## Instalação do legado

```bash
sudo apt update
sudo apt install -y python3-venv python3-tk

git clone https://github.com/leon337/predixai-robo-de-listas.git
cd predixai-robo-de-listas

bash install.sh
bash run.sh
```

## Criar ícone

```bash
bash install_desktop.sh
```

## Execução manual

```bash
source .venv/bin/activate
python app/main.py
```

## Estrutura principal do legado

```text
app/main.py
assets/logo_predixai.svg
config/
docs/history/
docs/roadmap/
tests/test_smoke.py
requirements.txt
install.sh
install_desktop.sh
run.sh
VERSION
CHANGELOG.md
```