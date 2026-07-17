# PROMPT — REVISÃO CRÍTICA INDEPENDENTE DA PTM V2.6

## LEA-15 / PR #35

Atue como revisor crítico independente. Não aceite a auto-revisão do builder como Boss Gate.

## Fontes obrigatórias

1. PR `#35`, incluindo todos os arquivos alterados e discussão;
2. `docs/architecture/PTM_V2.6_OBSERVACAO_ANALISE_SINAIS_LEA-14_20260716.md`;
3. `docs/architecture/PTM_V2.6_MATRIZ_RASTREABILIDADE_LEA-14_20260716.md`;
4. `docs/history/reviews/AUTO_REVISAO_BUILDER_PTM_V2.6_LEA-14_20260716.md` apenas como evidência preliminar;
5. PTM V2.5 definitiva e matriz de rastreabilidade;
6. Auditoria Mestra, adendo e revisão crítica aprovados;
7. `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md`;
8. `PROJECT_RUNTIME_STATE.yaml`, `PROJECT_STATE.md`, tronco e Linear `LEA-14`/`LEA-15`.

## Missão

Determinar se a PTM V2.6 está completa, coerente, rastreável, segura e estritamente limitada a observação, análise e sinais simulados.

## Verificações obrigatórias

### A. Integridade documental

- confirmar `28` requisitos estruturais;
- confirmar `50` requisitos funcionais;
- confirmar `78` IDs totais;
- detectar duplicidades, lacunas e referências órfãs;
- confrontar arquitetura, matriz, PR, runtime state, PROJECT_STATE, tronco e Linear.

### B. Fronteira de versão

- V2.5 deve permanecer fundação e migração segura;
- V2.6 deve terminar em sinal simulado e evidência;
- V2.7 deve concentrar qualquer execução futura;
- nenhum requisito V2.6 pode produzir movimento, clique, ordem, saldo ou resultado físico.

### C. Observação

- fonte visual autorizada e fail-closed;
- identidade de janela/processo;
- perfil, monitor, escala, ROI e assinatura compatíveis;
- proveniência, hash, sequence, tempo e retenção de frames;
- oclusão, frescor, duplicidade, ordem e estabilidade.

### D. Qualidade e confiança

- dimensões separadas;
- blockers dominantes;
- `UNKNOWN` não aumenta elegibilidade;
- caps monotônicos e conservadores;
- score agregado não contorna falha;
- thresholds permanecem provisórios até benchmark.

### E. Análise A–H

- contratos de entrada e saída claros;
- envelope comum, versões e hashes;
- evidências e reason codes;
- ausência de estado oculto não versionado;
- determinismo ou divergência explicada;
- Motor H não contorna blockers A–G.

### F. Strategy-001 e sinais

- estratégia explicável;
- candidato diferente de sinal;
- arbitragem determinística;
- fingerprint e validade;
- expiração, invalidação e supersessão;
- nenhum estado físico como `CLIQUE_ENVIADO` ou `EXECUTADO`.

### G. Contratos, persistência e replay

- existência progressiva por produtor, consumidor, requisito, teste e retenção;
- REST/eventos conceituais não tratados como implementação;
- SQL, migrations e schema físico ausentes;
- replay sanitizado, offline e sem fonte real.

### H. Segurança

- minimização e redaction;
- ausência de segredos ou imagens não sanitizadas em commits;
- dependências de captura/OCR isoladas por adaptador e feature gate;
- prova negativa de ponteiro, teclado, clique e ordem.

## Classificação de achados

- `CRITICAL`: permite execução real, quebra escopo/segurança, perda de rastreabilidade ou conclusão inválida;
- `MAJOR`: requisito ambíguo, lacuna de lifecycle/qualidade/contrato, contagem ou matriz inconsistente;
- `MINOR`: clareza, nomenclatura ou melhoria sem comprometer o gate.

## Saída obrigatória

Registrar revisão no GitHub e comentar o PR `#35` com:

```text
PTM_V2_6_CRITICAL_REVIEW=PASS|FAIL
REQUIREMENT_ID_UNIQUENESS=PASS|FAIL
TRACEABILITY_COMPLETENESS=PASS|FAIL
LEGACY_CLASSIFICATION_CONSISTENCY=PASS|FAIL
V2_5_V2_6_V2_7_SCOPE_SEPARATION=PASS|FAIL
AUTHORIZED_VISUAL_SOURCE_FAIL_CLOSED=PASS|FAIL
QUALITY_MODEL_AND_CONFIDENCE_CAPS=PASS|FAIL
ANALYSIS_ENGINE_A_H_CONTRACTS=PASS|FAIL
STRATEGY_AND_SIGNAL_LIFECYCLE=PASS|FAIL
PROGRESSIVE_CONTRACT_EXISTENCE=PASS|FAIL
SAFE_REPLAY=PASS|FAIL
VISUAL_DATA_SECURITY=PASS|FAIL
REAL_INPUT_AND_EXECUTION_EXCLUSION=PASS|FAIL
STATE_DOCUMENTATION_ALIGNMENT=PASS|FAIL
CRITICAL_BLOCKERS=<n>
MAJOR_FINDINGS=<n>
MINOR_FINDINGS=<n>
READY_FOR_MERGE=YES|NO
```

Se houver `CRITICAL` ou `MAJOR`, solicitar alterações e manter o PR em draft. Não iniciar PTM V2.7.