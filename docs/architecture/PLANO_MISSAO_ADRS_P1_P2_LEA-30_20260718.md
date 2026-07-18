# PLANO DA MISSÃO — ADRs P1/P2 DA ARQUITETURA V1.0

## LEA-30 — Formalização das decisões arquiteturais complementares

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_IN_PROGRESS
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=dff0c0f0c26e820756804af92dd7b3641121d51b
STATE_REVISION_BASE=12
TRANSITION_ID=LEA-30-T01
MISSION_SCOPE=DOCUMENTATION_ONLY
HUMAN_AUTHORIZATION=RECEIVED_2026-07-18
MERGE_AUTHORIZED=NO
```

Este documento planeja conteúdo arquitetural. O estado operacional vigente permanece em `PROJECT_RUNTIME_STATE.yaml`, GitHub e Linear.

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
4. auto-revisão preliminar;
5. prompt e issue de revisão independente;
6. manifesto, estado humano, tronco e README sincronizados no PR;
7. PR Draft sem autorização de merge.

## 7. Gates

```text
B1_PRECONDITIONS=PASS
B2_PLAN_AND_NUMBERING=PASS
B3_P1_P2_ADRS=IN_PROGRESS
B4_TRACEABILITY=IN_PROGRESS
B5_CROSS_ADR_CONSISTENCY=IN_PROGRESS
B6_BUILDER_SELF_REVIEW=PENDING
B7_INDEPENDENT_CRITICAL_REVIEW=REQUIRED
MISSION_GATES=2/7
```

## 8. Limites

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

## 9. Rollback documental

A branch pode ser descartada sem alterar a `main`. Nenhum ADR muda runtime, banco físico, infraestrutura, credenciais, interface real ou efeito financeiro.

## 10. Próxima ação

Produzir os seis ADRs, validar rastreabilidade e publicar PR Draft para `LEA-31`.