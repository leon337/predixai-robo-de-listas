# DOCUMENTO MESTRE DA ARQUITETURA V1.0

## PredixAI Robô de Listas — LEA-34

## DM-01 — Controle, autoridade e status

```text
DOCUMENT=DOCUMENTO_MESTRE_ARQUITETURA_V1
MISSION=LEA-34
DOCUMENT_STATUS=APPROVED_INTEGRATED_PENDING_ARCHITECTURE_FREEZE
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=65b18341c06a391ea48ae5029102ad7a095c3340
BASE_STATE_REVISION=18
DOCUMENTATION_ONLY=YES
ARCHITECTURE_VERSION=V1.0
REAL_PRODUCT_VERSION=V2.4.3-R1
REQUIREMENT_IDS=218
CANONICAL_DOMAINS=16
MANDATORY_HANDOFFS=12
ACCEPTED_ADRS=18
IMPLEMENTATION_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
```

### Autoridade por domínio documental

| Informação | Autoridade |
|---|---|
| estado operacional | `PROJECT_RUNTIME_STATE.yaml` |
| explicação humana | `PROJECT_STATE.md` |
| roadmap e continuidade | `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md` |
| tarefa, dependências e bloqueios | Linear |
| trabalho não integrado | branch e PR ativos |
| documentação consolidada | GitHub `main` |
| política A+B | `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` |
| decisões arquiteturais | ADR-0001 a ADR-0018 `ACCEPTED` |
| rastreabilidade | matrizes PTM e matriz consolidada LEA-18 |

Este documento consolida fontes aprovadas. Em divergência, prevalece a autoridade específica do domínio; histórico não substitui fonte viva.

## DM-02 — Propósito, escopo e limites

### Propósito

Definir a arquitetura lógica, responsabilidades, fronteiras, estados, contratos e gates do PredixAI Robô de Listas, preservando a cadeia completa entre intenção, observação, análise, sinal, autorização, ação controlada, recibo, reconciliação e auditoria.

### Escopo arquitetural

- servidor como autoridade global;
- cliente móvel como painel operacional e presença humana;
- listas e agendamentos independentes;
- captura e análise visual controladas;
- motores A–H determinísticos;
- lifecycle de candidatos e sinais;
- policy engine e grants explícitos;
- adaptadores `NULL`, `SIMULATED` e `CONTROLLED_UI`;
- suporte arquitetural futuro ao Modo B por gates separados;
- persistência conceitual de escritor único;
- segurança, auditoria, observabilidade, kill switch e recovery.

### Fora do escopo desta missão

```text
APPLICATION_CODE=NOT_AUTHORIZED
TEST_CODE=NOT_AUTHORIZED
PHYSICAL_DATABASE_SCHEMA=NOT_DEFINED
SQL=NOT_AUTHORIZED
MIGRATIONS=NOT_AUTHORIZED
RUNTIME_EXECUTION=NOT_AUTHORIZED
REAL_FINANCIAL_OPERATION=NOT_AUTHORIZED
LIVE_MODE=NOT_ARMED
INFRASTRUCTURE_DEPLOYMENT=NOT_AUTHORIZED
```

## DM-03 — Princípios e invariantes

```text
SERVER_STATE=GLOBAL_AUTHORITY
CLIENT_STATE=LOCAL_VIEW_NOT_GLOBAL_AUTHORITY
EXTERNAL_VISUAL_SOURCE=EVIDENCE_NOT_INTERNAL_AUTHORITY
FRAME_INVALID=ANALYSIS_BLOCKED
CANDIDATE!=SIGNAL
SIGNAL!=EXECUTION_COMMAND
EXECUTION_COMMAND!=AUTHORIZATION_GRANT
AUTHORIZATION_GRANT!=DISPATCH_ATTEMPT
DISPATCH_ATTEMPT!=CONFIRMED_EFFECT
ADAPTER_RECEIPT!=GLOBAL_TRUTH
COORDINATE!=TARGET_AUTHORIZATION
CONTROLLED_UI_ACTION!=LIVE_FINANCIAL_AUTHORIZATION
MODE_A_CONTROLLED_AUTOMATION=AUTHORIZED_WHEN_SCOPED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_WITHOUT_ALL_GATES=BLOCKED
UNKNOWN_DATA=CAPABILITY_REDUCTION
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
```

Princípios adicionais:

1. falhar fechado;
2. reduzir capacidade diante de incerteza;
3. registrar intenção antes de qualquer efeito;
4. separar autoridade, evidência e projeção;
5. preservar idempotência e rastreabilidade ponta a ponta;
6. criar persistência física apenas com produtor, consumidor, requisito, teste e retenção definidos;
7. manter segredos fora do Git;
8. não elevar silenciosamente Modo A para Modo B.

## DM-04 — Contexto, atores e topologia

### Atores

| Ator | Papel | Limite |
|---|---|---|
| operador humano | define intenção, confirma ações e pode interromper | não substitui validações técnicas |
| servidor local | autoridade global de estado, política e persistência | não presume efeito externo |
| cliente Android | painel, pareamento, presença e confirmação | não é autoridade global |
| fonte visual autorizada | fornece evidência observável | não é estado interno confiável |
| adaptador | executa canal declarado | não cria autorização |
| revisor independente | valida Boss Gates | não constrói o artefato revisado |
| GitHub | memória técnica e documental | não controla tarefa operacional |
| Linear | tarefa, bloqueios e progresso | não substitui documentação consolidada |

### Topologia lógica

```text
OPERADOR / ANDROID
        ↓ intenção, presença, confirmação
SERVIDOR DE AUTORIDADE
        ├─ GOVERNANÇA E CONFIGURAÇÃO
        ├─ LISTAS E AGENDAMENTOS
        ├─ PERFIS E GEOMETRIA
        ├─ OBSERVAÇÃO E ANÁLISE
        ├─ SINAIS E POLICY ENGINE
        ├─ ADAPTADORES E DISPATCH
        └─ PERSISTÊNCIA, AUDITORIA E RECOVERY
                ↓ canal explicitamente autorizado
        NULL | SIMULATED | CONTROLLED_UI | FUTURE_LIVE_GATED
```

## DM-05 — DOM-01 Governança e estado operacional

**Autoridade:** `PROJECT_RUNTIME_STATE.yaml`.

Responsabilidades:

- controlar missão, fase, gate, bloqueios e próxima ação;
- aplicar `state_revision` monotônica e `transition_id` idempotente;
- distinguir `main` de trabalho não integrado;
- bloquear escrita com baseline obsoleto;
- sincronizar manifesto, estado humano, tronco, Linear e README.

Estados canônicos de governança:

```text
STATE_STABLE
TRANSITION_IN_PROGRESS
SYNC_PENDING_GITHUB
SYNC_PENDING_LINEAR
SYNC_PARTIAL
STATE_CONFLICT
BLOCKED_BY_CONCURRENT_UPDATE
BLOCKED_BY_STATE_DRIFT
BLOCKED_BY_CONNECTOR_FAILURE
BLOCKED_BY_SCHEMA_MISMATCH
```

## DM-06 — DOM-02 Configuração, identidade e segredos

**Autoridade:** configuração resolvida, versionada e mantida no servidor.

Entradas: defaults seguros, arquivo autorizado, overrides explícitos e identidade do ambiente.

Saídas: snapshot de configuração, capacidades, reason codes e diagnóstico redigido.

Regras:

- resolução determinística;
- configuração inválida bloqueia capacidade crítica;
- feature flags possuem dependências e safe default;
- tokens, cookies, chaves privadas e credenciais nunca entram no Git;
- modo, alvo, allowlists e limites são explícitos;
- feature flag isolada não arma Modo B.

## DM-07 — DOM-03 Persistência, eventos, backup e recovery

**Autoridade:** fronteira única de escrita do servidor.

Decisões:

- SQLite é a opção arquitetural V1 para persistência local, conforme ADR-0002;
- cliente, rota ou handler não escreve diretamente;
- transações são curtas e preservam integridade;
- eventos externos críticos seguem outbox quando o fluxo existir;
- origem bruta do legado é preservada;
- backup, restore, reconciliação e rollback são verificáveis;
- schema físico nasce progressivamente, não por catálogo abstrato.

```text
ENTITY_EXISTS_PHYSICALLY_ONLY_IF=
PRODUCER_DEFINED
AND CONSUMER_DEFINED
AND REQUIREMENT_LINKED
AND TEST_LINKED
AND RETENTION_DEFINED_WHEN_HISTORICAL
```

Nenhuma tabela, migration ou SQL é definida neste documento.

## DM-08 — DOM-04 Listas, itens e agendamentos

**Autoridade:** domínio de listas no servidor.

Responsabilidades:

- CRUD independente de observação e execução;
- revisão versionada de listas e itens;
- validação de data, horário, direção, identidade, duplicidade e consistência;
- importação do schema legado com aceitos, rejeitados e normalizados;
- fornecimento de contexto versionado para sessão de observação.

Não pode:

- produzir sinal;
- chamar adaptador;
- converter item em autorização.

## DM-09 — DOM-05 Clientes, dispositivos e presença humana

Responsabilidades:

- pareamento local, revogável e auditável;
- identificação de dispositivo e sessão;
- reconexão por sequência e snapshot;
- confirmação humana explícita quando exigida;
- manutenção do servidor em `SAFE_IDLE` quando o cliente estiver ausente ou desconectado.

Presença não é grant. Reconexão não rearma comando anterior.

## DM-10 — DOM-06 Perfis, calibração, ROIs e geometria

Responsabilidades:

- versionar aplicação, monitor, resolução, escala, ROIs, âncoras e alvos;
- permitir captura geométrica no Modo A controlado;
- validar compatibilidade antes de observação ou resolução de alvo;
- gerar `target_logical_id` e geometria versionada.

```text
COORDINATE_CAPTURE=GEOMETRIC_EVIDENCE
COORDINATE_CAPTURE!=AUTHORIZATION
TARGET_LOGICAL_ID_PLUS_ALLOWLIST=REQUIRED_FOR_DISPATCH
```

## DM-11 — DOM-07 e DOM-08 Observação, captura e proveniência

### Sessão de observação

Uma sessão vincula perfil ativo, fonte visual autorizada, monitor, ROIs e configuração resolvida. Perda de identidade, estabilidade ou compatibilidade degrada ou bloqueia a sessão.

### Captura e frame

Cada frame elegível carrega:

- `session_id`;
- origem autorizada;
- sequência;
- timestamps aplicáveis;
- hash;
- versão do perfil e ROI;
- decisão de retenção;
- linhagem dos recortes.

Retenção visual é mínima e orientada por necessidade, com redaction e proteção de dados sensíveis.

## DM-12 — DOM-09 e DOM-10 Validação, extração e dados estimados

### Validação

Checks mínimos:

- identidade da fonte;
- compatibilidade geométrica;
- frescor;
- sequência;
- completude;
- estabilidade;
- assinatura visual;
- qualidade suficiente.

`UNKNOWN` reduz capacidade e não é aprovação.

### Extração

OCR e extração controlados produzem dados estimados com:

- versão do extrator;
- versão do mapping;
- incerteza;
- lacunas explícitas;
- linhagem até o frame;
- distinção entre estimado e oficial.

## DM-13 — DOM-11 e DOM-12 Motores A–H, estratégia e sinais

### Motores A–H

Os motores operam sobre snapshot imutável e elegível. Resultados são determinísticos ou têm divergência explicada. Estado oculto é proibido.

Saídas arquiteturais abrangem estrutura, tendência, zonas, volatilidade, contexto de candle, momentum, confluência e avaliação de estratégia.

### Estratégia, candidatos e sinais

- estratégia é versionada;
- candidato não é sinal;
- arbitragem é explícita;
- sinal possui fingerprint, validade, evidências, expiração e invalidação;
- qualidade e blockers limitam confiança;
- sinal não autoexecuta.

## DM-14 — DOM-13 Comando, autorização e policy engine

Cadeia obrigatória:

```text
ELIGIBLE_SIGNAL
→ IMMUTABLE_COMMAND
→ EXPLICIT_POLICY_DECISION
→ AUTHORIZATION_GRANT
→ PRECONDITION_REVALIDATION
→ DISPATCH_READINESS
```

O grant vincula:

- ator;
- canal;
- alvo lógico;
- ação;
- allowlist;
- limites;
- validade;
- snapshot de pré-condições;
- modo de efeito financeiro.

Estados previstos:

```text
DISABLED
SAFE_IDLE
VALIDATING
ARMED_DRY_RUN
ARMED_SIMULATED
ARMED_CONTROLLED_UI
ARMED_LIVE_GATED
BLOCKED
CANCELLED
KILLED
```

`ARMED_LIVE_GATED` exige todos os gates técnicos, comerciais, legais, regulatórios e de conformidade aplicáveis.

## DM-15 — DOM-14 Alvos, adaptadores e canais de execução

Canais declarados:

| Canal | Efeito permitido | Estado padrão |
|---|---|---|
| `NULL` | valida fluxo sem efeito | permitido em teste futuro |
| `SIMULATED` | produz resultado simulado | suportado, sem efeito financeiro real |
| `CONTROLLED_UI` | ação de interface em alvo autorizado | permitido no Modo A quando missão e alvo forem autorizados |
| `LIVE_GATED` | efeito financeiro real | somente capacidade arquitetural; desligado |

Regras:

- alvo lógico e allowlist precedem resolução geométrica;
- biblioteca de UI fica confinada ao adaptador;
- coordenada isolada não autoriza dispatch;
- `CONTROLLED_UI` não prova nem autoriza resultado financeiro;
- adaptador real futuro exige contrato e gate próprios.

## DM-16 — DOM-15 Dispatch, recibo, reconciliação e recovery

Responsabilidades:

- registrar intenção antes do efeito;
- aplicar idempotência, dedupe, serialização, deadline e circuit breaker;
- separar `ui_result` de `financial_result`;
- correlacionar tentativa, recibo e observação;
- tratar timeout como efeito desconhecido, não como ausência de efeito;
- impedir retry sem prova de ausência de efeito;
- não reenviar comando anterior após restart.

Estados de resultado incluem:

```text
COMPLETED_NO_EFFECT
COMPLETED_SIMULATED
COMPLETED_CONTROLLED_UI
COMPLETED_LIVE_GATED
TIMED_OUT
UNKNOWN_EFFECT
FAILED_NO_EFFECT
KILLED
```

O recibo do adaptador é evidência local. A verdade global só surge após reconciliação do servidor.

## DM-17 — DOM-16 Segurança, auditoria, observabilidade e contenção

Responsabilidades transversais:

- logs estruturados com redaction;
- auditoria append-only adequada ao risco;
- métricas com produtor, consumidor, retenção e custo conhecidos;
- correlação por `trace_id`, `command_id` e `authorization_id`;
- alertas e diagnósticos sanitizados;
- kill switch dominante;
- circuit breaker;
- evidência de bloqueios e provas negativas.

Provas negativas obrigatórias em implementação futura:

```text
ANALYSIS_ENGINE_DIRECT_UI_ACTION=BLOCK
UNCONTROLLED_UI_ACTION=BLOCK
UNAUTHORIZED_EXTERNAL_ACCESS=BLOCK
PRODUCTION_SECRET_IN_GIT=BLOCK
MODE_A_TO_UNGATED_LIVE_EFFECT=BLOCK
LIVE_WITHOUT_ALL_GATES=BLOCK
PRE_RESTART_COMMAND_REDISPATCH=BLOCK
TARGET_NOT_ALLOWLISTED=BLOCK
```

## DM-18 — Contratos, estados e versionamento

### Contratos

- REST JSON versionado para operações síncronas;
- SSE para eventos unidirecionais quando aplicável;
- contratos com schema, versionamento e reason codes estáveis;
- produtor, consumidor e teste antes de expansão física;
- `trace_id` propagado de ponta a ponta.

### Estados

Toda transição registra origem, destino, condição, ator, reason code, timestamp e evidência.

Máquinas de estado mínimas:

1. sistema e servidor;
2. sessão de observação;
3. candidato e sinal;
4. comando e autorização;
5. dispatch e reconciliação;
6. migração e recovery;
7. calibração e perfis.

## DM-19 — Migração do legado e compatibilidade

Princípio:

```text
PRESERVAR_COMPORTAMENTO_UTIL != PRESERVAR_MECANISMO_LEGADO
```

### Reutilizar

- conceitos de perfil, lista, sinal e sessão;
- preflight temporal puro;
- evidências históricas e testes úteis;
- leitura de versão e fallbacks válidos.

### Adaptar

- geometria, listas, agenda e históricos;
- lock, logging, diagnóstico, backup e recovery;
- scripts Linux e cobertura de testes;
- JSON schema 4 apenas como fonte de migração.

### Substituir

- monkey patches e composição por ordem de instalação;
- monólito Tkinter como autoridade de domínio;
- JSON como fonte final de verdade;
- workflows fragmentados como único quality gate.

### Descontinuar no baseline arquitetural

- elevação automática de modo;
- ação física não declarada;
- clique como confirmação de resultado financeiro;
- retry automático em efeito desconhecido.

Migração futura exige inventário, manifesto, backup verificado, transformação determinística, reconciliação por contagens e hashes e rollback demonstrável.

## DM-20 — Estratégia de testes e evidências

Princípio:

```text
TEST_SPEC_CREATED != TEST_RUNTIME_EXECUTED
CI_GREEN != RUNTIME_GATES_PASS
```

Camadas futuras:

| Família | Objetivo |
|---|---|
| `T-GOV-*` | estado, revisão, transição e drift |
| `T-CFG-*` | configuração, identidade, segredos e fail-closed |
| `T-DB-*` | writer único, integridade, backup e recovery |
| `T-LIST-*` | listas, agenda e importação |
| `T-OBS-*` | sessão e fonte visual |
| `T-CAP-*` | captura, proveniência e retenção |
| `T-VAL-*` | validação visual e bloqueios |
| `T-MAP-*` | OCR, extração, mapping e incerteza |
| `T-ANA-*` | motores A–H e determinismo |
| `T-SIG-*` | estratégia, candidato e lifecycle de sinais |
| `T-CMD-*` | comando, grant, revogação e policy engine |
| `T-ADP-*` | alvo, allowlist e adaptadores |
| `T-EXE-*` | dispatch, idempotência, timeout e circuito |
| `T-REC-*` | recibo, reconciliação, restart e compensação |
| `T-SEC-*` | redaction, auditoria, kill switch e provas negativas |
| `T-E2E-*` | fluxos verticais `NULL`, simulados e controlados |

Nesta missão, essas famílias são especificação de rastreabilidade; nenhum teste executável foi criado ou executado.

## DM-21 — Rastreabilidade de requisitos e ADRs

A matriz complementar preserva:

```text
REQUIREMENT_ID
→ PTM_SOURCE
→ PRIMARY_DOMAIN
→ HANDOFFS
→ ADR_IDS
→ DOCUMENT_MASTER_SECTION
→ FUTURE_TEST_IDS
```

Resultados esperados:

```text
V2_5=56/56
V2_6=78/78
V2_7=84/84
TOTAL=218/218
DUPLICATES=0
ORPHANS=0
ADRS=18/18
```

### ADRs incorporados

| ADR | Decisão consolidada | Seções principais |
|---|---|---|
| ADR-0001 | servidor e autoridade global | DM-04, DM-05 |
| ADR-0002 | SQLite V1 e escritor único | DM-07 |
| ADR-0003 | REST, SSE e versionamento | DM-18 |
| ADR-0004 | identidade e pareamento | DM-09 |
| ADR-0005 | perfis, ROIs e alvo lógico | DM-10, DM-15 |
| ADR-0006 | motores A–H | DM-13 |
| ADR-0007 | estratégia e lifecycle de sinais | DM-13 |
| ADR-0008 | FSMs de execução | DM-14, DM-16, DM-18 |
| ADR-0009 | adaptadores e Modos A/B | DM-15 |
| ADR-0010 | kill switch dominante | DM-17 |
| ADR-0011 | idempotência, recibo e reconciliação | DM-16 |
| ADR-0012 | observabilidade, auditoria e redaction | DM-17 |
| ADR-0013 | migrations e importação idempotente | DM-19 |
| ADR-0014 | retenção de frames | DM-11, DM-17 |
| ADR-0015 | serialização e circuit breaker | DM-16, DM-17 |
| ADR-0016 | relógios, deadlines e identidade de processo | DM-16, DM-18 |
| ADR-0017 | thresholds versionados | DM-12, DM-13 |
| ADR-0018 | testes e evidência por camada | DM-20 |

## DM-22 — Limites de implementação e roadmap

A arquitetura V1.0 define o destino normativo. Não escolhe, sem missão posterior:

- estrutura física de diretórios e módulos;
- schema SQL e migrations;
- biblioteca concreta de servidor, cliente ou captura;
- thresholds finais;
- topologia de deploy;
- taxonomia completa de `target_logical_id`;
- infraestrutura externa;
- cronograma e orçamento;
- autorização comercial, legal ou regulatória para Modo B.

Roadmap após aprovação deste documento:

```text
DOCUMENTO_MESTRE
→ REVISÃO CRÍTICA INDEPENDENTE
→ REMEDIAÇÃO E RETESTE SE NECESSÁRIO
→ MERGE AUTORIZADO
→ CONFIRMAÇÃO PÓS-MERGE
→ CONGELAMENTO DA ARQUITETURA V1.0
→ REVISÃO DE PRONTIDÃO PARA IMPLEMENTAÇÃO
→ GO | GO_WITH_CONDITIONS | NO_GO
```

## DM-23 — Gates de aceitação e fechamento

```text
BASELINE_AND_AUTHORITY=PASS
MASTER_STRUCTURE=PASS_BUILDER
CANONICAL_DOMAINS=16/16
MANDATORY_HANDOFFS=12/12
REQUIREMENTS_TRACEABLE=218/218_PENDING_MATRIX_VALIDATION
ADRS_REFERENCED=18/18
POLICY_A_B_ALIGNMENT=PASS_BUILDER
ARCHITECTURE_IMPLEMENTATION_BOUNDARY=PASS_BUILDER
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
SQL_CREATED=NO
MIGRATION_CREATED=NO
RUNTIME_EXECUTED=NO
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
MERGE_AUTHORIZATION=REQUIRED
POST_MERGE_CONFIRMATION=REQUIRED
```

Este Draft somente pode ser promovido após validação da matriz, CI documental e revisão crítica independente.

## DM-24 — Mapa canônico de desenvolvimento

Esta seção é a autoridade canônica da sequência de desenvolvimento. Os anexos de DM-33 detalham a matriz, o catálogo, o grafo e as políticas, mas não constituem roadmap paralelo e não podem substituir, contradizer ou ampliar este Documento Mestre.

```text
ROADMAP_AUTHORITY=DOCUMENTO_MESTRE
ROADMAP_STATUS=CANDIDATE_AWAITING_INDEPENDENT_RETEST
ARCHITECTURE_V1_CHANGED=NO
IMPLEMENTATION_AUTHORIZED=NO
NEXT_CODE_INCREMENT_AUTHORIZED=NO
```

| Ordem | ID e nome | Objetivo executivo | Depende de | Modo máximo | Situação | Gate de entrada | Gate de saída | Próxima etapa |
|---:|---|---|---|---|---|---|---|---|
| 1 | `FND-001` Safe Server Foundation | autoridade modular, contratos, fail-closed e adaptador NULL | Arquitetura V1.0 | `NULL_ONLY` | integrada | baseline congelada + autorização consumida | `FND-001_EXIT_PASS` | FND-002 |
| 2 | `FND-002` Safe Runtime Read Model | leitura de estado, auditoria e diagnóstico sem mutação | FND-001 | `NULL_ONLY` | integrada | FND-001 PASS + autorização consumida | `FND-002_EXIT_PASS` | FND-003 |
| 3 | `FND-003` Identity, Configuration and Client Trust | identidade, segredos, pareamento, revogação e presença | FND-002 | `NULL_ONLY` | candidata, não autorizada | predecessor PASS + missão humana | `FND-003_EXIT_PASS` | DAT-001 |
| 4 | `DAT-001` Durable State and Legacy Migration | escritor único, persistência, eventos, backup, restore e importação | FND-003 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `DAT-001_EXIT_PASS` | LST-001 |
| 5 | `LST-001` Lists and Scheduling | listas, itens, revisões e agenda sem efeito | DAT-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `LST-001_EXIT_PASS` | PRF-001 |
| 6 | `PRF-001` Profiles, ROIs and Logical Geometry | perfis, ROIs, calibração e identidade lógica | LST-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `PRF-001_EXIT_PASS` | OBS-001 |
| 7 | `OBS-001` Authorized Observation Session | sessão vinculada a contexto, perfil e fonte autorizada | PRF-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `OBS-001_EXIT_PASS` | CAP-001 |
| 8 | `CAP-001` Frame Capture and Provenance | hash, origem, sequência, ROI, linhagem e retenção | OBS-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `CAP-001_EXIT_PASS` | VAL-001 |
| 9 | `VAL-001` Visual Quality Gate | checks de qualidade, elegibilidade, blockers e caps | CAP-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `VAL-001_EXIT_PASS` | MAP-001 |
| 10 | `MAP-001` Estimated Data Extraction | extração estimada com mapping, incerteza e linhagem | VAL-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `MAP-001_EXIT_PASS` | ANA-001 |
| 11 | `ANA-001` Deterministic Engines A-H | motores determinísticos sobre snapshot elegível | MAP-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `ANA-001_EXIT_PASS` | SIG-001 |
| 12 | `SIG-001` Strategy and Signal Lifecycle | estratégia, candidatos, sinais, expiração e invalidação | ANA-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `SIG-001_EXIT_PASS` | CMD-001 |
| 13 | `CMD-001` Command, Grant and Policy Engine | comando imutável, grant, revogação e revalidação | SIG-001 | `NULL_ONLY` | bloqueada | predecessor PASS + missão humana | `CMD-001_EXIT_PASS` | ADP-001 |
| 14 | `ADP-001` Allowlisted Target and Simulated Adapter | alvo allowlisted e adaptadores NULL/SIMULATED | CMD-001 | `SIMULATED` | bloqueada | predecessor + gate SIMULATED + missão humana | `ADP-001_EXIT_PASS` | EXE-001 |
| 15 | `EXE-001` Simulated Dispatch, Receipt and Recovery | dispatch simulado, idempotência, recibo e recovery | ADP-001 | `SIMULATED` | bloqueada | predecessor PASS + missão humana | `EXE-001_EXIT_PASS` | SEC-001 |
| 16 | `SEC-001` Containment, Observability and Cumulative Simulation | contenção, auditoria, provas negativas e E2E acumulado | EXE-001 | `SIMULATED` | bloqueada | predecessor PASS + missão humana | `SEC-001_EXIT_PASS` | CUI-001 |
| 17 | `CUI-001` Controlled UI Capability | UI em alvo próprio/controlado, sem corretora ou efeito financeiro | SEC-001 | `CONTROLLED_UI` | bloqueada | missão própria + revisão independente + autorização humana | `CUI-001_EXIT_PASS` | LIV-GATE-001 |
| 18 | `LIV-GATE-001` Future LIVE_GATED Change Control | decisão futura técnica, comercial, jurídica, regulatória e humana | CUI-001 | `LIVE_GATED_CAPABILITY_ONLY` | bloqueada sem liberação automática | change control futuro completo | `FUTURE_LIVE_DECISION_RECORDED` | nenhuma automática |

```text
INCREMENT_COUNT=18
COMPLETED_INCREMENTS=2
NEXT_INCREMENT=FND-003
NEXT_INCREMENT_AUTHORIZED=NO
AMBIGUOUS_NEXT_INCREMENT=0
```

## DM-25 — Regras de decomposição incremental

Cada incremento deve ter fundamento em requisito, domínio, handoff e ADR existentes; resultado testável; escopo e fora de escopo; dependências; modo máximo; gates objetivos; testes; validação local; evidência; rollback; versão e próximo incremento inequívoco. Ausência de fundamento normativo bloqueia a unidade.

```text
DESENVOLVER_PEQUENO
→ TESTAR_NOVA_ETAPA
→ TESTAR_ETAPAS_ANTERIORES
→ TESTAR_INTEGRAÇÕES_AFETADAS
→ TESTAR_FLUXO_COMPLETO_ACUMULADO
→ SINCRONIZAR_REPOSITÓRIO_LOCAL
→ EXECUTAR_TESTE_LOCAL
→ GERAR_RELATÓRIO_TXT
→ CORRIGIR_SE_NECESSÁRIO
→ REVISAR
→ INTEGRAR
→ LIBERAR_PRÓXIMA_ETAPA
```

## DM-26 — Grafo macro de precedência

A precedência normativa é linear para que exista uma única próxima unidade liberável. Paralelismo interno só pode ocorrer como submissão da mesma missão, sem abrir duas próximas autoridades de incremento.

```text
FND-001→FND-002→FND-003→DAT-001→LST-001→PRF-001
→OBS-001→CAP-001→VAL-001→MAP-001→ANA-001→SIG-001
→CMD-001→ADP-001→EXE-001→SEC-001→CUI-001→LIV-GATE-001

DEPENDENCY_CYCLES=0
MISSING_DEPENDENCIES=0
UNKNOWN_INCREMENT_REFERENCES=0
AMBIGUOUS_NEXT_INCREMENT=0
```

## DM-27 — Política de versionamento

FND-001 e FND-002 mantêm a versão operacional histórica `V2.4.3-R1`; sufixos de evidência não as renumeram. Incrementos futuros usam pre-releases previstos no catálogo. Promoção exige commit, PR, issue Linear, requisitos cobertos, testes, relatório local e referência de rollback.

```text
VERSION_PROMOTION_REQUIRES=ALL_MANDATORY_GATES_PASS
TAG_CANDIDATE_BEFORE_LOCAL_AND_INDEPENDENT_PASS=NO
INTEGRATED_VERSION_REQUIRES=AUTHORIZED_MERGE_PLUS_POST_MERGE_RECEIPT
```

## DM-28 — Sincronização e validação local

Cada missão de incremento deve entregar um script all-in-one fail-closed para Linux Mint. Leo executa um único comando e não cria branch, commit, push, PR, stash nem resolve divergência Git no fluxo normal.

```text
LOCAL_SYNC_COMMAND=bash scripts/local_validate_<incremento>.sh --expected-commit <CANDIDATE_HEAD>
EXPECTED_COMMIT=FIXED_AT_CANDIDATE_HEAD
REPORT_PATH=reports/local/<incremento>_<commit>.txt
MISSING_REAL_LOCAL_EVIDENCE=⏳ AGUARDANDO EXECUÇÃO DO LEO
```

## DM-29 — Testes cumulativos e regressão

Na etapa N, executar testes da nova etapa, toda regressão de 1 a N-1, integrações afetadas e o fluxo acumulado de 1 a N. Teste antigo não pode ser removido, desabilitado ou ignorado para permitir avanço.

```text
STAGE_N_CAN_ADVANCE_ONLY_IF=
STAGES_1_TO_N_PASS
AND CUMULATIVE_INTEGRATION_PASS
AND LOCAL_TEST_PASS
AND TECHNICAL_DEBT_GATE_PASS
```

Conclusão também exige `CODE_COMPLETE`, unitários, integração, regressão anterior, fluxo cumulativo, provas negativas, CI, revisão crítica independente, Linux Mint, relatório TXT e sincronização GitHub–Linear em `PASS`.

## DM-30 — Gates NULL_ONLY, SIMULATED, CONTROLLED_UI e LIVE_GATED

```text
NULL_ONLY→SIMULATED→CONTROLLED_UI→LIVE_GATED
REAL_FINANCIAL_EFFECT=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
LIVE_MODE_ARMED=NO
```

Cada elevação exige missão própria, revisão crítica independente e autorização humana. `LIVE_GATED` é capacidade arquitetural futura e não é liberação automática do mapa. Requer decisões técnica, comercial, jurídica, regulatória e de conformidade.

## DM-31 — Rollback e controle de dívida técnica

Cada incremento reverte pelo PR, restaura a referência do predecessor e reexecuta regressão cumulativa. Dívida deve existir no Linear com risco, origem, impacto, responsável, gate de correção e decisão explícita. Dívida crítica ou bloqueadora impede avanço; dívida silenciosa é proibida.

```text
INCREMENT_WITHOUT_ROLLBACK=0
CRITICAL_OR_BLOCKING_TECHNICAL_DEBT=BLOCKS_ADVANCE
TECHNICAL_DEBT_GATE=PASS_REQUIRED
```

## DM-32 — Controle de mudanças do mapa

Alteração de ordem, ID, dependência, modo, gate, requisito ou anexo normativo exige missão documental, justificativa rastreável, revisão crítica independente e autorização humana antes do merge. Se a mudança exigir alterar a Arquitetura V1.0, registrar `BLOCKED_BY_ARCHITECTURE_CHANGE_REQUIRED`, identificar impactos e abrir change control; nenhuma solução silenciosa é permitida.

```text
ARCHITECTURE_V1_CHANGED=NO
NEW_REQUIREMENTS_CREATED=0
NEW_DOMAINS_CREATED=0
NEW_HANDOFFS_CREATED=0
NEW_ADRS_CREATED=0
```

## DM-33 — Índice de anexos normativos

Todos os anexos abaixo declaram `DOCUMENT_TYPE=NORMATIVE_ANNEX`, `PARENT_AUTHORITY=DOCUMENTO_MESTRE`, `CAN_OVERRIDE_MASTER=NO` e `REQUIRED_FOR_MASTER_VALIDITY=YES`:

1. `ANEXO_NORMATIVO_MATRIZ_218_REQUISITOS_INCREMENTOS_LEA_50_20260720.md` — cadeia verificável requisito → incremento → teste → gate → versão;
2. `ANEXO_NORMATIVO_CATALOGO_INCREMENTOS_LEA_50_20260720.md` — decomposição executiva completa dos 18 incrementos;
3. `ANEXO_NORMATIVO_GRAFO_PRECEDENCIA_INCREMENTOS_LEA_50_20260720.md` — dependências, estados e liberação de capacidades;
4. `ANEXO_NORMATIVO_POLITICAS_EXECUCAO_INCREMENTAL_LEA_50_20260720.md` — regressão, sincronização local, versionamento e dívida técnica.

O Documento Mestre prevalece. Anexo divergente invalida a candidatura até remediação; nunca prevalece sobre o mestre.
