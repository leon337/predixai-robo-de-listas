# RECIBO PÓS-MERGE — PTM V2.7

## LEA-16 / LEA-17

```text
DOCUMENT_STATUS=POST_MERGE_RECEIPT
MAIN_PULL_REQUEST=37
MAIN_PULL_REQUEST_MERGED=YES
MAIN_PULL_REQUEST_MERGE_COMMIT=4f7fb106db95c3a33583440fd1bf52fe6603b529
MERGED_HEAD=bfc811de3431bd3888e30d1d578cc769f92d62d8
PTM_V2_7_CRITICAL_REVIEW=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=4
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
WORKFLOWS_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
```

## Escopo consolidado

```text
CONTROLLED_CAPTURE_OCR_REPLAY=ALLOWED
CONTROLLED_POINTER_KEYBOARD_CLICK=ALLOWED
CONTROLLED_TEST_AUTHENTICATION=ALLOWED
CONTROLLED_UI_CHANNEL=ALLOWED
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
PRODUCTION_MONETARY_EFFECT_REQUIRES_SEPARATE_AUTHORIZATION_IN_ALL_TARGET_CLASSES=YES
```

## Contratos integrados

- política permanente de automação em ambiente controlado;
- canal e estado `CONTROLLED_UI`;
- autorização vinculada a alvo e allowlist;
- adaptador `NULL|SIMULATED|CONTROLLED_UI`;
- recibos com dimensões de UI e monetária separadas;
- invalidação fail-closed de comandos anteriores após qualquer restart;
- prova negativa voltada a bypass, alvo não autorizado, segredo e resultado monetário de produção.

## Revisão

```text
INITIAL_REVIEW=FAIL
RETEST_01=SUPERSEDED
RETEST_02=PASS
OPEN_REVIEW_THREADS=0
DOCUMENTAL_READY_FOR_MERGE=YES
```

Relatório final: `docs/history/reviews/REVISAO_CRITICA_RETESTE_02_PTM_V2.7_LEA-17_20260717.md`.

## Pendências carregadas

1. taxonomia integral de `target_logical_id`;
2. limites após benchmark reproduzível;
3. ADR da topologia do kill switch;
4. matriz integral de transições antes da implementação.

## Condição de fechamento

Este recibo confirma a integração do PR principal. A transição somente fica completa após este recibo ser integrado, o commit da integração do recibo ser confirmado e GitHub, Linear e documentos vivos permanecerem alinhados.
