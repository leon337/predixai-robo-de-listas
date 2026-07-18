# PLANO DA MISSÃO — ADRs P0 DA ARQUITETURA V1.0

## LEA-26 — Formalização das decisões arquiteturais prioritárias

## 1. Controle

```text
DOCUMENT_STATUS=CONTENT_COMPLETE_OPERATIONAL_HANDOFF_RETEST_03
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
PULL_REQUEST=46
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=c339ef253c2558300388901a67faf18734e2735f
STATE_REVISION=11
TRANSITION_ID=LEA-26-T01
MISSION_SCOPE=DOCUMENTATION_ONLY
RETEST_SEQUENCE=03
MERGE_AUTHORIZED=NO
```

Este documento define conteúdo arquitetural. O status operacional vigente deve ser obtido de `PROJECT_RUNTIME_STATE.yaml`, `PROJECT_STATE.md`, PR #46 e Linear.

## 2. Objetivo

Converter as 12 decisões P0 do catálogo consolidado em ADRs formais, coerentes entre si e rastreáveis aos 16 domínios, 12 handoffs e 218 requisitos aprovados.

Os ADRs permanecem `PROPOSED_FOR_REVIEW` até revisão crítica independente válida para o HEAD atual, autorização humana de merge e confirmação pós-merge.

## 3. ADRs da missão

| ADR | Candidato | Decisão |
|---|---|---|
| ADR-0001 | ADR-CAND-001 | servidor e autoridade de estado |
| ADR-0002 | ADR-CAND-002 | persistência e escritor único |
| ADR-0003 | ADR-CAND-004 | REST, eventos e versionamento |
| ADR-0004 | ADR-CAND-005 | identidade, pareamento e clientes |
| ADR-0005 | ADR-CAND-006 | perfis, ROIs e alvo lógico |
| ADR-0006 | ADR-CAND-008 | motores A–H e envelope de análise |
| ADR-0007 | ADR-CAND-009 | estratégias e lifecycle de sinais |
| ADR-0008 | ADR-CAND-010 | FSMs de comando, grant, arming e tentativa |
| ADR-0009 | ADR-CAND-011 | adaptadores e separação Modo A/Modo B |
| ADR-0010 | ADR-CAND-012 | kill switch dominante |
| ADR-0011 | ADR-CAND-014 | recibo, idempotência e reconciliação |
| ADR-0012 | ADR-CAND-015 | observabilidade, auditoria e redaction |

## 4. Semântica das relações

```text
DEPENDS_ON=PRE_REQUISITO_ACICLICO
MUST_ALIGN_WITH=COERENCIA_BIDIRECIONAL_SEM_ORDEM
GOVERNS=DECISAO_QUE_RESTRINGE_OUTRA
```

## 5. Grafo autoritativo de `DEPENDS_ON`

```text
ADR-0001=NONE
ADR-0002=ADR-0001
ADR-0003=ADR-0001|ADR-0002
ADR-0004=ADR-0001|ADR-0003
ADR-0005=ADR-0001
ADR-0006=ADR-0001|ADR-0003
ADR-0007=ADR-0006
ADR-0008=ADR-0001|ADR-0002|ADR-0007
ADR-0010=ADR-0001|ADR-0002
ADR-0009=ADR-0005|ADR-0008|ADR-0010
ADR-0011=ADR-0002|ADR-0008|ADR-0009|ADR-0010
ADR-0012=ADR-0001|ADR-0002|ADR-0003|ADR-0008|ADR-0010|ADR-0011
```

```text
TOPOLOGICAL_ORDER=ADR-0001|ADR-0002|ADR-0003|ADR-0004|ADR-0005|ADR-0006|ADR-0007|ADR-0008|ADR-0010|ADR-0009|ADR-0011|ADR-0012
DEPENDS_ON_NODE_COUNT=12
DEPENDS_ON_CYCLE_COUNT=0
DEPENDS_ON_DAG=PASS
```

## 6. Rastreabilidade

```text
P0_ADR_COUNT=12/12
CANONICAL_DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
REQUIREMENT_ROWS=218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
UNJUSTIFIED_NO_P0_MAPPING=0
```

## 7. Gates

```text
A1_PRECONDITIONS=PASS
A2_TEMPLATE_AND_INDEX=PASS
A3_P0_ADRS=12/12
A4_TRACEABILITY=PASS
A5_CROSS_ADR_CONSISTENCY=PASS
A6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY
A7_INDEPENDENT_CRITICAL_REVIEW=RETEST_03_REQUIRED
```

O `PASS_RETEST_02` foi invalidado por dois achados novos detectados na verificação pré-merge: incompatibilidade do manifesto com o schema 1.0.3 e referências operacionais antigas nas fontes arquiteturais.

## 8. Limites

```text
CODE_CHANGE_AUTHORIZED=NO
TEST_CODE_CHANGE_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
DOCUMENT_MASTER_START_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
FINANCIAL_EFFECT=BLOCKED_UNTIL_ALL_LIVE_GATES_PASS
```

## 9. Próxima ação

Executar `LEA-27 — Reteste 03` sobre o novo HEAD vivo do PR #46. Um eventual `PASS` exigirá nova autorização humana explícita de merge porque o HEAD anteriormente autorizado foi alterado.