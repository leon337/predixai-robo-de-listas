# ADR-NNNN — TÍTULO

## Controle

```text
ADR_ID=<ADR-NNNN>
CANDIDATE_ID=<ADR-CAND-NNN|N/A>
STATUS=<PROPOSED_FOR_REVIEW|ACCEPTED|SUPERSEDED|DEPRECATED|REJECTED>
MISSION=<LEA-NN>
REVIEW_ISSUE=<LEA-NN|N/A>
DATE=<YYYY-MM-DD>
ACCEPTED_AT=<YYYY-MM-DD|N/A>
ACCEPTANCE_EVIDENCE=<caminho ou referência verificável|N/A>
PUBLICATION_EVIDENCE=<caminho ou referência verificável|N/A>
SUPERSEDES=<ADR IDs|NONE>
SUPERSEDED_BY=<ADR ID|NONE>
DECISION_SCOPE=ARCHITECTURE_ONLY
IMPLEMENTATION_AUTHORIZED=NO
```

## Lifecycle documental

```text
PROPOSED_FOR_REVIEW=decisão redigida, ainda dependente de revisão crítica e publicação
ACCEPTED=decisão aprovada, publicada e vigente como base arquitetural
SUPERSEDED=decisão substituída por ADR posterior identificado
DEPRECATED=decisão ainda histórica, mas desencorajada e programada para substituição
REJECTED=proposta recusada e não normativa
```

Transições devem ser registradas, justificadas e rastreáveis. `ACCEPTED` exige revisão crítica independente válida, autorização humana de integração quando aplicável e evidência de publicação. Mudança para `SUPERSEDED`, `DEPRECATED` ou `REJECTED` exige missão documental própria e referência explícita ao motivo ou ADR sucessor.

O status documental não autoriza código, runtime, SQL, migrations, cliques reais, Modo LIVE ou efeito financeiro.

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

Declarar o mesmo `STATUS` do bloco de controle, as evidências que justificam o estado e os limites preservados. Um ADR `ACCEPTED` é normativo para arquitetura, mas não concede autorização de implementação.