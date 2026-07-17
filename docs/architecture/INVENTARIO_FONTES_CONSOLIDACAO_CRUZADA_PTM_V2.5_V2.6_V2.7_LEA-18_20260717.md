# INVENTÁRIO CANÔNICO DE FONTES — CONSOLIDAÇÃO CRUZADA

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=CANONICAL_SOURCE_INVENTORY
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
REVIEWED_PR_HEAD_BEFORE_WRITE=5335fc774ab6d68b71ea55ba77722ad3b47427b6
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
```

## 2. Objetivo

Definir, antes da consolidação arquitetural, quais fontes governam o presente, quais comprovam decisões históricas, quais cláusulas foram supersedidas e quais evidências devem ser preservadas sem serem tratadas como autoridade atual.

## 3. Regras de autoridade

```text
CURRENT_OPERATIONAL_STATE=PROJECT_RUNTIME_STATE.yaml
CURRENT_HUMAN_STATE=PROJECT_STATE.md
CURRENT_ROADMAP=PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md
CONSOLIDATED_DOCUMENTATION=GitHub main
UNMERGED_DOCUMENTATION=PR #40
TASK_STATUS=Linear LEA-18
HISTORICAL_EVIDENCE=docs/history + docs/audits
```

Não existe precedência única para todos os domínios. Estado operacional, trabalho não integrado, tarefa, documentação consolidada e evidência histórica são resolvidos por suas autoridades próprias.

## 4. Precedência normativa transversal

Para conflitos sobre captura, OCR, replay, ponteiro, teclado, clique, autenticação, alvo controlado e efeito financeiro:

```text
1. docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
2. docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md
3. docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md
4. docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md
5. documentos-pai e matrizes das PTMs para cláusulas não supersedidas
6. revisões, checkpoints e recibos históricos como evidência do estado anterior
```

Resultado obrigatório:

```text
CONTROLLED_UI_AUTOMATION=ALLOWED_IN_CONTROLLED_SCOPE
ANALYSIS_ENGINE_DIRECT_UI_ACTION=PROHIBITED
REAL_FINANCIAL_EFFECT=NOT_AUTHORIZED
CONTROLLED_UI_ACTION_DOES_NOT_IMPLY_FINANCIAL_EFFECT=TRUE
```

## 5. Fontes vivas da missão

| ID | Fonte | Papel | Autoridade atual | Tratamento |
|---|---|---|---|---|
| GOV-01 | `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md` | regras permanentes | normativa | aplicar integralmente |
| GOV-02 | `PROJECT_RUNTIME_STATE.yaml` no PR `#40` | estado operacional estruturado | canônica da transição ativa | manter sincronizado |
| GOV-03 | `PROJECT_STATE.md` no PR `#40` | visão humana do estado | derivada do manifesto | não divergir do GOV-02 |
| GOV-04 | `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` no PR `#40` | roadmap, gates e continuidade | governante do fluxo | manter alinhado |
| GOV-05 | `docs/protocols/AUTORIDADE_POR_DOMINIO.md` | resolução de autoridade e drift | normativa | aplicar por domínio |
| GOV-06 | `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` | capacidade e limites de automação | normativa ativa de maior precedência no tema | prevalece sobre proibições genéricas antigas |
| GOV-07 | Linear `LEA-18` | tarefa, dependências, bloqueios e progresso | operacional | manter alinhado ao PR `#40` |
| GOV-08 | GitHub PR `#40` | trabalho documental não integrado | autoridade do conteúdo em construção | manter Draft até revisão aplicável |

## 6. Fundação factual herdada

| ID | Fonte | Papel | Status | Uso na consolidação |
|---|---|---|---|---|
| AUD-01 | `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md` | snapshot factual inicial | histórico `DRAFT_PARTIAL` | usar fatos; não usar o marcador antigo como estado atual |
| AUD-02 | `docs/audits/ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md` | corrige evidência, estado e rastreabilidade | remediação concluída | governa a interpretação final dos snapshots do Anexo A |
| AUD-03 | `docs/audits/ANEXO_A_APENDICE_04_ARVORE_AST_DOCUMENTACAO_FINAL_PTP-GOV.6_20260716.md` | fechamento documental da árvore e AST | evidência final | sustenta inventário e contagens |
| AUD-04 | `docs/audits/PREDIXAI_PTP-GOV.6_ARVORE_AST_20260716.txt.gz.b64` | evidência bruta canônica | verificável por hash | preservar como prova reproduzível |
| AUD-05 | `docs/history/reviews/REVISAO_CRITICA_AUDITORIA_MESTRA_PTP-GOV.6_20260716.md` | Boss Gate da Auditoria Mestra | `PASS` | torna o inventário factual apto a sustentar as PTMs |
| AUD-06 | `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md` | contratos conceituais históricos | referência conceitual | adaptar; não transformar endpoints preliminares em implementação aprovada |

## 7. PTM V2.5 — Fundação, contratos e migração segura

| ID | Fonte | Papel | Estado preservado | Autoridade na consolidação |
|---|---|---|---|---|
| V25-01 | `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md` | documento-pai arquitetural | builder draft histórico | autoridade para cláusulas não supersedidas após aplicação do gate final |
| V25-02 | `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md` | rastreabilidade legado→V2.5 | builder complete histórico | base dos 56 IDs definitivos |
| V25-03 | revisão final do PR `#33`, review `4718668692` | revisão crítica independente | `PASS`, 0 críticos, 0 maiores, 2 menores | Boss Gate factual da V2.5 |
| V25-04 | Linear `LEA-13` — resultado final | controle operacional da revisão | `Done/PASS` | confirma tarefa e decisão |
| V25-05 | `docs/history/ptp/RECIBO_POS_MERGE_LEA-8_PTM_V2.5_20260716.md` | confirmação pós-merge | V2.5 documentalmente definitiva | autoridade do fechamento integrado |

Resultado definitivo carregado:

```text
V25_STRUCTURAL_REQUIREMENTS=29
V25_FUNCTIONAL_REQUIREMENTS=23
V25_ADDITIONAL_REQUIREMENTS_ACCEPTED=4
V25_TOTAL_UNIQUE_REQUIREMENT_IDS=56
V25_CRITICAL_REVIEW=PASS
```

Correção obrigatória: frases históricas de exclusão global de ponteiro/clique significam somente que a V2.5 não possui autoridade para produzir ação de UI. Elas não proíbem automação controlada em harness ou etapa competente.

## 8. PTM V2.6 — Observação, análise e sinais

| ID | Fonte | Papel | Estado preservado | Autoridade na consolidação |
|---|---|---|---|---|
| V26-01 | `docs/architecture/PTM_V2.6_OBSERVACAO_ANALISE_SINAIS_LEA-14_20260716.md` | documento-pai arquitetural | builder draft histórico | cláusulas analíticas não supersedidas |
| V26-02 | `docs/architecture/PTM_V2.6_MATRIZ_RASTREABILIDADE_LEA-14_20260716.md` | rastreabilidade V2.5/legado→V2.6 | builder `PASS` preliminar | base dos 78 IDs definitivos |
| V26-03 | `docs/history/reviews/REVISAO_CRITICA_PTM_V2.6_LEA-15_20260716.md` | revisão crítica independente | `PASS`, 0 críticos, 0 maiores, 2 menores | Boss Gate da V2.6 |
| V26-04 | Linear `LEA-15` — resultado final | controle operacional da revisão | `Done/PASS` | confirma tarefa e decisão |
| V26-05 | `docs/history/ptp/RECIBO_POS_MERGE_LEA-14_PTM_V2.6_20260716.md` | confirmação pós-merge | V2.6 documentalmente definitiva | autoridade do fechamento integrado |

Resultado definitivo carregado:

```text
V26_STRUCTURAL_REQUIREMENTS=28
V26_FUNCTIONAL_REQUIREMENTS=50
V26_TOTAL_REQUIREMENT_IDS=78
V26_CRITICAL_REVIEW=PASS
```

Achados menores obrigatoriamente herdados:

1. ampliar rastreabilidade funcional por requisito antes do Documento Mestre ou vínculo final com testes;
2. uniformizar a terminologia da prova negativa.

Correção obrigatória: `REAL_INPUT_AND_EXECUTION_EXCLUSION` significa ausência de acoplamento `ANALYSIS -> UNDECLARED_UI_ACTION`. Captura, OCR, replay e harness controlado permanecem permitidos.

## 9. Política transversal V2.5→V2.7

| ID | Fonte | Papel | Status | Autoridade |
|---|---|---|---|---|
| CAP-01 | `docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md` | corrige a fronteira capacidade/etapa/efeito | `NORMATIVE_ACTIVE` | prevalece sobre cláusulas genéricas conflitantes das três PTMs |

Decisões carregadas:

```text
V2_5_OWNS_UI_AUTOMATION=NO
V2_6_ANALYSIS_DOMAIN_PRODUCES_UI_ACTION=NO
CONTROLLED_CAPTURE_AND_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_UI_ADAPTER=ALLOWED
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
REAL_FINANCIAL_EFFECT=NOT_AUTHORIZED
```

## 10. PTM V2.7 — Comando e execução controlada

| ID | Fonte | Papel | Estado preservado | Autoridade na consolidação |
|---|---|---|---|---|
| V27-01 | `docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md` | documento-pai | builder draft histórico | usar somente cláusulas não supersedidas |
| V27-02 | `docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md` | matriz principal | builder remediado | base dos 84 IDs, complementada pelo suplemento |
| V27-03 | `docs/architecture/PTM_V2.7_ADENDO_REMEDIACAO_LEA-17_LEA-16_20260717.md` | remediação após revisão inicial | substituição normativa parcial | aplicar onde não foi substituído pelo reteste 02 |
| V27-04 | `docs/architecture/PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK_LEA-17_20260717.md` | contrato final de `CONTROLLED_UI`, dimensão monetária e restart | normativo substituto | prevalece nos contratos afetados |
| V27-05 | `docs/architecture/PTM_V2.7_SUPLEMENTO_RASTREABILIDADE_RETESTE_02_LEA-17_20260717.md` | interpretação final dos IDs afetados | sem novos IDs | complementa a matriz principal |
| V27-06 | `docs/history/reviews/REVISAO_CRITICA_RETESTE_02_PTM_V2.7_LEA-17_20260717.md` | revisão crítica independente final | `FINAL_PASS` | Boss Gate final; supersede review inicial e reteste 01 |
| V27-07 | Linear `LEA-17` — segundo reteste | controle operacional da revisão | `Done/PASS` | confirma tarefa e decisão |
| V27-08 | `docs/history/ptp/RECIBO_POS_MERGE_LEA-16_PTM_V2.7_20260717.md` | recibo do PR principal | integrado | confirma contratos e pendências carregadas |
| V27-09 | PR `#39`, merge `98bb1d33b9d8eca702fb4e52bdde02686021c766` | confirmação final do estado V2.7 | integrado | libera a consolidação cruzada |

Resultado definitivo carregado:

```text
V27_STRUCTURAL_REQUIREMENTS=32
V27_FUNCTIONAL_REQUIREMENTS=52
V27_TOTAL_REQUIREMENT_IDS=84
V27_CRITICAL_REVIEW=PASS
V27_INITIAL_REVIEW=FAIL_HISTORICAL
V27_RETEST_01=SUPERSEDED
V27_RETEST_02=PASS_AUTHORITY
```

## 11. Fontes históricas sem autoridade atual

As seguintes categorias permanecem consultáveis como sequência factual, mas não governam a consolidação atual:

- checkpoints anteriores aos recibos pós-merge;
- auto-revisões do builder;
- prompts de revisão;
- revisão inicial `FAIL` da V2.7 após sua remediação e reteste final;
- reteste 01 da V2.7, formalmente supersedido;
- cláusulas antigas que tratavam presença de bibliotecas de UI como falha absoluta;
- marcadores `DRAFT_PARTIAL`, `PENDING` ou `BLOCKED_BY_ENVIRONMENT` em snapshots da Auditoria Mestra.

## 12. Ausências e decisões explícitas

### 12.1 Relatório Markdown final da PTM V2.5

```text
EXPECTED_FILE=docs/history/reviews/REVISAO_CRITICA_PTM_V2.5_LEA-13_20260716.md
FILE_EXISTS=NO
INVENTED_REPLACEMENT=NO
```

A evidência final existente é composta por:

1. review final `4718668692` no PR `#33`;
2. resultado final da `LEA-13` no Linear;
3. recibo pós-merge `RECIBO_POS_MERGE_LEA-8_PTM_V2.5_20260716.md`.

A ausência não bloqueia a consolidação porque a decisão e o conteúdo do Boss Gate estão preservados em fontes rastreáveis e integradas.

### 12.2 Implementação

Nenhuma fonte documental deve ser interpretada como prova de runtime, banco, API, SQL, migration ou automação implementada.

```text
ARCHITECTURE_SPECIFIED=YES
APPLICATION_IMPLEMENTED=NO_EVIDENCE_IN_THIS_MISSION
RUNTIME_VALIDATED=NO
SQL_OR_MIGRATIONS_AUTHORIZED=NO
```

## 13. Pendências arquiteturais carregadas

1. taxonomia integral de `target_logical_id`;
2. limites numéricos após benchmark reproduzível;
3. ADR da topologia do kill switch;
4. matriz integral de transições antes da implementação;
5. granularidade funcional por requisito da V2.6;
6. contratos físicos, produtores, consumidores e IDs finais de testes;
7. separação explícita entre especificação de teste e evidência runtime.

## 14. Resultado do gate

```text
CANONICAL_SOURCE_CATEGORIES=6
CURRENT_GOVERNING_SOURCES_IDENTIFIED=PASS
LEGACY_FACTUAL_AUTHORITY_IDENTIFIED=PASS
PTM_V2_5_FINAL_AUTHORITY_IDENTIFIED=PASS
PTM_V2_6_FINAL_AUTHORITY_IDENTIFIED=PASS
PTM_V2_7_FINAL_AUTHORITY_IDENTIFIED=PASS
SUPERSESSION_CHAIN_IDENTIFIED=PASS
MISSING_SOURCE_HANDLING=PASS
SOURCE_INVENTORY_BLOCKERS=0
G2_SOURCE_INVENTORY_COMPLETE=PASS
NEXT_GATE=G3_DOMAIN_BOUNDARIES_CONSOLIDATED
```
