# CHECKPOINT — PTP-GOV.6

## Auditoria Mestra V2.4.3-R1 — Anexo A parcial

## 1. Identificação

```text
PROJECT=PredixAI Robô de Listas
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
WORK_BRANCH=docs/ptp-gov-6-anexo-a
DRAFT_PR=29
LINEAR_ISSUE=LEA-7
REAL_VERSION=V2.4.3-R1
ACTIVE_STAGE=PTP-GOV.6
FIRST_DELIVERABLE=ANEXO_A
CHECKPOINT_STATUS=MISSION_CONTINUES
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PTM_V2_5_STARTED=NO
```

## 2. Entregas publicadas

1. `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md`;
2. `docs/audits/ANEXO_A_APENDICE_01_IMPORTS_SIMBOLOS_JSON_PTP-GOV.6_20260716.md`;
3. `docs/audits/ANEXO_A_APENDICE_02_TESTES_WORKFLOWS_ESTADOS_JSON_RAIZ_PTP-GOV.6_20260716.md`.

Commits:

```text
f0fe0cf30e41b5069c0d9628704c8d5ee3565712
  docs(audit): iniciar Anexo A do legado V2.4.3-R1

eed19865fbb0ddd5ac9fd9cc0e0ac5d30851f3f3
  docs(audit): adicionar grafo de imports e schema JSON do legado

6d415f1481fe0e86de13dc92589c5ce86bb24bf9
  docs(audit): adicionar matrizes de testes, workflows, estados e JSON
```

## 3. Concluído nas passagens factuais

```text
REPOSITORY_AND_BASE_CONFIRMED=PASS
GITHUB_LINEAR_RECONCILIATION=PASS_WITH_DOCUMENT_GAPS
PRIMARY_ENTRYPOINT_CONFIRMED=PASS
APP_PYTHON_MODULES_CONFIRMED=17
TEST_FILES_CONFIRMED=7
TEST_FUNCTIONS_CONFIRMED=20
VERSIONED_WORKFLOWS_CONFIRMED=9
WORKFLOW_COVERED_TEST_FUNCTIONS=18/20
DIRECT_IMPORT_GRAPH=PASS_PRELIMINARY
CORE_SYMBOL_INDEX=PASS_PRELIMINARY
JSON_SCHEMA_4_INVENTORY=PASS_PRELIMINARY
JSON_FIELD_OPTIONALITY_MATRIX=PASS_PRELIMINARY
SIGNAL_TRANSITION_MATRIX=PASS_PRELIMINARY
SESSION_TRANSITION_MATRIX=PASS_PRELIMINARY
ROOT_FILE_INVENTORY=PASS_PRELIMINARY
DOCUMENT_CATEGORY_CLASSIFICATION=PASS_PRELIMINARY
RUNTIME_ARTIFACT_MODEL=PASS_PRELIMINARY
REAL_CLICK_PATHS=PASS
RUNTIME_VERSION_CONSISTENCY=PASS
DOCUMENTATION_ONLY_BRANCH=PASS
```

## 4. Achados críticos

### 4.1 Dois caminhos de clique real

1. teste de calibração em `app/main.py::_test_both_coordinates`;
2. execução agendada em `app/main.py::_execution_loop`, substituída por `app/bootstrap_v231.py::execution_loop`.

```text
CALIBRATION_REAL_CLICK=BLOCKED
SCHEDULED_REAL_CLICK=BLOCKED
REAL_CLICK_EXECUTED_DURING_AUDIT=NO
RISK=CRITICAL
```

### 4.2 Cadeia de monkey patching

O entrypoint instala patches sequenciais sobre `PredixAIRoboListas`. A ordem de instalação é dependência comportamental.

Classificação: `SUBSTITUIR` o mecanismo, preservando comportamentos úteis como requisitos de regressão.

### 4.3 Persistência

O legado usa `config/config_predixai_robo_listas.json`, schema 4, com perfis, listas, sinais e histórico de sessões.

Classificação: `ADAPTAR` como fonte de migração e `SUBSTITUIR` como fonte global definitiva futura.

Achado adicional: `session_history` é carregado sem validação estrutural integral.

Nenhum banco, SQL ou migration foi criado.

### 4.4 Testes e workflows

```text
TEST_FUNCTION_TOTAL=20
TEST_FUNCTIONS_MAPPED_TO_WORKFLOWS=18
UNMAPPED_TEST_FUNCTIONS=2
UNMAPPED_TEST_FILE=tests/test_smoke.py
AGGREGATED_FULL_TEST_SUITE_WORKFLOW=ABSENT
```

A validação é fragmentada por versão. Nenhum dos nove workflows executa a suíte completa.

### 4.5 Divergências documentais

```text
README_VERSION_CONSISTENCY=FAIL
README_ENTRYPOINT_CONSISTENCY=FAIL
CHANGELOG_VERSION_COVERAGE=FAIL
MULTICHAT_TRUNK_LEA_11_SYNC=FAIL
```

- `README.md` declara `1.0.0` e recomenda `python app/main.py`;
- `VERSION` contém `2.4.3`;
- o entrypoint real é `run.sh -> app/bootstrap_v23_entry.py`;
- `CHANGELOG.md` termina em `2.3.3`;
- o tronco multichat ainda registra `LEA_11=READY_FOR_DONE_AFTER_SYNC`.

### 4.6 Artefatos locais

`.gitignore` não cobre explicitamente:

```text
backups/
reports/
.runtime/
```

Risco: médio de versionamento acidental.

## 5. Classificações preliminares principais

```text
MAIN_UI_DOMAIN=ADAPTAR
PATCH_CHAIN=SUBSTITUIR
JSON_MIGRATION_SOURCE=ADAPTAR
JSON_FINAL_SOURCE_OF_TRUTH=SUBSTITUIR
RUNTIME_GUARD=ADAPTAR
CONFIG_SAFETY=ADAPTAR
DIAGNOSTICS=ADAPTAR
PURE_PREFLIGHT=REUTILIZAR
VERSION_READER=REUTILIZAR
PYNPUT_ACTIVE_EXECUTION=DESCONTINUAR_NO_BASELINE_V2_5
TEST_SUITE=ADAPTAR
VERSIONED_WORKFLOWS=ADAPTAR
HISTORICAL_DOCUMENTS=REUTILIZAR_AS_MEMORY_ONLY
README=SUBSTITUIR
CHANGELOG=ADAPTAR
```

## 6. Pendências obrigatórias

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
```

Pendências concluídas nesta retomada:

```text
TEST_FUNCTION_MATRIX=PASS
WORKFLOW_CROSS_COVERAGE_MATRIX=PASS
JSON_FIELD_OPTIONALITY_MATRIX=PASS_PRELIMINARY
STATUS_TRANSITION_MATRIX=PASS_PRELIMINARY
ROOT_FILE_INVENTORY=PASS_PRELIMINARY
DOCUMENT_CATEGORY_CLASSIFICATION=PASS_PRELIMINARY
```

## 7. Bloqueios e proibições

```text
TECHNICAL_BLOCKER=NONE
IMPLEMENTATION_V2_5=PROHIBITED
CODE_CHANGE=PROHIBITED_DURING_AUDIT
SQL=PROHIBITED
MIGRATIONS=PROHIBITED
REAL_CLICK_EXECUTION=PROHIBITED
PTM_V2_5_ADVANCE=BLOCKED
LEA_10_START=BLOCKED
PR_29_MERGE=BLOCKED_UNTIL_DRAFT_COMPLETE
```

## 8. Próxima ação exata

```text
1. Continuar na branch docs/ptp-gov-6-anexo-a e Draft PR #29.
2. Reconciliar a árvore recursiva e a enumeração integral da raiz.
3. Completar a contagem de métodos, funções e funções aninhadas.
4. Classificar individualmente a documentação restante.
5. Reconciliar o histórico de commits do legado.
6. Avaliar se validação estática adicional resolve os estados supersedidos sem executar clique real.
7. Corrigir README, CHANGELOG e tronco somente após fechar a coleta factual correspondente.
8. Não alterar código e não avançar para LEA-10.
```

## 9. Gate de checkpoint

```text
CHECKPOINT_DOCUMENTED=PASS
GITHUB_BRANCH_PRESERVED=PASS
DRAFT_PR_PRESERVED=PASS
LINEAR_SYNC_REQUIRED=YES
MISSION_COMPLETE=NO
NEXT_STAGE_UNLOCKED=NO
```
