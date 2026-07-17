# CONSOLIDAÇÃO CRUZADA — PTM V2.5, V2.6 E V2.7

## LEA-18 — Arquitetura documental integrada para preparação dos ADRs

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_CROSS_CONSOLIDATION_READY_FOR_SELF_REVIEW
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
PRE_WRITE_EXPECTED_PR_HEAD=f8a9121f4975a7f4d07ccf3522c5aaf7f09dd55b
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
LEGACY_VERSION=V2.4.3-R1
DOCUMENTATION_ONLY=YES
CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
APPLICATION_EXECUTED=NO
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
INDEPENDENT_CRITICAL_REVIEW=PENDING
```

## 2. Decisão executiva

As PTMs V2.5, V2.6 e V2.7 formam uma única arquitetura em camadas:

```text
V2.5=FOUNDATION_CONTRACTS_SAFE_MIGRATION
V2.6=OBSERVATION_ANALYSIS_SIMULATED_SIGNALS
V2.7=CONTROLLED_COMMAND_AUTHORIZATION_ACTION_RECEIPT_RECONCILIATION
```

A integração documental preserva as responsabilidades de cada etapa e impede bypass entre elas.

```text
FOUNDATION_DOES_NOT_EXECUTE
ANALYSIS_DOES_NOT_AUTHORIZE_OR_DISPATCH
SIGNAL_DOES_NOT_AUTOEXECUTE
COORDINATE_DOES_NOT_AUTHORIZE
ADAPTER_RECEIPT_DOES_NOT_CONFIRM_GLOBAL_TRUTH
CONTROLLED_UI_DOES_NOT_AUTHORIZE_REAL_FINANCIAL_EFFECT
```

Esta consolidação prepara ADRs. Ela não é o Documento Mestre, não congela a Arquitetura V1.0 e não autoriza implementação.

## 3. Fontes integrantes

### 3.1 Entregas da LEA-18

1. `INVENTARIO_FONTES_CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
2. `MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
3. `MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
4. `APENDICE_INDICE_INDIVIDUAL_218_REQUISITOS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
5. `REGISTRO_CONFLITOS_SUPERSESSOES_PRECEDENCIA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
6. `CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`.

### 3.2 Autoridades herdadas

- PTM V2.5, matriz, revisão independente e recibo pós-merge;
- PTM V2.6, matriz, revisão independente e recibo pós-merge;
- PTM V2.7, matriz, adendos, suplemento, reteste 02 e recibo pós-merge;
- Auditoria Mestra V2.4.3-R1 e evidência factual aprovada;
- política de automação em ambiente controlado;
- autoridade por domínio e protocolos de continuidade.

## 4. Autoridade por domínio

```text
PROJECT_OPERATIONAL_STATE=PROJECT_RUNTIME_STATE.yaml
HUMAN_STATE=PROJECT_STATE.md
ROADMAP=PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md
TASK_STATUS=Linear
INTEGRATED_CODE_AND_DOCS=GitHub_main
UNMERGED_WORK=active_PR_and_branch
PRODUCT_GLOBAL_STATE=server
CLIENTS=local_views_and_commands_subject_to_server_policy
EXTERNAL_VISUAL_SOURCE=evidence_not_internal_authority
```

Nenhuma fonte substitui outra fora de seu domínio. PR aberto não equivale a documentação integrada; issue concluída não equivale a merge; histórico não governa o presente.

## 5. Cadeia arquitetural

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

## 6. Handoffs obrigatórios

```text
H-01 LISTS_CONTEXT -> OBSERVATION
H-02 APPROVED_PROFILE -> OBSERVATION_SESSION
H-03 AUTHORIZED_SESSION -> FRAME_CAPTURE
H-04 FRAME_PROVENANCE -> VALIDATION
H-05 ELIGIBLE_FRAME -> EXTRACTION
H-06 ESTIMATED_DATA_WITH_LINEAGE -> ANALYSIS
H-07 ENGINE_RESULTS -> STRATEGY
H-08 ELIGIBLE_SIGNAL -> COMMAND
H-09 COMMAND_PLUS_GRANT -> TARGET_RESOLUTION
H-10 RESOLVED_TARGET_PLUS_CAPABLE_ADAPTER -> DISPATCH
H-11 ATTEMPT_PLUS_RECEIPT -> AUDIT_AND_RECONCILIATION
H-12 KILL_SWITCH_AND_POLICY -> ARMING_AND_DISPATCH_CONTROL
```

Falha em um handoff reduz capacidade, degrada ou bloqueia. Nenhuma falha eleva confiança ou amplia limites.

## 7. PTM V2.5 — fundação integrada

### 7.1 Responsabilidades

- servidor como autoridade de estado;
- configuração versionada e fail-closed;
- segredos fora do Git e redaction;
- fronteira de escritor único;
- existência física progressiva;
- listas independentes de análise e execução;
- cliente móvel pareado, revogável e sem autoridade global;
- perfis, ROIs, âncoras e alvos geométricos versionados;
- migração do JSON legado com backup, reconciliação e rollback;
- observabilidade, auditoria e diagnóstico separados.

### 7.2 Limites

```text
V2_5_OWNS_UI_AUTOMATION=NO
V2_5_GLOBAL_CONTROLLED_UI_PROHIBITION=NO
COORDINATE_CAPTURE_IN_CONTROLLED_SCOPE=ALLOWED
COORDINATE_AS_AUTHORIZATION=PROHIBITED
JSON_AS_FINAL_SOURCE_OF_TRUTH=REJECTED
CLIENT_DIRECT_DATABASE_ACCESS=PROHIBITED
```

## 8. PTM V2.6 — observação, análise e sinais

### 8.1 Pipeline

```text
AUTHORIZED_VISUAL_SOURCE
→ FRAME_WITH_PROVENANCE
→ VALIDATION_AND_QUALITY
→ VERSIONED_EXTRACTION
→ ESTIMATED_SERIES_WITH_UNCERTAINTY
→ IMMUTABLE_ANALYSIS_SNAPSHOT
→ ENGINES_A_TO_H
→ VERSIONED_STRATEGY
→ CANDIDATE_ARBITRATION
→ SIMULATED_SIGNAL_LIFECYCLE
```

### 8.2 Regras

- frame inválido não alimenta análise;
- `UNKNOWN` nunca aumenta elegibilidade;
- score não supera blocker;
- dado estimado não é dado oficial da corretora;
- motores usam inputs explícitos e envelope comum;
- motor H não contorna blockers A–G;
- estratégia é explicável e versionada;
- candidato não é sinal;
- sinal expira, invalida ou é supersedido;
- sinal não cria comando ou ação.

### 8.3 Automação controlada

```text
CONTROLLED_CAPTURE_AND_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_TEST_HARNESS_UI_ACTION=ALLOWED_OUTSIDE_ANALYSIS_AUTHORITY
ANALYSIS_ENGINE_DIRECT_UI_ACTION=PROHIBITED
```

## 9. PTM V2.7 — execução controlada

### 9.1 Dimensões independentes

```text
EXECUTION_CHANNEL=DRY_RUN|SIMULATED|CONTROLLED_UI
FINANCIAL_EFFECT_MODE=NONE|SIMULATED_ONLY
CONTROLLED_UI_WITH_REAL_FINANCIAL_EFFECT=INVALID_AND_BLOCKED
```

A restrição financeira se aplica a qualquer classe de alvo, inclusive aplicação própria ou sandbox conectada a infraestrutura financeira de produção.

### 9.2 Domínios separados

```text
VALIDATED_SIGNAL != EXECUTION_COMMAND
EXECUTION_COMMAND != AUTHORIZATION_GRANT
AUTHORIZATION_GRANT != DISPATCH_ATTEMPT
DISPATCH_ATTEMPT != EFFECT_RECEIPT
EFFECT_RECEIPT != RECONCILIATION_RESULT
```

### 9.3 Estados normativos

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

Nenhum estado confirma ordem financeira real, alteração de saldo ou resultado monetário de produção.

### 9.4 Contratos mínimos

`ExecutionCommand` deve vincular:

- IDs de comando, trace, sinal e idempotência;
- canal e dimensão financeira;
- classe e identidade do alvo;
- ação e versão da allowlist;
- contexto, política e versão do adaptador;
- UTC, TTL, fonte temporal, boot e instância de processo.

`AuthorizationGrant` deve vincular:

- hash do comando;
- ator, cliente e sessão;
- canal, dimensão financeira, alvo e allowlist;
- política, emissão, expiração e revogação.

`EffectReceipt` deve separar:

```text
ui_result=NO_EFFECT|CONTROLLED_UI_EFFECT|UNKNOWN
financial_result=NONE|SIMULATED_EFFECT|UNKNOWN
```

### 9.5 Restart e recovery

```text
PROCESS_INSTANCE_CHANGED=RESTART_DETECTED
PRE_RESTART_COMMAND_DISPATCHABLE=NO
PRE_RESTART_COMMAND_AUTO_REARM=NO
PRE_RESTART_COMMAND_AUTO_REDISPATCH=NO
NEW_ACTION_REQUIRES=NEW_COMMAND_AND_NEW_AUTHORIZATION
```

Tentativa já despachada entra em reconciliação. Comando não despachado é bloqueado sem efeito. UTC e TTL preservam auditoria e expiração, mas não restauram despachabilidade.

## 10. Segurança transversal

### 10.1 Permitido em escopo controlado

```text
CONTROLLED_SCREEN_CAPTURE=ALLOWED
CONTROLLED_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_POINTER_MOVEMENT=ALLOWED
CONTROLLED_KEYBOARD_INPUT=ALLOWED
CONTROLLED_CLICK=ALLOWED
CONTROLLED_TEST_AUTHENTICATION=ALLOWED
CONTROLLED_END_TO_END_TESTS=ALLOWED
```

Condições: alvo identificado, allowlist, sessão declarada, parada imediata, limites, auditoria, redaction, segredo de teste fora do Git e ambiente reversível.

### 10.2 Permanentemente não autorizado por esta arquitetura

```text
SECRETS_IN_GIT=PROHIBITED
UNAUTHORIZED_THIRD_PARTY_ACCESS=PROHIBITED
REAL_FINANCIAL_EFFECT=NOT_AUTHORIZED
EXTERNAL_FINANCIAL_ORDER=NOT_AUTHORIZED
REAL_BALANCE_CHANGE=NOT_AUTHORIZED
PRODUCTION_CREDENTIAL_DISCLOSURE=PROHIBITED
```

### 10.3 Provas negativas

```text
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCK
UNCONTROLLED_UI_ACTION=BLOCK
TARGET_NOT_ALLOWLISTED=BLOCK
UNKNOWN_TARGET=BLOCK
AUTHORIZATION_BYPASS=BLOCK
KILL_SWITCH_BYPASS=BLOCK
PRODUCTION_SECRET_DETECTED=BLOCK
REAL_FINANCIAL_EFFECT_ATTEMPT=BLOCK
PRE_RESTART_COMMAND_REDISPATCH=BLOCK
```

A prova não falha apenas porque existem ferramentas de captura, OCR ou automação usadas dentro do adaptador/harness controlado.

## 11. Persistência e existência progressiva

```text
ENTITY_EXISTS_PHYSICALLY_ONLY_IF=
PRODUCER_DEFINED
AND CONSUMER_DEFINED
AND REQUIREMENT_LINKED
AND TEST_LINKED
AND RETENTION_DEFINED_WHEN_HISTORICAL
```

Esta consolidação não escolhe tecnologia, não define tabela, não gera SQL e não cria migration. Essas decisões pertencem aos ADRs.

## 12. Cobertura documental

```text
V2_5_REQUIREMENT_IDS=56
V2_6_REQUIREMENT_IDS=78
V2_7_REQUIREMENT_IDS=84
TOTAL_REQUIREMENT_IDS=218
INDIVIDUAL_INDEX_ROWS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
NEW_REQUIREMENT_IDS=0
SUPERSEDED_INTERPRETATION_IDS=32
```

Cada ID está vinculado a domínio primário; a matriz consolidada registra domínios secundários, handoffs e fontes normativas.

## 13. Conflitos e supersessões

```text
CONFLICT_CLASSES_REVIEWED=24
UNRESOLVED_NORMATIVE_CONFLICTS=0
```

Principais resoluções:

- exclusão de UI por etapa não é proibição global de capacidade controlada;
- V2.7 separa canal de execução e dimensão financeira;
- `CONTROLLED_UI` é adaptador de interface, não adaptador financeiro;
- estado, comando, grant, recibo e recovery do reteste 02 prevalecem nas cláusulas conflitantes;
- restart invalida comando anterior;
- recibo é evidência, não verdade global;
- mergeabilidade não é autorização de merge;
- especificação de teste não equivale a runtime executado.

## 14. ADRs candidatos

```text
ADR_CANDIDATE_COUNT=18
P0_CANDIDATES=12
P1_CANDIDATES=5
P2_CANDIDATES=1
```

Grupos:

1. governança, servidor e lifecycle;
2. persistência, migrations e contratos;
3. identidade, clientes e pareamento;
4. perfis, ROIs, alvos e retenção visual;
5. motores A–H, estratégia e thresholds;
6. máquina de execução, adaptadores, kill switch e tempo;
7. idempotência, recibo, reconciliação e auditoria;
8. estratégia de testes e evidências.

Nenhum ADR foi criado ou decidido nesta missão.

## 15. Não objetivos

```text
APPLICATION_IMPLEMENTATION=OUT_OF_SCOPE
DATABASE_IMPLEMENTATION=OUT_OF_SCOPE
SQL_AND_MIGRATIONS=OUT_OF_SCOPE
REAL_BROKER_INTEGRATION=OUT_OF_SCOPE
PRODUCTION_CREDENTIALS=OUT_OF_SCOPE
REAL_MONEY_OPERATION=OUT_OF_SCOPE
AUTONOMOUS_EXTERNAL_INFRASTRUCTURE=OUT_OF_SCOPE
ARCHITECTURE_V1_FREEZE=OUT_OF_SCOPE_UNTIL_DOCUMENT_MASTER_REVIEW
```

## 16. Condições para avançar aos ADRs

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
TRACEABILITY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=PASS
UNRESOLVED_NORMATIVE_CONFLICTS=0
GITHUB_LINEAR_ALIGNMENT=PASS
```

O builder não pode emitir sozinho esse Boss Gate.

## 17. Resultado do builder — documento consolidado

```text
SOURCE_INVENTORY_COMPLETE=PASS_BUILDER
DOMAIN_BOUNDARIES_CONSOLIDATED=PASS_BUILDER
REQUIREMENTS_TRACEABILITY_COMPLETE=PASS_BUILDER
INDIVIDUAL_REQUIREMENT_INDEX_COMPLETE=PASS_BUILDER
CONFLICTS_AND_SUPERSESSIONS_RESOLVED=PASS_BUILDER
ADR_CANDIDATE_CATALOG_COMPLETE=PASS_BUILDER
CONSOLIDATED_ARCHITECTURE_DOCUMENT_COMPLETE=PASS_BUILDER
DOCUMENTAL_BLOCKERS=0
G6_CONSOLIDATED_DOCUMENT_READY=READY_FOR_BUILDER_SELF_REVIEW
INDEPENDENT_CRITICAL_REVIEW=PENDING
```

## 18. Próxima ação

Executar auto-revisão preliminar do builder, corrigir bloqueadores encontrados e preparar o PR `#40` para revisão crítica independente.