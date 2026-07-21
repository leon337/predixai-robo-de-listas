# HOTFIX — promoção da versão instalada para V2.5.0-alpha.2

```text
MISSION=LEA-101
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=bd2db3772898c46d9422818b780e91b5f132941e
PULL_REQUEST=73
REVIEW_ISSUE=LEA-102
TARGET_VERSION=V2.5.0-alpha.2
MODE_MAX=NULL_ONLY
```

## Problema

A DAT-001 foi integrada na `main`, porém o arquivo `VERSION` e o launcher desktop
continuaram apontando para V2.4.3. O código estava presente, mas a identificação
visual e operacional permanecia na versão anterior.

## Correção

- `VERSION` promovido para `2.5.0-alpha.2`;
- nova entrada `app/bootstrap_v250_alpha2_entry.py`;
- `run.sh` direcionado para a nova entrada;
- runtime validado da V2.4.3 preservado por delegação explícita;
- testes de regressão para versão, launcher e sintaxe/delegação.

## Decisão técnica

A nova entrada é um adaptador fino. Ela não duplica o bootstrap, não altera fluxo de
inicialização e delega para `bootstrap_v23_entry.run`. Assim, a promoção corrige a
identidade pública sem introduzir comportamento funcional fora do hotfix.

## Validação

```text
EXPECTED_PREVIOUS_TESTS=PASS_85
NEW_REGRESSION_TESTS=3
EXPECTED_CUMULATIVE_TESTS=PASS_88
RUFF=REQUIRED
MYPY=REQUIRED
CI=REQUIRED
INDEPENDENT_REVIEW=LEA-102_REQUIRED
```

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

## Rollback

Reverter integralmente o PR #73. O launcher volta a utilizar
`app/bootstrap_v23_entry.py` e o arquivo `VERSION` volta a `2.4.3`.
