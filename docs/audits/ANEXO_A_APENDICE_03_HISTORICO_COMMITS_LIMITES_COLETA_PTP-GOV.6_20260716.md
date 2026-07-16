# ANEXO A — APÊNDICE 03

## Histórico de commits, evolução do legado e limites da coleta integral

## 1. Controle

```text
DOCUMENT_STATUS=DRAFT_PARTIAL
PARENT_DOCUMENT=ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
WORK_BRANCH=docs/ptp-gov-6-anexo-a
CODE_CHANGED=NO
RUNTIME_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
```

Este apêndice reconcilia marcos verificáveis do histórico do repositório. Ele não substitui o código existente no commit-base e não transforma mensagens de commit em prova suficiente de comportamento atual.

## 2. Regra de autoridade

```text
CURRENT_CODE_AT_SOURCE_COMMIT > PROJECT_STATE > ACTIVE_STAGE_DOCUMENTS > HISTORICAL_COMMITS
```

Classificação do histórico de commits: `REUTILIZAR` como evidência cronológica e de intenção, sempre confrontada com os arquivos reais da versão auditada.

Certeza: alta para os SHAs e mensagens localizados pelo GitHub; média para intenções não reconfirmadas diretamente no código.

Risco: médio se mensagens históricas forem tratadas isoladamente como estado atual.

## 3. Formação da V1

Marcos confirmados:

| SHA | Mensagem factual | Papel histórico |
|---|---|---|
| `4eb79db76596aed1b258c09396574ba0a4ca78de` | V1: iniciar repositório e documentação | criação da base |
| `9dbd463ce15c226d5b3becc342c401ba00b9f9ea` | V1: publicar aplicação desktop funcional | núcleo desktop inicial |
| `c1ec95e261eb79ce71bfd422958ba089817f90b3` | V1: adicionar dependências | dependência externa |
| `4ed36f116a3f33168fb89ccdbe7aedf8714da017` | V1: proteger arquivos locais e credenciais | segurança de versionamento |
| `802968f9526d1ac4a4b10de73a0a6dce3c19aeba` | V1: adicionar instalador Linux | instalação |
| `f4eb5f44dda0605ae724107a1ce3d9ac39707adc` | V1: adicionar executor Linux | launcher |
| `acfebdc40938d332ef677286a6bbaeac8b0bc3cd` | V1: criar diretório de configuração | persistência local |
| `5f3fd09553bf2ffef842843b8d5da1b528af9ed8` | V1: adicionar testes mínimos | baseline de testes |
| `db3d6ebbbdcb1b3e13e32f133c50b2d896ff17d0` | V1: adicionar identidade visual vetorial | ativo visual |
| `20be73843c7b4a4bc9589a91458e229d6654049e` | V1: corrigir instruções de execução no Linux | documentação operacional |
| `25e0e6e4548bde1be3873e862179d1820d6c9e8e` | V1: adicionar atalho desktop e memória técnica | instalação e histórico |

Conclusão: a V1 foi construída incrementalmente como aplicação desktop local, com configuração, scripts Linux, testes mínimos e documentação adicionados em commits separados.

## 4. Marcos funcionais V2.1–V2.4.3

| Versão | SHA de marco confirmado | Evolução registrada | Classificação histórica |
|---|---|---|---|
| V2.1 | `134ac89276f8673452ff566dcfef8ab95514382c` | listas datadas, estados e correções visuais | REUTILIZAR como origem de requisitos |
| V2.2 | `f4b870958f5bc8d1fc9c4cbb09e44e4d5f99d415` | listas independentes, migração e histórico estruturado | ADAPTAR |
| V2.3 | `79a6264c117ca809df45e970168b3a3c00277a67` | UX de direção, listas contextuais e histórico | ADAPTAR |
| V2.3.1 | `c8e6f8d1271e6488bc071a431d94ead4a244e9c2` | pausa, retomada e cancelamento | ADAPTAR regras; execução permanece bloqueada |
| V2.3.2 | `4d199fa3481e631f1afce31e6801616e3c5c4464` | preflight temporal e ciclo de sessão | REUTILIZAR/ADAPTAR |
| V2.3.3 | `ae11f88545c7d5da409794a4e88f3ecf12b44e3a` | versão publicada 2.3.3 e apresentação de versão | REUTILIZAR metadata |
| V2.4.1 | `bb846500fbb6429240b771c465a0faa0edc9f3e3` | instância única, logs e diagnóstico de startup | ADAPTAR |
| V2.4.2 | `35bac48756cf64cc8ab3fa1e3b31d276865b6f45` | backup e recuperação da configuração | ADAPTAR |
| V2.4.2-R1 | `60b0136a43e046f5250e75f9db0d3f625574aaeb` | correção da cadeia de configuração | REUTILIZAR como evidência de regressão |
| V2.4.3 | `f1a7dce86279949f93665eea1a641243fcaa4e58` | diagnóstico e ferramentas operacionais | ADAPTAR |

Commits adicionais confirmam que V2.4.2-R1 passou por correções de preservação de `load/save`, teste da cadeia, CI e isolamento do teste da interface:

```text
ae005f9323b00a599cdaf4cb6532820f9b5c2857
c6648ce9c484a1199cf1eff68e7e8c6357cfabaf
369e240d3f5ad9dbc1d030510f6517f882021084
e86e4d8e4e950ff4196f20bbc07e0acafaf0972a
cf70ff8e041a4ac027ebc262ea9ded7b6e4eebd0
dd83131d247d2130dc3d0d8c0aec4b922e6efbd4
```

## 5. Formação da V2.4.3

Marcos confirmados:

```text
da6fca369a47a349a100cec3133a0645d66d42d3
  feat(v2.4.3): adicionar serviço de diagnóstico e ferramentas

5d14040bc66068f7e0d0adcd4c92154a3e7a235f
  feat(v2.4.3): adicionar tela de ferramentas e diagnóstico

3736ac3c6f7bbed92f446cd068e987aee250190c
  feat(v2.4.3): integrar ferramentas ao entrypoint

f1a7dce86279949f93665eea1a641243fcaa4e58
  merge da V2.4.3
```

Conclusão: a V2.4.3 preservou o padrão incremental de adicionar módulo, integrar pela cadeia de patches e publicar workflow/versionamento correspondente.

## 6. Transição para governança

Em 2026-07-16, o histórico passou a registrar predominantemente documentação, testes de memória, revisões e sincronização operacional.

Marcos confirmados:

```text
6710b265a76b06994c76638562b01bb5482b0502
  criar estado oficial autossuficiente

e8fce748424b81e5020a282bf91484ab730c481e
  definir testes objetivos de memória

978c8a735ef1013369bdf39e37b543d7df951d9c
  registrar engenharia, decisões e falhas

ef b98e17de3909926f210db52d278149868e0edb
  integrar memória GitHub testável

58973dcee5e0bbfe4445c96b8fd268cb866c373e
  publicar histórico integral da arquitetura futura

35dca0aaea25d6816396e74fa2cb146d510cf6b3
  adicionar anexo de contratos e schema conceitual

0e2d7e98d863769be32a8bcb8b93684a61674aa3
  alinhar PROJECT_STATE após conclusão da LEA-11
```

Correção de registro: o SHA `efb98e17de3909926f210db52d278149868e0edb` é o marco de integração da memória GitHub testável.

## 7. Conclusões arquiteturais do histórico

```text
EVOLUTION_STYLE=INCREMENTAL_PATCH_CHAIN
VERSIONED_VALIDATION_EVOLUTION=CONFIRMED
REGRESSION_REPAIR_HISTORY=CONFIRMED
DOCUMENTATION_LAG=CONFIRMED
GOVERNANCE_PIVOT=CONFIRMED
HISTORY_AS_CURRENT_TRUTH=PROHIBITED
```

Achados:

1. a aplicação cresceu por camadas e substituição dinâmica de comportamento;
2. testes e workflows foram acrescentados por versão, sem consolidação única da suíte;
3. a sequência V2.4.2-R1 evidencia regressão real na composição de persistência;
4. README e CHANGELOG não acompanharam integralmente a evolução do código;
5. a governança foi introduzida depois da evolução funcional e deve reconciliar o legado sem reescrevê-lo antecipadamente.

## 8. Limite técnico da coleta integral

A leitura de arquivos conhecidos e a busca de commits funcionam pelo conector GitHub. Contudo, nesta execução:

- o conector disponível não fornece enumeração recursiva de diretórios;
- a tentativa de clone somente leitura do repositório oficial falhou por indisponibilidade de resolução de rede no ambiente de análise;
- sem árvore local do commit-base, não é tecnicamente seguro declarar contagem integral de todos os arquivos, métodos e funções aninhadas.

```text
FULL_RECURSIVE_TREE_RECONCILIATION=BLOCKED_BY_ENVIRONMENT
FULL_ROOT_DIRECTORY_ENUMERATION=BLOCKED_BY_ENVIRONMENT
ALL_METHODS_AND_NESTED_FUNCTIONS_COUNT=BLOCKED_BY_ENVIRONMENT
COMMIT_HISTORY_MILESTONE_RECONCILIATION=PASS
ALL_COMMITS_EXHAUSTIVE_ENUMERATION=NOT_CLAIMED
RUNTIME_EXECUTION_REQUIRED=NO
REAL_CLICK_EXECUTION_REQUIRED=NO
```

O bloqueio não autoriza executar a aplicação nem qualquer caminho de interação automática.

## 9. Evidência necessária para desbloqueio

É necessário um relatório TXT somente leitura, gerado sobre o commit-base, contendo:

1. SHA do HEAD auditado;
2. árvore recursiva ordenada dos arquivos versionados;
3. contagem por extensão e diretório;
4. índice AST de classes, métodos, funções e funções aninhadas dos arquivos Python;
5. histórico completo de commits em ordem cronológica;
6. confirmação de que o working tree permaneceu inalterado.

O relatório deve registrar explicitamente:

```text
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
WORKTREE_CHANGED=NO
APPLICATION_EXECUTED=NO
REAL_CLICK_EXECUTED=NO
```

## 10. Gate do apêndice

```text
V1_COMMIT_MILESTONES=PASS
V2_VERSION_MILESTONES=PASS
V2_4_2_R1_REGRESSION_HISTORY=PASS
V2_4_3_FORMATION_HISTORY=PASS
GOVERNANCE_TRANSITION_HISTORY=PASS
COMMIT_HISTORY_MILESTONE_RECONCILIATION=PASS
FULL_TREE_AND_AST_EVIDENCE=PENDING_EXTERNAL_READ_ONLY_REPORT
APPENDIX_COMPLETE=PASS_WITH_DOCUMENTED_BLOCKER
```
