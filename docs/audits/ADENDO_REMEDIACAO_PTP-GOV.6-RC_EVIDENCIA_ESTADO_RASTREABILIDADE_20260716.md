# ADENDO DE REMEDIAÇÃO — PTP-GOV.6-RC

## Evidência integral, estado documental e rastreabilidade

## 1. Controle

```text
DOCUMENT_STATUS=REMEDIATION_COMPLETE_READY_FOR_REREVIEW
MISSION=PTP-GOV.6-RC
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
AUDIT_BRANCH=docs/ptp-gov-6-anexo-a
LINEAR_ISSUE=LEA-10
PULL_REQUEST=29
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PTM_V2_5_STARTED=NO
```

Este adendo responde aos três bloqueadores encontrados na primeira passagem da revisão crítica. Ele não aprova a própria revisão e não libera a PTM V2.5. Uma nova passagem independente ainda deve emitir `AUDITORIA_MESTRA_CRITICAL_REVIEW=PASS|FAIL`.

## 2. Evidência integral imutável

Artefato canônico versionado:

```text
docs/audits/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz.b64
```

Identidade verificada:

```text
BASE64_TEXT_LENGTH=15516
BASE64_GIT_BLOB_SHA1=07e516d837bbe7d715938433350a7d3910fcfff1
GZIP_SIZE_BYTES=11637
GZIP_SHA256=3fb6f033d624cad43eb6d1380076d2560de12c71b9f4a8d5702c0e8dbd41ef89
RAW_REPORT_SIZE_BYTES=36842
RAW_REPORT_LINE_COUNT=512
RAW_REPORT_SHA256=ac70a6bd4acfeb5b35bbfdbf15a7212247db9a8be438191463c54f4912b19428
```

Restauração no Linux Mint:

```bash
base64 -d docs/audits/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz.b64 \
  > /tmp/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz

gzip -dc /tmp/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz \
  > /tmp/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt

sha256sum /tmp/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt
wc -c -l /tmp/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt
```

Resultado esperado:

```text
SHA256=ac70a6bd4acfeb5b35bbfdbf15a7212247db9a8be438191463c54f4912b19428
SIZE_BYTES=36842
LINE_COUNT=512
```

O arquivo `docs/audits/EVIDENCIA_PTP-GOV.6_ARVORE_AST_20260716.txt` permanece como cópia textual não canônica. Para validação criptográfica, prevalece o artefato `.txt.gz.b64` identificado acima.

## 3. Reconciliação do estado documental

Os documentos abaixo registram passagens progressivas da coleta e são preservados como **snapshots imutáveis de trabalho**:

1. `ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md`;
2. `ANEXO_A_APENDICE_01_IMPORTS_SIMBOLOS_JSON_PTP-GOV.6_20260716.md`;
3. `ANEXO_A_APENDICE_02_TESTES_WORKFLOWS_ESTADOS_JSON_RAIZ_PTP-GOV.6_20260716.md`;
4. `ANEXO_A_APENDICE_03_HISTORICO_COMMITS_LIMITES_COLETA_PTP-GOV.6_20260716.md`.

Os marcadores `DRAFT_PARTIAL`, `PENDING` e `BLOCKED_BY_ENVIRONMENT` presentes nesses snapshots descrevem o estado no momento de cada passagem. Eles não representam o estado consolidado atual.

A autoridade de conclusão da entrega segue esta ordem:

```text
1. ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md
2. ANEXO_A_APENDICE_04_ARVORE_AST_DOCUMENTACAO_FINAL_PTP-GOV.6_20260716.md
3. PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz.b64
4. CHECKPOINT_PTP-GOV.6_ANEXO_A_DRAFT_COMPLETE_20260716.md
5. snapshots progressivos do documento pai e Apêndices 01–03
```

Estado consolidado:

```text
FULL_RECURSIVE_TREE_RECONCILIATION=PASS
FULL_ROOT_DIRECTORY_ENUMERATION=PASS
ALL_METHODS_AND_NESTED_FUNCTIONS_COUNT=PASS
ALL_DOCUMENT_FILES_INDIVIDUALLY_CLASSIFIED=PASS
COMMIT_HISTORY_EXHAUSTIVE_ENUMERATION=PASS
AUDITORIA_MESTRA_DRAFT_COMPLETE=PASS
AUDITORIA_MESTRA_CRITICAL_REVIEW=PENDING_REREVIEW
PR_29_MERGE=BLOCKED
PTM_V2_5_ADVANCE=BLOCKED
```

## 4. Contrato de herança dos campos obrigatórios

Cada linha ou conclusão classificatória do Anexo A e de seus apêndices deve ser lida com os campos locais da própria linha e com os metadados globais abaixo.

| Campo obrigatório | Regra de preenchimento por item |
|---|---|
| Fonte | arquivo real do repositório oficial ou evidência integral versionada |
| Caminho | valor da coluna `Item`, `Caminho`, `Arquivo`, `Workflow`, `Fonte/caminho` ou caminho citado na conclusão |
| Branch/commit | `main@0e2d7e98d863769be32a8bcb8b93684a61674aa3` |
| Evidência | descrição factual da linha, referência de símbolo/linha e seção correspondente do relatório bruto |
| Classificação | valor local `REUTILIZAR`, `ADAPTAR`, `SUBSTITUIR` ou `DESCONTINUAR` |
| Certeza | valor local; quando omitido, aplicar a matriz de família da seção 5 |
| Risco | valor local; quando omitido, aplicar a matriz de família da seção 5 |
| Rastreabilidade PTM | valor local; quando omitido, aplicar a matriz de família da seção 5 |

Este contrato não altera classificações existentes. Ele apenas elimina repetição e torna explícitos os campos herdados por todas as linhas.

## 5. Matriz complementar por família

| Família de itens | Evidência principal | Certeza padrão quando ausente | Risco padrão quando ausente | Rastreabilidade PTM V2.5 preliminar |
|---|---|---|---|---|
| `app/main.py` | símbolos, métodos e caminhos de clique no relatório AST e leitura direta | Alta | Alto; crítico para clique real | profiles, lists, schedules, calibration, runtime sessions; execução real não migra na V2.5 |
| `app/bootstrap_v21.py` a `bootstrap_v243.py` | grafo de imports, `install_patch` e índice AST | Alta | Alto para cadeia; crítico em V2.3.1 | decomposição de listas, perfis, sessões, diagnóstico e lifecycle; substituir monkey patching |
| `version_info.py` e `execution_preflight.py` | funções puras e testes associados | Alta | Baixo | metadata, component versions, validação temporal |
| `runtime_guard.py`, `config_safety.py`, `diagnostics_tools.py` | classes/funções, testes e scripts de runtime | Alta | Médio | instances, diagnostics, snapshots, backups e recovery |
| JSON schema 4 e artefatos locais | campos inventariados e caminhos definidos no código | Alta para estrutura estática | Alto | fonte de migração para profiles, lists, sessions e configuration snapshots; não é persistência final |
| `tests/` | sete arquivos e vinte testes enumerados | Alta | Médio | estratégia de testes, regressão e quality gates |
| `.github/workflows/` | nove workflows enumerados e cobertura cruzada | Alta | Médio | CI e quality gates; requer futura suíte agregada |
| `run.sh`, `install.sh`, `install_desktop.sh` | leitura direta dos scripts | Alta | Médio | packaging, instalação Linux e desktop client |
| `requirements.txt` | dependência `pynput==1.8.2` | Alta | Alto | dependency management; execução automática permanece bloqueada |
| `assets/logo_predixai.svg` | arquivo versionado e referência no instalador | Média | Baixo | identidade visual do desktop client |
| documentos vivos e protocolos | arquivos individualmente enumerados no Apêndice 04 | Alta | Baixo ou médio quando desatualizado | governança, operação e documentação; sem entidade runtime direta |
| documentos históricos | árvore integral e classificação individual | Alta | Baixo | memória e evidência; não define arquitetura futura isoladamente |
| `README.md` | divergência de versão e entrypoint | Alta | Alto | documentação operacional; substituir antes da entrega final |
| `CHANGELOG.md` | cobertura somente até V2.3.3 | Alta | Médio | histórico de releases; adaptar com evidência |
| árvore, índice AST e histórico de commits | artefato canônico `.txt.gz.b64` | Alta | Baixo de integridade | evidência de auditoria; não constitui arquitetura de produto |

## 6. Validação dos bloqueadores

```text
BLOCKER_1_RAW_EVIDENCE_UNAVAILABLE=RESOLVED
BLOCKER_2_CONFLICTING_DOCUMENT_STATUS=RESOLVED_BY_IMMUTABLE_SNAPSHOT_DECLARATION
BLOCKER_3_INCOMPLETE_REQUIRED_FIELDS=RESOLVED_BY_FIELD_INHERITANCE_CONTRACT_AND_FAMILY_MATRIX
CRITICAL_BLOCKERS_REMAINING_FOR_REREVIEW=0
```

## 7. Próxima ação

```text
1. manter PR #29 como Draft;
2. solicitar nova revisão independente;
3. validar a restauração e os hashes do artefato;
4. confirmar o contrato de herança em amostras de todas as famílias;
5. emitir AUDITORIA_MESTRA_CRITICAL_REVIEW=PASS|FAIL;
6. não iniciar PTM V2.5 antes de PASS e sincronização final.
```
