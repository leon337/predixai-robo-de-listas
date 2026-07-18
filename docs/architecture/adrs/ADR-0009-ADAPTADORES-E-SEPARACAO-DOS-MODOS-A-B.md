# ADR-0009 — Adaptadores isolados e separação dos Modos A e B

## Controle

```text
ADR_ID=ADR-0009
CANDIDATE_ID=ADR-CAND-011
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
DEPENDS_ON=ADR-0005|ADR-0008|ADR-0010
MUST_ALIGN_WITH=ADR-0008|ADR-0010|ADR-0011
GOVERNS=NONE
```

## Contexto

Automação de interface é capacidade legítima do projeto, mas análise, coordenada, sinal, perfil ou clique controlado não equivalem a autorização LIVE. Adaptadores são a única fronteira autorizada para produzir efeito externo.

## Decisão

Definir uma porta única com quatro tipos:

```text
NULL
SIMULATED
CONTROLLED_UI
LIVE_GATED
```

`NULL` registra intenção sem efeito. `SIMULATED` produz resultado simulado. `CONTROLLED_UI` atua apenas em alvo autorizado do Modo A. `LIVE_GATED` permanece contrato arquitetural sem implementação ou ativação nesta missão.

Cada adaptador declara identidade, versão, modo, capacidades, ações, plataformas e alvos permitidos. Antes de qualquer `adapter_request`, o servidor valida grant, sessão, `target_logical_id`, perfil, allowlist, capability descriptor e `kill_epoch`.

## Relações arquiteturais

```text
ADR-0005=PROVIDES_PROFILE_AND_LOGICAL_TARGET
ADR-0008=PROVIDES_COMMAND_GRANT_ARMING_AND_ATTEMPT_STATE
ADR-0010=GOVERNS_ALL_EFFECT_PATHS_WITH_KILL_EPOCH
ADR-0011=RECONCILES_RECEIPT_AND_EFFECT
```

A relação com ADR-0010 é pré-requisito e alinhamento de segurança. Não existe dependência inversa de ADR-0010 para ADR-0009; portanto, não existe ciclo em `DEPENDS_ON`.

## Regras normativas

```text
ADAPTER_PORT=SINGLE_CONTROLLED_EFFECT_BOUNDARY
ADAPTER_TYPES=NULL|SIMULATED|CONTROLLED_UI|LIVE_GATED
DEFAULT_ADAPTER=NULL
MODE_A=SIMULATED_OR_CONTROLLED_UI
MODE_B=LIVE_GATED_ONLY
MODE_B_DEFAULT=DISABLED
CONTROLLED_UI!=LIVE_AUTHORIZATION
TARGET_ALLOWLIST=REQUIRED
CAPABILITY_CHECK=REQUIRED
SECRET_ACCESS=ADAPTER_SCOPED_AND_ISOLATED
DIRECT_ENGINE_TO_ADAPTER=PROHIBITED
RAW_COORDINATE_DISPATCH=PROHIBITED
KILL_EPOCH_CHECK_BEFORE_EFFECT=REQUIRED
```

`LIVE_GATED` exige missão futura, decisão comercial/legal, termos e jurisdição, elegibilidade do titular, conta/plataforma em allowlist, limites, kill switch, auditoria, arming humano e confirmação explícita da sessão.

## Alternativas consideradas

### Chamadas diretas de UI

Rejeitadas por criar bypass de autorização, kill switch, testes e auditoria.

### Adaptador genérico com `live=true`

Rejeitado porque uma flag isolada pode elevar capacidade silenciosamente.

### Proibir automação de interface

Rejeitado por contrariar a política A+B e o Modo A controlado.

## Consequências

### Positivas

- Modo A implementável sem habilitar LIVE;
- bibliotecas de ação confinadas;
- allowlists e capability checks centralizados;
- kill switch verificado na fronteira de efeito.

### Negativas e custos

- contratos e testes por adaptador;
- manutenção por plataforma;
- compatibilidade visual vinculada aos perfis.

## Segurança, recovery e falha segura

```text
UNKNOWN_ADAPTER=NULL_OR_BLOCK
CAPABILITY_MISMATCH=BLOCK
TARGET_NOT_ALLOWLISTED=BLOCK
PROFILE_INCOMPATIBLE=BLOCK
KILL_SWITCH_ACTIVE=BLOCK
LIVE_GATE_INCOMPLETE=BLOCK
RESTART=NO_AUTOMATIC_ADAPTER_REARM
SECRET_DETECTED_IN_LOG=SECURITY_FAILURE
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-14
SECONDARY_DOMAINS=DOM-02|DOM-06|DOM-13|DOM-15|DOM-16
HANDOFFS=H-09|H-10|H-11|H-12
REQUIREMENTS=PTM-V27-003|PTM-V27-008|PTM-V27-009|PTM-V27-021|V27-EXE-003|V27-EXE-004|V27-SAF-006|PTM-V27-032
TRACEABILITY_APPENDIX=APENDICE_RASTREABILIDADE_INDIVIDUAL_218_ADRS_P0_LEA-26_20260718.md
```

## Critérios de aceitação

```text
FOUR_ADAPTER_TYPES_DEFINED=PASS
MODE_A_MODE_B_SEPARATION=PASS
LIVE_DEFAULT_DISABLED=PASS
DIRECT_UI_BYPASS_BLOCKED=PASS
ALLOWLIST_AND_CAPABILITY_REQUIRED=PASS
DEPENDENCY_SEMANTICS_RECONCILED=PASS
```

## Fora de escopo

- código de automação;
- bibliotecas específicas;
- integração de corretora;
- credenciais;
- ativação do Modo B.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.