# ADR-0018 — Estratégia de testes e evidência por camada

## Controle

```text
ADR_ID=ADR-0018
CANDIDATE_ID=ADR-CAND-018
PRIORITY=P1
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
TEST_CODE_CHANGE_AUTHORIZED=NO
DEPENDS_ON=ADR-0003|ADR-0008|ADR-0009|ADR-0010|ADR-0011|ADR-0012|ADR-0013|ADR-0014|ADR-0015|ADR-0016|ADR-0017
```

## Contexto

A arquitetura possui contratos de persistência, captura, análise, execução controlada, recovery e segurança. Especificação de teste, simulação, CI e execução runtime são evidências diferentes e não podem ser confundidas. O projeto precisa de uma estratégia única para provar comportamento positivo e ausência de bypass.

## Decisão

Adotar uma **matriz de testes por camada e risco**, com evidência reproduzível vinculada ao commit, ambiente, comando, resultado e artefatos.

Camadas:

```text
L1_UNIT=pure rules, reason codes, fingerprints e transições
L2_PROPERTY=invariantes, caps, idempotência e geração de casos
L3_CONTRACT=schemas, REST, eventos, adapters e compatibilidade
L4_REPLAY=fixtures sanitizadas, relógio controlado e determinismo
L5_INTEGRATION=persistência, outbox, migrations em sandbox e recovery
L6_E2E_CONTROLLED=aplicação própria, sandbox ou alvo allowlisted
L7_CRASH_RECOVERY=restart, timeout, lock, fila, circuito e reconciliação
L8_SECURITY_NEGATIVE=segredos, bypass, alvo inválido e LIVE sem gates
L9_BENCHMARK=hardware-alvo, thresholds e limites
L10_LIVE_GATE=futura missão separada; não autorizada por este ADR
```

## Contrato de evidência

Cada execução válida registra:

```text
test_id
test_version
requirement_ids
adr_ids
exact_commit_sha
environment_fingerprint
hardware_fingerprint
configuration_hash
fixture_or_dataset_hash
command_or_runner_version
started_at_utc
finished_at_utc
runtime_executed
result=PASS|FAIL|BLOCKED|NOT_EXECUTED
artifact_refs_and_hashes
redaction_status
reviewer_or_automation_identity
```

```text
TEST_SPEC_CREATED!=TEST_RUNTIME_EXECUTED
CI_GREEN!=ALL_RUNTIME_GATES_PASS
SIMULATED_RESULT!=CONTROLLED_UI_RESULT
CONTROLLED_UI_RESULT!=LIVE_FINANCIAL_RESULT
```

## Gates por risco

- migration/cutover: L1, L2, L3, L5 e restore reproduzível;
- captura persistente: L1, L3, L4, L6 controlado, privacidade e redaction;
- executor: L1 a L8, incluindo concorrência e crash/restart;
- thresholds aprovados: L4 e L9 com escopo identificado;
- Modo B: L10 em missão própria, após gates comerciais, legais e de conformidade.

## Regras normativas

```text
REQUIREMENT_WITHOUT_TEST_BINDING=NOT_IMPLEMENTATION_READY
TEST_WITHOUT_EXACT_COMMIT=INVALID_EVIDENCE
TEST_WITHOUT_ENVIRONMENT_FINGERPRINT=INCOMPLETE_EVIDENCE
ARTIFACT_WITHOUT_HASH=INCOMPLETE_EVIDENCE
RUNTIME_NOT_EXECUTED=CANNOT_DECLARE_RUNTIME_PASS
FAILED_OR_BLOCKED_TEST=CANNOT_BE_OVERRIDDEN_BY_SUMMARY_SCORE
NEGATIVE_TESTS=MANDATORY_FOR_SECURITY_BOUNDARIES
CRASH_RESTART_TESTS=MANDATORY_FOR_EFFECT_CAPABLE_EXECUTOR
REAL_SECRET_IN_FIXTURE=PROHIBITED
UNSANITIZED_PRODUCTION_IMAGE_IN_FIXTURE=PROHIBITED
EXTERNAL_UNAUTHORIZED_TARGET=PROHIBITED
LIVE_FINANCIAL_TEST=SEPARATE_GATE_AND_MISSION
TEST_REPORT_TXT=REQUIRED_WHEN_EXECUTED_BY_LOCAL_RUNNER
```

## Provas negativas mínimas

```text
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCK
SIGNAL_AUTO_EXECUTION=BLOCK
UNAUTHORIZED_TARGET=BLOCK
ADAPTER_BYPASS=BLOCK
PRODUCTION_SECRET_IN_GIT_OR_LOG=BLOCK
CONTROLLED_UI_TO_UNGATED_LIVE_EFFECT=BLOCK
RESTART_REDISPATCH=BLOCK
TIMEOUT_AUTOMATIC_RETRY=BLOCK
UNKNOWN_EFFECT_AUTOMATIC_RETRY=BLOCK
DIVERGENT_IDEMPOTENCY_REUSE=BLOCK
CLOCK_ROLLBACK_EXTENDS_VALIDITY=BLOCK
THRESHOLD_OVERRIDES_BLOCKER=BLOCK
```

## Alternativas consideradas

### Apenas testes E2E

Rejeitada porque falhas ficam difíceis de localizar e casos de propriedade, contrato e recovery não são cobertos adequadamente.

### Apenas CI e testes unitários

Rejeitada porque não prova integração, crash/restart, UI controlada ou hardware-alvo.

### Evidência manual sem hashes

Rejeitada porque não garante identidade do commit, ambiente ou artefato.

### Testar diretamente em ambiente financeiro real

Rejeitada para o estado atual; Modo B exige missão e gates separados.

## Consequências

### Positivas

- evidência reproduzível e auditável;
- distinção clara entre especificação e runtime;
- cobertura explícita de falha segura;
- thresholds vinculados a benchmark;
- revisão pode localizar a camada ausente.

### Negativas e custos

- maior volume de fixtures e relatórios;
- testes de recovery e E2E são mais caros;
- hardware e ambiente precisam ser identificados;
- nenhum GO pode ser inferido apenas por CI verde.

## Segurança, recovery e falha segura

```text
FIXTURE_SENSITIVITY_UNKNOWN=BLOCK
REDACTION_FAILED=BLOCK_ARTIFACT_PUBLICATION
TARGET_NOT_ALLOWLISTED=BLOCK_E2E
KILL_SWITCH_UNAVAILABLE=BLOCK_EFFECT_CAPABLE_E2E
TEST_PROCESS_CRASH=RESULT_BLOCKED_OR_FAIL_WITH_ARTIFACTS
PARTIAL_EVIDENCE=DO_NOT_PROMOTE_GATE
EVIDENCE_TAMPER_OR_HASH_MISMATCH=INVALIDATE_RESULT
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-16
SECONDARY_DOMAINS=DOM-03|DOM-08|DOM-09|DOM-11|DOM-13|DOM-14|DOM-15
HANDOFFS=H-04|H-05|H-07|H-09|H-10|H-11|H-12
REQUIREMENTS=V25-QA-001..002|V25-SEC-001|PTM-V26-024..028|V26-RPL-001..003|V26-API-001..002|V26-SEC-001..003|PTM-V27-010..019|PTM-V27-026..032|V27-EXE-001..008|V27-SAF-001..008|V27-REC-001..006|V27-OBS-001..005|V27-QA-001..007
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
```

## Critérios de aceitação

```text
TEST_LAYER_MODEL=PASS_BUILDER
EVIDENCE_CONTRACT=PASS_BUILDER
SPEC_RUNTIME_SEPARATION=PASS_BUILDER
NEGATIVE_TEST_CATALOG=PASS_BUILDER
CRASH_RECOVERY_REQUIRED=PASS_BUILDER
BENCHMARK_LAYER_REQUIRED=PASS_BUILDER
LIVE_GATE_SEPARATED=PASS_BUILDER
TEST_SPEC_CREATED=PASS_BUILDER
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```

## Fora de escopo

- código de teste;
- execução de testes;
- ferramentas específicas;
- credenciais ou ambiente de produção;
- gate LIVE.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW` até `LEA-31=PASS`, autorização humana de merge e confirmação pós-merge.