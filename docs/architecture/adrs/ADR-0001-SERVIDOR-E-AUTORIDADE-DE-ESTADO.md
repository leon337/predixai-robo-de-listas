# ADR-0001 — Servidor como autoridade global de estado

## Controle

```text
ADR_ID=ADR-0001
CANDIDATE_ID=ADR-CAND-001
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

O sistema terá painel mobile-first, servidor local no Linux Mint, fontes visuais externas e futuros adaptadores de ação. Sem autoridade única, clientes, caches, OCR, recibos locais ou processos reiniciados poderiam produzir estados conflitantes.

## Decisão

Adotar um **monólito modular orientado a domínios**, executado como uma unidade de implantação local na V1.0, com o servidor como autoridade global de estado.

Clientes web, celular, processos de captura e adaptadores são participantes subordinados. Eles enviam comandos ou evidências e recebem snapshots/eventos; não confirmam estado global por conta própria.

A unidade de implantação pode conter tarefas assíncronas internas e filas limitadas, mas não depende de workers persistentes externos, n8n, OpenClaw, Ollama ou infraestrutura autônoma adicional.

## Regras normativas

```text
GLOBAL_STATE_AUTHORITY=SERVER
CLIENT_STATE=LOCAL_VIEW
EXTERNAL_VISUAL_SOURCE=EVIDENCE_ONLY
MODULE_BOUNDARIES=INTERNAL_PORTS_AND_CONTRACTS
V1_DEPLOYMENT_TOPOLOGY=LOCAL_MODULAR_MONOLITH
BACKGROUND_WORK=BOUNDED_AND_SERVER_OWNED
STATE_MUTATION=DOMAIN_COMMAND_REQUIRED
UNKNOWN_STATE=CAPABILITY_REDUCTION
```

Toda mudança global passa por comando validado no servidor. Cada comando recebe identidade, ator, versão esperada, `trace_id` e resultado explícito.

## Alternativas consideradas

### Cliente como autoridade compartilhada

Rejeitada por permitir divergência entre celular, dashboard, processo de captura e servidor.

### Microserviços desde a V1.0

Rejeitada por elevar custo operacional, concorrência, observabilidade e recovery sem necessidade comprovada no hardware e no escopo atuais.

### Aplicação desktop monolítica sem fronteiras internas

Rejeitada porque preservaria acoplamento do legado e dificultaria testes, rastreabilidade e futura separação de processos.

## Consequências

### Positivas

- estado global reconstruível;
- implantação local simples e gratuita;
- fronteiras preparadas para futura extração de serviços;
- menor risco de concorrência distribuída;
- celular funciona como painel operacional, não como autoridade oculta.

### Negativas e custos

- o servidor é ponto crítico e exige backup, health checks e recovery;
- tarefas lentas precisam ser isoladas internamente para não bloquear o loop principal;
- escalabilidade horizontal não é objetivo da V1.0.

## Segurança, recovery e falha segura

```text
SERVER_UNAVAILABLE=NO_NEW_GLOBAL_MUTATION
CLIENT_DISCONNECTED=LOCAL_VIEW_STALE
RESTART=RECONSTRUCT_FROM_PERSISTED_AUTHORITY
PRE_RESTART_COMMAND_DISPATCHABILITY=INVALIDATED
SPLIT_BRAIN=BLOCKED_BY_SINGLE_AUTHORITY
```

O restart cria nova identidade de processo. Comandos anteriores não retornam automaticamente ao estado despachável.

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-01
SECONDARY_DOMAINS=DOM-03|DOM-05|DOM-16
HANDOFFS=H-01..H-12
REQUIREMENTS=PTM-V25-018|V25-SRV-001..004|V25-DOC-001|PTM-V27-032
```

Fontes: catálogo de ADRs, mapa unificado, consolidação cruzada e índice individual `218/218`.

## Critérios de aceitação

```text
SINGLE_GLOBAL_AUTHORITY_DEFINED=PASS
CLIENT_AUTHORITY_LIMIT_DEFINED=PASS
LOCAL_DEPLOYMENT_BOUNDARY_DEFINED=PASS
RESTART_IDENTITY_POLICY_DEFINED=PASS
EXTERNAL_WORKER_DEPENDENCY=NO
```

## Fora de escopo

- framework de servidor;
- configuração de systemd;
- código de deploy;
- alta disponibilidade distribuída;
- implementação de qualquer adaptador.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.