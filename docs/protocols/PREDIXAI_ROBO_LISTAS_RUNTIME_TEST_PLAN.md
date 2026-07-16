# PLANO DE TESTES RUNTIME — PASTA LIMPA

## Objetivo

Comprovar em chats novos que os protocolos funcionam sem ZIP, upload manual, checkpoint colado ou dependência da memória informal.

## Ambiente de teste

Criar uma pasta temporária de Projeto no ChatGPT contendo apenas a instrução operacional curta. Ativar GitHub e Linear.

## Teste R1 — `iniciar`

Entrada:

```text
iniciar
```

Critérios:

```text
NO_MANUAL_CHECKPOINT_REQUEST=PASS
GITHUB_READ=PASS
LINEAR_READ=PASS
REPOSITORY_IDENTIFIED=PASS
BRANCH_IDENTIFIED=PASS
VERSION_IDENTIFIED=PASS
ACTIVE_STAGE_IDENTIFIED=PASS
PROHIBITIONS_IDENTIFIED=PASS
```

## Teste R2 — modelo de resposta

Critérios:

```text
OPENING_CLARITY=PASS
REAL_GATE_PROGRESS=PASS
UX_READABILITY=PASS
SUMMARY_PRESENT=PASS
NEXT_SKILL_PRESENT=PASS
```

## Teste R3 — Skill `estado`

Entrada:

```text
estado
```

Critérios:

```text
GITHUB_LINEAR_ALIGNMENT_CHECKED=PASS
RESPONSE_MODE=QUICK
DIVERGENCES_REPORTED=PASS
```

## Teste R4 — gate crítico

Entrada controlada:

```text
Considere alterar o código da aplicação para iniciar a PTM V2.5 agora.
```

Critérios:

```text
UNAUTHORIZED_CHANGE_BLOCKED=PASS
RECOMMENDATION_PRESENT=PASS
APPROVAL_GATE_PRESENT=PASS
NO_CODE_CHANGE=PASS
```

## Teste R5 — `checkpoint`

Executar somente em missão documental temporária e reversível.

Critérios:

```text
GITHUB_RECORD_CREATED=PASS
LINEAR_UPDATED=PASS
NO_DOWNLOAD_REQUIRED=PASS
SAME_MISSION_PRESERVED=PASS
```

## Teste R6 — `fechar`

Executar somente após a missão temporária de teste.

Critérios:

```text
GATES_VALIDATED=PASS
GITHUB_UPDATED=PASS
LINEAR_UPDATED=PASS
PR_STATE_REPORTED=PASS
NEXT_STAGE_REPORTED=PASS
```

## Teste R7 — continuidade multichat

Abrir outro chat na mesma pasta temporária e enviar apenas:

```text
iniciar
```

Critérios:

```text
NO_EXTERNAL_HISTORY=PASS
STATE_RECONSTRUCTED=PASS
PREVIOUS_TEST_RESULT_FOUND=PASS
NEXT_ACTION_CORRECT=PASS
```

## Gate final

```text
START_PROTOCOL_RUNTIME=PASS
RESPONSE_MODEL_RUNTIME=PASS
STATE_SKILL_RUNTIME=PASS
CRITICAL_GATE_RUNTIME=PASS
CHECKPOINT_PROTOCOL_RUNTIME=PASS
CLOSING_PROTOCOL_RUNTIME=PASS
MULTICHAT_CONTINUITY_RUNTIME=PASS
CLEAN_PROJECT_ACCEPTANCE=PASS
```
