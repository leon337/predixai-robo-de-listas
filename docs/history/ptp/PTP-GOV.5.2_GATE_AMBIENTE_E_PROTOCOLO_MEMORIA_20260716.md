# PTP-GOV.5.2 — Gate de Ambiente e Protocolo de Memória

## Identificação

- **Código técnico:** PTP-GOV.5.2
- **Nome curto:** Gate de Ambiente
- **PTP principal:** `PTP-GOV.5 — Memória e Governança Documental`
- **Projeto:** PredixAI Robô de Listas
- **Repositório:** `leon337/predixai-robo-de-listas`
- **Data:** 2026-07-16
- **Status:** EM ANDAMENTO

## Objetivo

Corrigir a causa raiz do primeiro teste de memória, tornar a configuração do conector GitHub um gate obrigatório e unificar o conjunto oficial de arquivos usado no Teste A.

## Descoberta

O primeiro chat de teste não conseguiu ler o repositório porque o plugin/conector GitHub não havia sido adicionado àquela conversa. Depois da ativação do conector, o mesmo chat passou a acessar os arquivos reais.

## Correção formal

```text
CLASSIFICACAO_ANTERIOR=FAIL_POR_FALTA_DE_ACESSO_AO_REPOSITORIO
CLASSIFICACAO_CORRIGIDA=FAIL_POR_CONECTOR_GITHUB_NAO_CONFIGURADO
REPOSITORIO_INDISPONIVEL=NAO
DOCUMENTACAO_AVALIADA=NAO
FALHA_DE_AMBIENTE=SIM
```

## Protocolo oficial

```text
ETAPA 0 — VERIFICAÇÃO DO AMBIENTE
→ conector GitHub adicionado e autorizado;
→ repositório oficial acessível;
→ branch main acessível;
→ PROJECT_STATE.md legível.

TESTE A — ACESSO DOCUMENTAL
→ leitura comprovada dos três arquivos oficiais.

TESTE B — RECONSTRUÇÃO
→ reconstrução do estado somente após 0/A=PASS.

TESTE C — CONTINUIDADE
→ continuidade em outro chat somente após 0/A/B=PASS.
```

## Conjunto oficial único do Teste A

```text
1. PROJECT_STATE.md
2. docs/history/ptp/PTP-GOV.5_MEMORIA_E_GOVERNANCA_DOCUMENTAL_20260716.md
3. docs/governance/PROJECT_MEMORY_ACCEPTANCE_TESTS.md
```

Qualquer conjunto anterior diferente está revogado para fins de aceitação.

## Relação com o histórico integral

O arquivo:

`docs/history/ptp/CHECKPOINT_HISTORICO_COMPLETO_PTP-GOV.5_ARQUITETURA_V2.5_V2.7_20260716.md`

permanece como memória longa da sessão, mas não substitui o conjunto oficial do Teste A. Ele deve ser lido depois que o acesso documental básico for comprovado.

## Gate de avanço

```text
CAUSE_ROOT_CORRECTED=PASS
ENVIRONMENT_STAGE_DEFINED=PASS
OFFICIAL_TEST_A_FILESET_UNIFIED=PASS
PR_16_DOCUMENTATION_ALIGNED=PASS
MEMORY_ENVIRONMENT_GATE=PENDING
MEMORY_ACCESS_TEST_A=BLOCKED
MEMORY_RECONSTRUCTION_TEST_B=BLOCKED
MEMORY_CONTINUITY_TEST_C=BLOCKED
```

## Próxima ação

1. Integrar a PR #16.
2. Abrir chat novo sem memória do projeto.
3. Adicionar e ativar o conector GitHub.
4. Executar Etapa 0.
5. Executar Teste A somente com Etapa 0=PASS.
6. Registrar os resultados no GitHub e Linear.

## Proibições

```text
NÃO julgar a documentação quando o ambiente falhar.
NÃO executar Teste A sem Etapa 0=PASS.
NÃO executar reconstrução sem Teste A=PASS.
NÃO retomar Auditoria Mestra antes dos gates de memória.
NÃO iniciar implementação V2.5.
```