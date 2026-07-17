# REMEDIAÇÃO DO RETESTE 02 E AUDITORIA DOS IDs ESTRUTURAIS V2.7

## LEA-18 / preparação do Reteste 03 da LEA-19

## 1. Controle

```text
REMEDIATION_TYPE=BUILDER_DOCUMENTAL_REMEDIATION
BUILDER_ISSUE=LEA-18
REVIEW_ISSUE=LEA-19
PULL_REQUEST=40
RETEST_02_REVIEWED_HEAD=5096b449acc6607a9b9edd9955bf78bfbb0e6f80
RETEST_02_REPORT_COMMIT=5be3fea649418626a056a426881c7230e85d825c
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_OR_MIGRATIONS_CREATED=NO
MERGE_AUTHORIZED=NO
ADRS_START_AUTHORIZED=NO
```

## 2. MAJOR-06 remediado

`PTM-V27-031` foi removido do `DOM-01` e inserido no `DOM-16`.

```text
PTM_V27_031_PRIMARY_DOMAIN=DOM-16
PTM_V27_032_PRIMARY_DOMAIN=DOM-01
DOM_01_PRIMARY_IDS=7
DOM_16_PRIMARY_IDS=34
```

A decisão decorre da matriz canônica V2.7, que define `PTM-V27-031` como prova negativa contra ação não controlada e efeito financeiro real, e do mapa unificado, que atribui auditoria, segurança, contenção e evidências negativas ao `DOM-16`.

## 3. Auditoria integral dos 32 IDs estruturais V2.7

Critério: o domínio primário é o domínio que detém a autoridade sobre o resultado ou contrato dominante do requisito; vínculos secundários permanecem na matriz consolidada.

| IDs | Domínio primário | Resultado |
|---|---|---|
| `PTM-V27-001`, `002`, `004`, `005`, `006`, `007` | `DOM-13` | confirmado |
| `PTM-V27-003`, `008`, `009`, `021` | `DOM-14` | `003` reclassificado; demais confirmados |
| `PTM-V27-010` a `018`, `022` a `025`, `030` | `DOM-15` | confirmados |
| `PTM-V27-019`, `026`, `027`, `028`, `031` | `DOM-16` | `031` reclassificado; demais confirmados |
| `PTM-V27-020` | `DOM-05` | confirmado |
| `PTM-V27-029` | `DOM-03` | confirmado |
| `PTM-V27-032` | `DOM-01` | confirmado |

### Correção adicional descoberta pela auditoria

`PTM-V27-003` estava no `DOM-13`, porém o requisito governa ausência, capacidade e fronteira do adaptador real. O mapa define adaptadores e capability checks no `DOM-14`.

```text
PTM_V27_003_PRIMARY_DOMAIN=DOM-14
DOM_13_PRIMARY_IDS=32
DOM_14_PRIMARY_IDS=12
```

## 4. Reconciliação final

```text
V2_7_STRUCTURAL_IDS_EXPECTED=32
V2_7_STRUCTURAL_IDS_AUDITED=32
V2_7_STRUCTURAL_IDS_CONFIRMED_WITHOUT_CHANGE=30
V2_7_STRUCTURAL_IDS_RECLASSIFIED=2
TOTAL_IDS=218
UNIQUE_IDS=218
DUPLICATE_IDS=0
ORPHAN_IDS=0
DOM_01=7
DOM_13=32
DOM_14=12
DOM_16=34
PRIMARY_DOMAIN_AUDIT=PASS_BUILDER_REMEDIATED
```

## 5. Resultado do builder

```text
MAJOR_06_STATUS=REMEDIATED
ADDITIONAL_V2_7_DOMAIN_CORRECTION=REMEDIATED
OPEN_CRITICAL_FINDINGS=0
OPEN_MAJOR_FINDINGS=0
OPEN_MINOR_FINDINGS=0
RETEST_03_REQUIRED=YES
DOCUMENTAL_READY_FOR_MERGE=NO_PENDING_RETEST_03
ADRS_READY_TO_START=NO_PENDING_RETEST_03
```

## 6. Próxima ação

Sincronizar `PROJECT_RUNTIME_STATE.yaml`, `PROJECT_STATE.md`, tronco multichat e descrição do PR; resolver a thread de `MAJOR-06`; reabrir `LEA-19` e executar Reteste 03 independente sobre o HEAD final. Merge e ADRs permanecem bloqueados.