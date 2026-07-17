# PREDIXAI ROBÔ DE LISTAS — SKILLS OFICIAIS

## Finalidade

As Skills são comandos curtos que acionam protocolos completos sem depender de checkpoint colado, ZIP ou memória informal de outro chat.

## Regra universal de pré-escrita

Antes de qualquer escrita externa, a sessão captura expectativas efêmeras e consulta os valores atuais:

```text
PRE_WRITE_EXPECTED_MAIN_SHA == CURRENT_MAIN_SHA
PRE_WRITE_EXPECTED_PR_HEAD == CURRENT_PR_HEAD
PRE_WRITE_EXPECTED_STATE_REVISION == CURRENT_STATE_REVISION
PRE_WRITE_EXPECTED_TRANSITION_ID == CURRENT_TRANSITION_ID
```

```text
OBSERVED_PR_HEAD=PERSISTED_INFORMATIONAL_SNAPSHOT
PRE_WRITE_EXPECTED_PR_HEAD=EPHEMERAL_SESSION_VALUE
CURRENT_PR_HEAD=LIVE_GITHUB_QUERY
SELF_REFERENTIAL_EXPECTED_HEAD=PROHIBITED
```

Falha em qualquer condição:

```text
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
WRITE_OPERATION=PROHIBITED
STATE_RECONSTRUCTION_REQUIRED=YES
```

## Regra universal do painel público

O `README.md` é a projeção operacional mobile-first da primeira página do GitHub.

Toda Skill que altera versão, missão, fase, gate, progresso, bloqueios, política de automação ou próxima ação deve verificar o README.

```text
README_SYNC_REQUIRED_ON_STATE_CHANGE=YES
README_IS_CANONICAL_AUTHORITY=NO
README_IS_REQUIRED_PUBLIC_PROJECTION=YES
README_SNAPSHOT_METADATA_REQUIRED=YES
README_ARBITRARY_PROGRESS=PROHIBITED
```

## Skills operacionais

### `iniciar`

Skill de bootstrap estritamente somente leitura.

Ler inicialmente:

1. `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md`;
2. `PROJECT_RUNTIME_STATE.yaml`;
3. `PROJECT_STATE.md`;
4. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
5. Linear;
6. PR ativo indicado pelo manifesto, quando existir.

```text
INICIAR_MODE=READ_ONLY
BOOTSTRAP_MINIMAL_READ_SET=PASS
FULL_HISTORY_READ_ON_START=NO
INICIAR_EXECUTES_WORK=NO
INICIAR_CREATES_BRANCH=NO
INICIAR_WRITES_GITHUB=NO
INICIAR_WRITES_LINEAR=NO
INICIAR_WRITES_EXTERNAL_SYSTEMS=NO
INICIAR_ENDS_AFTER_STATE_RECONSTRUCTION=YES
```

Informar `README_SYNC_STATUS=PASS|WARN|FAIL` quando a primeira página estiver divergente.

### `continuar`

Executar a próxima unidade autorizada da missão. Capturar expectativas de pré-escrita, consultar valores atuais e respeitar o `transition_id`. Quando alterar estado visível, incluir o README na sincronização.

### `missão`

Mostrar objetivo, entregas, gates, condição de conclusão, limites de autonomia e impacto previsto no painel público.

### `estado`

Comparar manifesto, `PROJECT_STATE`, tronco, GitHub, PR, Linear e README. Declarar divergências por domínio.

### `painel`

Exibir campanha, missão, fase, progresso reproduzível por gates reais, risco, bloqueio e próxima Skill.

```text
PERCENTAGE_WITHOUT_FORMULA=PROHIBITED
GATE_COUNT_PREFERRED=YES
SNAPSHOT_METADATA_REQUIRED=YES
```

### `roadmap`

Ler o tronco multichat e verificar se o mapa resumido do README permanece coerente.

### `fontes`

Listar documentos vivos, históricos, evidências, commit, PR e issue Linear. Identificar o README como projeção pública, não autoridade canônica.

### `evidências`

Mostrar provas, origem, certeza e classificação consolidada, transitória, pública ou histórica.

### `riscos`

Verificar escopo, arquitetura, documentação, segurança, concorrência, state drift, README drift, sincronização parcial e avanço indevido.

### `revisar`

Executar revisão crítica formal.

```text
BUILDER_SELF_REVIEW=ALLOWED_PRELIMINARY
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
FINAL_BOSS_GATE_BY_BUILDER_ALONE=PROHIBITED
```

A revisão valida o README quando a missão altera estado, versão, roadmap, política ou próxima ação visível.

### `validar`

Comparar o resultado com os gates e declarar `PASS`, `WARN`, `FAIL` ou `BLOCKED`.

```text
README_VERSION_SYNC
README_MISSION_SYNC
README_PHASE_SYNC
README_GATE_SYNC
README_PROGRESS_SYNC
README_PROGRESS_REPRODUCIBLE
README_SNAPSHOT_METADATA
README_BLOCKERS_SYNC
README_NEXT_ACTION_SYNC
README_AUTOMATION_POLICY_SYNC
```

### `sincronizar`

Reconciliar manifesto, documentos vivos, GitHub, PR, Linear e README usando a mesma transição idempotente.

```text
TRANSITION_STATUS=PARTIAL
STATE_REVISION=UNCHANGED
TRANSITION_ID=UNCHANGED
```

Se apenas o painel estiver divergente:

```text
README_SYNC_STATUS=FAIL
PUBLIC_DELIVERY_STATUS=BLOCKED
CANONICAL_STATE_AUTHORITY=PRESERVED
```

### `checkpoint`

Registrar continuidade da mesma missão, estado da transição, branch, PR, revisão, bloqueios e próxima ação.

```text
README_CURRENT_STATE_REVIEWED=YES
README_UPDATE_REQUIRED=YES|NO
README_SNAPSHOT_METADATA=PASS
```

### `handoff`

Preparar a próxima missão sem declarar merge futuro como fato. O handoff só é ativado após a transição pós-merge.

### `fechar`

Validar gates, integrar somente após revisão independente e iniciar confirmação pós-merge em PR separado.

```text
PROJECT_RUNTIME_STATE_SYNC=PASS
PROJECT_STATE_SYNC=PASS
TRUNK_SYNC=PASS
LINEAR_SYNC=PASS
README_SYNC=PASS
```

### `mini`

Criar mini-PTP interna sem trocar a missão principal. Informar se altera o painel público.

### `md`

Criar ou atualizar Markdown por branch e PR. Aplicar leitura mobile-first quando o alvo for o README.

### `saúde`

Mostrar contexto, conectores, sincronização, lock consultivo, state drift, README drift e capacidade de continuar.

### `aprovar`, `reprovar`, `pausar`

Registrar decisão humana, justificativa, impacto e continuidade sem enfraquecer gates técnicos. Atualizar o painel quando a decisão alterar estado público.

## Autonomia padrão

```text
CONTINUE_AUTOMATICALLY=YES
STOP_ONLY_ON=CRITICAL_BLOCKER|CONCURRENT_UPDATE|STATE_DRIFT|CONNECTOR_FAILURE|INDEPENDENT_REVIEW|MERGE_AUTHORIZATION|IRREVERSIBLE_ACTION|COST|LEGAL_OR_COMMERCIAL_DECISION|SCOPE_CHANGE|UNAUTHORIZED_CODE_CHANGE|MISSION_COMPLETE
```

## Modos de resposta

- rápido: `estado`, `saúde`, `painel`, `fontes`, `roadmap`;
- missão: `iniciar`, `missão`, `continuar`, `mini`;
- crítico: `revisar`, `validar`, `riscos`, `evidências`;
- entrega: `checkpoint`, `handoff`, `fechar`, `sincronizar`.

## Segurança e modos A+B

Aplicar `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`.

Nenhuma Skill autoriza automaticamente código, SQL, migration, custo, contratação, ação irreversível ou acesso externo não autorizado.

Modo A permite análise visual, captura, OCR, replay, ponteiro, teclado, preenchimento, clique, autenticação controlada, E2E e ordem simulada quando missão e alvo estiverem autorizados.

Modo B permanece desligado por padrão. Seu suporte arquitetural exige gate separado com decisão comercial e legal registrada, validação dos termos e jurisdição da plataforma, elegibilidade do titular, escopo LIVE explícito, arming humano, allowlists, limites, kill switch e auditoria. Nenhuma Skill arma automaticamente uma sessão LIVE.
