# ANEXO A — APÊNDICE 04

## Árvore integral, contagem AST, documentação individual e fechamento factual

## 1. Controle

```text
DOCUMENT_STATUS=DRAFT_COMPLETE
PARENT_DOCUMENT=ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
AUDIT_BRANCH=docs/ptp-gov-6-anexo-a
LINEAR_ISSUE=LEA-7
DRAFT_PR=29
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PTM_V2_5_STARTED=NO
```

Este apêndice fecha as pendências factuais do Anexo A usando o relatório local somente leitura gerado diretamente do banco de objetos Git.

## 2. Identidade da evidência

```text
RAW_REPORT_FILENAME=PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt
RAW_REPORT_SHA256=ac70a6bd4acfeb5b35bbfdbf15a7212247db9a8be438191463c54f4912b19428
RAW_REPORT_SIZE_BYTES=36842
RAW_REPORT_LINE_COUNT=512
COLLECTION_METHOD=GIT_OBJECT_DATABASE
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
LOCAL_HEAD_UNCHANGED=YES
WORKTREE_STATUS_PRESERVED=YES
AST_PARSE_ERROR_COUNT=0
```

Manifesto versionado:

```text
docs/audits/EVIDENCIA_PTP-GOV.6_ARVORE_AST_20260716.txt
```

Certeza: alta.

Risco de integridade residual: baixo, controlado pelo SHA-256 e pela confirmação de preservação do repositório local.

## 3. Reconciliação numérica integral

```text
TRACKED_FILE_COUNT=82
ROOT_FILE_COUNT=11
WORKFLOW_FILE_COUNT=9
APP_FILE_COUNT=17
ASSET_FILE_COUNT=1
CONFIG_FILE_COUNT=1
DOCS_DIRECTORY_FILE_COUNT=36
TEST_FILE_COUNT=7

PYTHON_FILE_COUNT=24
DOCUMENTATION_FILE_COUNT=41
SHELL_FILE_COUNT=3
YAML_FILE_COUNT=9
SVG_FILE_COUNT=1
TXT_FILE_COUNT=1
NO_EXTENSION_FILE_COUNT=3
```

Equações:

```text
11 + 9 + 17 + 1 + 1 + 36 + 7 = 82
17 app Python + 7 test Python = 24 Python
5 Markdown na raiz + 36 Markdown em docs = 41 Markdown
```

```text
FULL_RECURSIVE_TREE_RECONCILIATION=PASS
FULL_ROOT_DIRECTORY_ENUMERATION=PASS
CATEGORY_COUNT_RECONCILIATION=PASS
EXTENSION_COUNT_RECONCILIATION=PASS
```

## 4. Árvore integral por grupo

### 4.1 Raiz — 11 arquivos

```text
.gitignore
CHANGELOG.md
PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md
PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md
PROJECT_STATE.md
README.md
VERSION
install.sh
install_desktop.sh
requirements.txt
run.sh
```

### 4.2 Workflows — 9 arquivos

```text
.github/workflows/v21-validate.yml
.github/workflows/v22-validate.yml
.github/workflows/v23-validate.yml
.github/workflows/v231-validate.yml
.github/workflows/v232-validate.yml
.github/workflows/v233-validate.yml
.github/workflows/v241-validate.yml
.github/workflows/v242-validate.yml
.github/workflows/v243-validate.yml
```

### 4.3 Aplicação — 17 arquivos

```text
app/bootstrap_v21.py
app/bootstrap_v22.py
app/bootstrap_v22_entry.py
app/bootstrap_v23.py
app/bootstrap_v231.py
app/bootstrap_v232.py
app/bootstrap_v233.py
app/bootstrap_v233_runtime.py
app/bootstrap_v23_entry.py
app/bootstrap_v242.py
app/bootstrap_v243.py
app/config_safety.py
app/diagnostics_tools.py
app/execution_preflight.py
app/main.py
app/runtime_guard.py
app/version_info.py
```

### 4.4 Ativo e configuração versionada — 2 arquivos

```text
assets/logo_predixai.svg
config/.gitkeep
```

### 4.5 Testes — 7 arquivos

```text
tests/test_config_safety.py
tests/test_diagnostics_tools.py
tests/test_execution_preflight.py
tests/test_runtime_guard.py
tests/test_smoke.py
tests/test_v242_patch_chain.py
tests/test_version_info.py
```

### 4.6 Documentação em `docs/` — 36 arquivos

```text
docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md
docs/history/20260715_V1_DESKTOP_E_MEMORIA.md
docs/history/20260715_V2.1_LISTAS_DATAS_ESTABILIDADE.md
docs/history/20260715_V2.2_LISTAS_INDEPENDENTES_HISTORICO.md
docs/history/20260715_V2.3.1_CONTROLE_EXECUCAO.md
docs/history/20260715_V2.3.2_EXPIRADOS_E_SESSAO.md
docs/history/20260715_V2.3.3_VERSAO_CABECALHO_HISTORICO.md
docs/history/20260715_V2.3_UX_LISTAS_HISTORICO.md
docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md
docs/history/ptp/CHECKPOINT_FINAL_MIGRACAO_PROJETO_LIMPO_20260716.md
docs/history/ptp/CHECKPOINT_HISTORICO_COMPLETO_PTP-GOV.5_ARQUITETURA_V2.5_V2.7_20260716.md
docs/history/ptp/CHECKPOINT_LEA-11_RUNTIME_R1_R5_20260716.md
docs/history/ptp/FECHAMENTO_LEA-11_RUNTIME_R1_R6_20260716.md
docs/history/ptp/PTP-GOV.5.1_PROTOCOLO_ACESSO_RECONSTRUCAO_20260716.md
docs/history/ptp/PTP-GOV.5.2_GATE_AMBIENTE_E_PROTOCOLO_MEMORIA_20260716.md
docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
docs/history/reviews/REVISAO_COMPLETUDE_HISTORICO_PTP-GOV.5_20260716.md
docs/history/reviews/REVISAO_CRITICA_MELHORIAS_OPERACIONAIS_LEVES_20260716.md
docs/history/reviews/REVISAO_CRITICA_MIGRACAO_PROJETO_LIMPO_20260716.md
docs/history/reviews/REVISAO_CRITICA_VALIDACAO_ESTATICA_PROTOCOLOS_20260716.md
docs/history/tests/CLEAN_PROJECT_ACCEPTANCE_RESULTADO_20260716.md
docs/history/tests/MEMORY_CONTINUITY_TEST_C_RESULTADO_20260716.md
docs/history/tests/MEMORY_GATES_0_A_B_RESULTADOS_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R1_R2_RESULTADO_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R3_RESULTADO_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R4_RESULTADO_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R5_RESULTADO_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R6_RESULTADO_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R7_RESULTADO_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_STATUS_20260716.md
docs/history/tests/PROTOCOL_ACCEPTANCE_STATIC_VALIDATION_20260716.md
docs/history/tests/TESTE_001_RESULTADO_20260716.md
docs/protocols/PREDIXAI_ROBO_LISTAS_RESPONSE_MODEL.md
docs/protocols/PREDIXAI_ROBO_LISTAS_RUNTIME_TEST_PLAN.md
docs/protocols/PREDIXAI_ROBO_LISTAS_SKILLS.md
docs/roadmap/V2_UI_COMPACTA.md
```

## 5. Índice AST integral

```text
PYTHON_FILE_COUNT=24
AST_CLASS_COUNT=18
AST_METHOD_COUNT=90
AST_FUNCTION_COUNT=95
AST_NESTED_FUNCTION_COUNT=15
AST_SYMBOL_TOTAL=218
AST_PARSE_ERROR_COUNT=0
```

Equação:

```text
18 + 90 + 95 + 15 = 218
```

Distribuição factual:

- os 17 arquivos de `app/` contêm o núcleo, bootstraps, guardas, persistência e diagnóstico;
- os 7 arquivos de `tests/` contêm classes auxiliares, casos `unittest`, funções `pytest` e funções aninhadas de teste;
- todos os 24 arquivos Python foram analisados sem erro de parse;
- o relatório bruto contém caminho, nome qualificado e linha de cada símbolo.

```text
ALL_METHODS_AND_NESTED_FUNCTIONS_COUNT=PASS
PYTHON_PARSE_COMPLETENESS=PASS
```

Classificação do índice AST: `REUTILIZAR` como inventário e evidência; não constitui decisão arquitetural definitiva.

## 6. Histórico integral

```text
COMMIT_HISTORY_COUNT=158
FIRST_COMMIT=4eb79db76596aed1b258c09396574ba0a4ca78de
LAST_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
HISTORY_ORDER=CHRONOLOGICAL_ASCENDING
COMMIT_HISTORY_EXHAUSTIVE_ENUMERATION=PASS
```

O relatório confirma a sequência completa desde a criação da V1, evolução V2, hotfix V2.4.3-R1 e transição para governança.

Classificação: `REUTILIZAR` como evidência cronológica, sempre subordinada ao conteúdo real do commit-base.

## 7. Classificação individual dos 41 documentos Markdown

| Caminho | Classificação | Uso factual | Risco |
|---|---|---|---|
| `README.md` | SUBSTITUIR | instrução pública desatualizada | Alto |
| `CHANGELOG.md` | ADAPTAR | completar versões posteriores à V2.3.3 | Médio |
| `PROJECT_STATE.md` | ADAPTAR | atualizar para rascunho concluído e revisão crítica | Médio |
| `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` | ADAPTAR | corrigir estado histórico da LEA-11 e continuidade | Médio |
| `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md` | REUTILIZAR | autoridade operacional atual | Baixo |
| `docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md` | REUTILIZAR | critérios de memória e continuidade | Baixo |
| `docs/history/20260715_V1_DESKTOP_E_MEMORIA.md` | REUTILIZAR | memória histórica V1 | Baixo |
| `docs/history/20260715_V2.1_LISTAS_DATAS_ESTABILIDADE.md` | REUTILIZAR | memória histórica V2.1 | Baixo |
| `docs/history/20260715_V2.2_LISTAS_INDEPENDENTES_HISTORICO.md` | REUTILIZAR | memória histórica V2.2 | Baixo |
| `docs/history/20260715_V2.3_UX_LISTAS_HISTORICO.md` | REUTILIZAR | memória histórica V2.3 | Baixo |
| `docs/history/20260715_V2.3.1_CONTROLE_EXECUCAO.md` | REUTILIZAR | memória de pausa/cancelamento | Médio |
| `docs/history/20260715_V2.3.2_EXPIRADOS_E_SESSAO.md` | REUTILIZAR | memória de preflight e sessões | Baixo |
| `docs/history/20260715_V2.3.3_VERSAO_CABECALHO_HISTORICO.md` | REUTILIZAR | memória de versão e UI | Baixo |
| `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md` | REUTILIZAR | referência conceitual preliminar | Médio |
| `docs/history/ptp/CHECKPOINT_FINAL_MIGRACAO_PROJETO_LIMPO_20260716.md` | REUTILIZAR | checkpoint histórico | Baixo |
| `docs/history/ptp/CHECKPOINT_HISTORICO_COMPLETO_PTP-GOV.5_ARQUITETURA_V2.5_V2.7_20260716.md` | REUTILIZAR | memória arquitetural preliminar | Médio |
| `docs/history/ptp/CHECKPOINT_LEA-11_RUNTIME_R1_R5_20260716.md` | REUTILIZAR | evidência de continuidade runtime | Baixo |
| `docs/history/ptp/FECHAMENTO_LEA-11_RUNTIME_R1_R6_20260716.md` | REUTILIZAR | fechamento histórico parcial | Baixo |
| `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md` | REUTILIZAR | governança documental anterior | Baixo |
| `docs/history/ptp/PTP-GOV.5.1_PROTOCOLO_ACESSO_RECONSTRUCAO_20260716.md` | REUTILIZAR | protocolo histórico de acesso | Baixo |
| `docs/history/ptp/PTP-GOV.5.2_GATE_AMBIENTE_E_PROTOCOLO_MEMORIA_20260716.md` | REUTILIZAR | gate anterior aprovado | Baixo |
| `docs/history/reviews/REVISAO_COMPLETUDE_HISTORICO_PTP-GOV.5_20260716.md` | REUTILIZAR | evidência de revisão | Baixo |
| `docs/history/reviews/REVISAO_CRITICA_MELHORIAS_OPERACIONAIS_LEVES_20260716.md` | REUTILIZAR | decisões operacionais | Baixo |
| `docs/history/reviews/REVISAO_CRITICA_MIGRACAO_PROJETO_LIMPO_20260716.md` | REUTILIZAR | revisão da migração | Baixo |
| `docs/history/reviews/REVISAO_CRITICA_VALIDACAO_ESTATICA_PROTOCOLOS_20260716.md` | REUTILIZAR | revisão dos protocolos | Baixo |
| `docs/history/tests/CLEAN_PROJECT_ACCEPTANCE_RESULTADO_20260716.md` | REUTILIZAR | prova de aceitação da pasta limpa | Baixo |
| `docs/history/tests/MEMORY_CONTINUITY_TEST_C_RESULTADO_20260716.md` | REUTILIZAR | prova de continuidade | Baixo |
| `docs/history/tests/MEMORY_GATES_0_A_B_RESULTADOS_20260716.md` | REUTILIZAR | provas dos gates iniciais | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R1_R2_RESULTADO_20260716.md` | REUTILIZAR | evidência runtime R1/R2 | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R3_RESULTADO_20260716.md` | REUTILIZAR | evidência runtime R3 | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R4_RESULTADO_20260716.md` | REUTILIZAR | evidência runtime R4 | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R5_RESULTADO_20260716.md` | REUTILIZAR | evidência runtime R5 | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R6_RESULTADO_20260716.md` | REUTILIZAR | evidência runtime R6 | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_R7_RESULTADO_20260716.md` | REUTILIZAR | evidência runtime R7 | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_RUNTIME_STATUS_20260716.md` | REUTILIZAR | consolidação do runtime | Baixo |
| `docs/history/tests/PROTOCOL_ACCEPTANCE_STATIC_VALIDATION_20260716.md` | REUTILIZAR | prova de validação estática | Baixo |
| `docs/history/tests/TESTE_001_RESULTADO_20260716.md` | REUTILIZAR | registro da falha e causa raiz | Baixo |
| `docs/protocols/PREDIXAI_ROBO_LISTAS_RESPONSE_MODEL.md` | REUTILIZAR | modelo oficial de resposta | Baixo |
| `docs/protocols/PREDIXAI_ROBO_LISTAS_RUNTIME_TEST_PLAN.md` | REUTILIZAR | plano oficial de testes | Baixo |
| `docs/protocols/PREDIXAI_ROBO_LISTAS_SKILLS.md` | REUTILIZAR | catálogo operacional de Skills | Baixo |
| `docs/roadmap/V2_UI_COMPACTA.md` | REUTILIZAR | referência histórica de requisitos de UI | Baixo |

```text
ALL_DOCUMENT_FILES_INDIVIDUALLY_CLASSIFIED=PASS
DOCUMENTATION_REUTILIZAR_COUNT=37
DOCUMENTATION_ADAPTAR_COUNT=3
DOCUMENTATION_SUBSTITUIR_COUNT=1
DOCUMENTATION_DESCONTINUAR_COUNT=0
DOCUMENTATION_CLASSIFICATION_TOTAL=41
```

## 8. Validações diferidas sem falsa alegação

O commit-base contém apenas `config/.gitkeep`; não contém amostra JSON operacional versionada. Além disso, executar a aplicação ou alcançar estados de clique real é proibido nesta auditoria.

```text
REAL_JSON_SAMPLE_VALIDATION=DEFERRED_NON_BLOCKING_NO_VERSIONED_SAMPLE
RUNTIME_STATE_REACHABILITY_VALIDATION=DEFERRED_NON_BLOCKING_EXECUTION_PROHIBITED
REAL_CLICK_RUNTIME_VALIDATION=PROHIBITED
```

Essas ausências permanecem registradas como risco e insumo da revisão crítica; não invalidam o inventário estático integral.

## 9. Correções documentais derivadas

```text
README_CORRECTION=REMEDIATION_PENDING_AFTER_INVENTORY
CHANGELOG_COMPLETION=REMEDIATION_PENDING_AFTER_INVENTORY
TRUNK_SYNC=REMEDIATION_PENDING_AFTER_INVENTORY
PROJECT_STATE_UPDATE=REMEDIATION_PENDING_AFTER_INVENTORY
```

Essas correções são consequência do inventário, não evidência necessária para fechar a coleta factual. Devem ser avaliadas na revisão crítica antes de merge definitivo.

## 10. Gate final do Anexo A

```text
REPOSITORY_AND_BASE_CONFIRMED=PASS
FULL_RECURSIVE_TREE_RECONCILIATION=PASS
FULL_ROOT_DIRECTORY_ENUMERATION=PASS
APP_INVENTORY=PASS
ENTRYPOINT_INVENTORY=PASS
JSON_AND_RUNTIME_ARTIFACT_INVENTORY=PASS
TEST_AND_WORKFLOW_INVENTORY=PASS
SCRIPT_AND_ROOT_FILE_INVENTORY=PASS
DIRECT_IMPORT_GRAPH=PASS_PRELIMINARY
ALL_METHODS_AND_NESTED_FUNCTIONS_COUNT=PASS
ALL_DOCUMENT_FILES_INDIVIDUALLY_CLASSIFIED=PASS
COMMIT_HISTORY_EXHAUSTIVE_ENUMERATION=PASS
CLASSIFICATION_MATRIX=PASS
EVIDENCE_INTEGRITY=PASS_WITH_SHA256
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
AUDITORIA_MESTRA_DRAFT_COMPLETE=PASS
PTP_GOV_6_RC_READY=YES
PTM_V2_5_STARTED=NO
```

## 11. Próxima etapa

```text
NEXT_STAGE=PTP-GOV.6-RC
LINEAR_NEXT_ISSUE=LEA-10
PR_29_MERGE=BLOCKED_PENDING_CRITICAL_REVIEW
AUDITORIA_MESTRA_CRITICAL_REVIEW=NOT_STARTED
```

A revisão crítica deve validar consistência, suficiência, riscos, classificações e remediações documentais antes de qualquer merge ou avanço para PTM V2.5.