# PredixAI Robô de Listas

> Painel operacional. A autoridade estruturada permanece em
> `PROJECT_RUNTIME_STATE.yaml`; o mapa de desenvolvimento permanece no Documento
> Mestre da Arquitetura V1.0.

## Estado atual

```text
MAIN_HEAD=bd2db3772898c46d9422818b780e91b5f132941e
MAIN_INSTALLED_VERSION=V2.4.3-R1
CANDIDATE_VERSION=V2.5.0-alpha.2
MISSÃO_ATIVA=LEA-101 — promoção de versão
REVISÃO_INDEPENDENTE=LEA-102 — TODO
BRANCH=leonpcsn/lea-101-hotfix-promote-installed-version-to-v250-alpha2
PR=73
PR_MODE=DRAFT
STATE_REVISION=40
GATE=FINAL_CI_AND_INDEPENDENT_REVIEW_LEA_102
ARQUITETURA_V1_CONGELADA=YES
MERGE_AUTORIZADO=NO
STATE_SOURCE=PROJECT_RUNTIME_STATE.yaml
```

## Campanha

| Entrega ou gate | Estado |
|---|---|
| Documento Mestre e mapa canônico | ✅ integrados |
| Requisitos, domínios, handoffs e ADRs | ✅ `218/218`, `16/16`, `12/12`, `18/18` |
| FND-001, FND-002 e FND-003 | ✅ integradas |
| DAT-001 — estado durável e migração legada | ✅ integrada no PR #72 |
| LEA-101 — promoção para V2.5.0-alpha.2 | 🟨 candidata e remediação CI publicadas |
| LEA-102 — revisão independente | ⏳ aguardando HEAD final e CI |
| PR #73 | ⏳ Draft; sem autorização de merge |
| LST-001 | ⛔ não autorizado |

## Hotfix de versão

A DAT-001 foi integrada com sucesso, mas a aplicação continuou exibindo V2.4.3
porque `VERSION` e `run.sh` não foram promovidos. O PR #73 corrige exclusivamente
essa divergência:

```text
VERSION=2.5.0-alpha.2
ENTRYPOINT=app/bootstrap_v250_alpha2_entry.py
STABLE_RUNTIME_DELEGATE=bootstrap_v23_entry.run
BEHAVIORAL_RUNTIME_CHANGE=NO
VERSION_PROMOTION_TESTS=3
SEMVER_VALIDATOR_TESTS=5
EXPECTED_CUMULATIVE_TESTS=PASS_93
```

A nova entrada é um adaptador fino: preserva o runtime validado e altera somente a
identificação pública da versão.

## Compatibilidade CI

O prerelease `2.5.0-alpha.2` revelou parsers históricos que aceitavam apenas números
separados por ponto ou igualdade exata com V2.4.3. O hotfix adiciona um validador
SemVer central e atualiza oito workflows para exigir o piso histórico de cada camada,
sem retirar seus testes funcionais.

```text
SEMVER_VALIDATOR=scripts/validate_version_floor.py
HISTORICAL_WORKFLOWS_REMEDIATED=8
CI_FIRST_ATTEMPT=FAIL_VERSION_PARSERS_ONLY
FINAL_HEAD_CI=AWAITING
```

## DAT-001 integrada

```text
DAT_001_MERGE_COMMIT=bd2db3772898c46d9422818b780e91b5f132941e
LOCAL_LINUX_MINT=PASS_85
CI=PASS_12_OF_12
INDEPENDENT_DECISION=PASS
NULL_ONLY=PRESERVED
```

## Limites

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

## Próxima ação

Confirmar o CI do HEAD final do PR #73, fixar o mesmo SHA no PR e na LEA-102 e
executar a revisão independente. Não promover nem mesclar sem autorização humana
explícita.
