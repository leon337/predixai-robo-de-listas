# ADR-0016 — Relógios, deadlines e identidade de processo

## Controle

```text
ADR_ID=ADR-0016
CANDIDATE_ID=ADR-CAND-016
PRIORITY=P1
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
DEPENDS_ON=ADR-0008|ADR-0010|ADR-0011
MUST_ALIGN_WITH=ADR-0015|ADR-0018
```

## Contexto

UTC é necessário para auditoria e correlação, mas pode sofrer ajuste, rollback ou skew. Relógio monotônico mede deadlines apenas dentro do mesmo processo. Após restart, um deadline monotônico anterior não pode restaurar a despachabilidade de comando ou grant.

## Decisão

Adotar um contrato temporal de três identidades complementares:

```text
UTC_CLOCK=auditoria, ordenação aproximada entre processos e expiração documental
MONOTONIC_PROCESS_CLOCK=orçamento e deadline somente dentro da mesma instância
PROCESS_IDENTITY=boot_id + process_instance_id
```

Todo artefato despachável registra `created_at_utc`, `expires_at_utc`, `ttl_ms`, `clock_source_id`, `boot_id_at_creation`, `process_instance_id_at_creation` e `deadline_monotonic_process_local` quando aplicável.

Mudança de `process_instance_id` invalida a despachabilidade de todo comando não terminal criado pela instância anterior. UTC ainda válido não reverte essa decisão.

## Regras normativas

```text
UTC_PURPOSE=AUDIT_AND_DOCUMENTAL_EXPIRATION
MONOTONIC_PURPOSE=SAME_PROCESS_DEADLINE
MONOTONIC_VALUE_PERSISTED_AS_CROSS_PROCESS_AUTHORITY=PROHIBITED
PROCESS_INSTANCE_ID=REQUIRED
BOOT_ID=REQUIRED_WHEN_PLATFORM_SUPPORTS_RELIABLE_IDENTITY
PROCESS_INSTANCE_CHANGED=RESTART_DETECTED
PRE_RESTART_COMMAND_DISPATCHABLE=NO
PRE_RESTART_AUTO_REARM=NO
PRE_RESTART_AUTO_REDISPATCH=NO
NEW_EFFECT_REQUIRES=NEW_COMMAND_AND_NEW_AUTHORIZATION
CLOCK_ROLLBACK_EXTENDS_VALIDITY=PROHIBITED
CLOCK_SKEW_UNKNOWN=BLOCK_OR_REDUCE_CAPABILITY
DEADLINE_EXPIRED=NO_DISPATCH
TTL_NEGATIVE_OR_OVERFLOW=BLOCK
TIME_SOURCE_CHANGE=AUDIT_AND_REVALIDATE
KILL_EPOCH_REVALIDATION=REQUIRED
```

## Avaliação temporal

Dentro da mesma instância, a ação só permanece elegível quando:

```text
same_process_instance
AND same_or_valid_boot_identity
AND monotonic_deadline_not_expired
AND utc_not_expired
AND clock_source_valid
AND policy_and_kill_epoch_valid
```

Qualquer resultado `UNKNOWN` reduz capacidade e bloqueia efeito.

## Alternativas consideradas

### Usar somente UTC

Rejeitada porque ajustes do relógio podem prolongar ou encurtar indevidamente a validade.

### Persistir timestamp monotônico e reutilizá-lo após restart

Rejeitada porque o domínio monotônico não é comparável entre instâncias.

### Retomar comandos anteriores quando UTC estiver válido

Rejeitada porque restart perde o contexto operacional e pode duplicar efeito.

### Sincronização distribuída complexa na V1

Não adotada; o servidor local é autoridade e falha conservadoramente quando a fonte temporal é incerta.

## Consequências

### Positivas

- rollback de relógio não amplia autorização;
- restart não rearma ou redistribui comando antigo;
- deadlines em processo usam fonte adequada;
- auditoria preserva UTC e identidade da fonte;
- recovery fica explícito.

### Negativas e custos

- novos IDs e reason codes;
- comandos não despachados antes de restart precisam ser recriados;
- skew pode causar bloqueio conservador;
- testes precisam controlar relógio e identidade de processo.

## Segurança, recovery e falha segura

```text
PROCESS_INSTANCE_MISMATCH=BLOCK_AND_RECONCILE
BOOT_ID_MISMATCH=BLOCK_AND_RECONCILE
UTC_ROLLBACK_DETECTED=BLOCK_AND_AUDIT
CLOCK_SOURCE_UNKNOWN=BLOCK
MONOTONIC_DEADLINE_MISSING_WHEN_REQUIRED=BLOCK
PRE_RESTART_OPEN_ATTEMPT=RECONCILE_NOT_REDISPATCH
PRE_RESTART_UNDISPATCHED_COMMAND=TERMINATE_NO_EFFECT
NEW_ACTION_AFTER_RESTART=NEW_IDS_AND_NEW_GRANT
```

Reason codes mínimos:

```text
PROCESS_INSTANCE_CHANGED
BOOT_ID_CHANGED
CLOCK_ROLLBACK_DETECTED
CLOCK_SKEW_EXCEEDED_POLICY
DEADLINE_EXPIRED
CLOCK_SOURCE_INVALID
PRE_RESTART_COMMAND_INVALIDATED
NEW_COMMAND_REQUIRED_AFTER_RESTART
NEW_AUTHORIZATION_REQUIRED_AFTER_RESTART
```

## Rastreabilidade

`V27-SAF-008` é o requisito diferido canônico de `ADR-CAND-016`. Ele pertence ao contrato de fonte temporal, boot, skew, sequência e assinatura antes do arming; não ao registro de thresholds.

```text
PRIMARY_DOMAINS=DOM-13|DOM-15
SECONDARY_DOMAINS=DOM-01|DOM-16
HANDOFFS=H-09|H-10|H-12
DEFERRED_REQUIREMENTS_FROM_P0_APPENDIX=V27-SAF-008
DEFERRED_REQUIREMENT_COUNT=1
COMPLEMENTARY_REQUIREMENTS=PTM-V27-004..007|PTM-V27-010..018|PTM-V27-030..031|V27-PRE-001..006|V27-CMD-001..006|V27-AUT-001..006|V27-EXE-005..007|V27-QA-003..007
NORMATIVE_ADDENDUM=docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
TRACEABILITY_APPENDIX=docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_ADRS_P1_P2_LEA-30_20260718.md
```

## Critérios de aceitação

```text
DUAL_CLOCK_PURPOSE_SEPARATED=PASS_BUILDER
PROCESS_INSTANCE_IDENTITY=PASS_BUILDER
RESTART_INVALIDATES_DISPATCHABILITY=PASS_BUILDER
UTC_ROLLBACK_CANNOT_EXTEND_VALIDITY=PASS_BUILDER
MONOTONIC_CROSS_PROCESS_REUSE_BLOCKED=PASS_BUILDER
NEW_COMMAND_AND_GRANT_AFTER_RESTART=PASS_BUILDER
DEFERRED_REQUIREMENTS_RECONCILED=1/1
V27_SAF_008_ASSIGNMENT=PASS_BUILDER_REMEDIATED
INDIVIDUAL_TRACEABILITY=PASS_BUILDER_REMEDIATED
NUMERIC_SKEW_LIMIT_DEFINED=NO
RUNTIME_TEST_EXECUTED=NO
```

## Fora de escopo

- biblioteca de relógio;
- limites numéricos de skew;
- sincronização NTP;
- implementação de IDs;
- execução de crash/restart.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW` até `LEA-31=PASS`, autorização humana de merge e confirmação pós-merge.