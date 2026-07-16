# PROJECT_STATE — PredixAI Robô de Listas

## Autoridade documental

- **Projeto:** PredixAI Robô de Listas
- **Repositório oficial:** `leon337/predixai-robo-de-listas`
- **Branch técnica:** `main`
- **Versão real atual:** `V2.4.3-R1`
- **PTP ativa:** `PTP-GOV.5 — Memória e Governança Documental`
- **Mini-PTP concluída:** `PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória`
- **Etapa operacional atual:** Auditoria Mestra do legado V2.4.3-R1
- **Status:** MEMÓRIA VALIDADA — AUDITORIA MESTRA LIBERADA
- **Data:** 2026-07-16

## Leia nesta ordem

1. `PROJECT_STATE.md`
2. `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md`
3. `docs/history/ptp/PTP-GOV.5.2_GATE_AMBIENTE_E_PROTOCOLO_MEMORIA_20260716.md`
4. `docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md`
5. `docs/history/tests/MEMORY_GATES_0_A_B_RESULTADOS_20260716.md`
6. `docs/history/tests/MEMORY_CONTINUITY_TEST_C_RESULTADO_20260716.md`
7. `docs/history/ptp/CHECKPOINT_HISTORICO_COMPLETO_PTP-GOV.5_ARQUITETURA_V2.5_V2.7_20260716.md`
8. `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md`
9. código e documentação técnica da branch `main`

## Fonte oficial

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
Histórico integral ............................ PUBLICADO E INTEGRADO
Etapa 0 — ambiente ............................ PASS
Teste A — acesso documental ................... PASS
Teste B — reconstrução ........................ PASS
Teste C — continuidade ........................ PASS
Suite de memória .............................. PASS
Auditoria Mestra V2.4.3-R1 .................... LIBERADA / PRÓXIMA ETAPA
Anexo A — Inventário real ..................... NÃO INICIADO
PTM V2.6 ...................................... NÃO INICIADA
PTM V2.7 ...................................... NÃO INICIADA
Documento Mestre .............................. NÃO GERADO
Implementação V2.5 ............................ NÃO AUTORIZADA
```

## Resultado oficial dos gates

```text
MEMORY_ENVIRONMENT_GATE=PASS
MEMORY_ACCESS_TEST_A=PASS
FILES_REQUESTED=3
FILES_READ=3
MEMORY_RECONSTRUCTION_TEST_B=PASS
MEMORY_CONTINUITY_TEST_C=PASS
MEMORY_ACCEPTANCE_SUITE=PASS
FAILURE_CODES=NONE
AUDITORIA_MESTRA=READY_TO_RESUME
```

Evidências:

- `docs/history/tests/MEMORY_GATES_0_A_B_RESULTADOS_20260716.md`
- `docs/history/tests/MEMORY_CONTINUITY_TEST_C_RESULTADO_20260716.md`

## Próxima ação obrigatória

```text
1. Retomar a Auditoria Mestra da V2.4.3-R1.
2. Iniciar pelo inventário factual do Anexo A.
3. Para cada conclusão registrar: fonte, caminho, branch/commit, classificação e nível de certeza.
4. Classificar cada item como REUTILIZAR, ADAPTAR, SUBSTITUIR ou DESCONTINUAR.
5. Rastrear os achados contra a PTM V2.5 preliminar.
6. Não implementar nada durante a auditoria.
```

## Roadmap

```text
✅ PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória
✅ Etapa 0 — ambiente e conector GitHub
✅ Teste A — acesso documental
✅ Teste B — reconstrução do estado
✅ Teste C — continuidade correta
🟧 Auditoria Mestra do legado V2.4.3-R1
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
- nenhuma implementação começa antes da Auditoria Mestra, PTMs e Documento Mestre.

## Estado real já confirmado

- aplicação desktop Python para Linux Mint/X11;
- base histórica em `app/main.py` com Tkinter, JSON, threads e `pynput`;
- modelos `Signal`, `ScheduleList`, `CoordinateProfile` e `PredixAIRoboListas`;
- persistência histórica em `config/config_predixai_robo_listas.json`;
- dependência confirmada `pynput==1.8.2`;
- HEAD possui `app/bootstrap_v243.py`, logs, backups, diagnóstico e reparo;
- README está parcialmente defasado em relação ao HEAD.

## Proibições atuais

```text
NÃO iniciar implementação V2.5.
NÃO gerar SQL ou migrations físicas.
NÃO tratar a PTM como definitiva.
NÃO usar dados do predixai-platform.
NÃO misturar V2.4.3-R1 real com V2.5–V2.7 futura.
NÃO alterar código durante a Auditoria Mestra.
```

## Gate atual

```text
HISTORICO_INTEGRAL_PR_16=PASS
MEMORY_GATES_0_A_B_PR_17=PASS
MEMORY_CONTINUITY_TEST_C=PASS
MEMORY_ACCEPTANCE_SUITE=PASS
AUDITORIA_MESTRA=READY_TO_RESUME
ANEXO_A_INVENTARIO_REAL=PENDING
IMPLEMENTACAO=NAO_AUTORIZADA
```