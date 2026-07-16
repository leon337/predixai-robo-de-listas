# PREDIXAI ROBÔ DE LISTAS — SKILLS OFICIAIS

## Finalidade

As Skills são comandos curtos que acionam protocolos completos. Elas não dependem de checkpoint colado, upload manual ou memória informal de chat.

## Skills operacionais

### `iniciar`
Ler GitHub e Linear, reconstruir o estado, confirmar missão, fase, gates, bloqueios, próxima ação e proibições.

### `missão`
Mostrar objetivo da missão ativa, entregas, submissões, gates e condição de conclusão.

### `continuar`
Executar automaticamente a próxima ação autorizada da missão sem solicitar confirmação trivial.

### `estado`
Mostrar estado oficial da `main`, estado operacional no Linear e divergências existentes.

### `painel`
Exibir visão gamificada curta: campanha, missão, fase, progresso real, riscos e próxima Skill.

### `roadmap`
Ler o tronco multichat e mostrar etapas, revisões críticas e bloqueios.

### `fontes`
Listar documentos vivos, históricos, evidências, commit e issue Linear que governam a etapa.

### `evidências`
Mostrar as provas que sustentam uma conclusão e o nível de certeza.

### `riscos`
Executar varredura de escopo, arquitetura, documentação, segurança, dependências e avanço indevido.

### `revisar`
Executar revisão crítica formal da etapa ou proposta ativa, classificar falhas e emitir decisão.

### `validar`
Comparar o resultado com os gates objetivos e declarar PASS, WARN, FAIL ou BLOCKED.

### `sincronizar`
Comparar e alinhar GitHub, Linear e documentos vivos antes do avanço.

### `mini`
Criar mini-PTP interna sem trocar a missão principal.

### `md`
Criar ou atualizar Markdown diretamente no GitHub por branch e PR.

### `checkpoint`
Registrar pausa, bloqueio ou continuidade da mesma missão diretamente no GitHub e Linear. Não gerar arquivo para transporte manual.

### `handoff`
Preparar automaticamente o próximo chat: atualizar estado, tronco, Linear e missão seguinte.

### `fechar`
Concluir a missão, validar gates, publicar documentos, integrar PR, atualizar Linear e desbloquear a próxima etapa.

### `saúde`
Mostrar saúde do chat, risco de contexto, sincronização e capacidade de continuar.

### `aprovar`
Aceitar a recomendação apresentada em gate crítico.

### `reprovar`
Recusar a recomendação e registrar justificativa e impacto.

### `pausar`
Interromper a missão preservando estado e próxima ação.

## Autonomia padrão

```text
CONTINUE_AUTOMATICALLY=YES
STOP_ONLY_ON=CRITICAL_BLOCKER|IRREVERSIBLE_ACTION|COST|LEGAL_OR_COMMERCIAL_DECISION|SCOPE_CHANGE|UNAUTHORIZED_CODE_CHANGE|MISSION_COMPLETE
```

## Modos de resposta por Skill

- modo rápido: `estado`, `saúde`, `painel`, `fontes`, `roadmap`;
- modo missão: `iniciar`, `missão`, `continuar`, `mini`;
- modo crítico: `revisar`, `validar`, `riscos`, `evidências`;
- modo entrega: `checkpoint`, `handoff`, `fechar`, `sincronizar`.

## Regra de segurança

Nenhuma Skill autoriza automaticamente alteração de código, SQL, migration, custo, contratação, ação irreversível ou mudança de escopo.
