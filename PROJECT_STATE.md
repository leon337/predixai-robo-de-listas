# PROJECT_STATE — PredixAI Robô de Listas

## Estado oficial

- Repositório: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- HEAD-base confirmado: `98bb1d33b9d8eca702fb4e52bdde02686021c766`
- Versão do legado: `V2.4.3-R1`
- Missão ativa: `LEA-18 — Consolidação cruzada das PTMs V2.5, V2.6 e V2.7`
- Branch de trabalho: `leonpcsn/lea-18-consolidacao-cruzada-das-ptms-v25-v26-e-v27`
- PR ativo: `#40`, Draft
- Revisão crítica independente: pendente

## Transição ativa

```text
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
TRANSITION_STATUS=IN_PROGRESS
FROM_STATE=PTM_V2_7_DOCUMENTALLY_DEFINITIVE
TO_STATE=CROSS_CONSOLIDATION_IN_PROGRESS
GITHUB_SYNC_STATUS=PASS
LINEAR_SYNC_STATUS=PASS
MISSION_LOCK=LEA-18
```

## Escopo

Consolidar as três PTMs em uma arquitetura documental única, sem reescrever históricos e respeitando a precedência normativa ativa.

```text
PTM_V2_5=FOUNDATION_CONTRACTS_SAFE_MIGRATION
PTM_V2_6=OBSERVATION_ANALYSIS_SIMULATED_SIGNALS
PTM_V2_7=CONTROLLED_COMMAND_AUTHORIZATION_ACTION_RECEIPT_RECONCILIATION
DOCUMENTATION_ONLY=YES
CODE_CHANGE_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

## Política transversal vigente

```text
CONTROLLED_SCREEN_CAPTURE=ALLOWED
CONTROLLED_OCR=ALLOWED
CONTROLLED_REPLAY=ALLOWED
CONTROLLED_POINTER_KEYBOARD_CLICK=ALLOWED_IN_CONTROLLED_SCOPE
CONTROLLED_TEST_AUTHENTICATION=ALLOWED
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
REAL_FINANCIAL_EFFECT=NOT_AUTHORIZED
```

## Gates

```text
G1_PRECONDITIONS_PASS=PASS
G2_SOURCE_INVENTORY_COMPLETE=PASS
G3_DOMAIN_BOUNDARIES_CONSOLIDATED=PASS_BUILDER
G4_REQUIREMENTS_TRACEABILITY_COMPLETE=PASS_BUILDER
G5_CONFLICTS_AND_SUPERSESSIONS_RESOLVED=IN_PROGRESS
G6_CONSOLIDATED_DOCUMENT_READY=NOT_STARTED
G7_INDEPENDENT_CRITICAL_REVIEW=NOT_STARTED
```

## Resultado G3

```text
CANONICAL_DOMAIN_COUNT=16
MANDATORY_HANDOFF_COUNT=12
DOMAIN_BOUNDARY_BLOCKERS=0
```

O mapa fixa a cadeia:

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

## Resultado G4

```text
V2_5_TOTAL_COVERED=56/56
V2_6_TOTAL_COVERED=78/78
V2_7_TOTAL_COVERED=84/84
CROSS_VERSION_TOTAL_COVERED=218/218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
NEW_REQUIREMENT_IDS=0
DOMAIN_LINKAGE_COMPLETE=PASS_BUILDER
HANDOFF_LINKAGE_COMPLETE=PASS_BUILDER
SUPERSEDED_ID_INTERPRETATION_LINKED=PASS_BUILDER
TRACEABILITY_BLOCKERS=0
```

Cobertura documental não equivale a implementação ou runtime aprovado. SQL, migrations, testes de runtime e schema físico permanecem não executados ou não definidos nesta missão.

## Invariantes consolidados

- servidor é autoridade global;
- Android e UI são clientes;
- frame inválido não alimenta análise;
- candidato não é sinal;
- sinal não é comando;
- coordenada não é autorização;
- recibo isolado não é verdade global;
- ação `CONTROLLED_UI` não autoriza efeito financeiro real;
- restart invalida a despachabilidade de comando anterior.

## Entregas

- ✅ `docs/architecture/INVENTARIO_FONTES_CONSOLIDACAO_CRUZADA_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`
- ✅ `docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`
- ✅ `docs/architecture/MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`
- 🟧 registro de conflitos, supersessões e precedência;
- ⬜ catálogo de decisões candidatas a ADR;
- ⬜ documento de consolidação cruzada;
- ⬜ pacote para revisão crítica independente.

## Achado documental controlado

Não existe um relatório Markdown final separado para a revisão V2.5 com o nome presumido. A autoridade é composta pela revisão final do PR `#33`, Linear `LEA-13` e recibo pós-merge da `LEA-8`.

## Próxima ação

Consolidar conflitos, supersessões e precedência normativa, distinguindo cláusulas vigentes, registros históricos e decisões candidatas a ADR.
