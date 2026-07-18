# ADR-0006 — Motores A–H e envelope imutável de análise

## Controle

```text
ADR_ID=ADR-0006
CANDIDATE_ID=ADR-CAND-008
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

A análise reúne motores de estrutura, tendência, zonas, volatilidade, contexto de candles, momentum, confluência e avaliação estratégica. Sem contrato comum, motores podem manter estado oculto, usar dados diferentes ou produzir decisão sem rastreabilidade.

## Decisão

Modelar os motores A–H como componentes determinísticos, sem efeito colateral de domínio, executados sobre um **snapshot imutável de análise**.

Cada motor recebe o mesmo `analysis_snapshot_id`, dados estimados com linhagem, caps de qualidade, contexto de estratégia e versões de configuração. Cada resultado usa envelope padronizado com estado, evidências, contradições, confiança limitada, reason codes, versão do motor e duração.

A orquestração será um DAG explícito. Motores independentes podem executar em paralelo; dependências são declaradas e não inferidas. O motor H agrega, mas não pode remover blocker ou elevar confiança acima do menor cap aplicável.

## Regras normativas

```text
ANALYSIS_INPUT=IMMUTABLE_SNAPSHOT
ENGINE_SIDE_EFFECTS=NONE_ON_DOMAIN_STATE
ENGINE_VERSION=REQUIRED
EVIDENCE_AND_CONTRADICTIONS=REQUIRED
QUALITY_CAPS=MONOTONIC
UNKNOWN=CAPABILITY_REDUCTION
ORCHESTRATION=EXPLICIT_DAG
PARALLELISM=ONLY_FOR_DECLARED_INDEPENDENCE
ENGINE_H=AGGREGATOR_NOT_POLICY_OVERRIDE
ANALYSIS_TO_ADAPTER_PATH=PROHIBITED
```

Envelope mínimo:

```text
engine_id|engine_version|snapshot_id|status|findings|evidence_refs|contradictions|confidence_raw|confidence_capped|reason_codes|started_at|completed_at
```

## Alternativas consideradas

### Pipeline sequencial rígido

Não adotado como regra global porque impede paralelismo seguro e acopla motores independentes.

### Objetos mutáveis compartilhados

Rejeitados por ordem não determinística, vazamento de estado e dificuldade de replay.

### Modelo único sem resultados por motor

Rejeitado por reduzir explicabilidade, testes e isolamento de falha.

## Consequências

### Positivas

- replay reproduzível;
- testes unitários por motor;
- contradições preservadas;
- paralelismo controlado;
- nenhuma ligação direta com execução.

### Negativas e custos

- envelopes aumentam volume documental e persistido;
- versionamento de motores exige disciplina;
- determinismo depende de controlar relógio, aleatoriedade e configuração.

## Segurança, recovery e falha segura

```text
SNAPSHOT_INELIGIBLE=ANALYSIS_BLOCKED
ENGINE_FAILURE=PARTIAL_OR_BLOCKED_WITH_REASON
MISSING_REQUIRED_ENGINE=NO_SIGNAL_ELIGIBILITY
CAP_VIOLATION=RESULT_REJECTED
RESTART=NEW_RUN_ID_WITH_SAME_SNAPSHOT_ALLOWED
DIRECT_UI_ACTION=BLOCK
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-11
SECONDARY_DOMAINS=DOM-09|DOM-10|DOM-12|DOM-16
HANDOFFS=H-06|H-07
REQUIREMENTS=PTM-V26-001|PTM-V26-009..018|V26-ANA-001..011
DEPENDS_ON=ADR-0001|ADR-0003
```

## Critérios de aceitação

```text
IMMUTABLE_ANALYSIS_SNAPSHOT=PASS
COMMON_ENGINE_ENVELOPE=PASS
EXPLICIT_DAG=PASS
QUALITY_CAP_MONOTONICITY=PASS
NO_ANALYSIS_SIDE_EFFECT_ON_EXECUTION=PASS
```

## Fora de escopo

- fórmulas dos motores;
- thresholds numéricos;
- linguagem ou biblioteca de paralelismo;
- código de análise;
- decisão de estratégia.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.