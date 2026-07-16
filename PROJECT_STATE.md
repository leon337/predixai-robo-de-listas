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
- Pull Request ativo: `#30`, Draft
- Etapa atual: `REMEDIACAO_RC3_CONCLUIDA_AGUARDANDO_RC4`
- Gate atual: `INDEPENDENT_CRITICAL_REVIEW_RC4_REQUIRED`
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
schema_version=1.0.2
state_revision=0
transition_id=PTP-MEM.1-T01
transition_status=READY_FOR_INDEPENDENT_REVIEW
github_sync_status=PASS
linear_sync_status=IN_PROGRESS
LOCK_ENFORCEMENT=ADVISORY
CONCURRENCY_MODEL=OPTIMISTIC
```

A `state_revision` permanece `0` durante revisões e remediações da mesma transição.

## Histórico das revisões independentes

```text
RC1=FAIL
RC1_CRITICAL_BLOCKERS=2
RC2=FAIL
RC2_CRITICAL_BLOCKERS=2
RC3=FAIL
RC3_CRITICAL_BLOCKERS=1
PR_30_MERGE_AUTHORIZATION=BLOCKED
RUNTIME_R8_R24=NOT_EXECUTED
```

## Remediação RC3

O bloqueador residual foi eliminado em todos os contratos ativos.

```text
PERSISTED_EXPECTED_FIELDS=PROHIBITED
OBSERVED_PR_HEAD=PERSISTED_INFORMATIONAL_SNAPSHOT
PRE_WRITE_EXPECTED_FIELDS=EPHEMERAL_SESSION_VALUES
CURRENT_FIELDS=LIVE_SOURCE_QUERIES
SELF_REFERENTIAL_EXPECTED_HEAD=PROHIBITED
```

Campos persistidos agora usam semântica de baseline, vínculo ou snapshot:

```text
BASELINE_MAIN_SHA
BASELINE_STATE_REVISION
BOUND_TRANSITION_ID
LOCK_STATE_REVISION_SNAPSHOT
LOCK_TRANSITION_ID_SNAPSHOT
```

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
STALE_WRITE_PROTECTION=REMEDIATED_PENDING_RC4
START_SKILL_BOUNDARY=PASS_DRAFT
DYNAMIC_MEMORY_TESTS_CREATED=PASS_SPEC_ONLY
INSTRUCTION_SOURCE_ALLOWLIST=PASS_DRAFT
DOCUMENT_PROMPT_INJECTION_PROTECTION=PASS_DRAFT
BOOTSTRAP_MINIMAL_READ_SET=PASS_DRAFT
CRITICAL_REVIEW=PENDING_RC4
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
SCHEMA_CONTRACT_MANUAL_VALIDATION=PASS
SCHEMA_RUNTIME_VALIDATION=NOT_EXECUTED
```

## Próxima ação

1. sincronizar a remediação RC3 no Linear;
2. manter a PR nº 30 como Draft;
3. executar RC4 em chat limpo e somente leitura;
4. integrar somente após Boss Gate independente `PASS`;
5. executar Transição B pós-merge em PR separado.

## Proibições

```text
NÃO alterar código da aplicação.
NÃO executar a aplicação ou clique real.
NÃO gerar SQL ou migrations.
NÃO iniciar implementação V2.5.
NÃO escrever diretamente na main.
NÃO integrar PR sem revisão crítica independente PASS.
NÃO declarar teste runtime PASS sem execução e evidência.
NÃO tratar lock consultivo como trava técnica.
NÃO persistir PRE_WRITE_EXPECTED_*.
NÃO ativar handoff antes do recibo pós-merge.
```
