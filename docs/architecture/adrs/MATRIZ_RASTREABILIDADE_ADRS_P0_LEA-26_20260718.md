# MATRIZ DE RASTREABILIDADE — ADRs P0

## LEA-26 — Arquitetura V1.0

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_TRACEABILITY_REMEDIATED_READY_FOR_RETEST_01
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
TRANSITION_ID=LEA-26-T01
ADR_COUNT=12/12
CANONICAL_DOMAIN_COUNT=16
MANDATORY_HANDOFF_COUNT=12
CROSS_VERSION_REQUIREMENTS=218
NEW_REQUIREMENT_IDS=0
IMPLEMENTATION_AUTHORIZED=NO
```

Esta matriz é o resumo por ADR, domínio e handoff. A prova requisito a requisito está no apêndice exaustivo:

`APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md`.

## 2. Cobertura por ADR

| ADR | Domínios primários | Domínios secundários | Handoffs | Grupos/IDs principais |
|---|---|---|---|---|
| ADR-0001 | DOM-01 | DOM-03, 05, 16 | H-01..12 | PTM-V25-018; V25-SRV-*; V25-DOC-001; PTM-V27-032 |
| ADR-0002 | DOM-03 | DOM-01, 15, 16 | H-11 | PTM-V25-003; PTM-V25-014A..E; V25-DB-*; V25-LEG-*; V26-API-*; PTM-V27-029 |
| ADR-0003 | DOM-01, 03 | DOM-05, 16 | H-01..12 | V25-SRV-*; V26-API-*; V27-OBS-* |
| ADR-0004 | DOM-05 | DOM-01, 02, 13, 16 | H-01, H-12 | PTM-V25-008/009; PTM-V27-020; V25-CFG-*; V27-AUT-* |
| ADR-0005 | DOM-06 | DOM-07, 08, 09, 14, 16 | H-02,03,04,09,10 | PTM-V25-010; PTM-V25-011A..D; alvo lógico e geometria V2.7 |
| ADR-0006 | DOM-11 | DOM-09, 10, 12, 16 | H-06, H-07 | PTM-V26-001; PTM-V26-009..018; V26-ANA-* |
| ADR-0007 | DOM-12 | DOM-04, 09, 11, 13, 16 | H-07, H-08 | PTM-V26-019..022; V26-STR-*; V26-SIG-* |
| ADR-0008 | DOM-13, 15 | DOM-01, 12, 14, 16 | H-08..12 | comando, grant, arming, tentativa e recovery |
| ADR-0009 | DOM-14 | DOM-02, 06, 13, 15, 16 | H-09..12 | adaptadores, alvo e separação A/B |
| ADR-0010 | DOM-16 | DOM-01, 13, 14, 15 | H-10..12 | kill switch, epoch e contenção |
| ADR-0011 | DOM-15 | DOM-03, 13, 14, 16 | H-10..12 | tentativa, idempotência, recibo e reconciliação |
| ADR-0012 | DOM-16 | DOM-01..15 | H-01..12 | logs, métricas, auditoria e redaction |

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

A tabela registra decisão, governança ou auditoria; não transfere propriedade funcional integral.

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

## 5. Decisões posteriores

```text
P1=ADR-CAND-003|007|013|016|018
P2=ADR-CAND-017
```

O apêndice individual classifica cada requisito sem ADR P0 como `GOVERNED_BY` ou `DEFERRED_WITH_REASON`.

## 6. Validação do builder

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
TRACEABILITY_STATUS=PASS_BUILDER_AFTER_MAJOR_01
```

## 7. Próxima ação

Executar `LEA-27 — Reteste 01` sobre o HEAD final vivo do PR #46.