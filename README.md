# PredixAI Robô de Listas

Aplicação desktop em Python para calibração de coordenadas globais, criação de uma agenda com até cinco sinais e execução controlada de cliques locais por horário do Linux.

## Estado

- **Versão:** 1.0.0
- **Status:** publicada e pronta para clonagem/teste
- **Plataforma alvo:** Linux Mint / X11

## Recursos da V1

- janela sempre acima;
- calibração de dois pontos globais: `LARANJA` e `CINZA`;
- teste manual das coordenadas;
- agenda dinâmica de até cinco sinais;
- direções `PARA_CIMA` e `PARA_BAIXO`;
- ordenação cronológica;
- execução por relógio local do Linux;
- movimento do mouse e clique esquerdo único;
- painel de execução;
- histórico da sessão;
- persistência local das coordenadas e da agenda.

## Instalação

```bash
sudo apt update
sudo apt install -y python3-venv python3-tk

git clone https://github.com/leon337/predixai-robo-de-listas.git
cd predixai-robo-de-listas

bash install.sh
bash run.sh
```

## Criar ícone no menu e na área de trabalho

Depois da instalação normal, execute uma vez:

```bash
bash install_desktop.sh
```

O instalador:

- registra o PredixAI no menu de aplicativos;
- usa a logomarca existente em `assets/`;
- cria um atalho na área de trabalho quando a pasta é localizada;
- abre a aplicação por `run.sh`;
- usa `Terminal=false`, sem abrir o terminal durante o uso normal.

Depois disso, abra **PredixAI Robô de Listas** pelo menu ou por dois cliques no ícone da área de trabalho.

## Execução manual

```bash
source .venv/bin/activate
python app/main.py
```

## Estrutura

```text
app/main.py
assets/logo_predixai.svg
config/
docs/history/
docs/roadmap/
tests/test_smoke.py
requirements.txt
install.sh
install_desktop.sh
run.sh
VERSION
CHANGELOG.md
```

## Segurança

Use somente em aplicações locais ou ambientes controlados sob sua responsabilidade. Antes de iniciar, confira a resolução, a escala e as coordenadas calibradas.

## Próxima versão

A V2 será desenvolvida em branch separada com interface mais compacta, seletor de horário por `Spinbox`, melhor responsividade, botões refinados e logomarca recortada.
