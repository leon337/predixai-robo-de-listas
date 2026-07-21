# Prompt — revisão independente do hotfix de versão / LEA-102

Execute uma revisão independente do hotfix de promoção para V2.5.0-alpha.2.
Não confie nas declarações do builder sem inspecionar o diff e a evidência.

## Alvo

```text
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=73
BASE_MAIN_SHA=bd2db3772898c46d9422818b780e91b5f132941e
REVIEW_HEAD=<LER_EXTERNAMENTE_NO_PR_73_E_NA_LEA_102>
BUILDER_ISSUE=LEA-101
REVIEW_ISSUE=LEA-102
MODE_MAX=NULL_ONLY
```

O SHA final deve ser fixado externamente no PR #73 e na LEA-102. Não embuta o SHA
do próprio commit dentro deste documento.

## Revisão obrigatória

1. Confirmar `VERSION=2.5.0-alpha.2`.
2. Confirmar que `run.sh` executa `app/bootstrap_v250_alpha2_entry.py`.
3. Confirmar que a entrada nova é sintaticamente válida e delega exclusivamente para
   `bootstrap_v23_entry.run`.
4. Revisar `scripts/validate_version_floor.py` e comprovar precedência SemVer,
   rejeição de versões inválidas e comparação correta entre prerelease e release.
5. Confirmar que os oito workflows históricos preservam suas verificações funcionais
   e alteram somente a validação de versão para pisos SemVer.
6. Confirmar que nenhuma lógica de runtime, corretora, clique, efeito financeiro,
   SIMULATED, CONTROLLED_UI ou LIVE foi adicionada.
7. Executar toda a suíte cumulativa e confirmar oito testes novos: três de promoção e
   cinco do validador SemVer.
8. Executar Ruff e Mypy e confirmar todos os workflows do HEAD final.
9. Confirmar PR Draft e alinhamento GitHub–Linear–documentação.
10. Publicar PASS ou FAIL no PR #73 e na LEA-102.

## Limites

```text
LST_001_AUTHORIZED=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

Não promover nem mesclar o PR.
