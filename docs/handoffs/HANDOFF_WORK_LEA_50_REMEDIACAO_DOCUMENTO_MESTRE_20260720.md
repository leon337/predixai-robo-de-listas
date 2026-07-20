# HANDOFF WORK — LEA-50

## Remediação da completude executiva do Documento Mestre

```text
REPOSITORY=leon337/predixai-robo-de-listas
BRANCH=leonpcsn/lea-50-roadmap-implementacao-v1
BASE_MAIN_SHA=0968ae86e92e7b640cbcc77941d49a9474839650
LINEAR_ISSUE=LEA-50
MISSION=REMEDIAR_DOCUMENTO_MESTRE_COM_MAPA_CANONICO_DE_DESENVOLVIMENTO
DOCUMENTATION_ONLY=YES
APPLICATION_CODE_AUTHORIZED=NO
TEST_CODE_AUTHORIZED=NO
SQL_AUTHORIZED=NO
MIGRATION_AUTHORIZED=NO
ARCHITECTURE_CHANGE_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

## Papel do Work

Atuar como engenheiro de software sênior, arquiteto, analista de produto, auditor técnico, revisor crítico, especialista em testes, segurança, documentação e rastreabilidade.

Usar exclusivamente o repositório `leon337/predixai-robo-de-listas` como fonte factual. GitHub é a memória técnica e documental. Linear controla missão, bloqueios, dependências e progresso. `PROJECT_RUNTIME_STATE.yaml` é o estado estruturado oficial. `PROJECT_STATE.md` é a explicação humana oficial.

## Problema confirmado

O Documento Mestre da Arquitetura V1.0 contém os 16 domínios, 218 requisitos, 12 handoffs, 18 ADRs, contratos, estados, limites e gates. Entretanto, sua seção de roadmap termina no processo de aprovação da arquitetura e não contém a sequência canônica de desenvolvimento do produto.

A consequência foi a implementação de FND-001 e FND-002 sem uma fila completa e congelada de incrementos posteriores.

```text
ARCHITECTURE_LOGIC=COMPLETE
REQUIREMENT_TRACEABILITY=218_OF_218
IMPLEMENTATION_SEQUENCE=INCOMPLETE
NEXT_INCREMENT_AMBIGUITY=CONFIRMED
```

## Decisão canônica

O mapa de desenvolvimento deve ficar dentro do Documento Mestre. Arquivos auxiliares podem existir apenas como anexos normativos subordinados.

```text
CANONICAL_ROADMAP_AUTHORITY=DOCUMENTO_MESTRE
SEPARATE_ROADMAP_AS_AUTHORITY=NO
NORMATIVE_ANNEXES_ALLOWED=YES
ANNEX_CAN_OVERRIDE_MASTER=NO
```

## Fontes obrigatórias

Ler integralmente antes de editar:

1. `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md`
2. `PROJECT_RUNTIME_STATE.yaml`
3. `PROJECT_STATE.md`
4. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`
5. `docs/protocols/PREDIXAI_ROBO_LISTAS_SKILLS.md`
6. `docs/protocols/PREDIXAI_ROBO_LISTAS_RESPONSE_MODEL.md`
7. `docs/architecture/DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md`
8. `docs/architecture/MATRIZ_RASTREABILIDADE_DOCUMENTO_MESTRE_LEA-34_20260718.md`
9. `docs/architecture/MATRIZ_CONSOLIDADA_REQUISITOS_RASTREABILIDADE_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`
10. `docs/architecture/MAPA_UNIFICADO_DOMINIOS_FRONTEIRAS_PTM_V2.5_V2.6_V2.7_LEA-18_20260717.md`
11. `docs/architecture/APENDICE_DOMINIOS_HANDOFFS_DOCUMENTO_MESTRE_LEA-34_20260718.md`
12. `docs/architecture/adrs/README.md` e ADR-0001 a ADR-0018
13. `docs/architecture/REVISAO_PRONTIDAO_IMPLEMENTACAO_LEA-40_20260719.md`
14. documentos de FND-001 e FND-002 indicados pelo estado oficial
15. Linear: LEA-40, LEA-41, LEA-43, LEA-44, LEA-45, LEA-46, LEA-47, LEA-48, LEA-49 e LEA-50

## Objetivo

Remediar o Documento Mestre para que ele passe a ser simultaneamente:

- autoridade arquitetural;
- mapa canônico de desenvolvimento;
- controlador da ordem dos incrementos;
- referência para requisitos, testes, versões, gates e rollback.

Não alterar a Arquitetura V1.0 congelada. Apenas completar sua dimensão executiva.

## Entregas obrigatórias

### 1. Atualização do Documento Mestre

Editar o arquivo canônico:

`docs/architecture/DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md`

Adicionar seções equivalentes a:

```text
DM-24 — Mapa canônico de desenvolvimento V1
DM-25 — Regras de decomposição incremental
DM-26 — Grafo macro de precedência
DM-27 — Política de versionamento e validação local
DM-28 — Gates NULL → SIMULATED → CONTROLLED_UI → LIVE_GATED
DM-29 — Política de rollback e continuidade
DM-30 — Índice e autoridade dos anexos normativos
```

A numeração pode ser ajustada apenas para preservar consistência interna.

### 2. Sequência completa de incrementos

Formalizar todos os incrementos posteriores à FND-002. Cada incremento deve conter:

```text
ID
NOME
OBJETIVO
DEPENDE_DE
DOMINIOS
REQUISITOS
ADRS
HANDOFFS
MODO
CRITERIOS_DE_ENTRADA
ENTREGAS
TESTES
VALIDACAO_LOCAL
ROLLBACK
PROIBICOES
GATE_DE_SAIDA
VERSAO_ALVO
```

### 3. Mapeamento integral dos 218 requisitos

Garantir:

```text
TOTAL_REQUIREMENTS=218
V2_5=56
V2_6=78
V2_7=84
DUPLICATES=0
ORPHANS=0
UNMAPPED_TO_INCREMENT=0
```

Criar matriz normativa:

```text
REQUIREMENT_ID
→ DOMAIN
→ HANDOFF
→ ADR
→ MASTER_SECTION
→ IMPLEMENTATION_INCREMENT
→ TEST_FAMILY
→ LOCAL_EVIDENCE
→ ACCEPTANCE_GATE
```

### 4. Grafo de dependências

Construir grafo de precedência sem ciclos e sem saltos indevidos de capacidade.

Validar pelo menos:

```text
DEPENDENCY_CYCLES=0
INCREMENT_WITHOUT_PREDECESSOR_JUSTIFICATION=0
MODE_ESCALATION_WITHOUT_GATE=0
```

### 5. Política de modos

Preservar a progressão:

```text
NULL_ONLY
→ SIMULATED
→ CONTROLLED_UI
→ LIVE_GATED
```

Regras:

- `LIVE_GATED` permanece apenas como capacidade arquitetural futura;
- nenhuma missão atual pode liberar efeito financeiro real;
- `CONTROLLED_UI` exige autorização separada, alvo lógico e allowlist;
- `SIMULATED` não pode produzir efeito externo;
- nenhum incremento pode elevar modo silenciosamente.

### 6. Versionamento e testes locais

Definir como cada incremento altera versão, gera evidência e é validado no Linux Mint.

Cada incremento deve prever um comando único para o Leo:

```text
ATUALIZAR_REPOSITORIO
→ EXECUTAR_TESTES
→ INICIAR_FUNCIONALIDADE_QUANDO_APLICAVEL
→ GERAR_RELATORIO_TXT
```

O Leo não deve criar branch, commit, push, PR ou administrar stash no fluxo normal.

### 7. Anexos normativos subordinados

Podem ser criados:

- matriz 218 requisitos → incrementos;
- grafo detalhado;
- catálogo de testes;
- catálogo de versões;
- matriz de evidências e rollback.

Cada anexo deve declarar:

```text
DOCUMENT_TYPE=NORMATIVE_ANNEX
PARENT_AUTHORITY=DOCUMENTO_MESTRE
CAN_OVERRIDE_MASTER=NO
REQUIRED_FOR_MASTER_VALIDITY=YES
```

### 8. Estado oficial

Atualizar na mesma branch:

- `PROJECT_RUNTIME_STATE.yaml`
- `PROJECT_STATE.md`
- `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`

Registrar:

```text
ACTIVE_MISSION=LEA-50
MISSION_TYPE=DOCUMENT_MASTER_EXECUTIVE_REMEDIATION
ROADMAP_AUTHORITY=DOCUMENTO_MESTRE
IMPLEMENTATION_SEQUENCE_STATUS=BUILDER_COMPLETE_AWAITING_INDEPENDENT_REVIEW
NEXT_CODE_INCREMENT=DEFINED_BY_MASTER_BUT_NOT_AUTHORIZED
```

### 9. Relatórios de validação

Produzir relatório builder contendo:

```text
REQUIREMENTS_MAPPED=218_OF_218
INCREMENTS_WITHOUT_REQUIREMENTS=0
REQUIREMENTS_WITHOUT_INCREMENT=0
DEPENDENCY_CYCLES=0
GATES_WITHOUT_TEST=0
INCREMENTS_WITHOUT_ROLLBACK=0
INCREMENTS_WITHOUT_LOCAL_VALIDATION=0
ARCHITECTURE_CHANGED=NO
APPLICATION_CODE_CHANGED=NO
```

### 10. PR Draft

Abrir PR Draft para `main` com:

```text
TITLE=docs(LEA-50): completar Documento Mestre com mapa de desenvolvimento V1
MERGE_AUTHORIZED=NO
INDEPENDENT_REVIEW_REQUIRED=YES
```

Não promover para Ready, não aprovar e não mesclar.

### 11. Revisão crítica independente

Criar uma issue separada no Linear para revisão independente do HEAD final da LEA-50.

A revisão deve validar:

- cobertura 218/218;
- ausência de alteração arquitetural;
- ausência de ciclos;
- ordem coerente dos incrementos;
- segurança dos gates;
- coerência de versões e testes locais;
- ausência de ambiguidade sobre o próximo incremento;
- GitHub e Linear sincronizados.

Decisão permitida:

```text
PASS
PASS_WITH_CONDITIONS
FAIL
```

## Gates objetivos

```text
G1_SOURCE_AUTHORITY=PASS
G2_MASTER_CANONICAL_ROADMAP=PASS
G3_REQUIREMENT_MAPPING=218_OF_218
G4_DEPENDENCY_GRAPH=PASS_NO_CYCLES
G5_INCREMENT_DECOMPOSITION=PASS
G6_MODE_GATES=PASS
G7_VERSIONING_AND_LOCAL_TESTS=PASS
G8_ROLLBACK_COMPLETE=PASS
G9_ARCHITECTURE_UNCHANGED=PASS
G10_STATE_SYNC=PASS
G11_DRAFT_PR_OPEN=PASS
G12_INDEPENDENT_REVIEW_PREPARED=PASS
```

## Proibições

```text
APPLICATION_CODE=NO
TEST_CODE=NO
SQL=NO
MIGRATIONS=NO
DATABASE_SCHEMA=NO
ANDROID_IMPLEMENTATION=NO
OCR_IMPLEMENTATION=NO
SIGNAL_ENGINE_IMPLEMENTATION=NO
RUNTIME_MUTATION=NO
REAL_CLICK=NO
BROKER=NO
LIVE=NO
REAL_FINANCIAL_EFFECT=NO
MERGE=NO
ARCHITECTURE_REOPEN=NO
NEW_REQUIREMENT_IDS=NO
```

## Regra de bloqueio

Parar somente por:

- divergência factual insolúvel entre fontes;
- requisito sem fonte normativa;
- necessidade real de alterar arquitetura congelada;
- conflito de baseline;
- falha de conector que impeça publicação;
- decisão humana obrigatória.

Nesses casos, registrar evidência no GitHub e Linear e marcar:

```text
BLOCKED=YES
REASON=<factual>
NEXT_REQUIRED_HUMAN_DECISION=<objetiva>
```

## Resultado esperado

O projeto deve sair da LEA-50 com um Documento Mestre que responda, sem decisão improvisada:

```text
QUAL_INCREMENTO_VEM_AGORA
POR_QUE_ELE_VEM_AGORA
DO_QUE_ELE_DEPENDE
QUAIS_REQUISITOS_ELE_CUMPRE
COMO_ELE_E_TESTADO
COMO_ELE_E_VALIDADO_LOCALMENTE
COMO_ELE_E_REVERTIDO
QUAL_GATE_LIBERA_O_PROXIMO
```

## Encerramento da execução do Work

Ao terminar, entregar:

1. branch e HEAD final;
2. lista de arquivos alterados;
3. resumo da sequência de incrementos;
4. cobertura 218/218;
5. relatório de validação;
6. PR Draft;
7. issue de revisão independente;
8. divergências encontradas;
9. bloqueios restantes;
10. próxima ação objetiva.
