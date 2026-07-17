# PTM V2.6 — MATRIZ DE RASTREABILIDADE

## LEA-14 — Builder Draft

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DRAFT
MISSION=LEA-14
BASE_MAIN_SHA=1ca1be40b570b3ba458cf28efc73113da2031e8d
STRUCTURAL_REQUIREMENTS=28
FUNCTIONAL_REQUIREMENTS=50
TOTAL_REQUIREMENT_IDS=78
TRACEABILITY_COMPLETENESS=PASS_BUILDER
INDEPENDENT_CRITICAL_REVIEW=PENDING
```

## 2. Fontes abreviadas

| Código | Fonte |
|---|---|
| V25 | `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md` |
| V25-M | `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md` |
| AUD | `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md` e apêndices |
| RC | revisão crítica aprovada da Auditoria Mestra |
| CT | `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md` |
| GOV | instruções, runtime state, PROJECT_STATE e tronco multichat |

## 3. Rastreabilidade estrutural

| ID | Fonte | Legado/classificação | Destino V2.6 | Exclusão V2.7 |
|---|---|---|---|---|
| PTM-V26-001 | V25, AUD | executor `pynput`: DESCONTINUAR na V2.6 | fronteira análise/execução | toda ação física |
| PTM-V26-002 | V25, AUD | perfis e calibração: ADAPTAR | sessão versionada | execução por coordenadas |
| PTM-V26-003 | V25, GOV | janela/perfil visual: ADAPTAR com fail-closed | fonte visual autorizada | auto-seleção insegura |
| PTM-V26-004 | AUD, CT | relatórios/artefatos locais: ADAPTAR | referência e retenção | captura operacional executável |
| PTM-V26-005 | CT, RC | pipeline ausente: NOVO | validação pré-análise | uso de frame inválido |
| PTM-V26-006 | CT, V25 | thresholds não medidos: ADAPTAR | modelo de qualidade | aprovação por score isolado |
| PTM-V26-007 | CT | mecanismo novo | extração versionada | automação física |
| PTM-V26-008 | CT, AUD | market data estruturado ausente: NOVO | séries estimadas | dado oficial presumido |
| PTM-V26-009 | CT | mecanismo novo | snapshot imutável | estado oculto do executor |
| PTM-V26-010 | CT | contratos A–H preliminares: ADAPTAR | envelope comum | efeito físico |
| PTM-V26-011 | CT | contrato A | estrutura | N/A |
| PTM-V26-012 | CT | contrato B | tendência | N/A |
| PTM-V26-013 | CT | contrato C | zonas | N/A |
| PTM-V26-014 | CT | contrato D | volatilidade | N/A |
| PTM-V26-015 | CT | contrato E | candle/contexto | N/A |
| PTM-V26-016 | CT | contrato F | momentum | N/A |
| PTM-V26-017 | CT | contrato G | confluência | N/A |
| PTM-V26-018 | CT | contrato H | estratégia | dispatch/executor |
| PTM-V26-019 | CT | Strategy-001 preliminar: ADAPTAR | versão e regras | execução automática |
| PTM-V26-020 | CT | catálogo lógico: NOVO | arbitragem | escolha por executor |
| PTM-V26-021 | AUD, CT | Signal legado: ADAPTAR | sinal simulado | ordem/clique |
| PTM-V26-022 | AUD, CT | histórico estruturado: ADAPTAR | lifecycle | resultado físico |
| PTM-V26-023 | V25 | contratos progressivos | REST/eventos | endpoint de execução |
| PTM-V26-024 | CT | replay lógico: NOVO | replay sanitizado | acesso à corretora |
| PTM-V26-025 | V25, AUD | logs/diagnóstico: ADAPTAR | correlação completa | telemetria de ordem real |
| PTM-V26-026 | GOV, AUD | risco de artefato local: ADAPTAR | redaction/minimização | segredos/imagens brutas em commit |
| PTM-V26-027 | V25, CT | catálogo físico preliminar: ADAPTAR | existência progressiva | SQL/migration nesta missão |
| PTM-V26-028 | AUD, RC | clique real confirmado: DESCONTINUAR | prova negativa | ponteiro/clique/ordem |

## 4. Rastreabilidade funcional por domínio

| IDs | Fonte | Entrada | Saída | Evidência futura | Bloqueio |
|---|---|---|---|---|---|
| V26-OBS-001..004 | V25, CT, GOV | perfil, janela, ROIs, configuração | sessão e transições | testes de lifecycle | fonte incompatível |
| V26-CAP-001..004 | CT, AUD | frame autorizado | referência, hash e recortes | fixture sanitizada | frame inválido/obsoleto |
| V26-VAL-001..006 | V25, CT | referência e contexto | checks, qualidade e caps | propriedades e negativos | `FAIL` obrigatório |
| V26-MAP-001..005 | CT | recortes elegíveis | extração, série e modelos | determinismo e benchmark | incerteza excessiva |
| V26-ANA-001..011 | CT | snapshot imutável | resultados A–H | testes por motor e replay | blocker A–G |
| V26-STR-001..004 | CT | resultados A–G e estratégia | avaliação explicável | regras/versões | threshold não validado |
| V26-SIG-001..008 | AUD, CT | candidato e arbitragem | sinal simulado/lifecycle | fingerprint e transições | conflito, expiração, contexto |
| V26-RPL-001..003 | CT, GOV | pacote sanitizado | comparação reproduzível | replay offline | acesso externo/físico |
| V26-API-001..002 | V25, CT | produtor+consumidor+requisito | contrato versionado | contract tests | vertical incompleta |
| V26-SEC-001..003 | GOV, AUD, RC | artefatos e dependências | redaction e prova negativa | scans e testes | segredo ou API física |

## 5. Cadeia V2.5 → V2.6

| Fundação V2.5 | Uso V2.6 | Regra |
|---|---|---|
| configuração versionada | versões dos extratores, motores e estratégias | fail-closed |
| perfis/calibração/ROIs | contexto e geometria de observação | compatibilidade obrigatória |
| observabilidade mínima | trace de sessão a sinal | redaction obrigatória |
| contratos versionados | REST/eventos de observação/análise/sinais | existência vertical |
| persistência conceitual | entidades lógicas V2.6 | sem schema físico nesta missão |
| listas independentes | exportação de sinal simulado | sem agenda executável |
| bloqueio de clique V2.5 | prova negativa V2.6 | execução permanece V2.7 |

## 6. Fronteira V2.6 → V2.7

```text
V2_6_OUTPUT=SIMULATED_SIGNAL_AND_EVIDENCE
V2_7_INPUT_MAY_REFERENCE=VALIDATED_SIGNAL
V2_6_MUST_NOT_CREATE=EXECUTION_REQUEST|CLICK_EVENT|REAL_ORDER|REAL_BALANCE_CHANGE
V2_7_START_AUTHORIZED=NO
```

## 7. Reconciliação de contagem

```text
STRUCTURAL_IDS=PTM-V26-001..028
FUNCTIONAL_IDS=
  V26-OBS-001..004
  V26-CAP-001..004
  V26-VAL-001..006
  V26-MAP-001..005
  V26-ANA-001..011
  V26-STR-001..004
  V26-SIG-001..008
  V26-RPL-001..003
  V26-API-001..002
  V26-SEC-001..003

STRUCTURAL_COUNT=28
FUNCTIONAL_COUNT=50
TOTAL_COUNT=78
DUPLICATE_IDS=0
```

## 8. Gate do builder

```text
REQUIREMENT_ID_UNIQUENESS=PASS_BUILDER
TRACEABILITY_COMPLETENESS=PASS_BUILDER
LEGACY_CLASSIFICATION_CONSISTENCY=PASS_BUILDER
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS_BUILDER
EXECUTION_EXCLUSION=PASS_BUILDER
INDEPENDENT_CRITICAL_REVIEW=PENDING
```

A revisão independente deverá confrontar cada requisito, fonte, classificação, fronteira de versão e critério de evidência.