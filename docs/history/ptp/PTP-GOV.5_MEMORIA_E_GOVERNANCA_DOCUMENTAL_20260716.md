# PTP-GOV.5 — Memória e Governança Documental

## Identificação

- **Código técnico:** PTP-GOV.5
- **Nome curto:** Memória GitHub Testável
- **Projeto:** PredixAI Robô de Listas
- **Repositório:** `leon337/predixai-robo-de-listas`
- **Versão real de referência:** V2.4.3-R1
- **Data:** 2026-07-16
- **Status:** EM ANDAMENTO
- **Tipo:** governança documental e continuidade multichat

## Objetivo

Transformar o GitHub na memória autossuficiente do projeto, permitindo que um chat sem contexto prévio reconstrua o estado, reconheça decisões congeladas e continue exatamente da etapa correta.

---

# 1. Motivo de criação

Durante uma longa sessão de arquitetura foram definidos doze pontos estruturais, revisões críticas, schema lógico do banco e PTMs preliminares. Quando a auditoria do legado começou, foi consultado por engano o repositório `leon337/predixai-platform`, que pertence a outro projeto.

O erro revelou que uma documentação espalhada apenas no histórico do chat não era suficiente para impedir mistura de escopo. A correção adotada foi interromper a auditoria, invalidar integralmente as conclusões do repositório incorreto e criar uma memória oficial testável no GitHub.

---

# 2. Estado que existia antes desta PTP

## 2.1 Arquitetura dos 12 pontos

Foram definidos e revisados:

1. Estrutura do servidor e clientes.
2. Contratos REST e WebSocket.
3. SQLite e tabelas.
4. ROIs.
5. Pontos de clique.
6. Frequências de leitura.
7. Cadeia de análise de gráfico.
8. Android mobile-first.
9. Compatibilidade Linux e Windows.
10. Testes sintéticos, replay e reais controlados.
11. Diretórios definitivos.
12. Sequência V2.5, V2.6 e V2.7.

## 2.2 Ponto 7 — cadeia analítica

A cadeia conceitual consolidada foi:

```text
captura do gráfico
→ extração estrutural
→ snapshot imutável
→ motores de análise
→ evidências
→ avaliação estratégica
→ candidato de sinal
→ arbitragem
→ validação
→ sinal final
```

Foram previstos motores de estrutura de mercado, tendência, suporte/resistência, volatilidade, medição/contexto de velas, momentum, confluência e estratégia.

## 2.3 Android mobile-first

O Android foi definido como painel operacional principal, mas não como dependência de inicialização do servidor. O cliente deverá usar REST, WebSocket, reconexão por sequence e cache local Room, sem acesso direto ao SQLite.

## 2.4 Linux e Windows

Linux Mint/X11 permanece plataforma central do projeto real atual. Windows é suporte progressivo futuro. Wayland deve ser detectado e limitado até validação específica.

## 2.5 Testes

Foram definidos níveis:

```text
R0 — sintético local
R1 — aplicação real somente leitura
R2 — validação visual sem mover cursor e sem clicar
R3 — pointer preview sem clique
R4 — clique controlado em ambiente local autorizado
```

## 2.6 Estrutura de versões

```text
V2.5 — fundação, servidor, SQLite, listas, conectividade, calibração e Android Foundation
V2.6 — observação, visão, análise, sinais e Android operacional
V2.7 — execução controlada, reconciliação, empacotamento e estabilização
```

---

# 3. Banco SQLite — decisões consolidadas

## 3.1 Princípios

- servidor é o único acesso ao banco;
- clientes não acessam o arquivo `.db`;
- WAL e foreign keys habilitados;
- escritor único por fila central;
- transações curtas;
- migrations versionadas e imutáveis;
- backup antes de migration de risco;
- eventos externos críticos somente após commit;
- schema lógico completo e schema físico progressivo.

## 3.2 Identidade e tempo

- UUID público para entidades distribuídas;
- INTEGER interno permitido em tabelas de alto volume;
- timestamps UTC em microssegundos;
- valores monetários em unidade mínima inteira;
- preços e medições em inteiro escalado;
- confiança em escala 0–10000.

## 3.3 Grupos lógicos de tabelas

Foram definidos grupos de governança, runtime, dispositivos, perfis, calibração, observação, extração, análise, estratégias, sinais, listas, execução, comandos, auditoria, replay e testes.

A revisão global concluiu que aproximadamente 125 entidades conceituais não devem ser criadas de uma vez. Cada tabela física exige produtor, consumidor, requisito, teste e, quando histórica, política de retenção.

## 3.4 Transações críticas

Foram definidas transações para:

- pareamento;
- ativação de perfil;
- aprovação de calibração;
- criação de snapshot;
- geração de sinal;
- dispatch de execução;
- feedback/reconciliação;
- parada emergencial;
- migration.

## 3.5 Outbox

A outbox transacional é obrigatória para impedir que o banco confirme uma alteração sem publicar o evento correspondente.

---

# 4. Ajustes pré-PTM consolidados

1. Separação de `STRATEGY_WAIT`, `WAIT_MORE_DATA`, `DEGRADED` e `BLOCKED`.
2. Modos `NORMAL`, `DIAGNOSTIC`, `REPLAY_RECORDING`, `TEST` e `MINIMAL_SAFE`.
3. Níveis reais R0–R4.
4. Autoridade de estado entre memória, SQLite, REST, WebSocket e Room.
5. Separação entre logs, eventos, auditoria, métricas e diagnóstico.
6. Gate de existência física de tabelas.
7. ADRs obrigatórios.
8. Frequências e thresholds como baseline provisória até benchmark.
9. Compatibilidade Windows progressiva.
10. Listas independentes da análise.

Correções adicionais:

- `MINIMAL_SAFE` só entra por condição formal e sai após health check;
- `STRATEGY_WAIT` não cria sinal final;
- R2 não move cursor;
- ADR não substitui requisito;
- tabelas históricas exigem retenção;
- Windows Foundation possui mínimo obrigatório.

---

# 5. PTM V2.5 — estado preliminar

Foi definida a estrutura de cada registro PTM, incluindo requisito, origem, milestone, domínio, componentes, contratos, banco, produtor, consumidor, testes, evidência, gate, criticidade, privacidade, retenção, feature flag e status.

Foram iniciados requisitos para:

- fonte única do estado;
- clientes sem acesso direto ao banco;
- escritor SQLite único;
- ciclo de vida do servidor;
- contratos externos versionados;
- outbox;
- listas independentes;
- Android Foundation;
- reconexão e snapshot;
- perfis;
- calibração, ROIs e alvos;
- Linux Foundation;
- Windows Foundation;
- migração V2.4.3;
- observabilidade;
- configuração segura;
- segurança de rede local;
- estado seguro sem Android.

A PTM permanece **preliminar**, pois ainda precisa ser reconciliada com a Auditoria Mestra do repositório real.

---

# 6. Auditoria do legado — mudança de método

## Método inicial

A ideia inicial era:

```text
Auditoria A — inventário
→ PTM
→ Auditoria B — comparação/migração
```

## Método substituto

Foi adotada uma Auditoria Mestra integrada:

```text
Inventário factual
+ classificação REUTILIZAR/ADAPTAR/SUBSTITUIR/DESCONTINUAR
+ rastreabilidade PTM
```

O estado real e o estado futuro permanecem em colunas conceitualmente separadas.

---

# 7. Erro crítico registrado

## 7.1 Ocorrência

Foi consultado o repositório errado:

```text
leon337/predixai-platform
```

em vez de:

```text
leon337/predixai-robo-de-listas
```

## 7.2 Sintomas do erro

Foram citados módulos, Flask, OCR e estruturas que não pertenciam ao Robô de Listas.

## 7.3 Correção

- todas as conclusões daquela auditoria foram invalidadas;
- nenhuma pode ser usada na PTM;
- nenhuma alteração foi feita nos repositórios;
- o repositório correto foi confirmado pelo conector GitHub;
- o HEAD real utilizado passou a ser `1c35534ee82d91ba34a6eab098eacf586a286b93`.

## 7.4 Regra preventiva

Cada conclusão de auditoria deverá informar:

```text
FONTE
CAMINHO
BRANCH OU COMMIT
CLASSIFICAÇÃO
NÍVEL DE CERTEZA
```

---

# 8. Estado real já confirmado da V2.4.3-R1

## Confirmado pelo repositório correto

- aplicação desktop em Python;
- Linux Mint/X11;
- Tkinter;
- `pynput`;
- perfis de coordenadas;
- listas datadas;
- até cinco sinais no histórico inicial;
- persistência JSON;
- execução por horário local;
- histórico de sessão;
- scripts de instalação e execução;
- `app/bootstrap_v243.py` no estado atual;
- ferramentas para abrir logs e backups;
- diagnóstico exportável;
- reparo de instalação.

## Divergência documental

O README descreve uma base anterior e não representa sozinho toda a V2.4.3-R1. A Auditoria Mestra deve priorizar código e HEAD real.

---

# 9. Nova governança de memória

## 9.1 Papéis

```text
GitHub  = verdade documental e técnica
Linear  = verdade operacional de tarefas e bloqueios
ChatGPT = motor de análise e engenharia
```

## 9.2 Regra de aprovação documental

Um documento histórico ou de estado só é aprovado quando um chat novo, sem memória, consegue reconstruir corretamente o projeto lendo apenas o GitHub.

## 9.3 Resultado esperado

Um chat novo deve identificar:

- repositório correto;
- versão real V2.4.3-R1;
- PTP ativa PTP-GOV.5;
- arquitetura conceitual já concluída;
- Auditoria Mestra como próxima etapa;
- PTM V2.5 como preliminar;
- Documento Mestre ainda inexistente;
- implementação não autorizada.

---

# 10. Roadmap atual

```text
🟧 PTP-GOV.5 — Memória e Governança Documental
⬜ Teste 1 — reconstrução de estado
⬜ Teste 2 — continuidade correta
⬜ Auditoria Mestra V2.4.3-R1
⬜ Anexo A — Inventário real
⬜ Reconciliar PTM V2.5
⬜ Revisar PTM V2.5
⬜ Construir/revisar PTM V2.6
⬜ Construir/revisar PTM V2.7
⬜ Consolidação cruzada final
⬜ ADRs finais
⬜ Documento Mestre
⬜ Revisão crítica
⬜ Arquitetura V1.0 congelada
⬜ Implementação
```

---

# 11. Pendências desta PTP

- publicar documentos na branch documental;
- criar guia operacional no Linear;
- executar Teste 1 em chat novo;
- executar Teste 2 em outro chat novo;
- registrar resultados;
- corrigir documentos se houver falha;
- abrir PR e integrar em `main` após aprovação.

---

# 12. Condição de fechamento

```text
PROJECT_STATE_CREATED=PASS
MEMORY_ACCEPTANCE_TESTS_DEFINED=PASS
LINEAR_OPERATIONAL_GUIDE_CREATED=PASS
MEMORY_TEST_1=PASS
MEMORY_TEST_2=PASS
DOCUMENTATION_MERGED_TO_MAIN=PASS
```

Enquanto esses gates não forem aprovados:

```text
PTP-GOV.5=EM_ANDAMENTO
AUDITORIA_MESTRA=PAUSADA_PARA_VALIDACAO_DA_MEMORIA
IMPLEMENTACAO=NAO_AUTORIZADA
```
