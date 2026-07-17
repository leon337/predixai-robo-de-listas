# ADENDO TRANSVERSAL — AUTOMAÇÃO EM AMBIENTE CONTROLADO

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=NORMATIVE_ACTIVE
MISSION=LEA-16
REVIEW_ISSUE=LEA-17
AUTHORIZED_BY=LEO
AUTHORIZED_AT=2026-07-17
PARENT_POLICY=docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
APPLIES_TO=PTM_V2.5|PTM_V2.6|PTM_V2.7
```

Este adendo corrige a fronteira entre capacidade técnica, responsabilidade de etapa e efeito financeiro. Ele prevalece sobre redações genéricas anteriores que tratavam OCR, captura, replay, ponteiro, teclado, clique ou autenticação como proibidos em qualquer contexto.

## 2. Modelo de classificação

### 2.1 Classe do alvo

```text
TARGET_CLASS=
  FIRST_PARTY_APPLICATION
  LOCAL_CONTROLLED_ENVIRONMENT
  DEDICATED_TEST_SANDBOX
  SANITIZED_FIXTURE_OR_REPLAY
  EXPLICITLY_ALLOWLISTED_TEST_TARGET
  EXTERNAL_PRODUCTION_SYSTEM
  EXTERNAL_FINANCIAL_SYSTEM
```

### 2.2 Classe do efeito

```text
EFFECT_CLASS=
  OBSERVATION_ONLY
  CONTROLLED_UI_ACTION
  CONTROLLED_TEST_AUTH
  SIMULATED_FINANCIAL_EFFECT
  EXTERNAL_NON_FINANCIAL_EFFECT
  REAL_FINANCIAL_EFFECT
```

### 2.3 Decisão normativa

```text
OBSERVATION_ONLY=ALLOWED_IN_CONTROLLED_SCOPE
CONTROLLED_UI_ACTION=ALLOWED_IN_CONTROLLED_SCOPE
CONTROLLED_TEST_AUTH=ALLOWED_IN_CONTROLLED_SCOPE
SIMULATED_FINANCIAL_EFFECT=ALLOWED
EXTERNAL_NON_FINANCIAL_EFFECT=REQUIRES_SPECIFIC_AUTHORIZATION
REAL_FINANCIAL_EFFECT=NOT_AUTHORIZED_BY_THIS_MISSION
```

## 3. Correção da PTM V2.5

As declarações `POINTER_MOVEMENT_ALLOWED=NO`, `REAL_CLICK_ALLOWED=NO`, `REAL_CLICK_EXCLUDED_FROM_V2_5`, `V25-SEC-001` e equivalentes passam a significar:

```text
V2_5_OWNS_UI_AUTOMATION=NO
V2_5_CONTROLLED_UI_AUTOMATION_GLOBAL_PROHIBITION=NO
V2_5_UI_ACTION=OUT_OF_SCOPE_FOR_FOUNDATION_STAGE
FUTURE_CONTROLLED_ADAPTER_ALLOWED=YES
```

Consequências:

- a V2.5 continua responsável por fundação, contratos, perfis e geometria;
- click targets permanecem dados geométricos, não autorização automática;
- captura de coordenadas é permitida em aplicação própria e ambiente controlado;
- testes controlados de ponteiro e clique podem existir em harness separado e explicitamente autorizado;
- a prova de segurança da V2.5 deve demonstrar ausência de ação **não declarada ou não controlada** dentro do domínio de fundação, não ausência global de capacidade.

## 4. Correção da PTM V2.6

As declarações `POINTER_MOVEMENT_ALLOWED=NO`, `REAL_CLICK_ALLOWED=NO`, `V2_6_REAL_INPUT_BLOCKED`, `REAL_INPUT_PROHIBITED`, `EXECUTION_EXCLUSION` e equivalentes passam a significar:

```text
V2_6_ANALYSIS_DOMAIN_PRODUCES_UI_ACTION=NO
CONTROLLED_CAPTURE_AND_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_TEST_HARNESS_UI_ACTION=ALLOWED
GLOBAL_UI_AUTOMATION_PROHIBITION=NO
```

Consequências:

- captura de tela e OCR são capacidades normais da pipeline V2.6;
- replay controlado pode usar fixtures, relógio controlado e alvo local autorizado;
- o domínio analítico não transforma sinal em clique por conta própria;
- um harness de validação pode mover ponteiro, digitar e clicar em aplicação própria ou sandbox, desde que permaneça fora da autoridade do motor analítico;
- a prova negativa V2.6 verifica ausência de acoplamento oculto `ANALYSIS -> UNDECLARED_UI_ACTION`, não ausência absoluta de bibliotecas de automação no repositório.

## 5. Correção da PTM V2.7

O baseline anterior `SIMULATED_ONLY` é dividido em duas dimensões independentes:

```text
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
CONTROLLED_UI_ADAPTER=ALLOWED
EXTERNAL_FINANCIAL_ADAPTER=NOT_AUTHORIZED
```

A V2.7 pode especificar e futuramente implementar adaptadores para:

- movimento de ponteiro em aplicação própria;
- entrada de teclado em formulário de teste;
- clique em controles allowlisted;
- autenticação com credenciais de teste;
- captura e OCR antes e depois da ação;
- replay e E2E controlados;
- recibo e reconciliação de efeito de UI.

O adaptador controlado deve receber:

```text
adapter_mode=CONTROLLED_UI
allowed_target_class
application_identity
window_or_route_identity
action_allowlist
session_authorization_id
kill_switch_state
rate_limit_policy
audit_trace_id
```

## 6. Substituição da prova negativa

A prova anterior de “ausência de ponteiro, teclado e clique” é substituída por:

```text
UNCONTROLLED_UI_ACTION_NEGATIVE_PROOF=REQUIRED
UNAUTHORIZED_EXTERNAL_ACCESS_NEGATIVE_PROOF=REQUIRED
REAL_FINANCIAL_EFFECT_NEGATIVE_PROOF=REQUIRED
CONTROLLED_UI_CAPABILITY_ABSENCE_PROOF=NOT_REQUIRED
```

A prova deve falhar quando houver:

- ação fora da allowlist;
- alvo não identificado;
- bypass de autorização ou kill switch;
- credencial de produção versionada;
- acesso externo não autorizado;
- ordem financeira real ou alteração de saldo real;
- acoplamento oculto do motor analítico ao adaptador.

A prova não deve falhar apenas porque existem `pynput`, `pyautogui`, Selenium, OCR, captura ou ferramentas equivalentes usadas em escopo controlado.

## 7. Tratamento do legado

```text
LEGACY_CLICK_BEHAVIOR=ADAPTAR_WITH_CONTROLLED_BOUNDARY
LEGACY_DIRECT_UNSCOPED_CLICK=SUBSTITUIR
LEGACY_COORDINATES=ADAPTAR_AS_VERSIONED_TARGETS
LEGACY_TEST_CLICK=ADAPTAR_TO_CONTROLLED_HARNESS
```

Não se reutiliza o mecanismo legado sem guardas. O comportamento pode ser adaptado por contrato explícito, allowlist, autorização de sessão, kill switch, auditoria e limites.

## 8. Gates corrigidos

```text
CONTROLLED_AUTOMATION_POLICY=PASS
CONTROLLED_TARGET_CLASSIFICATION=PASS
CONTROLLED_CAPTURE_OCR_REPLAY=PASS
CONTROLLED_POINTER_KEYBOARD_CLICK=PASS
CONTROLLED_TEST_AUTH=PASS
ANALYSIS_EXECUTION_SEPARATION=PASS
FINANCIAL_EFFECT_SEPARATION=PASS
UNCONTROLLED_ACTION_NEGATIVE_PROOF_SPECIFIED=PASS
REAL_FINANCIAL_EFFECT_NEGATIVE_PROOF_SPECIFIED=PASS
```

## 9. Precedência documental

```text
PRECEDENCE_ORDER=
  POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
  > THIS_TRANSVERSAL_ADDENDUM
  > PTM_V2.7_REMEDIATION_ADDENDUM_FOR_SUPERSEDED_CLAUSES
  > PTM_V2.5|PTM_V2.6|PTM_V2.7_PARENT_DOCUMENTS_FOR_SUPERSEDED_CLAUSES
  > HISTORICAL_REVIEWS_AND_CHECKPOINTS
```

Documentos históricos não são apagados nem reescritos. Eles registram o entendimento anterior e não constituem bloqueio operacional atual.
