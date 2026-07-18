# MATRIZ DE RASTREABILIDADE — ADRs P0

## LEA-26 — Arquitetura V1.0

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_TRACEABILITY_READY_FOR_REVIEW
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

## 2. Cobertura por ADR

| ADR | Domínios primários | Domínios secundários | Handoffs | Grupos/IDs principais |
|---|---|---|---|---|
| ADR-0001 | DOM-01 | DOM-03, 05, 16 | H-01..12 | PTM-V25-018; V25-SRV-001..004; V25-DOC-001; PTM-V27-032 |
| ADR-0002 | DOM-03 | DOM-01, 15, 16 | H-11 | PTM-V25-003; PTM-V25-014A..E; V25-DB-*; V25-LEG-*; V26-API-*; PTM-V27-029 |
| ADR-0003 | DOM-01, 03 | DOM-05, 16 | H-01..12 | V25-SRV-*; V26-API-*; PTM-V26-023/027; V27-OBS-* |
| ADR-0004 | DOM-05 | DOM-01, 02, 13, 16 | H-01, H-12 | PTM-V25-008/009; PTM-V27-020; V25-CFG-*; V27-AUT-* |
| ADR-0005 | DOM-06 | DOM-07, 08, 09, 14, 16 | H-02,03,04,09,10 | PTM-V25-010; PTM-V25-011A..D; PTM-V27-003/008/009/021; V27-EXE-003/004; V27-SAF-006 |
| ADR-0006 | DOM-11 | DOM-09, 10, 12, 16 | H-06, H-07 | PTM-V26-001; PTM-V26-009..018; V26-ANA-* |
| ADR-0007 | DOM-12 | DOM-04, 09, 11, 13, 16 | H-07, H-08 | PTM-V26-019..022; V26-STR-*; V26-SIG-* |
| ADR-0008 | DOM-13, 15 | DOM-01, 12, 14, 16 | H-08..12 | PTM-V27-001..007; V27-PRE-*; V27-CMD-*; V27-AUT-*; PTM-V27-010..018/022..025; V27-REC-* |
| ADR-0009 | DOM-14 | DOM-02, 06, 13, 15, 16 | H-09..12 | PTM-V27-003/008/009/021/032; V27-EXE-003/004; V27-SAF-006 |
| ADR-0010 | DOM-16 | DOM-01, 13, 14, 15 | H-10..12 | V27-EXE-008; V27-SAF-004/005/007; PTM-V27-019/026..028; V27-QA-* |
| ADR-0011 | DOM-15 | DOM-03, 13, 14, 16 | H-10..12 | PTM-V27-010..018/022..025/030; V27-EXE-001/002/005..007; V27-REC-* |
| ADR-0012 | DOM-16 | DOM-01..15 | H-01..12 | PTM-V25-015A..E; V25-SEC-*; V25-QA-*; PTM-V26-024..026/028; V26-RPL-*; V26-SEC-*; PTM-V27-019/026..031; V27-OBS-*; V27-QA-* |

## 3. Cobertura dos domínios

| Domínio | ADRs com responsabilidade primária ou secundária |
|---|---|
| DOM-01 | ADR-0001, 0002, 0003, 0004, 0008, 0010, 0012 |
| DOM-02 | ADR-0004, 0009, 0012 |
| DOM-03 | ADR-0001, 0002, 0003, 0011, 0012 |
| DOM-04 | ADR-0007, 0012 |
| DOM-05 | ADR-0001, 0003, 0004, 0012 |
| DOM-06 | ADR-0005, 0009, 0012 |
| DOM-07 | ADR-0005, 0012 |
| DOM-08 | ADR-0005, 0012 |
| DOM-09 | ADR-0005, 0006, 0007, 0012 |
| DOM-10 | ADR-0006, 0012 |
| DOM-11 | ADR-0006, 0007, 0012 |
| DOM-12 | ADR-0006, 0007, 0008, 0012 |
| DOM-13 | ADR-0004, 0007, 0008, 0009, 0010, 0011, 0012 |
| DOM-14 | ADR-0005, 0008, 0009, 0010, 0011, 0012 |
| DOM-15 | ADR-0001, 0002, 0008, 0009, 0010, 0011, 0012 |
| DOM-16 | ADR-0001..0012 |

Todos os 16 domínios possuem vínculo com ao menos um ADR P0. Isso não significa que toda decisão P1/P2 esteja resolvida.

## 4. Handoffs e ADRs vinculados

A tabela registra vínculo de decisão, governança ou auditoria. Ela não atribui automaticamente propriedade funcional integral do handoff ao ADR listado.

| Handoff | ADRs vinculados | Observação |
|---|---|---|
| H-01 | ADR-0001, 0003, 0004, 0012 | autoridade, transporte, cliente e auditoria |
| H-02 | ADR-0005, 0012 | perfil aprovado e auditoria |
| H-03 | ADR-0005, 0012 | identidade visual e auditoria |
| H-04 | ADR-0005, 0012 | perfil/proveniência e auditoria |
| H-05 | ADR-0012 | contrato funcional permanece no mapa consolidado; ADR P0 cobre auditoria transversal |
| H-06 | ADR-0006, 0012 | entrada do snapshot analítico e auditoria |
| H-07 | ADR-0006, 0007, 0012 | análise, estratégia e auditoria |
| H-08 | ADR-0007, 0008, 0012 | sinal, comando e auditoria |
| H-09 | ADR-0005, 0008, 0009, 0012 | alvo, grant, adaptador e auditoria |
| H-10 | ADR-0005, 0008, 0009, 0010, 0011, 0012 | alvo, dispatch, kill, reconciliação e auditoria |
| H-11 | ADR-0002, 0008, 0009, 0010, 0011, 0012 | persistência, tentativa, kill, reconciliação e auditoria |
| H-12 | ADR-0001, 0004, 0008, 0009, 0010, 0011, 0012 | autoridade, presença, estados, adaptadores, kill e reconciliação |

A decisão funcional de `H-05 — DOM-09 → DOM-10` não pertence ao ADR-0006. O handoff continua normativo no mapa unificado e não foi promovido artificialmente ao escopo de análise A–H.

## 5. Decisões ainda não formalizadas nesta missão

```text
P1=ADR-CAND-003|007|013|016|018
P2=ADR-CAND-017
```

Esses candidatos permanecem no catálogo para missão posterior. Os ADRs P0 não devem fingir resolver migrations completas, retenção numérica de frames, circuit breaker detalhado, relógio/process identity completo, estratégia integral de testes ou thresholds finais.

## 6. Validação do builder

```text
ADR_COUNT_MATCH=PASS
P0_CANDIDATES_MAPPED=12/12
DOMAIN_COVERAGE=16/16
HANDOFF_REFERENCE_COVERAGE=12/12
H05_FALSE_CONTROLLER_ASSIGNMENT=REMOVED
REQUIREMENT_GROUP_LINKS=PASS_PRELIMINARY
NEW_REQUIREMENT_IDS=0
MODE_A_MODE_B_SEPARATION=PASS_PRELIMINARY
TRACEABILITY_STATUS=PASS_BUILDER_PENDING_INDEPENDENT_REVIEW
```

## 7. Próxima ação

Executar revisão crítica independente da LEA-27 sobre o HEAD final do PR da LEA-26.