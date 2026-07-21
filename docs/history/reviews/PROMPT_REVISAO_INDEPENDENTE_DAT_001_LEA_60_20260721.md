# Prompt — revisão crítica independente DAT-001 / LEA-60

Execute uma revisão crítica independente da DAT-001. Não confie nas declarações do
builder sem reproduzir ou inspecionar a evidência.

## Alvo obrigatório

```text
REPOSITORY=leon337/predixai-robo-de-listas
PULL_REQUEST=<PR_DRAFT_DAT_001>
BASE_MAIN_SHA=f0faa79c157cbfeae75b620eddb9ccade6000a36
REVIEW_HEAD=<LER_EXTERNAMENTE_NO_PR_E_NA_LEA_60>
BUILDER_ISSUE=LEA-59
REVIEW_ISSUE=LEA-60
MODE_MAX=NULL_ONLY
```

Antes de revisar, confirme que o PR e a LEA-60 fixam o mesmo SHA completo. Pare com
FAIL se divergirem. O SHA não é embutido neste documento porque um commit não pode
referenciar o próprio hash.

## Revisão obrigatória

1. Leia o Documento Mestre, catálogo DAT-001, DOM-03, H-11, os 20 requisitos e
   ADR-0001/0002/0003/0013.
2. Inspecione integralmente o diff, migrations `up/down`, store, configuração,
   serviço, API, testes, workflow, executor e documentos.
3. Comprove escritor único, `BEGIN IMMEDIATE`, versão otimista, idempotência e
   atomicidade estado + outbox.
4. Comprove checksum de migration, FK, WAL/timeout, integridade e rollback somente
   em banco vazio.
5. Comprove backup consistente, hash e restore exclusivo para destino novo.
6. Comprove que a fonte legada não é alterada, que o ledger é idempotente, que
   divergências bloqueiam e que campos sensíveis não persistem em claro.
7. Confirme `aggregate_state=0` após importação: DAT-001 não autoriza cutover nem
   listas autoritativas.
8. Execute toda a suíte, Ruff e Mypy e confirme preservação dos 53 testes anteriores.
9. Valide o relatório Linux Mint contra o mesmo HEAD e registre seu SHA-256.
10. Confirme CI, Draft, GitHub–Linear–estado e ausência de arquivos fora do escopo.

## Limites invioláveis

```text
PRODUCTION_DATABASE=NO
EXISTING_REAL_DATA_MUTATION=NO
IRREVERSIBLE_MIGRATION=NO
DESTRUCTIVE_MIGRATION=NO
LST_001_AUTHORIZED=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

## Saída

Publique no PR e na LEA-60: HEAD revisado, testes, CI, relatório local, achados por
severidade, decisão PASS/FAIL e próximo gate. Não aprove o próprio trabalho, não
promova o PR e não faça merge.
