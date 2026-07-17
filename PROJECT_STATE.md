# PROJECT_STATE — PredixAI Robô de Listas

## Estado operacional

- Repositório: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- HEAD base: `f3c84d97523c1c631392cefb69b6cb3e8f6a56e2`
- Versão do legado: `V2.4.3-R1`
- Missão: `LEA-16 — PTM V2.7`, aguardando integração e recibo
- Revisão: `LEA-17 — PTM V2.7-RC`, `PASS`
- PR: `#37`, aprovado para integração
- Autorização: confirmada por Leo

## Transição

```text
STATE_REVISION=5
TRANSITION_ID=LEA-16-T01
TRANSITION_STATUS=APPROVED_FOR_MERGE
FROM_STATE=PTM_V2_6_DOCUMENTALLY_DEFINITIVE
TO_STATE=PTM_V2_7_APPROVED_FOR_MERGE
MAIN_PULL_REQUEST=37
GATE_STATUS=PASS
```

## Resultado da revisão

```text
PTM_V2_7_CRITICAL_REVIEW=PASS
RETEST_01=SUPERSEDED
RETEST_02=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=4
REQUIREMENT_ID_UNIQUENESS=PASS
TRACEABILITY_COMPLETENESS=PASS
LEGACY_CLASSIFICATION_CONSISTENCY=PASS
CONTROLLED_UI_NORMATIVE_CONTRACT=PASS
SAME_BOOT_RESTART_FAIL_CLOSED=PASS
PRODUCTION_MONETARY_EFFECT_REQUIRES_SEPARATE_GATE=PASS
DOCUMENTAL_READY_FOR_MERGE=YES
```

Fonte: `docs/history/reviews/REVISAO_CRITICA_RETESTE_02_PTM_V2.7_LEA-17_20260717.md`.

## Escopo controlado

```text
CONTROLLED_SCREEN_CAPTURE=ALLOWED
CONTROLLED_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_POINTER_MOVEMENT=ALLOWED
CONTROLLED_KEYBOARD_INPUT=ALLOWED
CONTROLLED_CLICK=ALLOWED
CONTROLLED_TEST_AUTHENTICATION=ALLOWED
CONTROLLED_END_TO_END_TESTS=ALLOWED
CONTROLLED_UI_CHANNEL=ALLOWED
```

A autorização aplica-se a aplicações próprias, ambientes controlados, sandboxes, fixtures e alvos de teste allowlisted.

```text
CONTROLLED_UI_ACTION_IS_INDEPENDENT_FROM_PRODUCTION_MONETARY_EFFECT=YES
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
PRODUCTION_MONETARY_EFFECT_REQUIRES_SEPARATE_AUTHORIZATION_IN_ALL_TARGET_CLASSES=YES
```

## Contratos aprovados

- canal `CONTROLLED_UI` independente da dimensão monetária;
- estado `ARMED_CONTROLLED_UI`;
- autorização vinculada a alvo, ação, allowlist e canal;
- adaptador `NULL|SIMULATED|CONTROLLED_UI`;
- recibo com `ui_result` e `financial_result` separados;
- qualquer restart invalida a despachabilidade de comando anterior;
- nova ação após restart exige novo comando e nova autorização.

## Achados menores carregados

1. taxonomia integral de `target_logical_id`;
2. limites numéricos após benchmark;
3. ADR da topologia do kill switch;
4. matriz integral de transições antes da implementação.

## Gate atual

```text
CURRENT_GATE=PTM_V2_7_MERGE
GATE_STATUS=PASS
MERGE_AUTHORIZED_BY_LEO=YES
NEXT_ACTION=MERGE_PR_37_WITH_EXPECTED_HEAD
POST_MERGE_RECEIPT_REQUIRED=YES
CROSS_CONSOLIDATION_AUTHORIZED=NO_UNTIL_RECEIPT
```
