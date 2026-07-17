# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> Esta é a primeira visão do projeto no GitHub. O estado apresentado abaixo é uma projeção pública derivada das fontes vivas e não substitui o manifesto operacional.

## 📍 Estado atual do projeto

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-18 — Consolidação cruzada das PTMs V2.5, V2.6 e V2.7
REVISÃO=LEA-19 — Revisão crítica independente
PULL_REQUEST=40
ACTIVE_PR_HEAD=c1ff8b19da966d6bb4b48ad237ea52db77c60d06
PR_STATUS=DRAFT
FASE=CROSS_CONSOLIDATION
GATE=G7 — RETESTE_03_FAIL
CONSOLIDACAO_GATES=6/7
BOSS_GATE=G7_FAIL
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=1
STATE_REVISION=7
SNAPSHOT_AT=2026-07-17
STATE_SOURCE=PROJECT_RUNTIME_STATE+PROJECT_STATE+PR_40+LINEAR
MERGE_AUTORIZADO=NO
ADRS_AUTORIZADOS=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
```

A consolidação cruzada já existe, mas ainda não é definitiva. A matriz e o índice de rastreabilidade precisam receber as correções do Reteste 03 antes do Reteste 04.

## 🗺️ Onde o projeto está agora

```text
AUDITORIA MESTRA
      ✅ concluída e revisada
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
      🟧 etapa atual — 6/7 gates concluídos
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

O painel não usa percentual arbitrário. A unidade de progresso é gate documental concluído e verificável.

```text
README_PROGRESS_SOURCE=LEA-18_GATES
ARBITRARY_PROGRESS=NO

G1_PRECONDITIONS=PASS
G2_SOURCE_INVENTORY=PASS
G3_DOMAIN_BOUNDARIES=PASS_PRE_RETEST_03
G4_REQUIREMENTS_TRACEABILITY=PASS_PRE_RETEST_03
G5_CONFLICTS_AND_SUPERSESSIONS=PASS
G6_CONSOLIDATED_DOCUMENT=PASS
G7_INDEPENDENT_CRITICAL_REVIEW=FAIL_RETEST_03

CONSOLIDACAO_GATES=6/7
CURRENT_BLOCKER=G7_INDEPENDENT_CRITICAL_REVIEW
```

Os gates G3 e G4 voltam a ser validados no Reteste 04 após as correções dos achados atuais.

---

# 🧩 O que já foi construído

## Auditoria e memória do legado

```text
✅ inventário factual do legado
✅ riscos e classificações
✅ fronteiras de segurança
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

## PTM V2.7 — Ação controlada

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
✅ inventário das fontes oficiais
✅ mapa de 16 domínios
✅ mapa de 12 handoffs
✅ matriz consolidada
✅ índice individual dos 218 requisitos
✅ registro de conflitos e supersessões
✅ catálogo preliminar de 18 ADRs
✅ documento consolidado
```

Cobertura preservada:

```text
PTM_V2_5=56 requisitos
PTM_V2_6=78 requisitos
PTM_V2_7=84 requisitos
TOTAL=218
DUPLICADOS=0
ÓRFÃOS=0
```

---

# 🚧 Bloqueios atuais da consolidação

## MAJOR-07 — matriz estrutural divergente

`PTM-V27-003` pertence ao `DOM-14 — Alvo lógico e adaptadores`, mas a matriz consolidada ainda o mantém dentro de um agrupamento do `DOM-13`.

```text
MATRIZ ATUAL
PTM-V27-002...007 ─────────→ DOM-13
             ↑
             └── PTM-V27-003 está no agrupamento incorreto

MATRIZ CORRETA
PTM-V27-002,004,005,006,007 → DOM-13
PTM-V27-003                 → DOM-14
```

## MAJOR-08 — requisitos funcionais agrupados incorretamente

```text
V27-EXE
├── DOM-14 — adaptador e capacidade
├── DOM-15 — tentativa, dispatch, timeout e retry
└── DOM-16 — kill switch e contenção

V27-SAF
├── DOM-13 — política e limites
├── DOM-14 — geometria e payload do adaptador
├── DOM-15 — fila e serialização
└── DOM-16 — segurança, segredos e redaction
```

Contagens esperadas após a correção:

```text
DOM-13=26
DOM-14=7
DOM-15=27
DOM-16=38
TOTAL=218
```

## MINOR-04 — reconciliação textual

```text
32 requisitos estruturais
2 reclassificados
30 permaneceram sem alteração
```

---

# 🛣️ Caminho até o Documento Mestre

## Etapa A — concluir a consolidação cruzada

```text
1. ⬜ corrigir MAJOR-07
2. ⬜ corrigir MAJOR-08
3. ⬜ corrigir MINOR-04
4. ⬜ auditar os 52/52 IDs funcionais V2.7
5. ⬜ atualizar as contagens dos 16 domínios
6. ⬜ sincronizar runtime, PROJECT_STATE, tronco e README
7. ⬜ solicitar Reteste 04
8. ⬜ obter RETESTE_04=PASS
```

Resultado necessário:

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
TRACEABILITY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=PASS
```

## Etapa B — integrar a consolidação

```text
⬜ autorização humana para merge
⬜ merge do PR #40
⬜ recibo pós-merge
⬜ atualização das fontes vivas
⬜ sincronização GitHub–Linear–README
⬜ fechamento da LEA-18 e LEA-19
```

## Etapa C — construir os ADRs

```text
ADRs_CANDIDATOS=18
ADRs_CRIADOS=0
ADRs_AUTORIZADOS=NO
```

Decisões previstas incluem autoridade do servidor, sinal/comando/autorização, single-writer, adaptadores, idempotência, timeout, `UNKNOWN_EFFECT`, kill switch, recovery e gates do modo LIVE.

## Etapa D — construir o Documento Mestre

O Documento Mestre reunirá visão do produto, limites, 16 domínios, 12 handoffs, contratos das PTMs, ADRs, modelo conceitual de dados, estados, segurança, observabilidade, testes, recovery e roadmap de implementação.

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

## Modo B — conta própria com possibilidade de efeito financeiro real

O modo `LIVE` é uma capacidade arquitetural separada. Ele permanece desligado por padrão. A existência da política não arma sessão, não autoriza implementação e não substitui decisão comercial ou legal.

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

```text
CLIQUE CONTROLADO
├── modo simulado/controlado → autorizado
└── modo financeiro LIVE     → condicionado a todos os gates LIVE
```

Política normativa: [`docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`](docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md).

---

# 🔄 Sincronização obrigatória do painel

O README é uma projeção visual das fontes vivas. Ele não substitui o manifesto, o `PROJECT_STATE.md`, o tronco, o PR ou o Linear.

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

Fontes oficiais:

- [`PROJECT_RUNTIME_STATE.yaml`](PROJECT_RUNTIME_STATE.yaml) — estado operacional estruturado;
- [`PROJECT_STATE.md`](PROJECT_STATE.md) — visão humana detalhada;
- [`PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`](PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md) — roadmap e continuidade;
- [PR #40](../../pull/40) — trabalho ativo ainda não integrado;
- Linear `LEA-18` e `LEA-19` — missão, revisão, bloqueios e progresso.

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
4. Bloqueios
5. Próxima sequência
6. Política de automação
7. Fontes oficiais
8. Legado executável
```
