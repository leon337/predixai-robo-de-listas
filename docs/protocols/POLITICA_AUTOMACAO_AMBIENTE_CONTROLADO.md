# POLÍTICA DE AUTOMAÇÃO EM AMBIENTE CONTROLADO

## 1. Status e autoridade

```text
DOCUMENT_STATUS=NORMATIVE_ACTIVE
POLICY=CONTROLLED_ENVIRONMENT_AUTOMATION
AUTHORIZED_BY=LEO
AUTHORIZED_AT=2026-07-17
REPOSITORY=leon337/predixai-robo-de-listas
APPLIES_TO=PTM_V2.5|PTM_V2.6|PTM_V2.7|FUTURE_DOCUMENTATION
```

Esta política corrige a interpretação excessivamente ampla de proibições anteriores. Exclusões locais de uma PTM não constituem proibição global de OCR, captura, replay ou automação de interface.

## 2. Regra central

```text
CONTROLLED_UI_AUTOMATION=ALLOWED
CONTROLLED_SCREEN_CAPTURE=ALLOWED
CONTROLLED_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_POINTER_MOVEMENT=ALLOWED
CONTROLLED_KEYBOARD_INPUT=ALLOWED
CONTROLLED_CLICK=ALLOWED
CONTROLLED_TEST_AUTHENTICATION=ALLOWED
CONTROLLED_END_TO_END_TESTS=ALLOWED
```

As capacidades acima são permitidas quando o alvo pertence a uma destas classes:

```text
FIRST_PARTY_APPLICATION
LOCAL_CONTROLLED_ENVIRONMENT
DEDICATED_TEST_SANDBOX
SANITIZED_FIXTURE_OR_REPLAY
EXPLICITLY_ALLOWLISTED_TEST_TARGET
```

## 3. Separação obrigatória de conceitos

```text
REAL_UI_ACTION != REAL_FINANCIAL_EFFECT
CONTROLLED_CLICK != EXTERNAL_FINANCIAL_ORDER
TEST_AUTHENTICATION != PRODUCTION_CREDENTIAL_PUBLICATION
SCREEN_CAPTURE != UNAUTHORIZED_DATA_COLLECTION
```

O termo `real` aplicado a ponteiro, teclado ou clique significa que a ação ocorre na interface controlada. Isso não autoriza, por si só, operação financeira, alteração de saldo ou efeito em sistema externo de produção.

## 4. Condições de controle

Automação controlada deve possuir, conforme o risco aplicável:

- alvo explicitamente identificado e autorizado;
- allowlist de aplicação, janela, processo, rota ou fixture;
- sessão e modo declarados;
- possibilidade de parada imediata;
- logs e auditoria proporcionais;
- limites de frequência e concorrência;
- segredo de teste fora do repositório;
- redaction de dados sensíveis;
- teste reversível ou ambiente restaurável;
- ausência de elevação silenciosa para alvo externo não autorizado.

A falta de identidade do alvo bloqueia a ação específica, mas não transforma a capacidade inteira em proibida.

## 5. Limites permanentes

```text
SECRETS_IN_GIT=PROHIBITED
ENV_TOKENS_COOKIES_PRIVATE_KEYS_IN_GIT=PROHIBITED
UNAUTHORIZED_THIRD_PARTY_ACCESS=PROHIBITED
REAL_MONEY_OPERATION=NOT_AUTHORIZED_BY_THIS_POLICY
EXTERNAL_FINANCIAL_ORDER=NOT_AUTHORIZED_BY_THIS_POLICY
REAL_BALANCE_CHANGE=NOT_AUTHORIZED_BY_THIS_POLICY
PRODUCTION_CREDENTIAL_DISCLOSURE=PROHIBITED
```

Operação financeira real, ordem financeira externa ou alteração de saldo real exigem decisão comercial e legal separada, escopo próprio, arquitetura específica e autorização explícita **em qualquer classe de alvo**, inclusive aplicação própria, ambiente local, sandbox ou teste allowlisted que possa alcançar infraestrutura financeira de produção.

A classificação como aplicação própria ou ambiente controlado dispensa apenas a proibição genérica de automação de interface. Ela nunca transforma autorização de OCR, ponteiro, teclado ou clique em autorização de efeito financeiro real.

Atuação externa não financeira também exige autorização específica quando o alvo não for próprio ou não estiver explicitamente allowlisted.

## 6. Aplicação por versão

### PTM V2.5

Movimento, teclado e clique podem permanecer fora do domínio de fundação V2.5. Isso significa `OUT_OF_SCOPE_FOR_STAGE`, não `GLOBALLY_PROHIBITED`.

### PTM V2.6

A pipeline de observação e análise não deve produzir efeito de UI por responsabilidade própria. Captura, OCR e replay controlados são permitidos. Harnesses de teste controlados também são permitidos, desde que não confundidos com o domínio analítico.

### PTM V2.7

A V2.7 pode definir e futuramente implementar adaptadores de automação de UI controlada para aplicações próprias e sandboxes. O baseline financeiro permanece sem ordem e sem alteração de saldo real.

```text
PTM_V2_7_CONTROLLED_UI_ADAPTER=ALLOWED
PTM_V2_7_EXTERNAL_FINANCIAL_ADAPTER=NOT_AUTHORIZED
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
```

## 7. Precedência

Esta política prevalece sobre redações genéricas anteriores que afirmem, sem qualificação de alvo ou etapa:

- proibição de captura ou OCR;
- proibição de replay;
- proibição de movimento de ponteiro;
- proibição de digitação;
- proibição de clique;
- proibição de autenticação de teste.

Documentos históricos permanecem imutáveis como evidência do estado anterior. Documentos vivos e arquiteturais devem referenciar esta política e usar terminologia qualificada.

Nenhuma precedência desta política enfraquece os limites permanentes contra efeito financeiro real, segredo em Git ou acesso externo não autorizado.

## 8. Gates de validação

```text
CONTROLLED_AUTOMATION_SCOPE_DEFINED=PASS
CONTROLLED_TARGET_ALLOWLIST_REQUIRED=PASS
CONTROLLED_OCR_CAPTURE_ALLOWED=PASS
CONTROLLED_POINTER_KEYBOARD_CLICK_ALLOWED=PASS
CONTROLLED_TEST_AUTH_ALLOWED=PASS
REAL_FINANCIAL_EFFECT_SEPARATED=PASS
REAL_FINANCIAL_EFFECT_REQUIRES_SEPARATE_AUTH_IN_ALL_TARGET_CLASSES=PASS
HISTORICAL_DOCUMENTS_NON_NORMATIVE=PASS
```
