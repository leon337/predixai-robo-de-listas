# MAPA UNIFICADO DE DOMÍNIOS E FRONTEIRAS

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DOMAIN_BOUNDARY_MAP_COMPLETE
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
PRE_WRITE_EXPECTED_PR_HEAD=5e2fb1cf4643d6f3adf5d0b156540ba7bb9015f1
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

Este documento consolida as fronteiras arquiteturais das PTMs V2.5, V2.6 e V2.7. Os identificadores `DOM-*` e `H-*` são identificadores internos deste mapa e não criam novos requisitos PTM.

## 2. Objetivo

Definir uma cadeia única de autoridade e responsabilidade para impedir:

- acoplamento oculto entre análise e execução;
- transformação automática de sinal em ação;
- uso de coordenada como autorização;
- promoção de recibo local a verdade global;
- mistura entre efeito de interface e efeito financeiro;
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
CONTROLLED_UI_ACTION!=REAL_FINANCIAL_EFFECT
UNKNOWN_DATA=CAPABILITY_REDUCTION
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
```

## 4. Cadeia arquitetural consolidada

```text
GOVERNANÇA E ESTADO
→ CONFIGURAÇÃO E SEGURANÇA
→ PERSISTÊNCIA E RECOVERY
→ LISTAS E AGENDAMENTOS
→ CLIENTES E DISPOSITIVOS
→ PERFIS, CALIBRAÇÃO E GEOMETRIA
→ SESSÃO DE OBSERVAÇÃO
→ CAPTURA E FRAME
→ VALIDAÇÃO E QUALIDADE
→ EXTRAÇÃO E DADOS ESTIMADOS
→ ANÁLISE A–H
→ ESTRATÉGIA, CANDIDATO E SINAL
→ COMANDO, AUTORIZAÇÃO E POLÍTICA
→ RESOLUÇÃO DE ALVO E ADAPTADOR
→ DISPATCH, RECIBO E RECONCILIAÇÃO
→ AUDITORIA, OBSERVABILIDADE E CONTENÇÃO
```

## 5. Domínios canônicos

### DOM-01 — Governança e estado operacional

```text
PRIMARY_OWNER=GOVERNANCE
PTM_ORIGIN=TRANSVERSAL
AUTHORITY=PROJECT_RUNTIME_STATE.yaml_FOR_OPERATIONAL_CONTINUITY
INPUTS=GitHub_main|active_PR|Linear|PROJECT_STATE|trunk
OUTPUTS=state_revision|transition_id|mission|gate|blockers|next_action
STATES=STATE_STABLE|TRANSITION_IN_PROGRESS|SYNC_PARTIAL|STATE_CONFLICT|BLOCKED
BLOCKERS=concurrent_update|state_drift|connector_failure|schema_mismatch
```

Responsabilidades:

- controlar continuidade, missão, gate e sincronização;
- impedir escrita com snapshot obsoleto;
- distinguir estado consolidado em `main` de trabalho não integrado no PR.

Não pode:

- decidir regra de produto por comentário histórico;
- declarar merge futuro como fato;
- usar lock consultivo como garantia técnica exclusiva.

### DOM-02 — Configuração, identidade e segredos

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=SERVER_RESOLVED_VERSIONED_CONFIGURATION
INPUTS=safe_defaults|authorized_config|explicit_overrides|environment_identity
OUTPUTS=config_snapshot|feature_capabilities|reason_codes|redacted_diagnostics
STATES=UNRESOLVED|VALID|INVALID|BLOCKED
BLOCKERS=invalid_schema|unknown_secret_source|unsafe_default|identity_mismatch
```

Responsabilidades:

- resolver configuração de forma determinística e fail-closed;
- manter segredos fora do Git e aplicar redaction;
- impedir feature flag de elevar silenciosamente o modo operacional.

Não pode:

- armazenar token, cookie, chave privada ou credencial de produção no repositório;
- habilitar efeito financeiro real;
- substituir autorização de sessão.

### DOM-03 — Persistência, eventos, backup e recovery

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=SERVER_SINGLE_WRITE_BOUNDARY
INPUTS=validated_domain_commands|migration_inputs|audit_intents
OUTPUTS=committed_state|versioned_records|outbox_events|backup_catalog|recovery_result
STATES=READY|WRITING|COMMITTED|RECOVERING|DEGRADED|BLOCKED
BLOCKERS=integrity_failure|writer_conflict|migration_mismatch|restore_unverified
```

Responsabilidades:

- centralizar escrita;
- preservar origem bruta na migração do JSON legado;
- vincular evento externo crítico à transação quando o fluxo existir;
- demonstrar backup, restauração, reconciliação e rollback seguro.

Não pode:

- permitir escrita direta por Android, UI, rota ou handler;
- criar schema físico sem produtor, consumidor, requisito, teste e retenção;
- tratar JSON legado como autoridade persistente final.

### DOM-04 — Listas, itens e agendamentos

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=LISTS_DOMAIN_ON_SERVER
INPUTS=validated_list_commands|schedule_definitions|operator_identity
OUTPUTS=list_revision|item_revision|schedule_context|validation_reason_codes
STATES=DRAFT|PUBLISHED|ACTIVE|ARCHIVED|INVALID
BLOCKERS=duplicate_identity|invalid_time|invalid_direction|stale_revision
```

Responsabilidades:

- manter listas independentes de observação, análise e execução;
- versionar revisões publicadas/ativas;
- fornecer contexto de intenção e agenda, não ação física.

Não pode:

- produzir sinal por conta própria;
- disparar clique ou ordem;
- editar silenciosamente versão já publicada.

### DOM-05 — Clientes, dispositivos, pareamento e sessão humana

```text
PRIMARY_OWNER=PTM_V2.5_FOUNDATION_WITH_V2.7_AUTHORIZATION_USE
AUTHORITY=SERVER_FOR_GLOBAL_STATE
INPUTS=pairing_request|device_identity|operator_presence|revocation_state
OUTPUTS=paired_device|client_session|local_snapshot|human_confirmation
STATES=UNPAIRED|PAIRING|PAIRED|REVOKED|DISCONNECTED|STALE
BLOCKERS=unknown_device|expired_pairing|revoked_client|sequence_gap_unresolved
```

Responsabilidades:

- oferecer cliente móvel e painel como visão operacional;
- suportar pareamento local, revogável e auditável;
- usar sequence e snapshot para reconexão;
- fornecer presença/confirmação humana quando exigida pela V2.7.

Não pode:

- tornar Android autoridade global;
- confirmar efeito apenas por estado local;
- rearmar execução automaticamente após desconexão.

### DOM-06 — Perfis, calibração, ROIs e geometria de alvo

```text
PRIMARY_OWNER=PTM_V2.5
AUTHORITY=APPROVED_VERSIONED_PROFILE_AND_GEOMETRY
INPUTS=application_identity|monitor|resolution|scale|anchors|coordinate_capture
OUTPUTS=profile_version|roi_version|target_geometry|compatibility_result
STATES=DRAFT|VALIDATING|APPROVED|ACTIVE|INCOMPATIBLE|REVOKED
BLOCKERS=identity_mismatch|geometry_drift|scale_change|unapproved_profile
```

Responsabilidades:

- separar perfil de ambiente, aplicação e monitor;
- versionar ROIs, âncoras, assinaturas e alvos geométricos;
- permitir captura de coordenadas em escopo controlado;
- fornecer dados para observação e resolução posterior do alvo.

Não pode:

- transformar coordenada em autorização;
- autorizar ação apenas porque o perfil está ativo;
- manter perfil compatível após mudança não validada de janela, resolução ou escala.

### DOM-07 — Sessão de observação

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=OBSERVATION_SESSION_STATE_ON_SERVER
INPUTS=active_profile|authorized_application|monitor|rois|resolved_config
OUTPUTS=observation_session|eligibility_state|session_reason_codes
STATES=CREATED|VALIDATING|ACTIVE|DEGRADED|BLOCKED|CLOSED
BLOCKERS=unauthorized_source|profile_incompatible|window_lost|freshness_failure
```

Responsabilidades:

- ligar toda observação a sessão identificada e versionada;
- validar fonte visual antes de aceitar frames;
- degradar ou bloquear quando identidade, geometria ou estabilidade forem perdidas.

Não pode:

- selecionar silenciosamente janela desconhecida;
- produzir ação de UI;
- elevar confiança na presença de dado desconhecido.

### DOM-08 — Captura, frame e proveniência

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=FRAME_REFERENCE_WITH_PROVENANCE
INPUTS=authorized_visual_source|observation_session|capture_policy
OUTPUTS=frame_reference|frame_hash|roi_crops|sequence|retention_decision
STATES=CAPTURED|DUPLICATE|STALE|OUT_OF_ORDER|REJECTED|ELIGIBLE_FOR_VALIDATION
BLOCKERS=source_mismatch|sequence_error|obsolete_frame|retention_violation
```

Responsabilidades:

- registrar hash, origem, dimensões, timestamps e sequência;
- preservar vínculo entre frame, sessão, perfil e ROI;
- minimizar retenção de imagem sensível.

Não pode:

- declarar frame válido antes do DOM-09;
- persistir conteúdo bruto indefinidamente por padrão;
- usar captura como autorização de ação.

### DOM-09 — Validação visual e qualidade

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=VALIDATION_AND_QUALITY_RESULT
INPUTS=frame_reference|profile_version|roi_version|visual_signature
OUTPUTS=check_results|blockers|confidence_caps|frame_eligibility
STATES=PASS|DEGRADED|FAIL|UNKNOWN
BLOCKERS=mandatory_fail|unknown_identity|occlusion|instability|quality_below_gate
```

Responsabilidades:

- validar identidade, geometria, frescor, completude, estabilidade e extração;
- aplicar caps monotônicos;
- impedir score agregado de superar o menor cap obrigatório.

Não pode:

- considerar `UNKNOWN` como aprovação;
- liberar análise de frame com `FAIL` obrigatório;
- substituir benchmark por threshold arbitrário definitivo.

### DOM-10 — Extração visual e dados estimados

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=VERSIONED_EXTRACTION_RESULT
INPUTS=eligible_frame|roi|extractor_version|mapping_version
OUTPUTS=visual_features|estimated_series|estimated_candles|uncertainty|lineage
STATES=EXTRACTED|PARTIAL|DEGRADED|FAILED|INVALIDATED
BLOCKERS=extractor_failure|mapping_incompatible|scale_change|insufficient_quality
```

Responsabilidades:

- produzir resultado determinístico para os mesmos inputs e versões;
- declarar incerteza e linhagem;
- manter diferença entre dado visual estimado e dado oficial de mercado.

Não pode:

- ocultar lacunas ou duplicidades;
- declarar candle estimado como dado oficial da corretora;
- executar ponteiro, teclado ou clique.

### DOM-11 — Análise A–H

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=IMMUTABLE_ANALYSIS_SNAPSHOT_AND_ENGINE_RESULTS
INPUTS=eligible_estimated_data|strategy_context|engine_versions|config_snapshot
OUTPUTS=structure|trend|zones|volatility|candle_context|momentum|confluence|strategy_evaluation
STATES=READY|WAIT_MORE_DATA|DEGRADED|BLOCKED|COMPLETE
BLOCKERS=invalid_snapshot|insufficient_data|quality_cap|engine_contradiction
```

Responsabilidades:

- executar motores A–H com envelope comum;
- preservar evidências, contradições e versões;
- impedir o motor H de contornar blockers A–G;
- produzir resultado equivalente para mesmos inputs ou divergência explicada.

Não pode:

- manter estado oculto não versionado;
- chamar adaptador de UI;
- criar autorização ou comando de execução.

### DOM-12 — Estratégia, candidatos e sinais

```text
PRIMARY_OWNER=PTM_V2.6
AUTHORITY=VERSIONED_STRATEGY_AND_SIGNAL_LIFECYCLE
INPUTS=analysis_results|quality_caps|strategy_version|schedule_context
OUTPUTS=strategy_decision|candidate_set|arbitration_result|signal
STATES=WAIT|CANDIDATE|ACTIVE|EXPIRED|INVALIDATED|SUPERSEDED|BLOCKED
BLOCKERS=contradiction|low_quality|stale_analysis|strategy_rule_failure|duplicate_fingerprint
```

Responsabilidades:

- aplicar estratégia versionada e explicável;
- arbitrar candidatos de forma determinística;
- emitir sinal com fingerprint, validade, confiança, qualidade e evidências;
- expirar, invalidar ou superseder sinais explicitamente.

Não pode:

- autoexecutar sinal;
- escolher alvo de UI;
- criar grant de autorização;
- reinterpretar análise após emissão sem nova versão.

### DOM-13 — Comando, autorização e policy engine

```text
PRIMARY_OWNER=PTM_V2.7
AUTHORITY=SERVER_EXECUTION_POLICY_AND_EXPLICIT_GRANT
INPUTS=eligible_signal|context_snapshot|operator_confirmation|target_identity|policy_version
OUTPUTS=immutable_command|authorization_grant|policy_decision|frozen_preconditions
STATES=DISABLED|SAFE_IDLE|VALIDATING|ARMED_DRY_RUN|ARMED_SIMULATED|ARMED_CONTROLLED_UI|BLOCKED|CANCELLED|KILLED
BLOCKERS=signal_ineligible|grant_expired|policy_denied|target_unknown|kill_switch_unhealthy|financial_mode_invalid
```

Responsabilidades:

- separar sinal, comando, grant e decisão de política;
- vincular autorização a comando, canal, alvo, ação, allowlist, validade e ator;
- congelar e revalidar pré-condições imediatamente antes do dispatch;
- invalidar comando anterior após qualquer mudança de instância do processo.

Não pode:

- criar comando sem sinal elegível;
- ampliar limites automaticamente;
- aceitar capacidade financeira real;
- tratar presença do cliente como grant implícito.

### DOM-14 — Resolução de alvo e adaptadores

```text
PRIMARY_OWNER=PTM_V2.7
AUTHORITY=ALLOWLISTED_LOGICAL_TARGET_PLUS_ADAPTER_CAPABILITY
INPUTS=authorized_command|target_logical_id|profile_geometry|application_identity|allowlist
OUTPUTS=resolved_target|adapter_request|capability_check|dispatch_readiness
STATES=UNRESOLVED|RESOLVED|INCOMPATIBLE|UNAUTHORIZED|READY|BLOCKED
BLOCKERS=coordinate_only|target_not_allowlisted|identity_mismatch|adapter_unknown|capability_mismatch
```

Responsabilidades:

- resolver alvo por identidade lógica e geometria versionada;
- expor adaptadores `NULL`, `SIMULATED` e `CONTROLLED_UI` com capacidades explícitas;
- bloquear alvo, canal ou ação fora da allowlist;
- sanitizar payload e rejeitar credencial de produção.

Não pode:

- tratar adaptador `CONTROLLED_UI` como adaptador financeiro;
- despachar usando coordenada isolada;
- permitir biblioteca de UI fora da fronteira controlada do adaptador.

### DOM-15 — Dispatch, recibo, reconciliação e recovery

```text
PRIMARY_OWNER=PTM_V2.7
AUTHORITY=RECONCILED_SERVER_STATE
INPUTS=ready_command|authorization_grant|adapter_request|kill_switch|deadlines
OUTPUTS=attempt_record|adapter_receipt|ui_result|financial_result|reconciliation_result
STATES=DISPATCHING|AWAITING_RECEIPT|RECONCILING|COMPLETED_NO_EFFECT|COMPLETED_SIMULATED|COMPLETED_CONTROLLED_UI|TIMED_OUT|UNKNOWN_EFFECT|FAILED_NO_EFFECT|KILLED
BLOCKERS=receipt_ambiguity|unknown_effect|restart|deadline_expired|dedupe_conflict|circuit_open
```

Responsabilidades:

- registrar intenção antes do efeito;
- aplicar idempotência, deduplicação, serialização, deadline e circuit breaker;
- separar `ui_result` de `financial_result`;
- reconciliar comando, tentativa, recibo e estado observado;
- bloquear retry quando ausência de efeito não estiver comprovada;
- preservar auditoria durante recovery.

Não pode:

- considerar timeout como ausência comprovada de efeito;
- reenviar automaticamente após restart;
- apagar evidência de tentativa;
- inferir resultado financeiro real a partir de efeito de UI.

### DOM-16 — Segurança, auditoria, observabilidade e contenção

```text
PRIMARY_OWNER=TRANSVERSAL_V2.5_V2.6_V2.7
AUTHORITY=SECURITY_POLICY_PLUS_APPEND_ONLY_AUDIT_CONTRACT
INPUTS=all_domain_events|trace_id|command_id|authorization_id|security_context
OUTPUTS=audit_records|structured_logs|metrics|alerts|diagnostics|kill_switch_events
STATES=HEALTHY|DEGRADED|ALERTED|CIRCUIT_OPEN|KILLED|RECOVERING
BLOCKERS=secret_detected|unauthorized_access|audit_gap|kill_switch_failure|real_financial_effect_attempt
```

Responsabilidades:

- correlacionar cadeia completa sem expor dados sensíveis;
- separar auditoria de segurança, comando, efeito e diagnóstico;
- aplicar redaction, retenção e minimização;
- prover kill switch dominante e evidências negativas verificáveis.

Provas negativas obrigatórias:

```text
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCK
UNCONTROLLED_UI_ACTION=BLOCK
UNAUTHORIZED_EXTERNAL_ACCESS=BLOCK
PRODUCTION_SECRET_IN_GIT=BLOCK
CONTROLLED_UI_WITH_REAL_FINANCIAL_EFFECT=BLOCK
PRE_RESTART_COMMAND_REDISPATCH=BLOCK
TARGET_NOT_ALLOWLISTED=BLOCK
```

## 6. Handoffs obrigatórios

| ID | Origem → destino | Contrato mínimo | Falha obrigatória |
|---|---|---|---|
| H-01 | DOM-04 → DOM-07 | lista/agendamento fornece contexto versionado | contexto inválido não inicia sessão |
| H-02 | DOM-06 → DOM-07 | perfil, aplicação, monitor e ROIs aprovados | incompatibilidade bloqueia observação |
| H-03 | DOM-07 → DOM-08 | sessão ativa autoriza somente captura da fonte identificada | fonte perdida rejeita frame |
| H-04 | DOM-08 → DOM-09 | frame possui proveniência completa | frame sem hash/origem é rejeitado |
| H-05 | DOM-09 → DOM-10 | somente frame elegível alimenta extração | `FAIL` ou blocker impede extração |
| H-06 | DOM-10 → DOM-11 | dados estimados carregam incerteza e linhagem | mapping incompatível bloqueia snapshot |
| H-07 | DOM-11 → DOM-12 | resultados A–H e caps são imutáveis | motor H não contorna blockers |
| H-08 | DOM-12 → DOM-13 | sinal válido, elegível e não expirado | sinal não vira comando automaticamente |
| H-09 | DOM-13 → DOM-14 | comando e grant vinculam alvo, ação e canal | grant incompatível bloqueia resolução |
| H-10 | DOM-14 → DOM-15 | alvo resolvido e adaptador capaz | coordenada isolada ou alvo desconhecido bloqueia dispatch |
| H-11 | DOM-15 → DOM-16 | tentativa e recibo sempre produzem auditoria | lacuna de auditoria bloqueia recovery seguro |
| H-12 | DOM-16 → DOM-13/15 | kill switch, circuito e política dominam arming/dispatch | estado inseguro cancela ou mata fluxo |

## 7. Autoridades que não podem ser confundidas

| Informação | Autoridade | Não autoridade |
|---|---|---|
| Estado operacional do projeto | `PROJECT_RUNTIME_STATE.yaml` | conversa ou histórico |
| Trabalho ainda não integrado | PR ativo | `main` |
| Estado global do produto | servidor | Android/UI/cache local |
| Identidade visual elegível | sessão + perfil + validação | janela encontrada por conveniência |
| Qualidade do frame | DOM-09 | score isolado ou OCR bruto |
| Resultado analítico | snapshot + motores versionados | executor |
| Sinal | DOM-12 | lista, UI ou adaptador |
| Autorização | grant explícito DOM-13 | sinal, coordenada ou presença do cliente |
| Alvo executável | identidade lógica + allowlist DOM-14 | par X/Y isolado |
| Efeito confirmado | reconciliação DOM-15 | recibo do adaptador isolado |
| Permissão financeira real | gate comercial/legal futuro e separado | política de UI controlada |

## 8. Caminhos proibidos

```text
LIST_ITEM -> DIRECT_CLICK                       = PROHIBITED
ANALYSIS_ENGINE -> UI_ADAPTER                   = PROHIBITED
SIGNAL -> AUTO_EXECUTION                        = PROHIBITED
COORDINATE -> AUTHORIZATION                     = PROHIBITED
CLIENT_CACHE -> GLOBAL_STATE_CONFIRMATION       = PROHIBITED
ADAPTER_RECEIPT -> GLOBAL_TRUTH                 = PROHIBITED
TIMEOUT -> ASSUME_NO_EFFECT                     = PROHIBITED
UNKNOWN_EFFECT -> AUTOMATIC_RETRY               = PROHIBITED
CONTROLLED_UI -> REAL_FINANCIAL_AUTHORIZATION   = PROHIBITED
RESTART -> REARM_OLD_COMMAND                    = PROHIBITED
```

## 9. Decisões candidatas a ADR identificadas

Este mapa não cria ADRs, mas registra candidatos para etapa posterior:

1. topologia e autoridade do servidor;
2. fronteira de escritor único e tecnologia de persistência;
3. contratos REST/eventos e existência progressiva;
4. modelo de pareamento e identidade de cliente;
5. representação de perfil, ROI, alvo lógico e compatibilidade;
6. retenção de frames e artefatos visuais;
7. arquitetura dos motores A–H e estratégia versionada;
8. máquina de estados de execução e persistência temporal;
9. contrato dos adaptadores `NULL|SIMULATED|CONTROLLED_UI`;
10. topologia do kill switch e circuit breaker;
11. idempotência, deduplicação e serialização por alvo;
12. estrutura de recibo e reconciliação multidimensional;
13. taxonomia completa de `target_logical_id`;
14. observabilidade, auditoria append-only e redaction.

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
CONTROLLED_UI_FINANCIAL_EFFECT_SEPARATION=PASS_BUILDER
DOMAIN_BOUNDARY_BLOCKERS=0
G3_DOMAIN_BOUNDARIES_CONSOLIDATED=PASS_BUILDER
INDEPENDENT_CRITICAL_REVIEW=PENDING
```

## 11. Próxima ação

Construir a matriz consolidada de requisitos e rastreabilidade, preservando os IDs existentes das três PTMs e vinculando cada requisito ao domínio e handoff aplicável.