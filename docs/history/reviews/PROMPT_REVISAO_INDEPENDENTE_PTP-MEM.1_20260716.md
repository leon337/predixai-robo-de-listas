# Prompt de Revisão Crítica Independente — PTP-MEM.1

Use GitHub e Linear em chat limpo.

## Modo

Somente leitura. Não alterar arquivos, PR, Linear ou `main`.

## Escopo

Revisar a branch `docs/ptp-mem-1-hardening` e o PR principal da PTP-MEM.1 contra a `main`.

## Verificações obrigatórias

1. confirmar `main` e base SHA;
2. confirmar PR e head atuais;
3. verificar que apenas documentação e governança foram alteradas;
4. validar `PROJECT_RUNTIME_STATE.yaml` contra o schema;
5. verificar autoridade por domínio e tratamento de drift;
6. verificar `state_revision` monotônica e vínculo com `transition_id`;
7. verificar sincronização parcial idempotente;
8. verificar lock consultivo e concorrência otimista;
9. verificar proteção por main SHA, PR head, revisão e transição;
10. confirmar que `iniciar` é somente leitura;
11. confirmar allowlist contra prompt injection;
12. verificar retenção, compactação e migração de schema;
13. confirmar que R8–R24 são apenas especificações quando não executados;
14. verificar separação entre PR principal e recibo pós-merge;
15. confirmar que LEA-8 não recebeu bloqueio funcional indevido;
16. verificar consistência entre manifesto, PROJECT_STATE, tronco, Skills e Linear.

## Saída obrigatória

```text
INDEPENDENT_CRITICAL_REVIEW=PASS|FAIL|BLOCKED
CRITICAL_BLOCKERS=<N>
MAJOR_WARNINGS=<N>
MANIFEST_SCHEMA_VALIDATION=PASS|FAIL|BLOCKED
MANIFEST_DOCUMENTATION_ALIGNMENT=PASS|FAIL
FIELD_LEVEL_AUTHORITY_DEFINED=PASS|FAIL
STATE_REVISION_PROTOCOL=PASS|FAIL
IDEMPOTENT_TRANSITION_PROTOCOL=PASS|FAIL
PARTIAL_SYNC_RECOVERY=PASS|FAIL
CONCURRENT_CHAT_CONTROL=PASS|FAIL
STALE_WRITE_PROTECTION=PASS|FAIL
START_SKILL_BOUNDARY=PASS|FAIL
TEST_STATUS_SEPARATION=PASS|FAIL
INSTRUCTION_SOURCE_ALLOWLIST=PASS|FAIL
DOCUMENT_PROMPT_INJECTION_PROTECTION=PASS|FAIL
BOOTSTRAP_MINIMAL_READ_SET=PASS|FAIL
POST_MERGE_TWO_TRANSITION_MODEL=PASS|FAIL
APPLICATION_CODE_CHANGED=NO|YES
PR_MERGE_AUTHORIZATION=BLOCKED
```

Para cada bloqueador, informar arquivo, seção, evidência, impacto e correção objetiva.

Não declarar runtime PASS para R8–R24 sem execução real e evidência.