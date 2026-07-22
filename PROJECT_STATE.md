# PROJECT_STATE — PredixAI Robô de Listas

## Estado oficial

```text
REPOSITORY=leon337/predixai-robo-de-listas
MAIN_HEAD=bd2db3772898c46d9422818b780e91b5f132941e
MAIN_INSTALLED_VERSION=V2.4.3-R1
CANDIDATE_VERSION=V2.5.0-alpha.2
STATE_REVISION=41
TRANSITION_ID=LEA-101-T02
ACTIVE_MISSION=LEA-101
FAILED_REVIEW=LEA-102_DONE_FAIL
INDEPENDENT_RETEST=LEA-124_TODO
PR_DRAFT=73
CURRENT_GATE=FINAL_CI_AND_INDEPENDENT_RETEST_LEA_124
```

A DAT-001 foi integrada no PR #72, mas `VERSION` e o launcher permaneceram em
V2.4.3. A LEA-101 publicou o hotfix de promoção para V2.5.0-alpha.2, preservando o
runtime validado por delegação ao entrypoint estável.

A revisão independente LEA-102 reprovou o primeiro candidato por dois achados:

- `LEA-102-F01`: o parser aceitava prerelease numérico com zero à esquerda e
  prefixos `v`/`V`;
- `LEA-102-F02`: Ruff e Mypy não cobriam os arquivos Python introduzidos pelo hotfix.

## Remediação publicada

- parser SemVer estrito sem prefixos `v`/`V`;
- rejeição de `2.5.0-alpha.01`;
- testes negativos ampliados;
- workflow `.github/workflows/validate-version-promotion.yml`;
- suíte cumulativa completa no workflow do hotfix;
- Ruff e Mypy sobre parser, entrypoint e testes da promoção;
- prompt e missão de reteste independente LEA-124 criados;
- PR #73 mantido em Draft.

## Validação esperada

```text
PREVIOUS_CUMULATIVE_TESTS=PASS_93
NEW_NEGATIVE_CASES=3
EXPECTED_CUMULATIVE_TESTS=PASS_96
PREVIOUS_GITHUB_ACTIONS=PASS_11_OF_11
NEW_VERSION_PROMOTION_WORKFLOW=1
EXPECTED_GITHUB_ACTIONS=PASS_12_OF_12
RUFF_HOTFIX=REQUIRED
MYPY_HOTFIX=REQUIRED
INDEPENDENT_RETEST=LEA_124_TODO
```

## Limites preservados

```text
MODE_MAX=NULL_ONLY
LST_001_AUTHORIZED=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

## Próximo gate

Confirmar o CI do HEAD final do PR #73, fixar o mesmo SHA externamente no GitHub e
na LEA-124 e executar o reteste independente. Não promover nem mesclar sem nova
autorização humana explícita.
