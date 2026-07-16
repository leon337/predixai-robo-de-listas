# CHECKPOINT HISTÓRICO COMPLETO — PTP-GOV.5

## PredixAI Robô de Listas — Arquitetura V2.5 a V2.7

---

## 0. Identificação e autoridade

- **Projeto:** PredixAI Robô de Listas
- **Repositório oficial:** `leon337/predixai-robo-de-listas`
- **Branch técnica de referência:** `main`
- **Versão real atual do legado:** `V2.4.3-R1`
- **PTP ativa:** `PTP-GOV.5 — Memória e Governança Documental`
- **Data de consolidação:** 2026-07-16
- **Status:** HISTÓRICO INTEGRAL DE ENGENHARIA — BASE DE CONTINUIDADE
- **Natureza:** arquitetura conceitual, rastreabilidade preliminar, governança, erros, decisões e próximos gates
- **Implementação V2.5:** NÃO AUTORIZADA

Este documento registra o trabalho arquitetural realizado nesta sessão. Ele não substitui o código, não declara implementação concluída e não transforma hipóteses em fatos do legado. O estado real da aplicação deve sempre ser confirmado no repositório oficial.

---

# 1. Objetivo da sessão

A sessão foi aberta para concluir as definições arquiteturais que faltavam antes da criação do Documento Mestre do PredixAI Robô de Listas.

Foram trabalhados doze pontos:

1. Estrutura do servidor e clientes.
2. Contratos REST e WebSocket.
3. Banco SQLite e tabelas.
4. Lista inicial de ROIs.
5. Lista inicial de pontos de clique.
6. Frequência de leitura de cada ROI.
7. Arquitetura da análise de gráfico.
8. Estratégia Android mobile-first.
9. Compatibilidade Linux e Windows.
10. Política de testes reais, sintéticos e replay.
11. Estrutura definitiva de diretórios.
12. Sequência V2.5, V2.6 e V2.7.

O objetivo não era implementar. Era amadurecer, revisar, cruzar e congelar conceitualmente os contratos necessários para que o Documento Mestre se tornasse executável por etapas.

---

# 2. Estado inicial recebido

O projeto já possuía uma aplicação legada funcional na linha `V2.4.3-R1`, com interface desktop, listas de sinais, perfis de coordenadas, persistência local e evolução recente em ferramentas, logs, backups e diagnóstico.

O planejamento futuro deveria preservar o legado, evitar reescrita destrutiva e migrar progressivamente para uma arquitetura com:

```text
servidor central
+ SQLite
+ desktop como cliente
+ Android mobile-first
+ contratos REST/WebSocket
+ captura e análise desacopladas
+ execução controlada apenas em fase posterior
```

Desde o início ficou estabelecido que arquitetura futura e estado real do legado não poderiam ser confundidos.

---

# 3. Resultado geral dos doze pontos

## 3.1 Situação consolidada

```text
PONTO_1_SERVIDOR_CLIENTES=FECHADO_CONCEITUALMENTE
PONTO_2_REST_WEBSOCKET=FECHADO_CONCEITUALMENTE
PONTO_3_SQLITE=FECHADO_CONCEITUALMENTE
PONTO_4_ROIS=FECHADO_CONCEITUALMENTE
PONTO_5_CLICK_TARGETS=FECHADO_CONCEITUALMENTE
PONTO_6_FREQUENCIAS=FECHADO_COM_BASELINE_PROVISORIA
PONTO_7_ANALISE_GRAFICO=FECHADO_CONCEITUALMENTE
PONTO_8_ANDROID_MOBILE_FIRST=FECHADO_CONCEITUALMENTE
PONTO_9_LINUX_WINDOWS=FECHADO_COM_SUPORTE_PROGRESSIVO
PONTO_10_TESTES=FECHADO_CONCEITUALMENTE
PONTO_11_DIRETORIOS=FECHADO_CONCEITUALMENTE
PONTO_12_VERSOES=FECHADO_CONCEITUALMENTE
```

Esses pontos representam arquitetura desejada. A Auditoria Mestra ainda precisa confirmar como cada decisão se relaciona com o código real da `V2.4.3-R1`.

---

# 4. Ponto 1 — Estrutura do servidor e clientes

## 4.1 Decisão central

O servidor será a fonte global de verdade operacional e persistente.

```text
Servidor
├── domínio
├── persistência
├── lifecycle
├── contratos externos
├── segurança
├── captura/análise em versões futuras
└── publicação de eventos

Desktop
├── calibração
├── diagnóstico
├── confirmação física
└── compatibilidade temporária com legado

Android
├── painel operacional principal
├── cache local
├── comandos
├── monitoramento
└── reconexão
```

## 4.2 Autoridade de estado

```text
Memória do domínio = estado instantâneo
SQLite = estado persistente confirmado
REST = consulta e sincronização explícita
WebSocket = notificação de alterações
Room Android = último estado conhecido, sem autoridade global
```

## 4.3 Restrições

- Android e desktop não acessam o arquivo SQLite.
- Nenhum cliente redefine o estado global sozinho.
- O servidor deve iniciar em `SAFE_IDLE` mesmo sem Android conectado.
- O desktop não pode voltar a ser um monólito com acesso direto ao domínio e ao banco.

---

# 5. Ponto 2 — Contratos REST, WebSocket e eventos internos

## 5.1 Fronteiras

```text
REST = consulta, comando e sincronização explícita
WebSocket = atualização externa em tempo real
Internal Event Bus = comunicação entre módulos do servidor
Transactional Outbox = garantia de publicação externa após commit
```

## 5.2 Princípios

- contratos versionados;
- payloads validados;
- `reason_code` estável;
- `trace_id` transversal;
- `command_id` para comandos;
- sequência crescente em eventos WebSocket;
- snapshot completo quando o replay de eventos não estiver disponível;
- nenhum evento crítico publicado antes do commit.

## 5.3 Reconexão

Na V2.5, o buffer WebSocket principal foi definido como memória limitada.

```text
cliente reconecta
→ informa última sequence
→ servidor tenta replay em memória
→ se indisponível, envia snapshot completo
```

Eventos críticos permanecem protegidos pela outbox, mas não foi tornada obrigatória uma tabela física de buffer completo na V2.5.

---

# 6. Ponto 3 — Banco SQLite

Este foi o ponto mais extenso da sessão.

## 6.1 Princípios globais

- SQLite é fonte persistente do servidor.
- Apenas o servidor acessa o banco.
- Escritas passam por fila/escritor único.
- WAL e foreign keys são obrigatórios.
- Transações devem ser curtas.
- Arquivos grandes ficam fora do banco, catalogados por metadados.
- Migrations publicadas são imutáveis.
- Alteração de risco exige backup verificado.
- Schema lógico completo não implica criação física antecipada.

## 6.2 Identidades

```text
UUID público = entidades distribuídas e contratos externos
INTEGER interno = tabelas de alto volume quando justificado
```

## 6.3 Tempo e números

```text
timestamps operacionais = UNIX microssegundos UTC
agenda civil = data local + timezone IANA + ocorrência UTC
valores monetários = INTEGER em unidade mínima
preços/medições = INTEGER escalado
confiança/proporções = escala padrão 0–10000
```

## 6.4 Política de exclusão

- Configurações: arquivamento ou exclusão lógica quando houver ação real do usuário.
- Histórico crítico: estados finais e retenção protegida.
- Alta frequência: exclusão física controlada pelo `RetentionService`.
- Não adicionar `deleted_at` indiscriminadamente em todas as tabelas.

---

# 7. Grupos A–E do SQLite

Foram definidos e revisados os domínios iniciais:

```text
A. Governança
B. Runtime
C. Dispositivos e segurança
D. Perfis
E. Calibração
```

Entidades conceituais incluíram:

- migrations e metadata;
- versões e ativações de componentes;
- feature flags e dependências;
- snapshots de configuração;
- instâncias do servidor e sessões runtime;
- checks de dependência e diagnóstico;
- dispositivos, identificadores, permissões e tokens;
- pareamento e control leases;
- perfis de ambiente, aplicação e monitor;
- famílias e versões de calibração;
- ROIs, click targets, âncoras e assinaturas visuais;
- sessões e validações de calibração.

## 7.1 Decisões relevantes

- Calibração aprovada torna-se imutável.
- Alteração gera nova versão.
- Somente perfil compatível e aprovado pode alimentar observação ou execução.
- Click target é apenas alvo geométrico; não é autorização para ação.

---

# 8. Grupos F–I — Observação, visão, market data, análise e sinais

## 8.1 Fluxo consolidado

```text
observation_session
→ observation_context
→ frame_reference
→ frame_validation
→ visual_extraction
→ mapping models
→ candle estimates versionadas
→ visual series
→ analysis snapshot
→ engine results
→ evidências
→ strategy evaluation
→ signal candidate
→ arbitration
→ signal validation
→ final signal
```

## 8.2 Revisão crítica F–I

Foram corrigidas lacunas importantes:

1. Contadores de sessão não serão atualizados em alta frequência.
2. Pausas e retomadas usam histórico de transições/eventos.
3. Ativo e timeframe possuem contexto versionado.
4. Artefatos externos usam catálogo transversal.
5. Validações precisam ser extensíveis.
6. Séries registram associação explícita com frames e velas.
7. Velas visuais possuem família e versão.
8. Mapeamentos de preço e tempo possuem modelos próprios.
9. Deduplicação de snapshots é contextual.
10. Resultados principais dos motores devem ser consultáveis.
11. Linhagem de evidências foi normalizada conceitualmente.
12. Regras essenciais de estratégia não podem ficar apenas em JSON.
13. Arbitragem registra decisão por candidato.
14. Sinais usam `revision` para controle de concorrência.

---

# 9. Ponto 7 — Arquitetura da análise de gráfico

## 9.1 Cadeia principal

```text
captura do gráfico
→ extração estrutural
→ análise
→ candidato de sinal
→ validação
→ sinal final
```

Depois das revisões, a cadeia detalhada ficou:

```text
captura autorizada
→ validação de frame
→ extração visual
→ reconstrução estrutural
→ snapshot imutável
→ motores A–H
→ evidências e qualidade
→ estratégia
→ candidato
→ arbitragem
→ validação
→ sinal final
```

## 9.2 Motores A–H

Foram definidos contratos conceituais para:

```text
A. Market Structure Engine
B. Trend Engine
C. Support/Resistance ou Zone Engine
D. Volatility Engine
E. Candle Measurement/Context Engine
F. Momentum Engine
G. Confluence Engine
H. Strategy Engine
```

Cada motor deve declarar:

- versão;
- inputs;
- outputs;
- qualidade mínima;
- horizonte;
- evidências utilizadas;
- blockers;
- confiança técnica;
- reason codes;
- determinismo esperado;
- testes e replay.

## 9.3 Contratos transversais

Foram definidos nove contratos transversais antes da primeira estratégia:

- qualidade dos dados;
- confiança técnica;
- estabilidade;
- horizonte;
- linhagem de evidências;
- versionamento;
- reason codes;
- política de blockers;
- rastreabilidade e determinismo.

## 9.4 Estados analíticos congelados

```text
STRATEGY_WAIT = dados válidos, sem oportunidade
WAIT_MORE_DATA = dados insuficientes
DEGRADED = utilizável com limitações e confidence cap
BLOCKED = condição crítica impede continuidade
```

`STRATEGY_WAIT` não cria sinal final.

## 9.5 Primeira estratégia operacional

A primeira estratégia foi definida como simples, auditável e baseada em:

```text
estrutura
+ zona
+ confirmação
```

Sem thresholds numéricos definitivos nesta fase.

Objetivo: permitir explicação causal, replay e auditoria antes de estratégias mais complexas.

---

# 10. Ponto 8 — Android mobile-first

## 10.1 Papel

O Android é o painel operacional principal, mas não é requisito para inicialização do servidor.

## 10.2 Escopo conceitual

Foram definidos:

- telas e navegação;
- estados de conexão;
- pareamento;
- tokens e revogação;
- reconexão por sequence;
- snapshot fallback;
- cache Room;
- comandos idempotentes;
- confirmação de ações críticas;
- modo offline somente para leitura do último estado conhecido;
- indicação clara de estado não confirmado.

## 10.3 Regras

- Room não é autoridade global.
- Estado local só é confirmado após resposta/evento do servidor.
- Android pode desconectar sem derrubar o servidor.
- Operações críticas exigem política de confirmação e autorização da versão correspondente.

---

# 11. Ponto 9 — Linux e Windows

## 11.1 Decisão

```text
Linux Mint/X11 = plataforma central do legado e validação inicial
Windows 10/11 = suporte obrigatório progressivo
Wayland = detectado e limitado até comprovação
```

## 11.2 Fronteira de responsabilidade

O núcleo deve ser compartilhado. Diferenças ficam em adaptadores de plataforma:

- captura;
- janela e foreground;
- geometria e monitores;
- overlay;
- filesystem;
- lifecycle/serviço;
- input control em versões autorizadas.

## 11.3 Revisão crítica

Foi corrigida a interpretação de que “core compartilhado” significaria paridade imediata. Cada adaptador precisa de testes e gates próprios.

---

# 12. Ponto 10 — Testes sintéticos, replay e reais controlados

## 12.1 Níveis R0–R4

```text
R0 = interface sintética local
R1 = aplicação real somente leitura
R2 = validação visual sem movimento e sem clique
R3 = pointer preview, sem clique
R4 = clique controlado em ambiente local autorizado
```

## 12.2 Limites por versão

```text
V2.5 = R0–R2
V2.6 = R0–R2 com pipeline analítico real
V2.7 = R3–R4 somente após gates e autorização explícita
```

## 12.3 Replay

O replay deve registrar:

- pacote e manifesto;
- hashes de input e output;
- versões dos componentes;
- seed determinística;
- eventos em sequência;
- falhas injetadas;
- privacidade e retenção;
- relatório de determinismo.

---

# 13. Ponto 11 — Estrutura definitiva de diretórios

A estrutura futura foi alinhada por responsabilidades:

```text
bootstrap/
runtime/
server/
contracts/
messaging/
persistence/
devices/
security/
profiles/
calibration/
lists/
observation/
vision/
market_data/
analysis/
strategies/
signals/
execution/
platform/
desktop/
android/
tests/
replay/
diagnostics/
legacy/
docs/
```

O nome físico final e os caminhos exatos dependem da Auditoria Mestra. A arquitetura de diretórios não autoriza renomear o legado antes do plano de migração.

## 13.1 ADRs previstos

```text
ADR-001 server source of truth
ADR-002 SQLite single writer
ADR-003 clients no direct database
ADR-004 Android cache only
ADR-005 analysis/strategy/execution separation
ADR-006 progressive schema
ADR-007 transactional outbox
ADR-008 cross-platform adapters
ADR-009 fail-closed policy
ADR-010 incremental legacy migration
```

---

# 14. Ponto 12 — Sequência V2.5, V2.6 e V2.7

## 14.1 V2.5

```text
fundação
servidor
configuração
SQLite
migrations
listas independentes
migração controlada do legado
pareamento e Android Foundation
perfis e calibração
ROIs e alvos
Linux/Windows Foundation
observabilidade e recovery básicos
```

## 14.2 V2.6

```text
observação
captura
extração visual
market data
motores A–H
estratégias
candidatos
sinais
replay
Android operacional de análise
```

## 14.3 V2.7

```text
agenda completa
planos de execução
execution requests
eligibility
pointer preview
execução controlada autorizada
feedback
reconciliação
emergency stop
empacotamento
backup/restore final
estabilização multiplataforma
```

## 14.4 Gates

Cada versão precisa entregar fluxos verticais testáveis. Não é permitido avançar apenas com camadas incompletas.

---

# 15. Blocos J–N — Listas, execução, comandos, auditoria, replay e testes

## 15.1 Domínios definidos

```text
J. Listas e agenda
K. Execução
L. Alertas, comandos e idempotência
M. Auditoria, configuração e migração
N. Replay, testes e desempenho
```

## 15.2 Fluxo

```text
lista
→ versão da lista
→ versão do item
→ agenda versionada
→ ocorrência materializada
→ plano aprovado e imutável
→ execution session
→ execution request
→ eligibility
→ eventos
→ feedback
→ resultado
→ reconciliação
```

## 15.3 Revisão crítica J–N

Foram corrigidas quinze lacunas:

1. Item de lista precisa ser versionado.
2. UTC é autoridade operacional das ocorrências.
3. Agenda precisa de versão imutável.
4. Materialização futura precisa de janela limitada.
5. Contadores de execução ficam em memória e consolidam depois.
6. Elegibilidade precisa ser extensível.
7. Intenção de execution request torna-se imutável após dispatch.
8. Feedback precisa de grupo, sequência e fase.
9. Conciliação não usa lista opaca de IDs em JSON.
10. Emergency stop precisa de escopo.
11. Idempotência tem fonte única.
12. Payload de comando pode usar artefato externo redigido.
13. Logs de auditoria precisam de autoridade definida.
14. Backups precisam de cadeia, método e integridade.
15. Testes precisam de ambiente normalizado.

---

# 16. Cardinalidades, índices e transações críticas

## 16.1 Cardinalidades

Foram consolidadas relações globais entre:

- instalação e instâncias;
- runtime e sessões de domínio;
- dispositivos, tokens e leases;
- perfis e calibração;
- observação, frames e séries;
- snapshots e motores;
- estratégias, candidatos e sinais;
- listas, versões, agendas e planos;
- execução, comandos e resultados;
- migrations, backups, replay e testes.

## 16.2 Chaves estrangeiras

```text
foreign_keys=ON
ON_DELETE=RESTRICT por padrão
CASCADE apenas em dependências sem identidade histórica
SET NULL somente quando o histórico deve sobreviver
```

## 16.3 Índices

Obrigatórios desde a criação:

- PK;
- FK usada em consulta;
- unique lógico;
- estado ativo único;
- idempotência;
- sequência de eventos;
- expiração usada em retenção.

Índices analíticos e de histórico dependem de `EXPLAIN QUERY PLAN` e benchmark.

## 16.4 Escritor único

```text
serviço de domínio
→ WriteQueue
→ transação
→ commit
→ outbox
→ publicação pós-commit
```

Rotas REST, handlers WebSocket e clientes não escrevem diretamente.

## 16.5 Transações críticas

Foram definidas para:

- pareamento;
- ativação de perfil;
- aprovação de calibração;
- criação de snapshot;
- geração de sinal;
- dispatch de execução;
- resultado e reconciliação;
- emergency stop;
- migration.

Nenhuma transação SQLite fica aberta durante OCR, espera de rede, movimento de cursor ou feedback externo.

---

# 17. Política completa de migrations

## 17.1 Tipos

```text
SCHEMA
DATA
BACKFILL
NORMALIZATION
INDEX
RETENTION
REPAIR
VALIDATION
```

## 17.2 Regras

- numeração por versão;
- checksum imutável;
- dependências explícitas;
- executor mínimo sem iniciar o servidor completo;
- backup obrigatório em alterações de risco;
- migration de schema separada de transformação de dados;
- índices grandes criados depois da migração e validação dos dados;
- falha resulta em rollback ou `RECOVERY_REQUIRED`;
- nunca continuar em modo normal com migration incompleta.

## 17.3 Validações pós-migration

```text
PRAGMA integrity_check
PRAGMA foreign_key_check
schema version
checksums
contagens reconciliadas
uniques
índices esperados
dados críticos
startup mínimo
health check
```

---

# 18. Revisão crítica global do schema

## 18.1 Problema encontrado

O catálogo conceitual cresceu para aproximadamente 125 entidades. Isso seria excessivo para a primeira implementação física.

## 18.2 Correção

```text
SCHEMA_LOGICO_COMPLETO = visão até V2.7
SCHEMA_FISICO_PROGRESSIVO = somente o necessário em cada versão
```

Uma tabela física só é criada quando possui:

```text
produtor
consumidor
requisito
teste
retenção, se histórica
```

Sem essas ligações:

```text
TABLE_STATUS=DEFERRED
```

## 18.3 Estimativa física

```text
V2.5 = aproximadamente 35–45 tabelas, introduzidas progressivamente
V2.6 = observação, análise, sinais e replay
V2.7 = execução, agenda, reconciliação e testes completos
```

---

# 19. Revisão crítica geral dos doze pontos

A revisão cruzada encontrou dezoito ajustes. Os principais foram:

- separar autoridade do ponto 1 e localização física do ponto 11;
- separar REST, WebSocket, event bus e outbox;
- definir autoridade de estado;
- decompor responsabilidades do desktop;
- manter listas independentes da análise;
- impedir Strategy-001 de se tornar requisito da observação;
- separar `WAIT`, `WAIT_MORE_DATA`, `DEGRADED` e `BLOCKED`;
- separar confiança técnica, qualidade, estabilidade e confidence cap;
- tratar frequências e thresholds como provisórios até benchmark;
- preservar a cadeia `ClickTarget → Eligibility → Request → Adapter → Feedback`;
- manter o servidor seguro sem Android;
- declarar paridade Windows como progressiva;
- impedir schema lógico completo de virar backlog imediato;
- adicionar modos explícitos de persistência;
- formalizar R0–R4;
- reduzir duplicação de observabilidade;
- registrar decisões em ADRs.

Não foram encontrados conflitos arquiteturais bloqueadores após as correções.

---

# 20. Dez ajustes pré-PTM consolidados

```text
AJ-01 semântica de WAIT/DEGRADED/BLOCKED
AJ-02 PersistenceMode
AJ-03 níveis R0–R4
AJ-04 autoridade de estado
AJ-05 autoridade de observabilidade
AJ-06 gate de existência de tabelas
AJ-07 ADRs
AJ-08 thresholds provisórios
AJ-09 Windows progressivo
AJ-10 listas independentes da análise
```

Correções adicionais:

- `MINIMAL_SAFE` só entra por condição formal e sai após health check;
- `STRATEGY_WAIT` não cria `FinalSignal`;
- R2 não move o cursor;
- ADR não substitui requisito;
- tabela histórica exige retenção;
- Windows Foundation possui mínimo obrigatório.

---

# 21. PTM V2.5 preliminar

## 21.1 Estrutura de registro

Cada registro deverá conter:

```text
requirement_id
requirement
source_point
adr_ids
milestone
criticality
owner_domain
implementation_component
REST_contract
WebSocket_event
database_entities
migration_group
producer
consumer
feature_flag
safe_default
privacy_classification
retention_policy
test_ids
acceptance_criteria
failure_conditions
evidence_required
gate
dependencies
status
gaps
```

## 21.2 Requisitos estruturais iniciados

Foram mapeados requisitos para:

- servidor como fonte única;
- clientes sem banco direto;
- SQLite single writer;
- lifecycle;
- contratos versionados;
- outbox;
- listas independentes;
- Android Foundation;
- reconexão;
- perfis;
- calibração;
- Linux e Windows Foundation;
- migração do legado;
- observabilidade;
- configuração segura;
- segurança de rede;
- estado seguro sem Android.

## 21.3 Requisitos funcionais iniciados

Domínios iniciados:

```text
servidor
configuração
SQLite
listas
migração do legado
```

## 21.4 Revisão crítica da PTM preliminar

Foram adicionados:

- critérios de aceite mensuráveis;
- criticidade;
- ADRs;
- feature flags;
- privacidade e retenção;
- grupos de migration;
- desmembramento de requisitos grandes;
- decisão de buffer WebSocket em memória;
- bloqueio da migração até auditoria real;
- requisitos de configuração segura;
- segurança de rede;
- inicialização segura sem Android.

## 21.5 Status

```text
PTM_V2_5=PRELIMINAR
PTM_V2_5_RECONCILIADA=NAO
PTM_V2_5_DEFINITIVA=NAO
```

A PTM não pode ser finalizada antes da Auditoria Mestra.

---

# 22. Auditoria do legado — evolução do método

## 22.1 Método inicialmente proposto

```text
Auditoria A — inventário
→ PTM
→ Auditoria B — migração
```

## 22.2 Método substituto

Foi adotada a Auditoria Mestra integrada:

```text
inventário factual
+ classificação
+ rastreabilidade PTM
```

Para cada item real:

```text
fonte
caminho
branch/commit
responsabilidade atual
estado atual
classificação
REUTILIZAR/ADAPTAR/SUBSTITUIR/DESCONTINUAR
destino arquitetural
requisito PTM
teste
gate
nível de certeza
```

Estado real e arquitetura futura permanecem em colunas separadas.

---

# 23. Erro crítico de escopo ocorrido

## 23.1 Erro

Foi iniciada por engano uma auditoria no repositório:

```text
leon337/predixai-platform
```

quando o projeto correto era:

```text
leon337/predixai-robo-de-listas
```

## 23.2 Sintomas

Foram citados Flask, OCR, módulos e estruturas que pertenciam a outro projeto.

## 23.3 Correção formal

```text
AUDITORIA_REPOSITORIO_ERRADO=INVALIDADA_INTEGRALMENTE
DADOS_DO_PREDIXAI_PLATFORM_NA_PTM=PROIBIDOS
ALTERACOES_REALIZADAS_NOS_REPOSITORIOS=0
REPOSITORIO_UNICO_AUTORIZADO=predixai-robo-de-listas
```

## 23.4 Barreira anti-mistura

Toda conclusão da Auditoria Mestra deve informar:

```text
FONTE
CAMINHO
BRANCH_OU_COMMIT
CLASSIFICACAO
NIVEL_DE_CERTEZA
```

---

# 24. Estado real confirmado no repositório correto

Até a interrupção da auditoria, foram confirmados preliminarmente:

- repositório `leon337/predixai-robo-de-listas`;
- branch `main`;
- versão real `V2.4.3-R1`;
- aplicação desktop Python;
- orientação Linux Mint/X11;
- código histórico em `app/main.py`;
- Tkinter, threads, JSON e `pynput`;
- modelos históricos `Signal`, `ScheduleList`, `CoordinateProfile` e `PredixAIRoboListas`;
- persistência histórica em `config/config_predixai_robo_listas.json`;
- dependência `pynput==1.8.2`;
- HEAD contendo `app/bootstrap_v243.py`;
- ferramentas de logs, backups, diagnóstico e reparo;
- README parcialmente defasado em relação ao HEAD.

Essas constatações precisam ser ampliadas e verificadas na Auditoria Mestra. Não representam inventário completo.

---

# 25. Governança documental criada

## 25.1 Nova autoridade

```text
GitHub = verdade documental e técnica
Linear = verdade operacional de tarefas, bloqueios e progresso
ChatGPT = motor de análise e engenharia
```

## 25.2 PTP-GOV.5

Foi criada a PTP:

```text
PTP-GOV.5 — Memória e Governança Documental
```

Objetivo: permitir que um chat novo reconstrua e continue o projeto lendo a documentação oficial.

## 25.3 Documentos publicados

- `PROJECT_STATE.md`;
- `docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md`;
- `docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md`;
- documentos posteriores do protocolo de acesso e resultados de teste.

## 25.4 Linear

Foi criado o projeto operacional:

```text
PredixAI Robô de Listas — Governança e Documento Mestre
```

Tarefas iniciais:

```text
LEA-5 Teste de memória
LEA-6 Continuidade
LEA-7 Auditoria Mestra
LEA-8 Reconciliação da PTM V2.5
```

---

# 26. Testes de memória e falha descoberta

## 26.1 Objetivo original

Abrir um chat novo sem memória e pedir que reconstruísse o estado apenas pelo GitHub.

## 26.2 Resultado do primeiro experimento

```text
TESTE_001=FAIL_POR_FALTA_DE_ACESSO_AO_REPOSITORIO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_INTERPRETACAO=NAO
FALHA_DE_ACESSO=SIM
```

O chat novo recebeu o link, mas acessou apenas páginas genéricas do GitHub e pediu ZIP ou documentos anexados.

## 26.3 Lição

Integração GitHub visível na conta não prova que o conector esteja disponível ou seja acionado em uma conversa específica.

## 26.4 Novo protocolo

```text
Teste A — Acesso
→ provar leitura real de arquivos exatos

Teste B — Reconstrução
→ avaliar a documentação somente após A=PASS

Teste C — Continuidade
→ outro chat novo continua da etapa correta
```

## 26.5 Evidência mínima de acesso

O chat deve retornar:

- caminho do arquivo;
- conteúdo verificável;
- PTP ativa;
- SHA/blob quando disponível;
- indicação de uso do conector GitHub, não navegação genérica.

---

# 27. Decisões congeladas

- Servidor é fonte global de estado.
- SQLite é acessado somente pelo servidor.
- Escritor único/fila central para writes.
- REST, WebSocket, event bus e outbox têm responsabilidades distintas.
- Android e desktop são clientes.
- Android é mobile-first, não dependência de startup.
- Listas manuais e programadas independem da análise.
- Observação, análise, estratégia, sinal e execução são separados.
- Schema físico é progressivo.
- Frequências e thresholds não medidos são provisórios.
- R0–R4 definem níveis de validação real.
- GitHub é fonte técnica oficial.
- Auditoria usa apenas o repositório correto.
- PTM definitiva depende da Auditoria Mestra.
- Implementação depende do Documento Mestre revisado.

---

# 28. Decisões revogadas

## 28.1 Chat como memória principal

Revogada. GitHub passa a ser memória oficial.

## 28.2 Auditoria em duas fases desconectadas

Revogada. Substituída pela Auditoria Mestra integrada.

## 28.3 Teste de reconstrução sem pré-teste de acesso

Revogada. Substituída por Acesso → Reconstrução → Continuidade.

## 28.4 README como representação suficiente do legado

Revogada. O HEAD e o código real têm prioridade na auditoria.

---

# 29. Riscos atuais

```text
R1 acesso ao GitHub varia por conversa
R2 Auditoria Mestra ainda incompleta
R3 PTM V2.5 ainda não reconciliada
R4 PTMs V2.6 e V2.7 inexistentes
R5 Documento Mestre ainda não gerado
R6 README defasado
R7 mistura entre estado real e futuro
R8 excesso de schema se implementação antecipada
R9 thresholds ainda não medidos
R10 suporte Windows ainda não comprovado
R11 documentação extensa sem índice pode confundir novos chats
R12 repetição do erro de repositório
```

Mitigações:

- teste explícito de acesso;
- `PROJECT_STATE.md` como índice rápido;
- histórico integral como memória longa;
- fonte/caminho/commit em toda auditoria;
- Linear para sequência operacional;
- gates formais antes de cada avanço.

---

# 30. Proibições atuais

```text
NÃO iniciar implementação V2.5.
NÃO gerar schema SQL físico definitivo.
NÃO gerar migrations físicas.
NÃO criar código de servidor/Android por esta arquitetura ainda.
NÃO considerar a PTM V2.5 definitiva.
NÃO usar dados do predixai-platform.
NÃO misturar estado real V2.4.3-R1 com arquitetura V2.5–V2.7.
NÃO alterar ou remover legado antes de inventário, backup e plano.
NÃO declarar testes PASS sem evidência.
NÃO avançar para PTM V2.6 antes de reconciliar e revisar V2.5.
```

---

# 31. Roadmap oficial a partir deste documento

```text
🟧 PTP-GOV.5 — Memória e Governança Documental
🟧 Publicar e revisar este Histórico Integral
⬜ Teste A — acesso real ao GitHub
⬜ Teste B — reconstrução do estado
⬜ Teste C — continuidade correta
⬜ Auditoria Mestra V2.4.3-R1
⬜ Anexo A — inventário real e rastreabilidade
⬜ Reconciliar PTM V2.5
⬜ Revisar criticamente PTM V2.5
⬜ Construir e revisar PTM V2.6
⬜ Construir e revisar PTM V2.7
⬜ Consolidação cruzada final
⬜ Consolidar ADRs
⬜ Gerar Documento Mestre
⬜ Revisar criticamente Documento Mestre
⬜ Congelar Arquitetura V1.0
⬜ Iniciar implementação em novos chats
```

---

# 32. Próxima ação inequívoca

Depois que este documento estiver integrado na `main`:

1. Executar **Teste A — Acesso** em um chat com conector GitHub disponível.
2. Se `ACCESS_TEST=PASS`, executar **Teste B — Reconstrução**.
3. Em outro chat, executar **Teste C — Continuidade**.
4. Registrar evidências e resultados no GitHub e Linear.
5. Somente depois retomar a Auditoria Mestra.

O Teste A deve solicitar o arquivo exato, não apenas o link do repositório.

Prompt recomendado:

```text
Use o conector GitHub, não navegação web genérica.
Leia no repositório leon337/predixai-robo-de-listas, branch main:
1. PROJECT_STATE.md
2. docs/history/ptp/CHECKPOINT_HISTORICO_COMPLETO_PTP-GOV.5_ARQUITETURA_V2.5_V2.7_20260716.md
3. docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md

Informe o caminho, conteúdo verificável, PTP ativa e SHA/blob de cada arquivo quando disponível.
Não implemente nada.
```

---

# 33. Critérios de completude deste histórico

```text
IDENTIFICACAO_E_AUTORIDADE=PASS
OBJETIVO_DA_SESSAO=PASS
DOZE_PONTOS=PASS
ARQUITETURA_ANALITICA=PASS
ANDROID=PASS
CROSS_PLATFORM=PASS
TESTES=PASS
DIRETORIOS=PASS
VERSOES=PASS
SQLITE_A_N=PASS_RESUMIDO_E_ESTRUTURADO
CARDINALIDADES_INDICES_TRANSACOES=PASS
MIGRATIONS=PASS
REVISOES_CRITICAS=PASS
AJUSTES_PRE_PTM=PASS
PTM_V2_5_PRELIMINAR=PASS
AUDITORIA_MESTRA=PASS
ERRO_REPOSITORIO=PASS
GOVERNANCA_GITHUB_LINEAR=PASS
TESTE_MEMORIA_E_FALHA=PASS
DECISOES_CONGELADAS=PASS
DECISOES_REVOGADAS=PASS
RISCOS=PASS
PROIBICOES=PASS
ROADMAP=PASS
PROXIMA_ACAO=PASS
```

---

# 34. Estado de encerramento documental

```text
HISTORICO_INTEGRAL_GERADO=SIM
ESTADO_REAL_TOTALMENTE_AUDITADO=NAO
PTM_V2_5_RECONCILIADA=NAO
DOCUMENTO_MESTRE_GERADO=NAO
IMPLEMENTACAO_AUTORIZADA=NAO
```

Este documento deve ser lido junto com `PROJECT_STATE.md`. O primeiro informa rapidamente onde o projeto está; este explica como chegou até aqui, quais contratos foram definidos, quais erros ocorreram e qual sequência deve ser seguida.