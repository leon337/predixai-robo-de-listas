# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> Este README é a primeira visão do projeto no GitHub. Ele deve permitir uma auditoria à vista no celular sem exigir a abertura prévia dos documentos internos.

## 📍 Estado atual do projeto

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-18 — Consolidação cruzada das PTMs V2.5, V2.6 e V2.7
REVISÃO=LEA-19 — Revisão crítica independente
PULL_REQUEST=40
PR_STATUS=DRAFT
GATE=G7 — RETESTE_03_FAIL
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=1
MERGE_AUTORIZADO=NO
ADRS_AUTORIZADOS=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
```

A consolidação cruzada já existe, porém ainda não é definitiva. O índice e a matriz de rastreabilidade precisam receber as correções do Reteste 03 antes do Reteste 04.

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
      🟧 ESTAMOS AQUI
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
```

## 📊 Progresso da campanha documental

```text
[██████████] Auditoria Mestra          100%
[██████████] PTM V2.5                  100%
[██████████] PTM V2.6                  100%
[██████████] PTM V2.7                  100%
[████████░░] Consolidação cruzada       80%
[░░░░░░░░░░] ADRs                       0%
[░░░░░░░░░░] Documento Mestre           0%
```

O percentual representa entregas e gates documentais reais. Não representa progresso de implementação do produto final.

---

# 🧩 O que já foi construído

## 1. Auditoria e memória do legado

```text
✅ inventário factual do legado
✅ riscos e classificações
✅ fronteiras de segurança
✅ classificação REUTILIZAR
✅ classificação ADAPTAR
✅ classificação SUBSTITUIR
✅ classificação DESCONTINUAR
```

## 2. PTM V2.5 — Fundação

Define os contratos de fundação:

```text
✅ configuração
✅ identidade e segredos
✅ persistência
✅ listas
✅ clientes e dispositivos
✅ perfis e calibração
✅ backup e recovery
```

## 3. PTM V2.6 — Observação, inteligência e sinais

Define a pipeline de observação e análise:

```text
✅ sessão de observação
✅ captura de frames
✅ validação visual
✅ OCR e extração
✅ análise A–H
✅ estratégia
✅ candidatos e sinais
```

## 4. PTM V2.7 — Ação controlada

Define a fronteira de ação e execução:

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

## 5. Consolidação cruzada

Já foram produzidos:

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

Cobertura documental preservada:

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

Os grupos `V27-EXE-*` e `V27-SAF-*` possuem autoridades primárias diferentes.

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
ATUAL               CORRETO
DOM-13=32        →  DOM-13=26
DOM-14=12        →  DOM-14=7
DOM-15=20        →  DOM-15=27
DOM-16=34        →  DOM-16=38

TOTAL=218
```

Nenhum requisito será criado ou removido. Somente a autoridade primária será reconciliada.

## MINOR-04 — reconciliação textual

```text
32 requisitos estruturais
2 reclassificados
30 permaneceram sem alteração
```

O documento atual registra `29`; o valor correto é `30`.

---

# 🛣️ O que falta até o Documento Mestre

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

## Etapa B — integrar formalmente a consolidação

Após o `PASS`:

```text
⬜ autorização humana para merge
⬜ merge do PR #40
⬜ recibo pós-merge
⬜ atualização das fontes vivas
⬜ sincronização GitHub–Linear–README
⬜ fechamento da LEA-18 e LEA-19
```

O merge não é automático.

## Etapa C — construir os ADRs

Os ADRs consolidarão decisões que não podem permanecer espalhadas pelas PTMs.

Exemplos:

```text
ADR — autoridade global do servidor
ADR — separação sinal/comando/autorização
ADR — persistência single-writer
ADR — modelo de adaptadores
ADR — idempotência e deduplicação
ADR — timeout e UNKNOWN_EFFECT
ADR — kill switch
ADR — política de automação controlada
ADR — recuperação após restart
ADR — modo financeiro LIVE e seus gates
```

Situação:

```text
ADRs_CANDIDATOS=18
ADRs_CRIADOS=0
ADRs_AUTORIZADOS=NO
```

## Etapa D — construir o Documento Mestre

O Documento Mestre reunirá:

```text
1. visão e objetivos do produto
2. limites, modos e autorizações
3. arquitetura dos 16 domínios
4. cadeia completa dos 12 handoffs
5. contratos da PTM V2.5
6. contratos da PTM V2.6
7. contratos da PTM V2.7
8. decisões aprovadas nos ADRs
9. modelo de dados conceitual
10. estados e transições
11. segurança e threat model
12. observabilidade e auditoria
13. estratégia de testes
14. recovery e continuidade
15. roadmap de implementação
16. gates para implementação
```

Fluxo:

```text
CONSOLIDAÇÃO APROVADA
        ↓
ADRs APROVADOS
        ↓
DOCUMENTO MESTRE — DRAFT
        ↓
REVISÃO CRÍTICA INDEPENDENTE
        ↓
CORREÇÕES
        ↓
DOCUMENTO MESTRE — PASS
        ↓
ARQUITETURA V1.0 CONGELADA
```

## Próxima sequência objetiva

```text
CORRIGIR 3 ACHADOS
       ↓
AUDITAR 52/52 IDs FUNCIONAIS
       ↓
RETESTE 04
       ↓
PASS
       ↓
MERGE AUTORIZADO
       ↓
ADRs
       ↓
DOCUMENTO MESTRE
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

O projeto reconhece o modo `LIVE` como capacidade arquitetural separada. Ele permanece desligado por padrão e só pode ser ativado por gate específico.

```text
REAL_FINANCIAL_MODE=SUPPORTED_BY_SEPARATE_GATE
DEFAULT_STATE=DISABLED
HUMAN_ARMING_REQUIRED=YES
AUTHORIZED_ACCOUNT_ALLOWLIST_REQUIRED=YES
AUTHORIZED_PLATFORM_ALLOWLIST_REQUIRED=YES
SESSION_LIMITS_REQUIRED=YES
MAX_OPERATION_LIMIT_REQUIRED=YES
KILL_SWITCH_REQUIRED=YES
AUDIT_RECEIPT_REQUIRED=YES
EXPLICIT_LIVE_SESSION_CONFIRMATION_REQUIRED=YES
```

```text
CLIQUE CONTROLADO
├── modo simulado/controlado → autorizado
└── modo financeiro LIVE     → condicionado ao gate LIVE
```

Autorização de capacidade não equivale à ativação automática do modo `LIVE`.

Política normativa: [`docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`](docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md).

---

# 🔄 Sincronização obrigatória do painel

O README é uma projeção visual das fontes vivas. Ele não substitui o manifesto, o `PROJECT_STATE.md`, o tronco, o PR ou o Linear.

Toda transição, checkpoint ou fechamento deverá validar:

```text
README_OPERATIONAL_DASHBOARD=PASS
README_VERSION_SYNC=PASS
README_MISSION_SYNC=PASS
README_PHASE_SYNC=PASS
README_GATE_SYNC=PASS
README_BLOCKERS_SYNC=PASS
README_NEXT_ACTION_SYNC=PASS
```

A missão não pode ser declarada sincronizada quando a primeira página do GitHub apresentar estado antigo.

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

Ao abrir o repositório, use esta ordem:

```text
1. Estado atual
2. Mapa da campanha
3. Bloqueios
4. Próxima sequência
5. Política de automação
6. Fontes oficiais
7. Legado executável
```

A primeira página deve responder imediatamente:

```text
Onde estamos?
O que foi concluído?
O que está bloqueado?
O que falta?
Qual é a próxima ação?
```