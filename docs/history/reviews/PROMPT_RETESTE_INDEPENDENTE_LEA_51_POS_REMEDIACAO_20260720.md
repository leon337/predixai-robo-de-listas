# PROMPT — RETESTE CRÍTICO INDEPENDENTE LEA-51 PÓS-REMEDIAÇÃO

```text
MISSION=LEA-51_RETEST
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=69
BRANCH=leonpcsn/lea-50-roadmap-implementacao-v1
REVIEW_HEAD=OBTER_DO_HEAD_ATUAL_DO_PR_69_E_FIXAR_NO_COMENTARIO_DE_INICIO
PREVIOUS_REVIEW_HEAD=cb7eb26e6e9336fb45bc958c3d54bdab359b1431
PREVIOUS_DECISION=FAIL
RETEST_FINDINGS=LEA-51-F01,LEA-51-F02,LEA-51-F03
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
- `observed_pr_head=cb7eb26e6e9336fb45bc958c3d54bdab359b1431` como snapshot do HEAD anteriormente revisado;
- histórico de LEA-46/47/48 e PR #66 isolado em `fnd_002_history`;
- novo HEAD de reteste fixado externamente no GitHub e Linear.

## LEA-51-F02

- cada referência da coluna `ADR` da matriz usa `ADR-NNNN`;
- cada referência `ADRS=` do catálogo usa `ADR-NNNN`;
- todas pertencem ao conjunto `ADR-0001` a `ADR-0018`;
- nenhuma lista contém duplicação.

## LEA-51-F03

- o validador distingue `LOCAL_VALIDATION_SPECS`, scripts materializados e execução local;
- rollback é validado como especificação, com execução marcada como não realizada;
- gates têm tokens mensuráveis, com resultados não declarados como provados;
- a arquitetura é comparada mecanicamente ao baseline e descrita como inferência limitada;
- o validador não declara execução do produto nem aprovação sem evidência.

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
