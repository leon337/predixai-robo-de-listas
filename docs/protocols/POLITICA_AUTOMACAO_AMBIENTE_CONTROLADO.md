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

Esta política substitui interpretações genéricas que tratavam captura, OCR, replay, análise de gráficos, ponteiro, teclado, preenchimento de campos, clique ou autenticação como capacidades proibidas em todo o projeto.

## 2. Regra central

Automação de interface é uma capacidade legítima do PredixAI Robô de Listas.

```text
CONTROLLED_CHART_ANALYSIS=ALLOWED
CONTROLLED_SCREEN_CAPTURE=ALLOWED
CONTROLLED_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_POINTER_MOVEMENT=ALLOWED
CONTROLLED_KEYBOARD_INPUT=ALLOWED
CONTROLLED_FIELD_FILLING=ALLOWED
CONTROLLED_CLICK=ALLOWED
CONTROLLED_AUTHENTICATION=ALLOWED
CONTROLLED_END_TO_END_TESTS=ALLOWED
SIMULATED_ORDER=ALLOWED
```

A autorização efetiva é determinada pelo modo ativo, pelo alvo autorizado, pela allowlist e pelos gates da sessão.

## 3. Classes de alvo autorizáveis

```text
FIRST_PARTY_APPLICATION
LOCAL_CONTROLLED_ENVIRONMENT
DEDICATED_TEST_SANDBOX
SANITIZED_FIXTURE_OR_REPLAY
EXPLICITLY_ALLOWLISTED_TEST_TARGET
OWNER_AUTHORIZED_BROKER_ACCOUNT
OWNER_AUTHORIZED_PLATFORM_SESSION
```

A falta de identificação do alvo bloqueia a ação específica. Ela não transforma a capacidade inteira em proibida.

## 4. Modo A — próprio, simulado ou controlado

O Modo A cobre aplicações próprias, ambientes locais, sandboxes, fixtures, replays, contas de teste e alvos explicitamente autorizados sem efeito financeiro real.

```text
MODE_A=CONTROLLED_OR_SIMULATED
MODE_A_DEFAULT=ENABLED_WHEN_MISSION_AUTHORIZES
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

## 5. Modo B — conta própria com possível efeito financeiro real

O Modo B é uma capacidade arquitetural suportada, mas separada. Ele permanece desligado por padrão e não é ativado pela simples existência desta política.

```text
MODE_B=LIVE_FINANCIAL_GATED
REAL_FINANCIAL_MODE=SUPPORTED_BY_SEPARATE_GATE
DEFAULT_STATE=DISABLED
AUTO_ENABLE=PROHIBITED
```

Ativação exige todos os gates aplicáveis:

```text
LIVE_MODE_EXPLICIT_SCOPE=PASS
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

Sem todos os gates:

```text
LIVE_MODE=DISABLED
FINANCIAL_EFFECT=BLOCKED_BY_GATE
CONTROLLED_MODE_A_REMAINS_AVAILABLE=YES
```

## 6. Separação obrigatória de conceitos

```text
REAL_UI_ACTION != REAL_FINANCIAL_EFFECT
CONTROLLED_CLICK != AUTOMATIC_LIVE_ACTIVATION
CONTROLLED_AUTHENTICATION != SECRET_PUBLICATION
SCREEN_CAPTURE != UNAUTHORIZED_DATA_COLLECTION
SIMULATED_ORDER != LIVE_FINANCIAL_ORDER
MODE_B_SUPPORTED != MODE_B_ARMED
```

Um clique real na interface pode ocorrer em Modo A sem produzir efeito financeiro real. Um clique capaz de produzir efeito financeiro exige Modo B armado e gates LIVE aprovados.

## 7. Condições comuns de controle

A automação deve possuir, conforme o risco aplicável:

- alvo identificado e autorizado;
- allowlist de aplicação, janela, processo, rota, conta ou fixture;
- sessão e modo declarados;
- possibilidade de parada imediata;
- logs e auditoria proporcionais;
- limites de frequência e concorrência;
- segredos fora do repositório;
- redaction de dados sensíveis;
- teste reversível ou ambiente restaurável quando aplicável;
- ausência de elevação silenciosa de Modo A para Modo B;
- confirmação explícita antes de qualquer sessão LIVE.

## 8. Limites permanentes

```text
SECRETS_IN_GIT=PROHIBITED
ENV_TOKENS_COOKIES_PRIVATE_KEYS_IN_GIT=PROHIBITED
PRODUCTION_CREDENTIAL_DISCLOSURE=PROHIBITED
UNAUTHORIZED_THIRD_PARTY_ACCESS=PROHIBITED
UNALLOWLISTED_TARGET_ACTION=PROHIBITED
SILENT_MODE_ESCALATION=PROHIBITED
LIVE_WITHOUT_GATE=PROHIBITED
```

A autorização A+B aplica-se a alvos próprios e autorizados. Ela não autoriza acesso a conta, plataforma ou sistema de terceiros sem permissão.

## 9. Aplicação por versão

### PTM V2.5

Ponteiro, teclado, campos e clique podem ficar fora do domínio de fundação. Isso significa `OUT_OF_SCOPE_FOR_STAGE`, não `GLOBALLY_PROHIBITED`.

### PTM V2.6

A pipeline analítica não autoriza nem executa ações por responsabilidade própria. Captura, análise visual, OCR e replay controlados são permitidos, assim como harnesses de teste autorizados.

### PTM V2.7

A V2.7 define comando, autorização, alvo, adaptador, dispatch, recibo, reconciliação e contenção.

```text
PTM_V2_7_CONTROLLED_UI_ADAPTER=ALLOWED
PTM_V2_7_SIMULATED_ADAPTER=ALLOWED
PTM_V2_7_LIVE_ADAPTER=SUPPORTED_BY_FUTURE_LIVE_GATE
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
FINANCIAL_EFFECT_BASELINE=SIMULATED_UNTIL_LIVE_GATE_PASS
```

## 10. Precedência e documentos históricos

Esta política prevalece sobre redações genéricas anteriores que afirmem, sem qualificação de alvo, modo ou etapa:

- proibição de análise de gráficos;
- proibição de captura ou OCR;
- proibição de replay;
- proibição de movimento de ponteiro;
- proibição de digitação ou preenchimento de campos;
- proibição de clique;
- proibição de autenticação controlada;
- proibição absoluta de suporte arquitetural ao modo LIVE.

Documentos históricos permanecem imutáveis como evidência do estado anterior. Documentos vivos e novos documentos arquiteturais devem referenciar esta política e usar terminologia qualificada.

Redação correta:

```text
OUT_OF_SCOPE_FOR_STAGE
ALLOWED_IN_MODE_A
SUPPORTED_BY_MODE_B_GATE
DISABLED_UNTIL_GATE_PASS
PROHIBITED_FOR_UNAUTHORIZED_TARGET
```

Redação genérica proibida em documentos vivos:

```text
DO_NOT_CLICK_GLOBALLY
DO_NOT_AUTHENTICATE_GLOBALLY
DO_NOT_MOVE_POINTER_GLOBALLY
DO_NOT_CAPTURE_OR_OCR_GLOBALLY
REAL_MODE_CAN_NEVER_EXIST
```

## 11. Gates de validação

```text
CONTROLLED_AUTOMATION_SCOPE_DEFINED=PASS
CONTROLLED_TARGET_ALLOWLIST_REQUIRED=PASS
CONTROLLED_CHART_ANALYSIS_ALLOWED=PASS
CONTROLLED_OCR_CAPTURE_ALLOWED=PASS
CONTROLLED_POINTER_KEYBOARD_FIELDS_CLICK_ALLOWED=PASS
CONTROLLED_AUTH_ALLOWED=PASS
SIMULATED_ORDER_ALLOWED=PASS
MODE_A_MODE_B_SEPARATED=PASS
LIVE_MODE_DEFAULT_DISABLED=PASS
LIVE_MODE_SEPARATE_GATE_REQUIRED=PASS
HISTORICAL_GENERIC_PROHIBITIONS_SUPERSEDED=PASS
```

## 12. Estado atual

A aprovação A+B define a arquitetura e a governança dos dois modos. Ela não executa a aplicação, não arma sessão LIVE e não cria autorização automática de implementação.

```text
MODE_A_POLICY=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_RUNTIME_ACTIVATION=NOT_STARTED
LIVE_GATE_IMPLEMENTATION=NOT_STARTED
CURRENT_DOCUMENTAL_WORK=DOCUMENTATION_ONLY
```