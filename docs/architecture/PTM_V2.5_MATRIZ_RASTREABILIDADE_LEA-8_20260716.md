# PTM V2.5 — MATRIZ DE RASTREABILIDADE DA RECONCILIAÇÃO

## LEA-8 — Complemento do builder draft

## 1. Controle e herança

```text
DOCUMENT_STATUS=BUILDER_TRACEABILITY_COMPLETE
MISSION=LEA-8
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=7f7434ffd9f9424ab929ad6afe7d1fc76e1d67c9
LEGACY_AUDIT_SOURCE=main@0e2d7e98d863769be32a8bcb8b93684a61674aa3
WORKING_BRANCH=leonpcsn/lea-8-reconciliar-e-revisar-ptm-v25
PARENT_DOCUMENT=docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
APPLICATION_EXECUTED=NO
```

Cada linha herda:

- fonte factual: repositório oficial e Anexo A aprovado;
- branch/commit factual: `main@0e2d7e98d863769be32a8bcb8b93684a61674aa3`;
- versão do legado: `V2.4.3-R1`;
- milestone: `V2.5`;
- implementação: não autorizada;
- status final: depende de revisão crítica independente.

Semântica:

```text
NOVO=sem mecanismo equivalente confirmado no legado
REUTILIZAR=preservar comportamento/contrato comprovado
ADAPTAR=preservar comportamento com nova fronteira ou contrato
SUBSTITUIR=mecanismo legado não é base arquitetural futura
DESCONTINUAR=não pertence ao baseline V2.5
```

## 2. Registro estrutural

| ID | Domínio | Fonte/caminho factual | Classificação | Certeza | Risco | Decisão do builder | Status |
|---|---|---|---|---|---|---|---|
| PTM-V25-001 | server/persistence | `app/main.py`; JSON schema 4 | ADAPTAR dados; SUBSTITUIR autoridade JSON | Alta | Alto | servidor e persistência controlada tornam-se autoridade; JSON é somente migração | RECONCILIADO_BUILDER |
| PTM-V25-002 | clients | `app/main.py` monolítico | SUBSTITUIR acoplamento | Alta | Alto | clientes não acessam persistência diretamente | RECONCILIADO_BUILDER |
| PTM-V25-003 | persistence | ausência de banco no inventário; PTM preliminar | NOVO | Alta para ausência estática | Alto | fronteira de escritor único; schema físico progressivo | RECONCILIADO_BUILDER |
| PTM-V25-004 | runtime | `runtime_guard.py`; `bootstrap_v23_entry.py`; bootstraps | ADAPTAR guardas; SUBSTITUIR patch chain | Alta | Alto | lifecycle explícito, seguro e testável | RECONCILIADO_BUILDER |
| PTM-V25-005 | contracts | ausência de REST/WebSocket no inventário | NOVO | Alta | Médio | contratos externos versionados e validados | RECONCILIADO_BUILDER |
| PTM-V25-006 | messaging | ausência de outbox no inventário | NOVO | Alta | Médio | existência somente com evento crítico, produtor, consumidor e teste | RECONCILIADO_BUILDER |
| PTM-V25-007 | lists | `bootstrap_v22.py`; JSON `lists` no topo | ADAPTAR | Alta | Médio | listas permanecem independentes de análise e execução | RECONCILIADO_BUILDER |
| PTM-V25-008 | devices/android | ausência de Android no legado | NOVO | Alta | Alto | pareamento local, revogável e auditável | RECONCILIADO_BUILDER |
| PTM-V25-009 | devices/android | ausência de reconexão móvel no legado | NOVO | Alta | Médio | sequence quando possível; snapshot fallback | RECONCILIADO_BUILDER |
| PTM-V25-010 | profiles | `CoordinateProfile`; campos de perfil no schema 4 | ADAPTAR | Alta | Médio | separar perfis de ambiente, aplicação e monitor | RECONCILIADO_BUILDER |
| PTM-V25-011A | calibration | `app/main.py::_test_both_coordinates`; telas de perfil | ADAPTAR geometria; DESCONTINUAR clique | Alta | Crítico | calibração segura sem movimento/clique; aprovação versionada | RECONCILIADO_BUILDER |
| PTM-V25-011B | calibration | resolução, escala e coordenadas no schema 4 | ADAPTAR | Alta | Médio | ROIs versionadas e validadas sem autorizar observação | RECONCILIADO_BUILDER |
| PTM-V25-011C | calibration | `coordinates.LARANJA/CINZA`; caminhos de clique | ADAPTAR geometria; DESCONTINUAR ação | Alta | Crítico | click targets são dados geométricos, nunca autorização | RECONCILIADO_BUILDER |
| PTM-V25-011D | calibration | nenhuma âncora/assinatura confirmada | NOVO | Alta para ausência estática | Médio | contratos versionados de âncora e assinatura | RECONCILIADO_BUILDER |
| PTM-V25-012 | platform | `runtime_guard.py`; `diagnostics_tools.py`; scripts Bash | ADAPTAR | Alta | Médio | isolar Linux/X11 em adaptadores | RECONCILIADO_BUILDER |
| PTM-V25-013 | platform | Windows não implementado no inventário | NOVO | Alta | Médio | foundation progressiva com testes próprios | RECONCILIADO_BUILDER |
| PTM-V25-014A | legacy | Anexo A, apêndices e artefato canônico | REUTILIZAR | Alta | Baixo | inventário aprovado é fonte factual obrigatória | SATISFEITO_PELA_AUDITORIA |
| PTM-V25-014B | migration | `config_safety.py`; backups JSON | ADAPTAR | Alta | Médio | backup íntegro e verificado antes da transformação | RECONCILIADO_BUILDER |
| PTM-V25-014C | migration | JSON schema 4; opcionalidade documentada | ADAPTAR fonte; SUBSTITUIR destino final | Alta | Alto | transformação determinística, validada e versionada | RECONCILIADO_BUILDER |
| PTM-V25-014D | migration | JSON, listas, sinais e histórico | ADAPTAR | Alta | Alto | contagens, hashes, aceitos e rejeitados reconciliados | RECONCILIADO_BUILDER |
| PTM-V25-014E | migration | `ConfigSafetyManager`; política conceitual | ADAPTAR | Alta | Alto | rollback/recovery preserva origem e impede continuidade insegura | RECONCILIADO_BUILDER |
| PTM-V25-015A | observability | `runtime_guard.configure_logging` | ADAPTAR | Alta | Médio | logs estruturados, retenção e redaction | RECONCILIADO_BUILDER |
| PTM-V25-015B | audit | logs; `session_history`; eventos textuais | ADAPTAR | Alta | Alto | separar auditoria de segurança, comando e diagnóstico | RECONCILIADO_BUILDER |
| PTM-V25-015C | metrics | nenhuma camada de métricas confirmada | NOVO | Alta | Médio | métricas mínimas apenas com produtor, consumidor e retenção | RECONCILIADO_BUILDER |
| PTM-V25-015D | diagnostics | `diagnostics_tools.py`; relatórios TXT | REUTILIZAR comportamento; ADAPTAR contrato | Alta | Baixo | diagnóstico exportável, seguro e redigido | RECONCILIADO_BUILDER |
| PTM-V25-015E | tracing | ausência de `trace_id`/`command_id` transversal | NOVO | Alta | Médio | correlação transversal obrigatória | RECONCILIADO_BUILDER |
| PTM-V25-016 | configuration | `config_safety.py`; JSON schema 4 | ADAPTAR; SUBSTITUIR autoridade JSON | Alta | Alto | configuração versionada, validada, segura e recuperável | RECONCILIADO_BUILDER |
| PTM-V25-017 | security/network | nenhum servidor de rede confirmado | NOVO | Alta | Alto | bind seguro, autenticação, pareamento, revogação e limites | RECONCILIADO_BUILDER |
| PTM-V25-018 | runtime/safety | legado não possui servidor; clique real está presente | NOVO com bloqueio legado | Alta | Crítico | `SAFE_IDLE` sem Android e sem elevação automática | RECONCILIADO_BUILDER |

## 3. Registro funcional

| ID | Domínio | Fonte/caminho factual | Classificação | Certeza | Risco | Decisão do builder | Status |
|---|---|---|---|---|---|---|---|
| V25-SRV-001 | server | `runtime_guard.py`; entrypoint protegido | ADAPTAR | Alta | Alto | inicialização segura e não executável | RECONCILIADO_BUILDER |
| V25-SRV-002 | server | lock/logging; encerramento da aplicação legada | ADAPTAR | Média/Alta | Médio | shutdown explícito sem corrupção | RECONCILIADO_BUILDER |
| V25-SRV-003 | server | ausência de Android; risco de clique legado | NOVO | Alta | Crítico | `SAFE_IDLE` independente de cliente | RECONCILIADO_BUILDER |
| V25-SRV-004 | server/contracts | ausência de REST/WebSocket | NOVO | Alta | Médio | contratos mínimos health/state/compatibility/bootstrap | RECONCILIADO_BUILDER |
| V25-CFG-001 | configuration | carga de JSON e defaults do legado | ADAPTAR | Alta | Alto | resolução determinística com defaults seguros | RECONCILIADO_BUILDER |
| V25-CFG-002 | configuration | opcionalidade do schema 4; `config_safety.py` | ADAPTAR | Alta | Alto | validação explícita e fail-closed | RECONCILIADO_BUILDER |
| V25-CFG-003 | configuration/security | `.gitignore`; diagnóstico exportável | ADAPTAR | Alta | Alto | redaction de segredos e dados sensíveis | RECONCILIADO_BUILDER |
| V25-CFG-004 | configuration | feature flags não confirmadas no legado | NOVO | Alta | Alto | dependências e safe defaults; execução real sempre desabilitada | RECONCILIADO_BUILDER |
| V25-DB-001 | persistence | banco ausente no inventário | NOVO | Alta | Alto | inicialização íntegra e progressiva | RECONCILIADO_BUILDER |
| V25-DB-002 | persistence | monólito grava JSON diretamente | SUBSTITUIR mecanismo | Alta | Alto | escritor único e fronteira de writes | RECONCILIADO_BUILDER |
| V25-DB-003 | persistence | migrations físicas ausentes e proibidas nesta missão | NOVO | Alta | Alto | política versionada e verificável; sem gerar migration agora | RECONCILIADO_BUILDER |
| V25-DB-004 | messaging | outbox ausente | NOVO | Alta | Médio | publicação externa somente após commit | RECONCILIADO_BUILDER |
| V25-DB-005 | recovery | `ConfigSafetyManager` e backups | ADAPTAR | Alta | Alto | backup/restore com integridade e teste autorizado | RECONCILIADO_BUILDER |
| V25-LIST-001 | lists | `ScheduleList`; `bootstrap_v22.py` | ADAPTAR | Alta | Médio | CRUD desacoplado de análise e executor | RECONCILIADO_BUILDER |
| V25-LIST-002 | lists | listas e sinais mutáveis no schema 4 | ADAPTAR | Alta | Médio | versões imutáveis após ativação/publicação | RECONCILIADO_BUILDER |
| V25-LIST-003 | lists | `Signal`; preflight; estados e horários | REUTILIZAR regras puras; ADAPTAR validação | Alta | Médio | reason codes e validação determinística | RECONCILIADO_BUILDER |
| V25-LIST-004 | lists/migration | JSON schema 4 | ADAPTAR | Alta | Alto | importar sem executar e relatar aceitos/rejeitados | RECONCILIADO_BUILDER |
| V25-LEG-001 | legacy | Auditoria Mestra e Anexo A | REUTILIZAR | Alta | Baixo | inventário físico concluído | SATISFEITO_PELA_AUDITORIA |
| V25-LEG-002 | legacy | versão, schema e artefatos auditados | ADAPTAR | Alta | Médio | manifesto de origem e opções | RECONCILIADO_BUILDER |
| V25-LEG-003 | legacy/recovery | backups e `config_safety.py` | ADAPTAR | Alta | Alto | backup verificado pré-transformação | RECONCILIADO_BUILDER |
| V25-LEG-004 | legacy/migration | schema 4 e regras de fallback | ADAPTAR | Alta | Alto | transformação determinística e idempotente | RECONCILIADO_BUILDER |
| V25-LEG-005 | legacy/migration | contagens/campos do Anexo A | ADAPTAR | Alta | Alto | reconciliação quantitativa e por hash | RECONCILIADO_BUILDER |
| V25-LEG-006 | legacy/recovery | recovery JSON existente; política futura | ADAPTAR | Alta | Alto | rollback/recovery impede startup normal em falha | RECONCILIADO_BUILDER |

## 4. Requisitos adicionais propostos

| ID | Domínio | Fonte/caminho factual | Classificação | Certeza | Risco | Decisão do builder | Status |
|---|---|---|---|---|---|---|---|
| V25-SEC-001 | safety | `app/main.py`; `bootstrap_v231.py`; `pynput` | DESCONTINUAR ação; preservar evidência | Alta | Crítico | bloquear e provar ausência de movimento/clique em R0–R2 | PROPOSTO_PARA_RC |
| V25-QA-001 | quality | `tests/`; nove workflows | ADAPTAR | Alta | Médio | gate agregado cobre toda suíte aplicável | PROPOSTO_PARA_RC |
| V25-QA-002 | quality/safety | ausência de E2E seguro de agenda | NOVO | Alta | Alto | adapter nulo/simulado e prova negativa de clique | PROPOSTO_PARA_RC |
| V25-DOC-001 | documentation | `README.md`; `VERSION`; `run.sh`; `CHANGELOG.md` | SUBSTITUIR README; ADAPTAR CHANGELOG | Alta | Alto | consistência de versão, entrypoint e instalação | PROPOSTO_PARA_RC |

## 5. Campos PTM herdados e pendentes

Todos os registros usam o seguinte contrato até a revisão crítica:

| Campo PTM | Valor/regra nesta etapa |
|---|---|
| `requirement_id` | ID único da linha |
| `requirement` | decisão descrita no documento pai |
| `source_point` | fonte/caminho desta matriz |
| `adr_ids` | `PENDING_ADR_CONSOLIDATION`; ADR não substitui requisito |
| `milestone` | `V2.5` |
| `criticality` | derivada do risco: Crítico/Alto/Médio/Baixo |
| `owner_domain` | coluna Domínio |
| `implementation_component` | `NOT_AUTHORIZED`; será definido no Documento Mestre |
| `REST_contract` | `N/A` ou `PRELIMINARY` conforme requisito; contrato final pendente |
| `WebSocket_event` | `N/A` ou `PRELIMINARY`; evento final pendente |
| `database_entities` | catálogo lógico somente; existência física progressiva |
| `migration_group` | somente requisitos `014*`, `V25-LEG-*` e correlatos |
| `producer`/`consumer` | obrigatórios antes de existência física; pendentes de Documento Mestre |
| `feature_flag` | safe default obrigatório quando aplicável |
| `safe_default` | `SAFE_IDLE`, bloqueado ou recurso desabilitado |
| `privacy_classification` | obrigatório antes da implementação |
| `retention_policy` | obrigatória para histórico e artefatos |
| `test_ids` | pendentes de plano de implementação; tipo de teste já definido |
| `acceptance_criteria` | documento pai, seções 6–12 |
| `failure_conditions` | fail-closed; falhas críticas bloqueiam avanço |
| `evidence_required` | teste/relatório/artefato versionado |
| `gate` | documento pai e baseline preliminar |
| `dependencies` | Auditoria Mestra PASS; requisitos relacionados |
| `status` | `RECONCILIADO_BUILDER`, `SATISFEITO_PELA_AUDITORIA` ou `PROPOSTO_PARA_RC` |
| `gaps` | campos finais de contrato, entidade física e teste dependem das etapas posteriores |

## 6. Validação da matriz

```text
STRUCTURAL_ID_COUNT=29
FUNCTIONAL_ID_COUNT=23
PROPOSED_ADDITIONAL_ID_COUNT=4
TOTAL_UNIQUE_ID_COUNT=56
DUPLICATE_REQUIREMENT_IDS=0
SOURCE_PATH_PRESENT_PER_ROW=PASS
CLASSIFICATION_PRESENT_PER_ROW=PASS
CERTAINTY_PRESENT_PER_ROW=PASS
RISK_PRESENT_PER_ROW=PASS
DECISION_PRESENT_PER_ROW=PASS
STATUS_PRESENT_PER_ROW=PASS
LEGACY_AND_FUTURE_SEPARATED=PASS
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
PTM_V2_5_CRITICAL_REVIEW=PENDING
```

A matriz não torna os quatro requisitos adicionais definitivos. Eles devem ser aceitos, ajustados ou rejeitados pela revisão crítica independente.