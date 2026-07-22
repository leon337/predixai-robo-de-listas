# Prompt — reteste independente LEA-124

Retestar exclusivamente as remediações LEA-102-F01 e LEA-102-F02 no HEAD final do
PR Draft #73. Não confiar nas declarações do builder sem inspecionar diff, código,
testes e CI.

## Alvo

```text
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=73
BASE_MAIN_SHA=bd2db3772898c46d9422818b780e91b5f132941e
RETEST_HEAD=<LER_EXTERNAMENTE_NO_PR_73_E_NA_LEA_124>
BUILDER_ISSUE=LEA-101
PREVIOUS_REVIEW=LEA-102_DONE_FAIL
RETEST_ISSUE=LEA-124
FINDINGS_TO_RETEST=LEA-102-F01,LEA-102-F02
MODE_MAX=NULL_ONLY
```

O SHA final deve ser fixado externamente no PR #73 e na LEA-124. Não embutir o SHA
do próprio commit neste documento.

## Reteste obrigatório

1. Confirmar que `scripts/validate_version_floor.py` rejeita:
   - `2.5.0-alpha.01`;
   - `v2.5.0`;
   - `V2.5.0`;
   - versões incompletas.
2. Confirmar precedência SemVer entre prerelease e release e entre identificadores
   numéricos e alfanuméricos.
3. Confirmar execução dos testes negativos adicionados.
4. Confirmar que `.github/workflows/validate-version-promotion.yml` executa a suíte
   cumulativa completa.
5. Confirmar Ruff e Mypy sobre:
   - `scripts/validate_version_floor.py`;
   - `app/bootstrap_v250_alpha2_entry.py`;
   - `tests/test_version_floor.py`;
   - `tests/test_version_promotion.py`.
6. Confirmar todos os workflows acionados no HEAD final.
7. Confirmar PR aberto, Draft, mergeável e alinhamento GitHub–Linear–documentação.
8. Confirmar ausência de SQL, migration, corretora, clique, efeito financeiro,
   SIMULATED, CONTROLLED_UI e LIVE.
9. Publicar `PASS` ou `FAIL` no PR #73 e na LEA-124.

## Limites

```text
LST_001_AUTHORIZED=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

Não promover nem mesclar o PR.
