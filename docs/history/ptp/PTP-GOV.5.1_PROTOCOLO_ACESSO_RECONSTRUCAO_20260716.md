# PTP-GOV.5.1 — Protocolo Acesso → Reconstrução

## Identificação

- **PTP principal:** `PTP-GOV.5 — Memória e Governança Documental`
- **Mini-PTP:** `PTP-GOV.5.1`
- **Nome curto:** Acesso antes da reconstrução
- **Projeto:** PredixAI Robô de Listas
- **Repositório:** `leon337/predixai-robo-de-listas`
- **Data:** 2026-07-16
- **Status:** EM ANDAMENTO
- **Substitui:** protocolo de teste único que avaliava acesso e reconstrução simultaneamente

## Objetivo

Corrigir o protocolo de validação da memória após o primeiro experimento mostrar que um chat pode não possuir acesso técnico ao conteúdo do GitHub. A documentação só pode ser julgada depois que a leitura real dos arquivos for comprovada.

## Evento de origem

O Teste 001 foi executado em chat novo usando apenas o link do repositório. O chat informou que conseguia acessar somente páginas genéricas do GitHub e não conseguia abrir README, PTPs ou arquivos de governança.

Resultado oficial:

```text
TESTE_001=FAIL_POR_FALTA_DE_ACESSO_AO_REPOSITORIO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_INTERPRETACAO=NAO
FALHA_DE_ACESSO=SIM
```

Evidência documental:

`docs/history/tests/TESTE_001_RESULTADO_20260716.md`

## Análise crítica

O teste original possuía duas variáveis independentes:

1. disponibilidade de ferramenta/conector capaz de ler o GitHub;
2. qualidade da documentação para reconstrução do estado.

Como a primeira variável falhou, a segunda não foi testada. Classificar o resultado como simples falha documental seria incorreto.

## Decisão

Fica congelado o protocolo sequencial:

```text
ETAPA A — ACESSO
→ comprovar leitura dos arquivos obrigatórios.

ETAPA B — RECONSTRUÇÃO
→ avaliar estado, concluído, pendências, PTP, próxima ação e proibições.

ETAPA C — CONTINUIDADE
→ confirmar que outro chat continua da etapa correta sem pedir checkpoint ou implementar.
```

A Etapa B não pode ser executada ou avaliada quando a Etapa A falhar.

## Arquivos obrigatórios do gate de acesso

```text
PROJECT_STATE.md
docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md
```

O chat deve demonstrar leitura informando caminho, título e pelo menos um fato correto de cada arquivo.

## Estados formais

```text
ACCESS_NOT_TESTED
ACCESS_PASS
ACCESS_FAIL
RECONSTRUCTION_BLOCKED_BY_ACCESS
RECONSTRUCTION_PASS
RECONSTRUCTION_FAIL
CONTINUITY_PASS
CONTINUITY_FAIL
```

## Códigos de falha

```text
FAIL_ACCESS_GENERIC_GITHUB_PAGE
FAIL_ACCESS_PROJECT_STATE
FAIL_ACCESS_PTP_GOV_5
FAIL_ACCESS_MEMORY_PROTOCOL
FAIL_ACCESS_UNVERIFIED_CLAIM
FAIL_REPOSITORY_MIX
FAIL_IMPLEMENTATION_STARTED
FAIL_WRONG_ACTIVE_PTP
FAIL_WRONG_NEXT_ACTION
FAIL_STATE_ARCHITECTURE_CONFUSION
```

## Lição aprendida

```text
GITHUB PODE SER A MEMORIA OFICIAL SEM QUE TODO CHAT TENHA ACESSO AUTOMATICO AO GITHUB.
A GOVERNANCA DEVE VALIDAR PRIMEIRO O CANAL DE ACESSO E DEPOIS O CONTEUDO.
```

## Impacto no roadmap

Antes:

```text
Teste 1 — reconstrução
→ Teste 2 — continuidade
```

Agora:

```text
Teste A — acesso
→ Teste B — reconstrução
→ Teste C — continuidade
→ Auditoria Mestra
```

## Impacto no Linear

- `LEA-5` permanece aberto para repetição como teste de acesso e reconstrução.
- `LEA-6` permanece bloqueado até A e B passarem.
- `LEA-7` Auditoria Mestra não deve avançar antes da validação da memória.

## Critérios de conclusão

```text
TESTE_001_RESULTADO_REGISTRADO=PASS
PROTOCOLO_DUAS_ETAPAS_DOCUMENTADO=PASS
PROJECT_STATE_ATUALIZADO=PASS
LINEAR_ATUALIZADO=PASS
MEMORY_ACCESS_TEST_A=PASS
MEMORY_RECONSTRUCTION_TEST_B=PASS
MEMORY_CONTINUITY_TEST_C=PASS
```

## Próxima ação

Executar a **Etapa A — Teste de Acesso** em um chat novo que possua conector ou ferramenta capaz de ler o repositório. Somente depois executar a reconstrução.
