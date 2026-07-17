# PROMPT DE REVISÃO INDEPENDENTE — PTM V2.5

## LEA-8 — Reconciliação factual com o legado V2.4.3-R1

Atue como revisor crítico independente. Não confie na auto-revisão do builder e não altere código.

## Escopo obrigatório

Repositório exclusivo:

```text
leon337/predixai-robo-de-listas
```

Branch/PR a revisar:

```text
BRANCH=leonpcsn/lea-8-reconciliar-e-revisar-ptm-v25
BASE_MAIN_SHA=7f7434ffd9f9424ab929ad6afe7d1fc76e1d67c9
```

Artefatos principais:

1. `docs/architecture/PTM_V2.5_RECONCILIADA_LEA-8_20260716.md`;
2. `docs/architecture/PTM_V2.5_MATRIZ_RASTREABILIDADE_LEA-8_20260716.md`;
3. `docs/history/reviews/AUTO_REVISAO_BUILDER_PTM_V2.5_LEA-8_20260716.md`;
4. `PROJECT_RUNTIME_STATE.yaml`;
5. `PROJECT_STATE.md`;
6. `PREDIXAI_ROBO_LISTAS_TRONCO_MULTICHAT.md`.

Fontes factuais de confronto:

1. `docs/audits/ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md`;
2. Apêndices 01–04 do Anexo A;
3. `docs/audits/ADENDO_REMEDIACAO_PTP-GOV.6-RC_EVIDENCIA_ESTADO_RASTREABILIDADE_20260716.md`;
4. `docs/history/reviews/REVISAO_CRITICA_AUDITORIA_MESTRA_PTP-GOV.6_20260716.md`;
5. `docs/history/ptp/ANEXO_CONTRATOS_PTM_SCHEMA_PTP-GOV.5_20260716.md`;
6. `docs/history/ptp/HANDOFF_PTP-GOV.6-RC_PARA_PTM_V2.5_20260716.md`;
7. issue Linear `LEA-8`.

## Perguntas obrigatórias

1. Os 29 requisitos estruturais preliminares foram reconciliados sem omissão?
2. Os 23 requisitos funcionais preliminares foram reconciliados sem omissão?
3. Os 56 IDs registrados são únicos e rastreáveis?
4. Fonte, caminho, classificação, certeza, risco, decisão e status estão presentes por requisito?
5. A arquitetura futura foi separada corretamente dos fatos do legado?
6. JSON schema 4 foi preservado apenas como fonte de migração e rejeitado como autoridade final?
7. A cadeia de monkey patches foi corretamente marcada para substituição sem perder comportamentos úteis?
8. Click targets foram tratados apenas como geometria?
9. Movimento do ponteiro, clique real e execução física estão excluídos da V2.5?
10. R0–R2 estão separados de R3–R4?
11. V2.5, V2.6 e V2.7 possuem fronteiras coerentes?
12. O catálogo lógico foi impedido de virar schema físico automático?
13. Os quatro requisitos adicionais são necessários, bem fundamentados e pertencem à V2.5?
14. Algum requisito adicional deve ser ajustado, dividido, rejeitado ou movido de versão?
15. Contratos, estados, lifecycle, persistência, segurança, observabilidade e recovery estão suficientemente definidos para a etapa arquitetural?
16. Há contradição entre manifesto, `PROJECT_STATE`, tronco, PR e Linear?
17. Alguma frase declara implementação, runtime, SQL, migration ou teste como concluído sem evidência?
18. O draft está pronto para integração documental ou exige remediação?

## Critérios de bloqueio crítico

Considere bloqueador crítico qualquer ocorrência de:

- mistura com outro repositório;
- omissão de requisito-base;
- perda de rastreabilidade factual;
- clique real ou movimento de ponteiro autorizado na V2.5;
- JSON mantido como fonte final de verdade;
- monkey patching mantido como arquitetura futura;
- avanço implícito para V2.6/V2.7;
- schema físico transformado em compromisso automático;
- implementação, SQL ou migrations tratados como autorizados;
- auto-revisão do builder usada como Boss Gate;
- divergência operacional insolúvel entre GitHub e Linear.

## Saída obrigatória

Produza um documento formal contendo:

```text
REVIEW_STATUS=FINAL
REVIEW_TYPE=INDEPENDENT_CRITICAL_REVIEW
MISSION=LEA-8-RC
PTM_V2_5_CRITICAL_REVIEW=PASS|FAIL
CRITICAL_BLOCKERS=<n>
MAJOR_FINDINGS=<n>
MINOR_FINDINGS=<n>
REQUIREMENT_ID_UNIQUENESS=PASS|FAIL
TRACEABILITY_COMPLETENESS=PASS|FAIL
LEGACY_FUTURE_SEPARATION=PASS|FAIL
SCOPE_V2_5_V2_6_V2_7_SEPARATION=PASS|FAIL
REAL_CLICK_EXCLUSION=PASS|FAIL
JSON_MIGRATION_BOUNDARY=PASS|FAIL
PATCH_CHAIN_REPLACEMENT=PASS|FAIL
PHYSICAL_SCHEMA_PROGRESSIVENESS=PASS|FAIL
ADDITIONAL_REQUIREMENTS_DECISION=ACCEPT|ACCEPT_WITH_CHANGES|REJECT
READY_FOR_MERGE=YES|NO
```

Para cada achado, informe:

- severidade;
- arquivo e seção;
- evidência;
- impacto;
- correção objetiva;
- condição de resolução.

Não faça merge. Não altere código. Não avance para PTM V2.6. O builder não pode emitir o Boss Gate final.