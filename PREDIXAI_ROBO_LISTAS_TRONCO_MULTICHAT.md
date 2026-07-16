# PREDIXAI ROBÔ DE LISTAS — TRONCO MULTICHAT OFICIAL

## 1. Estado de entrada

```text
VERSÃO_REAL=V2.4.3-R1
PTP-GOV.5.2=CONCLUÍDA
MEMORY_ENVIRONMENT_GATE=PASS
MEMORY_ACCESS_TEST_A=PASS
MEMORY_RECONSTRUCTION_TEST_B=PASS
MEMORY_CONTINUITY_TEST_C=PASS
MEMORY_ACCEPTANCE_SUITE=PASS
AUDITORIA_MESTRA=LIBERADA
IMPLEMENTAÇÃO=NAO_AUTORIZADA
```

## 2. Roadmap oficial

```text
✅ PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória
✅ Etapa 0 — Verificação do Ambiente
✅ Teste A — Acesso Documental
✅ Teste B — Reconstrução
✅ Teste C — Continuidade

🟧 PTP-GOV.6 — Auditoria Mestra V2.4.3-R1
⬜ Anexo A — Inventário factual do legado
⬜ PTP-GOV.6-RC — Revisão crítica da Auditoria Mestra e do Anexo A

⬜ PTM V2.5 — Reconciliação com o legado
⬜ PTM V2.5-RC — Revisão crítica

⬜ PTM V2.6 — Observação, extração, análise e sinais
⬜ PTM V2.6-RC — Revisão crítica

⬜ PTM V2.7 — Execução controlada, reconciliação e estabilização
⬜ PTM V2.7-RC — Revisão crítica

⬜ PTP-ARCH.1 — Consolidação cruzada
⬜ PTP-ARCH.1-RC — Revisão crítica da consolidação

⬜ PTP-ADR.1 — Consolidação dos ADRs
⬜ PTP-ADR.1-RC — Revisão crítica dos ADRs

⬜ PTP-DOC.1 — Documento Mestre
⬜ PTP-DOC.1-RC — Revisão crítica final

⬜ PTP-ARCH.2 — Congelamento da Arquitetura V1.0
⬜ PTP-READY.1 — Revisão de prontidão para implementação
⬜ Implementação autorizada em novos chats
```

## 3. Chats oficiais

### CHAT 01 — PTP-GOV.6 — Auditoria Mestra

Objetivo:
- produzir o Anexo A;
- inventariar diretórios, arquivos, módulos, funções, entrypoints, configuração, persistência, scripts, testes, logs, backups e documentos;
- classificar cada item;
- rastrear com a PTM V2.5 preliminar.

Saída: `AUDITORIA_MESTRA_DRAFT_COMPLETE=PASS`

Prompt específico:

```text
Este chat trabalha exclusivamente na PTP-GOV.6.
Inicie pelo Anexo A.
Registre fonte, caminho, branch/commit, evidência, classificação, certeza, risco e rastreabilidade PTM.
Não altere código.
Não avance para PTM V2.5.
```

### CHAT 02 — PTP-GOV.6-RC

Objetivo: revisão crítica da Auditoria Mestra e do Anexo A.

Gate: `AUDITORIA_MESTRA_CRITICAL_REVIEW=PASS`

### CHAT 03 — PTM V2.5

Objetivo: reconciliar a PTM preliminar com o legado aprovado.

Gate: `PTM_V2_5_DRAFT_COMPLETE=PASS`

### CHAT 04 — PTM V2.5-RC

Gate: `PTM_V2_5_CRITICAL_REVIEW=PASS`

### CHAT 05 — PTM V2.6

Objetivo: observação, extração, análise, estratégias, sinais e Android operacional.

Gate: `PTM_V2_6_DRAFT_COMPLETE=PASS`

### CHAT 06 — PTM V2.6-RC

Gate: `PTM_V2_6_CRITICAL_REVIEW=PASS`

### CHAT 07 — PTM V2.7

Objetivo: execução controlada e simulada, comandos, reconciliação, distribuição e estabilização.

Gate: `PTM_V2_7_DRAFT_COMPLETE=PASS`

### CHAT 08 — PTM V2.7-RC

Gate: `PTM_V2_7_CRITICAL_REVIEW=PASS`

### CHAT 09 — PTP-ARCH.1

Objetivo: consolidação cruzada entre Auditoria Mestra e PTMs.

Gate: `CROSS_CONSOLIDATION_COMPLETE=PASS`

### CHAT 10 — PTP-ARCH.1-RC

Gate: `CROSS_CONSOLIDATION_CRITICAL_REVIEW=PASS`

### CHAT 11 — PTP-ADR.1

Objetivo: consolidar decisões arquiteturais em ADRs.

Gate: `ADR_SET_COMPLETE=PASS`

### CHAT 12 — PTP-ADR.1-RC

Gate: `ADR_CRITICAL_REVIEW=PASS`

### CHAT 13 — PTP-DOC.1

Objetivo: gerar o Documento Mestre.

Gate: `MASTER_DOCUMENT_DRAFT_COMPLETE=PASS`

### CHAT 14 — PTP-DOC.1-RC

Gate: `MASTER_DOCUMENT_CRITICAL_REVIEW=PASS`

### CHAT 15 — PTP-ARCH.2

Objetivo: congelar Arquitetura V1.0.

Gate: `ARCHITECTURE_V1_0_FROZEN=PASS`

### CHAT 16 — PTP-READY.1

Objetivo: decisão `GO`, `GO_WITH_CONDITIONS` ou `NO_GO`.

Gate: `IMPLEMENTATION_READINESS=GO|GO_WITH_CONDITIONS|NO_GO`

## 4. Regra de atualização

Atualizar este documento sempre que uma etapa ou revisão iniciar/concluir, surgir mini-PTP, mudar escopo, dependência, versão, gate ou sequência.

Nenhuma mudança de roadmap é válida apenas no chat.

## 5. Gate universal

```text
CURRENT_STAGE_DOCUMENTED=PASS
CRITICAL_REVIEW_STATUS=PASS|PENDING
CRITICAL_BLOCKERS=0
PROJECT_STATE_UPDATED=PASS
TRUNK_UPDATED=PASS
LINEAR_UPDATED=PASS
PR_MERGED=PASS
HANDOFF_CHECKPOINT=PASS
```