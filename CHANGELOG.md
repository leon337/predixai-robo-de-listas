# Changelog

Todas as mudanças relevantes do PredixAI Robô de Listas serão registradas neste arquivo.

## [2.2.0] — 2026-07-15

### Adicionado

- listas independentes dos perfis de coordenadas;
- cadastro de lista com nome, data e descrição;
- classificação automática em Hoje, Amanhã, Futura e Histórico;
- arquivamento e duplicação de listas;
- seleção de perfil e lista apenas no preparo da sessão;
- histórico estruturado por sessão;
- resumo de enviados, expirados, cancelados e erros;
- exportação do histórico em CSV;
- limpeza de histórico com confirmação;
- migração automática do formato V2.1 para V2.2.

### Corrigido

- perfis não removem nem substituem listas ao serem trocados;
- listas com nomes iguais continuam diferenciadas por data e ID;
- configuração passa a ser gravada de forma atômica no formato 4.

## [1.0.0] — 2026-07-15

### Adicionado

- aplicação desktop funcional em Python;
- calibração global dos alvos LARANJA e CINZA;
- agenda com até cinco sinais;
- ordenação cronológica;
- execução pelo relógio local do Linux;
- movimento do mouse e clique esquerdo único;
- histórico local da sessão;
- persistência das coordenadas e da agenda;
- janela mantida acima das demais;
- instalador Linux e executor `run.sh`;
- instalador de atalho para menu e área de trabalho;
- identidade visual PredixAI.

### Estado

Versão V1 funcional, publicada e preservada antes do início da V2 de interface compacta.
