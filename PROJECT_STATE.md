# PROJECT_STATE — PredixAI Robô de Listas

## Estado oficial

- Repositório: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- HEAD-base confirmado: `98bb1d33b9d8eca702fb4e52bdde02686021c766`
- Versão do legado: `V2.4.3-R1`
- Missão ativa: `LEA-18 — Consolidação cruzada das PTMs V2.5, V2.6 e V2.7`
- Revisão ativa: `LEA-19 — Revisão crítica independente do PR #40`
- Branch de trabalho: `leonpcsn/lea-18-consolidacao-cruzada-das-ptms-v25-v26-e-v27`
- PR ativo: `#40`, pronto para revisão
- Merge: não autorizado
- ADRs: não autorizados

## Transição ativa

```text
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
TRANSITION_STATUS=IN_PROGRESS
FROM_STATE=PTM_V2_7_DOCUMENTALLY_DEFINITIVE
TO_STATE=CROSS_CONSOLIDATION_AWAITING_INDEPENDENT_REVIEW
GITHUB_SYNC_STATUS=PASS
LINEAR_SYNC_STATUS=PASS
MISSION_LOCK=LEA-18
```

## Escopo

```text
PTM_V2_5=FOUNDATION_CONTRACTS_SAFE_MIGRATION
PTM_V2_6=OBSERVATION_ANALYSIS_SIMULATED_SIGNALS
PTM_V2_7=CONTROLLED_COMMAND_AUTHORIZATION_ACTION_RECEIPT_RECONCILIATION
DOCUMENTATION_ONLY=YES
CODE_CHANGE_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
ADRS_START_AUTHORIZED=NO
```

## Gates

```text
G1_PRECONDITIONS_PASS=PASS
G2_SOURCE_INVENTORY_COMPLETE=PASS
G3_DOMAIN_BOUNDARIES_CONSOLIDATED=PASS_BUILDER
G4_REQUIREMENTS_TRACEABILITY_COMPLETE=PASS_BUILDER
G5_CONFLICTS_AND_SUPERSESSIONS_RESOLVED=PASS_BUILDER
G6_CONSOLIDATED_DOCUMENT_READY=PASS_BUILDER
G7_INDEPENDENT_CRITICAL_REVIEW=AWAITING_LEA_19
```

## Resultado do builder

```text
CANONICAL_DOMAIN_COUNT=16
MANDATORY_HANDOFF_COUNT=12
V2_5_TOTAL_COVERED=56/56
V2_6_TOTAL_COVERED=78/78
V2_7_TOTAL_COVERED=84/84
CROSS_VERSION_TOTAL_COVERED=218/218
INDIVIDUAL_REQUIREMENT_ROWS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
NEW_REQUIREMENT_IDS=0
SUPERSEDED_INTERPRETATION_IDS=32
CONFLICT_CLASSES_REVIEWED=24
UNRESOLVED_NORMATIVE_CONFLICTS=0
ADR_CANDIDATE_COUNT=18
BUILDER_SELF_REVIEW=PASS_PRELIMINARY
BUILDER_CRITICAL_FINDINGS=0
BUILDER_MAJOR_FINDINGS=0
BUILDER_MINOR_FINDINGS=2
BUILDER_MINOR_RESOLVED=2/2
DOCUMENTAL_BLOCKERS=0
```

O builder não emite o Boss Gate final. A consolidação permanece não definitiva até o resultado independente da `LEA-19`.

## Fronteira arquitetural

```text
LISTAS E PERFIS
→ OBSERVAÇÃO E FRAME
→ VALIDAÇÃO E EXTRAÇÃO
→ ANÁLISE A–H
→ CANDIDATO E SINAL
→ COMANDO E AUTORIZAÇÃO
→ ALVO E ADAPTADOR
→ DISPATCH, RECIBO E RECONCILIAÇÃO
```

Invariantes:

- servidor é autoridade global;
- Android e UI são clientes;
- frame inválido não alimenta análise;
- sinal não é comando;
- coordenada não é autorização;
- recibo isolado não é verdade global;
- `CONTROLLED_UI` não autoriza efeito financeiro real;
- restart invalida comando anterior;
- timeout não comprova ausência de efeito;
- `UNKNOWN_EFFECT` bloqueia ação correlata.

## Entregas

- ✅ inventário canônico de fontes;
- ✅ mapa de 16 domínios e 12 handoffs;
- ✅ matriz consolidada `218/218`;
- ✅ índice individual dos 218 IDs;
- ✅ registro de conflitos e supersessões;
- ✅ catálogo de 18 ADRs candidatos;
- ✅ documento final da consolidação cruzada;
- ✅ auto-revisão preliminar do builder;
- ✅ pacote para revisão independente;
- 🟧 revisão crítica independente `LEA-19`.

## Condição para avançar

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
TRACEABILITY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=PASS
UNRESOLVED_NORMATIVE_CONFLICTS=0
GITHUB_LINEAR_ALIGNMENT=PASS
```

## Próxima ação

Executar a `LEA-19` como revisão crítica independente do PR `#40`. Não realizar merge nem iniciar ADRs antes do resultado final.
