# PROMPT — REVISÃO CRÍTICA INDEPENDENTE DA LEA-50

```text
BUILDER_ISSUE=LEA-50
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=0968ae86e92e7b640cbcc77941d49a9474839650
BRANCH=leonpcsn/lea-50-roadmap-implementacao-v1
REVIEW_HEAD=PINNED_EXTERNALLY_IN_LINEAR_REVIEW_ISSUE_AND_PR_DRAFT_AFTER_FINAL_COMMIT
BUILDER_MUST_NOT_REVIEW=YES
MERGE_AUTHORIZED=NO
IMPLEMENTATION_AUTHORIZED=NO
```

Atue como revisor crítico independente. Leia todos os arquivos alterados entre a base e o `REVIEW_HEAD` exato indicado na issue Linear e no PR Draft. Não edite o trabalho do builder, não aprove merge e não autorize implementação.

## Validar

1. cobertura real e individual `218/218`;
2. `16/16` domínios, `12/12` handoffs e `18/18` ADRs sem criação nova;
3. ausência de mudança da Arquitetura V1.0;
4. sequência completa, coerente e derivada das dependências;
5. grafo sem ciclos, referências desconhecidas ou dependências ausentes;
6. nenhum incremento sem fundamento normativo;
7. critérios objetivos de entrada e saída, rollback e validação local;
8. regressão cumulativa e fluxo 1→N;
9. versionamento sem renumeração retroativa de FND-001/FND-002;
10. gate de dívida técnica bloqueando riscos críticos;
11. progressão `NULL_ONLY→SIMULATED→CONTROLLED_UI→LIVE_GATED` sem liberação automática;
12. ausência de roadmap paralelo: Documento Mestre continua autoridade;
13. próxima unidade inequívoca e ainda não autorizada;
14. alinhamento entre GitHub, Linear e estado oficial;
15. ausência de código de aplicação, teste do produto, SQL, migration ou runtime executado.

## Comando documental

```bash
python3 scripts/validate_lea50_documental.py
```

## Decisão permitida

```text
PASS
PASS_WITH_CONDITIONS
FAIL
```

Registrar severidade, evidência, impacto e correção para cada achado. `PASS` exige zero achado crítico, zero major e zero bloqueador aberto.

