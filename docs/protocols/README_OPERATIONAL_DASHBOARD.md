# PROTOCOLO DO PAINEL OPERACIONAL README

## 1. Status

```text
DOCUMENT_STATUS=NORMATIVE_ACTIVE
PROTOCOL=README_OPERATIONAL_DASHBOARD
OWNER=LEO
BUILDER_ISSUE=LEA-20
REPOSITORY=leon337/predixai-robo-de-listas
TARGET_BRANCH=main
```

## 2. Finalidade

O `README.md` é a primeira página operacional do projeto no GitHub e deve permitir auditoria à vista, principalmente no aplicativo móvel.

Ele responde sem navegação adicional:

```text
Onde o projeto está?
Qual é a versão real?
O que já foi concluído?
O que está em andamento?
Qual é o gate atual?
Quais bloqueios estão abertos?
O que falta até os ADRs?
O que falta até o Documento Mestre?
Qual é a próxima ação?
```

## 3. Autoridade

O README é uma projeção pública derivada. Ele não substitui:

1. `PROJECT_RUNTIME_STATE.yaml`;
2. `PROJECT_STATE.md`;
3. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
4. Linear;
5. PR e branch ativos;
6. GitHub `main` para trabalho integrado.

```text
README_IS_CANONICAL_AUTHORITY=NO
README_IS_REQUIRED_PUBLIC_PROJECTION=YES
```

## 4. Primeira dobra obrigatória

A parte inicial do README deve exibir:

```text
REAL_VERSION
ACTIVE_MISSION
ACTIVE_REVIEW
ACTIVE_PULL_REQUEST
PR_STATUS
CURRENT_PHASE
CURRENT_GATE
CRITICAL_FINDINGS
MAJOR_FINDINGS
MINOR_FINDINGS
MERGE_AUTHORIZED
ADRS_AUTHORIZED
IMPLEMENTATION_AUTHORIZED
```

Informação histórica ou instrução de instalação não pode aparecer antes do estado operacional.

## 5. Mapa obrigatório da campanha

O painel deve mostrar, no mínimo:

```text
AUDITORIA MESTRA
→ PTM V2.5
→ PTM V2.6
→ PTM V2.7
→ CONSOLIDAÇÃO CRUZADA
→ ADRs
→ DOCUMENTO MESTRE
→ REVISÃO CRÍTICA
→ ARQUITETURA V1.0 CONGELADA
→ PRONTIDÃO PARA IMPLEMENTAÇÃO
```

Cada etapa usa somente estados reais:

```text
✅ concluída
🟨 em andamento
🟧 etapa atual
⏳ aguardando
🟦 auditada
🟪 pausada
🟥 falha
⛔ bloqueada
⬜ não iniciada
🚀 publicada
```

## 6. Conteúdo obrigatório

O README deve conter seções para:

1. estado atual;
2. mapa da campanha;
3. progresso visual;
4. entregas concluídas;
5. bloqueios abertos;
6. caminho até os ADRs;
7. caminho até o Documento Mestre;
8. política de automação A+B;
9. fontes oficiais;
10. próxima ação;
11. legado executável, quando existir.

## 7. Progresso

Percentuais e barras representam gates ou entregas reais. Não usar progresso arbitrário.

```text
README_PROGRESS_SOURCE=REAL_GATES_AND_DELIVERABLES
ARBITRARY_PROGRESS=PROHIBITED
```

## 8. Política de automação visível

O painel deve mostrar a síntese da política vigente:

```text
MODE_A=CONTROLLED_OR_SIMULATED_ALLOWED
MODE_B=SUPPORTED_BY_SEPARATE_LIVE_GATE
MODE_B_DEFAULT=DISABLED
```

Não reproduzir proibições globais supersedidas contra análise de gráficos, captura, OCR, replay, ponteiro, teclado, preenchimento, clique ou autenticação controlada.

## 9. Conteúdo legado

Instalação, execução e recursos históricos permanecem disponíveis, mas abaixo do painel e identificados como legado.

```text
LEGACY_CONTENT_PRESERVED=YES
LEGACY_CONTENT_PRESENTED_AS_CURRENT_STATE=NO
```

## 10. Gatilhos de sincronização

Revisar e atualizar o README quando ocorrer qualquer alteração em:

- versão real;
- missão ou revisão ativa;
- branch ou PR ativo;
- fase ou gate;
- progresso;
- achados e bloqueios;
- autorização de merge, ADRs ou implementação;
- política de automação;
- próxima ação;
- roadmap até o Documento Mestre.

## 11. Skills que exigem verificação

```text
continuar
estado
painel
roadmap
revisar
validar
sincronizar
checkpoint
handoff
fechar
aprovar
reprovar
pausar
```

## 12. PR ativo e branch main

O aplicativo GitHub exibe por padrão o README da `main`.

Trabalho em PR ainda não integrado pode ser refletido no painel como estado transitório, desde que identificado:

```text
ACTIVE_WORK_SOURCE=PR_AND_LINEAR
INTEGRATION_STATUS=UNMERGED
SNAPSHOT_TIMESTAMP_REQUIRED=WHEN_AMBIGUOUS
```

O README não deve declarar como integrado aquilo que existe apenas no PR.

## 13. Drift e falha

Quando o README divergir das fontes vivas:

```text
README_STATE_DRIFT=YES
README_SYNC_STATUS=FAIL
PUBLIC_DELIVERY_STATUS=BLOCKED
CANONICAL_STATE_AUTHORITY=PRESERVED
```

Correção do painel não altera fatos históricos nem inventa estado novo.

## 14. Condição de checkpoint

```text
README_CURRENT_STATE_REVIEWED=YES
README_UPDATE_REQUIRED=YES|NO
README_SYNC_STATUS=PASS
```

Quando `README_UPDATE_REQUIRED=YES`, o checkpoint não pode ser declarado publicamente completo antes da atualização.

## 15. Condição de fechamento

```text
PROJECT_RUNTIME_STATE_SYNC=PASS
PROJECT_STATE_SYNC=PASS
TRUNK_SYNC=PASS
LINEAR_SYNC=PASS
README_SYNC=PASS
```

Sem esses cinco resultados, a missão permanece aberta ou parcialmente sincronizada.

## 16. Leitura mobile-first

- títulos curtos;
- blocos de código estreitos;
- evitar tabelas largas quando houver alternativa;
- estado atual antes do histórico;
- bloqueios e próxima ação visíveis;
- listas divididas por etapa;
- links relativos para documentos do repositório;
- nenhuma informação essencial apenas em imagem.

## 17. Gates de aceitação

```text
README_OPERATIONAL_DASHBOARD=PASS
README_VERSION_SYNC=PASS
README_MISSION_SYNC=PASS
README_PHASE_SYNC=PASS
README_GATE_SYNC=PASS
README_PROGRESS_SYNC=PASS
README_COMPLETED_WORK_VISIBLE=PASS
README_BLOCKERS_SYNC=PASS
README_PATH_TO_MASTER_DOCUMENT=PASS
README_AUTOMATION_POLICY_SYNC=PASS
README_NEXT_ACTION_SYNC=PASS
README_LEGACY_SEPARATION=PASS
MOBILE_FIRST_READABILITY=PASS
```

## 18. Regra final

A primeira página do GitHub deve funcionar como mapa do projeto.

```text
PAST=COMPLETED_WORK
PRESENT=MISSION_PHASE_GATE_BLOCKERS
FUTURE=ADRS_MASTER_DOCUMENT_ARCHITECTURE_IMPLEMENTATION
```