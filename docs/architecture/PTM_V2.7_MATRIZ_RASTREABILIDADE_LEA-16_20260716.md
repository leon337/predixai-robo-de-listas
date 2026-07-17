# PTM V2.7 — MATRIZ DE RASTREABILIDADE

## LEA-16 — Builder remediado para reteste

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_TRACEABILITY_REMEDIATED_READY_FOR_RETEST
MISSION=LEA-16
BASE_MAIN_SHA=f3c84d97523c1c631392cefb69b6cb3e8f6a56e2
PARENT_DOCUMENT=docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md
CONTROLLED_AUTOMATION_POLICY=docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md
TRANSVERSAL_ADDENDUM=docs/architecture/ADENDO_TRANSVERSAL_AUTOMACAO_CONTROLADA_PTM_V2.5_V2.7_20260717.md
STRUCTURAL_REQUIREMENTS=32
FUNCTIONAL_REQUIREMENTS=52
TOTAL_REQUIREMENT_IDS=84
TRACEABILITY_COMPLETENESS=PASS_BUILDER_REMEDIATED
INDEPENDENT_CRITICAL_RETEST=PENDING
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
```

## 2. Fontes abreviadas

| Código | Fonte |
|---|---|
| V25 | `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md` |
| V25-M | `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md` |
| V26 | `docs/architecture/PTM_V2.6_OBSERVACAO_ANALISE_SINAIS_LEA-14_20260716.md` |
| V26-M | `docs/architecture/PTM_V2.6_MATRIZ_RASTREABILIDADE_LEA-14_20260716.md` |
| AUD | Auditoria Mestra V2.4.3-R1, Anexo A e apêndices |
| RC | revisões críticas independentes aprovadas |
| GOV | instruções, runtime state, PROJECT_STATE, tronco e protocolos |
| CAP | política e adendo transversal de automação controlada |
| L16 | issue Linear `LEA-16` |

## 3. Semântica de tratamento do legado

```text
REUTILIZAR=preservar comportamento ou evidência comprovada
ADAPTAR=preservar comportamento com nova fronteira ou contrato
SUBSTITUIR=mecanismo legado não serve como base futura
DESCONTINUAR=ação ou mecanismo não pertence ao baseline específico
NOVO=sem equivalente confirmado no legado
```

`DESCONTINUAR` em uma etapa não significa proibição global. Automação de UI em alvo próprio ou sandbox é regida pela política CAP.

## 4. Rastreabilidade estrutural

| ID | Fonte | Legado/classificação | Destino V2.7 | Evidência futura |
|---|---|---|---|---|
| PTM-V27-001 | V26, V26-M | sinal legado: ADAPTAR; acoplamento direto sinal→clique: SUBSTITUIR | domínios separados | testes de fronteira |
| PTM-V27-002 | GOV, CAP, L16 | efeito financeiro real não autorizado; UI controlada autorizada | `FINANCIAL_SIMULATED_ONLY` + `CONTROLLED_UI_ALLOWED` | configuração e testes de alvo |
| PTM-V27-003 | AUD, V25-M, CAP | executor direto sem fronteira: SUBSTITUIR; comportamento de UI: ADAPTAR | adaptador controlado permitido; adaptador financeiro externo ausente | scan de fronteira e allowlist |
| PTM-V27-004 | V25, V26 | `command_id`: ADAPTAR_FROM_V2_5; sinal versionado: ADAPTAR_FROM_V2_6; agregado `ExecutionCommand`: NOVO | comando imutável | contract tests |
| PTM-V27-005 | V25, GOV | Android/cliente: NOVO sem autoridade global | autorização limitada | testes de auth/revogação |
| PTM-V27-006 | V25, V26 | fail-closed: ADAPTAR | snapshot e revalidação | mutation tests |
| PTM-V27-007 | GOV, L16 | mecanismo ausente: NOVO | policy engine puro | tabela de decisão |
| PTM-V27-008 | V25-M, AUD, CAP | coordenadas: ADAPTAR geometria; ação direta não controlada: SUBSTITUIR | alvo lógico versionado e allowlisted | testes de incompatibilidade |
| PTM-V27-009 | V25, CAP | adaptadores de plataforma: ADAPTAR | contrato `NULL`, `SIMULATED` e `CONTROLLED_UI` | contract tests |
| PTM-V27-010 | V25 | auditoria de comando: ADAPTAR | intent antes de efeito | crash tests |
| PTM-V27-011 | V25 | idempotência de migração: ADAPTAR | chave por comando | testes de repetição |
| PTM-V27-012 | V26 | fingerprint/deduplicação: ADAPTAR | registry de dedupe | concorrência |
| PTM-V27-013 | V25-M, AUD | runtime guard ADAPTAR; monkey patches SUBSTITUIR | state machine explícita | transition tests |
| PTM-V27-014 | GOV | mecanismo novo | expiração UTC estável + TTL + boot/clock + orçamento monotônico local | restart e clock-skew tests |
| PTM-V27-015 | GOV | retry inseguro: SUBSTITUIR | retry somente sem efeito | fault injection |
| PTM-V27-016 | V25, AUD | guardas: ADAPTAR | circuit breaker | threshold tests |
| PTM-V27-017 | V25 | rate limit: ADAPTAR | limites operacionais | property tests |
| PTM-V27-018 | V26 | arbitragem: ADAPTAR | serialização por alvo | concurrency tests |
| PTM-V27-019 | GOV, L16 | kill switch ausente: NOVO | contenção dominante | property tests |
| PTM-V27-020 | V25, GOV | cliente não é autoridade | human-in-the-loop | auth tests |
| PTM-V27-021 | V26, CAP | replay seguro: ADAPTAR | dry-run, simulação e harness controlado | fixtures sanitizadas |
| PTM-V27-022 | V26, GOV | fonte externa não é autoridade | recibo como evidência | receipt tests |
| PTM-V27-023 | V25 | reconciliação de migração: ADAPTAR | reconciliação de efeito | contagem/hash |
| PTM-V27-024 | V25 | rollback/recovery: ADAPTAR | compensação como novo comando | compensation tests |
| PTM-V27-025 | GOV | mecanismo ausente: NOVO | contenção de efeito desconhecido | fault injection |
| PTM-V27-026 | V25-M | logs/auditoria: ADAPTAR | trilhas separadas | audit completeness |
| PTM-V27-027 | V25, V26 | `trace_id` e cadeia a sinal: ADAPTAR | trace até reconciliação | trace assertions |
| PTM-V27-028 | GOV, AUD | artefatos locais sensíveis: ADAPTAR | rejeição/redaction | secret scans |
| PTM-V27-029 | V25, V26 | contratos progressivos: ADAPTAR | existência vertical | producer-consumer tests |
| PTM-V27-030 | V25 | recovery seguro: ADAPTAR | restart sem redespacho | crash/restart tests |
| PTM-V27-031 | AUD, RC, CAP | ferramentas de UI: ADAPTAR em escopo controlado; ação não autorizada: SUBSTITUIR | prova negativa de ação não controlada e efeito financeiro real | AST/import/contract/runtime scan |
| PTM-V27-032 | GOV | ativação financeira real não autorizada | gate futuro separado | ADR + RC + GO |

## 5. Rastreabilidade funcional por domínio

| IDs | Fonte | Entrada | Saída | Evidência futura | Bloqueio dominante |
|---|---|---|---|---|---|
| V27-PRE-001..006 | V25, GOV | configuração, sessão, dependências | estado seguro e snapshot | lifecycle tests | elevação automática |
| V27-CMD-001..006 | V26, V26-M | sinal elegível | comando imutável | fingerprint/idempotência | sinal inválido ou mutação |
| V27-AUT-001..006 | V25, GOV | comando + ator + política | grant/revogação/decisão | auth e policy tests | ausência ou expiração |
| V27-EXE-001..008 | GOV, CAP, L16 | comando autorizado | tentativa/recibo simulado ou controlado | adapter e fault tests | capability mismatch/kill |
| V27-SAF-001..008 | V25, AUD, RC, CAP | limites, fila, alvo e dependências | contenção e rejeição | property/negative tests | alvo não allowlisted/segredo |
| V27-REC-001..006 | V25, GOV | tentativa + recibo | reconciliação/terminal state | hash e divergência | efeito desconhecido |
| V27-OBS-001..005 | V25, V26 | cadeia completa | audit/trace/métricas | completeness tests | lacuna ou dado sensível |
| V27-QA-001..007 | GOV, RC, CAP | especificação e fixtures | evidência verificável | suíte futura | fonte externa não autorizada |

## 6. Cadeia V2.5 → V2.6 → V2.7

| Fundação V2.5 | Produto V2.6 | Uso V2.7 | Regra |
|---|---|---|---|
| configuração versionada | versões de análise e estratégia | política, limites e adaptador versionados | fail-closed |
| perfis/calibração/ROIs | fonte visual e contexto | alvo lógico e compatibilidade | coordenada não autoriza sozinha |
| `trace_id`/`command_id` | trace até sinal | trace até reconciliação | correlação integral |
| servidor `SAFE_IDLE` | sessão de observação | executor `DISABLED/SAFE_IDLE` | sem autoelevação |
| Android Foundation | painel e estado | autorização explícita | cliente não é autoridade |
| observabilidade | sessão a sinal | sinal a efeito simulado/controlado | auditoria separada |
| existência progressiva | contratos de análise/sinal | contratos de execução | vertical completa |
| recovery | replay seguro | restart sem redespacho | evidência preservada |
| fronteira de etapa | sinal sem ação própria | adaptador controlado allowlisted | ação de UI separada do efeito financeiro |

## 7. Fronteira V2.6 → V2.7

```text
V2_6_OUTPUT=VALIDATED_SIMULATED_SIGNAL_AND_EVIDENCE
V2_7_ACCEPTS_ONLY=ELIGIBLE_SIGNAL_REFERENCE
V2_7_CREATES=COMMAND|AUTHORIZATION|SIMULATED_OR_CONTROLLED_ATTEMPT|RECEIPT|RECONCILIATION
V2_7_CONTROLLED_UI_ACTION=ALLOWED_FOR_FIRST_PARTY_OR_ALLOWLISTED_TEST_TARGET
V2_7_MUST_NOT_CREATE=UNAUTHORIZED_EXTERNAL_ACCESS|REAL_FINANCIAL_ORDER|REAL_BALANCE_CHANGE|PRODUCTION_CREDENTIAL_STORE
FINANCIAL_EFFECT_BASELINE=SIMULATED_ONLY
CONTROLLED_UI_ACTION_BASELINE=ALLOWED
```

## 8. Tratamento explícito do legado de execução

| Evidência factual | Classificação V2.7 | Tratamento |
|---|---|---|
| `pynput` e caminhos de clique | ADAPTAR comportamento; SUBSTITUIR acesso direto sem guardas | somente por adaptador controlado, allowlist, autorização, kill switch e auditoria |
| `coordinates.LARANJA/CINZA` | ADAPTAR geometria | alvo lógico versionado e compatível |
| `_test_both_coordinates` | ADAPTAR intenção e ação para harness controlado | teste em aplicação própria/sandbox, com parada e auditoria |
| `runtime_guard.py` | ADAPTAR | lifecycle, lock, logging e diagnóstico explícitos |
| monkey patch/bootstrap encadeado | SUBSTITUIR | composição e state machine explícitas |
| `diagnostics_tools.py` e TXT | REUTILIZAR comportamento; ADAPTAR contrato | relatório sanitizado e rastreável |
| `ConfigSafetyManager`/backups | ADAPTAR | integridade, recovery e preservação de origem |
| `Signal` e histórico JSON | ADAPTAR conceitos; SUBSTITUIR autoridade | entidades versionadas e fonte controlada futura |

## 9. Reconciliação de contagem

```text
STRUCTURAL_IDS=PTM-V27-001..032
FUNCTIONAL_IDS=
  V27-PRE-001..006
  V27-CMD-001..006
  V27-AUT-001..006
  V27-EXE-001..008
  V27-SAF-001..008
  V27-REC-001..006
  V27-OBS-001..005
  V27-QA-001..007

STRUCTURAL_COUNT=32
FUNCTIONAL_COUNT=52
TOTAL_COUNT=84
DUPLICATE_IDS=0
```

## 10. Gates do builder remediado

```text
REQUIREMENT_ID_UNIQUENESS=PASS_BUILDER
TRACEABILITY_COMPLETENESS=PASS_BUILDER_REMEDIATED
LEGACY_CLASSIFICATION_CONSISTENCY=PASS_BUILDER_REMEDIATED
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS_BUILDER
CONTROLLED_AUTOMATION_POLICY=PASS_BUILDER
CONTROLLED_UI_FINANCIAL_EFFECT_SEPARATION=PASS_BUILDER
RESTART_STABLE_DEADLINE=PASS_BUILDER_REMEDIATED
UNCONTROLLED_ACTION_NEGATIVE_PROOF_SPECIFIED=PASS_BUILDER
REAL_FINANCIAL_EFFECT_NEGATIVE_PROOF_SPECIFIED=PASS_BUILDER
INDEPENDENT_CRITICAL_RETEST=PENDING
```

O reteste independente deverá confrontar requisitos, fontes, classificação do legado, política de alvo controlado, prazo recuperável, separação UI/efeito financeiro e ausência de acesso externo não autorizado.
