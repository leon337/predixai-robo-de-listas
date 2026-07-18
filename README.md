# PredixAI Robô de Listas

> Painel operacional, histórico arquitetural e mapa da campanha.
>
> O README é projeção derivada. A autoridade operacional permanece em `PROJECT_RUNTIME_STATE.yaml`.

## 📍 Estado atual

```text
VERSÃO_REAL=V2.4.3-R1
MISSÃO_ATIVA=LEA-26 — ADRs P0 da Arquitetura V1.0
REVISÃO_ATIVA=LEA-27 — RETESTE_03
PULL_REQUEST=46
PR_STATUS=DRAFT
OBSERVED_PR_HEAD=decb578bd9b4c4bbe9d62947359eb59569d89020
LIVE_PR_HEAD_SOURCE=GITHUB_API
SNAPSHOT_CONTENT_HEAD=6f1ac10005e7231e9efe88da9c7a27931038a989
FASE=SCHEMA_AND_SOURCE_AUTHORITY_REMEDIATION
GATE=A7_INDEPENDENT_CRITICAL_REVIEW_RETEST_03
STATE_REVISION=11
MERGE_AUTORIZADO=NO
DOCUMENTO_MESTRE_AUTORIZADO=NO
IMPLEMENTAÇÃO_AUTORIZADA=NO
LIVE_MODE_ARMED=NO
```

## ⛔ Bloqueio pré-merge

A autorização recebida para o HEAD `decb578bd9b4c4bbe9d62947359eb59569d89020` não foi executada. A verificação imediatamente anterior ao merge encontrou duas threads novas:

```text
FINDING_01=PROJECT_RUNTIME_STATE_SCHEMA_1_0_3_INCOMPATIBILITY
FINDING_02=STALE_OPERATIONAL_RETEST_REFERENCES_IN_ADR_SOURCES
OPEN_REVIEW_THREADS_AT_BLOCK=2
MERGE_EXECUTED=NO
```

As correções alteram o HEAD. Portanto, o novo HEAD exigirá Reteste 03 `PASS` e nova autorização humana explícita de merge.

## 🔧 Remediação

```text
SCHEMA_VERSION=1.0.3
TOP_LEVEL_OBSERVED_PR_HEAD=RESTORED
MISSION_LOCK_OBSERVED_PR_HEAD=RESTORED
TRANSITION_STATUS=SCHEMA_ENUM_COMPATIBLE
SYNC_STATUS=SCHEMA_ENUM_COMPATIBLE
GATE_STATUS=SCHEMA_ENUM_COMPATIBLE
EXECUTION_STATUS=SCHEMA_ENUM_COMPATIBLE
OPERATIONAL_SOURCE_AUTHORITY=REFRESHED
STALE_ARCHITECTURE_STATUS=CONTENT_EVIDENCE_NOT_OPERATIONAL_GATE
```

## 📊 Revisões

```text
INITIAL_REVIEW=FAIL
RETEST_01=FAIL
RETEST_02=PASS_REVOKED_BY_NEW_PRE_MERGE_FINDINGS
RETEST_03=IN_PROGRESS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS_OPEN=2
DOCUMENTAL_READY_FOR_MERGE=NO
RETEST_REQUIRED=YES
```

As quatro correções maiores permanecem aprovadas:

```text
MAJOR_01_TRACEABILITY_218=PASS
MAJOR_02_DEPENDENCY_DAG=PASS
MAJOR_03_FOUR_FSMS=PASS
MAJOR_04_IDEMPOTENCY_COLLISION=PASS
```

## 🧱 ADRs P0

| ADR | Decisão | Estado |
|---|---|---|
| [ADR-0001](docs/architecture/adrs/ADR-0001-SERVIDOR-E-AUTORIDADE-DE-ESTADO.md) | servidor e autoridade global | proposto |
| [ADR-0002](docs/architecture/adrs/ADR-0002-PERSISTENCIA-E-ESCRITOR-UNICO.md) | persistência e escritor único | proposto |
| [ADR-0003](docs/architecture/adrs/ADR-0003-CONTRATOS-REST-EVENTOS-E-VERSIONAMENTO.md) | REST, eventos e versionamento | proposto |
| [ADR-0004](docs/architecture/adrs/ADR-0004-IDENTIDADE-PAREAMENTO-E-CLIENTES.md) | identidade e pareamento | proposto |
| [ADR-0005](docs/architecture/adrs/ADR-0005-PERFIS-ROIS-E-ALVO-LOGICO.md) | perfis, ROIs e alvo lógico | proposto |
| [ADR-0006](docs/architecture/adrs/ADR-0006-MOTORES-A-H-E-ENVELOPE-DE-ANALISE.md) | motores A–H | proposto |
| [ADR-0007](docs/architecture/adrs/ADR-0007-ESTRATEGIAS-E-LIFECYCLE-DE-SINAIS.md) | estratégias e sinais | proposto |
| [ADR-0008](docs/architecture/adrs/ADR-0008-MAQUINA-DE-ESTADOS-DE-COMANDO-E-EXECUCAO.md) | quatro FSMs | proposto remediado |
| [ADR-0009](docs/architecture/adrs/ADR-0009-ADAPTADORES-E-SEPARACAO-DOS-MODOS-A-B.md) | adaptadores e separação A/B | proposto remediado |
| [ADR-0010](docs/architecture/adrs/ADR-0010-KILL-SWITCH-DOMINANTE.md) | kill switch dominante | proposto remediado |
| [ADR-0011](docs/architecture/adrs/ADR-0011-RECIBO-E-RECONCILIACAO-MULTIDIMENSIONAL.md) | idempotência e reconciliação | proposto remediado |
| [ADR-0012](docs/architecture/adrs/ADR-0012-OBSERVABILIDADE-AUDITORIA-E-REDACTION.md) | observabilidade e auditoria | proposto |

## 🔗 Métricas preservadas

```text
REQUIREMENT_ROWS=218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
UNJUSTIFIED_NO_P0_MAPPING=0
CANONICAL_DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
DEPENDS_ON_NODE_COUNT=12
DEPENDS_ON_CYCLE_COUNT=0
COMMAND_FSM=DEFINED
AUTHORIZATION_GRANT_FSM=DEFINED
SESSION_ARMING_FSM=DEFINED
EXECUTION_ATTEMPT_FSM=DEFINED
SAME_KEY_AND_DIFFERENT_CANONICAL_FINGERPRINT=BLOCK_CONFLICT_AND_AUDIT
```

## 🎛️ Política A+B

```text
MODE_A=CONTROLLED_OR_SIMULATED_ALLOWED
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
AUTO_ENABLE=PROHIBITED
LIVE_WITHOUT_ALL_GATES=BLOCKED
```

Nenhuma sessão LIVE, operação real ou implementação foi autorizada.

## 🧾 Fontes operacionais

- `PROJECT_RUNTIME_STATE.yaml`;
- `docs/protocols/PROJECT_RUNTIME_STATE_SCHEMA.yaml`;
- `PROJECT_STATE.md`;
- `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
- `docs/history/reviews/REMEDIACAO_SCHEMA_E_FONTES_ADRS_P0_LEA-26_20260718.md`;
- PR #46 vivo;
- Linear LEA-26 e LEA-27.

Plano, índice, matriz e apêndice preservam o conteúdo arquitetural. Status operacionais antigos nesses artefatos não substituem as fontes acima.

## 🗺️ Próxima sequência

```text
1. concluir remediação do schema e das fontes
2. responder e resolver as duas threads
3. confirmar CI 9/9
4. executar LEA-27 Reteste 03
5. obter PASS sem achados
6. solicitar nova autorização humana para o novo HEAD
7. integrar PR #46
8. publicar recibo pós-merge
```

```text
NEXT_ACTION=COMPLETE_REMEDIATION_AND_EXECUTE_LEA_27_RETEST_03
```