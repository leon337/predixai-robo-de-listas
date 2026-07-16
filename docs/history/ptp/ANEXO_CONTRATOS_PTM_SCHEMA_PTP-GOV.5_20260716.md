# ANEXO — CONTRATOS, PTM E SCHEMA CONCEITUAL

## PTP-GOV.5 — PredixAI Robô de Listas

Este anexo complementa o histórico integral. Seu objetivo é impedir que a continuidade dependa apenas de resumos narrativos.

---

# 1. Contratos externos conceituais

## 1.1 REST — grupos de recursos previstos

```text
/system
/health
/compatibility
/configuration
/devices
/pairing
/profiles
/calibration
/rois
/click-targets
/lists
/schedules
/observation
/analysis
/strategies
/signals
/execution
/alerts
/diagnostics
/backups
/replay
/tests
```

Princípios:

- prefixo versionado `/api/v1`;
- comandos mutáveis carregam `command_id` e idempotência;
- leitura é separada de comando;
- payload validado por schema;
- erro retorna `reason_code` estável;
- estado confirmado vem do servidor;
- endpoint futuro só entra quando possuir produtor, consumidor, requisito e teste.

## 1.2 Endpoints V2.5 preliminares citados na PTM

```text
GET  /api/v1/health
GET  /api/v1/system/state
GET  /api/v1/compatibility
GET  /api/v1/diagnostics

GET  /api/v1/lists
POST /api/v1/lists
PATCH /api/v1/lists/{id}
POST /api/v1/lists/{id}/archive
GET  /api/v1/lists/{id}/items
POST /api/v1/lists/{id}/items
PATCH /api/v1/lists/{id}/items/{item_id}

POST /api/v1/pairing/sessions
POST /api/v1/pairing/sessions/{id}/confirm
POST /api/v1/devices/{id}/refresh-token

GET  /api/v1/mobile/bootstrap
GET  /api/v1/mobile/snapshot

GET  /api/v1/profiles
POST /api/v1/profiles
PATCH /api/v1/profiles/{id}
POST /api/v1/profiles/{id}/activate

POST /api/v1/calibration/sessions
GET  /api/v1/rois
PATCH /api/v1/rois/{id}
GET  /api/v1/click-targets
PATCH /api/v1/click-targets/{id}
```

Esses endpoints são conceituais e ainda dependem da Auditoria Mestra e do Documento Mestre.

---

# 2. Eventos WebSocket conceituais

```text
server.state_changed
server.snapshot
server.degraded
server.recovered

device.paired
device.revoked
device.permission_changed

profile.activated
profile.invalidated

calibration.state_changed
roi.validation_completed
click_target.validation_completed

list.created
list.updated
list.archived

observation.state_changed
analysis.snapshot_ready
strategy.evaluated
signal.generated
signal.invalidated

execution.state_changed
execution.feedback_received
execution.reconciled

alert.created
alert.resolved
```

Regras:

- `event_schema_version` obrigatório;
- `server_instance_id` e `sequence` quando externo;
- eventos críticos saem da outbox;
- consumidores devem ser idempotentes;
- perda de replay força snapshot;
- WebSocket não substitui REST nem event bus interno.

---

# 3. Contratos dos motores A–H

## A — Market Structure Engine

**Entrada:** snapshot validado, séries estruturais e horizonte.

**Saída:** pivôs, pernas, quebras, mudanças estruturais, estado e evidências.

**Falhas:** série insuficiente, geometria instável, contexto inválido.

## B — Trend Engine

**Entrada:** estrutura, inclinações e horizontes.

**Saída:** direção, força, estabilidade, transição e evidências.

## C — Zone Engine

**Entrada:** estrutura, pivôs, densidade e contexto.

**Saída:** zonas, tipo, limites, validade, força e histórico de testes.

## D — Volatility Engine

**Entrada:** séries, deslocamentos e janelas.

**Saída:** regime, expansão/contração, estabilidade e blockers.

## E — Candle Measurement/Context Engine

**Entrada:** velas estimadas, mapeamentos e qualidade visual.

**Saída:** corpo, pavios, relações, contexto e confiança.

## F — Momentum Engine

**Entrada:** séries e movimentos estruturais.

**Saída:** direção, aceleração, divergência estrutural e qualidade.

## G — Confluence Engine

**Entrada:** resultados A–F e linhagem de evidências.

**Saída:** confluências, contradições, overlap e confidence cap.

## H — Strategy Engine

**Entrada:** snapshot, resultados A–G, blockers e estratégia versionada.

**Saída:** `STRATEGY_WAIT`, `WAIT_MORE_DATA`, `DEGRADED`, `BLOCKED` ou candidato de sinal.

Todos os motores devem declarar versão, input hash, configuration hash, evidências, reason codes, qualidade e determinismo.

---

# 4. Estratégia inicial

```text
Nome conceitual: Strategy-001
Princípio: estrutura + zona + confirmação
```

Requisitos:

- simples;
- explicável;
- sem thresholds definitivos antes de benchmark;
- independente do executor;
- candidato não equivale a sinal final;
- sinal final depende de arbitragem e validação;
- `STRATEGY_WAIT` não cria registro operacional de sinal.

---

# 5. Catálogo lógico de tabelas por domínio

## 5.1 Governança e configuração

```text
schema_migrations
app_metadata
component_versions
component_activations
feature_flags
feature_flag_dependencies
configuration_snapshots
configuration_change_log
transactional_outbox
```

## 5.2 Runtime

```text
server_instances
runtime_sessions
system_state_transitions
dependency_checks
diagnostic_snapshots
```

## 5.3 Dispositivos e segurança

```text
devices
device_identifiers
device_permissions
device_tokens
pairing_sessions
control_leases
security_audit_log
```

## 5.4 Perfis e calibração

```text
environment_profiles
application_profiles
monitor_profiles
calibration_profile_families
calibration_profiles
profile_compatibility_checks
profile_activations
calibration_sessions
rois
roi_validations
click_targets
click_target_validations
anchors
visual_signature_definitions
visual_signature_artifacts
```

## 5.5 Observação e visão

```text
observation_sessions
observation_contexts
observation_events
capture_metrics
frame_references
frame_validations
frame_validation_checks
visual_extractions
external_artifacts
```

## 5.6 Market data

```text
visual_series
visual_series_frames
visual_series_candles
candle_estimates
price_mapping_models
price_mapping_samples
time_mapping_models
time_mapping_samples
```

## 5.7 Análise

```text
analysis_snapshots
baseline_statistics
analysis_horizon_results
analysis_engine_results
market_structure_samples
swing_points
structure_legs
trend_samples
volatility_samples
candle_feature_samples
momentum_samples
confluence_results
analysis_evidence
evidence_sources
evidence_relations
analysis_eligibility_states
```

## 5.8 Estratégias e sinais

```text
strategy_definitions
strategy_engine_requirements
strategy_horizon_requirements
strategy_rule_definitions
strategy_blocker_definitions
strategy_evaluations
signal_candidates
candidate_arbitrations
candidate_arbitration_entries
signal_validations
signals
signal_invalidations
signal_state_transitions
```

## 5.9 Listas e agenda

```text
signal_lists
signal_list_versions
signal_list_items
signal_list_item_versions
schedules
schedule_versions
scheduled_items
list_execution_plans
list_execution_plan_items
```

## 5.10 Execução

```text
execution_sessions
execution_requests
execution_eligibility_checks
execution_eligibility_rules
execution_events
execution_feedback
execution_results
execution_reconciliations
execution_reconciliation_feedback
emergency_stop_events
```

## 5.11 Comandos e alertas

```text
idempotency_records
command_log
command_confirmations
command_results
alerts
alert_acknowledgements
```

## 5.12 Migração e recovery

```text
data_migration_log
data_migration_items
backup_records
restore_runs
```

## 5.13 Replay e testes

```text
replay_packages
replay_events
replay_runs
test_environments
test_cases
test_runs
test_results
test_artifact_links
performance_samples
```

O catálogo é lógico. A criação física é progressiva.

---

# 6. Entidades e campos críticos

## 6.1 Identidade comum

```text
id público ou interno
status
revision quando mutável
created_at_utc
updated_at_utc quando aplicável
last_state_changed_at_utc quando aplicável
schema_version/definition_version quando versionada
```

## 6.2 Command envelope

```text
command_id
device_id
command_type
command_schema_version
idempotency_record_id
payload_hash
requested_at_utc
received_at_utc
trace_id
risk_level
confirmation_level
status
result_code
```

## 6.3 Event envelope

```text
event_id
event_type
event_schema_version
aggregate_type
aggregate_id
sequence
trace_id
command_id
occurred_at_utc
reason_code
payload_hash
```

## 6.4 Analysis result envelope

```text
analysis_engine_result_id
analysis_snapshot_id
engine_key
engine_version
horizon
input_hash
configuration_hash
status
technical_confidence_scaled
data_quality_scaled
stability_scaled
confidence_cap_scaled
reason_code
result_json secundário
```

## 6.5 Signal candidate

```text
signal_candidate_id
strategy_evaluation_id
direction
validity_start_utc
validity_end_utc
technical_confidence_scaled
data_quality_scaled
stability_scaled
signal_fingerprint
status
```

## 6.6 Execution request

```text
execution_request_id
execution_session_id
plan_item_id
signal_id
request_type
execution_mode
target_click_id
expected_window_identity_hash
expected_profile_revision
intended_direction
intended_amount_minor
currency_code
currency_scale
intended_duration_value
intended_duration_unit
requested_at_utc
valid_from_utc
expires_at_utc
command_id
idempotency_record_id
request_hash
revision
status
```

A definição da intenção torna-se imutável após `DISPATCHED`.

---

# 7. PTM V2.5 — registros preliminares

## Estruturais

```text
PTM-V25-001 fonte única da verdade
PTM-V25-002 clientes sem acesso direto ao banco
PTM-V25-003 escritor SQLite único
PTM-V25-004 ciclo de vida do servidor
PTM-V25-005 contratos externos versionados
PTM-V25-006 transactional outbox
PTM-V25-007 listas independentes da análise
PTM-V25-008 pareamento Android Foundation
PTM-V25-009 reconexão e snapshot Android
PTM-V25-010 perfis de ambiente e aplicação
PTM-V25-011A workflow de calibração
PTM-V25-011B ROIs
PTM-V25-011C click targets
PTM-V25-011D âncoras e assinaturas
PTM-V25-012 Linux X11 Foundation
PTM-V25-013 Windows Foundation
PTM-V25-014A inventário do legado
PTM-V25-014B backup pré-migração
PTM-V25-014C migração de dados
PTM-V25-014D reconciliação
PTM-V25-014E rollback
PTM-V25-015A logs estruturados
PTM-V25-015B auditoria
PTM-V25-015C métricas básicas
PTM-V25-015D diagnóstico exportável
PTM-V25-015E trace/command correlation
PTM-V25-016 configuração versionada e segura
PTM-V25-017 segurança da rede local
PTM-V25-018 estado seguro sem Android
```

## Funcionais iniciados

```text
V25-SRV-001 inicialização segura
V25-SRV-002 encerramento limpo
V25-SRV-003 SAFE_IDLE sem Android
V25-SRV-004 REST/WebSocket básicos

V25-CFG-001 resolução de configuração
V25-CFG-002 validação
V25-CFG-003 redação de segredos
V25-CFG-004 feature flags seguras

V25-DB-001 inicialização SQLite
V25-DB-002 escritor único
V25-DB-003 migrations versionadas
V25-DB-004 outbox
V25-DB-005 backup/restore básico

V25-LIST-001 CRUD sem análise
V25-LIST-002 itens versionados
V25-LIST-003 validação de itens
V25-LIST-004 importação V2.4.3

V25-LEG-001 inventário físico
V25-LEG-002 manifesto legado
V25-LEG-003 backup pré-migração
V25-LEG-004 transformação
V25-LEG-005 reconciliação
V25-LEG-006 rollback
```

Todos permanecem preliminares até reconciliação com a Auditoria Mestra.

---

# 8. Gates citados

```text
SERVER_SOURCE_OF_TRUTH
NO_CLIENT_DIRECT_DATABASE_ACCESS
SQLITE_SINGLE_WRITER
SERVER_LIFECYCLE
CONTRACT_VERSIONING
TRANSACTIONAL_OUTBOX
LISTS_DOMAIN_INDEPENDENT
ANDROID_FOUNDATION
ANDROID_RECONNECTION
PROFILE_FOUNDATION
CALIBRATION_FOUNDATION
LINUX_X11_FOUNDATION
WINDOWS_FOUNDATION
V2_4_3_COMPATIBILITY
OBSERVABILITY_MINIMUM
CONFIGURATION_FOUNDATION
LOCAL_NETWORK_SECURITY
SERVER_SAFE_WITHOUT_CLIENT
MIGRATIONS_FOUNDATION
BACKUP_RESTORE_BASIC
LEGACY_LIST_IMPORT
LEGACY_RECONCILIATION
LEGACY_ROLLBACK_AVAILABLE
```

---

# 9. Políticas transversais

## 9.1 Persistência

```text
NORMAL
DIAGNOSTIC
REPLAY_RECORDING
TEST
MINIMAL_SAFE
```

## 9.2 Imutabilidade

Imutáveis após ativação/aprovação/conclusão:

- versões de configuração;
- calibração aprovada;
- snapshots;
- planos aprovados;
- intenção despachada;
- resultados concluídos;
- eventos append-only;
- migrations publicadas;
- pacotes de replay prontos;
- casos de teste publicados.

## 9.3 Retenção

- crítica: longa ou permanente;
- diagnóstica: curta;
- replay: autorizada e versionada;
- métricas: amostradas;
- artefatos: hash, privacidade, expiração e catálogo.

## 9.4 Fail-closed

Dúvida sobre janela, perfil, lease, assinatura, alvo, duplicidade ou emergência resulta em `WAIT`, `BLOCKED` ou rejeição. Nunca em elevação silenciosa de modo.

---

# 10. Dependência de continuidade

```text
Auditoria Mestra
→ Anexo A real
→ PTM V2.5 reconciliada
→ revisão crítica V2.5
→ PTM V2.6
→ PTM V2.7
→ consolidação cruzada
→ ADRs
→ Documento Mestre
→ revisão
→ arquitetura congelada
→ implementação
```

Este anexo não autoriza avanço fora dessa sequência.