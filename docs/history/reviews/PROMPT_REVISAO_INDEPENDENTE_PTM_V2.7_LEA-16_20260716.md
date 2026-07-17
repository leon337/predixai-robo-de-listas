# PROMPT — REVISÃO CRÍTICA INDEPENDENTE DA PTM V2.7

## Missão de revisão separada

Executar revisão crítica independente da PTM V2.7 publicada no PR associado à `LEA-16`.

## Fontes obrigatórias

1. PR da `LEA-16`, incluindo todos os arquivos alterados e comentários;
2. `docs/architecture/PTM_V2.7_EXECUCAO_CONTROLADA_GATES_LEA-16_20260716.md`;
3. `docs/architecture/PTM_V2.7_MATRIZ_RASTREABILIDADE_LEA-16_20260716.md`;
4. `docs/history/reviews/AUTO_REVISAO_BUILDER_PTM_V2.7_LEA-16_20260716.md` apenas como evidência preliminar, nunca como autoridade;
5. PTM V2.5 definitiva e matriz;
6. PTM V2.6 definitiva e matriz;
7. Auditoria Mestra V2.4.3-R1, Anexo A e apêndices;
8. revisões críticas independentes das etapas anteriores;
9. `PROJECT_RUNTIME_STATE.yaml`, `PROJECT_STATE.md` e tronco multichat;
10. instruções e protocolos oficiais.

## Objetivo

Determinar se a PTM V2.7 é arquiteturalmente consistente, rastreável, segura, fail-closed e estritamente limitada ao baseline `SIMULATED_ONLY`, sem importar mecanismos legados de clique ou criar autorização implícita para implementação e operação real.

## Verificações obrigatórias

### A. Escopo e fronteira

- confirmar separação V2.5/V2.6/V2.7;
- confirmar que sinal não é comando, autorização ou efeito;
- confirmar que não existe `ARMED_REAL`, modo real configurável, adaptador real ou armazenamento de credenciais reais;
- confirmar que a PTM não autoriza implementação.

### B. Legado e classificação

- confrontar `pynput`, caminhos de clique, `_test_both_coordinates`, coordenadas `LARANJA/CINZA`, runtime guard, monkey patches, diagnóstico, backups e JSON;
- reprovar qualquer tentativa de reutilizar mecanismo físico legado;
- confirmar que coordenadas permanecem apenas metadados geométricos.

### C. State machine

- verificar estados, transições, terminais e contenção;
- procurar transições permissivas, rearmamento automático, sucesso presumido e bypass de `SAFE_IDLE`;
- confirmar ausência de transição para modo real.

### D. Autorização e policy engine

- confirmar autorização explícita, limitada, temporária, revogável e vinculada ao hash do comando;
- verificar se UI/Android pode indevidamente assumir autoridade;
- confirmar reautorização após mutação de contexto, política, adaptador ou comando.

### E. Idempotência, duplicidade e concorrência

- validar chave idempotente, dedupe, serialização e conflitos;
- procurar possibilidade de dispatch duplo, retry paralelo ou repetição após restart;
- confirmar que duplicidade divergente bloqueia.

### F. Timeout, retry e efeito desconhecido

- confirmar que timeout não equivale a falha sem efeito;
- confirmar que retry exige prova de `FAILED_NO_EFFECT`;
- confirmar contenção em `UNKNOWN_EFFECT` e bloqueio de comandos correlatos.

### G. Limites, circuit breaker e kill switch

- confirmar safe defaults e impossibilidade de autoampliação;
- confirmar dominância do kill switch sobre fila, dispatch, retry e rearmamento;
- avaliar risco da topologia local/remota ainda não detalhada.

### H. Recibo, reconciliação e recovery

- confirmar que recibo é evidência, não verdade global;
- validar reconciliação, divergência, compensação e restart;
- confirmar ausência de rollback cego e redespacho automático.

### I. Segurança, privacidade e prova negativa

- confirmar rejeição de senha, cookie, token, chave, tela ou credencial real;
- confirmar redaction, minimização e retenção;
- validar especificação da prova negativa de ponteiro, teclado, clique e ordem.

### J. Rastreabilidade e contagem

- validar os 32 requisitos estruturais e 52 funcionais;
- confirmar 84 IDs únicos;
- confrontar cada linha estrutural com fonte, classificação, destino e evidência;
- verificar cobertura funcional por domínio e ausência de requisito órfão.

## Perguntas hostis mínimas

1. Um sinal pode alcançar dispatch sem autorização humana válida?
2. Um timeout pode causar segundo dispatch enquanto o primeiro efeito é desconhecido?
3. Um cliente móvel pode elevar modo ou confirmar efeito?
4. Uma coordenada pode ser usada diretamente como ação?
5. Um restart pode reenviar comando intermediário?
6. O kill switch pode ser contornado por fila, retry, recovery ou cliente desconectado?
7. Um adaptador pode declarar capacidade desconhecida e continuar?
8. Um recibo divergente pode ser aceito silenciosamente?
9. Existe qualquer texto que possa ser interpretado como GO para clique ou ordem real?
10. Algum requisito depende de threshold numérico sem benchmark?

## Classificação dos achados

```text
CRITICAL=risco de efeito real, duplicidade, bypass de autorização, perda de contenção ou avanço indevido
MAJOR=lacuna arquitetural relevante, requisito sem rastreabilidade ou contrato contraditório
MINOR=clareza, granularidade ou detalhe posterior sem violar segurança/gates
```

## Saída obrigatória

Criar relatório histórico separado contendo:

```text
REVIEW_ISSUE=<LEA-ID>
REVIEWED_PR=<PR-NUMBER>
REVIEWED_PR_HEAD=<SHA>
PTM_V2_7_CRITICAL_REVIEW=PASS|FAIL|BLOCKED
CRITICAL_FINDINGS=<N>
MAJOR_FINDINGS=<N>
MINOR_FINDINGS=<N>
REQUIREMENT_ID_UNIQUENESS=PASS|FAIL
TRACEABILITY_COMPLETENESS=PASS|FAIL
LEGACY_CLASSIFICATION_CONSISTENCY=PASS|FAIL
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS|FAIL
SIMULATED_ONLY_BASELINE=PASS|FAIL
SIGNAL_EXECUTION_SEPARATION=PASS|FAIL
AUTHORIZATION_MODEL=PASS|FAIL
IDEMPOTENCY_AND_DEDUPLICATION=PASS|FAIL
UNKNOWN_EFFECT_CONTAINMENT=PASS|FAIL
KILL_SWITCH_DOMINANCE=PASS|FAIL
REAL_ADAPTER_ABSENCE=PASS|FAIL
REAL_EFFECT_NEGATIVE_PROOF=PASS|FAIL
DOCUMENTAL_READY_FOR_MERGE=YES|NO
```

Cada achado deve informar requisito afetado, evidência, severidade, impacto, correção exigida e condição de reteste.

## Regra de independência

```text
BUILDER_SELF_REVIEW_IS_FINAL_AUTHORITY=NO
INDEPENDENT_REVIEW_MUST_READ_PRIMARY_SOURCES=YES
FINAL_BOSS_GATE_BY_BUILDER_ALONE=PROHIBITED
```

O revisor não pode aprovar apenas porque a auto-revisão declarou `PASS`.