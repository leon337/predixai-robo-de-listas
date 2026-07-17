# PTM V2.6 — OBSERVAÇÃO, ANÁLISE E SINAIS

## LEA-14 — Builder Draft

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DRAFT
MISSION=LEA-14
LINEAR_ISSUE=LEA-14
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=1ca1be40b570b3ba458cf28efc73113da2031e8d
WORKING_BRANCH=leonpcsn/lea-14-ptm-v26-observacao-analise-e-sinais
LEGACY_VERSION=V2.4.3-R1
PTM_V2_5_DEFINITIVE=YES_DOCUMENTAL
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
POINTER_MOVEMENT_ALLOWED=NO
REAL_CLICK_ALLOWED=NO
REAL_ORDER_ALLOWED=NO
IMPLEMENTATION_AUTHORIZED=NO
PTM_V2_6_CRITICAL_REVIEW=PENDING
```

Este documento consolida a arquitetura documental da PTM V2.6. Ele não autoriza implementação, banco físico, captura em runtime, movimento de ponteiro, clique, login, ordem, compra ou venda real.

## 2. Fontes de autoridade

1. `PROJECT_RUNTIME_STATE.yaml`;
2. `PROJECT_STATE.md`;
3. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
4. `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md`;
5. `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md`;
6. `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md` e apêndices;
7. `docs/audits/ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md`;
8. `docs/history/reviews/REVISAO_CRITICA_AUDITORIA_MESTRA_PTP-GOV.6_20260716.md`;
9. `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md`;
10. issue Linear `LEA-14`.

## 3. Fronteira da versão

```text
V2_5=FOUNDATION_AND_SAFE_MIGRATION_DESIGN
V2_6=OBSERVATION_ANALYSIS_AND_SIMULATED_SIGNALS
V2_7=CONTROLLED_EXECUTION_AFTER_OWN_GATES
```

A V2.6 recebe perfis, calibração, ROIs, contratos, configuração, segurança, observabilidade e persistência conceitual da V2.5. Ela produz observações, análises e sinais simulados. Ela não produz efeitos físicos.

## 4. Invariantes

- a corretora observada é fonte visual externa, nunca autoridade de estado interno;
- toda leitura depende de janela, perfil e ROI compatíveis;
- frame inválido não alimenta análise;
- dado desconhecido reduz capacidade e nunca aumenta confiança;
- confiança técnica não substitui qualidade, estabilidade ou elegibilidade;
- thresholds definitivos exigem benchmark e evidência;
- cada resultado declara versão, hashes, razão, qualidade e linhagem;
- candidato não equivale a sinal;
- sinal não equivale a execução;
- `WAIT`, `DEGRADED` e `BLOCKED` são resultados válidos;
- nenhuma capacidade da V2.6 pode mover ponteiro ou clicar.

## 5. Requisitos estruturais

| ID | Requisito | Origem e tratamento | Gate |
|---|---|---|---|
| PTM-V26-001 | Observação, análise, estratégia e sinal são domínios separados do executor. | V2.5 separa listas da análise; execução legada com `pynput` é descontinuada nesta etapa. | `EXECUTION_BOUNDARY` |
| PTM-V26-002 | Sessão de observação possui identidade, estado, perfil, aplicação, monitor, ROIs e configuração versionada. | Perfis e calibração legados são `ADAPTAR`. | `OBSERVATION_SESSION_CONTRACT` |
| PTM-V26-003 | Apenas janela autorizada, identidade compatível e geometria aprovada podem originar frame elegível. | Dependência visual do legado exige fail-closed. | `AUTHORIZED_VISUAL_SOURCE` |
| PTM-V26-004 | Frame é referenciado por hash, tempo, origem, dimensões e política de retenção; imagem sensível não é persistida por padrão. | Artefatos locais e risco de versionamento são `ADAPTAR`. | `FRAME_PROVENANCE` |
| PTM-V26-005 | Validação de frame ocorre antes de extração e análise. | Não há pipeline analítico confirmado no legado; requisito novo. | `FRAME_VALIDATION_GATE` |
| PTM-V26-006 | Qualidade é multidimensional e produz blockers e confidence caps monotônicos. | Thresholds não medidos permanecem provisórios. | `QUALITY_MODEL` |
| PTM-V26-007 | Extrações visuais são versionadas, determinísticas para mesma entrada e rastreáveis ao frame e ROI. | Novo mecanismo; comportamento visual útil pode ser adaptado. | `VISUAL_EXTRACTION_CONTRACT` |
| PTM-V26-008 | Séries visuais, velas estimadas e mapeamentos de preço/tempo carregam incerteza e linhagem. | Não há market data estruturado confirmado no legado. | `ESTIMATED_MARKET_DATA` |
| PTM-V26-009 | Snapshot analítico é imutável e referencia exatamente seus inputs, versões e configuração. | Novo mecanismo. | `ANALYSIS_SNAPSHOT_IMMUTABILITY` |
| PTM-V26-010 | Motores A–H usam envelope comum de resultado e não mantêm estado oculto não versionado. | Contratos conceituais PTP-GOV.5. | `ENGINE_RESULT_ENVELOPE` |
| PTM-V26-011 | Motor A identifica estrutura, pivôs, pernas e mudanças estruturais com evidência. | Contrato histórico A. | `MARKET_STRUCTURE_ENGINE` |
| PTM-V26-012 | Motor B classifica direção, força, estabilidade e transição de tendência. | Contrato histórico B. | `TREND_ENGINE` |
| PTM-V26-013 | Motor C produz zonas com limites, tipo, validade, força e histórico de testes. | Contrato histórico C. | `ZONE_ENGINE` |
| PTM-V26-014 | Motor D classifica regime de volatilidade, expansão, contração e blockers. | Contrato histórico D. | `VOLATILITY_ENGINE` |
| PTM-V26-015 | Motor E mede candle e contexto visual com qualidade explícita. | Contrato histórico E. | `CANDLE_CONTEXT_ENGINE` |
| PTM-V26-016 | Motor F avalia momentum, aceleração e divergência estrutural. | Contrato histórico F. | `MOMENTUM_ENGINE` |
| PTM-V26-017 | Motor G agrega confluências e contradições sem ocultar evidências. | Contrato histórico G. | `CONFLUENCE_ENGINE` |
| PTM-V26-018 | Motor H aplica estratégia versionada e pode retornar espera, degradação, bloqueio ou candidato. | Contrato histórico H. | `STRATEGY_ENGINE` |
| PTM-V26-019 | Estratégias possuem definição, versão, regras, horizontes, blockers e testes vinculados. | Strategy-001 histórica é preliminar. | `STRATEGY_VERSIONING` |
| PTM-V26-020 | Candidatos passam por arbitragem determinística antes de sinal. | Catálogo lógico histórico. | `CANDIDATE_ARBITRATION` |
| PTM-V26-021 | Sinal final possui fingerprint, validade temporal, direção, confiança, qualidade, estabilidade e evidências. | Conceitos legados de sinal são `ADAPTAR`, sem execução. | `SIGNAL_CONTRACT` |
| PTM-V26-022 | Expiração, invalidação e supersessão são explícitas e auditáveis. | Histórico estruturado legado é `ADAPTAR`. | `SIGNAL_LIFECYCLE` |
| PTM-V26-023 | REST e eventos são progressivos: só existem com produtor, consumidor, requisito e teste. | Política V2.5. | `VERTICAL_CONTRACT_EXISTENCE` |
| PTM-V26-024 | Replay reproduz decisões documentais com inputs sanitizados e sem captura ou execução real. | Catálogo lógico histórico. | `SAFE_REPLAY` |
| PTM-V26-025 | Logs, métricas e auditoria correlacionam sessão, frame, snapshot, avaliação, candidato e sinal. | Observabilidade V2.5. | `ANALYSIS_OBSERVABILITY` |
| PTM-V26-026 | Segurança, redaction e minimização de dados aplicam-se a frames, OCR, artefatos, eventos e relatórios. | Segurança permanente. | `VISUAL_DATA_SECURITY` |
| PTM-V26-027 | Entidades físicas só nascem com produtor, consumidor, requisito, teste e retenção definidos. | Existência progressiva V2.5. | `PROGRESSIVE_PHYSICAL_SCHEMA` |
| PTM-V26-028 | Prova negativa verificável garante ausência de APIs de ponteiro, clique e ordem em todos os fluxos V2.6. | Risco crítico confirmado no legado. | `V2_6_REAL_INPUT_BLOCKED` |

## 6. Requisitos funcionais

### 6.1 Observação e captura

| ID | Critério de aceite arquitetural |
|---|---|
| V26-OBS-001 | Criar sessão somente com perfil, aplicação, monitor, ROIs e configuração resolvidos. |
| V26-OBS-002 | Iniciar em `VALIDATING`; somente transitar para `ACTIVE` após todos os checks obrigatórios. |
| V26-OBS-003 | Perda de identidade, geometria, frescor ou estabilidade degrada ou bloqueia a sessão. |
| V26-OBS-004 | Encerramento impede novos frames e preserva razão, último sequence e resumo. |
| V26-CAP-001 | Registrar referência do frame com hash, timestamp monotônico/UTC, dimensão, origem e sequence. |
| V26-CAP-002 | Recusar frame duplicado, fora de ordem, obsoleto ou proveniente de fonte não autorizada. |
| V26-CAP-003 | Recortes por ROI preservam vínculo com frame, perfil e versão geométrica. |
| V26-CAP-004 | Conteúdo bruto segue retenção mínima e redaction; referência pode sobreviver ao artefato. |

### 6.2 Validação e qualidade

| ID | Critério de aceite arquitetural |
|---|---|
| V26-VAL-001 | Validar identidade da janela e processo autorizado. |
| V26-VAL-002 | Validar perfil, resolução, escala, monitor, ROI e assinatura visual. |
| V26-VAL-003 | Validar frescor, completude, estabilidade, oclusão e qualidade de extração. |
| V26-VAL-004 | Cada check retorna `PASS`, `DEGRADED`, `FAIL` ou `UNKNOWN` com reason code. |
| V26-VAL-005 | `FAIL` obrigatório bloqueia; `UNKNOWN` nunca eleva elegibilidade. |
| V26-VAL-006 | Score agregado não pode superar o menor cap obrigatório aplicável. |

### 6.3 Extração e mapeamento

| ID | Critério de aceite arquitetural |
|---|---|
| V26-MAP-001 | Extração declara extractor/version, ROI, input hash, output hash e métricas. |
| V26-MAP-002 | Série visual preserva ordem, lacunas, duplicidades e origem de cada ponto. |
| V26-MAP-003 | Candle estimado declara incerteza de OHLC, tempo e qualidade; não é dado oficial da corretora. |
| V26-MAP-004 | Modelo preço-pixel e tempo-pixel é versionado, validado e limitado ao contexto compatível. |
| V26-MAP-005 | Mudança de escala, zoom, janela ou perfil invalida mapeamentos incompatíveis. |

### 6.4 Análise A–H

| ID | Critério de aceite arquitetural |
|---|---|
| V26-ANA-001 | Criar snapshot somente de frames e séries elegíveis e imutáveis. |
| V26-ANA-002 | Cada motor recebe input explícito e retorna envelope comum sem efeito colateral físico. |
| V26-ANA-003 | Motor A retorna estrutura e evidências ou `WAIT_MORE_DATA`/blocker. |
| V26-ANA-004 | Motor B retorna tendência por horizonte e transição. |
| V26-ANA-005 | Motor C retorna zonas versionadas e critérios de validade. |
| V26-ANA-006 | Motor D retorna regime de volatilidade e estabilidade. |
| V26-ANA-007 | Motor E retorna medidas e contexto de candles estimados. |
| V26-ANA-008 | Motor F retorna momentum e divergências estruturais. |
| V26-ANA-009 | Motor G agrega confluência, contradição e confidence cap. |
| V26-ANA-010 | Motor H avalia estratégia e não pode contornar blockers A–G. |
| V26-ANA-011 | Repetição com mesmos inputs e versões deve produzir resultado equivalente ou divergência explicada. |

### 6.5 Estratégia, candidatos e sinais

| ID | Critério de aceite arquitetural |
|---|---|
| V26-STR-001 | Strategy-001 usa estrutura + zona + confirmação, sem thresholds definitivos sem benchmark. |
| V26-STR-002 | Estratégia retorna `STRATEGY_WAIT`, `WAIT_MORE_DATA`, `DEGRADED`, `BLOCKED` ou candidato. |
| V26-STR-003 | Avaliação registra regras satisfeitas, falhas, blockers, evidências e configuração. |
| V26-STR-004 | Alteração de regra cria nova versão; resultados antigos mantêm sua versão. |
| V26-SIG-001 | Candidato possui fingerprint determinístico e janela de validade. |
| V26-SIG-002 | Arbitragem deduplica, resolve conflito e aplica prioridade de blockers. |
| V26-SIG-003 | Apenas candidato aceito e validado gera sinal. |
| V26-SIG-004 | Sinal contém direção, validade, confiança técnica, qualidade, estabilidade e cap. |
| V26-SIG-005 | Sinal expira automaticamente após a janela; não é executado. |
| V26-SIG-006 | Mudança de contexto ou evidência pode invalidar sinal com reason code. |
| V26-SIG-007 | Sinal pode ser exportado para lista simulada sem acionar agenda executável. |
| V26-SIG-008 | Nenhum estado usa `CLIQUE_ENVIADO`, `EXECUTADO` ou equivalente físico. |

### 6.6 Replay, contratos e segurança

| ID | Critério de aceite arquitetural |
|---|---|
| V26-RPL-001 | Replay usa pacote sanitizado, versões fixadas e relógio controlado. |
| V26-RPL-002 | Replay compara hashes, estados, reason codes e resultados esperados. |
| V26-RPL-003 | Replay não acessa corretora, ponteiro, teclado ou rede externa não autorizada. |
| V26-API-001 | Leituras e comandos documentais usam contratos versionados e idempotência quando mutáveis. |
| V26-API-002 | Eventos externos usam schema version, sequence, trace e snapshot fallback. |
| V26-SEC-001 | Segredos, tokens, nomes sensíveis e imagens não sanitizadas não entram em logs ou commits. |
| V26-SEC-002 | Dependência de captura ou OCR deve ser isolada por adaptador e feature gate seguro. |
| V26-SEC-003 | Quality gate inclui busca negativa por APIs de movimento, clique e ordem. |

## 7. Estados e lifecycle

```text
OBSERVATION_SESSION=CREATED|VALIDATING|ACTIVE|DEGRADED|BLOCKED|STOPPING|STOPPED|FAILED
FRAME=REFERENCED|VALIDATING|ACCEPTED|REJECTED|EXPIRED
ANALYSIS_SNAPSHOT=PENDING|RUNNING|READY|DEGRADED|BLOCKED|FAILED|SUPERSEDED
STRATEGY_EVALUATION=PENDING|EVALUATING|STRATEGY_WAIT|WAIT_MORE_DATA|CANDIDATE|DEGRADED|BLOCKED|FAILED
SIGNAL_CANDIDATE=PROPOSED|ARBITRATING|ACCEPTED|REJECTED|EXPIRED|INVALIDATED
SIGNAL=ACTIVE|EXPIRED|INVALIDATED|SUPERSEDED
```

Toda transição registra origem, destino, razão, UTC, trace, versão e evidência. Estado desconhecido é `BLOCKED` ou `DEGRADED`, nunca apto por padrão.

## 8. Modelo de qualidade e confiança

Representação recomendada: inteiro escalado `0..10000`, sem ponto flutuante como fonte canônica.

Dimensões mínimas:

```text
WINDOW_IDENTITY
PROFILE_COMPATIBILITY
ROI_COVERAGE
CAPTURE_FRESHNESS
VISUAL_STABILITY
EXTRACTION_QUALITY
MAPPING_CONFIDENCE
SERIES_COMPLETENESS
TEMPORAL_ALIGNMENT
ENGINE_STABILITY
```

Regras:

- dimensão ausente exige reason code;
- cap obrigatório é monotônico e conservador;
- confiança técnica nunca supera qualidade, estabilidade e elegibilidade;
- score não converte blocker em aprovação;
- thresholds iniciais são `PROVISIONAL` até benchmark reproduzível.

## 9. Envelope de resultado analítico

```text
analysis_engine_result_id
analysis_snapshot_id
engine_key
engine_version
horizon
input_hash
configuration_hash
status
technical_confidence_scaled
data_quality_scaled
stability_scaled
confidence_cap_scaled
reason_code
evidence_refs
result_payload_version
```

`result_json` pode existir como payload secundário, nunca como substituto de campos críticos e relações rastreáveis.

## 10. Strategy-001

```text
NAME=Strategy-001
PRINCIPLE=STRUCTURE_PLUS_ZONE_PLUS_CONFIRMATION
EXECUTOR_DEPENDENCY=NONE
THRESHOLDS=PROVISIONAL_UNTIL_BENCHMARK
EXPLAINABILITY=REQUIRED
```

Um candidato exige contexto estrutural válido, zona válida, confirmação definida, ausência de blocker e qualidade mínima. Falta de dados resulta em espera, não em direção presumida.

## 11. Contratos progressivos

Grupos previstos, não automaticamente físicos:

```text
/api/v1/observation
/api/v1/analysis
/api/v1/strategies
/api/v1/signals
/api/v1/replay
```

Eventos previstos:

```text
observation.state_changed
analysis.snapshot_ready
strategy.evaluated
signal.generated
signal.invalidated
```

Cada contrato só entra quando possuir produtor, consumidor, requisito, teste, schema versionado e política de erro.

## 12. Persistência conceitual

Entidades lógicas candidatas:

- observation sessions, contexts, events, capture metrics e frame references;
- frame validations, visual extractions e external artifacts;
- visual series, candle estimates e mapping models/samples;
- analysis snapshots, engine results, evidence e eligibility states;
- strategy definitions/evaluations, candidates, arbitrations e signals;
- replay packages/runs e test artifacts.

```text
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PHYSICAL_SCHEMA_DEFINED=NO
```

## 13. Reason codes mínimos

```text
WINDOW_NOT_AUTHORIZED
WINDOW_IDENTITY_MISMATCH
PROFILE_INCOMPATIBLE
ROI_INVALID
FRAME_STALE
FRAME_DUPLICATE
FRAME_OUT_OF_ORDER
FRAME_OCCLUDED
VISUAL_SIGNATURE_MISMATCH
EXTRACTION_FAILED
MAPPING_UNCERTAIN
SERIES_INCOMPLETE
WAIT_MORE_DATA
ENGINE_DEGRADED
ENGINE_BLOCKED
STRATEGY_WAIT
CANDIDATE_CONFLICT
CANDIDATE_DUPLICATE
SIGNAL_EXPIRED
SIGNAL_INVALIDATED_CONTEXT_CHANGE
REAL_INPUT_PROHIBITED
```

O catálogo final deve ser versionado, estável e sem textos livres como única fonte de decisão.

## 14. Evidências futuras exigidas

- testes unitários de regras puras e fingerprints;
- testes de contrato de envelopes, REST e eventos;
- fixtures sanitizadas de frames e séries;
- testes determinísticos dos motores A–H;
- testes de propriedades para qualidade, caps e lifecycle;
- benchmark documentado antes de threshold definitivo;
- replay sem acesso a fonte real;
- prova negativa de ausência de ponteiro, clique, teclado e ordem;
- relatório TXT e artefatos versionados conforme protocolo.

```text
TEST_SPEC_CREATED=PASS_BUILDER
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```

## 15. Riscos residuais

| Risco | Severidade | Tratamento |
|---|---|---|
| fonte visual instável ou ocluída | Alto | validação obrigatória e fail-closed |
| confiança artificialmente alta | Crítico | caps multidimensionais e blockers dominantes |
| thresholds arbitrários | Alto | provisórios até benchmark |
| OCR/extração não determinística | Alto | versão, hashes, métricas e replay |
| acoplamento oculto ao executor legado | Crítico | fronteira explícita e prova negativa |
| persistência física prematura | Alto | existência progressiva |
| dados visuais sensíveis | Alto | minimização, redaction e retenção |
| confusão entre sinal e execução | Crítico | lifecycle sem estados físicos |

## 16. Gates do builder

```text
V2_6_SCOPE_BOUNDARY=PASS_BUILDER
STRUCTURAL_REQUIREMENTS_DEFINED=28
FUNCTIONAL_REQUIREMENTS_DEFINED=55
REQUIREMENT_ID_UNIQUENESS=PASS_BUILDER
OBSERVATION_QUALITY_MODEL=PASS_BUILDER
ANALYSIS_ENGINE_CONTRACTS=PASS_BUILDER
SIGNAL_LIFECYCLE=PASS_BUILDER
EXECUTION_EXCLUSION=PASS_BUILDER
PROGRESSIVE_SCHEMA_POLICY=PASS_BUILDER
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
APPLICATION_EXECUTED=NO
PTM_V2_6_DEFINITIVE=NO
PTM_V2_6_CRITICAL_REVIEW=PENDING
```

## 17. Condição de avanço

A PTM V2.6 somente poderá ser integrada e tratada como documentalmente definitiva após:

```text
BUILDER_SELF_REVIEW=PASS
TRACEABILITY_COMPLETENESS=PASS
REQUIREMENT_ID_UNIQUENESS=PASS
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS
INDEPENDENT_CRITICAL_REVIEW=PASS
CRITICAL_BLOCKERS=0
```

Mesmo após esse gate, implementação e PTM V2.7 permanecem não autorizadas.