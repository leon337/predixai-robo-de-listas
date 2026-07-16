# PROJECT_STATE — PredixAI Robô de Listas

## Autoridade documental

- **Projeto:** PredixAI Robô de Listas
- **Repositório oficial:** `leon337/predixai-robo-de-listas`
- **Branch técnica:** `main`
- **Versão real atual:** `V2.4.3-R1`
- **PTP ativa:** `PTP-GOV.5 — Memória e Governança Documental`
- **Mini-PTP ativa:** `PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória`
- **Status:** EM VALIDAÇÃO
- **Data:** 2026-07-16

## Leia nesta ordem

1. `PROJECT_STATE.md`
2. `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md`
3. `docs/history/ptp/PTP-GOV.5.2_GATE_AMBIENTE_E_PROTOCOLO_MEMORIA_20260716.md`
4. `docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md`
5. `docs/history/ptp/CHECKPOINT_HISTORICO_COMPLETO_PTP-GOV.5_ARQUITETURA_V2.5_V2.7_20260716.md`
6. `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md`
7. `docs/history/tests/TESTE_001_RESULTADO_20260716.md`
8. código e documentação técnica da branch `main`

## Regra de fonte oficial

```text
GitHub  = memória técnica e documental
Linear  = guia operacional de tarefas e bloqueios
ChatGPT = ambiente de análise e engenharia
```

Auditorias devem usar exclusivamente `leon337/predixai-robo-de-listas`. Dados de outros repositórios são `REJEITADO_POR_ESCOPO`.

## Estado atual

```text
Arquitetura conceitual dos 12 pontos .......... CONCLUÍDA
Revisões críticas arquiteturais ............... CONCLUÍDAS
Schema lógico SQLite .......................... CONGELADO CONCEITUALMENTE
Sequência V2.5–V2.7 ........................... CONGELADA CONCEITUALMENTE
PTM V2.5 ...................................... PRELIMINAR / NÃO RECONCILIADA
Histórico integral desta sessão ............... PUBLICADO NA PR #16
PTP-GOV.5 memória documental .................. EM VALIDAÇÃO
Teste 001 original ............................ FAIL_POR_CONECTOR_GITHUB_NAO_CONFIGURADO
Etapa 0 — ambiente ............................ PENDENTE DE REPETIÇÃO FORMAL
Teste A — acesso .............................. BLOQUEADO PELA ETAPA 0
Teste B — reconstrução ........................ BLOQUEADO POR 0/A
Teste C — continuidade ........................ BLOQUEADO POR 0/A/B
Auditoria Mestra V2.4.3-R1 .................... PAUSADA ATÉ VALIDAR MEMÓRIA
PTM V2.6 ...................................... NÃO INICIADA
PTM V2.7 ...................................... NÃO INICIADA
Documento Mestre .............................. NÃO GERADO
Implementação V2.5 ............................ NÃO AUTORIZADA
```

## Resultado oficial corrigido do primeiro experimento

```text
TESTE_001=FAIL_POR_CONECTOR_GITHUB_NAO_CONFIGURADO
REPOSITORIO_INDISPONIVEL=NAO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_INTERPRETACAO=NAO
FALHA_DE_AMBIENTE=SIM
CAUSA_RAIZ=PLUGIN_OU_CONECTOR_GITHUB_NAO_ADICIONADO_AO_CHAT
```

Depois que o conector GitHub foi adicionado ao chat de teste, o repositório e seus arquivos passaram a ser acessíveis. Portanto, a primeira falha não pode ser atribuída ao repositório nem à documentação.

## Protocolo vigente

```text
ETAPA 0 — VERIFICAÇÃO DO AMBIENTE
→ confirmar conector GitHub ativo, conta autorizada, repositório, branch e arquivos legíveis.

ETAPA A — ACESSO DOCUMENTAL
→ comprovar leitura real do conjunto oficial de três arquivos.

ETAPA B — RECONSTRUÇÃO
→ somente após 0/A=PASS, avaliar reconstrução do projeto.

ETAPA C — CONTINUIDADE
→ em outro chat novo, continuar exatamente da etapa correta.
```

## Conjunto oficial do Teste A

```text
1. PROJECT_STATE.md
2. docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
3. docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md
```

Qualquer lista anterior diferente desta está revogada para fins de gate.

## Próxima ação obrigatória

```text
1. Integrar a PR #16 após alinhamento documental.
2. Abrir chat novo sem memória ou checkpoint.
3. Adicionar/ativar o conector GitHub nesse chat.
4. Executar Etapa 0.
5. Com Etapa 0=PASS, executar Teste A.
6. Com A=PASS, executar Teste B.
7. Com B=PASS, executar Teste C em outro chat.
8. Registrar resultados no GitHub e Linear.
9. Somente então retomar a Auditoria Mestra V2.4.3-R1.
```

## Roadmap até o Documento Mestre

```text
🟧 PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória
⬜ Etapa 0 — verificar ambiente e conector GitHub
⬜ Teste A — acesso documental
⬜ Teste B — reconstrução do estado
⬜ Teste C — continuidade correta
⬜ Auditoria Mestra do legado V2.4.3-R1
⬜ Anexo A — Inventário real
⬜ Reconciliar e revisar PTM V2.5
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

- servidor é a fonte global oficial de estado;
- SQLite é acessado somente pelo servidor;
- escritas SQLite usam escritor único/fila central;
- REST consulta/comanda, WebSocket notifica e event bus comunica internamente;
- eventos críticos usam outbox transacional;
- Android e desktop são clientes sem acesso direto ao banco;
- Android é painel principal, mas não dependência de inicialização;
- listas manuais e programadas funcionam sem análise;
- análise, estratégia, sinal e execução permanecem separados;
- schema lógico é completo e schema físico progressivo;
- frequências e thresholds não medidos são `PROVISIONAL_BASELINE`;
- GitHub é a fonte das auditorias, inventários, validações e migrações;
- nenhuma implementação começa antes da Auditoria Mestra, PTMs e Documento Mestre.

## Estado real já confirmado

- aplicação desktop Python para Linux Mint/X11;
- base histórica em `app/main.py` com Tkinter, JSON, threads e `pynput`;
- modelos `Signal`, `ScheduleList`, `CoordinateProfile` e `PredixAIRoboListas`;
- persistência histórica em `config/config_predixai_robo_listas.json`;
- dependência confirmada `pynput==1.8.2`;
- HEAD atual possui `app/bootstrap_v243.py`, logs, backups, diagnóstico e reparo;
- README está parcialmente defasado em relação ao HEAD.

## Erros e decisões revogadas

### Repositório incorreto

Foi auditado por engano `leon337/predixai-platform`. Todas as conclusões foram invalidadas e são proibidas nesta PTP.

### Teste único de memória

Revogado. Acesso e reconstrução não podem ser avaliados no mesmo gate.

### Falha genérica de acesso

A classificação `FAIL_POR_FALTA_DE_ACESSO_AO_REPOSITORIO` foi refinada. A causa raiz confirmada foi `CONECTOR_GITHUB_NAO_CONFIGURADO`.

### Chat como memória principal

Revogado. GitHub é a memória oficial; checkpoints de chat são cópia de segurança.

## Proibições atuais

```text
NÃO iniciar implementação V2.5.
NÃO gerar SQL ou migrations físicas.
NÃO tratar a PTM como definitiva.
NÃO usar dados do predixai-platform.
NÃO misturar V2.4.3-R1 real com V2.5–V2.7 futura.
NÃO executar Teste A sem Etapa 0=PASS.
NÃO executar reconstrução se o Teste A falhar.
NÃO retomar a Auditoria Mestra antes dos gates de memória.
```

## Gate da etapa atual

```text
HISTORICO_INTEGRAL_PR_16=PASS
CAUSA_RAIZ_TESTE_001_CORRIGIDA=PASS
ETAPA_0_DOCUMENTADA=PASS
CONJUNTO_OFICIAL_TESTE_A_UNICO=PASS
MEMORY_ENVIRONMENT_GATE=PENDING
MEMORY_ACCESS_TEST_A=BLOCKED
MEMORY_RECONSTRUCTION_TEST_B=BLOCKED
MEMORY_CONTINUITY_TEST_C=BLOCKED
AUDITORIA_MESTRA=PAUSED
```