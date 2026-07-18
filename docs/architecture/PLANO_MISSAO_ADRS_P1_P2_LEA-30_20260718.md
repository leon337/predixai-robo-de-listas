# PLANO DA MISSÃO — ADRs P1/P2 DA ARQUITETURA V1.0

## LEA-30 — Formalização das decisões arquiteturais complementares

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_REMEDIATED_READY_FOR_RETEST_01
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=dff0c0f0c26e820756804af92dd7b3641121d51b
STATE_REVISION_BASE=12
TRANSITION_ID=LEA-30-T01
MISSION_SCOPE=DOCUMENTATION_ONLY
HUMAN_AUTHORIZATION=RECEIVED_2026-07-18
INITIAL_REVIEWED_HEAD=8ca08eaee367140a67ede7082e315b2844beab06
INITIAL_REVIEW_RESULT=FAIL_3_MAJOR
REMEDIATION_STATUS=COMPLETE_BUILDER
RETEST_REQUIRED=YES
MERGE_AUTHORIZED=NO
```

Este documento registra o plano e o estado corrente da entrega documental. O estado operacional autoritativo permanece em `PROJECT_RUNTIME_STATE.yaml`, GitHub e Linear.

## 2. Objetivo

Converter os cinco candidatos P1 e o candidato P2 remanescentes do catálogo consolidado em seis ADRs formais, coerentes com os 12 ADRs P0 publicados e preparados para revisão crítica independente.

Os ADRs permanecem `PROPOSED_FOR_REVIEW` até `LEA-31=PASS`, autorização humana de merge e confirmação pós-merge.

## 3. ADRs da missão

| ADR | Prioridade | Candidato | Decisão |
|---|---|---|---|
| ADR-0013 | P1 | ADR-CAND-003 | migrations, compatibilidade e importação idempotente do legado |
| ADR-0014 | P1 | ADR-CAND-007 | retenção de frames, recortes e evidências visuais |
| ADR-0015 | P1 | ADR-CAND-013 | idempotência de dispatch, serialização e circuit breaker |
| ADR-0016 | P1 | ADR-CAND-016 | relógios, deadlines e identidade de processo |
| ADR-0017 | P2 | ADR-CAND-017 | thresholds e limites numéricos versionados |
| ADR-0018 | P1 | ADR-CAND-018 | estratégia de testes e evidência por camada |

## 4. Semântica das relações

```text
DEPENDS_ON=PRE_REQUISITO_ACICLICO
MUST_ALIGN_WITH=COERENCIA_BIDIRECIONAL_SEM_ORDEM
GOVERNS=DECISAO_QUE_RESTRINGE_OUTRA
```

## 5. Grafo autoritativo proposto

```text
ADR-0013=ADR-0002
ADR-0014=ADR-0005|ADR-0012
ADR-0015=ADR-0008|ADR-0009|ADR-0010|ADR-0011
ADR-0016=ADR-0008|ADR-0010|ADR-0011
ADR-0017=ADR-0005|ADR-0006|ADR-0007|ADR-0012
ADR-0018=ADR-0003|ADR-0008|ADR-0009|ADR-0010|ADR-0011|ADR-0012|ADR-0013|ADR-0014|ADR-0015|ADR-0016|ADR-0017
```

```text
TOPOLOGICAL_ORDER=ADR-0013|ADR-0014|ADR-0015|ADR-0016|ADR-0017|ADR-0018
P1_P2_NODE_COUNT=6
P1_P2_DEPENDS_ON_CYCLE_COUNT=0
P1_P2_DEPENDS_ON_DAG=PASS_BUILDER
```

## 6. Entregas

1. seis ADRs completos;
2. índice e grafo de dependências atualizados;
3. matriz de rastreabilidade P1/P2;
4. apêndice de rastreabilidade individual P1/P2;
5. auto-revisão preliminar;
6. prompt e issue de revisão independente;
7. manifesto, estado humano, tronco e README sincronizados no PR;
8. PR Draft sem autorização de merge.

## 7. Revisão LEA-31 e remediação

A primeira revisão independente avaliou o HEAD `8ca08eaee367140a67ede7082e315b2844beab06` e registrou três achados MAJOR.

```text
MAJOR_01_TRACEABILITY=REMEDIATED_BUILDER
MAJOR_02_PLAN_STATE_SYNC=REMEDIATED_BUILDER
MAJOR_03_LINEAR_DEPENDENCY_CYCLE=REMEDIATED
CRITICAL_FINDINGS=0
OPEN_FINDINGS_BUILDER_VIEW=0
INDEPENDENT_RETEST_REQUIRED=YES
```

Evidências:

- `docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_ADRS_P1_P2_LEA-30_20260718.md`;
- `docs/architecture/adrs/MATRIZ_RASTREABILIDADE_ADRS_P1_P2_LEA-30_20260718.md`;
- seis ADRs com separação entre requisitos diferidos e complementares;
- relação circular `LEA-30 blocks LEA-31` removida no Linear.

## 8. Gates

```text
B1_PRECONDITIONS=PASS
B2_PLAN_AND_NUMBERING=PASS
B3_P1_P2_ADRS=6/6
B4_TRACEABILITY=PASS_BUILDER_REMEDIATED
B5_CROSS_ADR_CONSISTENCY=PASS_BUILDER_REMEDIATED
B6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY_REMEDIATED
B7_INDEPENDENT_CRITICAL_REVIEW=RETEST_01_REQUIRED
MISSION_GATES=6/7
```

## 9. Limites

```text
CODE_CHANGE_AUTHORIZED=NO
TEST_CODE_CHANGE_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
RUNTIME_TEST_EXECUTION=NO
MERGE_AUTHORIZED=NO
DOCUMENT_MASTER_START_AUTHORIZED=NO
MODE_A_POLICY=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_MODE_ARMED=NO
FINANCIAL_EFFECT=BLOCKED_UNTIL_ALL_LIVE_GATES_PASS
```

## 10. Rollback documental

A branch pode ser descartada sem alterar a `main`. Nenhum ADR muda runtime, banco físico, infraestrutura, credenciais, interface real ou efeito financeiro.

## 11. Próxima ação

```text
NEXT_ACTION=EXECUTE_LEA_31_RETEST_01_ON_NEW_PR_49_HEAD
AUTOMATIC_MERGE=NO
DOCUMENT_MASTER_START=NO
```
