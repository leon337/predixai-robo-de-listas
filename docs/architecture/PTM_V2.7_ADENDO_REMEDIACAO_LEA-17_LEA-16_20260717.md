# PTM V2.7 — ADENDO NORMATIVO DE REMEDIAÇÃO

## LEA-16 após revisão crítica LEA-17

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_REMEDIATION_READY_FOR_RETEST
MISSION=LEA-16
REVIEW_ISSUE=LEA-17
PARENT_DOCUMENT=docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md
TRACEABILITY_MATRIX=docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md
REVIEW_REPORT=docs/history/reviews/REVISAO_CRITICA_PTM_V2.7_LEA-17_20260717.md
BASE_MAIN_SHA=f3c84d97523c1c631392cefb69b6cb3e8f6a56e2
REMEDIATION_BASE_PR_HEAD=750e4d4916c9aef07838a935bf62c5a26472d4e1
EXECUTION_CAPABILITY_BASELINE=SIMULATED_ONLY
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
WORKFLOWS_CHANGED=NO
APPLICATION_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
REAL_EFFECT_EXECUTED=NO
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
INDEPENDENT_RETEST_REQUIRED=YES
```

Este adendo é normativo para a PTM V2.7 e prevalece sobre os trechos explicitamente substituídos abaixo. Ele não modifica o escopo simulado, não autoriza implementação e não cria integração, credencial, clique, entrada de teclado, ordem ou efeito real.

## 2. Precedência

```text
PRECEDENCE_ORDER=
  THIS_REMEDIATION_ADDENDUM
  > PTM_V2.7_PARENT_DOCUMENT_FOR_SUPERSEDED_CLAUSES
  > BUILDER_SELF_REVIEW
```

O relatório da LEA-17 permanece histórico e imutável. Este adendo registra a resposta do builder; somente novo reteste independente pode alterar o gate final.

## 3. MAJOR-02 — prazo estável após reinício

### 3.1 Substituição de PTM-V27-014

A redação anterior de `PTM-V27-014` é substituída por:

> Prazo persistido combina expiração UTC estável, duração original e identidade da fonte temporal. Relógio monotônico é usado apenas como orçamento local ao processo. Reinício, mudança de boot, rollback de relógio, skew acima da tolerância ou ausência de evidência resultam em bloqueio ou expiração fail-closed, nunca rearmamento automático.

Gate substituto:

```text
RESTART_STABLE_DEADLINE
```

### 3.2 Contrato revisado de ExecutionCommand

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
expires_at_utc
ttl_ms
clock_source_id
boot_id_at_creation
deadline_monotonic_process_local
status
```

Semântica:

- `expires_at_utc` é a representação persistida e auditável da expiração;
- `ttl_ms` preserva a duração original usada para validação e diagnóstico;
- `clock_source_id` identifica a fonte temporal confiável e sua versão;
- `boot_id_at_creation` permite detectar mudança de boot ou ambiente;
- `deadline_monotonic_process_local` é efêmero, recalculado apenas durante o mesmo processo e nunca é autoridade após restart;
- nenhuma divergência entre UTC, duração, boot ou fonte temporal pode ampliar validade.

### 3.3 Política fail-closed de relógio e recovery

```text
SAME_PROCESS_VALID_CLOCK=USE_MONOTONIC_BUDGET
RESTART_WITH_VALID_UTC_AND_UNEXPIRED_COMMAND=BLOCK_AND_REQUIRE_REVALIDATION
RESTART_WITH_EXPIRED_COMMAND=EXPIRE
BOOT_ID_CHANGED=BLOCK_AND_REQUIRE_REVALIDATION
CLOCK_ROLLBACK_DETECTED=BLOCK
CLOCK_SKEW_ABOVE_POLICY=BLOCK
CLOCK_SOURCE_UNKNOWN=BLOCK
EXPIRATION_EVIDENCE_INSUFFICIENT=BLOCK
AUTOMATIC_REARM_AFTER_RESTART=NO
AUTOMATIC_REDISPATCH_AFTER_RESTART=NO
```

Um comando persistido em estado intermediário entra em `SAFE_IDLE` e reconciliação. Mesmo ainda não expirado, ele não retorna diretamente a `ARMED_SIMULATED`; exige novo snapshot de pré-condições e nova autorização humana quando aplicável.

Reason codes mínimos adicionais:

```text
CLOCK_SOURCE_UNKNOWN
CLOCK_SKEW_DETECTED
CLOCK_ROLLBACK_DETECTED
BOOT_ID_CHANGED
EXPIRATION_AMBIGUOUS
RESTART_REVALIDATION_REQUIRED
```

Evidência futura:

- testes com restart no mesmo boot e em boot diferente;
- testes de avanço, atraso e rollback de relógio;
- testes de expiração exatamente no limite;
- prova de ausência de rearmamento e redespacho automáticos;
- reconciliação entre `created_at_utc`, `expires_at_utc`, `ttl_ms` e auditoria.

```text
RESTART_STABLE_DEADLINE_CONTRACT=PASS_BUILDER_REMEDIATED
CLOCK_SKEW_FAIL_CLOSED_POLICY=PASS_BUILDER_REMEDIATED
RUNTIME_VALIDATION=NOT_EXECUTED
```

## 4. MAJOR-03 — classificação de command_id

A linha `PTM-V27-004` da matriz deve ser interpretada e registrada como:

```text
command_id=ADAPTAR_FROM_V2_5
EXECUTION_COMMAND_AGGREGATE=NOVO_IN_V2_7
VERSIONED_SIGNAL_REFERENCE=ADAPTAR_FROM_V2_6
```

A V2.5 já introduziu `trace_id` e `command_id` como correlação transversal. A V2.7 adapta esse identificador para o agregado imutável `ExecutionCommand`; somente o agregado e seu lifecycle são novos.

```text
PTM_V27_004_SOURCE_ALIGNMENT=PASS_BUILDER_REMEDIATED
LEGACY_CLASSIFICATION_CONSISTENCY=PASS_BUILDER_REMEDIATED
```

## 5. MAJOR-04 — separação da prova negativa

### 5.1 Gates separados

```text
REAL_EFFECT_NEGATIVE_PROOF_SPECIFICATION=PASS_BUILDER_REMEDIATED
REAL_EFFECT_NEGATIVE_PROOF_RUNTIME=NOT_EXECUTED
RUNTIME_CLAIM_ACCURACY=PASS_BUILDER_REMEDIATED
```

A especificação documental não equivale a prova runtime. O merge documental da PTM V2.7 pode exigir a especificação aprovada, mas não pode declarar teste runtime executado enquanto não existir implementação autorizada.

### 5.2 Escopo normativo futuro

```text
NEGATIVE_PROOF_INCLUDED_SCOPE=
  FUTURE_V2_7_EXECUTION_DOMAIN_MODULES
  FUTURE_NULL_AND_SIMULATED_ADAPTERS
  FUTURE_EXECUTION_ROUTES_EVENTS_AND_HANDLERS
  IMPORT_BOUNDARIES_FROM_V2_7_TO_LEGACY
  DEPENDENCY_MANIFESTS_AND_BUILD_ARTIFACTS

NEGATIVE_PROOF_EXCLUDED_AS_EXECUTION_TARGET=
  LEGACY_V2_4_3_R1_SOURCE_PRESERVED_AS_AUDIT_EVIDENCE
```

O legado conhecido pode continuar contendo `pynput` e caminhos de clique como evidência histórica. A prova deve falhar se qualquer módulo V2.7 importar, chamar, encapsular, alcançar por dispatch ou reativar esses caminhos.

### 5.3 Camadas de evidência futura

1. scan AST e de imports nos módulos V2.7;
2. grafo de dependências provando ausência de caminho V2.7 → executor legado;
3. contract tests dos adaptadores `NULL` e `SIMULATED`;
4. testes negativos de payload, endpoint e evento;
5. scan de credenciais, cookies, tokens e APIs de ordem;
6. teste runtime negativo apenas em ambiente autorizado e sem fonte externa real;
7. relatório TXT com escopo, exclusões justificadas, hashes e resultado.

```text
NEGATIVE_PROOF_GATE_SEPARATION=PASS_BUILDER_REMEDIATED
NEGATIVE_PROOF_SCOPE_DEFINED=PASS_BUILDER_REMEDIATED
LEGACY_CLICK_PATHS_REMAIN_DESCONTINUED=PASS
```

## 6. Requisitos funcionais afetados

As seguintes interpretações normativas substituem ou complementam os critérios anteriores sem criar novos IDs:

| ID | Critério remediado |
|---|---|
| `V27-PRE-002` | Validar fonte temporal, identidade de boot e política de skew antes de sair de `DISABLED`/`SAFE_IDLE`. |
| `V27-CMD-002` | Comando inclui `expires_at_utc`, `ttl_ms`, `clock_source_id` e `boot_id_at_creation`; prazo monotônico é apenas local ao processo. |
| `V27-EXE-005` | Timeout, restart ou ambiguidade temporal levam a `TIMED_OUT`, `BLOCKED` ou `UNKNOWN_EFFECT`; nunca a sucesso, retry ou rearmamento presumidos. |
| `V27-SAF-004` | A proibição é aplicada aos módulos e fronteiras V2.7; o legado é evidência excluída como alvo, mas qualquer dependência V2.7 → clique legado falha o gate. |
| `V27-SAF-008` | Falha de fonte temporal, boot, skew, sequência ou assinatura bloqueia antes do arming. |
| `V27-QA-005` | Crash/recovery cobre expiração estável, boot diferente, clock skew e ausência de reenvio/rearmamento. |
| `V27-QA-006` | A especificação documental define scans e testes; resultado runtime permanece `NOT_EXECUTED` até implementação autorizada. |

## 7. Estado da remediação

```text
MAJOR_01_SCHEMA_ENUMS=REMEDIATED_PREVIOUSLY
MAJOR_02_RESTART_STABLE_DEADLINE=REMEDIATED_BUILDER
MAJOR_03_COMMAND_ID_CLASSIFICATION=REMEDIATED_BUILDER
MAJOR_04_NEGATIVE_PROOF_GATE=REMEDIATED_BUILDER
OPEN_CRITICAL_FINDINGS_BUILDER_VIEW=0
OPEN_MAJOR_FINDINGS_BUILDER_VIEW=0
RETEST_REQUIRED=YES
DOCUMENTAL_READY_FOR_INDEPENDENT_RETEST=YES
DOCUMENTAL_READY_FOR_MERGE=NO
PTM_V2_7_DEFINITIVE=NO
```

## 8. Condição de avanço

```text
INDEPENDENT_CRITICAL_RETEST=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
REQUIREMENT_ID_UNIQUENESS=PASS
TRACEABILITY_COMPLETENESS=PASS
LEGACY_CLASSIFICATION_CONSISTENCY=PASS
RESTART_STABLE_DEADLINE_CONTRACT=PASS
NEGATIVE_PROOF_GATE_SEPARATION=PASS
SIMULATED_ONLY_BASELINE=PASS
LEO_MERGE_AUTHORIZATION=REQUIRED
```

Até esse gate, o PR permanece sem merge e nenhuma etapa de consolidação cruzada pode iniciar.