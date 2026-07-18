# REGISTRO DE CONFLITOS, SUPERSESSÕES E PRECEDÊNCIA

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_CONFLICT_SUPERSESSION_REGISTER_REMEDIATED_FOR_RETEST_05
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASELINE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
CURRENT_MAIN_OBSERVED=236bc5df7f675ca5cf56d80c5812bd911d224651
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
HISTORICAL_DOCUMENTS_REWRITTEN=NO
IMPLEMENTATION_AUTHORIZED=NO
POLICY_A_B_ALIGNMENT=PASS_BUILDER
```

## 2. Método de resolução

Cada divergência é resolvida pela autoridade do domínio:

| Domínio de informação | Autoridade vigente |
|---|---|
| estado operacional estruturado | `PROJECT_RUNTIME_STATE.yaml` |
| visão humana derivada | `PROJECT_STATE.md` |
| roadmap e sequência | tronco multichat |
| tarefa, dependências e bloqueios | Linear |
| código e documentação integrados | GitHub `main` |
| trabalho ainda não integrado | branch e PR ativos |
| política permanente de automação A+B | `POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` |
| cláusulas arquiteturais específicas | PTM e adendo aplicável |
| evidência de decisão anterior | revisões, recibos e históricos |

Histórico não é apagado. Uma redação superada permanece evidência do entendimento anterior, mas deixa de governar o presente.

## 3. Precedência normativa

### 3.1 Automação e PTM V2.7

```text
POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
> PTM_V2.7_ADENDO_RETESTE_02_CONTROLLED_UI_CLOCK
> ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA
> PTM_V2.7_ADENDO_REMEDIACAO_01_FOR_NON_CONFLICTING_CLAUSES
> PTM_V2.7_PARENT_FOR_NON_CONFLICTING_CLAUSES
> BUILDER_SELF_REVIEWS_AND_HISTORICAL_CHECKPOINTS
```

### 3.2 PTM V2.5 e V2.6

```text
POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO
> ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA
> FINAL_INDEPENDENT_REVIEW_AND_POST_MERGE_RECEIPT
> PTM_PARENT_FOR_NON_SUPERSEDED_CLAUSES
> BUILDER_DRAFT_STATUS_AND_HISTORICAL_CHECKPOINTS
```

## 4. Registro de divergências resolvidas

| ID | Tema | Redação/estado anterior | Decisão vigente | Classificação | Impacto |
|---|---|---|---|---|---|
| CON-01 | `main` versus PR | `main` poderia ser lida como fonte de todo estado atual | `main` governa o integrado; PR `#40` governa a consolidação não integrada | NO_CONFLICT_BY_DOMAIN | impede declarar conteúdo do PR como consolidado antes do merge |
| CON-02 | manifesto versus documentos vivos | divergência podia ser ignorada por narrativa | manifesto governa campos operacionais; estado e tronco o refletem | RESOLVED_BY_AUTHORITY | drift bloqueia avanço automático |
| CON-03 | Linear versus GitHub | issue e PR podiam ser tratados como equivalentes | tarefa e integração são confirmadas separadamente | RESOLVED_BY_AUTHORITY | conclusão exige alinhamento dos dois sistemas |
| CON-04 | status `BUILDER_DRAFT` nas PTMs | marcador histórico parecia indicar PTM não aprovada | revisões e recibos tornam V2.5, V2.6 e V2.7 definitivas | HISTORICAL_STATUS_SUPERSEDED | preserva o draft sem negar o gate final |
| CON-05 | relatório final V2.5 ausente | caminho presumido não existe | autoridade composta: PR `#33` + Linear `LEA-13` + recibo `LEA-8` | RESOLVED_WITH_COMPOSITE_EVIDENCE | proíbe inventar arquivo ausente |
| CON-06 | exclusão de clique na V2.5 | `POINTER_MOVEMENT_ALLOWED=NO`, `REAL_CLICK_ALLOWED=NO` sugeriam proibição global | V2.5 não possui autoridade para ação; Modo A permanece autorizado | NORMATIVELY_SUPERSEDED | mantém separação sem remover capacidade controlada |
| CON-07 | exclusão de input na V2.6 | prova negativa exigia ausência de bibliotecas de UI | motor analítico não aciona UI; captura, OCR, replay e harness controlado são permitidos | NORMATIVELY_SUPERSEDED | prova busca bypass e acoplamento oculto |
| CON-08 | baseline V2.7 `SIMULATED_ONLY` | canal e efeito financeiro eram uma dimensão única | canal e efeito são dimensões separadas; Modo A autorizado e Modo B gated | NORMATIVELY_SUPERSEDED | ação de UI não implica LIVE |
| CON-09 | estados da V2.7 | fluxo centrado somente em `ARMED_SIMULATED` | estados incluem DRY_RUN, SIMULATED, CONTROLLED_UI e futuro LIVE_GATED | NORMATIVELY_SUPERSEDED | impede mascarar canal ou efeito |
| CON-10 | adaptadores V2.7 | contrato `NULL|SIMULATED` | `NULL|SIMULATED|CONTROLLED_UI`; suporte LIVE exige gate próprio | NORMATIVELY_SUPERSEDED | biblioteca de UI fica na fronteira controlada |
| CON-11 | comando de execução | campos não separavam canal, finanças e identidade | comando contém canal, modo financeiro, alvo, allowlist, ação e identidade temporal | NORMATIVELY_SUPERSEDED | grant e dispatch vinculados ao comando exato |
| CON-12 | grant de autorização | modo e validade insuficientes | grant vincula canal, modo financeiro, alvo, ação, política, ator e sessão | NORMATIVELY_SUPERSEDED | mudança material exige novo grant |
| CON-13 | recibo de efeito | resultado único | recibo separa `ui_result` e `financial_result` | NORMATIVELY_SUPERSEDED | efeito de UI não confirma finanças |
| CON-14 | prazo e restart | monotônico local parecia autoridade após restart | mudança de `process_instance_id` invalida despachabilidade | NORMATIVELY_SUPERSEDED | comando anterior não é rearmado automaticamente |
| CON-15 | timeout e retry | timeout podia ser falha sem efeito | timeout gera `TIMED_OUT` ou `UNKNOWN_EFFECT`; retry exige `FAILED_NO_EFFECT` | RESOLVED_NORMATIVELY | evita duplicidade |
| CON-16 | prova negativa | ausência de ferramentas de UI era exigida | prova busca ação fora da allowlist, bypass, alvo desconhecido, segredo e LIVE sem gates | NORMATIVELY_SUPERSEDED | ferramentas controladas não falham por existir |
| CON-17 | classe de alvo e Modo B | sandbox ou aplicação própria pareciam autorização financeira | Modo B requer todos os gates técnicos, comerciais, legais e de conformidade em qualquer classe de alvo | RESOLVED_NORMATIVELY | gate LIVE é independente da propriedade do alvo |
| CON-18 | coordenadas | pares X/Y eram destino executável | coordenada integra geometria de `target_logical_id`; não autoriza isoladamente | RESOLVED_NORMATIVELY | exige identidade e allowlist |
| CON-19 | recibo versus verdade global | retorno do adaptador encerrava fluxo | recibo é evidência; reconciliação do servidor confirma terminalidade | RESOLVED_NORMATIVELY | divergência vira `UNKNOWN_EFFECT` ou bloqueio |
| CON-20 | Android/UI versus servidor | cliente podia confirmar estado | Android/UI são clientes; servidor é autoridade global | RESOLVED_NORMATIVELY | cache e presença não substituem estado |
| CON-21 | catálogo versus schema físico | entidade prevista virava backlog físico | entidade física exige produtor, consumidor, requisito, teste e retenção | RESOLVED_NORMATIVELY | nenhum SQL nasce desta consolidação |
| CON-22 | thresholds | valores preliminares podiam ser definitivos | thresholds permanecem provisórios até benchmark | DEFERRED_WITH_SAFE_DEFAULT | dúvida reduz capacidade |
| CON-23 | especificação versus runtime | teste especificado era tratado como executado | especificação e execução são dimensões separadas | RESOLVED_NORMATIVELY | documentação não aprova runtime |
| CON-24 | mergeabilidade versus autorização | PR mergeável parecia autorizado ou seu modo Draft/ready era tratado como permanente | mergeabilidade, autorização e modo operacional do PR são estados independentes e temporais | RESOLVED_BY_GOVERNANCE | após `FAIL` o PR retorna a Draft; no handoff de novo reteste pode voltar a ready sem conceder merge |

## 5. Cláusulas históricas preservadas, mas não governantes

```text
POINTER_MOVEMENT_ALLOWED=NO
REAL_CLICK_ALLOWED=NO
REAL_INPUT_PROHIBITED
V2_6_REAL_INPUT_BLOCKED
REAL_EFFECT_NEGATIVE_PROOF=ABSENCE_OF_UI_LIBRARIES
EXECUTION_MODE_ALLOWED=DISABLED|DRY_RUN|SIMULATED_ONLY
ADAPTER_CAPABILITY=NULL|SIMULATED_ONLY
ARMED_SIMULATED_AS_ONLY_ARMED_STATE
ACTION_SIMULATED_AS_ONLY_ACTION_FIELD
MONOTONIC_DEADLINE_AS_POST_RESTART_AUTHORITY
```

Leitura vigente:

```text
STAGE_DOES_NOT_OWN_UI_ACTION != GLOBAL_UI_CAPABILITY_PROHIBITION
MODE_A_CONTROLLED_UI_ACTION=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_DEFAULT=DISABLED
LIVE_WITHOUT_ALL_GATES=BLOCKED
UI_LIBRARY_PRESENT != UNCONTROLLED_ACTION
RESTART != RESUME_PREVIOUS_DISPATCHABILITY
```

## 6. Pendências deliberadas para ADR

| Tema | Default seguro vigente | Motivo para ADR posterior |
|---|---|---|
| topologia do servidor | servidor é autoridade única conceitual | definir processos e implantação |
| persistência | escritor único e existência progressiva | selecionar engine e transações |
| `target_logical_id` | alvo desconhecido bloqueia | definir taxonomia e compatibilidade |
| kill switch | domina todos os fluxos | definir local/remoto, latência e autoridade |
| limites numéricos | defaults conservadores | benchmark reproduzível |
| retenção de frames | conteúdo bruto mínimo | privacidade, diagnóstico e custo |
| contratos REST/eventos | existência vertical progressiva | definir fronteiras e versionamento |
| máquina de estados física | modelo documental aprovado | decidir persistência e concorrência |
| recibo e reconciliação | UI e finanças separadas | definir armazenamento e operação |
| gate LIVE | Modo B desligado por padrão | formalizar termos, elegibilidade, limites, arming e auditoria |

## 7. Verificações de consistência

```text
CURRENT_POLICY_CONTRADICTS_CONTROLLED_UI=NO
MODE_A_CONTROLLED_UI=AUTHORIZED
MODE_B_ARCHITECTURAL_SUPPORT=AUTHORIZED
MODE_B_AUTO_ENABLE=NO
LIVE_WITHOUT_ALL_GATES=BLOCKED
ANALYSIS_CAN_DIRECTLY_CALL_UI_ADAPTER=NO
COORDINATE_IS_AUTHORIZATION=NO
CLIENT_IS_GLOBAL_AUTHORITY=NO
RECEIPT_IS_GLOBAL_TRUTH=NO
PRE_RESTART_COMMAND_CAN_REARM=NO
UNKNOWN_EFFECT_CAN_AUTORETRY=NO
HISTORICAL_DOCUMENTS_REWRITTEN=NO
UNRESOLVED_NORMATIVE_CONFLICTS=0
PR_MODE_IS_TEMPORAL=YES
MERGEABILITY_IS_NOT_AUTHORIZATION=YES
```

## 8. Resultado do builder — G5

```text
CONFLICT_CLASSES_REVIEWED=24
NORMATIVE_SUPERSESSIONS_RECORDED=PASS
AUTHORITY_BY_DOMAIN_RECORDED=PASS
HISTORICAL_STATUS_PRESERVED=PASS
CONTROLLED_AUTOMATION_PRECEDENCE=PASS
POLICY_A_B_ALIGNMENT=PASS_BUILDER
V2_7_RETEST_02_PRECEDENCE=PASS
RESTART_FAIL_CLOSED_SEMANTICS=PASS
DOCUMENTAL_VS_RUNTIME_SEPARATION=PASS
MERGEABILITY_VS_AUTHORIZATION_SEPARATION=PASS
PR_DRAFT_READY_TEMPORAL_SEMANTICS=PASS_BUILDER
UNRESOLVED_NORMATIVE_CONFLICTS=0
CONFLICT_RESOLUTION_BLOCKERS=0
G5_CONFLICTS_AND_SUPERSESSIONS_RESOLVED=PASS_BUILDER_REMEDIATED
INDEPENDENT_CRITICAL_REVIEW=RETEST_05_REQUIRED
```

## 9. Próxima ação

Executar o Reteste 05 independente da LEA-19 sobre o HEAD final do PR #40.
