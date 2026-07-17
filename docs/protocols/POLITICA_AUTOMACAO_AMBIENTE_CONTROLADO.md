# POLÍTICA DE AUTOMAÇÃO — MODOS A E B

## 1. Status e autoridade

```text
DOCUMENT_STATUS=NORMATIVE_ACTIVE
POLICY=CONTROLLED_AND_LIVE_GATED_AUTOMATION
AUTHORIZED_BY=LEO
INITIAL_AUTHORIZATION_AT=2026-07-17
MODE_A_AND_B_CONFIRMED_AT=2026-07-17
REPOSITORY=leon337/predixai-robo-de-listas
APPLIES_TO=PTM_V2.5|PTM_V2.6|PTM_V2.7|ADRS|DOCUMENTO_MESTRE|FUTURE_IMPLEMENTATION
```

Esta política substitui interpretações genéricas que tratavam análise visual, captura, OCR, replay, ponteiro, teclado, preenchimento, clique ou autenticação como capacidades globalmente proibidas.

## 2. Modo A — próprio, simulado ou controlado

O Modo A cobre aplicações próprias, ambientes locais, sandboxes, fixtures, replays, contas de teste e alvos explicitamente autorizados sem efeito financeiro real.

```text
MODE_A=CONTROLLED_OR_SIMULATED
CHART_ANALYSIS=ALLOWED
SCREEN_CAPTURE=ALLOWED
OCR=ALLOWED
REPLAY=ALLOWED
POINTER_MOVEMENT=ALLOWED
KEYBOARD_INPUT=ALLOWED
FIELD_FILLING=ALLOWED
CLICK=ALLOWED
CONTROLLED_AUTHENTICATION=ALLOWED
E2E=ALLOWED
SIMULATED_ORDER=ALLOWED
REAL_FINANCIAL_EFFECT=NO
```

A falta de identificação do alvo bloqueia a ação específica. Ela não transforma a capacidade inteira em proibida.

## 3. Modo B — capacidade arquitetural condicionada

O Modo B é reconhecido apenas como capacidade arquitetural separada. Ele permanece desligado por padrão. Esta política não arma sessão, não autoriza implementação e não substitui autorização específica.

```text
MODE_B=LIVE_FINANCIAL_GATED
REAL_FINANCIAL_MODE=SUPPORTED_BY_SEPARATE_GATE
DEFAULT_STATE=DISABLED
AUTO_ENABLE=PROHIBITED
```

Qualquer futura ativação exige todos os gates abaixo, registrados e verificáveis:

```text
COMMERCIAL_AND_LEGAL_DECISION_RECORDED=PASS
PLATFORM_TERMS_AND_JURISDICTION_VALIDATED=PASS
ACCOUNT_HOLDER_ELIGIBILITY_VALIDATED=PASS
EXPLICIT_LIVE_SCOPE_AND_AUTHORIZATION=PASS
HUMAN_ARMING_REQUIRED=PASS
AUTHORIZED_ACCOUNT_ALLOWLIST=PASS
AUTHORIZED_PLATFORM_ALLOWLIST=PASS
EXPLICIT_LIVE_SESSION_CONFIRMATION=PASS
SESSION_LIMITS_DEFINED=PASS
MAX_OPERATION_LIMIT_DEFINED=PASS
LOSS_AND_EXPOSURE_LIMITS_DEFINED=PASS
KILL_SWITCH_AVAILABLE=PASS
AUDIT_RECEIPT_ENABLED=PASS
SECRET_ISOLATION=PASS
TARGET_IDENTITY_VALIDATED=PASS
ROLLBACK_OR_CONTAINMENT_PLAN=PASS
```

Sem qualquer gate:

```text
LIVE_MODE=DISABLED
FINANCIAL_EFFECT=BLOCKED_BY_GATE
CONTROLLED_MODE_A_REMAINS_AVAILABLE=YES
```

## 4. Separação obrigatória

```text
REAL_UI_ACTION != REAL_FINANCIAL_EFFECT
CONTROLLED_CLICK != AUTOMATIC_LIVE_ACTIVATION
CONTROLLED_AUTHENTICATION != SECRET_PUBLICATION
SIMULATED_ORDER != LIVE_FINANCIAL_ORDER
MODE_B_SUPPORTED != MODE_B_ARMED
TECHNICAL_GATE_PASS != COMMERCIAL_OR_LEGAL_APPROVAL
```

## 5. Condições comuns de controle

A automação deve possuir, conforme o risco aplicável:

- alvo identificado e autorizado;
- allowlist de aplicação, janela, processo, rota, conta ou fixture;
- sessão e modo declarados;
- possibilidade de parada imediata;
- logs e auditoria proporcionais;
- limites de frequência e concorrência;
- segredos fora do repositório;
- proteção de dados sensíveis;
- ausência de elevação silenciosa do Modo A para o Modo B.

## 6. Limites permanentes

```text
SECRETS_IN_GIT=PROHIBITED
PRODUCTION_CREDENTIAL_DISCLOSURE=PROHIBITED
UNAUTHORIZED_THIRD_PARTY_ACCESS=PROHIBITED
UNALLOWLISTED_TARGET_ACTION=PROHIBITED
SILENT_MODE_ESCALATION=PROHIBITED
LIVE_WITHOUT_ALL_GATES=PROHIBITED
```

A autorização A+B não supera contratos, termos da plataforma, legislação, jurisdição ou requisitos regulatórios aplicáveis.

## 7. Aplicação por versão

### PTM V2.5

Ponteiro, teclado, campos e clique podem ficar fora do domínio de fundação. Isso significa `OUT_OF_SCOPE_FOR_STAGE`, não `GLOBALLY_PROHIBITED`.

### PTM V2.6

A pipeline analítica não autoriza nem executa ações por responsabilidade própria. Captura, análise visual, OCR e replay controlados são permitidos em alvos autorizados.

### PTM V2.7

A V2.7 define comando, autorização, alvo, adaptador, dispatch, recibo, reconciliação e contenção.

```text
PTM_V2_7_CONTROLLED_UI_ADAPTER=ALLOWED
PTM_V2_7_SIMULATED_ADAPTER=ALLOWED
PTM_V2_7_LIVE_ADAPTER=SUPPORTED_BY_FUTURE_GATE
FINANCIAL_EFFECT_BASELINE=SIMULATED_UNTIL_ALL_LIVE_GATES_PASS
```

## 8. Precedência

Esta política prevalece sobre redações genéricas anteriores que proibiam globalmente análise de gráficos, captura, OCR, replay, movimento de ponteiro, digitação, preenchimento, clique ou autenticação controlada.

Documentos históricos permanecem como evidência do estado anterior. Documentos vivos devem usar terminologia qualificada:

```text
OUT_OF_SCOPE_FOR_STAGE
ALLOWED_IN_MODE_A
SUPPORTED_BY_MODE_B_GATE
DISABLED_UNTIL_GATE_PASS
PROHIBITED_FOR_UNAUTHORIZED_TARGET
```

## 9. Gates de validação

```text
CONTROLLED_AUTOMATION_SCOPE_DEFINED=PASS
CONTROLLED_TARGET_ALLOWLIST_REQUIRED=PASS
MODE_A_MODE_B_SEPARATED=PASS
LIVE_MODE_DEFAULT_DISABLED=PASS
LIVE_MODE_SEPARATE_GATE_REQUIRED=PASS
MODE_B_COMMERCIAL_LEGAL_GATE_REQUIRED=PASS
MODE_B_PLATFORM_COMPLIANCE_GATE_REQUIRED=PASS
MODE_B_ACCOUNT_ELIGIBILITY_GATE_REQUIRED=PASS
MODE_B_EXPLICIT_SCOPE_GATE_REQUIRED=PASS
HISTORICAL_GENERIC_PROHIBITIONS_SUPERSEDED=PASS
```

## 10. Estado atual

```text
MODE_A_POLICY=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_RUNTIME_ACTIVATION=NOT_STARTED
LIVE_GATE_IMPLEMENTATION=NOT_STARTED
COMMERCIAL_LEGAL_LIVE_DECISION=NOT_STARTED
PLATFORM_COMPLIANCE_VALIDATION=NOT_STARTED
ACCOUNT_ELIGIBILITY_VALIDATION=NOT_STARTED
CURRENT_DOCUMENTAL_WORK=DOCUMENTATION_ONLY
```
