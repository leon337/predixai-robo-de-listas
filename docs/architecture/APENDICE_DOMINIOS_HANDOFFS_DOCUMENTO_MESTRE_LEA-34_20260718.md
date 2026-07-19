# APÊNDICE NORMATIVO — DOMÍNIOS E HANDOFFS

## Documento Mestre da Arquitetura V1.0 — LEA-34

## 1. Controle

```text
DOCUMENT_ROLE=NORMATIVE_APPENDIX_OF_DOCUMENT_MASTER
CANONICAL_DOMAINS=16
MANDATORY_HANDOFFS=12
NEW_REQUIREMENT_IDS=0
IMPLEMENTATION_AUTHORIZED=NO
```

Este apêndice torna explícitos, no pacote do Documento Mestre, os contratos dos 16 domínios e dos 12 handoffs aprovados na consolidação cruzada. Ele não cria requisitos ou decisões novas.

## 2. Domínios canônicos — 16/16

| ID | Domínio | Autoridade principal | Responsabilidade central | Bypass proibido |
|---|---|---|---|---|
| DOM-01 | Governança e estado | `PROJECT_RUNTIME_STATE.yaml` | missão, gate, transição e sincronização | declarar merge futuro ou escrever com baseline obsoleto |
| DOM-02 | Configuração, identidade e segredos | configuração resolvida no servidor | capacidades, identidade, allowlists e redaction | publicar segredo ou armar Modo B por flag isolada |
| DOM-03 | Persistência, eventos e recovery | fronteira única de escrita | integridade, outbox, backup, restore e rollback | escrita direta por cliente ou schema sem fluxo/teste |
| DOM-04 | Listas e agendamentos | domínio de listas no servidor | revisões, validações e contexto de agenda | produzir sinal, grant ou chamar adaptador |
| DOM-05 | Clientes e presença humana | servidor para estado global | pareamento, revogação, snapshot e confirmação | tornar cache autoridade ou presença grant implícito |
| DOM-06 | Perfis, ROIs e geometria | perfil aprovado e versionado | compatibilidade visual e alvo lógico | coordenada virar autorização ou dispatch |
| DOM-07 | Sessão de observação | estado da sessão no servidor | vincular fonte visual e degradar por perda de identidade | escolher fonte desconhecida ou produzir comando |
| DOM-08 | Captura e proveniência | referência de frame com linhagem | hash, origem, sequência, ROI e retenção | frame sem proveniência alimentar análise |
| DOM-09 | Validação e qualidade | resultado de checks visuais | elegibilidade, blockers e caps | tratar `UNKNOWN` como aprovação |
| DOM-10 | Extração e dados estimados | resultado de extração versionado | OCR, mappings, incerteza e linhagem | dado estimado virar dado oficial |
| DOM-11 | Análise A–H | snapshot e resultados imutáveis | motores determinísticos e evidências | análise chamar adaptador ou criar grant |
| DOM-12 | Estratégia e sinais | lifecycle versionado | candidato, arbitragem, sinal e expiração | sinal autoexecutar ou escolher alvo de UI |
| DOM-13 | Comando e autorização | policy engine e grant explícito | comando imutável, limites e revalidação | presença ou sinal virar autorização automática |
| DOM-14 | Alvo e adaptadores | alvo lógico allowlisted + capability | `NULL`, `SIMULATED`, `CONTROLLED_UI` e futuro LIVE gated | coordenada isolada ou UI fora do adaptador |
| DOM-15 | Dispatch e reconciliação | estado reconciliado do servidor | intent-before-effect, recibo, retry seguro e recovery | timeout virar ausência de efeito ou restart reenviar |
| DOM-16 | Segurança e contenção | política + auditoria append-only | redaction, observabilidade, parada de emergência e provas negativas | bypass de fronteira ou LIVE sem gates |

## 3. Handoffs obrigatórios — 12/12

| ID | Origem → destino | Contrato mínimo | Falha obrigatória | Seções do Documento Mestre |
|---|---|---|---|---|
| H-01 | DOM-04 → DOM-07 | lista/agendamento fornece contexto versionado | contexto inválido não inicia sessão | DM-08 → DM-11 |
| H-02 | DOM-06 → DOM-07 | perfil, aplicação, monitor e ROIs aprovados | incompatibilidade bloqueia observação | DM-10 → DM-11 |
| H-03 | DOM-07 → DOM-08 | sessão ativa autoriza captura da fonte identificada | fonte perdida rejeita frame | DM-11 |
| H-04 | DOM-08 → DOM-09 | frame possui hash, origem, sequência e linhagem | frame sem proveniência é rejeitado | DM-11 → DM-12 |
| H-05 | DOM-09 → DOM-10 | somente frame elegível alimenta extração | `FAIL` ou blocker impede extração | DM-12 |
| H-06 | DOM-10 → DOM-11 | dados estimados carregam incerteza e linhagem | mapping incompatível bloqueia snapshot | DM-12 → DM-13 |
| H-07 | DOM-11 → DOM-12 | resultados A–H e caps são imutáveis | motor H não contorna blocker | DM-13 |
| H-08 | DOM-12 → DOM-13 | sinal válido, elegível e não expirado | sinal não vira comando automaticamente | DM-13 → DM-14 |
| H-09 | DOM-13 → DOM-14 | comando e grant vinculam alvo, ação, canal e allowlist | grant incompatível bloqueia resolução | DM-14 → DM-15 |
| H-10 | DOM-14 → DOM-15 | alvo resolvido, allowlisted e adaptador capaz | alvo desconhecido bloqueia dispatch | DM-15 → DM-16 |
| H-11 | DOM-15 → DOM-16 | tentativa e recibo sempre produzem auditoria correlacionada | lacuna bloqueia recovery seguro | DM-16 → DM-17 |
| H-12 | DOM-16 → DOM-13/15 | parada de emergência, circuito e política dominam arming e dispatch | estado inseguro cancela e interrompe o fluxo | DM-17 → DM-14/DM-16 |

## 4. Caminho ponta a ponta

```text
LIST_OR_SCHEDULE_CONTEXT
--H-01-->
OBSERVATION_SESSION
--H-03-->
FRAME_WITH_PROVENANCE
--H-04-->
VALIDATION_RESULT
--H-05-->
ESTIMATED_DATA_WITH_LINEAGE
--H-06-->
ANALYSIS_A_TO_H
--H-07-->
VERSIONED_SIGNAL
--H-08-->
COMMAND_AND_EXPLICIT_GRANT
--H-09-->
ALLOWLISTED_TARGET_AND_ADAPTER
--H-10-->
DISPATCH_AND_RECONCILIATION
--H-11-->
AUDIT_AND_CONTAINMENT
--H-12-->
POLICY_DOMINATES_ARMING_AND_DISPATCH
```

H-02 fornece a compatibilidade geométrica da sessão. H-12 é transversal e pode bloquear ou interromper o fluxo em qualquer ponto crítico.

## 5. Gates

```text
CANONICAL_DOMAINS_EXPLICIT=16/16
MANDATORY_HANDOFF_CONTRACTS_EXPLICIT=12/12
HANDOFF_FAILURE_BEHAVIOR_EXPLICIT=12/12
FORBIDDEN_BYPASS_PATHS_PRESERVED=PASS_BUILDER
NEW_REQUIREMENT_IDS=0
INDEPENDENT_CRITICAL_REVIEW=REQUIRED
```
