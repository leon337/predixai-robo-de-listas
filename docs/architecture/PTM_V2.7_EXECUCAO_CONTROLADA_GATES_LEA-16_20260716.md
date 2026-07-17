# PTM V2.7 — EXECUÇÃO CONTROLADA E GATES DE SEGURANÇA

## LEA-16 — Builder Draft

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DRAFT
MISSION=LEA-16
LINEAR_ISSUE=LEA-16
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=f3c84d97523c1c631392cefb69b6cb3e8f6a56e2
WORKING_BRANCH=leonpcsn/lea-16-ptm-v27-execucao-controlada-e-gates-de-seguranca
LEGACY_VERSION=V2.4.3-R1
PTM_V2_5_DEFINITIVE=YES_DOCUMENTAL
PTM_V2_6_DEFINITIVE=YES_DOCUMENTAL
EXECUTION_CAPABILITY_BASELINE=SIMULATED_ONLY
REAL_EXECUTION_ADAPTER_EXISTS=NO
CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
WORKFLOWS_CHANGED=NO
APPLICATION_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
POINTER_MOVEMENT_EXECUTED=NO
KEYBOARD_INPUT_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
REAL_ORDER_EXECUTED=NO
IMPLEMENTATION_AUTHORIZED=NO
PTM_V2_7_CRITICAL_REVIEW=PENDING
```

Este documento define a arquitetura documental da PTM V2.7. Ele não autoriza implementação, integração com corretora, autenticação, captura em runtime, movimento de ponteiro, teclado, clique, ordem, compra, venda ou alteração de saldo real.

## 2. Fontes de autoridade

1. `PROJECT_RUNTIME_STATE.yaml`;
2. `PROJECT_STATE.md`;
3. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
4. `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md`;
5. `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md`;
6. `docs/architecture/PTM_V2.6_OBSERVACAO_ANALISE_SINAIS_LEA-14_20260716.md`;
7. `docs/architecture/PTM_V2.6_MATRIZ_RASTREABILIDADE_LEA-14_20260716.md`;
8. Auditoria Mestra V2.4.3-R1, Anexo A e apêndices;
9. revisão crítica aprovada da Auditoria Mestra;
10. protocolos oficiais de autoridade, segurança, continuidade e revisão crítica;
11. issue Linear `LEA-16`.

## 3. Fronteira da versão

```text
V2_5=FOUNDATION_AND_SAFE_MIGRATION_DESIGN
V2_6=OBSERVATION_ANALYSIS_AND_SIMULATED_SIGNALS
V2_7=CONTROLLED_EXECUTION_DOMAIN_WITH_SIMULATED_ONLY_BASELINE
```

A V2.7 recebe somente sinais V2.6 validados e ainda elegíveis. Um sinal não é comando, autorização ou efeito. A V2.7 transforma uma intenção autorizada em tentativa controlada, recibo e reconciliação, mas o baseline documental atual oferece apenas adaptador nulo ou simulado.

```text
VALIDATED_SIGNAL != EXECUTION_COMMAND
EXECUTION_COMMAND != AUTHORIZATION_GRANT
AUTHORIZATION_GRANT != EFFECT
DISPATCH_ATTEMPT != CONFIRMED_EFFECT
```

## 4. Decisão arquitetural principal

```text
EXECUTION_MODE_ALLOWED=DISABLED|DRY_RUN|SIMULATED
REAL_MODE_ENUM_EXPOSED=NO
REAL_ADAPTER_IMPLEMENTED=NO
REAL_CREDENTIALS_ACCEPTED=NO
REAL_TARGET_RESOLUTION_ALLOWED=NO
REAL_SIDE_EFFECT_ALLOWED=NO
```

Qualquer capacidade futura de efeito físico ou financeiro exigirá decisão comercial e legal explícita, ADR própria, threat model, implementação autorizada, testes em camadas, revisão crítica independente, gate de prontidão e GO humano separado. A PTM V2.7 não satisfaz esses requisitos por si só.

## 5. Invariantes

- sinal nunca se autoexecuta;
- executor nunca cria, altera ou reinterpreta estratégia;
- autorização é explícita, limitada, temporária, revogável e vinculada ao comando exato;
- ausência, dúvida, divergência ou dado desconhecido bloqueia;
- configuração segura domina configuração conveniente;
- o servidor é autoridade do estado; Android ou UI são clientes, não autoridade global;
- toda tentativa possui `trace_id`, `command_id`, `authorization_id` e `idempotency_key`;
- mesma chave idempotente não produz dois efeitos;
- retry somente ocorre quando a ausência de efeito é comprovada;
- timeout não equivale a falha sem efeito;
- efeito desconhecido exige reconciliação e bloqueia nova tentativa correlata;
- kill switch domina fila, autorização, retry e dispatch;
- limites não podem ser ampliados automaticamente;
- adaptador simulado não pode carregar bibliotecas de ponteiro, teclado, clique ou ordem;
- coordenadas são metadados geométricos, nunca autorização;
- nenhuma persistência física nasce sem produtor, consumidor, requisito, teste e retenção;
- auditoria é append-only conceitual e separada de logs diagnósticos;
- recuperação nunca apaga evidência de tentativa ou efeito desconhecido.

## 6. Modelo de estados

```text
DISABLED
  -> SAFE_IDLE
  -> VALIDATING
  -> ARMED_SIMULATED
  -> DISPATCHING
  -> AWAITING_RECEIPT
  -> RECONCILING
  -> COMPLETED_SIMULATED
```

Estados terminais ou de contenção:

```text
BLOCKED
CANCELLED
TIMED_OUT
UNKNOWN_EFFECT
KILLED
FAILED_NO_EFFECT
```

Regras:

- `DISABLED` é o estado inicial e seguro;
- `SAFE_IDLE` permite observação de estado, nunca efeito;
- `VALIDATING` congela o snapshot de pré-condições;
- `ARMED_SIMULATED` existe somente com autorização válida e adaptador simulado;
- `DISPATCHING` registra tentativa antes de invocar o adaptador;
- `AWAITING_RECEIPT` não permite retry paralelo;
- `RECONCILING` compara intenção, tentativa, recibo e estado simulado;
- `UNKNOWN_EFFECT` bloqueia comandos correlatos até resolução explícita;
- `KILLED` exige rearmamento humano após diagnóstico;
- não existe estado `ARMED_REAL` nesta versão.

## 7. Requisitos estruturais

| ID | Requisito | Origem e tratamento | Gate |
|---|---|---|---|
| PTM-V27-001 | Sinal, comando, autorização, tentativa, efeito e recibo são domínios separados. | V2.6 separa sinal de execução; mecanismo novo. | `EXECUTION_DOMAIN_BOUNDARY` |
| PTM-V27-002 | O baseline aceita somente `DISABLED`, `DRY_RUN` e `SIMULATED`. | Segurança permanente; modo real inexistente. | `SIMULATED_ONLY_BASELINE` |
| PTM-V27-003 | Adaptador real, credenciais reais e integração de ordem não existem no baseline. | Clique legado `pynput`: DESCONTINUAR. | `REAL_ADAPTER_ABSENT` |
| PTM-V27-004 | Comando é imutável, versionado e vinculado a sinal elegível e snapshot de contexto. | `command_id` V2.5 e sinal V2.6: ADAPTAR. | `IMMUTABLE_COMMAND` |
| PTM-V27-005 | Autorização é entidade própria, limitada por modo, alvo lógico, comando, validade e política. | Android Foundation e segurança local: ADAPTAR. | `EXPLICIT_AUTHORIZATION` |
| PTM-V27-006 | Pré-condições são congeladas e revalidadas imediatamente antes do dispatch. | Fail-closed V2.5/V2.6: ADAPTAR. | `PRE_DISPATCH_REVALIDATION` |
| PTM-V27-007 | Policy engine puro decide `ALLOW_SIMULATED`, `BLOCK`, `CANCEL` ou `REQUIRE_REAUTH`. | Mecanismo novo. | `EXECUTION_POLICY_ENGINE` |
| PTM-V27-008 | Resolução de alvo usa identificadores lógicos e geometria versionada; coordenada isolada é inválida. | Click targets legados: ADAPTAR geometria, DESCONTINUAR ação. | `TARGET_RESOLUTION` |
| PTM-V27-009 | Adaptadores implementam contrato comum e declaram capacidades; adaptador nulo é obrigatório. | Isolamento de plataforma V2.5: ADAPTAR. | `EXECUTION_ADAPTER_CONTRACT` |
| PTM-V27-010 | Intenção de efeito é registrada antes da invocação e não confirma resultado. | Auditoria de comandos V2.5: ADAPTAR. | `INTENT_BEFORE_EFFECT` |
| PTM-V27-011 | Toda tentativa possui chave idempotente determinística. | Migração idempotente V2.5: ADAPTAR. | `IDEMPOTENCY_KEY` |
| PTM-V27-012 | Registro de deduplicação impede reenvio simultâneo ou posterior incompatível. | Mecanismo novo. | `DEDUPLICATION_REGISTRY` |
| PTM-V27-013 | Lifecycle do executor é explícito e sem monkey patch. | Runtime guard: ADAPTAR; patch chain: SUBSTITUIR. | `EXECUTION_STATE_MACHINE` |
| PTM-V27-014 | Deadline e timeout são monotônicos e preservam distinção entre sem efeito e efeito desconhecido. | Mecanismo novo. | `DEADLINE_AND_TIMEOUT` |
| PTM-V27-015 | Retry é proibido quando efeito não pode ser descartado. | Risco crítico de duplicidade; mecanismo novo. | `SAFE_RETRY_POLICY` |
| PTM-V27-016 | Circuit breaker bloqueia novas tentativas após sequência ou categoria crítica de falhas. | Guardas do legado: ADAPTAR. | `CIRCUIT_BREAKER` |
| PTM-V27-017 | Limites de frequência, concorrência, sessão e lote possuem safe defaults e não autoescalam. | Rate limit V2.5: ADAPTAR. | `OPERATIONAL_LIMITS` |
| PTM-V27-018 | Comandos conflitantes sobre o mesmo alvo lógico são serializados ou bloqueados. | Arbitragem V2.6: ADAPTAR. | `CONCURRENCY_CONTROL` |
| PTM-V27-019 | Kill switch local e remoto auditável domina todos os fluxos. | Requisito novo de segurança. | `KILL_SWITCH` |
| PTM-V27-020 | Presença e confirmação humana são exigidas para armar sessão simulada. | Android não é autoridade; autorização explícita. | `HUMAN_IN_THE_LOOP` |
| PTM-V27-021 | Dry-run e simulação produzem recibos determinísticos sem fonte externa real. | Replay seguro V2.6: ADAPTAR. | `SIMULATED_EFFECT_ADAPTER` |
| PTM-V27-022 | Recibo do adaptador é evidência, não verdade global; reconciliação é obrigatória. | Fonte externa não é autoridade interna. | `EFFECT_RECEIPT` |
| PTM-V27-023 | Reconciliação compara comando, tentativa, recibo e estado simulado observado. | Reconciliação V2.5: ADAPTAR. | `EXECUTION_RECONCILIATION` |
| PTM-V27-024 | Compensação é comando novo e nunca rollback cego de efeito. | Recovery V2.5: ADAPTAR. | `COMPENSATION_POLICY` |
| PTM-V27-025 | `UNKNOWN_EFFECT` bloqueia novas ações correlatas e exige resolução explícita. | Mecanismo novo. | `UNKNOWN_EFFECT_CONTAINMENT` |
| PTM-V27-026 | Auditoria separa autorização, comando, tentativa, efeito, segurança e diagnóstico. | Observabilidade V2.5: ADAPTAR. | `EXECUTION_AUDIT` |
| PTM-V27-027 | Métricas e tracing correlacionam sinal até reconciliação sem dados sensíveis. | `trace_id` V2.5 e trace V2.6: ADAPTAR. | `EXECUTION_OBSERVABILITY` |
| PTM-V27-028 | Segredos, cookies, tokens, telas e credenciais reais são rejeitados e redigidos. | Segurança permanente. | `EXECUTION_DATA_SECURITY` |
| PTM-V27-029 | REST, eventos e persistência seguem existência progressiva e testes verticais. | Política V2.5/V2.6: ADAPTAR. | `PROGRESSIVE_EXECUTION_CONTRACTS` |
| PTM-V27-030 | Recovery restaura estado seguro, preserva auditoria e nunca reenvia automaticamente. | Recovery e backup V2.5: ADAPTAR. | `SAFE_EXECUTION_RECOVERY` |
| PTM-V27-031 | Prova negativa verifica ausência de imports e chamadas de ponteiro, teclado, clique e ordem. | `pynput` legado: DESCONTINUAR. | `REAL_EFFECT_NEGATIVE_PROOF` |
| PTM-V27-032 | Qualquer modo real futuro depende de ADR, threat model, testes, revisão independente e GO separado. | Governança permanente. | `FUTURE_REAL_ACTIVATION_GATE` |

## 8. Requisitos funcionais

### 8.1 Pré-condições e sessão

| ID | Critério de aceite arquitetural |
|---|---|
| V27-PRE-001 | Inicializar sempre em `DISABLED`; nenhuma configuração pode elevar automaticamente o modo. |
| V27-PRE-002 | Entrar em `SAFE_IDLE` somente com configuração, relógio, identidade de sessão e dependências válidas. |
| V27-PRE-003 | Criar sessão simulada com operador, cliente, política, limites e versão de adaptador resolvidos. |
| V27-PRE-004 | Perda de cliente, identidade, política ou integridade degrada para `BLOCKED` ou `KILLED`. |
| V27-PRE-005 | Congelar snapshot de pré-condições antes do arming e revalidar antes do dispatch. |
| V27-PRE-006 | Encerramento revoga autorizações, cancela fila não despachada e preserva auditoria. |

### 8.2 Comando e elegibilidade

| ID | Critério de aceite arquitetural |
|---|---|
| V27-CMD-001 | Aceitar somente sinal V2.6 validado, não expirado, não invalidado e com fingerprint íntegra. |
| V27-CMD-002 | Criar comando imutável com versão, modo, alvo lógico, ação simulada, prazo e origem. |
| V27-CMD-003 | Rejeitar comando sem `trace_id`, `command_id`, `signal_id` e `idempotency_key`. |
| V27-CMD-004 | Rejeitar alteração de direção, alvo, prazo ou contexto após autorização. |
| V27-CMD-005 | Duplicidade exata retorna o resultado anterior; duplicidade divergente bloqueia. |
| V27-CMD-006 | Comando cancelado, expirado ou supersedido nunca volta à fila. |

### 8.3 Autorização e política

| ID | Critério de aceite arquitetural |
|---|---|
| V27-AUT-001 | Criar autorização somente por ação humana explícita e autenticada em sessão autorizada. |
| V27-AUT-002 | Vincular autorização ao hash do comando, modo, validade e política aplicável. |
| V27-AUT-003 | Revogação entra em vigor antes de qualquer nova tentativa. |
| V27-AUT-004 | Mudança de comando, contexto, política ou adaptador exige nova autorização. |
| V27-AUT-005 | Policy engine retorna reason codes estáveis e não usa texto livre como decisão única. |
| V27-AUT-006 | UI ou Android não podem marcar efeito como concluído nem alterar auditoria do servidor. |

### 8.4 Dispatch e adaptador

| ID | Critério de aceite arquitetural |
|---|---|
| V27-EXE-001 | Dispatch só ocorre em `ARMED_SIMULATED` após revalidação integral. |
| V27-EXE-002 | Registrar tentativa durável conceitual antes de chamar adaptador. |
| V27-EXE-003 | Adaptador declara `NULL` ou `SIMULATED`; qualquer capacidade desconhecida bloqueia. |
| V27-EXE-004 | Adaptador simulado recebe somente payload sanitizado, sem credenciais ou coordenadas reais. |
| V27-EXE-005 | Timeout move para `TIMED_OUT` ou `UNKNOWN_EFFECT`, nunca para sucesso presumido. |
| V27-EXE-006 | Retry exige prova de `FAILED_NO_EFFECT` e reutiliza a mesma chave idempotente. |
| V27-EXE-007 | Circuit breaker aberto rejeita dispatch antes de invocar adaptador. |
| V27-EXE-008 | Kill switch interrompe fila, bloqueia retry e impede rearmamento automático. |

### 8.5 Limites e segurança

| ID | Critério de aceite arquitetural |
|---|---|
| V27-SAF-001 | Limites possuem versão, origem, safe default e redução imediata; ampliação exige nova autorização. |
| V27-SAF-002 | Apenas um comando conflitante por alvo lógico pode estar em dispatch/reconciliação. |
| V27-SAF-003 | Fila tem capacidade limitada; overflow bloqueia sem descartar silenciosamente. |
| V27-SAF-004 | Nenhum módulo V2.7 importa ou chama `pynput`, `pyautogui`, Selenium de clique ou API de ordem. |
| V27-SAF-005 | Nenhum endpoint aceita senha, cookie, token ou chave de corretora. |
| V27-SAF-006 | Coordenadas de calibração não entram no payload do adaptador simulado. |
| V27-SAF-007 | Eventos e relatórios aplicam redaction, minimização e retenção definida. |
| V27-SAF-008 | Falha de integridade, relógio, sequência ou assinatura bloqueia antes do arming. |

### 8.6 Recibo e reconciliação

| ID | Critério de aceite arquitetural |
|---|---|
| V27-REC-001 | Recibo declara adaptador, versão, tentativa, tempo, resultado e hash. |
| V27-REC-002 | Recibo duplicado idêntico é idempotente; divergente abre incidente. |
| V27-REC-003 | Reconciliação compara intenção, tentativa, recibo e estado simulado. |
| V27-REC-004 | Divergência resulta em `UNKNOWN_EFFECT` ou `BLOCKED`, nunca correção silenciosa. |
| V27-REC-005 | Compensação exige comando, autorização, chave e auditoria próprios. |
| V27-REC-006 | Conclusão somente ocorre após reconciliação `PASS`. |

### 8.7 Observabilidade e auditoria

| ID | Critério de aceite arquitetural |
|---|---|
| V27-OBS-001 | Trace cobre sinal, comando, autorização, tentativa, recibo, reconciliação e terminal state. |
| V27-OBS-002 | Auditoria registra ator, cliente, política, versões, reason codes e hashes. |
| V27-OBS-003 | Logs diagnósticos não substituem auditoria e não contêm segredos. |
| V27-OBS-004 | Métricas distinguem bloqueio, cancelamento, falha sem efeito, timeout e efeito desconhecido. |
| V27-OBS-005 | Relatório TXT futuro reconcilia contagens e fingerprints sem dados sensíveis. |

### 8.8 Testabilidade e governança

| ID | Critério de aceite arquitetural |
|---|---|
| V27-QA-001 | Testes unitários cobrem policy engine, state machine, idempotência e reason codes. |
| V27-QA-002 | Testes de propriedade provam monotonicidade de limites e dominância do kill switch. |
| V27-QA-003 | Contract tests cobrem adaptador nulo/simulado, recibos e falhas. |
| V27-QA-004 | Testes concorrentes provam serialização, deduplicação e ausência de dispatch duplo. |
| V27-QA-005 | Crash/recovery tests provam ausência de reenvio automático. |
| V27-QA-006 | Scans e testes negativos provam ausência de ponteiro, teclado, clique, ordem e credenciais reais. |
| V27-QA-007 | Nenhum teste contra fonte real é permitido antes de gate e autorização próprios. |

## 9. Contratos conceituais mínimos

### 9.1 ExecutionCommand

```text
command_id
trace_id
signal_id
signal_fingerprint
idempotency_key
mode=DRY_RUN|SIMULATED
target_logical_id
action_simulated
context_snapshot_hash
policy_version
adapter_contract_version
created_at_utc
deadline_monotonic
status
```

### 9.2 AuthorizationGrant

```text
authorization_id
command_hash
actor_id
client_id
session_id
allowed_mode
policy_version
issued_at_utc
expires_at_utc
revoked_at_utc
reason_code
```

### 9.3 ExecutionAttempt

```text
attempt_id
command_id
authorization_id
idempotency_key
adapter_name
adapter_version
precondition_snapshot_hash
started_at_utc
finished_at_utc
attempt_status
reason_code
```

### 9.4 EffectReceipt

```text
receipt_id
attempt_id
adapter_name
adapter_version
result=NO_EFFECT|SIMULATED_EFFECT|UNKNOWN
result_hash
produced_at_utc
sequence
reason_code
```

### 9.5 ReconciliationResult

```text
reconciliation_id
command_id
attempt_id
receipt_id
expected_hash
observed_hash
status=PASS|DIVERGED|UNKNOWN
terminal_state
reason_codes
completed_at_utc
```

## 10. Catálogo mínimo de reason codes

```text
EXECUTION_DISABLED
REAL_MODE_UNAVAILABLE
REAL_ADAPTER_ABSENT
SIGNAL_NOT_ELIGIBLE
SIGNAL_EXPIRED
SIGNAL_INVALIDATED
COMMAND_MUTATED
COMMAND_DUPLICATE_CONFLICT
AUTHORIZATION_REQUIRED
AUTHORIZATION_EXPIRED
AUTHORIZATION_REVOKED
POLICY_CHANGED
PRECONDITION_CHANGED
TARGET_UNRESOLVED
ADAPTER_CAPABILITY_MISMATCH
LIMIT_EXCEEDED
CONCURRENCY_CONFLICT
QUEUE_CAPACITY_EXCEEDED
CIRCUIT_BREAKER_OPEN
KILL_SWITCH_ACTIVE
DEADLINE_EXCEEDED
FAILED_NO_EFFECT
EFFECT_UNKNOWN
RECEIPT_MISSING
RECEIPT_DIVERGED
RECONCILIATION_FAILED
REAL_INPUT_PROHIBITED
SENSITIVE_DATA_REJECTED
```

## 11. Persistência conceitual

Entidades candidatas:

- execution sessions e state transitions;
- execution commands e command snapshots;
- authorization grants e revocations;
- policy decisions e limit snapshots;
- deduplication records e concurrency leases;
- execution attempts e adapter receipts;
- reconciliation results e incidents;
- kill-switch events, circuit-breaker state e audit records.

```text
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PHYSICAL_SCHEMA_DEFINED=NO
```

## 12. Estratégia de falha e recovery

- falha antes do registro da tentativa: nenhum dispatch;
- falha após registro e antes da chamada: retomar como `FAILED_NO_EFFECT` somente com evidência;
- falha durante chamada: `UNKNOWN_EFFECT` até reconciliação;
- falha após recibo: reprocessar reconciliação idempotente, nunca redespachar;
- reinício com comando em estado intermediário: entrar em `SAFE_IDLE`, abrir reconciliação e bloquear correlatos;
- kill switch persistente conceitual permanece ativo após restart;
- recovery não remove auditoria nem recria autorização expirada.

## 13. Evidências futuras exigidas

- diagramas de estado validados;
- testes unitários e de propriedade;
- fixtures sanitizadas de comandos e recibos;
- testes determinísticos do adaptador nulo/simulado;
- testes de concorrência e crash/recovery;
- prova de idempotência e deduplicação;
- prova de dominância do kill switch;
- prova negativa de imports/chamadas físicas;
- scans de segredos e dados sensíveis;
- relatório TXT de reconciliação;
- revisão crítica independente.

```text
TEST_SPEC_CREATED=PASS_BUILDER
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```

## 14. Riscos residuais

| Risco | Severidade | Tratamento |
|---|---|---|
| confundir sinal com autorização | Crítico | entidades e gates separados |
| dispatch duplicado | Crítico | idempotência, dedupe e serialização |
| timeout com efeito desconhecido | Crítico | `UNKNOWN_EFFECT` e reconciliação |
| retry inseguro | Crítico | somente após prova de nenhum efeito |
| bypass por UI/Android | Crítico | servidor como autoridade e policy engine |
| coordenada tratada como autorização | Crítico | alvo lógico + geometria versionada |
| kill switch ineficaz | Crítico | dominância e testes de propriedade |
| adaptador real introduzido prematuramente | Crítico | ausência arquitetural e prova negativa |
| auditoria incompleta | Alto | cadeia correlacionada e append-only conceitual |
| persistência física prematura | Alto | existência progressiva |

## 15. Gates do builder

```text
PTM_V2_7_SCOPE_BOUNDARY=PASS_BUILDER
STRUCTURAL_REQUIREMENTS_DEFINED=32
FUNCTIONAL_REQUIREMENTS_DEFINED=52
REQUIREMENT_ID_UNIQUENESS=PASS_BUILDER
SIGNAL_EXECUTION_SEPARATION=PASS_BUILDER
SIMULATED_ONLY_BASELINE=PASS_BUILDER
EXECUTION_AUTHORIZATION_MODEL=PASS_BUILDER
FAIL_CLOSED_EXECUTION_GATES=PASS_BUILDER
IDEMPOTENCY_AND_DEDUPLICATION=PASS_BUILDER
LIMITS_AND_KILL_SWITCH=PASS_BUILDER
RECONCILIATION_AND_AUDIT=PASS_BUILDER
REAL_EFFECT_NEGATIVE_PROOF_SPECIFIED=PASS_BUILDER
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
APPLICATION_EXECUTED=NO
PTM_V2_7_DEFINITIVE=NO
PTM_V2_7_CRITICAL_REVIEW=PENDING
```

## 16. Condição de avanço

A PTM V2.7 somente poderá ser integrada e tratada como documentalmente definitiva após:

```text
BUILDER_SELF_REVIEW=PASS
TRACEABILITY_COMPLETENESS=PASS
REQUIREMENT_ID_UNIQUENESS=PASS
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS
SIMULATED_ONLY_BASELINE=PASS
INDEPENDENT_CRITICAL_REVIEW=PASS
CRITICAL_BLOCKERS=0
```

Mesmo após integração documental, implementação, adaptador real, credenciais, clique e ordem real permanecem não autorizados.