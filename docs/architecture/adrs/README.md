# ADRs — PredixAI Robô de Listas

## Estado da missão LEA-26

```text
ADR_SET=P0_ARCHITECTURE_V1
ADR_COUNT=12/12
ADR_STATUS=PROPOSED_FOR_REVIEW
BUILDER_ISSUE=LEA-26
REVIEW_ISSUE=LEA-27
TRANSITION_ID=LEA-26-T01
IMPLEMENTATION_AUTHORIZED=NO
MERGE_AUTHORIZED=NO
DOCUMENT_MASTER_START_AUTHORIZED=NO
```

## Índice

| ADR | Decisão | Candidato | Domínios primários | Estado |
|---|---|---|---|---|
| [ADR-0001](ADR-0001-SERVIDOR-E-AUTORIDADE-DE-ESTADO.md) | servidor e autoridade global | ADR-CAND-001 | DOM-01 | proposto |
| [ADR-0002](ADR-0002-PERSISTENCIA-E-ESCRITOR-UNICO.md) | SQLite V1 e escritor único | ADR-CAND-002 | DOM-03 | proposto |
| [ADR-0003](ADR-0003-CONTRATOS-REST-EVENTOS-E-VERSIONAMENTO.md) | REST JSON, SSE e versionamento | ADR-CAND-004 | DOM-01, DOM-03 | proposto |
| [ADR-0004](ADR-0004-IDENTIDADE-PAREAMENTO-E-CLIENTES.md) | identidade e pareamento local | ADR-CAND-005 | DOM-05 | proposto |
| [ADR-0005](ADR-0005-PERFIS-ROIS-E-ALVO-LOGICO.md) | perfis, ROIs e alvo lógico | ADR-CAND-006 | DOM-06 | proposto |
| [ADR-0006](ADR-0006-MOTORES-A-H-E-ENVELOPE-DE-ANALISE.md) | motores A–H determinísticos | ADR-CAND-008 | DOM-11 | proposto |
| [ADR-0007](ADR-0007-ESTRATEGIAS-E-LIFECYCLE-DE-SINAIS.md) | estratégias e lifecycle de sinais | ADR-CAND-009 | DOM-12 | proposto |
| [ADR-0008](ADR-0008-MAQUINA-DE-ESTADOS-DE-COMANDO-E-EXECUCAO.md) | FSM de comando e execução | ADR-CAND-010 | DOM-13, DOM-15 | proposto |
| [ADR-0009](ADR-0009-ADAPTADORES-E-SEPARACAO-DOS-MODOS-A-B.md) | adaptadores e Modos A/B | ADR-CAND-011 | DOM-14 | proposto |
| [ADR-0010](ADR-0010-KILL-SWITCH-DOMINANTE.md) | kill switch dominante | ADR-CAND-012 | DOM-16 | proposto |
| [ADR-0011](ADR-0011-RECIBO-E-RECONCILIACAO-MULTIDIMENSIONAL.md) | recibo e reconciliação | ADR-CAND-014 | DOM-15 | proposto |
| [ADR-0012](ADR-0012-OBSERVABILIDADE-AUDITORIA-E-REDACTION.md) | observabilidade e auditoria | ADR-CAND-015 | DOM-16 | proposto |

## Ordem lógica de leitura

```text
ADR-0001 autoridade global
  ├─ ADR-0002 persistência
  ├─ ADR-0003 contratos
  ├─ ADR-0004 identidade
  ├─ ADR-0008 estados
  ├─ ADR-0010 kill switch
  └─ ADR-0012 auditoria

ADR-0005 perfil e alvo ──→ ADR-0009 adaptadores
ADR-0006 análise ──→ ADR-0007 sinais ──→ ADR-0008 estados
ADR-0008 + ADR-0009 + ADR-0010 ──→ ADR-0011 reconciliação
ADR-0011 ──→ ADR-0012 auditoria
```

## Invariantes do conjunto

```text
SERVER_STATE=GLOBAL_AUTHORITY
CLIENT_STATE=LOCAL_VIEW
SINGLE_WRITE_BOUNDARY=SERVER
SIGNAL!=COMMAND
COMMAND!=GRANT
GRANT!=ATTEMPT
ATTEMPT!=CONFIRMED_EFFECT
COORDINATE!=TARGET_AUTHORIZATION
ADAPTER_RECEIPT!=GLOBAL_TRUTH
MODE_A=AUTHORIZED_BY_EXPLICIT_MISSION_AND_TARGET
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
LIVE_WITHOUT_ALL_GATES=BLOCKED
RESTART=NO_AUTOMATIC_REDISPATCH_OR_REARM
UNKNOWN_EFFECT=CORRELATED_ACTION_BLOCK
KILL_SWITCH=DOMINANT
```

## Autoridade e precedência

Os ADRs formalizam decisões derivadas da consolidação aprovada. Enquanto estiverem `PROPOSED_FOR_REVIEW`, não substituem as fontes normativas já aprovadas quando houver divergência.

Após revisão independente, autorização humana, merge e confirmação pós-merge, os ADRs aprovados passam a orientar o Documento Mestre.

## Fontes

- `docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
- `docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
- `docs/architecture/MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
- `docs/architecture/APENDICE_INDICE_INDIVIDUAL_218_REQUISITOS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`;
- `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`.

## Próximo gate

```text
A7_INDEPENDENT_CRITICAL_REVIEW=LEA-27
ADR_P0_CRITICAL_REVIEW=PASS_REQUIRED
MERGE_AUTHORIZED=NO
```