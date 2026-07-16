# Testes de Aceitação da Memória do Projeto

## Autoridade

- **Projeto:** PredixAI Robô de Listas
- **Repositório:** `leon337/predixai-robo-de-listas`
- **PTP:** `PTP-GOV.5`
- **Status:** ATIVO
- **Data:** 2026-07-16

## Objetivo

Comprovar que um chat novo, sem memória prévia, sem checkpoint colado e sem instruções personalizadas, consegue reconstruir e continuar corretamente o projeto lendo apenas o GitHub.

A documentação não será considerada aprovada por parecer completa. Será aprovada somente por teste.

---

# TESTE 1 — Reconstrução do estado

## Ambiente

- Novo chat.
- Nenhum histórico do projeto.
- Nenhum checkpoint.
- Nenhuma instrução personalizada do PredixAI.
- Acesso ao GitHub.

## Prompt exato

```text
Leia o repositório https://github.com/leon337/predixai-robo-de-listas e explique, sem implementar nada:

1. Em que etapa o projeto está.
2. O que já foi concluído.
3. O que ainda está pendente.
4. Qual é a PTP ativa.
5. Qual é a próxima ação obrigatória.
6. Quais ações estão proibidas neste momento.
```

## Resposta esperada mínima

A resposta deve conter, sem contradição:

```text
Projeto: PredixAI Robô de Listas.
Repositório oficial: leon337/predixai-robo-de-listas.
Versão real atual: V2.4.3-R1.
PTP ativa: PTP-GOV.5 — Memória e Governança Documental.

Concluído:
- os 12 pontos da arquitetura conceitual;
- revisões críticas arquiteturais;
- schema lógico SQLite conceitual;
- divisão V2.5–V2.7;
- PTM V2.5 preliminar.

Etapa atual:
- validar a memória documental;
- continuar a Auditoria Mestra do legado V2.4.3-R1.

Pendente:
- Anexo A do inventário real;
- reconciliação e revisão da PTM V2.5;
- PTMs V2.6 e V2.7;
- consolidação cruzada;
- ADRs;
- Documento Mestre;
- congelamento da Arquitetura V1.0.

Próxima ação:
- executar os testes de memória e continuar a Auditoria Mestra apenas no repositório correto.

Proibido:
- iniciar implementação;
- usar o repositório predixai-platform;
- misturar estado real com arquitetura futura;
- considerar a PTM definitiva antes do inventário.
```

## Critérios de PASS

- Identifica o repositório correto.
- Identifica `V2.4.3-R1`.
- Identifica `PTP-GOV.5`.
- Distingue estado real de arquitetura futura.
- Informa que a Auditoria Mestra está pendente/em andamento.
- Não inicia código ou implementação.
- Não menciona `predixai-platform` como fonte válida.

## Falhas automáticas

```text
FAIL_REPOSITORY_MIX
FAIL_IMPLEMENTATION_STARTED
FAIL_WRONG_ACTIVE_PTP
FAIL_WRONG_NEXT_ACTION
FAIL_LEGACY_TARGET
FAIL_STATE_ARCHITECTURE_CONFUSION
```

---

# TESTE 2 — Continuidade correta

## Ambiente

Outro chat novo e independente do Teste 1.

## Prompt exato

```text
Leia o repositório https://github.com/leon337/predixai-robo-de-listas e continue exatamente da última etapa registrada. Não peça checkpoint e não implemente código antes de confirmar o estado e a próxima ação.
```

## Resposta esperada mínima

```text
1. Confirmar que a fonte oficial é o repositório predixai-robo-de-listas.
2. Confirmar que a arquitetura conceitual já foi concluída.
3. Confirmar que a PTM V2.5 é preliminar e não reconciliada.
4. Confirmar que a PTP ativa é PTP-GOV.5.
5. Informar que a próxima atividade é validar a memória documental e continuar a Auditoria Mestra.
6. Retomar a auditoria pelo inventário real da branch main/V2.4.3-R1.
7. Não produzir código, script, migration, correção ou implementação.
```

A resposta pode iniciar a leitura/auditoria somente após declarar essas sete confirmações.

## Critérios de PASS

- Continua da etapa correta sem reiniciar a arquitetura.
- Não solicita um checkpoint externo.
- Não cria código.
- Não altera a PTM como definitiva.
- Mantém o GitHub como fonte técnica.
- Respeita a ordem do roadmap.

## Falhas automáticas

```text
FAIL_RESTART_FROM_ZERO
FAIL_CHECKPOINT_DEPENDENCY
FAIL_CODE_BEFORE_AUDIT
FAIL_WRONG_REPOSITORY
FAIL_SKIP_PTM_RECONCILIATION
FAIL_SKIP_DOCUMENT_MASTER
```

---

# TESTE 3 — Decisões congeladas

## Prompt

```text
Quais decisões estão congeladas e quais foram revogadas neste projeto?
```

## PASS mínimo

Deve mencionar:

- servidor como fonte global;
- SQLite somente pelo servidor e escritor único;
- clientes sem acesso direto ao banco;
- listas independentes da análise;
- separação entre análise, sinal e execução;
- schema físico progressivo;
- GitHub como memória oficial;
- auditoria exclusiva no repositório correto;
- revogação do chat como memória primária;
- revogação da auditoria separada da rastreabilidade.

---

# TESTE 4 — Riscos e erro histórico

## Prompt

```text
Quais são os riscos atuais e qual erro de escopo já ocorreu?
```

## PASS mínimo

Deve reconhecer:

- Auditoria Mestra ainda não concluída.
- PTM V2.5 ainda não reconciliada.
- Documento Mestre inexistente.
- Implementação não autorizada.
- Erro anterior de auditar `predixai-platform`.
- Invalidação completa das conclusões daquele repositório.

---

# Registro dos resultados

Cada teste deve ser registrado neste formato:

```text
TEST_ID=
DATE_UTC=
MODEL_OR_CHAT=
PROMPT_EXACT=
RESULT=PASS|FAIL|PASS_WITH_WARNINGS
FAILURE_CODES=
MISSING_FACTS=
WRONG_FACTS=
DOCUMENT_CHANGES_REQUIRED=
EVIDENCE_LINK=
```

## Gate final

```text
MEMORY_TEST_1=PASS
MEMORY_TEST_2=PASS
```

Os testes 3 e 4 são obrigatórios antes do congelamento da Arquitetura V1.0.

Se qualquer teste falhar, a documentação deve ser corrigida e o teste repetido em outro chat novo.
