# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README projeta as fontes vivas para leitura rápida no GitHub. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual do projeto

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_EM_FECHAMENTO=LEA-18 — Consolidação cruzada PTM V2.5/V2.6/V2.7
REVISÃO_CONCLUÍDA=LEA-19 — RETESTE_05_PASS
PR_PRINCIPAL=40
PR_PRINCIPAL_STATUS=MERGED
PR_PRINCIPAL_MERGE_COMMIT=3b24115dd0b5d4a3a8ba3222b249dc5c3d8fd6f9
PR_RECIBO=44
PR_RECIBO_STATUS=IN_PROGRESS
FASE=POST_MERGE_CONFIRMATION
GATE=POST_MERGE_CONFIRMATION
CONSOLIDACAO_GATES=7/7
BOSS_GATE=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
STATE_REVISION=7
SNAPSHOT_AT=2026-07-18
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+TRONCO+GITHUB+LINEAR
ADRS_AUTORIZADOS=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

A consolidação cruzada foi aprovada no Reteste 05 e integrada na `main`. A etapa atual publica o recibo pós-merge, fecha a LEA-18 e prepara os ADRs para uma nova autorização humana.

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
CONSOLIDAÇÃO CRUZADA V2.5 + V2.6 + V2.7
      ✅ Boss Gate PASS
      ✅ PR #40 integrado
      🟧 recibo e sincronização pós-merge — PR #44
      ↓
ADRs — decisões arquiteturais formais
      ⏳ aguardando fechamento da LEA-18 e nova autorização
      ↓
DOCUMENTO MESTRE
      ⬜ não iniciado
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
README_PROGRESS_SOURCE=REAL_GATES_AND_DELIVERABLES
ARBITRARY_PROGRESS=NO

G1_PRECONDITIONS=PASS
G2_SOURCE_INVENTORY=PASS
G3_DOMAIN_BOUNDARIES=PASS
G4_REQUIREMENTS_TRACEABILITY=PASS
G5_CONFLICTS_AND_SUPERSESSIONS=PASS
G6_CONSOLIDATED_DOCUMENT=PASS
G7_INDEPENDENT_CRITICAL_REVIEW=PASS_RETEST_05

CONSOLIDACAO_GATES=7/7
POST_MERGE_CONFIRMATION=IN_PROGRESS_PR_44
```

## ✅ Entregas consolidadas

### Auditoria e memória do legado

```text
✅ inventário factual do legado
✅ riscos e classificações
✅ fronteiras de segurança
✅ REUTILIZAR
✅ ADAPTAR
✅ SUBSTITUIR
✅ DESCONTINUAR
```

### PTM V2.5 — Fundação

```text
✅ configuração, identidade e segredos
✅ persistência e recovery
✅ listas, clientes e dispositivos
✅ perfis e calibração
```

### PTM V2.6 — Observação e inteligência

```text
✅ sessão de observação
✅ captura e proveniência
✅ validação visual
✅ OCR e extração
✅ análise A–H
✅ estratégia, candidatos e sinais
```

### PTM V2.7 — Ação controlada

```text
✅ comando e autorização
✅ policy engine
✅ alvo lógico e adaptadores
✅ dispatch e recibo
✅ reconciliação e recovery
✅ auditoria, observabilidade e contenção
```

### Consolidação cruzada

```text
✅ inventário canônico das fontes
✅ mapa de 16 domínios
✅ mapa de 12 handoffs
✅ matriz consolidada
✅ índice individual dos 218 requisitos
✅ auditoria estrutural V2.7 — 32/32
✅ auditoria funcional V2.7 — 52/52
✅ registro de conflitos e supersessões
✅ catálogo de 18 ADRs candidatos
✅ política A+B reconciliada
✅ Reteste 05 — PASS
✅ PR #40 — MERGED
```

## 🔢 Métricas consolidadas

```text
PTM_V2_5=56/56
PTM_V2_6=78/78
PTM_V2_7=84/84
TOTAL=218/218
DUPLICADOS=0
ÓRFÃOS=0
NOVOS_REQUISITOS=0
DOMÍNIOS=16
HANDOFFS=12
ADRS_CANDIDATOS=18
```

```text
DOM_13=26
DOM_14=7
DOM_15=27
DOM_16=38
```

## 🧭 Estado dos gates e PRs

```text
LEA_19=Done_PASS_RETEST_05
LEA_18=In_Progress_POST_MERGE_SYNC
PR_40=MERGED
PR_40_MERGE_COMMIT=3b24115dd0b5d4a3a8ba3222b249dc5c3d8fd6f9
PR_43=CLOSED_SUPERSEDED
PR_44=POST_MERGE_RECEIPT_IN_PROGRESS
OPEN_REVIEW_FINDINGS=0
```

## 🛣️ Próxima sequência

```text
1. 🟧 publicar o recibo pós-merge no PR #44
2. ⬜ confirmar o merge do recibo
3. ⬜ sincronizar GitHub, Linear, manifesto, PROJECT_STATE, tronco e README
4. ⬜ fechar formalmente a LEA-18
5. ⬜ apresentar a missão de ADRs para nova autorização
6. ⬜ construir e revisar os ADRs
7. ⬜ produzir o Documento Mestre
8. ⬜ congelar a Arquitetura V1.0 após revisão crítica
```

ADRs não são iniciados automaticamente. A próxima missão exige autorização própria.

---

# 🎛️ Política de automação — modos A e B

Automação de interface é uma capacidade legítima do projeto. O efeito permitido é determinado pelo modo ativo, pelo alvo autorizado e pelos gates da sessão.

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

O modo `LIVE` é suportado arquiteturalmente, permanece desligado por padrão e não é armado por esta fase documental.

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

# 🔄 Sincronização obrigatória do painel

```text
README_OPERATIONAL_DASHBOARD=PASS_IN_BRANCH
README_VERSION_SYNC=PASS
README_MISSION_SYNC=PASS
README_PHASE_SYNC=PASS
README_GATE_SYNC=PASS
README_PROGRESS_SYNC=PASS
README_BLOCKERS_SYNC=PASS
README_NEXT_ACTION_SYNC=PASS
README_SNAPSHOT_METADATA=PASS
README_AUTOMATION_POLICY_SYNC=PASS
README_SYNC=PENDING_PR_44_MERGE
```

Fontes oficiais:

- [`PROJECT_RUNTIME_STATE.yaml`](PROJECT_RUNTIME_STATE.yaml) — estado operacional estruturado;
- [`PROJECT_STATE.md`](PROJECT_STATE.md) — visão humana detalhada;
- [`PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`](PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md) — roadmap e continuidade;
- [PR #40](../../pull/40) — consolidação integrada;
- [PR #44](../../pull/44) — recibo e sincronização pós-merge;
- Linear `LEA-18` e `LEA-19` — missão e revisão.

Protocolo: [`docs/protocols/README_OPERATIONAL_DASHBOARD.md`](docs/protocols/README_OPERATIONAL_DASHBOARD.md).

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

## Criar ícone no menu e na área de trabalho

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

---

# 📌 Regra de leitura rápida

```text
1. Estado atual
2. Mapa da campanha
3. Progresso auditável
4. Entregas e métricas
5. Próxima sequência
6. Política de automação
7. Fontes oficiais
8. Legado executável
```
