# CATÁLOGO DE DECISÕES CANDIDATAS A ADR

## Consolidação cruzada PTM V2.5 → V2.6 → V2.7

## 1. Controle

```text
DOCUMENT_STATUS=BUILDER_ADR_CANDIDATE_CATALOG_COMPLETE
MISSION=LEA-18
LINEAR_ISSUE=LEA-18
PULL_REQUEST=40
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=98bb1d33b9d8eca702fb4e52bdde02686021c766
PRE_WRITE_EXPECTED_PR_HEAD=57d7a8d95bd462d6b673921e6ff0f9835cc3502f
STATE_REVISION=7
TRANSITION_ID=LEA-18-T01
ADR_CREATED=NO
ARCHITECTURAL_DECISION_FINALIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

Este catálogo identifica decisões que deverão ser formalizadas após a aprovação da consolidação cruzada. Ele não substitui ADR, não escolhe tecnologia e não autoriza implementação.

## 2. Critérios de prioridade

```text
P0=necessária antes do Documento Mestre definitivo
P1=necessária antes do plano de implementação ou do primeiro fluxo vertical
P2=pode ser refinada durante planejamento, sem enfraquecer o default seguro
```

## 3. Candidatos

| ID | Prioridade | Decisão a formalizar | Default seguro vigente | Evidência/dependência necessária | Gate de resolução |
|---|---|---|---|---|---|
| ADR-CAND-001 | P0 | topologia do servidor e autoridade de estado | servidor é autoridade global; clientes são visões locais | mapa de processos, isolamento, lifecycle, recuperação e implantação no Linux Mint | antes do Documento Mestre final |
| ADR-CAND-002 | P0 | tecnologia de persistência e fronteira de escritor único | nenhuma escrita direta por cliente/handler; schema físico progressivo | requisitos de integridade, concorrência, backup, migrations e recuperação | antes do Documento Mestre final |
| ADR-CAND-003 | P1 | estratégia de migrations, compatibilidade e importação do JSON legado | origem preservada, transformação idempotente, reconciliação e rollback | schema de destino, volume real, testes de restauração e plano de corte | antes da implementação de persistência |
| ADR-CAND-004 | P0 | contratos REST, eventos e versionamento | endpoint/evento só existe com produtor, consumidor, requisito e teste | fluxos verticais, consumidores móveis, sequência, idempotência e snapshot fallback | antes do Documento Mestre final |
| ADR-CAND-005 | P0 | identidade, pareamento e autoridade de clientes | pareamento local, revogável; servidor mantém autoridade global | threat model, expiração, rotação, reconexão e perda de dispositivo | antes do Documento Mestre final |
| ADR-CAND-006 | P0 | modelo de perfil, ROI, assinatura visual e `target_logical_id` | identidade desconhecida ou geometria incompatível bloqueia | taxonomia de alvos, compatibilidade, versionamento, calibração e resolução | antes do Documento Mestre final |
| ADR-CAND-007 | P1 | política de retenção de frames, recortes e evidências visuais | referência e hash podem sobreviver; imagem bruta mínima por padrão | privacidade, custo, diagnóstico, redaction e requisitos de auditoria | antes do primeiro fluxo de captura persistente |
| ADR-CAND-008 | P0 | arquitetura dos motores A–H e envelope de análise | snapshot imutável, inputs explícitos, ausência de efeito colateral físico | interfaces, paralelismo, determinismo, cache e tratamento de contradições | antes do Documento Mestre final |
| ADR-CAND-009 | P0 | versionamento de estratégias, arbitragem e lifecycle de sinais | estratégia versionada; sinal não autoexecuta | catálogo de regras, horizons, fingerprint, expiração e supersessão | antes do Documento Mestre final |
| ADR-CAND-010 | P0 | máquina de estados de comando e execução | estados documentais V2.7; dúvida bloqueia; restart invalida comando anterior | transições integrais, persistência, concorrência, crash/recovery e reason codes | antes do Documento Mestre final |
| ADR-CAND-011 | P0 | contrato e isolamento dos adaptadores `NULL|SIMULATED|CONTROLLED_UI` | capacidade desconhecida bloqueia; UI apenas por adaptador controlado | plataformas, allowlists, identidade de foreground, payload e testes negativos | antes do Documento Mestre final |
| ADR-CAND-012 | P0 | topologia e autoridade do kill switch | kill switch domina fila, grant, retry e dispatch | local/remoto, latência, disponibilidade, autenticação, auditoria e recovery | antes do Documento Mestre final |
| ADR-CAND-013 | P1 | idempotência, deduplicação, serialização e circuit breaker | conflito por alvo bloqueia; retry só com `FAILED_NO_EFFECT` | chave determinística, escopo, retenção, concorrência e categorias de falha | antes do executor implementado |
| ADR-CAND-014 | P0 | recibo e reconciliação multidimensional | `ui_result` e `financial_result` separados; recibo não é verdade global | fontes de observação, divergência, compensação, `UNKNOWN_EFFECT` e retenção | antes do Documento Mestre final |
| ADR-CAND-015 | P0 | observabilidade, auditoria append-only e redaction | auditoria separada de logs; segredos e dados sensíveis redigidos | catálogo de eventos, retenção, acesso, integridade, exportação e métricas | antes do Documento Mestre final |
| ADR-CAND-016 | P1 | modelo de relógio, prazo e identidade de processo | UTC/TTL auditáveis; monotônico local; restart invalida despachabilidade | fonte temporal, skew, rollback, boot/process IDs e testes de recovery | antes do executor implementado |
| ADR-CAND-017 | P2 | thresholds e limites numéricos | valores conservadores e provisórios; desconhecido reduz capacidade | benchmark reproduzível, hardware-alvo, dados e critérios de estabilidade | após benchmark, antes do GO de runtime |
| ADR-CAND-018 | P1 | estratégia de testes e evidência por camada | especificação não equivale a runtime; provas negativas obrigatórias | unit, property, contract, replay, E2E controlado, crash/restart e relatórios | antes do plano de implementação aprovado |

## 4. Agrupamento por capítulo do futuro Documento Mestre

| Capítulo | Candidatos |
|---|---|
| governança e lifecycle | ADR-CAND-001, 010, 012, 016 |
| dados e persistência | ADR-CAND-002, 003, 004 |
| identidade e clientes | ADR-CAND-005 |
| perfis e fonte visual | ADR-CAND-006, 007 |
| análise e estratégia | ADR-CAND-008, 009, 017 |
| execução controlada | ADR-CAND-011, 013, 014 |
| segurança, auditoria e qualidade | ADR-CAND-015, 018 |

## 5. Dependências entre decisões

```text
ADR-CAND-001 -> ADR-CAND-002|004|005|010|012|015
ADR-CAND-002 -> ADR-CAND-003|004|014|015
ADR-CAND-006 -> ADR-CAND-007|011
ADR-CAND-008 -> ADR-CAND-009
ADR-CAND-009 -> ADR-CAND-010
ADR-CAND-010 -> ADR-CAND-011|012|013|014|016
ADR-CAND-011 -> ADR-CAND-014|018
ADR-CAND-012 -> ADR-CAND-018
ADR-CAND-014 -> ADR-CAND-015|018
```

As setas indicam dependência de decisão, não ordem automática de implementação.

## 6. Decisões explicitamente fora de escopo

```text
REAL_FINANCIAL_ADAPTER=OUT_OF_SCOPE
PRODUCTION_BROKER_INTEGRATION=OUT_OF_SCOPE
REAL_MONEY_OPERATION=OUT_OF_SCOPE
PRODUCTION_CREDENTIAL_MODEL=OUT_OF_SCOPE
AUTONOMOUS_EXTERNAL_INFRASTRUCTURE=OUT_OF_SCOPE
```

Qualquer uma dessas decisões exigirá missão própria, análise comercial/legal, threat model, autorização explícita e revisão crítica independente.

## 7. Critério de prontidão para iniciar ADRs

```text
CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
UNRESOLVED_NORMATIVE_CONFLICTS=0
TRACEABILITY_COMPLETENESS=PASS
DOMAIN_BOUNDARY_CONSISTENCY=PASS
```

Antes desse gate, os itens permanecem apenas candidatos.

## 8. Resultado do builder

```text
ADR_CANDIDATE_COUNT=18
P0_CANDIDATES=12
P1_CANDIDATES=5
P2_CANDIDATES=1
DEPENDENCY_MAP_DEFINED=PASS
DOCUMENT_MASTER_GROUPING_DEFINED=PASS
OUT_OF_SCOPE_DECISIONS_RECORDED=PASS
ADR_CREATED=NO
FINAL_DECISION_TAKEN=NO
CATALOG_BLOCKERS=0
```

## 9. Próxima ação

Consolidar as entregas G2–G5 em um documento arquitetural único e executar auto-revisão preliminar do builder antes do handoff para revisão crítica independente.