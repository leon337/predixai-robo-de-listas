# ADR-0017 — Thresholds e limites numéricos versionados

## Controle

```text
ADR_ID=ADR-0017
CANDIDATE_ID=ADR-CAND-017
PRIORITY=P2
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
DEPENDS_ON=ADR-0005|ADR-0006|ADR-0007|ADR-0012
MUST_ALIGN_WITH=ADR-0014|ADR-0015|ADR-0016|ADR-0018
```

## Contexto

Qualidade visual, frescor, estabilidade, confiança, deadlines, retenção, filas e circuit breaker exigirão limites numéricos. Fixar valores sem benchmark reproduzível pode elevar confiança artificialmente, ocultar blockers ou tornar o sistema inseguro no hardware-alvo.

## Decisão

Adotar um **registro versionado de thresholds e limites**, com valores inicialmente provisórios e incapazes de superar blockers estruturais.

Estados do valor:

```text
PROVISIONAL=default conservador sem aprovação para GO
CALIBRATING=em benchmark controlado
CALIBRATED=evidência suficiente para escopo específico
APPROVED=gate independente aprovou uso no escopo declarado
RETIRED=não aceito para novas execuções
```

Cada entrada declara:

```text
threshold_id
threshold_version
domain_and_metric
unit_and_scale
value_or_range
comparison_semantics
scope_hardware
scope_profile
scope_strategy_or_adapter
source_dataset_or_fixture
benchmark_protocol
sample_summary
false_positive_and_false_negative_risk
status
effective_from
supersedes
reason_code_policy
```

## Regras normativas

```text
THRESHOLD_WITHOUT_VERSION=BLOCK
UNKNOWN_THRESHOLD=REDUCE_CAPABILITY_OR_BLOCK
PROVISIONAL_THRESHOLD=NO_RUNTIME_GO_AUTHORITY
BLOCKER_OVERRIDE_BY_SCORE=PROHIBITED
CONFIDENCE_CAP=MONOTONIC_CONSERVATIVE
QUALITY_SCORE_CAN_APPROVE_FAIL=NO
SCOPE_MISMATCH=BLOCK_OR_USE_SAFER_DEFAULT
HARDWARE_SPECIFIC_VALUE=NOT_GLOBAL_DEFAULT
THRESHOLD_CHANGE=NEW_VERSION
RETROACTIVE_RESULT_MUTATION=PROHIBITED
BENCHMARK_REPRODUCIBLE=REQUIRED_FOR_CALIBRATED
APPROVAL_GATE=REQUIRED_FOR_APPROVED
LIMIT_EXPANSION=EXPLICIT_HUMAN_AND_POLICY_GATE
SAFE_DEFAULT=LOWER_CAPABILITY
```

Valores de domínio diferente não são agregados sem normalização declarada. Representação canônica deve evitar ponto flutuante não determinístico quando inteiro escalado for adequado.

## Benchmark mínimo

Um valor só pode avançar para `CALIBRATED` quando houver:

- commit e configuração exatos;
- hardware e perfil identificados;
- dataset ou fixture sanitizada e versionada;
- protocolo repetível;
- métricas de erro e estabilidade;
- análise de casos limítrofes;
- evidência de que `UNKNOWN` e `FAIL` não foram promovidos;
- relatório e hashes dos artefatos.

## Alternativas consideradas

### Valores fixos no código

Rejeitada porque oculta origem, escopo, revisão e histórico.

### Ajuste automático irrestrito

Rejeitado porque pode ampliar capacidade sem autorização e mascarar degradação.

### Um score único global

Rejeitado porque dimensões distintas possuem blockers e caps próprios.

### Sem thresholds

Rejeitado como solução definitiva; estados discretos e limites são necessários, mas permanecem conservadores até evidência.

## Consequências

### Positivas

- valores rastreáveis e reproduzíveis;
- calibração separada por hardware e perfil;
- alterações não reescrevem resultados históricos;
- thresholds não contornam blockers;
- limites podem evoluir com evidência.

### Negativas e custos

- exige catálogo e benchmark;
- resultados podem ficar bloqueados até calibração;
- múltiplos escopos aumentam manutenção;
- tuning automático fica restrito.

## Segurança, recovery e falha segura

```text
THRESHOLD_VERSION_MISSING=BLOCK
THRESHOLD_STATUS_UNKNOWN=BLOCK
SCOPE_INCOMPATIBLE=USE_SAFER_DEFAULT_OR_BLOCK
BENCHMARK_ARTIFACT_MISSING=NOT_CALIBRATED
LIMIT_OVERFLOW_OR_INVALID_UNIT=BLOCK
MODEL_OR_PROFILE_CHANGE=RECALIBRATION_REQUIRED
ROLLBACK_TO_RETIRED_VERSION=BLOCK_UNLESS_EXPLICIT_RECOVERY
AUTOMATIC_LIMIT_EXPANSION=SECURITY_EVENT
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-09|DOM-11|DOM-12
SECONDARY_DOMAINS=DOM-06|DOM-08|DOM-15|DOM-16
HANDOFFS=H-05|H-06|H-07|H-08|H-12
REQUIREMENTS=PTM-V26-005..006|PTM-V26-009..022|V26-VAL-003..006|V26-ANA-001..011|V26-STR-001..004|V26-SIG-001..008|V27-SAF-001|V27-SAF-008|V27-QA-001..007
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
```

## Critérios de aceitação

```text
THRESHOLD_REGISTRY_CONTRACT=PASS_BUILDER
PROVISIONAL_NOT_GO_AUTHORITY=PASS_BUILDER
BLOCKER_OVERRIDE_PROHIBITED=PASS_BUILDER
SCOPE_AND_VERSION_REQUIRED=PASS_BUILDER
REPRODUCIBLE_BENCHMARK_GATE=PASS_BUILDER
AUTOMATIC_LIMIT_EXPANSION_BLOCKED=PASS_BUILDER
NUMERIC_VALUES_FINALIZED=NO
BENCHMARK_EXECUTED=NO
```

## Fora de escopo

- valores numéricos finais;
- datasets reais;
- benchmark executado;
- tuning automático;
- autorização de runtime.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW` até `LEA-31=PASS`, autorização humana de merge e confirmação pós-merge.