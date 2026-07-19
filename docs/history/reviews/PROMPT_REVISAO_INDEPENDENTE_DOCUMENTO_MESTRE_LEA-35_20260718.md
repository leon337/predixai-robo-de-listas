# PROMPT DE REVISÃO CRÍTICA INDEPENDENTE

## LEA-35 — Documento Mestre da Arquitetura V1.0

Atue exclusivamente como revisor crítico independente do PR `#56` do repositório `leon337/predixai-robo-de-listas`.

## 1. Baseline

```text
BUILDER_ISSUE=LEA-34
REVIEW_ISSUE=LEA-35
PULL_REQUEST=56
BASE_MAIN_SHA=65b18341c06a391ea48ae5029102ad7a095c3340
STATE_REVISION=19
TRANSITION_ID=LEA-34-T01
DOCUMENTATION_ONLY=YES
IMPLEMENTATION_AUTHORIZED=NO
```

Use o HEAD vivo do PR no início da revisão e registre a SHA revisada. Não aceite SHA prevista ou snapshot como substituto da consulta ao GitHub.

## 2. Artefatos obrigatórios

1. `docs/architecture/PLANO_MISSAO_DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md`;
2. `docs/architecture/DOCUMENTO_MESTRE_ARQUITETURA_V1_LEA-34_20260718.md`;
3. `docs/architecture/MATRIZ_RASTREABILIDADE_DOCUMENTO_MESTRE_LEA-34_20260718.md`;
4. `docs/architecture/APENDICE_DOMINIOS_HANDOFFS_DOCUMENTO_MESTRE_LEA-34_20260718.md`;
5. `docs/history/reviews/AUTO_REVISAO_BUILDER_DOCUMENTO_MESTRE_LEA-34_20260718.md`;
6. `PROJECT_RUNTIME_STATE.yaml`;
7. `PROJECT_STATE.md`;
8. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
9. `README.md`;
10. Linear LEA-34 e LEA-35.

## 3. Fontes normativas de comparação

- `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md`;
- `docs/protocols/POLITICA_AUTOMACAO_AMBIENTE_CONTROLADO.md`;
- PTM V2.5, V2.6 e V2.7 e suas matrizes/adendos finais;
- matriz consolidada LEA-18;
- mapa unificado de 16 domínios e 12 handoffs;
- ADR-0001 a ADR-0018 `ACCEPTED`;
- matriz de prontidão LEA-32 Reteste 01;
- relatórios finais das revisões críticas anteriores.

## 4. Verificações obrigatórias

### G1 — autoridade e estado

- missão, PR, Linear, revisão 19 e transição LEA-34-T01 coerentes;
- `observed_main_head` é snapshot informacional, não SHA prevista;
- README é projeção derivada e está sincronizado;
- nenhuma declaração de merge futuro como fato.

### G2 — cobertura arquitetural

- 16 domínios presentes e semanticamente coerentes;
- 12 handoffs com origem, destino, contrato mínimo e falha obrigatória;
- caminhos de bypass proibidos preservados;
- fronteiras V2.5/V2.6/V2.7 preservadas.

### G3 — requisitos

Recalcule e confira:

```text
V2_5=56
V2_6=78
V2_7=84
TOTAL=218
DUPLICATES=0
ORPHANS=0
NEW_REQUIREMENT_IDS=0
```

Verifique se cada faixa da matriz LEA-34 corresponde à matriz consolidada LEA-18 e possui domínio, handoff aplicável, ADR, seção DM e família de teste futuro.

### G4 — ADRs

- ADR-0001 a ADR-0018 referenciados;
- decisões e dependências não alteradas silenciosamente;
- lifecycle `ACCEPTED` preservado;
- DAG sem ciclo preservado.

### G5 — política A+B

- Modo A controlado não é confundido com LIVE;
- domínio analítico não chama adaptador diretamente;
- Modo B permanece desligado;
- efeito financeiro real exige gates separados;
- autenticação, alvos e allowlists permanecem condicionados;
- parada de emergência, circuit breaker e reconciliação dominam o fluxo.

### G6 — testes e evidências

- famílias `T-*` não são apresentadas como testes executados;
- IDs individuais podem permanecer para plano de implementação se a postergação estiver explícita e não quebrar rastreabilidade;
- `CI_GREEN != RUNTIME_GATES_PASS`;
- nenhuma evidência runtime inventada.

### G7 — limites

Confirme ausência de:

- alteração de código de aplicação ou testes;
- SQL ou migrations;
- execução de runtime;
- clique real;
- segredo, token ou credencial;
- autorização de implementação;
- armamento LIVE.

## 5. Classificação de achados

```text
CRITICAL=risco de segurança, autoridade ou efeito real indevido
MAJOR=quebra normativa, requisito/ADR/domínio/handoff ausente ou contradição material
MINOR=inconsistência documental localizada sem quebra arquitetural
ADVISORY=melhoria não bloqueante
```

Para cada achado informe:

1. ID e severidade;
2. arquivo e trecho;
3. evidência normativa;
4. impacto;
5. correção objetiva;
6. necessidade de reteste.

## 6. Decisão

Emitir apenas uma decisão formal:

```text
PASS
WARN
FAIL
BLOCKED
```

`PASS` exige:

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
OPEN_BLOCKING_FINDINGS=0
CANONICAL_DOMAINS=16/16
MANDATORY_HANDOFFS=12/12
REQUIREMENTS_TRACEABLE=218/218
ADRS_REFERENCED=18/18
POLICY_A_B_ALIGNMENT=PASS
ARCHITECTURE_IMPLEMENTATION_BOUNDARY=PASS
README_SYNC=PASS
```

O revisor não deve alterar o PR do builder nem autorizar merge, implementação ou congelamento da arquitetura. O merge permanece gate humano separado.