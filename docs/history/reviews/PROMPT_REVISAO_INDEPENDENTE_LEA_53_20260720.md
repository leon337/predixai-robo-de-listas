# PROMPT — RETESTE INDEPENDENTE LEA-53

```text
MISSION=LEA-53_RETEST
BUILDER_ISSUE=LEA-52
REVIEW_ISSUE=LEA-53
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=70_DRAFT
BASE_MAIN_SHA=0d68ba5238cb12ba6414ee8a6b80da4a9166b42e
REVIEWED_HEAD=12ba5e4565bac26f4b4790e7a9339d1d5e889696
PREVIOUS_REVIEW_HEAD=8019c392fbeef515eb58604698a501b74735e48a
PREVIOUS_DECISION=FAIL
RETEST_HEAD=OBTER_DO_PR_DRAFT_E_FIXAR_EXTERNAMENTE
RETEST_FINDINGS=LEA-53-F04,LEA-53-F05
F01_F02_F03=PASS_PRESERVED
HEAD_PIN_AUTHORITY=GITHUB_PR_70_AND_LINEAR_LEA_53
SELF_REFERENCE_POLICY=CURRENT_COMMIT_SHA_MUST_NOT_BE_EMBEDDED_IN_ITS_OWN_CONTENT
DOCUMENTATION_ONLY=YES
MERGE_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
FND_003_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
```

## Retestar

1. `PROJECT_RUNTIME_STATE.yaml`:
   - `observed_main_head`, `baseline_main_sha` e `safety.baseline_commit` iguais a `0d68ba...`;
   - `previous_candidate_head=8ea79ca0daf318507c4c28766174cd3747fddce9`;
   - autoridade do HEAD atual definida externamente no PR #70 e na LEA-53;
   - não exigir que o commit contenha o próprio SHA, pois isso é autorreferencial;
   - `requirements_mapped_to_increment=218/218_INTEGRATED`;
   - LEA-52 e LEA-53 como missões ativas de builder/review;
   - implementação, FND-003, merge e LIVE não autorizados.
2. Tronco:
   - resultado ativo da LEA-50 usa reviewed HEAD `12ba5e...` e merge `0d68ba...`;
   - valores antigos `24b1e8...` e `ff40cef...` aparecem somente como histórico explicitamente identificado.
3. README:
   - mapa canônico, matriz 218/218 e LEA-51 aparecem como integrados/aprovados;
   - LEA-52 remediada e LEA-53 aguardando reteste.
4. Validador:
   - compara estado operacional, estado humano, tronco, README, checkpoint, relatório e este prompt;
   - restringe o diff aos oito arquivos da missão;
   - não superdeclara execução de produto, rollback ou gates futuros.
5. Preservar:
   - PR #69 merged por squash em `0d68ba...`;
   - LEA-50 e LEA-51 Done;
   - LEA-52 e LEA-53 In Progress;
   - arquitetura V1.0, 218 requisitos, 16 domínios, 12 handoffs, 18 ADRs e 18 incrementos inalterados;
   - código de aplicação, testes do produto, SQL e migrations sem alterações.

## Execução

```bash
python3 scripts/validate_lea50_documental.py
```

## Decisão permitida

```text
PASS | PASS_WITH_CONDITIONS | FAIL
```

O revisor deve ser diferente do builder, fixar o novo HEAD externamente no GitHub e Linear, publicar review ancorada nesse commit e não fazer merge.
