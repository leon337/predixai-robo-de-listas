# PROMPT — RETESTE INDEPENDENTE DA SIMPLIFICAÇÃO DOCUMENTAL

```text
REVIEW_ISSUE=LEA-149
BUILDER_ISSUE=LEA-146
PREVIOUS_REVIEW=LEA-147_DONE_FAIL
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=74
BASE_MAIN_SHA=40aca6ff9c470e44ea37e2d066092bc1349564fc
RETEST_HEAD=EXACT_HEAD_PINNED_IN_LEA_149_AND_PR_74
DOCUMENTATION_ONLY=YES
MERGE_AUTHORIZED=NO
LST_001_AUTHORIZED=NO
```

## Objetivo

Executar um reteste independente da remediação documental da LEA-146 após a autorização humana que simplificou o tratamento das capturas locais.

## Decisão humana vinculante para este reteste

```text
CAPTURES_ROLE=LOCAL_VISUAL_CORROBORATION_REPORTED_BY_LEO
PERSISTENT_IMAGE_BINARIES_REQUIRED=NO
INDEPENDENT_HASH_RECALCULATION_REQUIRED=NO
CHAIN_OF_CUSTODY_REQUIRED=NO
FORENSIC_EVIDENCE_CLAIMED=NO
```

O reteste não deve reintroduzir exigência de anexos binários, hashes auditáveis ou cadeia de custódia. Deve verificar se a documentação descreve com precisão a limitação da evidência.

## Verificações obrigatórias

1. Confirmar que o PR #74 está aberto, Draft e fixado no mesmo HEAD informado externamente na LEA-149.
2. Confirmar que somente arquivos documentais foram alterados.
3. Confirmar que `PROJECT_RUNTIME_STATE.yaml` registra:
   - `active_review_issue: LEA-149`;
   - `active_pull_request: 74`;
   - `current_gate: SIMPLIFIED_EVIDENCE_POLICY_RETEST`;
   - `state_revision: 44`;
   - F01 remediado e F02 resolvido por decisão humana de escopo.
4. Confirmar que o relatório:
   - classifica as fotos como corroboração visual local;
   - separa observação visual de relato humano;
   - não declara binários persistentes, cadeia de custódia, hashes auditáveis ou prova forense;
   - preserva os limites `NULL_ONLY`.
5. Confirmar consistência entre:
   - `PROJECT_STATE.md`;
   - `PROJECT_RUNTIME_STATE.yaml`;
   - `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
   - `README.md`;
   - relatório da LEA-146.
6. Confirmar ausência de alterações em código da aplicação, testes, workflows, SQL, migrations ou runtime operacional.
7. Confirmar que LST-001 permanece apenas candidata, sem autorização.
8. Confirmar que nenhum merge foi autorizado.

## Critério de decisão

```text
DECISION=PASS
```

Somente quando todas as verificações acima passarem e não houver achados bloqueantes.

Caso contrário:

```text
DECISION=FAIL
OPEN_BLOCKING_FINDINGS=<N>
```

## Publicação

Publicar a decisão no PR #74 e na LEA-149. Não editar a branch do builder, não promover o PR e não realizar merge.