# MATRIZ DE RASTREABILIDADE — ADRs P0

## LEA-26 — Arquitetura V1.0

## 1. Controle

```text
DOCUMENT_STATUS=CONTENT_APPROVED_RETEST_03_AWAITING_MERGE_AUTHORIZATION
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
TRANSITION_ID=LEA-26-T01
ADR_COUNT=12/12
CANONICAL_DOMAIN_COUNT=16
MANDATORY_HANDOFF_COUNT=12
CROSS_VERSION_REQUIREMENTS=218
NEW_REQUIREMENT_IDS=0
RETEST_SEQUENCE=03
ADR_P0_CRITICAL_REVIEW=PASS
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
```

Esta matriz resume ADR, domínio e handoff. A prova requisito a requisito permanece no apêndice exaustivo. O estado operacional vigente é obtido do manifesto, do estado humano, do PR #46 e do Linear.

## 2. Cobertura por ADR

| ADR | Domínios primários | Domínios secundários | Handoffs | Grupos/IDs principais |
|---|---|---|---|---|
| ADR-0001 | DOM-01 | DOM-03, 05, 16 | H-01..12 | autoridade global e servidor |
| ADR-0002 | DOM-03 | DOM-01, 15, 16 | H-11 | persistência e escritor único |
| ADR-0003 | DOM-01, 03 | DOM-05, 16 | H-01..12 | REST, SSE e versionamento |
| ADR-0004 | DOM-05 | DOM-01, 02, 13, 16 | H-01, H-12 | identidade e pareamento |
| ADR-0005 | DOM-06 | DOM-07, 08, 09, 14, 16 | H-02,03,04,09,10 | perfil, ROI e alvo lógico |
| ADR-0006 | DOM-11 | DOM-09, 10, 12, 16 | H-06, H-07 | motores A–H |
| ADR-0007 | DOM-12 | DOM-04, 09, 11, 13, 16 | H-07, H-08 | estratégias e sinais |
| ADR-0008 | DOM-13, 15 | DOM-01, 12, 14, 16 | H-08..12 | comando, grant, arming e tentativa |
| ADR-0009 | DOM-14 | DOM-02, 06, 13, 15, 16 | H-09..12 | adaptadores e separação A/B |
| ADR-0010 | DOM-16 | DOM-01, 13, 14, 15 | H-10..12 | kill switch e epoch |
| ADR-0011 | DOM-15 | DOM-03, 13, 14, 16 | H-10..12 | idempotência e reconciliação |
| ADR-0012 | DOM-16 | DOM-01..15 | H-01..12 | observabilidade e redaction |

## 3. Cobertura dos domínios

```text
DOM_01=ADR-0001|0002|0003|0004|0008|0010|0012
DOM_02=ADR-0004|0009|0012
DOM_03=ADR-0001|0002|0003|0011|0012
DOM_04=ADR-0007|0012
DOM_05=ADR-0001|0003|0004|0012
DOM_06=ADR-0005|0009|0012
DOM_07=ADR-0005|0012
DOM_08=ADR-0005|0012
DOM_09=ADR-0005|0006|0007|0012
DOM_10=ADR-0006|0012
DOM_11=ADR-0006|0007|0012
DOM_12=ADR-0006|0007|0008|0012
DOM_13=ADR-0004|0007|0008|0009|0010|0011|0012
DOM_14=ADR-0005|0008|0009|0010|0011|0012
DOM_15=ADR-0001|0002|0008|0009|0010|0011|0012
DOM_16=ADR-0001..0012
DOMAIN_COVERAGE=16/16
```

## 4. Handoffs e ADRs vinculados

| Handoff | ADRs vinculados | Observação |
|---|---|---|
| H-01 | ADR-0001, 0003, 0004, 0012 | autoridade, transporte, cliente e auditoria |
| H-02 | ADR-0005, 0012 | perfil aprovado e auditoria |
| H-03 | ADR-0005, 0012 | identidade visual e auditoria |
| H-04 | ADR-0005, 0012 | perfil/proveniência e auditoria |
| H-05 | ADR-0012 | contrato funcional no mapa consolidado; auditoria transversal P0 |
| H-06 | ADR-0006, 0012 | snapshot analítico e auditoria |
| H-07 | ADR-0006, 0007, 0012 | análise, estratégia e auditoria |
| H-08 | ADR-0007, 0008, 0012 | sinal, comando e auditoria |
| H-09 | ADR-0005, 0008, 0009, 0012 | alvo, grant, adaptador e auditoria |
| H-10 | ADR-0005, 0008, 0009, 0010, 0011, 0012 | dispatch, kill e reconciliação |
| H-11 | ADR-0002, 0008, 0009, 0010, 0011, 0012 | persistência, tentativa e reconciliação |
| H-12 | ADR-0001, 0004, 0008, 0009, 0010, 0011, 0012 | autoridade, presença, estados e contenção |

## 5. Validação

```text
ADR_COUNT_MATCH=PASS
P0_CANDIDATES_MAPPED=12/12
DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
REQUIREMENT_ROWS=218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
UNJUSTIFIED_NO_P0_MAPPING=0
H05_FALSE_CONTROLLER_ASSIGNMENT=REMOVED
MODE_A_MODE_B_SEPARATION=PASS
TRACEABILITY_STATUS=PASS
RETEST_03=PASS
```

## 6. Próxima ação

Aguardar nova autorização humana explícita para o HEAD final sincronizado. O `PASS_RETEST_03` não reutiliza a autorização vinculada ao HEAD anterior.