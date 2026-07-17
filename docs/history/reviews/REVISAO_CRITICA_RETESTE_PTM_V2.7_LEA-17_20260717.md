# REVISÃO CRÍTICA INDEPENDENTE — RETESTE PTM V2.7

## LEA-17 / PR #37

## 1. Controle

```text
REVIEW_STATUS=FINAL_PASS
REVIEW_TYPE=INDEPENDENT_CRITICAL_RETEST
MISSION=LEA-17
REVIEWED_PR=37
REVIEWED_HEAD=510e6a1e19ac6b3dc4778797b3f003fcd9d20afb
BASE_MAIN_SHA=f3c84d97523c1c631392cefb69b6cb3e8f6a56e2
TRANSITION_ID=LEA-16-T01
STATE_REVISION=5
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
WORKFLOWS_CHANGED=NO
APPLICATION_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
```

O reteste foi reconstruído a partir dos arquivos do PR, fontes primárias V2.5/V2.6/V2.7, manifesto, schema, documentos vivos, política de automação controlada, Linear e threads do GitHub. A auto-revisão do builder não foi usada como autoridade final.

## 2. Resultado

```text
PTM_V2_7_CRITICAL_RETEST=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=4
REQUIREMENT_ID_UNIQUENESS=PASS
TRACEABILITY_COMPLETENESS=PASS
LEGACY_CLASSIFICATION_CONSISTENCY=PASS
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS
RESTART_STABLE_DEADLINE=PASS
CONTROLLED_AUTOMATION_POLICY=PASS
CONTROLLED_CAPTURE_OCR_REPLAY=PASS
CONTROLLED_POINTER_KEYBOARD_CLICK=PASS
CONTROLLED_TEST_AUTH=PASS
ANALYSIS_EXECUTION_SEPARATION=PASS
FINANCIAL_EFFECT_SEPARATION=PASS
UNCONTROLLED_ACTION_NEGATIVE_PROOF=PASS_SPECIFIED
REAL_FINANCIAL_EFFECT_NEGATIVE_PROOF=PASS_SPECIFIED
STATE_SCHEMA_COMPATIBILITY=PASS
STATE_DOCUMENTATION_ALIGNMENT=PASS
GITHUB_LINEAR_ALIGNMENT=PASS
OPEN_REVIEW_THREADS=0
DOCUMENTAL_READY_FOR_MERGE=YES
```

## 3. Reconciliação dos achados maiores

### MAJOR-01 — schema do manifesto

Remediado.

```text
transition_status=READY_FOR_INDEPENDENT_REVIEW
allowed_by_schema=YES
gate_status=IN_PROGRESS
allowed_by_schema=YES
github_sync_status=IN_PROGRESS
linear_sync_status=IN_PROGRESS
safety.execution_status=AUTHORIZED_DOCUMENTATION_ONLY
```

Os valores pertencem aos enums do schema 1.0.3. O manifesto não persiste campos `expected_*` proibidos.

### MAJOR-02 — prazo após restart

Remediado pela combinação:

```text
expires_at_utc
ttl_ms
clock_source_id
boot_id_at_creation
deadline_monotonic_process_local
```

O monotônico é apenas orçamento local. Restart, troca de boot, clock rollback, skew, fonte desconhecida ou evidência insuficiente bloqueiam e exigem revalidação. Não há rearmamento nem redespacho automáticos.

### MAJOR-03 — `command_id`

Remediado diretamente na matriz:

```text
command_id=ADAPTAR_FROM_V2_5
VERSIONED_SIGNAL_REFERENCE=ADAPTAR_FROM_V2_6
EXECUTION_COMMAND_AGGREGATE=NOVO_IN_V2_7
```

### MAJOR-04 — prova negativa

Remediado. A especificação documental foi separada da execução runtime.

```text
UNCONTROLLED_UI_ACTION_NEGATIVE_PROOF=REQUIRED
UNAUTHORIZED_EXTERNAL_ACCESS_NEGATIVE_PROOF=REQUIRED
REAL_FINANCIAL_EFFECT_NEGATIVE_PROOF=REQUIRED
CONTROLLED_UI_CAPABILITY_ABSENCE_PROOF=NOT_REQUIRED
RUNTIME_TEST_EXECUTED=NO
```

A existência de OCR, captura, `pynput`, `pyautogui`, Selenium ou ferramentas equivalentes não constitui falha quando o uso ocorre em alvo controlado e allowlisted.

## 4. Correção transversal de escopo

A política ativa estabelece:

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

Classes permitidas:

- aplicação própria;
- ambiente local controlado;
- sandbox dedicada;
- fixture ou replay sanitizado;
- alvo de teste explicitamente allowlisted.

A correção foi aplicada às instruções oficiais, Skills, manifesto, estado, tronco, matriz V2.7, PR e Linear. Issues históricos receberam notas de precedência sem reescrever a memória original.

## 5. Separação de efeitos

```text
CONTROLLED_UI_ACTION != REAL_FINANCIAL_EFFECT
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
EXTERNAL_FINANCIAL_EXECUTION_AUTHORIZED=NO
REAL_MONEY_OPERATION_AUTHORIZED=NO
```

A política permite automação técnica em aplicações próprias e não autoriza, por consequência, operação financeira real ou acesso externo sem autorização.

## 6. Auditoria do PR

```text
CHANGED_FILES=13
APPLICATION_FILES_CHANGED=0
TEST_FILES_CHANGED=0
WORKFLOW_FILES_CHANGED=0
DOCUMENTATION_AND_PROTOCOL_FILES_ONLY=YES
REVIEW_THREADS_TOTAL=3
REVIEW_THREADS_RESOLVED=3
```

A contagem permanece:

```text
STRUCTURAL_REQUIREMENTS=32
FUNCTIONAL_REQUIREMENTS=52
TOTAL_REQUIREMENT_IDS=84
DUPLICATE_IDS=0
```

## 7. Achados menores preservados

1. taxonomia completa de `target_logical_id` deverá ser consolidada antes do Documento Mestre;
2. limites numéricos e thresholds dependem de benchmark reproduzível;
3. topologia local/remota do kill switch requer ADR específica;
4. matriz integral `estado × evento × guarda × próximo estado` deverá existir antes da implementação vinculante.

Esses itens não bloqueiam o merge documental.

## 8. Limites e segurança

```text
SECRETS_IN_GIT=PROHIBITED
UNAUTHORIZED_THIRD_PARTY_ACCESS=PROHIBITED
PRODUCTION_CREDENTIAL_DISCLOSURE=PROHIBITED
REAL_FINANCIAL_ORDER=NOT_AUTHORIZED
REAL_MONEY_OPERATION=NOT_AUTHORIZED
CONTROLLED_AUTOMATION=AUTHORIZED
```

## 9. Decisão

```text
PTM_V2_7_CRITICAL_REVIEW=PASS
DOCUMENTAL_READY_FOR_MERGE=YES
CRITICAL_BLOCKERS=0
OPEN_MAJOR_FINDINGS=0
MERGE_AUTHORIZATION_BY_LEO=CONFIRMED
MERGE_EXECUTED=NO_AT_REVIEW_TIME
POST_MERGE_CONFIRMATION_REQUIRED=YES
CROSS_CONSOLIDATION_AUTHORIZED=NO_UNTIL_RECEIPT
```

O PR #37 está documentalmente apto ao merge. Após integração, deve ser criada transição pós-merge separada, com confirmação do commit em `main`, atualização de `state_revision`, fechamento de LEA-16/LEA-17 e recibo próprio.
