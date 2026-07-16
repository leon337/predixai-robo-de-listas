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

Semântica obrigatória:

```text
OBSERVED_PR_HEAD=PERSISTED_INFORMATIONAL_SNAPSHOT
PRE_WRITE_EXPECTED_PR_HEAD=EPHEMERAL_SESSION_VALUE
CURRENT_PR_HEAD=LIVE_GITHUB_QUERY
SELF_REFERENTIAL_EXPECTED_HEAD=PROHIBITED
```

O `OBSERVED_PR_HEAD` persistido não substitui a captura efêmera da sessão e não pode tentar prever o SHA do commit que ainda será criado.

Falha em qualquer condição:

```text
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
WRITE_OPERATION=PROHIBITED
STATE_RECONSTRUCTION_REQUIRED=YES
```

## Skills operacionais

### `iniciar`

Skill de bootstrap estritamente somente leitura.

Ler inicialmente apenas:

1. `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md`;
2. `PROJECT_RUNTIME_STATE.yaml`;
3. `PROJECT_STATE.md`;
4. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
5. Linear;
6. PR ativo indicado pelo manifesto, quando existir.

Abrir outras evidências somente sob demanda.

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

O comando deve reconstruir o estado, informar missão, fase, gate, divergências, bloqueios, proibições e próxima ação; depois parar.

### `continuar`

Executar a próxima unidade autorizada da missão. Deve reconstruir somente o delta necessário, capturar as expectativas efêmeras de pré-escrita, consultar os valores atuais e respeitar o `transition_id` vigente.

Não criar nova missão durante retry de sincronização parcial.

### `missão`

Mostrar objetivo, entregas, submissões, gates, condição de conclusão e limites de autonomia.

### `estado`

Comparar manifesto, `PROJECT_STATE`, tronco, GitHub, PR e Linear. Declarar divergências por domínio.

### `painel`

Exibir campanha, missão, fase, progresso por gates reais, risco, bloqueio e próxima Skill.

### `roadmap`

Ler o tronco multichat e mostrar etapas, revisões críticas e bloqueios.

### `fontes`

Listar documentos vivos, históricos, evidências, commit, PR e issue Linear que governam a etapa.

### `evidências`

Mostrar provas, origem, nível de certeza e se a evidência é consolidada, transitória ou histórica.

### `riscos`

Verificar escopo, arquitetura, documentação, segurança, concorrência, state drift, sincronização parcial e avanço indevido.

### `revisar`

Executar revisão crítica formal. O builder pode fazer auto-revisão preliminar, mas não emitir sozinho o Boss Gate final.

```text
BUILDER_SELF_REVIEW=ALLOWED_PRELIMINARY
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
FINAL_BOSS_GATE_BY_BUILDER_ALONE=PROHIBITED
```

### `validar`

Comparar resultado com gates e declarar `PASS`, `WARN`, `FAIL` ou `BLOCKED`. Especificação criada não equivale a runtime aprovado.

### `sincronizar`

Reconciliar manifesto, documentos vivos, GitHub, PR e Linear usando a mesma transição idempotente.

Em falha parcial:

```text
TRANSITION_STATUS=PARTIAL
STATE_REVISION=UNCHANGED
TRANSITION_ID=UNCHANGED
```

### `checkpoint`

Registrar continuidade da mesma missão, estado da transição, branch, PR, revisão, bloqueios e próxima ação. Não gerar arquivo para transporte manual.

### `handoff`

Preparar a próxima missão sem declarar merge futuro como fato. O handoff só é ativado após a transição pós-merge.

### `fechar`

Validar gates, integrar somente após revisão independente e iniciar a confirmação pós-merge em PR separado. A missão só fecha após o recibo pós-merge integrado.

### `mini`

Criar mini-PTP interna sem trocar a missão principal.

### `md`

Criar ou atualizar Markdown por branch e PR.

### `saúde`

Mostrar contexto, conectores, sincronização, lock consultivo, state drift e capacidade de continuar.

### `aprovar`, `reprovar`, `pausar`

Registrar decisão humana, justificativa, impacto e continuidade sem enfraquecer gates técnicos.

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

## Segurança

Nenhuma Skill autoriza automaticamente código, SQL, migration, custo, contratação, ação irreversível, clique real ou mudança de escopo.
