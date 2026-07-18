# ADR-0005 — Perfis versionados, ROIs e alvo lógico

## Controle

```text
ADR_ID=ADR-0005
CANDIDATE_ID=ADR-CAND-006
STATUS=PROPOSED_FOR_REVIEW
MISSION=LEA-26
REVIEW_ISSUE=LEA-27
DATE=2026-07-18
IMPLEMENTATION_AUTHORIZED=NO
```

## Contexto

Captura, OCR e ação controlada dependem da identidade da aplicação, monitor, escala, resolução, âncoras, ROIs e alvos. Coordenadas isoladas são frágeis e não podem representar autorização nem identidade de alvo.

## Decisão

Adotar **perfil visual versionado e imutável após aprovação**, identificado por `profile_id` e `profile_version`.

O perfil reúne identidade da aplicação, ambiente gráfico, monitor, resolução, escala, assinatura visual, âncoras, ROIs e catálogo de `target_logical_id`. Cada alvo lógico possui finalidade, tipo de ação permitido, geometria relativa ao perfil, tolerâncias e requisitos de compatibilidade.

Calibração produz uma nova versão de perfil. Mudança de aplicação, monitor, escala, assinatura ou âncora invalida compatibilidade até nova validação.

## Regras normativas

```text
PROFILE=VERSIONED_AND_IMMUTABLE_WHEN_APPROVED
TARGET_IDENTITY=TARGET_LOGICAL_ID
RAW_COORDINATE=NOT_IDENTITY
RAW_COORDINATE=NOT_AUTHORIZATION
GEOMETRY=PROFILE_SCOPED
ROI=PURPOSE_SCOPED
VISUAL_SIGNATURE=REQUIRED_FOR_COMPATIBILITY
PROFILE_CHANGE=NEW_VERSION
INCOMPATIBLE_PROFILE=OBSERVATION_AND_DISPATCH_BLOCKED
TARGET_ALLOWLIST=REQUIRED
```

Geometria deve preferir coordenadas normalizadas e relações com âncoras, mantendo coordenadas absolutas somente como resultado derivado da resolução do alvo.

## Alternativas consideradas

### Coordenadas globais fixas

Rejeitadas por quebrarem com resolução, escala, posição da janela e monitor.

### Detecção livre sem perfil

Rejeitada por permitir identidade ambígua e ação em alvo não autorizado.

### Perfil mutável no lugar

Rejeitado por destruir rastreabilidade entre evidência, análise e ação.

## Consequências

### Positivas

- calibração reproduzível;
- alvo independente de par X/Y isolado;
- mesma identidade usada por captura e adaptador;
- rollback para versão anterior aprovada;
- bloqueio seguro após mudança visual.

### Negativas e custos

- manutenção de versões e compatibilidade;
- necessidade de assinatura visual e testes por ambiente;
- perfis podem exigir recalibração após atualização da plataforma.

## Segurança, recovery e falha segura

```text
APPLICATION_IDENTITY_UNKNOWN=BLOCK
VISUAL_SIGNATURE_MISMATCH=BLOCK
ANCHOR_MISSING=BLOCK
TARGET_NOT_ALLOWLISTED=BLOCK
GEOMETRY_OUT_OF_BOUNDS=BLOCK
PROFILE_REVOKED=BLOCK
RESTART=PROFILE_RELOAD_AND_REVALIDATION
```

## Rastreabilidade

```text
PRIMARY_DOMAINS=DOM-06
SECONDARY_DOMAINS=DOM-07|DOM-08|DOM-09|DOM-14|DOM-16
HANDOFFS=H-02|H-03|H-04|H-09|H-10
REQUIREMENTS=PTM-V25-010|PTM-V25-011A..011D|PTM-V27-003|PTM-V27-008|PTM-V27-009|PTM-V27-021|V27-EXE-003|V27-EXE-004|V27-SAF-006
DEPENDS_ON=ADR-0001
```

## Critérios de aceitação

```text
PROFILE_VERSIONING=PASS
TARGET_LOGICAL_ID_DEFINED=PASS
COORDINATE_NOT_AUTHORITY=PASS
COMPATIBILITY_FAILURE_BLOCKS=PASS
CAPTURE_AND_ACTION_SHARE_PROFILE_IDENTITY=PASS
```

## Fora de escopo

- algoritmo de assinatura visual;
- formato físico de armazenamento;
- valores numéricos de tolerância;
- automação de calibração;
- adaptador LIVE.

## Estado da decisão

Permanece `PROPOSED_FOR_REVIEW`.