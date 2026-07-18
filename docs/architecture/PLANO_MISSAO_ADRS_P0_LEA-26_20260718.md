# PLANO DA MISSÃO — ADRs P0 DA ARQUITETURA V1.0

## LEA-26 — Formalização das decisões arquiteturais prioritárias

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DELIVERY_READY_FOR_INDEPENDENT_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
PULL_REQUEST=46
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=c339ef253c2558300388901a67faf18734e2735f
STATE_REVISION=9
TRANSITION_ID=LEA-26-T01
PREVIOUS_TRANSITION=LEA-18-T01_COMPLETE
MISSION_SCOPE=DOCUMENTATION_ONLY
HUMAN_AUTHORIZATION=RECEIVED_2026-07-18
```

## 2. Objetivo

Converter as 12 decisões P0 do catálogo consolidado em ADRs formais, coerentes entre si e rastreáveis aos 16 domínios, 12 handoffs e 218 requisitos aprovados.

Os documentos foram produzidos com status `PROPOSED_FOR_REVIEW`. Nenhum ADR se torna definitivo antes da revisão crítica independente da LEA-27, autorização humana de merge e confirmação pós-merge.

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
| ADR-0008 | ADR-CAND-010 | máquina de estados de comando e execução |
| ADR-0009 | ADR-CAND-011 | adaptadores e separação Modo A/Modo B |
| ADR-0010 | ADR-CAND-012 | kill switch dominante |
| ADR-0011 | ADR-CAND-014 | recibo e reconciliação multidimensional |
| ADR-0012 | ADR-CAND-015 | observabilidade, auditoria e redaction |

## 4. Dependências de decisão

```text
ADR-0001 -> ADR-0002|ADR-0003|ADR-0004|ADR-0008|ADR-0010|ADR-0012
ADR-0002 -> ADR-0003|ADR-0011|ADR-0012
ADR-0005 -> ADR-0009
ADR-0006 -> ADR-0007
ADR-0007 -> ADR-0008
ADR-0008 -> ADR-0009|ADR-0010|ADR-0011
ADR-0009 -> ADR-0011
ADR-0010 -> ADR-0008|ADR-0009|ADR-0011
ADR-0011 -> ADR-0012
```

A dependência define coerência documental, não ordem automática de implementação.

## 5. Gates

```text
A1_PRECONDITIONS=PASS
A2_TEMPLATE_AND_INDEX=PASS
A3_P0_ADRS=12/12
A4_TRACEABILITY=PASS_BUILDER
A5_CROSS_ADR_CONSISTENCY=PASS_BUILDER
A6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY
A7_INDEPENDENT_CRITICAL_REVIEW=REQUIRED
```

## 6. Critérios de qualidade aplicados

Cada ADR contém:

1. contexto e problema;
2. decisão objetiva;
3. alternativas rejeitadas;
4. consequências positivas e negativas;
5. invariantes de segurança, recovery e autoridade;
6. domínios, handoffs e requisitos relacionados;
7. critérios verificáveis de aceitação;
8. itens explicitamente fora de escopo.

## 7. Limites da missão

```text
CODE_CHANGE_AUTHORIZED=NO
TEST_CODE_CHANGE_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
DOCUMENT_MASTER_START_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
REAL_FINANCIAL_EFFECT_RUNTIME_AUTHORIZED=NO
```

A missão define contratos e decisões arquiteturais. Ela não produz implementação, schema físico, migration, credencial, integração de produção ou sessão LIVE.

## 8. Política A+B

```text
MODE_A_POLICY=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_ADAPTER_IMPLEMENTATION=OUT_OF_SCOPE
LIVE_SESSION_ARMING=PROHIBITED_IN_THIS_MISSION
FINANCIAL_EFFECT=BLOCKED_UNTIL_ALL_LIVE_GATES_PASS
```

## 9. Condição de handoff

```text
ADR_P0_COUNT=12/12
ADR_STATUS=PROPOSED_FOR_REVIEW
TRACEABILITY_MATRIX=PASS_BUILDER
CROSS_ADR_CONSISTENCY=PASS_BUILDER
BUILDER_SELF_REVIEW=PASS_PRELIMINARY
PR_STATUS=READY_FOR_INDEPENDENT_REVIEW
MERGE_AUTHORIZED=NO
```

A próxima etapa é a revisão crítica independente da LEA-27.