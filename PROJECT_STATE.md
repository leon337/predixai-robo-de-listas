# PROJECT_STATE — PredixAI Robô de Listas

## Estado operacional

- Repositório: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- HEAD de `main` confirmado: `f3c84d97523c1c631392cefb69b6cb3e8f6a56e2`
- Versão real do legado: `V2.4.3-R1`
- Missão ativa: `LEA-16 — PTM V2.7 — Execução controlada e gates de segurança`, `In Progress`
- Revisão crítica independente: `LEA-17 — PTM V2.7-RC`, aguardando reteste
- PR ativo: `#37`, rascunho pronto para reteste independente
- Branch de trabalho: `leonpcsn/lea-16-ptm-v27-execucao-controlada-e-gates-de-seguranca`
- Fase: correção transversal de escopo controlado concluída pelo builder
- Autorização humana: correção, merge e publicação autorizados por Leo em 17/07/2026, condicionados ao reteste técnico `PASS`

## Transição ativa

```text
STATE_REVISION=5
TRANSITION_ID=LEA-16-T01
TRANSITION_STATUS=READY_FOR_INDEPENDENT_REVIEW
FROM_STATE=PTM_V2_6_DOCUMENTALLY_DEFINITIVE
TO_STATE=PTM_V2_7_SCOPE_CORRECTION_READY_FOR_RETEST
BASE_MAIN_SHA=f3c84d97523c1c631392cefb69b6cb3e8f6a56e2
MAIN_PULL_REQUEST=37
MAIN_PULL_REQUEST_STATUS=DRAFT_READY_FOR_RETEST
ACTIVE_REVIEW_ISSUE=LEA-17
MISSION_LOCK=LOCKED_ADVISORY
GITHUB_SYNC_STATUS=IN_PROGRESS
LINEAR_SYNC_STATUS=IN_PROGRESS
```

O `state_revision` permanece `5` durante a transição não consolidada. Ele avançará somente na confirmação pós-merge.

## Política ativa de automação controlada

Fontes normativas:

1. `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`;
2. `docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md`;
3. `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md`.

```text
CONTROLLED_SCREEN_CAPTURE=ALLOWED
CONTROLLED_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_POINTER_MOVEMENT=ALLOWED
CONTROLLED_KEYBOARD_INPUT=ALLOWED
CONTROLLED_CLICK=ALLOWED
CONTROLLED_TEST_AUTHENTICATION=ALLOWED
CONTROLLED_END_TO_END_TESTS=ALLOWED
```

A autorização aplica-se a aplicações próprias, ambiente local controlado, sandbox dedicada, fixture sanitizada e alvo de teste explicitamente allowlisted.

Separação obrigatória:

```text
CONTROLLED_UI_ACTION != REAL_FINANCIAL_EFFECT
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
EXTERNAL_FINANCIAL_EXECUTION_AUTHORIZED=NO
REAL_MONEY_OPERATION_AUTHORIZED=NO
```

## Correção das versões

### PTM V2.5

Exclusões de ponteiro e clique significam `OUT_OF_SCOPE_FOR_FOUNDATION_STAGE`, não proibição global.

### PTM V2.6

Captura, OCR e replay controlados são permitidos. O domínio analítico não produz ação de UI por responsabilidade própria, mas harnesses controlados de teste são permitidos.

### PTM V2.7

Adaptador de automação de UI controlada é permitido para aplicações próprias e sandboxes. Adaptador financeiro externo e operação com saldo real não são autorizados por esta missão.

## Entregas

1. `docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md`;
2. `docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md`;
3. `docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md`;
4. `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`;
5. `docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md`;
6. `docs/history/reviews/REVISAO_CRITICA_PTM_V2.7_LEA-17_20260717.md`;
7. PR `#37`;
8. Linear `LEA-16` e `LEA-17`.

## Estado dos achados anteriores

```text
MAJOR_01_SCHEMA_ENUMS=REMEDIATED
MAJOR_02_RESTART_STABLE_DEADLINE=REMEDIATED
MAJOR_03_COMMAND_ID_CLASSIFICATION=REMEDIATED
MAJOR_04_NEGATIVE_PROOF_GATE=REMEDIATED
GLOBAL_CONTROLLED_AUTOMATION_SCOPE=REMEDIATED
OPEN_CRITICAL_FINDINGS_BUILDER_VIEW=0
OPEN_MAJOR_FINDINGS_BUILDER_VIEW=0
RETEST_REQUIRED=YES
```

A prova negativa passa a verificar ação não controlada, acesso externo não autorizado e efeito financeiro real. Ela não proíbe a existência de OCR, captura, `pynput`, `pyautogui`, Selenium ou ferramentas equivalentes em escopo controlado.

## Segurança preservada

```text
SECRETS_IN_GIT=NO
PRODUCTION_CREDENTIAL_DISCLOSURE=NO
UNAUTHORIZED_THIRD_PARTY_ACCESS=NO
EXTERNAL_FINANCIAL_ORDER=NO
REAL_MONEY_OPERATION=NO
APPLICATION_CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
APPLICATION_EXECUTED_DURING_DOCUMENTAL_MISSION=NO
```

## Gate atual

```text
CURRENT_GATE=PTM_V2_7_INDEPENDENT_RETEST
GATE_STATUS=IN_PROGRESS
ACTIVE_PULL_REQUEST=37
PULL_REQUEST_MODE=DRAFT_READY_FOR_RETEST
ACTIVE_REVIEW_ISSUE=LEA-17
MERGE_AUTHORIZATION_RECORDED=YES
MERGE_EXECUTION_CONDITION=INDEPENDENT_RETEST_PASS
AUTOMATIC_ADVANCE=NO
```

## Próxima ação

Executar reteste independente da `LEA-17` sobre o HEAD atualizado do PR `#37`. Em `PASS`, marcar o PR pronto, integrar com o SHA verificado e publicar a confirmação pós-merge em transição separada.

## Limites vigentes

```text
CONTROLLED_AUTOMATION=ALLOWED
SECRETS_OR_CREDENTIALS_IN_GIT=PROHIBITED
UNAUTHORIZED_EXTERNAL_ACCESS=PROHIBITED
REAL_FINANCIAL_EFFECT=NOT_AUTHORIZED
MERGE_BEFORE_RETEST_PASS=PROHIBITED
CROSS_CONSOLIDATION_BEFORE_POST_MERGE_RECEIPT=PROHIBITED
```
