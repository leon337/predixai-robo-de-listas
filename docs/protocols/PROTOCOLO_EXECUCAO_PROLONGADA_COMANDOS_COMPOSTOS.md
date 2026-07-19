# PROTOCOLO DE EXECUÇÃO PROLONGADA E COMANDOS COMPOSTOS

## 1. Finalidade

Permitir que uma única mensagem do usuário acione uma cadeia extensa, segura e rastreável de tarefas relacionadas, reduzindo interrupções para comandos repetitivos sem ampliar implicitamente escopo ou autorização.

Este protocolo governa somente a execução dentro da resposta ativa do ChatGPT. Ele não cria processo em segundo plano, não promete continuidade após o encerramento da resposta e não substitui automação agendada quando o usuário solicitar execução futura.

```text
LONG_RUNNING_MODE=FOREGROUND_MULTI_STEP
BACKGROUND_EXECUTION=NO
SINGLE_USER_COMMAND_CAN_TRIGGER_MULTIPLE_SKILLS=YES
CONTINUE_UNTIL_OBJECTIVE_GATE_OR_HARD_STOP=YES
```

## 2. Prefixo obrigatório em novo chat

Quando a missão depende das fontes operacionais do projeto, o comando de novo chat começa por:

```text
@GitHub @Linear
```

Forma mínima:

```text
@GitHub @Linear iniciar
```

Forma composta:

```text
@GitHub @Linear iniciar e revisar LEA-35
```

Forma prolongada:

```text
@GitHub @Linear iniciar e executar fluxo LEA-XX até GATE_ALVO
```

O prefixo indica explicitamente que GitHub e Linear devem ser consultados. Ele não muda a autoridade das fontes e não autoriza escrita por si só.

## 3. Semântica dos comandos compostos

Um comando composto possui fases encadeadas por `e`, `depois`, `até` ou por uma lista de objetivos.

Exemplo:

```text
@GitHub @Linear iniciar e revisar LEA-35
```

Expansão canônica:

```text
FASE_1=INICIAR_READ_ONLY
FASE_2=VALIDAR_BASELINE_GITHUB_LINEAR
FASE_3=EXECUTAR_SKILL_REVISAR_LEA_35
FASE_4=PUBLICAR_PARECER_SE_AUTORIZADO
FASE_5=SINCRONIZAR_REGISTROS_PERMITIDOS
FASE_6=PARAR_NO_PROXIMO_GATE_HUMANO
```

A Skill `iniciar` continua estritamente somente leitura durante sua própria fase. Quando houver uma Skill subsequente explícita, a sessão pode prosseguir após a reconstrução, aplicando as autorizações e limites da missão seguinte.

```text
INICIAR_PHASE_READ_ONLY=YES
COMPOSITE_COMMAND_STOPS_AFTER_INICIAR=NO
SUBSEQUENT_SKILL_REQUIRES_SCOPE_VALIDATION=YES
```

## 4. Skill `fluxo`

`fluxo` executa várias unidades relacionadas em uma única resposta, de forma sequencial, validada e idempotente.

Sintaxe recomendada:

```text
@GitHub @Linear iniciar e executar fluxo <MISSÃO> até <GATE>
```

Parâmetros opcionais:

```text
MODO=DOCUMENTAL|REVISÃO|ENTREGA|IMPLEMENTAÇÃO_AUTORIZADA
OBJETIVO=<resultado final verificável>
ORÇAMENTO_DE_UNIDADES=<número alvo>
PERMITIDO=<ações explicitamente autorizadas>
PROIBIDO=<ações explicitamente bloqueadas>
PARAR_EM=<gates humanos ou técnicos>
ENTREGA=<artefatos esperados>
```

Exemplo estruturado:

```text
@GitHub @Linear

Iniciar e executar fluxo LEA-XX até READY_FOR_INDEPENDENT_REVIEW.

OBJETIVO=produzir pacote documental completo e rastreável
ORÇAMENTO_DE_UNIDADES=12
PERMITIDO=investigar|planejar|documentar|validar|branch|commit|PR_DRAFT|Linear|checkpoint
PROIBIDO=código|SQL|migration|runtime|merge|custo|ação_legal_ou_comercial
PARAR_EM=CONCURRENT_UPDATE|STATE_DRIFT|INDEPENDENT_REVIEW|MERGE_AUTHORIZATION|CRITICAL_BLOCKER
ENTREGA=plano|artefatos|auto_revisão|CI|PR_DRAFT|issue_de_revisão|handoff
```

## 5. Orçamento de trabalho

O orçamento é uma meta de unidades, não uma autorização adicional e não um progresso arbitrário.

```text
DEFAULT_WORK_UNIT_BUDGET=12
RECOMMENDED_RANGE=8_TO_20
EXPLICIT_EXTENDED_RANGE=21_TO_30
WORK_UNIT=entrega_verificável_ou_gate_real
```

Exemplos de unidades:

1. reconstruir estado;
2. validar baseline;
3. investigar fontes;
4. formular plano;
5. registrar issue Linear;
6. criar branch;
7. produzir artefato;
8. validar artefato;
9. executar CI permitido;
10. abrir ou atualizar PR;
11. sincronizar GitHub e Linear;
12. preparar revisão independente;
13. corrigir achados autorizados;
14. repetir validação;
15. gerar checkpoint ou handoff.

A sessão não deve parar apenas porque uma unidade terminou. Ela continua para a próxima unidade autorizada enquanto houver capacidade, contexto e ausência de gate obrigatório.

```text
STOP_AFTER_EACH_SUBTASK=NO
CONTINUE_QUEUE_AUTOMATICALLY=YES
ASK_FOR_CONFIRMATION_BETWEEN_REVERSIBLE_TASKS=NO
```

## 6. Construção da fila

Após reconstruir o estado, a sessão monta uma fila interna ordenada:

```text
RECONSTRUIR
→ VALIDAR
→ INVESTIGAR
→ PLANEJAR
→ REGISTRAR_LINEAR
→ PREPARAR_BRANCH
→ PRODUZIR
→ AUTO_REVISAR
→ VALIDAR_CI
→ PUBLICAR_PR
→ SINCRONIZAR
→ PREPARAR_BOSS_GATE
→ CHECKPOINT_OU_ENTREGA
```

A fila pode ser reduzida ou expandida conforme a missão, mas não pode pular pré-condições, revisão independente ou autorização humana obrigatória.

## 7. Regra de autonomia

Dentro de uma missão explicitamente autorizada, a sessão assume decisões técnicas que sejam:

- fundamentadas;
- reversíveis;
- sem custo adicional;
- sem risco crítico;
- sem mudança de escopo;
- sem alteração de arquitetura congelada;
- compatíveis com as proibições do estado oficial.

A sessão deve executar automaticamente as tarefas seguintes da fila, em vez de solicitar `continuar` a cada etapa.

```text
AUTOMATIC_CONTINUATION_WITHIN_AUTHORIZED_SCOPE=YES
INTERMEDIATE_USER_COMMAND_REQUIRED=NO
```

## 8. Paradas obrigatórias

A execução prolongada para imediatamente em:

```text
CONCURRENT_UPDATE
STATE_DRIFT
SCHEMA_MISMATCH
CONNECTOR_FAILURE_WITHOUT_SAFE_FALLBACK
CRITICAL_BLOCKER
INDEPENDENT_CRITICAL_REVIEW_WHEN_BUILDER_IS_ACTIVE
MERGE_AUTHORIZATION
IRREVERSIBLE_ACTION
COST_OR_CONTRACTING
LEGAL_OR_COMMERCIAL_DECISION
SCOPE_CHANGE
UNAUTHORIZED_CODE_CHANGE
UNAUTHORIZED_RUNTIME
UNAUTHORIZED_LIVE_OR_FINANCIAL_EFFECT
MISSION_COMPLETE
CONTEXT_OR_CONNECTOR_LIMIT_REACHED
```

Ao parar por limite de contexto ou conector, criar checkpoint reproduzível e fornecer um único comando composto de continuação.

## 9. Gates humanos que nunca são implícitos

Nenhuma formulação como `trabalhe até concluir`, `faça tudo`, `continue sozinho` ou `entregue pronto` autoriza automaticamente:

- merge;
- alteração de código sem autorização aplicável;
- SQL ou migration;
- contratação ou custo;
- decisão legal ou comercial;
- ação irreversível;
- congelamento arquitetural;
- implementação;
- runtime externo;
- clique real fora de alvo controlado autorizado;
- Modo LIVE ou efeito financeiro real.

```text
GENERAL_AUTONOMY_COMMAND!=MERGE_AUTHORIZATION
GENERAL_AUTONOMY_COMMAND!=CODE_AUTHORIZATION
GENERAL_AUTONOMY_COMMAND!=LIVE_ARMING
```

## 10. Política de comunicação

Durante um fluxo prolongado:

- não pedir confirmação entre tarefas reversíveis já autorizadas;
- emitir atualizações somente em mudança relevante de fase, bloqueio ou gate;
- evitar respostas intermediárias que encerrem o trabalho prematuramente;
- retornar ao usuário no bloqueio obrigatório ou ao alcançar o resultado solicitado;
- registrar evidências no GitHub e progresso no Linear.

```text
RETURN_ON=HARD_STOP|HUMAN_GATE|MISSION_RESULT|CHECKPOINT_REQUIRED
NOISE_REDUCTION=ENABLED
FINAL_RESPONSE_MUST_INCLUDE=resultado|evidências|pendências|bloqueios|próxima_ação
```

## 11. Modelos de comando

### 11.1 Curto

```text
@GitHub @Linear iniciar e revisar LEA-35
```

### 11.2 Fluxo documental

```text
@GitHub @Linear iniciar e executar fluxo LEA-XX até READY_FOR_INDEPENDENT_REVIEW, com até 12 unidades. Investigue, planeje, documente, valide, publique PR Draft, sincronize GitHub e Linear e prepare o Boss Gate. Pare antes de revisão independente, merge, código, SQL, migration, runtime, custo ou decisão irreversível.
```

### 11.3 Fluxo de revisão

```text
@GitHub @Linear iniciar e executar fluxo de revisão LEA-XX até REVIEW_DECISION_RECORDED. Valide o HEAD, recalcule os gates, publique o parecer no GitHub, registre o resultado no Linear e sincronize somente os registros permitidos. Não edite o PR do builder, não faça merge e não autorize implementação.
```

### 11.4 Campanha documental extensa

```text
@GitHub @Linear

Iniciar e executar campanha documental <MISSÃO> até <GATE_ALVO>.

Execute automaticamente:
1. reconstrução do estado;
2. auditoria GitHub × Linear;
3. investigação das fontes;
4. plano formal;
5. criação ou atualização da issue;
6. branch documental;
7. produção dos artefatos;
8. rastreabilidade;
9. auto-revisão;
10. validação e CI permitido;
11. PR Draft;
12. sincronização;
13. preparação da revisão independente;
14. checkpoint e handoff.

Continue sem pedir `continuar` entre etapas reversíveis. Pare somente nos gates obrigatórios definidos pelo projeto.
```

## 12. Resultado esperado

Um comando bem estruturado pode produzir uma dezena ou mais de entregas relacionadas na mesma interação. A quantidade real depende do escopo, dos conectores, do tamanho dos documentos, do limite de contexto e dos gates de segurança.

```text
PROMISE_OF_UNBOUNDED_RUNTIME=NO
MULTI_STEP_COMPLETION_IN_ONE_INTERACTION=YES
CHECKPOINT_ON_LIMIT=REQUIRED
EVIDENCE_REQUIRED_FOR_EACH_COMPLETED_UNIT=YES
```

## 13. Validação deste protocolo

```text
COMPOSITE_COMMAND_GRAMMAR=DEFINED
NEW_CHAT_PREFIX_GITHUB_LINEAR=REQUIRED_WHEN_CONNECTORS_ARE_NEEDED
LONG_RUNNING_FOREGROUND_MODEL=DEFINED
WORK_UNIT_BUDGET=DEFINED
AUTOMATIC_QUEUE_CONTINUATION=DEFINED
HARD_STOP_RULES=DEFINED
HUMAN_GATE_BOUNDARIES=PRESERVED
BACKGROUND_PROMISE=PROHIBITED
MERGE_IMPLICIT_AUTHORIZATION=PROHIBITED
CODE_IMPLICIT_AUTHORIZATION=PROHIBITED
LIVE_IMPLICIT_AUTHORIZATION=PROHIBITED
```