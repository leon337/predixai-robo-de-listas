# ADR-0014 — Retenção mínima de frames, recortes e evidências visuais

## Controle

```text
ADR_ID=ADR-0014
CANDIDATE_ID=ADR-CAND-007
PRIORITY=P1
STATUS=ACCEPTED
MISSION=LEA-30
REVIEW_ISSUE=LEA-31
DATE=2026-07-18
ACCEPTED_AT=2026-07-18
ACCEPTANCE_EVIDENCE=docs/history/reviews/REVISAO_CRITICA_RETESTE_02_ADRS_P1_P2_LEA-31_20260718.md
PUBLICATION_EVIDENCE=docs/history/receipts/CONFIRMACAO_FINAL_LEA-30_PR-50_20260718.md
IMPLEMENTATION_AUTHORIZED=NO
DEPENDS_ON=ADR-0005|ADR-0012
MUST_ALIGN_WITH=ADR-0006|ADR-0017|ADR-0018
```

## Contexto

Frames e recortes podem conter dados visuais sensíveis, ocupar armazenamento limitado e aumentar a superfície de exposição. Ao mesmo tempo, hashes, proveniência e evidências sanitizadas são necessários para diagnóstico, replay, auditoria e explicação dos sinais.

## Decisão

Adotar uma política **reference-first e data-minimizing**. A referência, hash, origem, sequence, perfil, ROI, versões e resultado de validação podem sobreviver ao artefato bruto; a imagem bruta é efêmera por padrão.

Classes de retenção:

```text
EPHEMERAL_RAW=memória ou armazenamento temporário estritamente necessário ao pipeline
DIAGNOSTIC_REDACTED=artefato sanitizado criado por evento ou autorização explícita
REPLAY_FIXTURE_SANITIZED=fixture controlada, versionada e sem dado de produção
AUDIT_DERIVATIVE=hash, metadados, métricas e reason codes sem imagem bruta
```

A política de retenção é versionada e vinculada à sessão, perfil, ROI e finalidade. Nenhuma classe define duração numérica definitiva sem benchmark, capacidade e avaliação de privacidade documentados.

## Regras normativas

```text
RAW_FRAME_DEFAULT_RETENTION=EPHEMERAL
RAW_FRAME_INDEFINITE_RETENTION=PROHIBITED
REFERENCE_AND_HASH_MAY_OUTLIVE_ARTIFACT=YES
PERSIST_RAW_REQUIRES=EXPLICIT_POLICY_AND_PURPOSE
REDACTION_BEFORE_PERSISTENCE=REQUIRED
RETENTION_POLICY_VERSION=REQUIRED
ARTIFACT_PROVENANCE=REQUIRED
ROI_CROP_INHERITS_FRAME_IDENTITY=YES
UNKNOWN_SENSITIVITY=DO_NOT_PERSIST_RAW
DELETION_EVENT=AUDITED_WITHOUT_RETAINING_DELETED_CONTENT
ACCESS_TO_RETAINED_ARTIFACT=AUDITED_AND_LEAST_PRIVILEGE
EXPORT=SANITIZED_AND_EXPLICIT
GIT_STORAGE_OF_RAW_FRAME=PROHIBITED
```

Metadados mínimos sobreviventes:

```text
frame_reference_id
frame_hash
source_identity_hash
observation_session_id
profile_id|profile_version
roi_id|roi_version
captured_at_utc
sequence
retention_policy_version
validation_status
artifact_state=PRESENT|REDACTED|EXPIRED|DELETED|NEVER_PERSISTED
```

## Alternativas consideradas

### Persistir todos os frames

Rejeitada por custo, privacidade, risco de versionamento e ausência de necessidade comprovada.

### Não preservar nenhuma evidência

Rejeitada porque impede replay, diagnóstico, explicação e auditoria de divergências.

### Usar apenas nomes de arquivos sem hash ou proveniência

Rejeitada porque não prova identidade, integridade ou vínculo com sessão e ROI.

## Consequências

### Positivas

- minimização de dados sensíveis;
- menor consumo de disco;
- rastreabilidade mesmo após expiração do artefato;
- fixtures de replay controladas e reproduzíveis;
- política ajustável por finalidade sem alterar o contrato base.

### Negativas e custos

- diagnóstico tardio pode não ter imagem bruta;
- redaction exige pipeline próprio;
- retenção e deleção precisam de auditoria;
- criação de fixtures exige curadoria.

## Segurança, recovery e falha segura

```text
REDACTION_FAILURE=DO_NOT_PERSIST
POLICY_UNKNOWN=EPHEMERAL_ONLY
ARTIFACT_HASH_MISMATCH=REJECT
SOURCE_IDENTITY_MISMATCH=REJECT
DISK_PRESSURE=REDUCE_RETENTION_AND_PRESERVE_METADATA
UNAUTHORIZED_ACCESS=BLOCK_AND_AUDIT
DELETION_FAILURE=ALERT_AND_RETRY_WITHOUT_EXPANDING_ACCESS
SECRET_OR_CREDENTIAL_DETECTED=BLOCK_PERSISTENCE
```

## Rastreabilidade

Os 26 requisitos diferidos para `ADR-CAND-007` atravessam sessão de observação, captura, validação e mapping. Eles são distintos dos requisitos complementares de replay, segurança e auditoria já decididos pelos ADRs P0.

```text
PRIMARY_DOMAINS=DOM-08
SECONDARY_DOMAINS=DOM-06|DOM-07|DOM-09|DOM-10|DOM-16
HANDOFFS=H-03|H-04|H-05
DEFERRED_REQUIREMENTS_FROM_P0_APPENDIX=PTM-V26-002..008|V26-OBS-001..004|V26-CAP-001..004|V26-VAL-001..006|V26-MAP-001..005
DEFERRED_REQUIREMENT_COUNT=26
COMPLEMENTARY_REQUIREMENTS=PTM-V26-024..026|V26-RPL-001..003|V26-SEC-001..003
SOURCE_CATALOG=docs/architecture/CATALOGO_DECISOES_CANDIDATAS_ADR_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
SOURCE_MAP=docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md
TRACEABILITY_APPENDIX=docs/architecture/adrs/APENDICE_RASTREABILIDADE_INDIVIDUAL_ADRS_P1_P2_LEA-30_20260718.md
```

## Critérios de aceitação

```text
REFERENCE_FIRST_POLICY=PASS_BUILDER
RAW_EPHEMERAL_DEFAULT=PASS_BUILDER
REDACTION_BEFORE_PERSISTENCE=PASS_BUILDER
PROVENANCE_SURVIVES_ARTIFACT=PASS_BUILDER
UNKNOWN_SENSITIVITY_FAIL_CLOSED=PASS_BUILDER
REPLAY_FIXTURE_SANITIZATION=PASS_BUILDER
DEFERRED_REQUIREMENTS_RECONCILED=26/26
INDIVIDUAL_TRACEABILITY=PASS_BUILDER_REMEDIATED
NUMERIC_RETENTION_VALUES_DEFINED=NO
RUNTIME_CAPTURE_EXECUTED=NO
```

## Fora de escopo

- duração numérica final;
- implementação de captura;
- armazenamento físico;
- imagens reais;
- política jurídica definitiva de produção.

## Estado da decisão

Status `ACCEPTED`. A decisão foi aprovada pela revisão crítica independente `LEA-31` no Reteste 02 e publicada com confirmação final da LEA-30. A aceitação não autoriza captura runtime nem retenção de imagens reais.