# PROJECT_STATE — PredixAI Robô de Listas

## Estado operacional

- Projeto: PredixAI Robô de Listas
- Repositório: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- HEAD consolidado de entrada: `0c7591eeb571b80ae726018c7ddff9a9c5563954`
- Versão real: `V2.4.3-R1`
- Missão ativa: `PTP-MEM.1 — Endurecimento da Continuidade GitHub–Linear–Multichat`
- Issue ativa: `LEA-12`
- Branch de trabalho: `docs/ptp-mem-1-hardening`
- Pull Request: ainda não aberto
- Etapa do produto preservada: `PTM V2.5 — Reconciliação com o legado`
- Issue do produto: `LEA-8`, `Todo`, não iniciada e sem bloqueio formal pela PTP-MEM.1

## Autoridade

```text
PROJECT_RUNTIME_STATE.yaml = estado operacional canônico estruturado
PROJECT_STATE.md = visão humana detalhada derivada
PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md = roadmap e histórico resumido
GitHub main = código e documentação consolidados
Pull Request ativo = trabalho ainda não integrado
Linear = tarefas, bloqueios, dependências e progresso
ChatGPT = contexto temporário
```

Divergência entre manifesto e documentação bloqueia avanço automático.

## Transição atual

```text
schema_version=1.0.0
state_revision=0
transition_id=PTP-MEM.1-T01
transition_status=IN_PROGRESS
github_sync_status=IN_PROGRESS
linear_sync_status=PASS
LOCK_ENFORCEMENT=ADVISORY
CONCURRENCY_MODEL=OPTIMISTIC
```

A `state_revision` permanece `0` enquanto a transição não estiver consolidada. Retentativas parciais preservam o mesmo `transition_id` e a mesma revisão.

## Estado consolidado anterior

```text
AUDITORIA_MESTRA_DRAFT_COMPLETE=PASS
AUDITORIA_MESTRA_CRITICAL_REVIEW=PASS
CRITICAL_BLOCKERS=0
PR_29_MERGED=PASS
LEA_7=DONE
LEA_10=DONE
PTM_V2_5=READY_FOR_DOCUMENTAL_RECONCILIATION
IMPLEMENTATION_V2_5=NOT_AUTHORIZED
```

A antiga orientação para concluir o merge da PR #29 foi removida porque o merge já ocorreu.

## Gates da PTP-MEM.1

```text
CURRENT_STATE_RECONSTRUCTED=PASS
NO_CONCURRENT_WORK=PASS
POST_MERGE_STATE_RECONCILIATION=PASS_DRAFT
PERMANENT_INSTRUCTIONS_STATE_FREE=PASS_DRAFT
FIELD_LEVEL_AUTHORITY_DEFINED=PASS_DRAFT
MACHINE_READABLE_STATE_MANIFEST=PASS_DRAFT
STATE_SCHEMA_VERSIONED=PASS_DRAFT
IDEMPOTENT_TRANSITION_PROTOCOL=PASS_DRAFT
PARTIAL_SYNC_RECOVERY=PASS_DRAFT
CONCURRENT_CHAT_CONTROL=PASS_DRAFT
STALE_WRITE_PROTECTION=PASS_DRAFT
START_SKILL_BOUNDARY=PASS_DRAFT
DYNAMIC_MEMORY_TESTS_CREATED=PASS_SPEC_ONLY
INSTRUCTION_SOURCE_ALLOWLIST=PASS_DRAFT
DOCUMENT_PROMPT_INJECTION_PROTECTION=PASS_DRAFT
BOOTSTRAP_MINIMAL_READ_SET=PASS_DRAFT
CRITICAL_REVIEW=PENDING_INDEPENDENT
PR_MERGED=NO
POST_MERGE_RECEIPT=NOT_STARTED
APPLICATION_CODE_CHANGED=NO
SQL_OR_MIGRATIONS_CREATED=NO
```

## Testes R8–R24

```text
TEST_SPEC_CREATED=PASS
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```

Nenhum teste runtime recebe PASS sem execução real e evidência individual.

## Bootstrap obrigatório

A Skill `iniciar` lê inicialmente apenas:

1. instruções permanentes;
2. `PROJECT_RUNTIME_STATE.yaml`;
3. este arquivo;
4. tronco multichat;
5. Linear;
6. PR indicado pelo manifesto, quando existir.

```text
INICIAR_MODE=READ_ONLY
FULL_HISTORY_READ_ON_START=NO
INICIAR_EXECUTES_WORK=NO
INICIAR_WRITES_EXTERNAL_SYSTEMS=NO
INICIAR_ENDS_AFTER_STATE_RECONSTRUCTION=YES
```

## Próxima ação

1. concluir atualização do tronco e do modelo de resposta;
2. consolidar protocolo de retenção e testes R8–R24;
3. produzir relatório documental do draft;
4. abrir PR principal sem merge;
5. preparar prompt para revisão crítica independente;
6. corrigir bloqueadores encontrados pelo revisor;
7. integrar somente após Boss Gate independente PASS;
8. executar Transição B pós-merge em PR separado.

## Proibições

```text
NÃO alterar código da aplicação.
NÃO executar a aplicação ou clique real.
NÃO gerar SQL ou migrations.
NÃO iniciar implementação V2.5.
NÃO escrever diretamente na main.
NÃO integrar PR sem revisão crítica independente.
NÃO declarar teste runtime PASS sem execução e evidência.
NÃO tratar lock consultivo como trava técnica.
NÃO ativar handoff antes do recibo pós-merge.
```