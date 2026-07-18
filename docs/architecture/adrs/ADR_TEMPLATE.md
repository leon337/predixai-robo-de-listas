# ADR-NNNN — TÍTULO

## Controle

```text
ADR_ID=ADR-NNNN
CANDIDATE_ID=ADR-CAND-NNN
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
DECISION_SCOPE=ARCHITECTURE_ONLY
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

Descrever o problema arquitetural, as autoridades envolvidas, as restrições vigentes e o motivo pelo qual uma decisão explícita é necessária.

## Decisão

Registrar uma decisão única, objetiva e verificável. Separar arquitetura, contrato e implementação.

## Regras normativas

```text
REGRA_1=...
REGRA_2=...
```

## Alternativas consideradas

### Alternativa A — nome

Motivo da rejeição ou da não adoção como padrão.

### Alternativa B — nome

Motivo da rejeição ou da não adoção como padrão.

## Consequências

### Positivas

- consequência verificável.

### Negativas e custos

- custo, limitação ou complexidade introduzida.

## Segurança, recovery e falha segura

Definir comportamento em erro, restart, desconexão, timeout, dado desconhecido e tentativa de bypass.

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-XX
SECONDARY_DOMAINS=DOM-YY
HANDOFFS=H-XX
REQUIREMENTS=<IDs ou grupos aprovados>
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
```

## Critérios de aceitação

```text
ACCEPTANCE_1=PASS|FAIL
ACCEPTANCE_2=PASS|FAIL
```

## Fora de escopo

- código;
- escolha não necessária para a decisão;
- ativação de runtime;
- efeito financeiro;
- segredo ou credencial de produção.

## Estado da decisão

Este ADR permanece `PROPOSED_FOR_REVIEW` até revisão crítica independente, autorização humana de merge e confirmação pós-merge.