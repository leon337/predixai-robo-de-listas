# REVISÃO CRÍTICA INDEPENDENTE — ADRs P0

## LEA-27 — PR #46

## 1. Controle

```text
REVIEW_TYPE=INDEPENDENT_CRITICAL_REVIEW
REVIEW_ISSUE=LEA-27
BUILDER_ISSUE=LEA-26
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=46
BASE_BRANCH=main
BASE_MAIN_SHA=c339ef253c2558300388901a67faf18734e2735f
REVIEWED_PR_HEAD=2c9c2432058c5f119bd1802c3ba00e845c6a5ca0
TRANSITION_ID=LEA-26-T01
STATE_REVISION=9
REVIEW_DATE=2026-07-18
DOCUMENTATION_ONLY=YES
CODE_CHANGED_BY_REVIEW=NO
TEST_CODE_CHANGED_BY_REVIEW=NO
SQL_CREATED=NO
MIGRATION_CREATED=NO
IMPLEMENTATION_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

A revisão foi executada sobre o HEAD informado e reconfirmado antes da publicação. A `main` permaneceu em `c339ef253c2558300388901a67faf18734e2735f` durante a auditoria.

## 2. Escopo auditado

Foram examinados:

1. plano da missão LEA-26;
2. template e índice mestre dos ADRs;
3. ADR-0001 a ADR-0012;
4. matriz de rastreabilidade dos ADRs P0;
5. auto-revisão do builder;
6. `PROJECT_RUNTIME_STATE.yaml`;
7. `PROJECT_STATE.md`;
8. tronco multichat;
9. `README.md`;
10. política normativa A+B;
11. catálogo de candidatos, mapa de domínios/handoffs e índice individual dos 218 requisitos;
12. PTM V2.7 e contratos de comando, autorização, tentativa e reconciliação;
13. PR, threads e nove workflows do HEAD revisado.

## 3. Resultado executivo

```text
ADR_P0_CRITICAL_REVIEW=FAIL
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=4
MINOR_FINDINGS=1
OPEN_FINDINGS=5
RETEST_REQUIRED=YES
DOCUMENTAL_READY_FOR_MERGE=NO
DOCUMENT_MASTER_READY_TO_START=NO
MERGE_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
```

Os 12 ADRs existem, preservam o status `PROPOSED_FOR_REVIEW`, mantêm a separação A+B e não autorizam implementação. Entretanto, rastreabilidade, dependências, lifecycle de comando/grant, idempotência e sincronização final ainda não satisfazem o Boss Gate.

## 4. Verificações obrigatórias

```text
ADR_COUNT=PASS_12_OF_12
ADR_STATUS=PASS_PROPOSED_FOR_REVIEW
DECISION_SCOPE_SEPARATION=PASS
CROSS_ADR_CONSISTENCY=FAIL
REQUIREMENT_TRACEABILITY=FAIL
DOMAIN_OWNERSHIP_ALIGNMENT=PASS
ALTERNATIVES_AND_CONSEQUENCES=PASS
POLICY_A_B_ALIGNMENT=PASS
LIVE_GATE_SEPARATION=PASS
SECURITY_AND_RECOVERY_INVARIANTS=FAIL
README_AND_STATE_SYNC=FAIL
CI_STATUS=PASS_9_OF_9
```

## 5. Achados

### MAJOR-01 — A matriz não entrega rastreabilidade individual requisito–domínio–ADR

#### Evidência

A entrega autorizada exige uma matriz `requisito–domínio–ADR` e rastreabilidade aos 218 requisitos consolidados.

A matriz do PR possui uma linha por ADR e usa grupos ou intervalos descritos como `Grupos/IDs principais`. Ela declara:

```text
CROSS_VERSION_REQUIREMENTS=218
HANDOFF_REFERENCE_COVERAGE=12/12
REQUIREMENT_GROUP_LINKS=PASS_PRELIMINARY
```

Porém, não existe uma linha determinística para cada um dos 218 requisitos indicando:

- domínio primário;
- ADR P0 aplicável;
- ausência justificada de ADR P0;
- candidato P1/P2 relacionado;
- regra preservada sem nova decisão;
- fonte e estado de cobertura.

Exemplo verificável: o índice individual consolidado contém em DOM-04 `PTM-V25-007`, `V25-LIST-001..004` e `V25-QA-002`. A matriz dos ADRs não os reconcilia individualmente com um ADR, com `NO_P0_ADR_REQUIRED` ou com candidato posterior.

Os ADRs transversais que referenciam `H-01..H-12` ou `DOM-01..15` não comprovam, por si, cobertura requisito a requisito.

#### Risco

A declaração `218/218` não é reproduzível a partir da matriz entregue. Requisitos podem ficar sem decisão, ser atribuídos excessivamente a ADR transversal ou ser confundidos com decisões P1/P2 ainda pendentes.

#### Correção obrigatória

Criar apêndice ou matriz exaustiva com 218 linhas, usando ao menos:

```text
REQUIREMENT_ID
PRIMARY_DOMAIN
P0_ADR_ID=ADR-NNNN|NO_P0_ADR_REQUIRED
P1_P2_CANDIDATE=<id>|N/A
RELATION=GOVERNED_BY|DECIDED_BY|AUDITED_BY|DEFERRED_WITH_REASON
SOURCE
COVERAGE_STATUS
```

Validar:

```text
REQUIREMENT_ROWS=218
UNIQUE_REQUIREMENT_IDS=218
DUPLICATE_REQUIREMENT_IDS=0
ORPHAN_REQUIREMENT_IDS=0
UNJUSTIFIED_NO_P0_MAPPING=0
```

### MAJOR-02 — O grafo de dependências é contraditório e contém ciclo não qualificado

#### Evidência

O plano da missão declara simultaneamente:

```text
ADR-0008 -> ADR-0010
ADR-0010 -> ADR-0008
```

O mesmo plano também declara `ADR-0010 -> ADR-0009`, enquanto:

- ADR-0008 registra `DEPENDS_ON=ADR-0001|ADR-0002|ADR-0007`;
- ADR-0009 registra `DEPENDS_ON=ADR-0005|ADR-0008|ADR-0010`;
- ADR-0010 registra `DEPENDS_ON=ADR-0001|ADR-0002`;
- o índice mestre apresenta apenas a convergência de ADR-0008, ADR-0009 e ADR-0010 para ADR-0011.

Assim, não existe um único modelo autoritativo para distinguir pré-requisito, dependência lógica, influência transversal e obrigação de coerência.

#### Risco

O ciclo torna impossível obter uma ordem de decisão reproduzível caso `->` signifique dependência. Se significar apenas coerência mútua, o mesmo símbolo está sendo usado com duas semânticas. Isso pode produzir Documento Mestre inconsistente e implementação baseada em ordem errada.

#### Correção obrigatória

Separar explicitamente:

```text
DEPENDS_ON=<grafo acíclico de pré-requisitos>
MUST_ALIGN_WITH=<relações bidirecionais permitidas>
GOVERNS=<decisão que restringe outra>
```

Publicar um grafo único e reconciliar plano, índice e campo `DEPENDS_ON` de cada ADR. Validar ausência de ciclo em `DEPENDS_ON`.

### MAJOR-03 — A FSM de comando/grant não fecha supersessão, revogação e lifecycle do grant

#### Evidência

O ADR-0008 afirma adotar uma `Command/Grant FSM`, mas publica:

- estados de comando;
- estados de arming da sessão;
- estados da tentativa.

Não publica estados próprios do `AuthorizationGrant`.

O mesmo ADR declara cobrir `V27-CMD-001..006`, mas sua lista de estados do comando não contém `SUPERSEDED`. A PTM V2.7 exige em `V27-CMD-006` que comando cancelado, expirado ou supersedido nunca retorne à fila.

Além disso, ADR-0008 afirma que comando e grant são imutáveis após `AUTHORIZED`, enquanto:

- `V27-AUT-003` exige revogação antes de nova tentativa;
- ADR-0010 invalida grants ao mudar o `kill_epoch`;
- grants possuem validade e expiração.

A imutabilidade dos campos de autorização pode ser correta, mas o lifecycle de estado e a revogação não foram separados dessa imutabilidade.

#### Risco

Sem estados e transições completos, um grant expirado, revogado ou invalidado por kill switch pode ser interpretado de formas diferentes pelos módulos. Um comando supersedido pode não possuir estado terminal canônico, enfraquecendo serialização, fila e recovery.

#### Correção obrigatória

Definir separadamente:

```text
COMMAND_FSM=<estados e transições>
AUTHORIZATION_GRANT_FSM=<estados e transições>
SESSION_ARMING_FSM=<estados e transições>
EXECUTION_ATTEMPT_FSM=<estados e transições>
```

Incluir ou mapear explicitamente `SUPERSEDED`, revogação, expiração, consumo/invalidação e efeito do `kill_epoch`. Esclarecer:

```text
IMMUTABLE_FIELDS != IMMUTABLE_LIFECYCLE_STATE
```

Demonstrar que nenhum estado permite rearmamento ou redispatch automático após restart.

### MAJOR-04 — Colisão divergente de idempotency key não é bloqueada

#### Evidência

ADR-0011 registra:

```text
DUPLICATE_IDEMPOTENCY_KEY=RETURN_EXISTING_ATTEMPT
```

A PTM V2.7 exige em `V27-CMD-005`:

```text
DUPLICIDADE_EXATA=RETURN_PREVIOUS_RESULT
DUPLICIDADE_DIVERGENTE=BLOCK
```

O ADR não condiciona o retorno ao fingerprint canônico do comando, grant, alvo, adaptador e payload. Assim, a regra documental permite interpretar que qualquer reutilização da chave retorna a tentativa existente.

#### Risco

Uma chave repetida com conteúdo divergente pode ocultar conflito de comando, alvo ou ação e transformar erro de integridade em resposta idempotente aparentemente válida.

#### Correção obrigatória

Definir:

```text
SAME_KEY_AND_SAME_CANONICAL_FINGERPRINT=RETURN_EXISTING_ATTEMPT
SAME_KEY_AND_DIFFERENT_CANONICAL_FINGERPRINT=BLOCK_CONFLICT_AND_AUDIT
```

O fingerprint deve vincular, no mínimo, comando, grant, modo, alvo lógico, adaptador, ação e contexto congelado.

### MINOR-01 — Snapshot final e README não exibem o HEAD ativo correto

#### Evidência

O HEAD revisado é:

```text
2c9c2432058c5f119bd1802c3ba00e845c6a5ca0
```

O `PROJECT_RUNTIME_STATE.yaml` ainda registra:

```text
observed_pr_head=1ee5c0641cab92ed184797776504ab7091fe9972
mission_lock.observed_pr_head=1ee5c0641cab92ed184797776504ab7091fe9972
```

O protocolo do README exige `ACTIVE_PR_HEAD` na primeira dobra e sincronização quando branch, PR ou HEAD mudam. O README do PR #46 não exibe `ACTIVE_PR_HEAD`.

O README também mostra `MINOR_FINDINGS=0_BUILDER`, enquanto a auto-revisão registra um achado menor encontrado e remediado. O valor deveria distinguir achados históricos de achados abertos.

#### Risco

O leitor não consegue provar que o painel e o manifesto correspondem ao HEAD entregue para revisão.

#### Correção obrigatória

Atualizar manifesto, lock consultivo e README no HEAD final do builder, usando:

```text
ACTIVE_PR_HEAD=<head final de remediação>
BUILDER_MINOR_FINDINGS_FOUND=1
BUILDER_MINOR_FINDINGS_REMEDIATED=1
OPEN_BUILDER_MINOR_FINDINGS=0
SNAPSHOT_AT=<timestamp>
STATE_SOURCE=...
```

## 6. Verificações aprovadas

### Contagem e status

```text
ADR_COUNT=12/12
P0_CANDIDATE_MAPPING=12/12
ADR_STATUS_UNIFORM=PROPOSED_FOR_REVIEW
```

### Escopo

```text
DOCUMENTATION_ONLY=PASS
CODE_CHANGE=NO
TEST_CODE_CHANGE=NO
WORKFLOW_CHANGE=NO
SQL_CREATED=NO
MIGRATION_CREATED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

### Domínios e estrutura

Os domínios primários declarados são coerentes com o mapa consolidado:

```text
ADR-0001=DOM-01
ADR-0002=DOM-03
ADR-0003=DOM-01|DOM-03
ADR-0004=DOM-05
ADR-0005=DOM-06
ADR-0006=DOM-11
ADR-0007=DOM-12
ADR-0008=DOM-13|DOM-15
ADR-0009=DOM-14
ADR-0010=DOM-16
ADR-0011=DOM-15
ADR-0012=DOM-16
```

### Qualidade documental

Todos os ADRs possuem contexto, decisão, regras normativas, alternativas, consequências, segurança/recovery, rastreabilidade, critérios de aceitação e fora de escopo.

### Política A+B

```text
MODE_A_POLICY=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_WITHOUT_ALL_GATES=BLOCKED
COMMERCIAL_AND_LEGAL_GATE=PRESERVED
PLATFORM_TERMS_AND_JURISDICTION_GATE=PRESERVED
ACCOUNT_HOLDER_ELIGIBILITY_GATE=PRESERVED
EXPLICIT_LIVE_SCOPE_GATE=PRESERVED
LIVE_MODE_ARMED=NO
```

Nenhum ADR transforma clique controlado em autorização LIVE ou remove os gates comerciais, legais, de conformidade e elegibilidade.

### Segurança aprovada

Foram preservados:

- servidor como autoridade global;
- escritor único;
- sinal diferente de comando;
- comando diferente de grant;
- grant diferente de tentativa;
- tentativa diferente de efeito confirmado;
- coordenada diferente de autorização;
- recibo diferente de verdade global;
- timeout diferente de ausência de efeito;
- `UNKNOWN_EFFECT` bloqueando retry correlato;
- kill switch dominante;
- restart sem rearmamento ou redispatch automático;
- redaction allowlist-first;
- segredos fora do Git.

### CI e PR

```text
PR_STATE=OPEN
PR_DRAFT=NO_AT_REVIEW_START
PR_MERGEABLE=YES
WORKFLOW_RUNS=9
WORKFLOW_SUCCESS=9
WORKFLOW_FAILURE=0
OPEN_REVIEW_THREADS=0
```

## 7. Gate final

```text
A1_PRECONDITIONS=PASS
A2_TEMPLATE_AND_INDEX=PASS
A3_P0_ADRS=12/12
A4_TRACEABILITY=FAIL_MAJOR_01
A5_CROSS_ADR_CONSISTENCY=FAIL_MAJOR_02
A6_BUILDER_SELF_REVIEW=PASS_PRELIMINARY_NOT_FINAL
A7_INDEPENDENT_CRITICAL_REVIEW=FAIL
SECURITY_AND_RECOVERY_INVARIANTS=FAIL_MAJOR_03_MAJOR_04
README_AND_STATE_SYNC=FAIL_MINOR_01
```

## 8. Condição para Reteste 01

```text
MAJOR_01_REMEDIATED=PASS_REQUIRED
MAJOR_02_REMEDIATED=PASS_REQUIRED
MAJOR_03_REMEDIATED=PASS_REQUIRED
MAJOR_04_REMEDIATED=PASS_REQUIRED
MINOR_01_REMEDIATED=PASS_REQUIRED
BUILDER_SELF_REVIEW_RERUN=PASS_PRELIMINARY_REQUIRED
CI_STATUS=PASS_REQUIRED
OPEN_REVIEW_THREADS=0_REQUIRED
RETEST_TARGET_HEAD=NEW_FINAL_BUILDER_HEAD
```

A revisão do Reteste 01 deve ocorrer sobre um novo HEAD final, não sobre o commit deste relatório.

## 9. Próxima ação

Remediar os cinco achados na LEA-26, atualizar a auto-revisão, sincronizar as fontes vivas e solicitar `LEA-27 — Reteste 01` sobre o novo HEAD do PR #46.
