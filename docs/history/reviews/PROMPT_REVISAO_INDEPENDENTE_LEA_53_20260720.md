# PROMPT — REVISÃO INDEPENDENTE LEA-53

```text
MISSION=LEA-53
BUILDER_ISSUE=LEA-52
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=0d68ba5238cb12ba6414ee8a6b80da4a9166b42e
REVIEW_HEAD=OBTER_DO_PR_DRAFT_E_FIXAR_EXTERNAMENTE
MERGE_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
FND_003_AUTHORIZED=NO
```

## Validar

1. PR #69 integrado por squash em `0d68ba5238cb12ba6414ee8a6b80da4a9166b42e`.
2. LEA-50 e LEA-51 concluídas.
3. Roadmap integrado e aprovado pela revisão independente.
4. LEA-52 ativa e LEA-53 preparada para revisão.
5. Zero achados bloqueadores remanescentes da LEA-51.
6. Nenhuma autorização para FND-003, implementação ou LIVE.
7. Nenhuma alteração em código de aplicação, testes do produto, SQL ou migrations.
8. Saída reproduzível de `python3 scripts/validate_lea50_documental.py`.

O revisor deve ser diferente do builder e revisar somente o HEAD exato fixado no GitHub e Linear.
