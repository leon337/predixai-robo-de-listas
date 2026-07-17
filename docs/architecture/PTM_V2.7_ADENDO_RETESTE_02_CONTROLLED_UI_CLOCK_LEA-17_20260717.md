# PTM V2.7 — ADENDO NORMATIVO DE RETESTE 02

## CONTROLLED_UI, efeito financeiro e recovery temporal

## 1. Controle

```text
DOCUMENT_STATUS=NORMATIVE_REMEDIATION_READY_FOR_RETEST
MISSION=LEA-16
REVIEW_ISSUE=LEA-17
PARENT_DOCUMENT=docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md
PREVIOUS_REMEDIATION=docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md
CONTROLLED_AUTOMATION_POLICY=docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
APPLICATION_CODE_CHANGED=NO
RUNTIME_EXECUTED=NO
```

Este adendo substitui as cláusulas conflitantes do documento pai e do primeiro adendo quanto ao modo do adaptador, estados de execução, recibos e recuperação após restart.

## 2. Duas dimensões independentes

```text
EXECUTION_CHANNEL=NONE|NULL|SIMULATED|CONTROLLED_UI
FINANCIAL_EFFECT_MODE=NONE|SIMULATED_ONLY
```

`CONTROLLED_UI` representa ação física de interface em aplicação própria, sandbox ou alvo de teste allowlisted. Ele não representa e não pode declarar ordem financeira real, alteração de saldo real ou efeito financeiro de produção.

```text
CONTROLLED_UI + FINANCIAL_EFFECT_MODE=NONE      = ALLOWED
CONTROLLED_UI + FINANCIAL_EFFECT_MODE=SIMULATED_ONLY = ALLOWED_FOR_SIMULATED_FINANCIAL_FIXTURE
CONTROLLED_UI + REAL_FINANCIAL_EFFECT           = INVALID_AND_BLOCKED
```

A restrição financeira aplica-se a todas as classes de alvo, inclusive aplicação própria que possua ligação com backend financeiro real.

## 3. Estados normativos substitutos

```text
DISABLED
SAFE_IDLE
VALIDATING
ARMED_DRY_RUN
ARMED_SIMULATED
ARMED_CONTROLLED_UI
DISPATCHING
AWAITING_RECEIPT
RECONCILING
COMPLETED_NO_EFFECT
COMPLETED_SIMULATED
COMPLETED_CONTROLLED_UI
BLOCKED
CANCELLED
TIMED_OUT
UNKNOWN_EFFECT
KILLED
FAILED_NO_EFFECT
```

Regras:

- `ARMED_CONTROLLED_UI` exige alvo allowlisted, autorização humana vinculada ao comando, adaptador com capacidade `CONTROLLED_UI`, kill switch saudável, limites válidos e `financial_effect_mode` compatível;
- `DISPATCHING` registra a tentativa antes de qualquer ação de UI;
- `COMPLETED_CONTROLLED_UI` confirma somente o efeito de interface reconciliado;
- nenhum estado confirma ordem financeira, alteração de saldo ou resultado financeiro real;
- dúvida sobre alvo, capacidade, sessão, política ou dimensão financeira resulta em `BLOCKED`;
- `ARMED_SIMULATED` não é usado para mascarar uma ação física de UI.

## 4. ExecutionCommand revisado

```text
command_id
trace_id
signal_id
signal_fingerprint
idempotency_key
execution_channel=DRY_RUN|SIMULATED|CONTROLLED_UI
financial_effect_mode=NONE|SIMULATED_ONLY
target_class
target_logical_id
target_identity_hash
action_type
action_payload_sanitized_hash
action_allowlist_version
context_snapshot_hash
policy_version
adapter_contract_version
created_at_utc
expires_at_utc
ttl_ms
clock_source_id
boot_id_at_creation
process_instance_id_at_creation
deadline_monotonic_process_local
status
```

`action_type` pode representar movimento, entrada de teclado, clique, captura, OCR, replay ou autenticação de teste. O payload persistido deve ser sanitizado e não pode conter credencial de produção.

## 5. AuthorizationGrant revisado

```text
authorization_id
command_hash
actor_id
client_id
session_id
allowed_execution_channel
allowed_financial_effect_mode
target_class
target_identity_hash
action_allowlist_version
policy_version
issued_at_utc
expires_at_utc
revoked_at_utc
reason_code
```

Mudança de canal, alvo, ação, allowlist, política ou dimensão financeira invalida o grant.

## 6. Contrato de adaptador

Capacidades permitidas:

```text
NULL
SIMULATED
CONTROLLED_UI
```

Contrato `CONTROLLED_UI`:

```text
adapter_name
adapter_version
capability=CONTROLLED_UI
supported_target_classes
supported_action_types
requires_foreground_identity
requires_kill_switch
requires_human_authorization
financial_effect_capability=NONE|SIMULATED_ONLY
```

O adaptador deve bloquear antes da ação quando:

- alvo não estiver allowlisted;
- identidade de janela, processo, rota ou aplicação divergir;
- ação não estiver na allowlist;
- autorização estiver ausente, expirada, revogada ou incompatível;
- kill switch estiver ativo ou indisponível;
- capacidade financeira declarada não for `NONE|SIMULATED_ONLY`;
- segredo de produção ou payload sensível proibido for detectado.

## 7. EffectReceipt revisado

```text
receipt_id
attempt_id
adapter_name
adapter_version
execution_channel=NULL|SIMULATED|CONTROLLED_UI
target_identity_hash
action_type
ui_result=NO_EFFECT|CONTROLLED_UI_EFFECT|UNKNOWN
financial_result=NONE|SIMULATED_EFFECT|UNKNOWN
result_hash
produced_at_utc
sequence
reason_code
```

Regras:

- `ui_result=CONTROLLED_UI_EFFECT` não implica efeito financeiro;
- `financial_result` nunca aceita valor de produção real nesta PTM;
- ausência ou divergência de recibo resulta em `UNKNOWN_EFFECT` ou `BLOCKED`;
- conclusão exige reconciliação independente das dimensões UI e financeira.

## 8. Requisitos funcionais substituídos

```text
V27-EXE-001=Dispatch ocorre somente no estado ARMED correspondente ao execution_channel autorizado.
V27-EXE-003=Adaptador declara NULL, SIMULATED ou CONTROLLED_UI; capacidade desconhecida bloqueia.
V27-EXE-004=CONTROLLED_UI recebe alvo e ação allowlisted, payload sanitizado e financial_effect_mode NONE|SIMULATED_ONLY.
V27-SAF-004=Módulos V2.7 podem usar bibliotecas de UI somente pelo adaptador CONTROLLED_UI e nunca por bypass do contrato.
V27-SAF-006=Coordenadas podem integrar target versionado e allowlisted; coordenada isolada não autoriza ação.
V27-QA-006=Testes provam ausência de bypass, alvo não autorizado, segredo de produção e efeito financeiro real.
```

## 9. Recovery temporal reforçado

### 9.1 Regra de restart

Qualquer mudança de `process_instance_id` torna todo comando não terminal criado pela instância anterior **não despachável**, mesmo quando o boot não mudou e o relógio UTC aparenta estar dentro da validade.

```text
PROCESS_INSTANCE_CHANGED=RESTART_DETECTED
PRE_RESTART_COMMAND_DISPATCHABLE=NO
PRE_RESTART_COMMAND_AUTO_REARM=NO
PRE_RESTART_COMMAND_AUTO_REDISPATCH=NO
PRE_RESTART_COMMAND_ACTION=BLOCK_AND_RECONCILE
NEW_ACTION_REQUIRES=NEW_COMMAND_AND_NEW_AUTHORIZATION
```

Essa regra elimina a dependência de inferir tempo decorrido por relógio de parede após restart. `created_at_utc`, `expires_at_utc` e `ttl_ms` permanecem para auditoria, expiração e diagnóstico, mas não restauram a despachabilidade do comando anterior.

### 9.2 Mesmo processo

Somente durante a mesma `process_instance_id` o orçamento `deadline_monotonic_process_local` pode autorizar continuação, desde que UTC, fonte temporal, boot e política permaneçam válidos.

### 9.3 Recovery

Após restart:

- tentativa já despachada entra em reconciliação e pode resultar em `UNKNOWN_EFFECT`;
- comando ainda não despachado é bloqueado e encerrado sem efeito;
- nenhum comando anterior retorna a `ARMED_*`;
- qualquer nova ação exige novo `command_id`, novo snapshot e nova autorização;
- relógio rollback ou skew continuam gerando bloqueio e incidente de auditoria.

Reason codes adicionais:

```text
PROCESS_INSTANCE_CHANGED
PRE_RESTART_COMMAND_INVALIDATED
NEW_COMMAND_REQUIRED_AFTER_RESTART
NEW_AUTHORIZATION_REQUIRED_AFTER_RESTART
```

## 10. Gates

```text
CONTROLLED_UI_NORMATIVE_CONTRACT=PASS_BUILDER_REMEDIATED
CONTROLLED_UI_STATE_MODEL=PASS_BUILDER_REMEDIATED
CONTROLLED_UI_RECEIPT_SEMANTICS=PASS_BUILDER_REMEDIATED
FINANCIAL_EFFECT_INDEPENDENT_DIMENSION=PASS_BUILDER_REMEDIATED
REAL_FINANCIAL_EFFECT_BLOCKED_FOR_ALL_TARGET_CLASSES=PASS
SAME_BOOT_RESTART_FAIL_CLOSED=PASS_BUILDER_REMEDIATED
CLOCK_ROLLBACK_CANNOT_EXTEND_DISPATCHABILITY=PASS_BUILDER_REMEDIATED
INDEPENDENT_RETEST_REQUIRED=YES
```

## 11. Precedência

```text
PRECEDENCE_ORDER=
  POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
  > THIS_RETEST_02_ADDENDUM
  > ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA
  > PTM_V2.7_ADENDO_REMEDIACAO_01_FOR_NON_CONFLICTING_CLAUSES
  > PTM_V2.7_PARENT_FOR_NON_CONFLICTING_CLAUSES
```
