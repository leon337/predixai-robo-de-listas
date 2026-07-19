# REVISÃO DE PRONTIDÃO PARA IMPLEMENTAÇÃO

## LEA-40 — Arquitetura V1.0

```text
DOCUMENT_STATUS=BUILDER_DECISION_READY_FOR_INDEPENDENT_REVIEW
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=cb2f180aabce484f6830594cf1e4d9211743e472
ARCHITECTURE_V1_FROZEN=YES
READINESS_DECISION=GO_WITH_CONDITIONS
IMPLEMENTATION_AUTHORIZED=NO
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_CREATED=NO
MIGRATION_CREATED=NO
RUNTIME_EXECUTED=NO
```

## 1. Resposta executiva

O projeto está pronto para iniciar uma primeira missão de implementação exclusivamente fundacional, desde que as condicionantes abaixo sejam incorporadas ao escopo e validadas antes de qualquer funcionalidade de observação, sinal, adaptador ou execução.

A decisão é `GO_WITH_CONDITIONS`. Não é `GO` irrestrito porque o repositório atual ainda representa o legado V2.4.3-R1: interface Tkinter monolítica, composição por patches, persistência JSON e dependência `pynput` com capacidade de clique físico.

## 2. Evidências do repositório

```text
LEGACY_ENTRYPOINT=run.sh -> app/bootstrap_v23_entry.py
LEGACY_UI=Tkinter
LEGACY_DOMAIN_AUTHORITY=app/main.py
LEGACY_COMPOSITION=ordered_monkey_patch_chain
CURRENT_REQUIREMENTS=pynput==1.8.2
CONFIRMED_TEST_FILES=7
CONFIRMED_VERSIONED_WORKFLOWS=9
REAL_CLICK_IMPLEMENTATION_PRESENT=YES
REAL_CLICK_AUTHORIZED=NO
```

Pontos reutilizáveis ou adaptáveis:

- `app/version_info.py`;
- `app/execution_preflight.py`;
- lock, logging e diagnósticos de `app/runtime_guard.py`;
- backup e recuperação de `app/config_safety.py`;
- conceitos de listas, perfis, agenda e sessões;
- testes históricos como evidência de regressão.

Mecanismos a substituir progressivamente:

- monólito Tkinter como autoridade de domínio;
- patches dependentes de ordem;
- JSON como fonte final de verdade;
- `pynput` e clique físico no baseline de implementação;
- workflows fragmentados como único quality gate.

## 3. Primeiro incremento implementável

```text
FIRST_INCREMENT=FND-001_SAFE_SERVER_FOUNDATION
PURPOSE=criar_fundacao_do_servidor_local_sem_efeito_externo
MODE=NULL_ONLY
REAL_FINANCIAL_EFFECT=NO
CONTROLLED_UI_ACTION=NO
SIMULATED_DISPATCH=NO_NESTE_INCREMENTO
```

### Entregas da missão FND-001

1. criar estrutura modular nova sem remover o legado;
2. criar servidor local como autoridade de estado;
3. implementar configuração tipada com defaults fail-closed;
4. implementar endpoint de saúde e snapshot de capacidades;
5. definir contratos iniciais versionados e `reason_code`;
6. criar estado mínimo do sistema: `BOOTING`, `SAFE_IDLE`, `DEGRADED`, `STOPPED`;
7. criar adaptador `NULL`, incapaz de produzir efeito externo;
8. criar trilha de auditoria local sem segredos;
9. consolidar suíte de testes e workflow principal;
10. manter o legado executável isolado, sem promovê-lo a autoridade.

## 4. Stack recomendada para FND-001

A escolha é reversível e adequada ao servidor local Python já existente:

```text
LANGUAGE=Python_3.11+
API=FastAPI
ASGI=Uvicorn
SCHEMAS=Pydantic_v2
TESTS=Pytest+HTTPX
QUALITY=Ruff
TYPE_CHECKING=Mypy
PERSISTENCE=NONE_IN_FND_001
DATABASE=SQLite_DEFERRED_TO_DEDICATED_MISSION
CLIENT_ANDROID=DEFERRED
```

Não criar SQL, migration ou schema físico na FND-001. A persistência SQLite deve nascer em missão própria, com produtor, consumidor, requisito, teste e rollback definidos.

## 5. Estrutura inicial proposta

```text
src/predixai/
  api/
  application/
  domain/
  infrastructure/
  contracts/
  safety/
  observability/
tests/
  unit/
  integration/
  negative/
legacy/
  README.md
```

A movimentação física do legado para `legacy/` não é obrigatória na primeira missão. Pode ser substituída por documentação e fronteiras de importação para reduzir risco.

## 6. Estratégia de testes da FND-001

```text
T-GOV-FOUNDATION=estado_e_transicoes
T-CFG-FOUNDATION=configuracao_fail_closed
T-SEC-FOUNDATION=segredos_e_provas_negativas
T-ADP-NULL=efeito_externo_impossivel
T-API-HEALTH=contrato_versionado
T-E2E-NULL=boot_para_safe_idle_sem_efeito
```

Provas negativas obrigatórias:

- nenhum import de `pynput` na nova fundação;
- nenhum movimento ou clique de mouse;
- nenhuma conexão com corretora;
- nenhum segredo versionado;
- nenhum SQL ou migration;
- nenhum adaptador diferente de `NULL` habilitado;
- nenhuma transição para LIVE.

## 7. Critérios de aceite da FND-001

```text
AC01_NEW_FOUNDATION_IMPORTS_WITHOUT_LEGACY_PATCH_CHAIN=PASS
AC02_SERVER_STARTS_IN_SAFE_IDLE=PASS
AC03_HEALTH_ENDPOINT_VERSIONED=PASS
AC04_CONFIGURATION_INVALID_FAILS_CLOSED=PASS
AC05_NULL_ADAPTER_CANNOT_CREATE_EXTERNAL_EFFECT=PASS
AC06_AUDIT_EVENT_CONTAINS_TRACE_ID_AND_REASON_CODE=PASS
AC07_ALL_NEW_TESTS_PASS=PASS
AC08_CONSOLIDATED_CI_PASS=PASS
AC09_LEGACY_RUNTIME_NOT_INVOKED_BY_NEW_SERVER=PASS
AC10_NO_PYNPUT_SQL_MIGRATION_LIVE_OR_REAL_CLICK=PASS
```

## 8. Condicionantes para o GO

```text
C01_INDEPENDENT_CRITICAL_REVIEW_OF_LEA_40=REQUIRED
C02_HUMAN_AUTHORIZATION_FOR_FND_001=REQUIRED
C03_FND_001_MISSION_MUST_INCLUDE_FULL_BUILD_TEST_DOCUMENT_PR_FLOW=REQUIRED
C04_REAL_CLICK_AND_PYNPUT_MUST_REMAIN_QUARANTINED=REQUIRED
C05_GITIGNORE_MUST_COVER_BACKUPS_REPORTS_RUNTIME=REQUIRED
C06_CONSOLIDATED_CI_MUST_BE_CREATED=REQUIRED
C07_NO_DATABASE_IN_FIRST_INCREMENT=REQUIRED
C08_NO_ANDROID_CLIENT_IN_FIRST_INCREMENT=REQUIRED
C09_NO_SIGNAL_ENGINE_OR_EXECUTION_IN_FIRST_INCREMENT=REQUIRED
C10_ROLLBACK_BY_PR_REVERT_AND_LEGACY_ENTRYPOINT_PRESERVATION=REQUIRED
```

## 9. Riscos

| Risco | Nível | Controle |
|---|---:|---|
| novo servidor importar acidentalmente o monólito | alto | proibição de import e teste negativo |
| `pynput` permanecer acessível à nova fundação | crítico | isolamento e scanner de imports |
| tentar criar todas as entidades de uma vez | alto | FND-001 sem banco e sem domínios avançados |
| CI verde apenas por workflows históricos | médio | workflow agregado novo |
| artefatos locais entrarem no Git | médio | atualizar `.gitignore` |
| confundir `GO_WITH_CONDITIONS` com autorização de código | alto | gate humano e revisão independente separados |

## 10. Gates da LEA-40

```text
G1_FROZEN_BASELINE=PASS
G2_FIRST_INCREMENT_DEFINED=PASS
G3_STACK_AND_REPOSITORY_FIT=PASS_WITH_CONDITIONS
G4_TEST_STRATEGY_DEFINED=PASS
G5_LOCAL_ENVIRONMENT_READY=PASS_WITH_CONDITIONS
G6_SECURITY_AND_SIMULATION_BOUNDARY=PASS
G7_DEPENDENCIES_AND_ROLLBACK=PASS_WITH_CONDITIONS
G8_ACCEPTANCE_CRITERIA=PASS
G9_GITHUB_LINEAR_STATE_SYNC=IN_PROGRESS
G10_READINESS_DECISION=GO_WITH_CONDITIONS
```

## 11. Próximo fluxo

```text
LEA_40_BUILDER_DECISION
→ LEA_40_RC_INDEPENDENT_REVIEW
→ REMEDIATION_IF_REQUIRED
→ HUMAN_AUTHORIZATION_OF_FND_001
→ EXECUTE_COMPLETE_FND_001_MISSION
```

A missão FND-001 deverá ser entregue como comando composto e executada integralmente: investigar, planejar, construir, testar, corrigir, documentar, publicar PR e validar CI, parando apenas em bloqueio real ou gate humano.