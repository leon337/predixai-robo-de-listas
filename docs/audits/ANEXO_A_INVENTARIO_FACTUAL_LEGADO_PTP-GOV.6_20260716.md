# ANEXO A — INVENTÁRIO FACTUAL DO LEGADO

## PTP-GOV.6 — Auditoria Mestra V2.4.3-R1

## 1. Controle documental

```text
DOCUMENT_STATUS=DRAFT_PARTIAL
AUDIT_STAGE=PTP-GOV.6
REAL_VERSION=V2.4.3-R1
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
AUDIT_BRANCH=docs/ptp-gov-6-anexo-a
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PTM_V2_5_STARTED=NO
```

Este documento é um inventário factual inicial do legado. Não declara a Auditoria Mestra concluída e não transforma a PTM V2.5 preliminar em arquitetura definitiva.

## 2. Método e limites

Fontes utilizadas:

1. arquivos reais da branch `main` no commit-base indicado;
2. `PROJECT_STATE.md` e protocolos oficiais;
3. documentos históricos apenas como memória e referência conceitual;
4. issue `LEA-7` no Linear para estado operacional.

Método aplicado:

- busca de arquivos no repositório oficial;
- leitura direta de arquivos com `fetch_file`;
- confronto de entrypoint, imports, persistência, execução, testes e automações;
- classificação preliminar `REUTILIZAR`, `ADAPTAR`, `SUBSTITUIR` ou `DESCONTINUAR`.

Limite atual:

- a contagem abaixo foi confirmada por busca indexada e leitura direta;
- a enumeração recursiva integral da árvore ainda deve ser reconciliada antes do gate final;
- logs, backups, relatórios e JSON são artefatos de runtime ignorados ou gerados localmente e não foram executados nesta auditoria.

## 3. Resumo factual inicial

```text
APP_PYTHON_MODULES_CONFIRMED=17
TEST_FILES_CONFIRMED=7
VERSIONED_VALIDATION_WORKFLOWS_CONFIRMED=9
PRIMARY_RUNTIME_ENTRYPOINT=run.sh -> app/bootstrap_v23_entry.py
BASE_UI_AND_LEGACY_DOMAIN=app/main.py
LOCAL_PERSISTENCE=config/config_predixai_robo_listas.json
CONFIG_SCHEMA_CURRENT=4
REAL_CLICK_IMPLEMENTATION=PRESENT
REAL_CLICK_EXECUTED_DURING_AUDIT=NO
DATABASE_IMPLEMENTATION=PRESENT=NO_EVIDENCE
REST_IMPLEMENTATION=PRESENT=NO_EVIDENCE
WEBSOCKET_IMPLEMENTATION=PRESENT=NO_EVIDENCE
```

## 4. Cadeia real de inicialização

```text
run.sh
→ ativa .venv
→ python app/bootstrap_v23_entry.py
→ configura logging rotativo
→ adquire lock de instância única
→ executa diagnóstico mínimo
→ instala patches V2.2, V2.3, V2.3.1, V2.3.2, V2.3.3, runtime V2.3.3, V2.4.2 e V2.4.3
→ chama app.main.main()
→ abre interface Tkinter
```

Evidências principais:

- `run.sh` executa `app/bootstrap_v23_entry.py`;
- `app/bootstrap_v23_entry.py` instala a cadeia de patches e chama `app_main.main()`;
- `app/main.py` contém a classe principal Tkinter, modelos de dados, persistência JSON e execução por coordenadas.

Classificação da cadeia: `SUBSTITUIR` como mecanismo arquitetural, preservando comportamentos úteis por testes e migração controlada.

Certeza: alta.

Risco: alto, devido ao acoplamento por substituição dinâmica de métodos e dependência da ordem de instalação.

Rastreabilidade PTM preliminar: servidor/clientes, lifecycle, configuração, listas, perfis, calibração, diagnóstico e execução futura.

## 5. Inventário factual de `app/`

Base aplicável a todas as linhas: `main@0e2d7e98d863769be32a8bcb8b93684a61674aa3`.

| Item | Evidência factual | Classificação | Certeza | Risco | Rastreabilidade PTM preliminar |
|---|---|---|---|---|---|
| `app/main.py` | Monólito Tkinter com `Signal`, `ScheduleList`, `CoordinateProfile`, UI, JSON, histórico, thread e clique por `pynput`. | ADAPTAR | Alta | Alto | perfis, listas, calibração, runtime, execução |
| `app/version_info.py` | Lê `VERSION` com fallback explícito. | REUTILIZAR | Alta | Baixo | metadata e component versions |
| `app/execution_preflight.py` | Função pura que separa sinais expirados e futuros. | REUTILIZAR | Alta | Baixo | validação de agenda e lifecycle |
| `app/runtime_guard.py` | Lock com `fcntl`, logs rotativos e diagnóstico mínimo de startup. | ADAPTAR | Alta | Médio | server instances, dependency checks, diagnostics |
| `app/config_safety.py` | Backup, escrita atômica, retenção de dez cópias e recuperação de JSON. | ADAPTAR | Alta | Médio | configuration snapshots, backups, recovery |
| `app/diagnostics_tools.py` | Coleta ambiente, exporta relatório TXT, abre pastas com `xdg-open` e executa instalador. | ADAPTAR | Alta | Médio | diagnostics, reports, compatibility |
| `app/bootstrap_v21.py` | Corrige seleção e rótulo de listas por nome e data. | SUBSTITUIR | Alta | Médio | lists e schedules |
| `app/bootstrap_v22.py` | Separa listas de perfis, introduz JSON schema 4 e histórico estruturado. | SUBSTITUIR | Alta | Alto | lists, schedules, runtime sessions, migration source |
| `app/bootstrap_v22_entry.py` | Ajusta seleção, exclusão e apresentação de perfis independentes. | SUBSTITUIR | Alta | Médio | profiles e calibration |
| `app/bootstrap_v23.py` | Refina direção, agenda, gestão contextual e histórico mestre-detalhe. | SUBSTITUIR | Alta | Médio | lists, signals, UX desktop |
| `app/bootstrap_v231.py` | Implementa pausa, retomada, cancelamento e loop determinístico que envia clique real. | SUBSTITUIR | Alta | Crítico | execution lifecycle; execução futura somente após gate próprio |
| `app/bootstrap_v232.py` | Executa preflight temporal e registra ciclo estruturado de sessão. | SUBSTITUIR | Alta | Médio | runtime sessions, state transitions, signal validation |
| `app/bootstrap_v233.py` | Exibe versão e torna histórico por sessão mais responsivo. | SUBSTITUIR | Alta | Baixo | metadata e desktop client |
| `app/bootstrap_v233_runtime.py` | Finaliza título da janela usando versão publicada. | SUBSTITUIR | Alta | Baixo | metadata e desktop client |
| `app/bootstrap_v242.py` | Envolve carga e salvamento com backup e recuperação. | SUBSTITUIR | Alta | Médio | configuration snapshots e backups |
| `app/bootstrap_v243.py` | Adiciona telas de diagnóstico, ferramentas e informações da versão. | SUBSTITUIR | Alta | Médio | diagnostics e desktop client |
| `app/bootstrap_v23_entry.py` | Entrypoint protegido com lock, diagnóstico, logging e instalação ordenada dos patches. | ADAPTAR | Alta | Alto | lifecycle, diagnostics e composição da aplicação |

### 5.1 Decisão sobre `app/main.py`

O arquivo não pode receber classificação única sem decomposição funcional:

- modelos e regras de lista/perfil: `ADAPTAR`;
- UI desktop e calibração: `ADAPTAR`;
- persistência JSON como fonte final de verdade: `SUBSTITUIR` progressivamente;
- clique real e movimentação automática do mouse: `DESCONTINUAR` no baseline V2.5 e manter bloqueado até etapa futura explicitamente autorizada;
- histórico estruturado: `ADAPTAR` para persistência e contratos futuros.

## 6. Persistência e artefatos de runtime

| Item | Fonte/caminho | Evidência | Classificação | Certeza | Risco | PTM preliminar |
|---|---|---|---|---|---|---|
| Configuração principal | `config/config_predixai_robo_listas.json` | `app/main.py` define o caminho; V2.2 grava schema 4 com perfis, listas e sessões. | ADAPTAR | Alta | Alto | migration source, profiles, lists, runtime sessions |
| Backups | `backups/config/config_*.json` | `ConfigSafetyManager` cria, valida e poda backups. | ADAPTAR | Alta | Médio | backups e configuration snapshots |
| Cópia corrompida | `backups/config/corrompido_*.json` | recuperação preserva JSON inválido antes de restaurar backup. | ADAPTAR | Alta | Médio | recovery e diagnostics |
| Logs | `logs/predixai_robo_listas.log` | logger rotativo de 1 MB com cinco backups. | ADAPTAR | Alta | Médio | diagnostics e audit trail |
| Relatórios | `reports/diagnostico_v243_*.txt` | exportação local de diagnóstico. | ADAPTAR | Alta | Baixo | diagnostic snapshots e reports |
| Lock | `.runtime/predixai_robo_listas.lock` | lock não bloqueante com PID. | ADAPTAR | Alta | Médio | server/runtime instance |

### 6.1 Observação de segurança do versionamento

`.gitignore` protege `.venv`, caches, logs, `.env` e `config/*.json`, mas não declara explicitamente padrões para `backups/`, `reports/` e `.runtime/`.

Classificação: `ADAPTAR`.

Risco: médio, pois artefatos locais podem ser adicionados acidentalmente se não houver revisão antes do commit.

## 7. Execução real por coordenadas

Fatos confirmados:

- `requirements.txt` fixa `pynput==1.8.2`;
- `app/main.py` importa `Controller` e `Button`;
- o loop posiciona o mouse e envia clique esquerdo;
- `app/bootstrap_v231.py` mantém esse comportamento em uma versão mais controlada;
- histórico registra coordenadas e resultado `CLIQUE_ENVIADO`.

Classificação:

```text
PYNPUT_ACTIVE_EXECUTION=DESCONTINUAR_NO_BASELINE_V2_5
LEGACY_BEHAVIOR_REFERENCE=REUTILIZAR_COMO_EVIDENCIA
REAL_CLICK_RUNTIME=BLOCKED
```

Certeza: alta.

Risco: crítico.

Rastreabilidade PTM preliminar: execução pertence à etapa futura V2.7 e não pode ser antecipada pela PTM V2.5.

## 8. Scripts e instalação

| Caminho | Evidência | Classificação | Certeza | Risco |
|---|---|---|---|---|
| `run.sh` | Ativa `.venv` e usa o entrypoint protegido. | ADAPTAR | Alta | Baixo |
| `install.sh` | Cria `.venv`, atualiza pip e instala `requirements.txt`. | ADAPTAR | Alta | Médio |
| `install_desktop.sh` | Instala ícone e `.desktop` no ambiente Linux. | ADAPTAR | Alta | Médio |
| `requirements.txt` | Declara apenas `pynput==1.8.2`; Tkinter é dependência de sistema. | SUBSTITUIR | Alta | Alto |
| `assets/logo_predixai.svg` | Referenciado pelo instalador desktop. | REUTILIZAR | Média | Baixo |

A compatibilidade observada é Linux/X11. `runtime_guard.py` usa `fcntl` e `diagnostics_tools.py` usa `xdg-open`; portanto compatibilidade Windows não está implementada no legado confirmado.

## 9. Testes confirmados

Arquivos localizados:

1. `tests/test_smoke.py`;
2. `tests/test_version_info.py`;
3. `tests/test_runtime_guard.py`;
4. `tests/test_config_safety.py`;
5. `tests/test_v242_patch_chain.py`;
6. `tests/test_execution_preflight.py`;
7. `tests/test_diagnostics_tools.py`.

Classificação do conjunto: `ADAPTAR`.

Pontos fortes:

- funções puras e utilitários possuem testes;
- lock, logging, diagnóstico, versão, backup e preflight possuem evidência automatizada;
- existe teste de integração da cadeia V2.4.2.

Lacunas preliminares:

- nenhuma evidência localizada de teste automatizado completo da UI Tkinter;
- nenhuma evidência localizada de teste end-to-end seguro do fluxo de agenda sem clique real;
- `tests/test_smoke.py` verifica apenas presença de `app/main.py` e declaração de `pynput`;
- a cobertura do monólito e da ordem total dos patches ainda precisa ser reconciliada.

## 10. Workflows confirmados

Workflows versionados localizados:

```text
v21-validate.yml
v22-validate.yml
v23-validate.yml
v231-validate.yml
v232-validate.yml
v233-validate.yml
v241-validate.yml
v242-validate.yml
v243-validate.yml
```

Classificação: `ADAPTAR`.

Achado:

- a validação é fragmentada por versão;
- o workflow V2.4.3 valida sintaxe e testes de diagnóstico, integração textual e valor de `VERSION`;
- não há evidência no workflow V2.4.3 de execução agregada de todos os sete arquivos de teste.

Risco: médio.

Recomendação futura: consolidar uma suíte principal sem apagar evidências históricas dos workflows versionados.

## 11. Documentação e divergências

### 11.1 README

Fatos:

- `README.md` declara versão `1.0.0`;
- `VERSION` contém `2.4.3`;
- o README recomenda `python app/main.py` para execução manual;
- `run.sh` utiliza `app/bootstrap_v23_entry.py`, que aplica as proteções e patches atuais.

Classificação: `SUBSTITUIR` por uma versão atualizada e coerente com o entrypoint real.

Risco: alto, pois seguir a execução manual documentada ignora a cadeia atual.

### 11.2 Tronco multichat

Fato:

- `PROJECT_STATE.md` e o Linear registram `LEA-11` concluída;
- `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` ainda registra `LEA_11=READY_FOR_DONE_AFTER_SYNC`.

Classificação: `ADAPTAR` por correção documental na mesma branch da auditoria ou em sincronização dedicada.

Risco: baixo operacional, médio de continuidade documental.

### 11.3 Documentos históricos

Classificação: `REUTILIZAR` como memória histórica e referência de decisões, sem tratá-los como prova isolada do código atual.

## 12. Matriz preliminar de risco

| Risco | Severidade | Evidência | Tratamento recomendado |
|---|---|---|---|
| Clique real presente no legado | Crítico | `main.py`, `bootstrap_v231.py`, `requirements.txt` | manter bloqueado; isolar e descontinuar no baseline V2.5 |
| README aponta entrypoint incorreto | Alto | `README.md` versus `run.sh` | corrigir documentação antes do fechamento |
| Monkey patching em cadeia | Alto | bootstraps instalados sequencialmente | substituir por composição explícita e testes de regressão |
| JSON como fonte local única | Alto | schema 4 em `bootstrap_v22.py` | tratar como fonte de migração; não criar SQL nesta etapa |
| Compatibilidade Linux específica | Médio | `fcntl`, `xdg-open`, scripts Bash | adaptar por portas e abstrações futuras |
| Workflows fragmentados | Médio | nove workflows versionados | consolidar validação principal mantendo histórico |
| Artefatos não cobertos explicitamente no `.gitignore` | Médio | backups, reports e `.runtime` | revisar padrões antes de qualquer publicação de runtime |
| Tronco documental desatualizado | Médio | estado da LEA-11 | sincronizar documento vivo |

## 13. Rastreabilidade preliminar com PTM V2.5

| Legado confirmado | Destino conceitual preliminar | Estado |
|---|---|---|
| `CoordinateProfile` | profiles, monitor/application profiles, calibration | RECONCILIAR |
| coordenadas `LARANJA` e `CINZA` | click targets | BLOQUEADO PARA EXECUÇÃO; geometria pode ser migrada |
| resolução e escala | compatibility checks e monitor profiles | RECONCILIAR |
| `ScheduleList` e `Signal` | lists, list items, schedules e signal candidates | RECONCILIAR |
| JSON schema 4 | fonte de migração para configuração e histórico | RECONCILIAR |
| `session_history` | runtime sessions, transitions e execution history | RECONCILIAR |
| logs e diagnóstico | diagnostic snapshots, alerts e audit trail | RECONCILIAR |
| backups JSON | backup catalog e configuration snapshots | RECONCILIAR |
| clique por `pynput` | execução futura V2.7 | NÃO MIGRAR NA V2.5 |
| Tkinter desktop | cliente desktop de calibração e diagnóstico | ADAPTAR |

Esta tabela é rastreabilidade preliminar, não especificação definitiva.

## 14. Pendências para completar o Anexo A

```text
FULL_RECURSIVE_TREE_RECONCILIATION=PENDING
ALL_ROOT_FILES_RECONCILIATION=PENDING
ALL_DOCS_CLASSIFICATION=PENDING
ALL_TEST_FUNCTIONS_MATRIX=PENDING
ALL_WORKFLOW_CROSS_COVERAGE=PENDING
IMPORT_GRAPH_COMPLETE=PENDING
FUNCTION_AND_CLASS_INDEX_COMPLETE=PENDING
JSON_FIELD_LEVEL_INVENTORY=PENDING
COMMIT_HISTORY_RECONCILIATION=PENDING
BACKUP_LOG_RUNTIME_SAMPLE_EXECUTION=NOT_AUTHORIZED_NOT_EXECUTED
README_CORRECTION=PENDING
TRUNK_SYNC=PENDING
CRITICAL_REVIEW=NOT_STARTED
```

## 15. Gate atual

```text
AUDIT_INITIALIZATION=PASS
PRIMARY_ENTRYPOINT_CONFIRMED=PASS
REAL_VERSION_CONFIRMED=PASS
APP_PRIMARY_MODULE_INVENTORY=PASS_PRELIMINARY
TEST_FILE_INVENTORY=PASS_PRELIMINARY
WORKFLOW_INVENTORY=PASS_PRELIMINARY
RUNTIME_ARTIFACT_MODEL=PASS_PRELIMINARY
CLASSIFICATION_MATRIX=PASS_PRELIMINARY
AUDITORIA_MESTRA_DRAFT_COMPLETE=PENDING
AUDITORIA_MESTRA_CRITICAL_REVIEW=NOT_STARTED
```

Próxima ação: reconciliar árvore integral, imports, funções/classes, JSON em nível de campos, testes/workflows e documentação antes de declarar o rascunho completo.