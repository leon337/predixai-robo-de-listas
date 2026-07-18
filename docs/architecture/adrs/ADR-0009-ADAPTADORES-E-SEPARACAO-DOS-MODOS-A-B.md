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
```

## Contexto

O projeto reconhece automação de interface como capacidade legítima, mas precisa impedir que análise, coordenada, sinal, perfil ou clique controlado sejam confundidos com autorização LIVE. Adaptadores são a única fronteira autorizada para produzir efeito externo.

## Decisão

Definir uma porta de adaptador única com quatro tipos de capacidade:

```text
NULL
SIMULATED
CONTROLLED_UI
LIVE_GATED
```

`NULL` registra intenção sem efeito. `SIMULATED` produz resultado simulado e auditável. `CONTROLLED_UI` executa ação de interface em alvo autorizado do Modo A. `LIVE_GATED` é contrato arquitetural reservado e permanece sem implementação/ativação nesta missão.

Cada adaptador declara `adapter_id`, versão, modo, capacidades, tipos de ação, plataformas e alvos autorizados. O servidor resolve `target_logical_id`, valida allowlist, grant, sessão, kill switch e capability descriptor antes de criar `adapter_request`.

Bibliotecas de ponteiro, teclado, browser automation ou integração externa só podem existir atrás dessa fronteira.

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
```

O `LIVE_GATED` exige, em missão futura própria: decisão comercial/legal, termos e jurisdição, elegibilidade do titular, conta e plataforma em allowlist, limites, kill switch, auditoria, arming humano e confirmação explícita da sessão.

## Alternativas consideradas

### Chamadas diretas de UI pelos módulos

Rejeitadas por criar bypass de autorização, testes e auditoria.

### Um adaptador genérico com flag `live=true`

Rejeitado porque uma flag isolada pode elevar capacidade silenciosamente.

### Proibir qualquer automação de interface

Rejeitado por contrariar a política A+B e o objetivo do Modo A controlado.

## Consequências

### Positivas

- testes com `NULL` e `SIMULATED`;
- Modo A implementável sem habilitar LIVE;
- bibliotecas perigosas confinadas;
- allowlists e capability checks centralizados.

### Negativas e custos

- mais contratos e testes por adaptador;
- plataformas diferentes exigem implementações específicas;
- adaptação visual precisa acompanhar perfis versionados.

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
DEPENDS_ON=ADR-0005|ADR-0008|ADR-0010
```

## Critérios de aceitação

```text
FOUR_ADAPTER_TYPES_DEFINED=PASS
MODE_A_MODE_B_SEPARATION=PASS
LIVE_DEFAULT_DISABLED=PASS
DIRECT_UI_BYPASS_BLOCKED=PASS
ALLOWLIST_AND_CAPABILITY_REQUIRED=PASS
```

## Fora de escopo

- código de automação;
- biblioteca Selenium/Puppeteer/pyautogui;
- integração de corretora;
- credenciais;
- ativação do Modo B.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.