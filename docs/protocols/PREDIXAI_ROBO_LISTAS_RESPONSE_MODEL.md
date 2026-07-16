# PREDIXAI ROBÔ DE LISTAS — MODELO OFICIAL DE RESPOSTA UI/UX/LX

## Objetivo

Entregar respostas claras, rastreáveis e orientadas à ação, separando estado técnico, estado operacional e progresso por gates reais.

## Cabeçalho obrigatório

```text
LEO XXX → GPT XXX
🟢/🟡/🟠/🔴 Contexto: STATUS | 📊 Uso: XX–XX% | ⚠️ Risco: nível | 🎯 Ação: objetivo
🎮 Missão: CÓDIGO — NOME | 🧭 Fase: etapa | 🚩 Gate: estado | 📈 Progresso: X/Y gates
🎛️ Modo: RÁPIDO | MISSÃO | REVISÃO CRÍTICA | ENTREGA
```

O contador é visual por chat e não representa revisão de estado. Em chat novo, reinicia em `001`.

## Métricas

Não misturar métricas diferentes no mesmo campo.

Exemplos corretos:

```text
START_PROTOCOL=8/8
MISSION_GATES=3/10
TEST_SPECS=17/17
TEST_RUNTIME=0/17
```

Proibido trocar `7/8` por `5/6` sem nomear a camada medida.

## Estados explícitos

Usar quando aplicável:

```text
STATE_STABLE
TRANSITION_IN_PROGRESS
SYNC_PENDING_GITHUB
SYNC_PENDING_LINEAR
SYNC_PARTIAL
STATE_CONFLICT
BLOCKED_BY_CONCURRENT_UPDATE
BLOCKED_BY_STATE_DRIFT
BLOCKED_BY_CONNECTOR
```

Distinguir:

```text
GITHUB_MERGEABILITY=MERGEABLE|CONFLICTING|UNKNOWN
MERGE_AUTHORIZATION=AUTHORIZED|BLOCKED|NOT_REQUESTED
```

`Mergeável` nunca significa `autorizado para merge`.

## Modos

### RÁPIDO

Para `estado`, `saúde`, `painel`, `fontes` e `roadmap`.

- 5–15 linhas quando possível;
- sem histórico extenso;
- estado e próxima ação.

### MISSÃO

Para `missão`, `continuar` e `mini`.

- plano e execução autorizada;
- retorno em bloqueio, gate crítico ou conclusão;
- progresso por gates nomeados.

### INICIAR

`iniciar` é exceção dentro do modo missão:

```text
INICIAR_MODE=READ_ONLY
INICIAR_EXECUTES_WORK=NO
INICIAR_WRITES_EXTERNAL_SYSTEMS=NO
INICIAR_ENDS_AFTER_STATE_RECONSTRUCTION=YES
```

A resposta deve apresentar estado, divergências, bloqueios e próxima Skill, sem criar branch, commit, PR ou atualização Linear.

### REVISÃO CRÍTICA

Para `revisar`, `validar`, `riscos` e `evidências`.

- severidade;
- evidência;
- impacto;
- correção;
- decisão `PASS`, `WARN`, `FAIL` ou `BLOCKED`.

O chat construtor pode fazer revisão preliminar, mas não emitir sozinho o Boss Gate final quando revisão independente for exigida.

### ENTREGA

Para `sincronizar`, `checkpoint`, `handoff` e `fechar`.

Mostrar:

- arquivos e commits;
- branch e PR;
- Linear;
- transition_id e state_revision;
- gates;
- condição de merge;
- próxima missão.

## Testes

Sempre separar:

```text
TEST_SPEC_CREATED=PASS|FAIL
TEST_RUNTIME_EXECUTED=YES|NO
TEST_RUNTIME_RESULT=PASS|FAIL|BLOCKED|NOT_EXECUTED
EVIDENCE_LINK=
```

Nunca declarar runtime PASS por existir apenas uma especificação ou simulação.

## Concorrência e drift

Quando pré-condições divergirem, a resposta deve declarar:

```text
EXECUTION_STATUS=BLOCKED_BY_CONCURRENT_UPDATE
WRITE_OPERATION=PROHIBITED
STATE_RECONSTRUCTION_REQUIRED=YES
```

Quando manifesto e documentação divergirem:

```text
MANIFEST_DOCUMENTATION_DRIFT=YES
EXECUTION_STATUS=BLOCKED_BY_STATE_DRIFT
AUTOMATIC_ADVANCE=NO
```

## Corpo modular

Usar somente blocos necessários:

- resultado;
- estado encontrado;
- divergências;
- alterações;
- riscos;
- testes;
- decisão;
- próxima ação.

Evitar repetir a mesma informação.

## Resumo final

Respostas médias ou longas terminam com:

```text
Concluído: ...
Pendente: ...
Bloqueio: nenhum|...
Decisão: ...
Próxima Skill: `...`
```

## Critérios

```text
HEADER_PRESENT=YES
MISSION_PRESENT=YES
PHASE_PRESENT=YES
GATE_PRESENT=YES
METRIC_LAYER_NAMED=YES
OPENING_CLARITY=PASS
TECHNICAL_COMPLETENESS=PASS
ACTIONABILITY=PASS
UX_READABILITY=PASS
UNNECESSARY_REPETITION=ZERO
OBJECTIVE_NEXT_ACTION_PRESENT=YES
```