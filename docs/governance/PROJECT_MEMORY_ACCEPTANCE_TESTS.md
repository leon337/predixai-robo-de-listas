# Protocolo de Aceitação da Memória do Projeto

## Autoridade

- **Projeto:** PredixAI Robô de Listas
- **Repositório:** `leon337/predixai-robo-de-listas`
- **PTP:** `PTP-GOV.5 — Memória e Governança Documental`
- **Mini-PTP:** `PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória`
- **Revisão:** 3
- **Data:** 2026-07-16
- **Status:** ATIVO

## Objetivo

Comprovar, em gates independentes, que um chat novo:

1. possui ambiente e conector GitHub corretamente configurados;
2. consegue ler os arquivos oficiais do repositório;
3. reconstrói corretamente o estado do projeto;
4. continua exatamente da etapa registrada.

A documentação só pode ser avaliada depois que o ambiente e o acesso forem comprovados.

---

# Resultado histórico corrigido do primeiro experimento

```text
TESTE_001=FAIL_POR_CONECTOR_GITHUB_NAO_CONFIGURADO
REPOSITORIO_INDISPONIVEL=NAO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_INTERPRETACAO=NAO
FALHA_DE_AMBIENTE=SIM
CAUSA_RAIZ=PLUGIN_OU_CONECTOR_GITHUB_NAO_ADICIONADO_AO_CHAT
```

Registro oficial:

`docs/history/tests/TESTE_001_RESULTADO_20260716.md`

## Lição aprendida

A integração GitHub estar autorizada na conta não garante que o conector esteja adicionado e disponível naquele chat. Antes de testar a memória, é obrigatório validar o ambiente.

---

# ETAPA 0 — VERIFICAÇÃO DO AMBIENTE

## Objetivo

Confirmar que o chat possui acesso funcional ao conector GitHub antes de avaliar documentação ou continuidade.

## Pré-condições

- chat novo;
- sem checkpoint;
- sem memória do projeto;
- sem instruções personalizadas do PredixAI;
- conector/plugin GitHub adicionado ao chat;
- conta GitHub autorizada.

## Prompt exato

```text
Use exclusivamente o conector GitHub, não navegação web genérica.

Repositório: leon337/predixai-robo-de-listas
Branch: main
Arquivo: PROJECT_STATE.md

Confirme:
1. que o conector GitHub está ativo;
2. que o repositório foi localizado;
3. que a branch main foi acessada;
4. que PROJECT_STATE.md foi lido;
5. o título do arquivo e a PTP ativa encontrada.

Se o conector não estiver disponível ou o arquivo não puder ser lido, responda ENVIRONMENT_FAIL e não continue.
```

## PASS obrigatório

```text
GITHUB_CONNECTOR_ENABLED=PASS
GITHUB_ACCOUNT_AUTHORIZED=PASS
OFFICIAL_REPOSITORY_ACCESSIBLE=PASS
MAIN_BRANCH_ACCESSIBLE=PASS
PROJECT_STATE_READABLE=PASS
ENVIRONMENT_GATE=PASS
```

## Falhas automáticas

```text
FAIL_CONNECTOR_NOT_ADDED
FAIL_CONNECTOR_NOT_AUTHORIZED
FAIL_REPOSITORY_NOT_ACCESSIBLE
FAIL_MAIN_BRANCH_NOT_ACCESSIBLE
FAIL_PROJECT_STATE_NOT_READABLE
FAIL_GENERIC_WEB_USED_INSTEAD_OF_CONNECTOR
```

Se `ENVIRONMENT_GATE=FAIL`, o Teste A não foi executado e a documentação não pode ser julgada.

---

# ETAPA A — TESTE DE ACESSO DOCUMENTAL

## Pré-condição

```text
ENVIRONMENT_GATE=PASS
```

## Conjunto oficial único

```text
1. PROJECT_STATE.md
2. docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
3. docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md
```

Qualquer lista anterior diferente desta está revogada para fins de gate.

## Prompt exato

```text
Use o conector GitHub no repositório leon337/predixai-robo-de-listas, branch main.

Confirme leitura real destes três arquivos:

1. PROJECT_STATE.md
2. docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
3. docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md

Não interprete o projeto ainda. Para cada arquivo, informe:
- caminho exato;
- título encontrado;
- uma informação factual presente no conteúdo;
- SHA/blob quando disponível.

Se não conseguir abrir algum arquivo, declare ACCESS_FAIL e não tente reconstruir o projeto.
```

## PASS obrigatório

O chat deve demonstrar leitura dos três arquivos:

```text
PROJECT_STATE.md
→ identifica PredixAI Robô de Listas, V2.4.3-R1 ou PTP-GOV.5.

PTP-GOV.5...
→ identifica Memória e Governança Documental e o objetivo de memória GitHub testável.

PROJECT_MEMORY_ACCEPTANCE_TESTS.md
→ identifica Etapa 0 → Acesso → Reconstrução → Continuidade.
```

## Resultado formal

```text
MEMORY_ACCESS_TEST_A=PASS|FAIL
FILES_REQUESTED=3
FILES_READ=0..3
FAILURE_CODES=
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

## Pré-condições

```text
ENVIRONMENT_GATE=PASS
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
- PTM V2.5 preliminar;
- histórico integral publicado.

Etapa atual:
- governança documental em validação;
- Auditoria Mestra pausada até os gates de memória.

Pendente:
- Teste C de continuidade;
- Auditoria Mestra e Anexo A;
- reconciliação da PTM V2.5;
- PTMs V2.6 e V2.7;
- consolidação cruzada;
- ADRs;
- Documento Mestre;
- congelamento da Arquitetura V1.0.

Próxima ação:
- concluir os gates de memória e retomar a Auditoria Mestra exclusivamente no repositório correto.

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

Executado em outro chat novo, somente após Etapa 0, A e B passarem.

## Prompt

```text
Adicione e use o conector GitHub. Leia o repositório https://github.com/leon337/predixai-robo-de-listas e continue exatamente da última etapa registrada. Não peça checkpoint e não implemente código antes de confirmar o estado e a próxima ação.
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
CONNECTOR_USED=
PROMPT_EXACT=
ENVIRONMENT_STATUS=PASS|FAIL|NOT_APPLICABLE
ACCESS_STATUS=PASS|FAIL|NOT_APPLICABLE
RESULT=PASS|FAIL|PASS_WITH_WARNINGS|BLOCKED_BY_ENVIRONMENT|BLOCKED_BY_ACCESS
FAILURE_CODES=
FILES_READ=
MISSING_FACTS=
WRONG_FACTS=
DOCUMENT_CHANGES_REQUIRED=
EVIDENCE_LINK=
```

# Gate da PTP-GOV.5

```text
MEMORY_ENVIRONMENT_GATE=PASS
MEMORY_ACCESS_TEST_A=PASS
MEMORY_RECONSTRUCTION_TEST_B=PASS
MEMORY_CONTINUITY_TEST_C=PASS
```

Se qualquer etapa falhar, o avanço para a Auditoria Mestra permanece bloqueado até correção e repetição em chat independente.