# PROMPT — RETESTE CRÍTICO INDEPENDENTE LEA-51 PÓS-REMEDIAÇÃO

```text
MISSION=LEA-51_RETEST
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=69
BRANCH=leonpcsn/lea-50-roadmap-implementacao-v1
REVIEW_HEAD=OBTER_DO_HEAD_ATUAL_DO_PR_69_E_FIXAR_NO_COMENTARIO_DE_INICIO
PREVIOUS_REVIEW_HEAD=8aebab96d7ca98b183e5973384df2cba28eabd83
PREVIOUS_DECISION=FAIL_ONE_MAJOR
RETEST_FINDINGS=LEA-51-F01
BUILDER_MUST_DIFFER_FROM_REVIEWER=YES
MERGE_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

## Procedimento obrigatório

1. Ler o HEAD atual do PR Draft #69 e publicar esse SHA exato no comentário de início do reteste antes de analisar.
2. Confirmar que o PR permanece Draft e que o HEAD não mudou durante a revisão.
3. Reexecutar `python3 scripts/validate_lea50_documental.py`.
4. Revisar criticamente as limitações declaradas pelo validador; não converter especificação documental em prova de execução.
5. Validar separadamente os três achados abaixo e registrar `PASS` ou `FAIL` para cada um.

## LEA-51-F01

- `builder_issue=LEA-50`;
- `review_issue=LEA-51`;
- `observed_pr_head=8aebab96d7ca98b183e5973384df2cba28eabd83` como snapshot do último HEAD efetivamente retestado;
- `implementation_pr_head=8aebab96d7ca98b183e5973384df2cba28eabd83`;
- LEA-50 e LEA-51 em `In Progress` nas projeções operacionais;
- `ready_for_independent_retest=true`, `current_product_issue=LEA-50` e `current_review_issue=LEA-51`;
- histórico de LEA-46/47/48 e PR #66 isolado em `fnd_002_history`;
- novo HEAD de reteste fixado externamente no GitHub e Linear.

## Achados já aprovados no reteste anterior

- `LEA-51-F02=PASS` e `LEA-51-F03=PASS` foram confirmados no HEAD `8aebab96d7ca98b183e5973384df2cba28eabd83` e só devem ser reabertos se houver regressão objetiva.

## Saída esperada do revisor

```text
REVIEW_HEAD=<SHA_EXATO_FIXADO>
PULL_REQUEST=69
DECISION=PASS|FAIL
LEA_51_F01=PASS|FAIL
LEA_51_F02=PASS|FAIL
LEA_51_F03=PASS|FAIL
OPEN_BLOCKING_FINDINGS=<N>
MERGE_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

O builder deve apenas preparar o reteste e parar. O reteste não autoriza merge nem FND-003.
