# REGISTRO DE CONFLITOS, SUPERSESSÕES E PRECEDÊNCIA

## PTM V2.5 → PTM V2.6 → PTM V2.7

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_CONFLICT_SUPERSESSION_REGISTER_COMPLETE
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
PRE_WRITE_EXPECTED_PR_HEAD=caadffe3974783229d62695273236e89e09a4a97
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
DOCUMENTATION_ONLY=YES
HISTORICAL_DOCUMENTS_REWRITTEN=NO
IMPLEMENTATION_AUTHORIZED=NO
```

## 2. Método de resolução

Não existe uma única precedência válida para todos os campos. Cada divergência é resolvida pela autoridade do domínio:

| Domínio de informação | Autoridade vigente |
|---|---|
| estado operacional estruturado | `PROJECT_RUNTIME_STATE.yaml` |
| visão humana derivada | `PROJECT_STATE.md` |
| roadmap e sequência | tronco multichat |
| tarefa, dependências e bloqueios | Linear |
| código e documentação integrados | GitHub `main` |
| trabalho ainda não integrado | branch e PR ativos |
| política permanente de automação | `POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md` |
| cláusulas arquiteturais específicas | PTM e adendo normativo aplicável |
| evidência de decisão anterior | revisões, recibos e históricos |

Histórico não é apagado. Uma redação superada permanece evidência do entendimento anterior, mas deixa de governar o presente.

## 3. Precedência normativa explícita

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

Revisão e recibo comprovam aprovação e integração. O conteúdo normativo continua nos documentos arquiteturais e adendos aplicáveis.

## 4. Registro de divergências resolvidas

| ID | Tema | Redação/estado anterior | Decisão vigente | Classificação | Impacto |
|---|---|---|---|---|---|
| CON-01 | `main` versus PR | `main` poderia ser lida como fonte de todo estado atual | `main` governa o integrado; PR `#40` governa somente a consolidação ainda não integrada | NO_CONFLICT_BY_DOMAIN | impede declarar o conteúdo do PR como consolidado antes do merge |
| CON-02 | manifesto versus documentos vivos | divergência poderia ser ignorada por narrativa | manifesto governa campos operacionais; `PROJECT_STATE` e tronco devem refletir o manifesto | RESOLVED_BY_AUTHORITY | drift bloqueia avanço automático |
| CON-03 | Linear versus GitHub | issue em andamento ou PR aberto poderiam ser tratados como equivalentes | status da tarefa e integração são confirmados separadamente | RESOLVED_BY_AUTHORITY | conclusão exige alinhamento dos dois sistemas |
| CON-04 | status `BUILDER_DRAFT` nas PTMs | marcador histórico poderia ser interpretado como PTM ainda não aprovada | revisões independentes e recibos pós-merge tornam V2.5, V2.6 e V2.7 documentalmente definitivas | HISTORICAL_STATUS_SUPERSEDED | preserva o draft sem negar o gate final |
| CON-05 | relatório final V2.5 ausente em Markdown | caminho presumido não existe | autoridade composta: revisão final do PR `#33` + Linear `LEA-13` + recibo pós-merge `LEA-8` | RESOLVED_WITH_COMPOSITE_EVIDENCE | proíbe inventar arquivo ausente |
| CON-06 | exclusão de clique na V2.5 | `POINTER_MOVEMENT_ALLOWED=NO`, `REAL_CLICK_ALLOWED=NO` e equivalentes podiam sugerir proibição global | V2.5 não possui autoridade para ação de UI; geometria e harness controlado são permitidos; ação não controlada é bloqueada | NORMATIVELY_SUPERSEDED | mantém separação de etapa sem remover capacidade técnica controlada |
| CON-07 | exclusão de input na V2.6 | prova negativa podia exigir ausência absoluta de bibliotecas de UI | motor analítico não aciona UI; captura, OCR, replay e harness controlado são permitidos fora da autoridade analítica | NORMATIVELY_SUPERSEDED | prova passa a buscar bypass e acoplamento oculto |
| CON-08 | baseline V2.7 `SIMULATED_ONLY` | modo de execução e dimensão financeira eram tratados como uma única dimensão | `execution_channel=DRY_RUN|SIMULATED|CONTROLLED_UI`; `financial_effect_mode=NONE|SIMULATED_ONLY` | NORMATIVELY_SUPERSEDED | ação física de UI controlada não implica efeito financeiro real |
| CON-09 | estados da V2.7 | fluxo centrado em `ARMED_SIMULATED` não representava UI controlada | estados incluem `ARMED_DRY_RUN`, `ARMED_SIMULATED`, `ARMED_CONTROLLED_UI` e terminais separados | NORMATIVELY_SUPERSEDED | impede mascarar ação física como simulação |
| CON-10 | adaptadores V2.7 | contrato `NULL|SIMULATED` | contrato `NULL|SIMULATED|CONTROLLED_UI` com capacidades explícitas e fail-closed | NORMATIVELY_SUPERSEDED | biblioteca de UI só é alcançável pelo adaptador controlado |
| CON-11 | comando de execução | `mode`, `action_simulated` e alvo mínimo não separavam canal, finanças e identidade | comando contém canal, dimensão financeira, classe/identidade do alvo, allowlist, ação sanitizada e identidade temporal/processual | NORMATIVELY_SUPERSEDED | grant e dispatch passam a ser vinculados ao comando exato |
| CON-12 | grant de autorização | modo e validade eram insuficientes para UI controlada | grant vincula canal, dimensão financeira, alvo, ação/allowlist, política, ator, cliente e sessão | NORMATIVELY_SUPERSEDED | qualquer mudança material exige novo grant |
| CON-13 | recibo de efeito | resultado único `NO_EFFECT|SIMULATED_EFFECT|UNKNOWN` | recibo separa `ui_result` e `financial_result` | NORMATIVELY_SUPERSEDED | efeito de UI não confirma resultado financeiro |
| CON-14 | prazo e restart | monotônico local podia ser interpretado como autoridade após restart | qualquer mudança de `process_instance_id` invalida despachabilidade; UTC/TTL ficam para auditoria e expiração | NORMATIVELY_SUPERSEDED | comando anterior nunca é rearmado ou redespachado automaticamente |
| CON-15 | timeout e retry | timeout poderia ser tratado como falha sem efeito | timeout produz `TIMED_OUT` ou `UNKNOWN_EFFECT`; retry exige prova de `FAILED_NO_EFFECT` | RESOLVED_NORMATIVELY | evita duplicidade de efeito |
| CON-16 | prova negativa | ausência de `pynput`, `pyautogui`, Selenium ou OCR poderia ser exigida globalmente | prova busca ação fora da allowlist, bypass, alvo desconhecido, segredo e efeito financeiro real | NORMATIVELY_SUPERSEDED | ferramentas controladas não falham o gate apenas por existirem |
| CON-17 | classe de alvo e efeito financeiro | sandbox ou aplicação própria poderiam parecer autorização financeira | efeito financeiro real exige gate comercial/legal separado em qualquer classe de alvo | RESOLVED_NORMATIVELY | bloqueio financeiro é independente do alvo |
| CON-18 | coordenadas | pares X/Y poderiam ser tratados como destino executável | coordenada integra geometria versionada de `target_logical_id`; nunca autoriza ação isoladamente | RESOLVED_NORMATIVELY | resolução exige identidade e allowlist |
| CON-19 | recibo versus verdade global | retorno do adaptador poderia encerrar fluxo | recibo é evidência; somente reconciliação do servidor confirma terminalidade | RESOLVED_NORMATIVELY | divergência resulta em `UNKNOWN_EFFECT` ou bloqueio |
| CON-20 | Android/UI versus servidor | cliente poderia confirmar estado ou efeito | Android/UI são clientes; servidor é autoridade global | RESOLVED_NORMATIVELY | cache e presença não substituem estado confirmado |
| CON-21 | catálogo conceitual versus schema físico | endpoint/entidade prevista poderia virar backlog físico automático | entidade física só existe com produtor, consumidor, requisito, teste e retenção | RESOLVED_NORMATIVELY | nenhum SQL ou migration nasce desta consolidação |
| CON-22 | thresholds | valores preliminares poderiam ser congelados como definitivos | thresholds permanecem `PROVISIONAL` até benchmark reproduzível | DEFERRED_WITH_SAFE_DEFAULT | dúvida reduz capacidade e não aumenta confiança |
| CON-23 | especificação versus runtime | teste especificado poderia ser declarado executado | `TEST_SPEC_CREATED` e `TEST_RUNTIME_EXECUTED` permanecem dimensões separadas | RESOLVED_NORMATIVELY | consolidação documental não aprova runtime |
| CON-24 | mergeabilidade versus autorização | PR mergeável poderia ser tratado como autorizado | `GITHUB_MERGEABILITY` e `MERGE_AUTHORIZATION` são estados independentes | RESOLVED_BY_GOVERNANCE | PR `#40` permanece Draft e merge não autorizado |

## 5. Cláusulas históricas preservadas, mas não governantes

Os seguintes marcadores permanecem válidos apenas no contexto temporal em que foram escritos:

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
CONTROLLED_UI_ACTION != REAL_FINANCIAL_EFFECT
UI_LIBRARY_PRESENT != UNCONTROLLED_ACTION
RESTART != RESUME_PREVIOUS_DISPATCHABILITY
```

## 6. Pendências deliberadas para ADR — não são conflitos abertos

| Tema | Default seguro vigente | Motivo para ADR posterior |
|---|---|---|
| topologia do servidor | servidor é autoridade única conceitual | definir processos, componentes e implantação |
| tecnologia de persistência | escritor único e existência progressiva | selecionar engine, transações e migrations |
| taxonomia de `target_logical_id` | alvo desconhecido bloqueia | definir hierarquia e compatibilidade |
| topologia do kill switch | kill switch domina todos os fluxos | definir local/remoto, latência e autoridade |
| limites numéricos | safe defaults conservadores | depender de benchmark reproduzível |
| retenção de frames | conteúdo bruto mínimo por padrão | equilibrar diagnóstico, privacidade e custo |
| contratos REST/eventos | existência vertical progressiva | definir fronteiras e versionamento final |
| máquina de estados física | modelo documental aprovado | decidir persistência e concorrência de implementação |
| recibo e reconciliação | dimensões UI/financeira separadas | definir armazenamento e estratégia operacional |

## 7. Verificações de consistência

```text
CURRENT_POLICY_CONTRADICTS_CONTROLLED_UI=NO
CONTROLLED_UI_IMPLIES_REAL_FINANCIAL_EFFECT=NO
ANALYSIS_CAN_DIRECTLY_CALL_UI_ADAPTER=NO
COORDINATE_IS_AUTHORIZATION=NO
CLIENT_IS_GLOBAL_AUTHORITY=NO
RECEIPT_IS_GLOBAL_TRUTH=NO
PRE_RESTART_COMMAND_CAN_REARM=NO
UNKNOWN_EFFECT_CAN_AUTORETRY=NO
HISTORICAL_DOCUMENTS_REWRITTEN=NO
UNRESOLVED_NORMATIVE_CONFLICTS=0
```

## 8. Resultado do builder — G5

```text
CONFLICT_CLASSES_REVIEWED=24
NORMATIVE_SUPERSESSIONS_RECORDED=PASS
AUTHORITY_BY_DOMAIN_RECORDED=PASS
HISTORICAL_STATUS_PRESERVED=PASS
CONTROLLED_AUTOMATION_PRECEDENCE=PASS
V2_7_RETEST_02_PRECEDENCE=PASS
REAL_FINANCIAL_EFFECT_SEPARATION=PASS
RESTART_FAIL_CLOSED_SEMANTICS=PASS
DOCUMENTAL_VS_RUNTIME_SEPARATION=PASS
MERGEABILITY_VS_AUTHORIZATION_SEPARATION=PASS
UNRESOLVED_NORMATIVE_CONFLICTS=0
CONFLICT_RESOLUTION_BLOCKERS=0
G5_CONFLICTS_AND_SUPERSESSIONS_RESOLVED=PASS_BUILDER
INDEPENDENT_CRITICAL_REVIEW=PENDING
```

## 9. Próxima ação

Publicar o catálogo formal de decisões candidatas a ADR e consolidar o documento arquitetural final da LEA-18.