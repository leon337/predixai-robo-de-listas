# PROJECT_STATE — PredixAI Robô de Listas

## Estado operacional

- Repositório: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- HEAD base de `main`: `f3c84d97523c1c631392cefb69b6cb3e8f6a56e2`
- Versão real do legado: `V2.4.3-R1`
- Missão ativa: `LEA-16 — PTM V2.7`, `In Progress`
- Revisão ativa: `LEA-17 — PTM V2.7-RC`, segundo reteste pendente
- PR ativo: `#37`, pronto para revisão
- Branch: `leonpcsn/lea-16-ptm-v27-execucao-controlada-e-gates-de-seguranca`
- Autorização humana: correção, merge e publicação autorizados por Leo, condicionados ao `PASS` independente final

## Transição

```text
STATE_REVISION=5
TRANSITION_ID=LEA-16-T01
TRANSITION_STATUS=READY_FOR_INDEPENDENT_REVIEW
FROM_STATE=PTM_V2_6_DOCUMENTALLY_DEFINITIVE
TO_STATE=PTM_V2_7_RETEST_02_READY
MAIN_PULL_REQUEST=37
ACTIVE_REVIEW_ISSUE=LEA-17
GITHUB_SYNC_STATUS=IN_PROGRESS
LINEAR_SYNC_STATUS=IN_PROGRESS
```

## Escopo controlado ativo

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

Classes de alvo permitidas: aplicação própria, ambiente local controlado, sandbox, fixture sanitizada ou alvo de teste explicitamente allowlisted.

```text
CONTROLLED_UI_ACTION != REAL_FINANCIAL_EFFECT
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
REAL_FINANCIAL_EFFECT_REQUIRES_SEPARATE_AUTHORIZATION_IN_ALL_TARGET_CLASSES=YES
EXTERNAL_FINANCIAL_EXECUTION_AUTHORIZED=NO
REAL_MONEY_OPERATION_AUTHORIZED=NO
```

## Contrato CONTROLLED_UI

O adendo normativo de reteste 02 define:

- canal `CONTROLLED_UI` separado da dimensão financeira;
- estado `ARMED_CONTROLLED_UI`;
- comando com alvo, allowlist, canal e dimensão financeira;
- autorização vinculada a alvo, ação e canal;
- adaptador `NULL|SIMULATED|CONTROLLED_UI`;
- recibo com `ui_result` e `financial_result` independentes;
- bloqueio de qualquer resultado financeiro real nesta PTM.

Fonte: `docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md`.

## Recovery temporal

```text
PROCESS_INSTANCE_CHANGED=RESTART_DETECTED
PRE_RESTART_COMMAND_DISPATCHABLE=NO
PRE_RESTART_COMMAND_AUTO_REARM=NO
PRE_RESTART_COMMAND_AUTO_REDISPATCH=NO
NEW_ACTION_REQUIRES=NEW_COMMAND_AND_NEW_AUTHORIZATION
```

Essa regra aplica-se inclusive a restart no mesmo boot. O relógio monotônico só possui autoridade dentro da mesma instância de processo.

## Ciclos de revisão

```text
INITIAL_CRITICAL_REVIEW=FAIL
RETEST_01=SUPERSEDED_BY_LATE_FINDINGS
RETEST_02=PENDING
CURRENT_CRITICAL_FINDINGS=0
CURRENT_MAJOR_FINDINGS=2_REMEDIATED_BY_BUILDER
CURRENT_MINOR_FINDINGS=2_REMEDIATED_BY_BUILDER
DOCUMENTAL_READY_FOR_MERGE=NO_PENDING_RETEST_02
```

O primeiro relatório `PASS` foi supersedido pelo aviso `AVISO_SUPERSESSAO_RETESTE_01_PTM_V2.7_LEA-17_20260717.md` e não possui autoridade de merge.

## Fontes normativas atuais

1. `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`;
2. `docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md`;
3. `docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md`;
4. `docs/architecture/PTM_V2.7_SUPLEMENTO_RASTREABILIDADE_RETESTE_02_LEA-17_20260717.md`;
5. `PROJECT_RUNTIME_STATE.yaml`;
6. Linear `LEA-16` e `LEA-17`.

## Gate atual

```text
CURRENT_GATE=PTM_V2_7_INDEPENDENT_RETEST_02
GATE_STATUS=IN_PROGRESS
MERGE_AUTHORIZED_BY_LEO=YES
MERGE_EXECUTION_CONDITION=INDEPENDENT_RETEST_02_PASS
AUTOMATIC_ADVANCE=NO
```

## Próxima ação

Executar o segundo reteste independente sobre o HEAD que contém todas as remediações. Em `PASS`, sincronizar o estado aprovado, integrar o PR `#37` com verificação de SHA e publicar o recibo pós-merge.
