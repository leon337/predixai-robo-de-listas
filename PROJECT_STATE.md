# PROJECT_STATE — PredixAI Robô de Listas

## Autoridade documental

- **Projeto:** PredixAI Robô de Listas
- **Repositório oficial:** `leon337/predixai-robo-de-listas`
- **Branch técnica:** `main`
- **Versão real atual:** `V2.4.3-R1`
- **PTP ativa:** `PTP-GOV.5 — Memória e Governança Documental`
- **Mini-PTP ativa:** `PTP-GOV.5.1 — Protocolo Acesso → Reconstrução`
- **Status:** ATIVO
- **Data:** 2026-07-16

## Leia nesta ordem

1. `PROJECT_STATE.md`
2. `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md`
3. `docs/history/ptp/PTP-GOV.5.1_PROTOCOLO_ACESSO_RECONSTRUCAO_20260716.md`
4. `docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md`
5. `docs/history/tests/TESTE_001_RESULTADO_20260716.md`
6. documentação técnica e código da branch `main`

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
PTP-GOV.5 memória documental .................. EM VALIDAÇÃO
Teste 001 original ............................ FAIL_POR_FALTA_DE_ACESSO
Teste A — acesso .............................. PENDENTE
Teste B — reconstrução ......................... BLOQUEADO PELO TESTE A
Teste C — continuidade ......................... BLOQUEADO PELOS TESTES A/B
Auditoria Mestra V2.4.3-R1 .................... PAUSADA ATÉ VALIDAR MEMÓRIA
PTM V2.6 ...................................... NÃO INICIADA
PTM V2.7 ...................................... NÃO INICIADA
Documento Mestre .............................. NÃO GERADO
Implementação V2.5 ............................ NÃO AUTORIZADA
```

## Resultado oficial do primeiro experimento

```text
TESTE_001=FAIL_POR_FALTA_DE_ACESSO_AO_REPOSITORIO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_INTERPRETACAO=NAO
FALHA_DE_ACESSO=SIM
```

O chat novo não conseguiu abrir o conteúdo real do GitHub. Portanto, a qualidade da documentação ainda não foi testada.

## Protocolo vigente

```text
ETAPA A — ACESSO
→ comprovar leitura real dos arquivos obrigatórios.

ETAPA B — RECONSTRUÇÃO
→ somente após A=PASS, avaliar a reconstrução do projeto.

ETAPA C — CONTINUIDADE
→ em outro chat novo, continuar exatamente da etapa correta.
```

A Etapa B não pode ser julgada quando a Etapa A falhar.

## Próxima ação obrigatória

```text
1. Executar o Teste A — Acesso com o prompt oficial.
2. Se A=PASS, executar o Teste B — Reconstrução.
3. Se B=PASS, executar o Teste C — Continuidade.
4. Registrar resultados no GitHub e Linear.
5. Somente então retomar a Auditoria Mestra V2.4.3-R1.
```

## Roadmap até o Documento Mestre

```text
🟧 PTP-GOV.5.1 — Protocolo Acesso → Reconstrução
⬜ Teste A — acesso ao conteúdo real
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

O protocolo que avaliava acesso e reconstrução ao mesmo tempo foi revogado. Foi substituído pelo fluxo Acesso → Reconstrução → Continuidade.

### Chat como memória principal

Revogado. GitHub é a memória oficial; checkpoints de chat são cópia de segurança.

## Proibições atuais

```text
NÃO iniciar implementação V2.5.
NÃO gerar SQL ou migrations físicas.
NÃO tratar a PTM como definitiva.
NÃO usar dados do predixai-platform.
NÃO misturar V2.4.3-R1 real com V2.5–V2.7 futura.
NÃO executar reconstrução se o teste de acesso falhar.
NÃO retomar a Auditoria Mestra antes dos gates de memória.
```

## Gate da etapa atual

```text
TESTE_001_RESULTADO_REGISTRADO=PASS
PROTOCOLO_DUAS_ETAPAS_DOCUMENTADO=PASS
MEMORY_ACCESS_TEST_A=PENDING
MEMORY_RECONSTRUCTION_TEST_B=BLOCKED
MEMORY_CONTINUITY_TEST_C=BLOCKED
AUDITORIA_MESTRA=PAUSED
```
