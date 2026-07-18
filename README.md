# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> Esta é a primeira visão do projeto no GitHub. O conteúdo abaixo é uma projeção pública das fontes vivas e não substitui o manifesto operacional.

## 📍 Estado atual do projeto

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-18 — Consolidação cruzada das PTMs V2.5, V2.6 e V2.7
REVISÃO_ATIVA=LEA-19 — Reteste 04 independente
PULL_REQUEST_ATIVO=40
ACTIVE_PR_HEAD=ab8e02bc6f07d8822012f667ac0a8f1f02a63941
PR_STATUS=READY_FOR_REVIEW
PR_MERGEABLE=YES
FASE=CROSS_CONSOLIDATION_INDEPENDENT_RETEST_04
GATE=G7 — RETESTE_04_SOLICITADO
CONSOLIDACAO_GATES=6/7
BOSS_GATE=PENDING_RETEST_04
OPEN_CRITICAL_FINDINGS=0
OPEN_MAJOR_FINDINGS=0
OPEN_MINOR_FINDINGS=0
STATE_REVISION=7
SNAPSHOT_AT=2026-07-18
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+PR_40+LINEAR
MAIN_HEAD_OBSERVED=236bc5df7f675ca5cf56d80c5812bd911d224651
MERGE_AUTORIZADO=NO
ADRS_AUTORIZADOS=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
```

A remediação do Reteste 03 foi concluída pelo builder. O PR `#40` está pronto para o Reteste 04 independente, mas a consolidação ainda não é definitiva e não está autorizada para merge.

---

## 🗺️ Onde o projeto está agora

```text
AUDITORIA MESTRA
      ✅ concluída e revisada
      ↓
PTM V2.5 — Fundação
      ✅ revisada, aprovada e integrada
      ↓
PTM V2.6 — Observação, análise e sinais
      ✅ revisada, aprovada e integrada
      ↓
PTM V2.7 — Execução controlada e segurança
      ✅ revisada, aprovada e integrada
      ↓
CONSOLIDAÇÃO CRUZADA V2.5 + V2.6 + V2.7
      🟧 etapa atual — 6/7 gates concluídos
      🟧 Reteste 04 solicitado
      ↓
ADRs — decisões arquiteturais formais
      ⬜ não iniciados
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

O painel usa gates e entregas reproduzíveis, sem percentual arbitrário.

```text
README_PROGRESS_SOURCE=LEA-18_GATES
ARBITRARY_PROGRESS=NO

G1_PRECONDITIONS=PASS
G2_SOURCE_INVENTORY=PASS_BUILDER_REMEDIATED
G3_DOMAIN_BOUNDARIES=PASS_BUILDER_REMEDIATED
G4_REQUIREMENTS_TRACEABILITY=PASS_BUILDER_REMEDIATED
G5_CONFLICTS_AND_SUPERSESSIONS=PASS_BUILDER_REMEDIATED
G6_CONSOLIDATED_DOCUMENT=PASS_BUILDER_REMEDIATED
G7_INDEPENDENT_CRITICAL_REVIEW=PENDING_RETEST_04

CONSOLIDACAO_GATES=6/7
CURRENT_BLOCKER=G7_INDEPENDENT_CRITICAL_REVIEW
```

---

# 🧩 O que já foi construído

## Auditoria e memória do legado

```text
✅ inventário factual do legado
✅ riscos e classificações
✅ fronteiras e contratos
✅ REUTILIZAR
✅ ADAPTAR
✅ SUBSTITUIR
✅ DESCONTINUAR
```

## PTM V2.5 — Fundação

```text
✅ configuração
✅ identidade e segredos
✅ persistência
✅ listas
✅ clientes e dispositivos
✅ perfis e calibração
✅ backup e recovery
```

## PTM V2.6 — Observação, inteligência e sinais

```text
✅ sessão de observação
✅ captura de frames
✅ validação visual
✅ OCR e extração
✅ análise A–H
✅ estratégia
✅ candidatos e sinais
```

## PTM V2.7 — Execução controlada

```text
✅ comando
✅ autorização
✅ policy engine
✅ alvo lógico
✅ adaptadores
✅ dispatch
✅ recibo
✅ reconciliação
✅ auditoria e contenção
```

## Consolidação cruzada

```text
✅ inventário canônico das fontes
✅ mapa de 16 domínios
✅ mapa de 12 handoffs
✅ matriz consolidada
✅ índice individual dos 218 requisitos
✅ registro de conflitos e supersessões
✅ catálogo preliminar de 18 ADRs
✅ documento consolidado
✅ auditoria estrutural V2.7 — 32/32
✅ auditoria funcional V2.7 — 52/52
✅ alinhamento à política normativa A+B
```

Cobertura reconciliada:

```text
PTM_V2_5=56 requisitos
PTM_V2_6=78 requisitos
PTM_V2_7=84 requisitos
TOTAL=218
ÚNICOS=218
DUPLICADOS=0
ÓRFÃOS=0
```

---

# ✅ Remediações do Reteste 03

## MAJOR-07 — corrigido

```text
PTM-V27-002,004,005,006,007 → DOM-13
PTM-V27-003                 → DOM-14
STATUS=PASS_BUILDER_REMEDIATED
```

## MAJOR-08 — corrigido

Os requisitos `V27-EXE-*` e `V27-SAF-*` foram auditados individualmente e distribuídos conforme a autoridade de comando, adaptador, dispatch e contenção.

```text
DOM-13=26
DOM-14=7
DOM-15=27
DOM-16=38
TOTAL=218
STATUS=PASS_BUILDER_REMEDIATED
```

## MINOR-04 — corrigido

```text
REQUISITOS_ESTRUTURAIS_V2_7=32
RECLASSIFICADOS=2
CONFIRMADOS_SEM_ALTERAÇÃO=30
STATUS=PASS_BUILDER_REMEDIATED
```

Evidência detalhada:

- [`docs/history/reviews/REMEDIACAO_RETESTE_03_CONSOLIDACAO_CRUZADA_LEA-18_20260717.md`](docs/history/reviews/REMEDIACAO_RETESTE_03_CONSOLIDACAO_CRUZADA_LEA-18_20260717.md)
- [`docs/history/reviews/REMEDIACAO_RETESTE_03_AUDITORIA_IDS_FUNCIONAIS_V2.7_LEA-18_20260718.md`](docs/history/reviews/REMEDIACAO_RETESTE_03_AUDITORIA_IDS_FUNCIONAIS_V2.7_LEA-18_20260718.md)

---

# 🛣️ Caminho até o Documento Mestre

## Etapa A — aprovar a consolidação cruzada

```text
1. ✅ corrigir MAJOR-07
2. ✅ corrigir MAJOR-08
3. ✅ corrigir MINOR-04
4. ✅ auditar os 52/52 IDs funcionais V2.7
5. ✅ reconciliar as contagens dos 16 domínios
6. ✅ sincronizar runtime, PROJECT_STATE, tronco, PR e Linear
7. ✅ solicitar Reteste 04
8. ⏳ obter RETESTE_04=PASS
```

Resultado exigido:

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
TRACEABILITY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=PASS
GITHUB_LINEAR_ALIGNMENT=PASS
```

## Etapa B — integrar a consolidação

Somente após o `PASS` e nova autorização humana:

```text
⬜ autorizar merge do PR #40
⬜ integrar o PR #40 na main
⬜ publicar recibo pós-merge
⬜ atualizar as fontes vivas
⬜ sincronizar GitHub–Linear–README
⬜ encerrar LEA-18 e LEA-19
```

## Etapa C — construir os ADRs

```text
ADRs_CANDIDATOS=18
ADRs_CRIADOS=0
ADRs_AUTORIZADOS=NO
```

## Etapa D — construir o Documento Mestre

```text
CONSOLIDAÇÃO APROVADA
        ↓
ADRs APROVADOS
        ↓
DOCUMENTO MESTRE — DRAFT
        ↓
REVISÃO CRÍTICA INDEPENDENTE
        ↓
DOCUMENTO MESTRE — PASS
        ↓
ARQUITETURA V1.0 CONGELADA
```

O Documento Mestre reunirá visão do produto, limites, 16 domínios, 12 handoffs, contratos das PTMs, ADRs, modelo conceitual de dados, estados, segurança, observabilidade, testes, recovery e roadmap de implementação.

---

# 🎛️ Política de automação — modos A e B

Automação de interface é uma capacidade legítima do projeto. O efeito permitido é determinado pelo modo ativo, pelo alvo autorizado e pelos gates da sessão.

## Modo A — próprio, simulado ou controlado

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

## Modo B — capacidade arquitetural condicionada

```text
REAL_FINANCIAL_MODE=SUPPORTED_BY_SEPARATE_GATE
DEFAULT_STATE=DISABLED
AUTO_ENABLE=PROHIBITED
COMMERCIAL_AND_LEGAL_DECISION_RECORDED_REQUIRED=YES
PLATFORM_TERMS_AND_JURISDICTION_VALIDATION_REQUIRED=YES
ACCOUNT_HOLDER_ELIGIBILITY_VALIDATION_REQUIRED=YES
EXPLICIT_LIVE_SCOPE_AND_AUTHORIZATION_REQUIRED=YES
HUMAN_ARMING_REQUIRED=YES
AUTHORIZED_ACCOUNT_ALLOWLIST_REQUIRED=YES
AUTHORIZED_PLATFORM_ALLOWLIST_REQUIRED=YES
SESSION_LIMITS_REQUIRED=YES
MAX_OPERATION_LIMIT_REQUIRED=YES
LOSS_AND_EXPOSURE_LIMITS_REQUIRED=YES
KILL_SWITCH_REQUIRED=YES
AUDIT_RECEIPT_REQUIRED=YES
EXPLICIT_LIVE_SESSION_CONFIRMATION_REQUIRED=YES
```

```text
MODE_A_POLICY=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_RUNTIME_ACTIVATION=NOT_STARTED
LIVE_MODE_ARMED=NO
```

Política normativa: [`docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`](docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md).

---

# 🔄 Fontes oficiais e sincronização

O README é uma projeção visual. As autoridades permanecem:

- [`PROJECT_RUNTIME_STATE.yaml`](PROJECT_RUNTIME_STATE.yaml) — estado operacional estruturado;
- [`PROJECT_STATE.md`](PROJECT_STATE.md) — visão humana detalhada;
- [`PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`](PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md) — roadmap e continuidade;
- [PR #40](../../pull/40) — consolidação ainda não integrada;
- Linear `LEA-18` e `LEA-19` — tarefa, revisão, bloqueios e progresso.

Toda transição, checkpoint ou fechamento valida:

```text
README_OPERATIONAL_DASHBOARD=PASS
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

Protocolo: [`docs/protocols/README_OPERATIONAL_DASHBOARD.md`](docs/protocols/README_OPERATIONAL_DASHBOARD.md).

---

# 🗃️ Legado executável disponível

A aplicação desktop legada permanece no repositório como fonte auditada e executável histórica.

```text
ARQUIVO_DE_VERSÃO=2.4.3
VERSÃO_DOCUMENTAL_REAL=V2.4.3-R1
PLATAFORMA_LEGADA=Linux Mint / X11
```

Recursos históricos:

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

## Estrutura principal

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
4. Entregas concluídas
5. Remediações
6. Caminho até o Documento Mestre
7. Política de automação A+B
8. Fontes oficiais
9. Legado executável
```

## Próxima ação

```text
NEXT_ACTION=EXECUTE_LEA_19_INDEPENDENT_RETEST_04_ON_PR_40
```