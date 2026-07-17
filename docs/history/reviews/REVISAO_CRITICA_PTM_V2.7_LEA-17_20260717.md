# REVISÃO CRÍTICA INDEPENDENTE — PTM V2.7

## LEA-17 / PR #37

## 1. Controle

```text
REVIEW_STATUS=FINAL_FAIL_REMEDIATION_REQUIRED
REVIEW_TYPE=INDEPENDENT_CRITICAL_REVIEW
MISSION=LEA-17
REVIEWED_PR=37
REVIEWED_HEAD=f475d94ae389109f466c23d2a8731b65364794ef
BASE_MAIN_SHA=f3c84d97523c1c631392cefb69b6cb3e8f6a56e2
TRANSITION_ID=LEA-16-T01
STATE_REVISION=5
APPLICATION_CODE_CHANGED=NO
TEST_CODE_CHANGED=NO
WORKFLOWS_CHANGED=NO
APPLICATION_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
POINTER_MOVEMENT_EXECUTED=NO
KEYBOARD_INPUT_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
REAL_ORDER_EXECUTED=NO
```

Esta revisão confrontou diretamente os arquivos do PR, PTM V2.5 e V2.6, matrizes, Auditoria Mestra, schema do manifesto, protocolos oficiais, Linear e comentários de revisão existentes. A auto-revisão do builder foi tratada apenas como evidência preliminar.

## 2. Resultado executivo

```text
PTM_V2_7_CRITICAL_REVIEW=FAIL
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=4
MINOR_FINDINGS=4
REQUIREMENT_ID_UNIQUENESS=PASS
TRACEABILITY_COMPLETENESS=FAIL
LEGACY_CLASSIFICATION_CONSISTENCY=FAIL
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS
SIMULATED_ONLY_BASELINE=PASS
SIGNAL_EXECUTION_SEPARATION=PASS
AUTHORIZATION_MODEL=PASS
IDEMPOTENCY_AND_DEDUPLICATION=PASS_CONCEPTUAL
UNKNOWN_EFFECT_CONTAINMENT=PASS
KILL_SWITCH_DOMINANCE=PASS_SPECIFIED_NOT_RUNTIME
REAL_ADAPTER_ABSENCE=PASS_DOCUMENTAL
REAL_EFFECT_NEGATIVE_PROOF=FAIL_NOT_EXECUTED_AND_SCOPE_AMBIGUOUS
STATE_SCHEMA_COMPATIBILITY=FAIL
DOCUMENTAL_READY_FOR_MERGE=NO
RETEST_REQUIRED=YES
```

## 3. Aspectos aprovados

1. A fronteira V2.5 → V2.6 → V2.7 está preservada.
2. O baseline expõe somente `DISABLED`, `DRY_RUN` e `SIMULATED`.
3. Não existe `ARMED_REAL`, adaptador real, aceitação de credenciais reais ou autorização de implementação.
4. Sinal, comando, autorização, tentativa, recibo e reconciliação são domínios separados.
5. Timeout não é confundido com ausência de efeito.
6. `UNKNOWN_EFFECT` bloqueia comandos correlatos.
7. Retry exige prova de `FAILED_NO_EFFECT`.
8. Kill switch domina fila, retry, dispatch e rearmamento no contrato documental.
9. Os 84 IDs são únicos e a contagem 32 + 52 é consistente.
10. O PR altera somente documentação.

## 4. Achados maiores bloqueantes

### MAJOR-01 — Manifesto incompatível com o schema 1.0.3

O `PROJECT_RUNTIME_STATE.yaml` usa valores não permitidos pelo contrato oficial:

```text
gate_status=PENDING
github_sync_status=PASS_IN_PROGRESS
linear_sync_status=PASS_IN_PROGRESS
safety.execution_status=IN_PROGRESS_AWAITING_INDEPENDENT_REVIEW
```

O schema permite `gate_status` entre `NOT_STARTED|IN_PROGRESS|PASS|WARN|FAIL|BLOCKED`, sync entre `NOT_STARTED|IN_PROGRESS|PASS|FAIL|PENDING` e execution status entre os enums explícitos, incluindo `AWAITING_INDEPENDENT_REVIEW`, mas não os valores compostos usados pelo PR.

Impacto: bootstrap com validação de schema deve bloquear o manifesto canônico.

Correção exigida:

1. substituir os valores pelos enums já permitidos; ou
2. versionar e migrar formalmente o schema antes de usar novos enums.

Condição de reteste:

```text
PROJECT_RUNTIME_STATE_SCHEMA_COMPATIBILITY=PASS
MANUAL_SCHEMA_CONTRACT_VALIDATION=PASS
```

### MAJOR-02 — Deadline monotônico não é recuperável após reinício

`ExecutionCommand` persiste apenas `deadline_monotonic`, enquanto o próprio documento prevê persistência conceitual, recuperação de comandos intermediários e reinício sem redespacho.

Relógios monotônicos têm origem local ao processo/boot e não fornecem representação portátil entre reinícios. O recovery não consegue determinar com segurança se um comando persistido expirou.

Impacto: comando antigo pode ser considerado válido ou comando válido pode ser rejeitado sem critério verificável.

Correção exigida:

- persistir uma expiração estável, como `expires_at_utc`, duração original e identidade do boot/clock;
- usar monotonicamente apenas o orçamento em processo;
- definir política fail-closed para clock skew, clock rollback, boot diferente e informação insuficiente;
- após restart, dúvida deve expirar ou bloquear, nunca rearmar.

Condição de reteste:

```text
RESTART_STABLE_DEADLINE_CONTRACT=PASS
CLOCK_SKEW_FAIL_CLOSED_POLICY=PASS
```

### MAJOR-03 — Classificação contraditória de `command_id`

A matriz da V2.7 registra em `PTM-V27-004`:

```text
command_id NOVO
```

A PTM V2.5 já introduziu `trace_id` e `command_id`, e o documento pai V2.7 classifica essa herança como `ADAPTAR`.

Impacto: `LEGACY_CLASSIFICATION_CONSISTENCY=PASS_BUILDER` não é sustentado e a orientação de migração fica ambígua.

Correção exigida:

- classificar `command_id` como `ADAPTAR` a partir da V2.5; ou
- definir explicitamente um identificador diferente e justificar por que não é o `command_id` herdado.

Condição de reteste:

```text
LEGACY_CLASSIFICATION_CONSISTENCY=PASS
PTM_V27_004_SOURCE_ALIGNMENT=PASS
```

### MAJOR-04 — Prova negativa confunde especificação documental com evidência executada

O documento declara corretamente:

```text
TEST_RUNTIME_EXECUTED=NO
TEST_RUNTIME_RESULT=NOT_EXECUTED
```

Porém os documentos vivos exigem `REAL_EFFECT_NEGATIVE_PROOF=PASS` para avanço. O protocolo oficial determina que especificação criada não equivale a runtime aprovado. Além disso, o legado auditado ainda contém `pynput`, movimento e clique real; portanto uma varredura sem escopo falharia por definição.

Impacto: o gate pode declarar como executada uma prova que apenas foi especificada ou pode produzir falso `FAIL` ao escanear o legado conhecido.

Correção exigida:

```text
REAL_EFFECT_NEGATIVE_PROOF_SPECIFICATION=PASS_DOCUMENTAL
REAL_EFFECT_NEGATIVE_PROOF_RUNTIME=NOT_EXECUTED
```

Também deve ser definido o escopo futuro da prova:

- módulos e adaptadores V2.7 autorizados;
- fronteiras de import e dispatch;
- exceções explícitas para o legado preservado apenas como evidência;
- scan AST/import, contract tests e runtime negativo quando houver implementação autorizada.

Condição de reteste:

```text
NEGATIVE_PROOF_GATE_SEPARATION=PASS
NEGATIVE_PROOF_SCOPE_DEFINED=PASS
RUNTIME_CLAIM_ACCURACY=PASS
```

## 5. Achados menores

### MINOR-01 — Taxonomia de `target_logical_id`

A tipagem, versão, cardinalidade e compatibilidade do alvo lógico ainda não estão definidas. Preservar como contrato tipado sem coordenada física e detalhar antes do Documento Mestre.

### MINOR-02 — Limites e thresholds sem valores

Frequência, fila, deadline e circuit breaker permanecem sem valores. Isso é aceitável sem benchmark, desde que nenhuma configuração conveniente substitua safe defaults conservadores.

### MINOR-03 — Topologia do kill switch

Precedência local/remota, partição de rede, autenticação, persistência e rearmamento precisam de ADR ou seção normativa posterior. A dominância local fail-closed deve permanecer obrigatória.

### MINOR-04 — State machine sem matriz integral de transições

O documento lista estados e regras principais, mas não apresenta tabela completa `estado atual × evento × guarda × próximo estado × efeito permitido`. A matriz deverá existir antes do Documento Mestre e dos testes vinculantes.

## 6. Threads de revisão consideradas

No HEAD revisado existiam três threads abertas e não obsoletas:

1. enums incompatíveis com o schema do manifesto;
2. deadline monotônico não recuperável;
3. classificação inconsistente de `command_id`.

Os três achados foram confirmados. Esta revisão acrescenta a separação obrigatória entre especificação e execução da prova negativa.

## 7. Condições para nova revisão

```text
MAJOR_01_SCHEMA_ENUMS=REMEDIATED
MAJOR_02_RESTART_STABLE_DEADLINE=REMEDIATED
MAJOR_03_COMMAND_ID_CLASSIFICATION=REMEDIATED
MAJOR_04_NEGATIVE_PROOF_GATE=REMEDIATED
OPEN_MAJOR_FINDINGS=0
OPEN_CRITICAL_FINDINGS=0
PR_HEAD_UPDATED=YES
REVIEW_THREADS_RESOLVED_OR_RESPONDED=YES
RE_REVIEW_REQUIRED=YES
```

## 8. Decisão

A PTM V2.7 possui uma base arquitetural segura e estritamente simulada, mas não está documentalmente apta para merge no HEAD revisado.

```text
REQUEST_CHANGES=YES
MERGE_AUTHORIZATION=BLOCKED
MERGE_EXECUTED=NO
PTM_V2_7_DEFINITIVE=NO
CROSS_CONSOLIDATION_AUTHORIZED=NO
```
