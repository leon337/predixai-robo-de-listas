# Protocolo de Aceitação da Memória do Projeto

## Autoridade

- **Projeto:** PredixAI Robô de Listas
- **Repositório:** `leon337/predixai-robo-de-listas`
- **PTP:** `PTP-GOV.5 — Memória e Governança Documental`
- **Revisão:** 2
- **Data:** 2026-07-16
- **Status:** ATIVO

## Objetivo

Comprovar, em duas etapas independentes, que um chat novo:

1. consegue acessar e ler os arquivos obrigatórios do GitHub;
2. depois consegue reconstruir e continuar corretamente o projeto sem memória prévia.

A documentação só pode ser avaliada depois que o acesso for comprovado.

---

# Resultado histórico do protocolo anterior

```text
TESTE_001=FAIL_POR_FALTA_DE_ACESSO_AO_REPOSITORIO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_INTERPRETACAO=NAO
FALHA_DE_ACESSO=SIM
```

Registro oficial:

`docs/history/tests/TESTE_001_RESULTADO_20260716.md`

## Lição aprendida

O protocolo anterior misturava capacidade de acesso e capacidade de interpretação. A recusa do chat em inventar o estado foi correta, mas o teste não chegou a avaliar a documentação.

---

# ETAPA A — TESTE DE ACESSO

## Objetivo

Confirmar que o chat consegue ler conteúdo real do repositório, e não apenas a página genérica do GitHub.

## Ambiente

- chat novo;
- sem checkpoint;
- sem memória do projeto;
- sem instruções personalizadas do PredixAI;
- acesso ao GitHub ou conector equivalente.

## Prompt exato

```text
Acesse o repositório https://github.com/leon337/predixai-robo-de-listas e confirme se consegue ler o conteúdo real destes três arquivos da branch main:

1. PROJECT_STATE.md
2. docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
3. docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md

Não interprete o projeto ainda. Para cada arquivo, informe:
- caminho;
- título encontrado;
- uma informação factual presente no conteúdo.

Se não conseguir abrir algum arquivo, declare ACCESS_FAIL e não tente reconstruir o projeto.
```

## PASS obrigatório

O chat deve demonstrar leitura dos três arquivos, informando corretamente:

```text
PROJECT_STATE.md
→ título relacionado ao estado do PredixAI Robô de Listas;
→ repositório oficial ou versão V2.4.3-R1.

PTP-GOV.5...
→ título PTP-GOV.5 — Memória e Governança Documental;
→ objetivo de memória GitHub testável ou erro de escopo registrado.

PROJECT_MEMORY_ACCEPTANCE_TESTS.md
→ protocolo em duas etapas Acesso → Reconstrução;
→ TESTE_001 registrado como falha de acesso.
```

## Resultado formal

```text
MEMORY_ACCESS_TEST_A=PASS|FAIL
FILES_REQUESTED=3
FILES_READ=0..3
FAILURE_CODE=
```

## Falhas automáticas

```text
FAIL_ACCESS_GENERIC_GITHUB_PAGE
FAIL_ACCESS_PROJECT_STATE
FAIL_ACCESS_PTP_GOV_5
FAIL_ACCESS_MEMORY_PROTOCOL
FAIL_ACCESS_UNVERIFIED_CLAIM
```

Se `MEMORY_ACCESS_TEST_A=FAIL`, a Etapa B é bloqueada.

---

# ETAPA B — TESTE DE RECONSTRUÇÃO

## Pré-condição

```text
MEMORY_ACCESS_TEST_A=PASS
```

## Prompt exato

```text
Agora que o acesso aos arquivos foi confirmado, leia o repositório https://github.com/leon337/predixai-robo-de-listas e explique, sem implementar nada:

1. Em que etapa o projeto está.
2. O que já foi concluído.
3. O que ainda está pendente.
4. Qual é a PTP ativa.
5. Qual é a próxima ação obrigatória.
6. Quais ações estão proibidas neste momento.
```

## Resposta esperada mínima

```text
Projeto: PredixAI Robô de Listas.
Repositório oficial: leon337/predixai-robo-de-listas.
Versão real atual: V2.4.3-R1.
PTP ativa: PTP-GOV.5 — Memória e Governança Documental.

Concluído:
- 12 pontos da arquitetura conceitual;
- revisões críticas arquiteturais;
- schema lógico SQLite conceitual;
- divisão V2.5–V2.7;
- PTM V2.5 preliminar.

Etapa atual:
- governança documental em validação;
- Auditoria Mestra do legado V2.4.3-R1 ainda pendente/em andamento.

Pendente:
- Anexo A do inventário real;
- reconciliação e revisão da PTM V2.5;
- PTMs V2.6 e V2.7;
- consolidação cruzada;
- ADRs;
- Documento Mestre;
- congelamento da Arquitetura V1.0.

Próxima ação:
- concluir a validação da memória e continuar a Auditoria Mestra exclusivamente no repositório correto.

Proibido:
- iniciar implementação;
- usar predixai-platform como fonte;
- misturar estado real com arquitetura futura;
- considerar a PTM definitiva antes do inventário.
```

## PASS obrigatório

- identifica repositório e versão corretos;
- identifica `PTP-GOV.5`;
- distingue legado real de arquitetura futura;
- reconhece que a PTM V2.5 é preliminar;
- informa a Auditoria Mestra como próxima etapa após validação;
- não cria código, script ou migration;
- não usa dados do repositório incorreto.

## Falhas automáticas

```text
FAIL_REPOSITORY_MIX
FAIL_IMPLEMENTATION_STARTED
FAIL_WRONG_ACTIVE_PTP
FAIL_WRONG_NEXT_ACTION
FAIL_STATE_ARCHITECTURE_CONFUSION
FAIL_SKIP_MASTER_AUDIT
```

---

# ETAPA C — TESTE DE CONTINUIDADE

Executado em outro chat novo, somente após A e B passarem.

## Prompt

```text
Leia o repositório https://github.com/leon337/predixai-robo-de-listas e continue exatamente da última etapa registrada. Não peça checkpoint e não implemente código antes de confirmar o estado e a próxima ação.
```

## PASS mínimo

- confirma a fonte oficial;
- confirma arquitetura conceitual concluída;
- confirma PTM V2.5 preliminar;
- confirma PTP-GOV.5;
- continua pela Auditoria Mestra;
- não reinicia a arquitetura;
- não pede checkpoint externo;
- não produz implementação.

---

# Registro de resultados

```text
TEST_ID=
DATE_UTC=
MODEL_OR_CHAT=
PROMPT_EXACT=
ACCESS_STATUS=PASS|FAIL|NOT_APPLICABLE
RESULT=PASS|FAIL|PASS_WITH_WARNINGS|BLOCKED_BY_ACCESS
FAILURE_CODES=
FILES_READ=
MISSING_FACTS=
WRONG_FACTS=
DOCUMENT_CHANGES_REQUIRED=
EVIDENCE_LINK=
```

# Gate da PTP-GOV.5

```text
MEMORY_ACCESS_TEST_A=PASS
MEMORY_RECONSTRUCTION_TEST_B=PASS
MEMORY_CONTINUITY_TEST_C=PASS
```

Se qualquer etapa falhar, o avanço para a Auditoria Mestra permanece bloqueado até correção e repetição em chat independente.
