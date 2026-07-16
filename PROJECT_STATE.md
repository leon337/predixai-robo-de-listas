# PROJECT_STATE — PredixAI Robô de Listas

## Autoridade documental

- **Projeto:** PredixAI Robô de Listas
- **Repositório oficial:** `leon337/predixai-robo-de-listas`
- **Branch técnica de referência:** `main`
- **Versão real atual:** `V2.4.3-R1`
- **HEAD usado para este estado:** `1c35534ee82d91ba34a6eab098eacf586a286b93`
- **Status deste documento:** ATIVO
- **Data:** 2026-07-16
- **Substitui:** checkpoints informais de chat como fonte principal
- **Complementa:** `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md`

## Leia nesta ordem

1. `PROJECT_STATE.md`
2. `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md`
3. `docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md`
4. documentação histórica e técnica já existente no repositório
5. código da branch `main`

## Regra de fonte oficial

- O **GitHub** é a memória técnica e documental oficial.
- O **Linear** é o guia operacional de tarefas, bloqueios e progresso.
- O **ChatGPT** é o ambiente de análise e engenharia, não a memória primária.
- Auditorias devem usar exclusivamente o repositório correto desta PTP.
- Dados de outros repositórios são `REJEITADO_POR_ESCOPO`.

## Estado atual do projeto

```text
Arquitetura conceitual dos 12 pontos .......... CONCLUÍDA
Revisões críticas arquiteturais ............... CONCLUÍDAS
Schema lógico SQLite .......................... CONGELADO CONCEITUALMENTE
Sequência V2.5–V2.7 ........................... CONGELADA CONCEITUALMENTE
PTM V2.5 ...................................... PRELIMINAR / NÃO RECONCILIADA
Auditoria Mestra do legado V2.4.3-R1 .......... EM ANDAMENTO
PTM V2.6 ...................................... NÃO INICIADA
PTM V2.7 ...................................... NÃO INICIADA
Documento Mestre de Arquitetura ............... NÃO GERADO
Implementação V2.5 ............................ NÃO AUTORIZADA
```

## Etapa atual

### PTP ativa

`PTP-GOV.5 — Memória e Governança Documental`

### Objetivo atual

Implantar uma memória autossuficiente no GitHub, validável por chats sem contexto, e depois concluir a Auditoria Mestra do legado real `V2.4.3-R1` antes de reconciliar a PTM V2.5.

### Próxima ação obrigatória

```text
1. Validar os testes de memória definidos em PROJECT_MEMORY_ACCEPTANCE_TESTS.md.
2. Continuar a Auditoria Mestra somente no repositório predixai-robo-de-listas.
3. Produzir o Anexo A — Inventário real da V2.4.3-R1.
4. Reconciliar a PTM V2.5 com o inventário real.
```

## Roadmap oficial até o Documento Mestre

```text
🟧 PTP-GOV.5 — Memória e Governança Documental
⬜ Teste 1 — reconstrução de estado por chat novo
⬜ Teste 2 — continuidade correta por chat novo
⬜ Auditoria Mestra do legado V2.4.3-R1
⬜ Anexo A — Inventário real
⬜ Reconciliar PTM V2.5
⬜ Revisar criticamente PTM V2.5
⬜ Construir e revisar PTM V2.6
⬜ Construir e revisar PTM V2.7
⬜ Consolidação cruzada final
⬜ Consolidar ADRs
⬜ Gerar Documento Mestre
⬜ Revisão crítica do Documento Mestre
⬜ Congelar Arquitetura V1.0
⬜ Iniciar implementação em outros chats
```

## Os 12 pontos arquiteturais concluídos

1. Estrutura do servidor e clientes.
2. Contratos REST e WebSocket.
3. Banco SQLite, tabelas, índices, transações e migrations.
4. Lista inicial de ROIs.
5. Lista inicial de pontos de clique.
6. Frequência de leitura das ROIs.
7. Arquitetura da análise de gráfico.
8. Estratégia Android mobile-first.
9. Compatibilidade Linux e Windows.
10. Política de testes sintéticos, replay e reais controlados.
11. Estrutura definitiva de diretórios.
12. Escopo, dependências, entregas e gates de V2.5, V2.6 e V2.7.

## Divisão congelada de versões

```text
V2.5 = fundação, servidor, SQLite, listas, conectividade, calibração e Android Foundation
V2.6 = observação, extração, análise, sinais e Android operacional
V2.7 = execução controlada, reconciliação, distribuição e estabilização
```

## Decisões congeladas

- Servidor é a fonte global oficial de estado.
- SQLite será acessado somente pelo servidor.
- Escritas SQLite passam por escritor único/fila central.
- REST consulta/comanda; WebSocket notifica; event bus comunica internamente.
- Eventos externos críticos usam outbox transacional.
- Android e desktop são clientes sem acesso direto ao banco.
- Android é painel operacional principal, mas não é dependência de inicialização.
- Listas manuais e programadas funcionam sem análise gráfica.
- Análise, estratégia, sinal e execução permanecem separados.
- Schema lógico é completo; schema físico será progressivo por versão.
- Linux Mint/X11 e Windows terão suporte progressivo comprovado por testes.
- Frequências e thresholds não medidos são `PROVISIONAL_BASELINE`.
- GitHub é fonte técnica para auditorias, inventários, validações e migrações.
- Nenhuma implementação começa antes da Auditoria Mestra, PTMs e Documento Mestre.

## Estados transversais congelados

```text
STRATEGY_WAIT  = análise válida sem oportunidade
WAIT_MORE_DATA = dados insuficientes ou confirmação pendente
DEGRADED       = processamento permitido com limitações
BLOCKED        = condição crítica impede continuidade
```

## Modos de persistência

```text
NORMAL
DIAGNOSTIC
REPLAY_RECORDING
TEST
MINIMAL_SAFE
```

## Níveis de teste real controlado

```text
R0 = interface sintética local
R1 = aplicação real somente leitura
R2 = validação visual sem movimento e sem clique
R3 = pointer preview sem clique
R4 = clique controlado em ambiente local autorizado
```

## Estado real já confirmado no repositório correto

- Aplicação desktop Python para Linux Mint/X11.
- Código histórico em `app/main.py` com Tkinter, JSON, threads e `pynput`.
- Modelos existentes: `Signal`, `ScheduleList`, `CoordinateProfile` e `PredixAIRoboListas`.
- Persistência histórica em `config/config_predixai_robo_listas.json`.
- Dependência externa confirmada: `pynput==1.8.2`.
- O HEAD atual contém `app/bootstrap_v243.py` e funcionalidades de logs, backups, diagnóstico e reparo de instalação.
- O README está parcialmente defasado em relação ao HEAD atual.

## Erro registrado e correção

### Erro

Foi iniciada uma auditoria no repositório incorreto `leon337/predixai-platform`.

### Impacto

As conclusões daquela auditoria não pertencem ao PredixAI Robô de Listas.

### Correção

- Auditoria incorreta invalidada integralmente.
- Nenhum dado dela pode entrar na PTM ou no Documento Mestre.
- Repositório único autorizado: `leon337/predixai-robo-de-listas`.
- Toda conclusão futura deve informar fonte, caminho, branch/commit, classificação e certeza.

## Decisões revogadas

### Auditoria separada da rastreabilidade

- **Decisão anterior:** inventariar e somente depois reconciliar a PTM.
- **Status:** REVOGADA.
- **Substituição:** Auditoria Mestra integrada, com inventário, classificação e rastreabilidade lado a lado.

### Chat como fonte principal de memória

- **Decisão implícita anterior:** checkpoints de chat carregariam o estado.
- **Status:** REVOGADA.
- **Substituição:** GitHub é memória oficial; checkpoints são apenas cópia de segurança.

## Regras permanentes de memória

1. Cada etapa relevante gera documento histórico versionado no GitHub.
2. O estado atual deve ser atualizado em `PROJECT_STATE.md`.
3. Um documento só é aprovado quando um chat novo consegue reconstruir o estado apenas pelo GitHub.
4. Falha no teste exige correção documental antes de continuar.
5. Linear acompanha tarefas; não substitui o conteúdo técnico do GitHub.
6. Nenhum chat pode declarar execução sem commit, relatório, evidência ou confirmação explícita.

## Proibições atuais

```text
NÃO iniciar implementação V2.5.
NÃO gerar SQL físico ou migrations físicas.
NÃO alterar a PTM como definitiva antes do inventário.
NÃO usar dados do predixai-platform.
NÃO tratar README como única descrição do estado real.
NÃO misturar estado real da V2.4.3-R1 com arquitetura futura V2.5–V2.7.
```

## Critério de passagem da etapa atual

```text
MEMORY_TEST_1=PASS
MEMORY_TEST_2=PASS
AUDITORIA_MESTRA=PASS
ANEXO_A_INVENTARIO_REAL=PASS
PTM_V2_5_RECONCILIADA=PASS
```
