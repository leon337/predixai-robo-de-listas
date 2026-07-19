# POLÍTICA DE CONTROLE DE MUDANÇAS — ARQUITETURA V1.0

## LEA-38 — PredixAI Robô de Listas

## 1. Finalidade

Definir como a Arquitetura V1.0 poderá ser corrigida, estendida, substituída ou reaberta após o congelamento, impedindo alteração silenciosa da baseline e preservando rastreabilidade entre GitHub, Linear, ADRs, requisitos e estado oficial.

## 2. Princípio central

```text
FROZEN_BASELINE=IMMUTABLE_REFERENCE
MAIN_CAN_EVOLVE=YES_BY_FORMAL_CHANGE
SILENT_NORMATIVE_CHANGE=PROHIBITED
HISTORY_REWRITE=PROHIBITED
IMPLEMENTATION_DEVIATION_WITHOUT_REVIEW=PROHIBITED
```

O commit da baseline continua sendo a referência da Arquitetura V1.0 mesmo quando a `main` recebe documentação ou implementação posterior.

## 3. Classes de mudança

| Classe | Descrição | Efeito na versão arquitetural | ADR | Revisão independente |
|---|---|---|---|---|
| `EDITORIAL` | ortografia, links, formatação e clareza sem mudança semântica | preserva V1.0 | não, salvo dúvida | validação proporcional |
| `CLARIFICATION` | explicita regra já aprovada sem alterar obrigação ou fronteira | V1.0.x documental | conforme impacto | obrigatória quando normativa |
| `COMPATIBLE_EXTENSION` | adiciona capacidade sem quebrar invariantes e contratos existentes | V1.x | obrigatório quando houver decisão | obrigatória |
| `BREAKING_CHANGE` | altera autoridade, fronteira, contrato, requisito ou segurança | V2.0 ou nova baseline maior | obrigatório | Boss Gate completo |
| `SECURITY_CONTAINMENT` | bloqueio emergencial que reduz capacidade para conter risco | preserva ou inicia revisão de versão | registro de emergência e ADR posterior | revisão acelerada, nunca dispensada |
| `DEPRECATION_OR_SUPERSESSION` | substitui decisão ou artefato congelado | conforme impacto | ADR com `SUPERSEDED` ou `DEPRECATED` | obrigatória |

## 4. Solicitação formal de mudança

Toda mudança normativa deve registrar:

```text
CHANGE_ID
REQUESTING_ISSUE
CURRENT_BASELINE_COMMIT
CHANGE_CLASS
MOTIVATION
AFFECTED_REQUIREMENT_IDS
AFFECTED_DOMAINS
AFFECTED_HANDOFFS
AFFECTED_ADRS
SECURITY_IMPACT
IMPLEMENTATION_IMPACT
COMPATIBILITY_IMPACT
TEST_EVIDENCE_REQUIRED
ROLLBACK_OR_CONTAINMENT
REVIEW_ISSUE
PULL_REQUEST
POST_MERGE_CONFIRMATION
```

## 5. Fluxo obrigatório

```text
CHANGE_REQUEST
→ IMPACT_ANALYSIS
→ ADR_WHEN_REQUIRED
→ BUILDER_ARTIFACT
→ BUILDER_SELF_REVIEW
→ INDEPENDENT_CRITICAL_REVIEW
→ REMEDIATION_AND_RETEST_IF_NEEDED
→ HUMAN_MERGE_AUTHORIZATION
→ MERGE
→ POST_MERGE_CONFIRMATION
→ NEW_BASELINE_OR_DOCUMENTED_OVERLAY
```

## 6. Regras de implementação

A implementação pode detalhar estrutura física, bibliotecas, schema, migrations e testes apenas em missão autorizada. Ela deve permanecer dentro da baseline congelada.

```text
IMPLEMENTATION_DETAIL_WITHIN_FROZEN_BOUNDARY=ALLOWED_WHEN_AUTHORIZED
IMPLEMENTATION_CHANGES_ARCHITECTURAL_CONTRACT=CHANGE_REQUEST_REQUIRED
TEST_FAILURE_REVEALS_ARCHITECTURE_DEFECT=REOPEN_REVIEW_REQUIRED
CONVENIENCE_BYPASS_OF_HANDOFF_OR_AUTHORITY=PROHIBITED
```

## 7. Reabertura da arquitetura

A Arquitetura V1.0 deve ser reaberta quando ocorrer qualquer condição abaixo:

- conflito normativo confirmado;
- vulnerabilidade ou risco crítico incompatível com a baseline;
- requisito obrigatório não coberto;
- impossibilidade técnica demonstrada por evidência reproduzível;
- mudança comercial, legal ou regulatória que altere o modelo;
- decisão de produto que modifique fronteiras, autoridade ou Modo B;
- alteração de um dos 16 domínios, 12 handoffs ou 18 ADRs aceitos.

```text
REOPENING_REQUIRES_EXPLICIT_MISSION=YES
CURRENT_FROZEN_BASELINE_REMAINS_HISTORICAL=YES
NEW_BASELINE_REQUIRES_REVIEW_AND_CONFIRMATION=YES
```

## 8. Segurança e Modo LIVE

Nenhuma mudança documental, ADR ou versão arma automaticamente o Modo B.

```text
ARCHITECTURE_CHANGE!=LIVE_AUTHORIZATION
ADR_ACCEPTED!=LIVE_SESSION_ARMED
IMPLEMENTATION_COMPLETE!=REAL_FINANCIAL_EFFECT_AUTHORIZED
MODE_B_DEFAULT=DISABLED
```

## 9. Rollback

- mudança não integrada: fechar o PR;
- mudança integrada, mas incorreta: nova PR corretiva e registro de incidente documental;
- risco crítico: reduzir capacidade, desarmar ações e preservar evidências;
- nunca executar force-push ou reescrever a baseline oficial.

## 10. Gate desta política

```text
CHANGE_CLASSES_DEFINED=PASS_BUILDER
MANDATORY_FIELDS_DEFINED=PASS_BUILDER
FORMAL_FLOW_DEFINED=PASS_BUILDER
REOPENING_RULES_DEFINED=PASS_BUILDER
IMPLEMENTATION_BOUNDARY_PRESERVED=PASS_BUILDER
LIVE_BOUNDARY_PRESERVED=PASS_BUILDER
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
```