# PredixAI Robô de Listas — V1 Desktop e Memória

**Data:** 2026-07-15  
**Versão:** 1.0.0  
**Branch de implementação:** `feature/v1-desktop-memory`

## Objetivo

Preservar a V1 funcional e adicionar um meio simples de abertura por dois cliques no Linux Mint, sem alterar a lógica da aplicação.

## Estado herdado

- calibração global: PASS;
- agenda de até cinco sinais: PASS;
- ordenação cronológica: PASS;
- relógio Linux: PASS;
- movimento do mouse: PASS;
- clique único: PASS;
- histórico local: PASS;
- persistência: PASS;
- janela sempre acima: PASS.

## Implementação desktop

O arquivo `install_desktop.sh`:

1. identifica automaticamente a raiz do repositório;
2. garante permissão de execução em `run.sh`;
3. instala a logomarca em `~/.local/share/icons/`;
4. cria o lançador em `~/.local/share/applications/`;
5. copia o lançador para a área de trabalho quando ela é localizada;
6. usa `Terminal=false`;
7. mantém a execução centralizada em `run.sh`.

## Arquivos adicionados

- `install_desktop.sh`;
- `VERSION`;
- `CHANGELOG.md`;
- `docs/history/20260715_V1_DESKTOP_E_MEMORIA.md`;
- `docs/roadmap/V2_UI_COMPACTA.md`.

## Segurança

- nenhuma alteração em `app/main.py`;
- nenhuma alteração na lógica de calibração, agenda ou clique;
- nenhum dado local ou credencial versionado;
- o atalho utiliza caminhos absolutos gerados durante a instalação local.

## Validação local necessária

A criação dos arquivos e commits ocorre no GitHub. A prova final do ícone exige execução no Linux Mint:

```bash
bash install_desktop.sh
```

Resultado esperado:

```txt
ATALHO_MENU=CRIADO
ATALHO_DESKTOP=CRIADO_OU_MENU_APENAS
TERMINAL=false
EXECUCAO_VIA_RUN_SH=SIM
```

## Próxima etapa

Após validar a abertura por dois cliques, iniciar a branch `feature/v2-ui-compacta` para as melhorias de design, campos de hora/minuto/segundo e modo compacto.
