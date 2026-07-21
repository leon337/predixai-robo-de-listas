# PROJECT_STATE — PredixAI Robô de Listas

## Estado oficial

```text
REPOSITORY=leon337/predixai-robo-de-listas
MAIN_HEAD=bd2db3772898c46d9422818b780e91b5f132941e
MAIN_INSTALLED_VERSION=V2.4.3-R1
CANDIDATE_VERSION=V2.5.0-alpha.2
STATE_REVISION=40
TRANSITION_ID=LEA-101-T01
ACTIVE_MISSION=LEA-101
INDEPENDENT_REVIEW=LEA-102_TODO
PR_DRAFT=73
CODE_HEAD=d6fb5569925313cc82bba83ace05ade19bfe0c53
CURRENT_GATE=FINAL_CI_AND_INDEPENDENT_REVIEW_LEA_102
```

A DAT-001 foi integrada no PR #72 e a `main` avançou para
`bd2db3772898c46d9422818b780e91b5f132941e`. A verificação local mostrou uma
divergência objetiva: o código do incremento estava integrado, porém o arquivo
`VERSION` e o launcher continuavam identificados como V2.4.3.

A autorização humana iniciou exclusivamente o hotfix LEA-101. A candidata promove
a identificação para V2.5.0-alpha.2 sem alterar o runtime validado da DAT-001.

A primeira execução do CI revelou incompatibilidade nos validadores históricos: oito
workflows tentavam converter prereleases SemVer em tuplas numéricas ou exigiam
igualdade com V2.4.3. A remediação centralizou a comparação em um validador de piso
SemVer e preservou todas as verificações funcionais anteriores.

## Entrega candidata

- `VERSION` promovido para `2.5.0-alpha.2`;
- nova entrada `app/bootstrap_v250_alpha2_entry.py`;
- `run.sh` direcionado para a nova entrada;
- delegação explícita ao runtime estável `bootstrap_v23_entry.run`;
- três testes de regressão da promoção;
- validador `scripts/validate_version_floor.py` com cinco testes;
- oito workflows históricos remediados para pisos SemVer;
- PR #73 mantido em Draft;
- revisão independente LEA-102 criada.

## Validação

```text
PREVIOUS_CUMULATIVE_TESTS=PASS_85
VERSION_PROMOTION_TESTS=3
SEMVER_VALIDATOR_TESTS=5
EXPECTED_CUMULATIVE_TESTS=PASS_93
HISTORICAL_WORKFLOWS_REMEDIATED=8
RUFF=REQUIRED
MYPY=REQUIRED
GITHUB_ACTIONS=AWAITING_FINAL_HEAD
INDEPENDENT_REVIEW=LEA-102_TODO
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

Confirmar CI do HEAD final do PR #73, fixar o mesmo SHA externamente no GitHub e
na LEA-102 e executar a revisão independente. Não promover nem mesclar sem nova
autorização humana explícita.
