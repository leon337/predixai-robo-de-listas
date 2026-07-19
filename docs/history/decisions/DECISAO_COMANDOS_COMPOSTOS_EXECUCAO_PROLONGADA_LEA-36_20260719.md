# DECISÃO — COMANDOS COMPOSTOS E EXECUÇÃO PROLONGADA

## LEA-36 — 2026-07-19

## Contexto

Leo testou em novo chat o comando curto:

```text
@GitHub @Linear iniciar e revisar LEA-35
```

O comando foi interpretado como fluxo composto e executou:

1. reconstrução do estado;
2. confirmação do PR #56 e do HEAD definitivo;
3. validação do baseline GitHub × Linear;
4. recálculo dos dez gates da LEA-35;
5. decisão formal `PASS`;
6. publicação do parecer no PR #56;
7. registro integral na LEA-35;
8. preservação das proibições de merge, código, SQL, migration, runtime, congelamento, implementação e Modo LIVE.

```text
SHORT_COMPOSITE_COMMAND_TEST=PASS
REVIEW_HEAD=a8ce01aa747046518d1da3e445a1f8c47fbe39ef
REVIEW_DECISION=PASS
GATES=10/10
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
OPEN_BLOCKING_FINDINGS=0
```

## Decisão de produto operacional

Formalizar comandos compostos e um modo de execução prolongada para que uma única mensagem possa acionar uma fila extensa de tarefas relacionadas, com retorno somente em resultado, bloqueio, gate humano ou checkpoint obrigatório.

Objetivo do usuário:

- reduzir a necessidade de retornar ao chat a cada 15–30 minutos;
- permitir uma dezena ou mais de tarefas relacionadas em uma interação;
- obter um resultado final rastreável semelhante a um workflow de engenharia;
- manter GitHub e Linear como memória e controle;
- preservar gates humanos e proibições críticas.

## Limite técnico declarado

Execução prolongada significa múltiplas etapas sequenciais dentro da resposta ativa. Não significa processo ilimitado, segundo plano ou promessa de continuar depois que a resposta terminar.

```text
LONG_RUNNING_FOREGROUND=YES
BACKGROUND_PROCESS=NO
MULTI_SKILL_SINGLE_INTERACTION=YES
CHECKPOINT_ON_LIMIT=YES
```

## Artefatos normativos

- `docs/protocols/PROTOCOLO_EXECUCAO_PROLONGADA_COMANDOS_COMPOSTOS.md`;
- `docs/protocols/PREDIXAI_ROBO_LISTAS_SKILLS.md`.

## Comandos adotados

### Composto curto

```text
@GitHub @Linear iniciar e revisar LEA-35
```

### Fluxo

```text
@GitHub @Linear iniciar e executar fluxo <MISSÃO> até <GATE_ALVO>
```

### Campanha

```text
@GitHub @Linear iniciar e executar campanha <MISSÃO> até <GATE_ALVO>
```

## Salvaguardas

```text
MERGE_IMPLICIT_AUTHORIZATION=NO
CODE_IMPLICIT_AUTHORIZATION=NO
SQL_IMPLICIT_AUTHORIZATION=NO
MIGRATION_IMPLICIT_AUTHORIZATION=NO
COST_IMPLICIT_AUTHORIZATION=NO
IRREVERSIBLE_ACTION_IMPLICIT_AUTHORIZATION=NO
ARCHITECTURE_FREEZE_IMPLICIT_AUTHORIZATION=NO
IMPLEMENTATION_IMPLICIT_AUTHORIZATION=NO
LIVE_IMPLICIT_AUTHORIZATION=NO
```

## Estado

```text
DOCUMENTATION_ONLY=YES
ACTIVE_PRODUCT_PR_56_MODIFIED=NO
MAIN_MODIFIED=NO
INDEPENDENT_REVIEW_REQUIRED=YES
MERGE_AUTHORIZED=NO
```