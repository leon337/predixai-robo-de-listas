# PTM V2.5 — RECONCILIAÇÃO FACTUAL COM O LEGADO

## LEA-8 — Builder Draft para revisão crítica independente

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_DRAFT_RECONCILED
MISSION=LEA-8
LINEAR_ISSUE=LEA-8
REPOSITORY=leon337/predixai-robo-de-listas
BASE_BRANCH=main
BASE_MAIN_SHA=7f7434ffd9f9424ab929ad6afe7d1fc76e1d67c9
LEGACY_VERSION=V2.4.3-R1
LEGACY_AUDIT_SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
WORKING_BRANCH=leonpcsn/lea-8-reconciliar-e-revisar-ptm-v25
CODE_CHANGED=NO
APPLICATION_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
IMPLEMENTATION_AUTHORIZED=NO
PTM_V2_5_CRITICAL_REVIEW=PENDING
```

Este documento reconcilia a arquitetura preliminar da PTM V2.5 com o inventário factual aprovado do legado. Ele é uma especificação arquitetural preliminar do builder, não uma autorização de implementação e não substitui a revisão crítica independente.

## 2. Fontes de autoridade

1. `PROJECT_RUNTIME_STATE.yaml`;
2. `PROJECT_STATE.md`;
3. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
4. `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md`;
5. Apêndices 01–04 do Anexo A;
6. `docs/audits/ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md`;
7. `docs/history/reviews/REVISAO_CRITICA_AUDITORIA_MESTRA_PTP-GOV.6_20260716.md`;
8. `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md`;
9. `docs/history/ptp/HANDOFF_PTP-GOV.6-RC_PARA_PTM_V2.5_20260716.md`;
10. issue `LEA-8` no Linear.

## 3. Método

Para cada requisito preliminar foram confrontados:

- comportamento factual existente;
- mecanismo atual do legado;
- classificação `REUTILIZAR`, `ADAPTAR`, `SUBSTITUIR` ou `DESCONTINUAR`;
- destino na V2.5;
- risco;
- critério de aceite arquitetural;
- evidência exigida em futura implementação autorizada.

Princípio aplicado:

```text
PRESERVAR_COMPORTAMENTO_UTIL
!=
PRESERVAR_MECANISMO_LEGADO
```

A cadeia de monkey patches, o JSON como fonte final de verdade e qualquer clique real não são transportados como mecanismos da V2.5.

## 4. Limites da V2.5 reconciliada

```text
V2_5_SCOPE=FOUNDATION_AND_SAFE_MIGRATION_DESIGN
VALIDATION_LEVELS_ALLOWED=R0|R1|R2
POINTER_MOVEMENT_ALLOWED=NO
REAL_CLICK_ALLOWED=NO
REAL_ORDER_ALLOWED=NO
SERVER_IMPLEMENTATION_AUTHORIZED=NO
DATABASE_IMPLEMENTATION_AUTHORIZED=NO
ANDROID_IMPLEMENTATION_AUTHORIZED=NO
```

A V2.5 cobre fundação, contratos, configuração, persistência conceitual, listas independentes, migração controlada do legado, perfis, calibração geométrica, Android Foundation, compatibilidade progressiva, observabilidade e recovery básico. Observação analítica pertence à V2.6. Execução controlada pertence à V2.7 e depende de gates próprios.

## 5. Resultado executivo da reconciliação

```text
STRUCTURAL_BASELINE_REQUIREMENTS=29
FUNCTIONAL_BASELINE_REQUIREMENTS=23
TOTAL_BASELINE_REQUIREMENTS=52
STRUCTURAL_REQUIREMENTS_RECONCILED=29
FUNCTIONAL_REQUIREMENTS_RECONCILED=23
ADDITIONAL_GAP_REQUIREMENTS_PROPOSED=4
REAL_CLICK_EXCLUDED_FROM_V2_5=PASS
JSON_FINAL_SOURCE_OF_TRUTH_REJECTED=PASS
JSON_MIGRATION_SOURCE_PRESERVED=PASS
PATCH_CHAIN_REPLACEMENT_REQUIRED=PASS
LEGACY_BEHAVIOR_PRESERVATION_REQUIRED=PASS
```

## 6. Requisitos estruturais reconciliados

| ID | Decisão reconciliada | Evidência factual e tratamento | Gate arquitetural |
|---|---|---|---|
| PTM-V25-001 | CONFIRMAR COM AJUSTE | O legado usa JSON local como fonte global. Preservar os dados como fonte de migração e substituir a autoridade persistente por servidor + persistência controlada. | `SERVER_SOURCE_OF_TRUTH` |
| PTM-V25-002 | CONFIRMAR | O monólito atual mistura UI, domínio e persistência. Clientes futuros não acessam diretamente a persistência. | `NO_CLIENT_DIRECT_DATABASE_ACCESS` |
| PTM-V25-003 | CONFIRMAR COMO NOVO | Não há banco confirmado no legado. A V2.5 exige fronteira de escrita única; schema físico permanece progressivo. | `SQLITE_SINGLE_WRITER` |
| PTM-V25-004 | ADAPTAR E SUBSTITUIR | Reutilizar conceitos de lock, logging e diagnóstico de `runtime_guard.py`; substituir bootstrap ordenado e monkey patching por lifecycle explícito. | `SERVER_LIFECYCLE` |
| PTM-V25-005 | CONFIRMAR COMO NOVO | REST/WebSocket não existem no legado auditado. Contratos devem ser versionados, validados e introduzidos apenas com produtor, consumidor e teste. | `CONTRACT_VERSIONING` |
| PTM-V25-006 | CONFIRMAR COM EXISTÊNCIA PROGRESSIVA | Outbox é necessária somente para eventos externos críticos realmente produzidos na V2.5; não criar estrutura sem fluxo vertical. | `TRANSACTIONAL_OUTBOX` |
| PTM-V25-007 | REUTILIZAR COM ADAPTAÇÃO | `bootstrap_v22.py` já separa listas dos perfis. Preservar independência funcional, removendo acoplamento à UI e execução. | `LISTS_DOMAIN_INDEPENDENT` |
| PTM-V25-008 | CONFIRMAR COMO NOVO | Não existe Android no legado. Pareamento deve ser local, revogável, auditável e sem transformar o Android em autoridade global. | `ANDROID_FOUNDATION` |
| PTM-V25-009 | CONFIRMAR COMO NOVO | Reconexão usa sequence quando disponível e snapshot como fallback; cache móvel não confirma estado global. | `ANDROID_RECONNECTION` |
| PTM-V25-010 | ADAPTAR | `CoordinateProfile`, aplicação, monitor, resolução e escala alimentam perfis separados e versionados. | `PROFILE_FOUNDATION` |
| PTM-V25-011A | ADAPTAR | O fluxo de calibração é preservado como captura e validação geométrica, sem teste físico por clique. Aprovação gera versão imutável. | `CALIBRATION_FOUNDATION` |
| PTM-V25-011B | ADAPTAR | ROIs entram como regiões versionadas e validadas; não autorizam observação ou execução sem gates posteriores. | `CALIBRATION_FOUNDATION` |
| PTM-V25-011C | ADAPTAR COM BLOQUEIO | Coordenadas `LARANJA`/`CINZA` tornam-se click targets geométricos. Movimento e clique são proibidos na V2.5. | `REAL_CLICK_EXCLUDED_FROM_V2_5` |
| PTM-V25-011D | CONFIRMAR COM AJUSTE | Âncoras e assinaturas visuais são conceitos novos necessários para compatibilidade; devem possuir versão e evidência. | `CALIBRATION_FOUNDATION` |
| PTM-V25-012 | ADAPTAR | O legado confirma Linux Mint/X11, `fcntl`, `xdg-open` e scripts Bash. Isolar dependências em adaptadores. | `LINUX_X11_FOUNDATION` |
| PTM-V25-013 | CONFIRMAR COMO PROGRESSIVO | Windows não está implementado. Foundation significa contratos e adaptadores mínimos testáveis, não paridade imediata. | `WINDOWS_FOUNDATION` |
| PTM-V25-014A | CONFIRMAR CONCLUÍDO COMO FONTE | O Anexo A aprovado é o inventário factual obrigatório. | `V2_4_3_COMPATIBILITY` |
| PTM-V25-014B | ADAPTAR | Usar conceitos de `ConfigSafetyManager`: cópia íntegra, hash e preservação da origem antes de transformação. | `BACKUP_RESTORE_BASIC` |
| PTM-V25-014C | ADAPTAR | JSON schema 4 é entrada de migração. Transformação deve validar campos, registrar rejeições e preservar o bruto. Nenhum SQL é definido nesta missão. | `LEGACY_LIST_IMPORT` |
| PTM-V25-014D | CONFIRMAR | Reconciliação compara origem, transformado, aceito, rejeitado e destino, com contagens e hashes. | `LEGACY_RECONCILIATION` |
| PTM-V25-014E | CONFIRMAR | Falha de transformação não pode destruir a origem; retorno ao estado anterior deve ser demonstrável. | `LEGACY_ROLLBACK_AVAILABLE` |
| PTM-V25-015A | ADAPTAR | Preservar logging rotativo e evoluir para eventos estruturados com redaction. | `OBSERVABILITY_MINIMUM` |
| PTM-V25-015B | CONFIRMAR COM AJUSTE | Separar auditoria de segurança, auditoria de comandos e logs diagnósticos. | `OBSERVABILITY_MINIMUM` |
| PTM-V25-015C | CONFIRMAR COMO MÍNIMO | Métricas básicas devem possuir produtor, consumidor, retenção e custo conhecidos. | `OBSERVABILITY_MINIMUM` |
| PTM-V25-015D | REUTILIZAR COM ADAPTAÇÃO | `diagnostics_tools.py` já coleta e exporta diagnóstico. Preservar comportamento, remover comandos inseguros e redigir dados sensíveis. | `OBSERVABILITY_MINIMUM` |
| PTM-V25-015E | CONFIRMAR COMO NOVO | `trace_id` e `command_id` correlacionam REST, eventos, auditoria e diagnóstico. | `OBSERVABILITY_MINIMUM` |
| PTM-V25-016 | ADAPTAR | Preservar escrita atômica, backup e recovery; substituir JSON como autoridade final por configuração versionada e validada. | `CONFIGURATION_FOUNDATION` |
| PTM-V25-017 | CONFIRMAR COMO NOVO | Rede local exige bind seguro, autenticação, pareamento, revogação, rate limit e redaction; detalhes dependem de revisão posterior. | `LOCAL_NETWORK_SECURITY` |
| PTM-V25-018 | CONFIRMAR | O servidor inicia em `SAFE_IDLE` sem Android e sem elevar modo automaticamente. Dúvida resulta em bloqueio. | `SERVER_SAFE_WITHOUT_CLIENT` |

## 7. Requisitos funcionais reconciliados

### 7.1 Servidor

| ID | Resultado | Critério de aceite arquitetural |
|---|---|---|
| V25-SRV-001 | RECONCILIADO | Inicialização em modo seguro; configuração e dependências validadas; nenhuma execução física disponível. |
| V25-SRV-002 | RECONCILIADO | Encerramento fecha writers, conexões e recursos sem corromper estado; não depende de monkey patch. |
| V25-SRV-003 | RECONCILIADO | Ausência ou perda do Android mantém `SAFE_IDLE`; estado local continua observável e não executável. |
| V25-SRV-004 | RECONCILIADO COM ESCOPO MÍNIMO | Health, state, compatibility e bootstrap/snapshot versionados; endpoints adicionais exigem fluxo vertical e testes. |

### 7.2 Configuração

| ID | Resultado | Critério de aceite arquitetural |
|---|---|---|
| V25-CFG-001 | RECONCILIADO | Resolução determinística de defaults seguros, arquivo autorizado e overrides explícitos. |
| V25-CFG-002 | RECONCILIADO | Configuração inválida falha fechada, produz diagnóstico e não ativa recursos críticos. |
| V25-CFG-003 | RECONCILIADO | Segredos nunca aparecem em logs, relatórios, eventos, commits ou snapshots exportáveis. |
| V25-CFG-004 | RECONCILIADO | Feature flags possuem dependências, safe default, auditoria e não habilitam execução real na V2.5. |

### 7.3 Persistência

| ID | Resultado | Critério de aceite arquitetural |
|---|---|---|
| V25-DB-001 | RECONCILIADO CONCEITUAL | Persistência local do servidor com integridade, foreign keys e modo seguro; schema físico só nasce com produtor, consumidor, requisito e teste. |
| V25-DB-002 | RECONCILIADO | Toda escrita passa por fronteira única; clientes, handlers e rotas não escrevem diretamente. |
| V25-DB-003 | RECONCILIADO SEM GERAR MIGRATION | Política versionada, checksum imutável, backup por risco, rollback/recovery e validações pós-migração. |
| V25-DB-004 | RECONCILIADO PROGRESSIVO | Eventos externos críticos são persistidos na mesma transação do estado e publicados após commit. |
| V25-DB-005 | RECONCILIADO | Backup e restore básicos incluem integridade, catálogo, cadeia de origem e teste de restauração autorizado. |

### 7.4 Listas

| ID | Resultado | Critério de aceite arquitetural |
|---|---|---|
| V25-LIST-001 | RECONCILIADO | CRUD de listas funciona sem análise, observação ou executor. |
| V25-LIST-002 | RECONCILIADO COM AJUSTE | Lista e item possuem versões imutáveis quando publicados/ativados; edição cria nova revisão conforme política. |
| V25-LIST-003 | RECONCILIADO | Data, horário, direção, identidade, duplicidade e consistência são validados com reason codes estáveis. |
| V25-LIST-004 | RECONCILIADO | Importa listas/sinais do schema 4 com relatório de aceitos, rejeitados e normalizados, sem clique e sem execução. |

### 7.5 Migração do legado

| ID | Resultado | Critério de aceite arquitetural |
|---|---|---|
| V25-LEG-001 | SATISFEITO PELA AUDITORIA | Inventário factual aprovado, rastreável e imutável. |
| V25-LEG-002 | RECONCILIADO | Manifesto identifica fonte, versão, hash, schema detectado, opções e política de erro. |
| V25-LEG-003 | RECONCILIADO | Backup pré-migração verificado antes de qualquer transformação autorizada. |
| V25-LEG-004 | RECONCILIADO | Transformação determinística, idempotente, versionada e sem apagar origem. |
| V25-LEG-005 | RECONCILIADO | Contagens e hashes reconciliam origem, destino, rejeições e perdas justificadas. |
| V25-LEG-006 | RECONCILIADO | Rollback ou recovery restaura estado anterior validado; falha impede startup normal. |

## 8. Requisitos adicionais derivados de lacunas factuais

Os itens abaixo são propostas do builder e dependem de revisão crítica independente.

| ID proposto | Requisito | Origem factual | Gate proposto |
|---|---|---|---|
| V25-SEC-001 | Bloqueio verificável de movimento de ponteiro e clique real em todos os modos V2.5. | Dois caminhos de clique real existentes no legado. | `V2_5_REAL_INPUT_BLOCKED` |
| V25-QA-001 | Quality gate agregado executa toda a suíte aplicável e impede validação fragmentada como única evidência. | Nove workflows fragmentados; nenhum executa todos os 20 testes. | `AGGREGATED_TEST_GATE` |
| V25-QA-002 | Fluxo end-to-end seguro de lista e agenda usa adapter nulo/simulado e prova ausência de clique. | Não existe E2E seguro da agenda no legado. | `SAFE_LIST_E2E` |
| V25-DOC-001 | Versão, entrypoint, instalação, README e CHANGELOG devem ser coerentes antes da entrega V2.5. | README indica versão e entrypoint incorretos; CHANGELOG incompleto. | `OPERATIONAL_DOCUMENTATION_CONSISTENCY` |

## 9. Classificação consolidada do legado

### REUTILIZAR

- leitura de versão e fallbacks;
- preflight temporal puro;
- identidades conceituais de perfil, lista, sinal e sessão;
- evidências históricas e testes unitários úteis;
- logo e memória documental, quando coerentes.

### ADAPTAR

- perfis, resolução, escala e geometria;
- listas, itens, agenda e históricos;
- lock de instância, logging, diagnóstico, backup e recovery;
- scripts Linux e cobertura de testes;
- JSON schema 4 exclusivamente como fonte de migração.

### SUBSTITUIR

- composição por monkey patch e ordem de instalação;
- monólito Tkinter como autoridade de domínio;
- JSON como fonte final de verdade;
- workflows fragmentados como único quality gate;
- README operacional incompatível com o entrypoint real.

### DESCONTINUAR NA V2.5

- teste de calibração com movimento e clique;
- execução agendada com `pynput`;
- status que represente clique físico como resultado válido da V2.5;
- qualquer elevação automática para modo executável.

## 10. Estados e lifecycle reconciliados

Os estados textuais do legado não são transportados automaticamente. A V2.5 deve distinguir ao menos:

```text
SYSTEM=STARTING|SAFE_IDLE|READY|DEGRADED|BLOCKED|STOPPING|STOPPED|RECOVERY_REQUIRED
MIGRATION=DISCOVERED|VALIDATED|BACKED_UP|TRANSFORMING|RECONCILING|COMPLETED|FAILED|ROLLED_BACK
LIST_VERSION=DRAFT|VALIDATED|ACTIVE|ARCHIVED|REJECTED
CALIBRATION=DRAFT|VALIDATING|APPROVED|REJECTED|SUPERSEDED
```

Regras:

- transições possuem origem, destino, condição, reason code, timestamp e evidência;
- `SAFE_IDLE` é o default;
- estado desconhecido não habilita capacidade;
- `CLIQUE_ENVIADO` não pertence ao lifecycle operacional da V2.5;
- nomes finais dependem da revisão crítica e dos ADRs posteriores.

## 11. Persistência e existência progressiva

O catálogo lógico histórico não vira backlog físico automático.

```text
ENTITY_EXISTS_PHYSICALLY_ONLY_IF=
PRODUCER_DEFINED
AND CONSUMER_DEFINED
AND REQUIREMENT_LINKED
AND TEST_LINKED
AND RETENTION_DEFINED_WHEN_HISTORICAL
```

A PTM V2.5 preserva a política de escritor único, transações curtas, publicação pós-commit, integridade e recovery. Nenhuma tabela, SQL ou migration é criada nesta missão.

## 12. Evidências futuras exigidas

Uma implementação futura só poderá declarar requisito atendido com evidência apropriada:

- teste unitário para regra pura;
- teste de contrato para REST/eventos;
- teste de integração para persistência e outbox;
- teste de migração com fixture sanitizada e hashes;
- teste de recovery e restauração;
- teste multiplataforma por adaptador;
- E2E seguro com adapter nulo;
- prova negativa de ausência de movimento e clique na V2.5;
- relatório TXT e artefatos versionados conforme protocolo.

## 13. Riscos residuais

| Risco | Severidade | Tratamento na PTM V2.5 |
|---|---|---|
| clique real presente no legado | Crítico | requisito explícito de bloqueio; não migrar executor |
| cadeia de monkey patches | Alto | substituir por composição explícita e regressão comportamental |
| JSON sem validação integral de sessão/eventos | Alto | validar entrada, preservar bruto e registrar rejeições |
| escopo físico excessivo | Alto | existência progressiva por produtor/consumidor/teste |
| Linux/X11 acoplado | Médio | adaptadores e Windows progressivo |
| workflows fragmentados | Médio | quality gate agregado proposto |
| documentação defasada | Alto | gate de consistência operacional proposto |
| thresholds não medidos | Médio | manter provisórios e fora da fundação quando não necessários |

## 14. Gates do builder

```text
BASELINE_PTM_RECONSTRUCTED=PASS
AUDIT_SOURCES_CONFIRMED=PASS
STRUCTURAL_RECONCILIATION=PASS_BUILDER
FUNCTIONAL_RECONCILIATION=PASS_BUILDER
LEGACY_CLASSIFICATION_PRESERVED=PASS
REAL_CLICK_SCOPE_EXCLUSION=PASS
JSON_MIGRATION_BOUNDARY=PASS
PATCH_CHAIN_REPLACEMENT=PASS
ADDITIONAL_GAPS_IDENTIFIED=PASS_BUILDER
CODE_CHANGED=NO
SQL_GENERATED=NO
MIGRATIONS_GENERATED=NO
APPLICATION_EXECUTED=NO
PTM_V2_5_DEFINITIVE=NO
PTM_V2_5_CRITICAL_REVIEW=PENDING
```

## 15. Condição de avanço

A LEA-8 somente pode avançar para fechamento após:

```text
BUILDER_SELF_REVIEW=PASS
TRACEABILITY_COMPLETENESS=PASS
REQUIREMENT_ID_UNIQUENESS=PASS
SCOPE_V2_5_V2_6_V2_7_SEPARATION=PASS
INDEPENDENT_CRITICAL_REVIEW=PASS
CRITICAL_BLOCKERS=0
```

Mesmo após o fechamento da LEA-8, implementação permanece proibida. A próxima etapa de produto só pode ser preparada após o Boss Gate da PTM V2.5.