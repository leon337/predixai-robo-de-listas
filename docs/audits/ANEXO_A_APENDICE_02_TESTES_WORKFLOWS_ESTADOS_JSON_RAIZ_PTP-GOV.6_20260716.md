# ANEXO A — APÊNDICE 02

## Testes, workflows, transições de estado, opcionalidade JSON e arquivos raiz

## 1. Controle

```text
DOCUMENT_STATUS=DRAFT_PARTIAL
PARENT_DOCUMENT=ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
AUDIT_BRANCH=docs/ptp-gov-6-anexo-a
CODE_CHANGED=NO
RUNTIME_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
```

Este apêndice amplia o inventário factual sem declarar a Auditoria Mestra concluída. As conclusões abaixo derivam de leitura direta dos arquivos reais da `main` no commit-base indicado.

## 2. Matriz integral dos testes confirmados

| Arquivo | Funções de teste confirmadas | Quantidade | Workflow que executa | Classificação | Risco residual |
|---|---|---:|---|---|---|
| `tests/test_smoke.py` | `test_main_exists`; `test_requirements_declares_pynput` | 2 | nenhum workflow localizado | ADAPTAR | Médio |
| `tests/test_version_info.py` | `test_reads_version_file`; `test_missing_version_file_uses_fallback`; `test_empty_version_file_uses_fallback` | 3 | `v233-validate.yml` | REUTILIZAR | Baixo |
| `tests/test_runtime_guard.py` | `test_single_instance_lock_blocks_second_instance`; `test_configure_logging_creates_rotating_log`; `test_startup_diagnostics_passes_with_required_structure`; `test_startup_diagnostics_reports_missing_paths` | 4 | `v241-validate.yml` | ADAPTAR | Médio |
| `tests/test_config_safety.py` | `test_atomic_write_creates_backup`; `test_corrupt_config_recovers_latest_valid_backup`; `test_invalid_config_without_backup_is_preserved_for_diagnostics`; `test_backup_rotation_keeps_limit` | 4 | `v242-validate.yml` | ADAPTAR | Médio |
| `tests/test_v242_patch_chain.py` | `test_safe_load_delegates_to_previous_loader`; `test_safe_save_preserves_previous_serializer` | 2 | `v242-validate.yml` | ADAPTAR | Médio |
| `tests/test_execution_preflight.py` | `test_separa_expirados_e_futuros`; `test_lista_totalmente_expirada` | 2 | `v232-validate.yml` | REUTILIZAR | Baixo |
| `tests/test_diagnostics_tools.py` | `test_read_version`; `test_collect_diagnostics_reports_missing_files`; `test_export_report` | 3 | `v243-validate.yml` | ADAPTAR | Baixo |

Resumo numérico:

```text
TEST_FILES_CONFIRMED=7
TEST_FUNCTIONS_CONFIRMED=20
TEST_FUNCTIONS_EXECUTED_BY_VERSIONED_WORKFLOWS=18
TEST_FUNCTIONS_WITHOUT_WORKFLOW_EXECUTION=2
UNMAPPED_TEST_FILE=tests/test_smoke.py
```

### 2.1 Cobertura factual existente

Cobertura automatizada confirmada:

- leitura de versão e fallbacks;
- lock de instância única;
- criação de log rotativo;
- diagnóstico mínimo de startup;
- backup e recuperação de JSON;
- retenção de backups;
- delegação da cadeia V2.4.2;
- separação temporal de sinais expirados e futuros;
- coleta e exportação de diagnóstico.

Lacunas confirmadas:

- nenhuma suíte integral da interface Tkinter;
- nenhuma validação automatizada da ordem completa de todos os patches;
- nenhum teste end-to-end seguro da agenda com o envio de clique bloqueado ou simulado;
- nenhuma validação agregada de todos os 20 testes em uma única execução;
- os dois testes de `test_smoke.py` não são executados pelos workflows localizados.

## 3. Matriz dos workflows versionados

| Workflow | Escopo factual | Testes executados | Cobertura estrutural | Limite principal |
|---|---|---|---|---|
| `v21-validate.yml` | sintaxe de `main.py` e JSON opcional | nenhum | `py_compile` e parse condicional do JSON | não valida comportamento |
| `v22-validate.yml` | sintaxe V2.2, scripts Bash, versão e JSON opcional | nenhum | `main`, bootstraps V2.2 e scripts | não executa testes |
| `v23-validate.yml` | sintaxe da cadeia V2.3, scripts e marcadores textuais | nenhum | `grep` de recursos V2.3 | validação textual frágil |
| `v231-validate.yml` | sintaxe, versão e marcadores de pausa/cancelamento | nenhum | `grep` do controle de execução | não valida loop em runtime |
| `v232-validate.yml` | preflight temporal e marcadores de sessão | 2 | teste unitário de `execution_preflight` | não valida UI nem thread |
| `v233-validate.yml` | versão e integração visual do histórico | 3 | teste unitário de versão e `grep` | não valida widgets em runtime |
| `v241-validate.yml` | lock, logging e diagnóstico de startup | 4 | testes unitários de runtime | dependência Linux por `fcntl` |
| `v242-validate.yml` | configuração segura e wrappers da cadeia | 6 | testes de backup, recuperação e delegação | não valida cadeia completa |
| `v243-validate.yml` | diagnóstico, tela de ferramentas, versão publicada | 3 | sintaxe, testes e marcadores textuais | executa somente testes de diagnóstico |

Conclusão:

```text
VERSIONED_WORKFLOWS_CONFIRMED=9
WORKFLOWS_WITH_UNIT_TEST_EXECUTION=5
WORKFLOWS_WITHOUT_UNIT_TEST_EXECUTION=4
AGGREGATED_FULL_TEST_SUITE_WORKFLOW=ABSENT
LATEST_WORKFLOW_RUNS_ALL_TESTS=NO
```

Classificação do conjunto: `ADAPTAR`.

Destino preliminar: preservar evidências históricas e criar futuramente uma suíte principal agregada, sem executar ou alterar código durante esta auditoria.

## 4. Cobertura cruzada teste × workflow

```text
v232 -> test_execution_preflight.py .......... 2/2
v233 -> test_version_info.py ................. 3/3
v241 -> test_runtime_guard.py ................ 4/4
v242 -> test_config_safety.py ................ 4/4
       + test_v242_patch_chain.py ............ 2/2
v243 -> test_diagnostics_tools.py ............ 3/3
nenhum -> test_smoke.py ...................... 0/2
```

```text
DISTINCT_TEST_FUNCTIONS_COVERED_ACROSS_ALL_WORKFLOWS=18/20
DISTINCT_TEST_FILES_COVERED_ACROSS_ALL_WORKFLOWS=6/7
SINGLE_WORKFLOW_COMPLETE_COVERAGE=0/9
```

Certeza: alta.

Risco: médio, pois a fragmentação pode permitir regressões fora do recorte validado pelo workflow mais recente.

## 5. Matriz de opcionalidade do JSON schema 4

Arquivo operacional: `config/config_predixai_robo_listas.json`.

### 5.1 Campos de topo

| Campo | Escrita atual | Leitura atual | Obrigatoriedade factual | Risco |
|---|---|---|---|---|
| `version` | sempre `4` | `payload.get("version") == 4` | obrigatório para selecionar explicitamente o schema 4; ausente aciona caminho legado | Alto |
| `active_profile_id` | sempre presente, pode ser `null` | `get` | opcional/nullable | Baixo |
| `active_list_id` | sempre presente, pode ser `null` | `get` | opcional/nullable | Baixo |
| `profiles` | sempre lista | `get(..., [])` | opcional na leitura; lista vazia por padrão | Médio |
| `lists` | sempre lista | `get(..., [])` | opcional na leitura; lista vazia por padrão | Médio |
| `legacy_history` | sempre lista limitada a 1000 | `get(..., [])` | opcional na leitura | Baixo |
| `session_history` | sempre lista limitada a 500 | `get(..., [])` | opcional na leitura, sem validação estrutural integral | Alto |

### 5.2 Perfil

| Campo | Obrigatoriedade factual | Fallback observado |
|---|---|---|
| `id` | obrigatório | acesso direto `item["id"]` |
| `name` | obrigatório | acesso direto `item["name"]` |
| `application` | opcional | `platform` ou `Aplicação` |
| `monitor` | opcional | `Tela principal` |
| `resolution` | opcional | string vazia |
| `scale` | opcional | string vazia |
| `coordinates` | opcional | `LARANJA/CINZA = null` |
| `updated_at` | opcional | string vazia |
| `validated` | opcional | `False` |
| `lists` | ignorado no schema 4 | substituído por lista vazia; listas ficam no topo |

### 5.3 Lista

| Campo | Obrigatoriedade factual | Fallback observado |
|---|---|---|
| `id` | obrigatório | acesso direto |
| `name` | obrigatório | acesso direto |
| `date_str` | obrigatório | acesso direto |
| `signals` | opcional | lista vazia |
| `updated_at` | opcional | string vazia |
| `description` | opcional | string vazia |
| `created_at` | opcional | `updated_at` ou timestamp atual |
| `archived` | opcional | `False` |

### 5.4 Sinal

| Campo | Obrigatoriedade factual | Observação |
|---|---|---|
| `id` | obrigatório | construtor `Signal(**signal)` |
| `date_str` | obrigatório | construtor |
| `time_str` | obrigatório | construtor |
| `direction` | obrigatório | construtor |
| `status` | opcional | dataclass usa `AGENDADO` como padrão |

### 5.5 Sessão e evento

As sessões são gravadas com:

```text
id
started_at
finished_at
profile_id
profile_name
list_id
list_name
list_date
status
events
```

Os eventos são gravados com:

```text
at
status
detail
```

Fato crítico: `session_history` é carregado como lista bruta, sem validação de schema. A leitura da UI usa majoritariamente `.get`, tornando campos tolerados como ausentes, porém sem garantir integridade semântica.

```text
SESSION_HISTORY_SCHEMA_VALIDATION=ABSENT
EVENT_SCHEMA_VALIDATION=ABSENT
REAL_JSON_SAMPLE_VALIDATION=NOT_EXECUTED
```

Classificação: `ADAPTAR` como fonte de migração; `SUBSTITUIR` como persistência definitiva futura.

## 6. Matriz de transições de sinal

| Origem | Destino | Condição factual | Caminho |
|---|---|---|---|
| criação/cópia | `AGENDADO` | sinal preparado para sessão | `main.py`, `bootstrap_v22.py` |
| `AGENDADO` | `EXECUTANDO` | relógio alcança horário e atraso é aceitável | `bootstrap_v231.py::execution_loop` |
| `AGENDADO` | `EXPIRADO` | atraso superior a 30 segundos | `bootstrap_v231.py::execution_loop` |
| `EXECUTANDO` | `AGENDADO` | pausa durante a janela anterior ao clique | `bootstrap_v231.py::execution_loop` |
| `EXECUTANDO` | `CLIQUE_ENVIADO` | clique esquerdo enviado | `bootstrap_v231.py::execution_loop` |
| `AGENDADO`/`EXECUTANDO` | `CANCELADO` | cancelamento manual | `bootstrap_v231.py::stop_execution` |
| `EXECUTANDO` | `ERRO` | exceção no loop | `bootstrap_v231.py::execution_loop` |
| preparação prévia | `EXPIRADO` | lista totalmente vencida antes do início | `bootstrap_v232.py::start_execution` |

Risco crítico: a transição para `CLIQUE_ENVIADO` representa ação física real e permanece bloqueada nesta auditoria.

## 7. Matriz de transições de sessão

| Origem | Destino | Condição factual | Situação na cadeia final |
|---|---|---|---|
| inexistente | `EM_EXECUÇÃO` | preflight aprovado e sessão criada antes da thread | ativa em V2.3.2 |
| inexistente | `EXPIRADA` | todos os sinais já venceram | ativa em V2.3.2 |
| `EM_EXECUÇÃO` | `FINALIZADO` | não existem sinais pendentes | confirmada pelo fechamento herdado |
| `EM_EXECUÇÃO` | `CANCELADO` | cancelamento manual na cadeia final V2.3.2 sobre V2.3.1 | ativa |
| `EM_EXECUÇÃO` | `EXPIRADA` | mudança temporal entre preflight e início impede execução | ativa |
| `EM_EXECUÇÃO` | `ERRO` | erro propagado ao handler estruturado | confirmada |
| `EM_EXECUÇÃO` | `ENCERRADO` | definido no patch V2.2 | caminho supersedido pela cadeia V2.3.1/V2.3.2; alcance final não confirmado |

Estados textuais adicionais presentes na UI, mas não equivalentes necessariamente ao status persistido de sessão:

```text
PRONTO
PAUSADO
EM EXECUÇÃO
LISTA EXPIRADA
CANCELADO
FINALIZADO
```

Conclusão:

```text
SIGNAL_TRANSITION_MATRIX=PASS_PRELIMINARY
SESSION_TRANSITION_MATRIX=PASS_PRELIMINARY
UNREACHABLE_OR_SUPERSEDED_STATE_PATHS_REQUIRE_RUNTIME_VALIDATION=YES
RUNTIME_VALIDATION_EXECUTED=NO
```

## 8. Arquivos raiz confirmados e classificação

Esta seção registra arquivos raiz confirmados por leitura direta ou referência factual do runtime. Não substitui a enumeração recursiva integral ainda pendente.

| Arquivo | Responsabilidade factual | Classificação | Certeza | Risco |
|---|---|---|---|---|
| `.gitignore` | ignora ambiente, caches, logs, `.env` e JSON de configuração; não cobre explicitamente `backups/`, `reports/` e `.runtime/` | ADAPTAR | Alta | Médio |
| `README.md` | documentação V1, versão e entrypoint desatualizados | SUBSTITUIR | Alta | Alto |
| `CHANGELOG.md` | histórico até V2.3.3 | ADAPTAR | Alta | Médio |
| `VERSION` | contém `2.4.3` e é lido pelo runtime | REUTILIZAR | Alta | Baixo |
| `requirements.txt` | fixa somente `pynput==1.8.2` | SUBSTITUIR progressivamente | Alta | Alto |
| `run.sh` | ativa `.venv` e executa o entrypoint protegido | ADAPTAR | Alta | Baixo |
| `install.sh` | cria `.venv`, atualiza pip e instala requisitos | ADAPTAR | Alta | Médio |
| `install_desktop.sh` | instala ícone e arquivo `.desktop` no Linux | ADAPTAR | Alta | Médio |
| `PROJECT_STATE.md` | estado oficial vivo | REUTILIZAR e manter atualizado | Alta | Baixo |
| `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md` | autoridade operacional permanente | REUTILIZAR | Alta | Baixo |
| `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` | continuidade e roadmap; contém divergência da LEA-11 | ADAPTAR | Alta | Médio |
| `assets/logo_predixai.svg` | identidade visual usada pelo instalador | REUTILIZAR | Média | Baixo |

```text
ROOT_FILE_INVENTORY_CONFIRMED=PASS_PRELIMINARY
FULL_ROOT_DIRECTORY_ENUMERATION=PENDING
```

## 9. Classificação documental por categoria

| Categoria | Exemplos confirmados | Classificação | Regra |
|---|---|---|---|
| documentos vivos | `PROJECT_STATE.md`, instruções, tronco e protocolos | REUTILIZAR/ADAPTAR | atualizar quando o estado mudar |
| histórico PTP e checkpoints concluídos | `docs/history/ptp/` | REUTILIZAR | memória imutável; corrigir por adendo |
| revisões históricas | `docs/history/reviews/` | REUTILIZAR | evidência de gates anteriores |
| resultados de testes de protocolo | `docs/history/tests/` | REUTILIZAR | prova histórica, não substitui código atual |
| roadmap legado | `docs/roadmap/V2_UI_COMPACTA.md` | REUTILIZAR COMO HISTÓRICO | não tratar como arquitetura V2.5 definitiva |
| documentação de uso atual | `README.md` | SUBSTITUIR | alinhar versão e entrypoint |
| registro de versões | `CHANGELOG.md` | ADAPTAR | complementar 2.4.1–2.4.3 somente com evidência |

```text
DOCUMENT_CATEGORY_CLASSIFICATION=PASS_PRELIMINARY
ALL_DOCUMENT_FILES_INDIVIDUALLY_CLASSIFIED=PENDING
```

## 10. Achados consolidados desta passagem

```text
TEST_FUNCTION_MATRIX=PASS
WORKFLOW_CROSS_COVERAGE_MATRIX=PASS
TEST_FUNCTION_TOTAL=20
WORKFLOW_COVERED_TEST_FUNCTION_TOTAL=18
JSON_FIELD_OPTIONALITY_MATRIX=PASS_PRELIMINARY
SIGNAL_TRANSITION_MATRIX=PASS_PRELIMINARY
SESSION_TRANSITION_MATRIX=PASS_PRELIMINARY
ROOT_FILE_INVENTORY=PASS_PRELIMINARY
DOCUMENT_CATEGORY_CLASSIFICATION=PASS_PRELIMINARY
CODE_CHANGED=NO
```

## 11. Pendências remanescentes

```text
FULL_RECURSIVE_TREE_RECONCILIATION=PENDING
FULL_ROOT_DIRECTORY_ENUMERATION=PENDING
ALL_DOCUMENT_FILES_INDIVIDUALLY_CLASSIFIED=PENDING
ALL_METHODS_AND_NESTED_FUNCTIONS_COUNT=PENDING
COMMIT_HISTORY_RECONCILIATION=PENDING
REAL_JSON_SAMPLE_VALIDATION=NOT_EXECUTED
RUNTIME_STATE_REACHABILITY_VALIDATION=NOT_EXECUTED
README_CORRECTION=PENDING
CHANGELOG_COMPLETION=PENDING
TRUNK_SYNC=PENDING
PROJECT_STATE_UPDATE_FOR_DRAFT=PENDING
AUDITORIA_MESTRA_DRAFT_COMPLETE=PENDING
AUDITORIA_MESTRA_CRITICAL_REVIEW=NOT_STARTED
```

## 12. Gate do apêndice

```text
APPENDIX_02_FACTUAL_COLLECTION=PASS
TEST_AND_WORKFLOW_MATRIX=PASS
JSON_OPTIONALITY=PASS_PRELIMINARY
STATE_TRANSITIONS=PASS_PRELIMINARY
ROOT_AND_DOCS_CLASSIFICATION=PASS_PRELIMINARY
MISSION_COMPLETE=NO
NEXT_STAGE_UNLOCKED=NO
```
