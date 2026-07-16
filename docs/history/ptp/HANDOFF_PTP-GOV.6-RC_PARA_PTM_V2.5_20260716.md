# HANDOFF — PTP-GOV.6-RC → PTM V2.5

## 1. Identificação

```text
PROJECT=PredixAI Robô de Listas
REPOSITORY=leon337/predixai-robo-de-listas
REAL_VERSION=V2.4.3-R1
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
PULL_REQUEST=29
COMPLETED_MISSION=PTP-GOV.6-RC
COMPLETED_LINEAR_ISSUE=LEA-10
NEXT_MISSION=PTM V2.5
NEXT_LINEAR_ISSUE=LEA-8
HANDOFF_STATUS=READY_AFTER_MERGE
```

## 2. Resultado encerrado

```text
AUDITORIA_MESTRA_DRAFT_COMPLETE=PASS
AUDITORIA_MESTRA_CRITICAL_REVIEW=PASS
CRITICAL_BLOCKERS=0
EVIDENCE_INTEGRITY=PASS
CLASSIFICATION_MATRIX=PASS
TRACEABILITY_MATRIX=PASS
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
```

## 3. Evidência canônica

```text
ARTIFACT=docs/audits/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz.b64
BASE64_GIT_BLOB_SHA1=07e516d837bbe7d715938433350a7d3910fcfff1
RAW_REPORT_SHA256=ac70a6bd4acfeb5b35bbfdbf15a7212247db9a8be438191463c54f4912b19428
RAW_REPORT_SIZE_BYTES=36842
RAW_REPORT_LINE_COUNT=512
```

## 4. Fontes obrigatórias da PTM V2.5

1. `PROJECT_STATE.md`;
2. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
3. `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md`;
4. Apêndices 01–04 do Anexo A;
5. `docs/audits/ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md`;
6. `docs/history/reviews/REVISAO_CRITICA_AUDITORIA_MESTRA_PTP-GOV.6_20260716.md`;
7. PTM V2.5 preliminar indicada pelos documentos históricos oficiais;
8. issue `LEA-8` no Linear.

## 5. Achados que devem ser preservados

```text
REAL_CLICK_IMPLEMENTATION=PRESENT
REAL_CLICK_RUNTIME=BLOCKED
PATCH_CHAIN=SUBSTITUIR
JSON_AS_FINAL_SOURCE_OF_TRUTH=SUBSTITUIR
JSON_AS_MIGRATION_SOURCE=ADAPTAR
README_VERSION_CONSISTENCY=FAIL
README_ENTRYPOINT_CONSISTENCY=FAIL
CHANGELOG_VERSION_COVERAGE=FAIL
AGGREGATED_FULL_TEST_SUITE_WORKFLOW=ABSENT
LINUX_X11_COUPLING=PRESENT
```

## 6. Escopo da próxima missão

A PTM V2.5 deve:

- reconciliar a arquitetura preliminar com o legado aprovado;
- revisar contratos, entidades, estados, lifecycle e persistência;
- separar requisitos preserváveis de mecanismos a substituir;
- manter execução real e clique real fora da V2.5;
- manter a PTM como documento arquitetural, sem implementação.

## 7. Proibições

```text
NÃO alterar código.
NÃO gerar SQL ou migrations.
NÃO executar a aplicação ou clique real.
NÃO tratar a PTM preliminar como definitiva antes da reconciliação.
NÃO avançar para PTM V2.6 antes de PTM_V2_5_CRITICAL_REVIEW=PASS.
NÃO usar outro repositório como fonte factual.
```

## 8. Condição de ativação

```text
PR_29_MERGED=PASS
LEA_10=DONE
PROJECT_STATE_UPDATED=PASS
TRUNK_UPDATED=PASS
LINEAR_UPDATED=PASS
```

Após esses gates, a `LEA-8` pode ser iniciada em novo chat com o comando `iniciar`.
