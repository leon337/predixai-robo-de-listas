# PREDIXAI ROBÔ DE LISTAS — INSTRUÇÕES OFICIAIS DO PROJETO

## 1. Identificação

- Projeto: PredixAI Robô de Listas
- Repositório oficial: `leon337/predixai-robo-de-listas`
- Branch oficial: `main`
- Versão real atual: `V2.4.3-R1`
- Fonte técnica e documental: GitHub
- Gestão operacional: Linear
- Ambiente de análise e engenharia: ChatGPT
- Estado atual: suite de memória concluída; Auditoria Mestra liberada
- Implementação V2.5: não autorizada

## 2. Finalidade desta pasta de Projeto

Esta pasta existe exclusivamente para concluir a Auditoria Mestra do legado V2.4.3-R1, as PTMs V2.5, V2.6 e V2.7, suas revisões críticas, a consolidação arquitetural, os ADRs e o Documento Mestre.

Não usar esta pasta para outros repositórios, outros produtos PredixAI, operações reais, experimentos paralelos ou tarefas não relacionadas ao PredixAI Robô de Listas.

## 3. Autoridade e precedência

Em caso de divergência, aplicar esta ordem:

1. código e arquivos reais da branch `main`;
2. `PROJECT_STATE.md`;
3. documento vigente da PTP ou PTM ativa;
4. evidências e relatórios publicados em `docs/`;
5. estado operacional correspondente no Linear;
6. contexto do chat.

O histórico de chat nunca substitui o GitHub.

## 4. Ordem obrigatória de leitura

1. `PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md`
2. `PROJECT_STATE.md`
3. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`
4. documento da PTP ou PTM ativa;
5. revisão crítica mais recente;
6. evidências indicadas pelo `PROJECT_STATE.md`;
7. código e documentação técnica da branch `main`, quando necessário.

Antes de trabalhar, confirmar repositório, branch, commit, versão real, etapa ativa, concluído, pendente, bloqueado, próxima ação e proibições.

## 5. Isolamento de escopo

Fonte autorizada: `leon337/predixai-robo-de-listas`.

É proibido usar como fonte:

- `leon337/predixai-platform`;
- outros repositórios PredixAI;
- conclusões de chats sem evidência no GitHub;
- arquivos locais não publicados;
- hipóteses tratadas como fatos do legado.

## 6. Legado real versus arquitetura futura

`V2.4.3-R1` representa o software existente e deve ser confirmado por evidência real.

`V2.5–V2.7` representa arquitetura planejada:

- PTM V2.5: preliminar até reconciliação;
- PTM V2.6: não iniciada;
- PTM V2.7: não iniciada.

## 7. Fluxo obrigatório

```text
INVESTIGAR
→ DOCUMENTAR
→ REVISAR CRITICAMENTE
→ CORRIGIR
→ VALIDAR
→ PUBLICAR
→ ATUALIZAR PROJECT_STATE
→ ATUALIZAR TRONCO MULTICHAT
→ ATUALIZAR LINEAR
→ INTEGRAR NA MAIN
→ GERAR CHECKPOINT
→ AVANÇAR
```

Nenhuma etapa avança apenas porque um documento foi produzido.

## 8. Revisões críticas obrigatórias

Toda etapa principal possui revisão crítica independente:

- Auditoria Mestra + Anexo A;
- PTM V2.5;
- PTM V2.6;
- PTM V2.7;
- consolidação cruzada;
- ADRs;
- Documento Mestre;
- prontidão para implementação.

A revisão deve verificar completude, consistência, aderência ao legado, conflitos, omissões, dependências, riscos, gates, rastreabilidade e condição de avanço.

## 9. Documentos vivos e históricos

Documentos vivos:

- `PROJECT_STATE.md`;
- este documento;
- `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`;
- documento da etapa ativa;
- roadmap operacional.

Documentos históricos são imutáveis. Correções devem ocorrer por adendo ou novo documento.

## 10. Sincronização GitHub–Linear–ChatGPT

Antes de avançar:

### GitHub
- documento principal publicado;
- revisão crítica publicada;
- evidências publicadas;
- `PROJECT_STATE.md` atualizado;
- tronco atualizado;
- PR integrada na `main`.

### Linear
- tarefa no estado correto;
- bloqueios atualizados;
- links para PR e documentos;
- próxima tarefa liberada apenas após os gates.

### ChatGPT
- fontes essenciais atualizadas;
- um chat por etapa principal;
- sem contexto de outros projetos.

## 11. Evidência mínima da Auditoria Mestra

```text
FONTE
CAMINHO
BRANCH_OU_COMMIT
ACHADO
CLASSIFICAÇÃO=REUTILIZAR|ADAPTAR|SUBSTITUIR|DESCONTINUAR
NÍVEL_DE_CERTEZA
EVIDÊNCIA
RASTREABILIDADE_PTM
RISCO
PENDÊNCIA
```

## 12. Proibições atuais

- não iniciar implementação V2.5;
- não alterar código durante a Auditoria Mestra;
- não gerar SQL ou migrations;
- não tratar PTM preliminar como definitiva;
- não misturar legado e futuro;
- não avançar sem revisão crítica;
- não iniciar outra etapa principal no mesmo chat;
- não usar outro repositório.

## 13. Gate universal de saída

```text
DOCUMENTO_PRINCIPAL=PASS
REVISAO_CRITICA=PASS
PENDENCIAS_CRITICAS=ZERO
PROJECT_STATE_ATUALIZADO=PASS
TRONCO_MULTICHAT_ATUALIZADO=PASS
LINEAR_ATUALIZADO=PASS
PR_MERGED=PASS
CHECKPOINT_GERADO=PASS
```

## 14. Prompt-base

```text
Use exclusivamente o conector GitHub.

Projeto: PredixAI Robô de Listas
Repositório: leon337/predixai-robo-de-listas
Branch: main

Leia:
1. PREDIXAI_ROBO_LISTAS_PROJECT_INSTRUCTIONS.md
2. PROJECT_STATE.md
3. PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md
4. documento da etapa ativa
5. revisão crítica e evidências indicadas

Confirme repositório, branch, commit, versão, etapa ativa, concluído, pendente, bloqueado, próxima ação e proibições.

Não use outro repositório.
Não implemente.
Não gere SQL ou migrations.
Não avance sem revisão crítica, publicação e sincronização.
```