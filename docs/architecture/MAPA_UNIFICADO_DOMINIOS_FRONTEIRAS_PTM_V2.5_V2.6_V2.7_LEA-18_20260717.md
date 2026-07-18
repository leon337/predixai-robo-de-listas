# MAPA UNIFICADO DE DOMÍNIOS E FRONTEIRAS

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DOMAIN_BOUNDARY_MAP_REMEDIATED_FOR_RETEST_04
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASELINE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
CURRENT_MAIN_OBSERVED=236bc5df7f675ca5cf56d80c5812bd911d224651
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
IMPLEMENTATION_AUTHORIZED=NO
POLICY_A_B_ALIGNMENT=PASS_BUILDER
```

Os identificadores `DOM-*` e `H-*` são internos deste mapa e não criam novos requisitos PTM.

## 2. Objetivo

Definir uma cadeia única de autoridade para impedir:

- acoplamento oculto entre análise e execução;
- transformação automática de sinal em ação;
- uso de coordenada como autorização;
- promoção de recibo local a verdade global;
- confusão entre ação de interface, autorização LIVE e resultado financeiro;
- escrita por cliente diretamente na persistência;
- expansão automática de capacidade em situação desconhecida.

## 3. Invariantes transversais

```text
SERVER_STATE=GLOBAL_AUTHORITY
CLIENT_STATE=LOCAL_VIEW_NOT_GLOBAL_AUTHORITY
EXTERNAL_VISUAL_SOURCE=EVIDENCE_NOT_INTERNAL_AUTHORITY
FRAME_INVALID=ANALYSIS_BLOCKED
CANDIDATE!=SIGNAL
SIGNAL!=EXECUTION_COMMAND
EXECUTION_COMMAND!=AUTHORIZATION_GRANT
AUTHORIZATION_GRANT!=DISPATCH_ATTEMPT
DISPATCH_ATTEMPT!=CONFIRMED_EFFECT
ADAPTER_RECEIPT!=GLOBAL_TRUTH
COORDINATE!=TARGET_AUTHORIZATION
CONTROLLED_UI_ACTION!=LIVE_FINANCIAL_AUTHORIZATION
MODE_A_CONTROLLED_AUTOMATION=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_WITHOUT_ALL_GATES=BLOCKED
UNKNOWN_DATA=CAPABILITY_REDUCTION
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
```

## 4. Cadeia arquitetural

```text
DOM-01 GOVERNANÇA E ESTADO
→ DOM-02 CONFIGURAÇÃO, IDENTIDADE E SEGREDOS
→ DOM-03 PERSISTÊNCIA, EVENTOS E RECOVERY
→ DOM-04 LISTAS E AGENDAMENTOS
→ DOM-05 CLIENTES, DISPOSITIVOS E PRESENÇA HUMANA
→ DOM-06 PERFIS, CALIBRAÇÃO, ROIS E GEOMETRIA
→ DOM-07 SESSÃO DE OBSERVAÇÃO
→ DOM-08 CAPTURA, FRAME E PROVENIÊNCIA
→ DOM-09 VALIDAÇÃO E QUALIDADE
→ DOM-10 EXTRAÇÃO E DADOS ESTIMADOS
→ DOM-11 ANÁLISE A–H
→ DOM-12 ESTRATÉGIA, CANDIDATO E SINAL
→ DOM-13 COMANDO, AUTORIZAÇÃO E POLICY ENGINE
→ DOM-14 ALVO LÓGICO E ADAPTADORES
→ DOM-15 DISPATCH, RECIBO, RECONCILIAÇÃO E RECOVERY
→ DOM-16 SEGURANÇA, AUDITORIA, OBSERVABILIDADE E CONTENÇÃO
```

## 5. Domínios canônicos

### DOM-01 — Governança e estado operacional

```text
PRIMARY_OWNER=GOVERNANCE
PTM_ORIGIN=TRANSVERSAL
AUTHORITY=PROJECT_RUNTIME_STATE.yaml
INPUTS=GitHub_main|active_PR|Linear|PROJECT_STATE|trunk
OUTPUTS=state_revision|transition_id|mission|gate|blockers|next_action
STATES=STATE_STABLE|TRANSITION_IN_PROGRESS|SYNC_PARTIAL|STATE_CONFLICT|BLOCKED
```

Responsabilidades:

- controlar missão, gate, continuidade e sincronização;
- distinguir `main` de trabalho não integrado;
- aplicar a política A+B como autoridade transversal;
- impedir escrita com snapshot obsoleto.

Não pode:

- declarar merge futuro como fato;
- tratar lock consultivo como garantia técnica;
- armar Modo B sem decisão e gates aplicáveis.

### DOM-02 — Configuração, identidade e segredos

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=SERVER_RESOLVED_VERSIONED_CONFIGURATION
INPUTS=safe_defaults|authorized_config|explicit_overrides|environment_identity
OUTPUTS=config_snapshot|feature_capabilities|reason_codes|redacted_diagnostics
STATES=UNRESOLVED|VALID|INVALID|BLOCKED
```

Responsabilidades:

- resolver configuração de forma determinística;
- manter segredos fora do Git;
- declarar modo, alvo, allowlists e capacidades;
- impedir elevação silenciosa de Modo A para Modo B.

Não pode:

- publicar token, cookie, chave privada ou credencial;
- armar Modo B por feature flag isolada;
- substituir autorização de sessão.

### DOM-03 — Persistência, eventos, backup e recovery

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=SERVER_SINGLE_WRITE_BOUNDARY
INPUTS=validated_domain_commands|migration_inputs|audit_intents
OUTPUTS=committed_state|versioned_records|outbox_events|backup_catalog|recovery_result
STATES=READY|WRITING|COMMITTED|RECOVERING|DEGRADED|BLOCKED
```

Responsabilidades:

- centralizar escrita;
- preservar origem bruta do legado;
- fornecer backup, restauração, reconciliação e rollback;
- manter persistência progressiva por fluxo vertical.

Não pode:

- permitir escrita direta por cliente ou handler;
- criar schema físico sem requisito e teste;
- tratar JSON legado como autoridade final.

### DOM-04 — Listas, itens e agendamentos

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=LISTS_DOMAIN_ON_SERVER
INPUTS=validated_list_commands|schedule_definitions|operator_identity
OUTPUTS=list_revision|item_revision|schedule_context|validation_reason_codes
STATES=DRAFT|PUBLISHED|ACTIVE|ARCHIVED|INVALID
```

Responsabilidades:

- manter listas independentes de observação, análise e execução;
- versionar revisões;
- fornecer contexto de intenção e agenda.

Não pode:

- produzir sinal por conta própria;
- chamar adaptador;
- transformar item de lista em autorização.

### DOM-05 — Clientes, dispositivos e presença humana

```text
PRIMARY_OWNER=PTM_V2.5_FOUNDATION_WITH_V2.7_AUTHORIZATION_USE
AUTHORITY=SERVER_FOR_GLOBAL_STATE
INPUTS=pairing_request|device_identity|operator_presence|revocation_state
OUTPUTS=paired_device|client_session|local_snapshot|human_confirmation
STATES=UNPAIRED|PAIRING|PAIRED|REVOKED|DISCONNECTED|STALE
```

Responsabilidades:

- suportar pareamento local e revogável;
- fornecer presença e confirmação humana;
- usar sequence e snapshot para reconexão.

Não pode:

- tornar cliente autoridade global;
- transformar presença em grant implícito;
- rearmar execução após desconexão.

### DOM-06 — Perfis, calibração, ROIs e geometria

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=APPROVED_VERSIONED_PROFILE_AND_GEOMETRY
INPUTS=application_identity|monitor|resolution|scale|anchors|coordinate_capture
OUTPUTS=profile_version|roi_version|target_geometry|compatibility_result
STATES=DRAFT|VALIDATING|APPROVED|ACTIVE|INCOMPATIBLE|REVOKED
```

Responsabilidades:

- versionar aplicação, monitor, ROIs, âncoras e alvos;
- permitir captura de coordenadas no Modo A;
- fornecer geometria para observação e resolução de alvo.

Não pode:

- transformar coordenada em autorização;
- manter compatibilidade após mudança não validada;
- despachar ação.

### DOM-07 — Sessão de observação

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=OBSERVATION_SESSION_STATE_ON_SERVER
INPUTS=active_profile|authorized_application|monitor|rois|resolved_config
OUTPUTS=observation_session|eligibility_state|session_reason_codes
STATES=CREATED|VALIDATING|ACTIVE|DEGRADED|BLOCKED|CLOSED
```

Responsabilidades:

- vincular observação a sessão identificada;
- validar fonte visual;
- degradar quando identidade ou estabilidade forem perdidas.

Não pode:

- selecionar janela desconhecida;
- produzir comando ou autorização;
- chamar adaptador por responsabilidade própria.

### DOM-08 — Captura, frame e proveniência

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=FRAME_REFERENCE_WITH_PROVENANCE
INPUTS=authorized_visual_source|observation_session|capture_policy
OUTPUTS=frame_reference|frame_hash|roi_crops|sequence|retention_decision
STATES=CAPTURED|DUPLICATE|STALE|OUT_OF_ORDER|REJECTED|ELIGIBLE_FOR_VALIDATION
```

Responsabilidades:

- capturar tela e recortes autorizados;
- registrar hash, origem, timestamps e sequência;
- minimizar retenção sensível.

Não pode:

- declarar frame válido antes do DOM-09;
- usar captura como autorização;
- persistir conteúdo bruto indefinidamente por padrão.

### DOM-09 — Validação visual e qualidade

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=VALIDATION_AND_QUALITY_RESULT
INPUTS=frame_reference|profile_version|roi_version|visual_signature
OUTPUTS=check_results|blockers|confidence_caps|frame_eligibility
STATES=PASS|DEGRADED|FAIL|UNKNOWN
```

Responsabilidades:

- validar identidade, geometria, frescor, completude e estabilidade;
- aplicar caps monotônicos;
- bloquear frames inelegíveis.

Não pode:

- tratar `UNKNOWN` como aprovação;
- substituir benchmark por threshold arbitrário;
- produzir sinal ou ação.

### DOM-10 — Extração visual e dados estimados

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=VERSIONED_EXTRACTION_RESULT
INPUTS=eligible_frame|roi|extractor_version|mapping_version
OUTPUTS=visual_features|estimated_series|estimated_candles|uncertainty|lineage
STATES=EXTRACTED|PARTIAL|DEGRADED|FAILED|INVALIDATED
```

Responsabilidades:

- executar OCR e extração autorizados;
- declarar incerteza e linhagem;
- diferenciar dado estimado de dado oficial.

Não pode:

- ocultar lacunas;
- declarar candle estimado como dado oficial;
- chamar adaptador por responsabilidade própria.

### DOM-11 — Análise A–H

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=IMMUTABLE_ANALYSIS_SNAPSHOT_AND_ENGINE_RESULTS
INPUTS=eligible_estimated_data|strategy_context|engine_versions|config_snapshot
OUTPUTS=structure|trend|zones|volatility|candle_context|momentum|confluence|strategy_evaluation
STATES=READY|WAIT_MORE_DATA|DEGRADED|BLOCKED|COMPLETE
```

Responsabilidades:

- executar motores A–H;
- preservar evidências, contradições e versões;
- produzir resultado determinístico ou divergência explicada.

Não pode:

- manter estado oculto;
- chamar adaptador;
- criar autorização ou comando.

### DOM-12 — Estratégia, candidatos e sinais

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=VERSIONED_STRATEGY_AND_SIGNAL_LIFECYCLE
INPUTS=analysis_results|quality_caps|strategy_version|schedule_context
OUTPUTS=strategy_decision|candidate_set|arbitration_result|signal
STATES=WAIT|CANDIDATE|ACTIVE|EXPIRED|INVALIDATED|SUPERSEDED|BLOCKED
```

Responsabilidades:

- aplicar estratégia versionada;
- arbitrar candidatos;
- emitir sinal com fingerprint, validade e evidências.

Não pode:

- autoexecutar sinal;
- escolher alvo de UI;
- criar grant.

### DOM-13 — Comando, autorização e policy engine

```text
PRIMARY_OWNER=PTM_V2.7
AUTHORITY=SERVER_EXECUTION_POLICY_AND_EXPLICIT_GRANT
INPUTS=eligible_signal|context_snapshot|operator_confirmation|target_identity|policy_version
OUTPUTS=immutable_command|authorization_grant|policy_decision|frozen_preconditions
STATES=DISABLED|SAFE_IDLE|VALIDATING|ARMED_DRY_RUN|ARMED_SIMULATED|ARMED_CONTROLLED_UI|ARMED_LIVE_GATED|BLOCKED|CANCELLED|KILLED
```

Responsabilidades:

- separar sinal, comando, grant e decisão;
- vincular autorização a canal, alvo, ação, allowlist, validade e ator;
- revalidar pré-condições;
- exigir todos os gates antes de `ARMED_LIVE_GATED`.

Não pode:

- criar comando sem sinal elegível;
- ampliar limites automaticamente;
- armar LIVE sem gates técnicos, comerciais, legais e de conformidade;
- tratar presença do cliente como grant.

### DOM-14 — Resolução de alvo e adaptadores

```text
PRIMARY_OWNER=PTM_V2.7
AUTHORITY=ALLOWLISTED_LOGICAL_TARGET_PLUS_ADAPTER_CAPABILITY
INPUTS=authorized_command|target_logical_id|profile_geometry|application_identity|allowlist
OUTPUTS=resolved_target|adapter_request|capability_check|dispatch_readiness
STATES=UNRESOLVED|RESOLVED|INCOMPATIBLE|UNAUTHORIZED|READY|BLOCKED
```

Responsabilidades:

- resolver alvo lógico e geometria versionada;
- expor `NULL`, `SIMULATED` e `CONTROLLED_UI`;
- suportar futuro adaptador LIVE somente por contrato e gate específicos;
- bloquear ação fora da allowlist.

Não pode:

- tratar `CONTROLLED_UI` como autorização LIVE;
- despachar por coordenada isolada;
- permitir biblioteca de UI fora da fronteira do adaptador.

### DOM-15 — Dispatch, recibo, reconciliação e recovery

```text
PRIMARY_OWNER=PTM_V2.7
AUTHORITY=RECONCILED_SERVER_STATE
INPUTS=ready_command|authorization_grant|adapter_request|kill_switch|deadlines
OUTPUTS=attempt_record|adapter_receipt|ui_result|financial_result|reconciliation_result
STATES=DISPATCHING|AWAITING_RECEIPT|RECONCILING|COMPLETED_NO_EFFECT|COMPLETED_SIMULATED|COMPLETED_CONTROLLED_UI|COMPLETED_LIVE_GATED|TIMED_OUT|UNKNOWN_EFFECT|FAILED_NO_EFFECT|KILLED
```

Responsabilidades:

- registrar intenção antes do efeito;
- aplicar idempotência, dedupe, serialização, deadline e circuit breaker;
- separar `ui_result` e `financial_result`;
- reconciliar tentativa, recibo e estado observado;
- impedir retry sem prova de ausência de efeito.

Não pode:

- considerar timeout como ausência de efeito;
- reenviar após restart;
- inferir resultado financeiro a partir de efeito de UI;
- despachar LIVE quando o gate não estiver íntegro.

### DOM-16 — Segurança, auditoria, observabilidade e contenção

```text
PRIMARY_OWNER=TRANSVERSAL_V2.5_V2.6_V2.7
AUTHORITY=SECURITY_POLICY_PLUS_APPEND_ONLY_AUDIT_CONTRACT
INPUTS=all_domain_events|trace_id|command_id|authorization_id|security_context
OUTPUTS=audit_records|structured_logs|metrics|alerts|diagnostics|kill_switch_events
STATES=HEALTHY|DEGRADED|ALERTED|CIRCUIT_OPEN|KILLED|RECOVERING
BLOCKERS=secret_detected|unauthorized_access|audit_gap|kill_switch_failure|live_without_all_gates
```

Responsabilidades:

- correlacionar a cadeia completa;
- aplicar redaction, retenção e minimização;
- prover kill switch dominante;
- demonstrar ausência de bypass e LIVE sem gates.

Provas negativas:

```text
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCK
UNCONTROLLED_UI_ACTION=BLOCK
UNAUTHORIZED_EXTERNAL_ACCESS=BLOCK
PRODUCTION_SECRET_IN_GIT=BLOCK
MODE_A_TO_UNGATED_LIVE_EFFECT=BLOCK
LIVE_WITHOUT_ALL_GATES=BLOCK
PRE_RESTART_COMMAND_REDISPATCH=BLOCK
TARGET_NOT_ALLOWLISTED=BLOCK
```

## 6. Handoffs obrigatórios

| ID | Origem → destino | Contrato mínimo | Falha obrigatória |
|---|---|---|---|
| H-01 | DOM-04 → DOM-07 | lista/agendamento fornece contexto versionado | contexto inválido não inicia sessão |
| H-02 | DOM-06 → DOM-07 | perfil, aplicação, monitor e ROIs aprovados | incompatibilidade bloqueia observação |
| H-03 | DOM-07 → DOM-08 | sessão ativa autoriza captura da fonte identificada | fonte perdida rejeita frame |
| H-04 | DOM-08 → DOM-09 | frame possui proveniência | frame sem hash/origem é rejeitado |
| H-05 | DOM-09 → DOM-10 | somente frame elegível alimenta extração | `FAIL` impede extração |
| H-06 | DOM-10 → DOM-11 | dados estimados carregam incerteza e linhagem | mapping incompatível bloqueia snapshot |
| H-07 | DOM-11 → DOM-12 | resultados A–H e caps são imutáveis | motor H não contorna blockers |
| H-08 | DOM-12 → DOM-13 | sinal válido, elegível e não expirado | sinal não vira comando automaticamente |
| H-09 | DOM-13 → DOM-14 | comando e grant vinculam alvo, ação e canal | grant incompatível bloqueia resolução |
| H-10 | DOM-14 → DOM-15 | alvo resolvido e adaptador capaz | alvo desconhecido bloqueia dispatch |
| H-11 | DOM-15 → DOM-16 | tentativa e recibo sempre produzem auditoria | lacuna bloqueia recovery seguro |
| H-12 | DOM-16 → DOM-13/15 | kill switch, circuito e política dominam arming/dispatch | estado inseguro cancela ou mata fluxo |

## 7. Autoridades que não podem ser confundidas

| Informação | Autoridade | Não autoridade |
|---|---|---|
| estado operacional | `PROJECT_RUNTIME_STATE.yaml` | conversa ou histórico |
| trabalho não integrado | PR ativo | `main` |
| estado global do produto | servidor | cliente/cache local |
| identidade visual | sessão + perfil + validação | janela encontrada por conveniência |
| qualidade do frame | DOM-09 | OCR bruto |
| resultado analítico | snapshot + motores | executor |
| sinal | DOM-12 | lista ou adaptador |
| autorização Modo A | grant DOM-13 | sinal, coordenada ou presença |
| autorização Modo B | política A+B + todos os gates LIVE | clique controlado ou propriedade da conta |
| alvo executável | identidade lógica + allowlist | par X/Y isolado |
| efeito confirmado | reconciliação DOM-15 | recibo isolado |

## 8. Caminhos bloqueados

```text
LIST_ITEM -> DIRECT_ADAPTER_CALL                = BLOCKED_BY_BOUNDARY
ANALYSIS_ENGINE -> UI_ADAPTER                   = BLOCKED_BY_BOUNDARY
SIGNAL -> AUTO_EXECUTION                        = BLOCKED_BY_BOUNDARY
COORDINATE -> AUTHORIZATION                     = BLOCKED_BY_BOUNDARY
CLIENT_CACHE -> GLOBAL_STATE_CONFIRMATION       = BLOCKED_BY_BOUNDARY
ADAPTER_RECEIPT -> GLOBAL_TRUTH                 = BLOCKED_BY_BOUNDARY
TIMEOUT -> ASSUME_NO_EFFECT                     = BLOCKED_BY_BOUNDARY
UNKNOWN_EFFECT -> AUTOMATIC_RETRY               = BLOCKED_BY_BOUNDARY
CONTROLLED_UI_ALONE -> LIVE_AUTHORIZATION       = BLOCKED_BY_LIVE_GATE
LIVE_WITHOUT_ALL_GATES -> DISPATCH              = BLOCKED_BY_LIVE_GATE
RESTART -> REARM_OLD_COMMAND                    = BLOCKED_BY_RECOVERY_POLICY
```

## 9. Decisões candidatas a ADR

1. topologia e autoridade do servidor;
2. fronteira de escritor único;
3. contratos REST/eventos;
4. pareamento e identidade;
5. perfil, ROI, alvo lógico e compatibilidade;
6. retenção de frames;
7. motores A–H e estratégia;
8. máquina de estados;
9. adaptadores Modo A e Modo B gated;
10. kill switch e circuit breaker;
11. idempotência, dedupe e serialização;
12. recibo e reconciliação;
13. taxonomia de `target_logical_id`;
14. observabilidade e redaction;
15. gate LIVE completo.

## 10. Resultado do builder — G3

```text
CANONICAL_DOMAIN_COUNT=16
MANDATORY_HANDOFF_COUNT=12
CROSS_CUTTING_INVARIANTS_DEFINED=PASS
DOMAIN_AUTHORITY_DEFINED=PASS
DOMAIN_INPUT_OUTPUT_DEFINED=PASS
DOMAIN_STATES_DEFINED=PASS
DOMAIN_BLOCKERS_DEFINED=PASS
FORBIDDEN_BYPASS_PATHS_DEFINED=PASS
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS_BUILDER
ANALYSIS_EXECUTION_SEPARATION=PASS_BUILDER
MODE_A_MODE_B_SEPARATION=PASS_BUILDER
POLICY_A_B_ALIGNMENT=PASS_BUILDER
DOMAIN_BOUNDARY_BLOCKERS=0
G3_DOMAIN_BOUNDARIES_CONSOLIDATED=PASS_BUILDER_REMEDIATED
INDEPENDENT_CRITICAL_REVIEW=RETEST_04_REQUIRED
```

## 11. Próxima ação

Executar o Reteste 04 independente da LEA-19 sobre o HEAD final do PR #40.