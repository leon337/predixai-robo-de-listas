# RELATÓRIO DE EVIDÊNCIA LOCAL — V2.5.0-alpha.2

```text
ISSUE=LEA-146
REPOSITORY=leon337/predixai-robo-de-listas
MAIN_HEAD=40aca6ff9c470e44ea37e2d066092bc1349564fc
VERSION=V2.5.0-alpha.2
DATE=2026-07-22
SOURCE=CAPTURAS_LOCAIS_FORNECIDAS_POR_LEO
ENVIRONMENT=LINUX_MINT_DESKTOP
MODE_BOUNDARY=NULL_ONLY
```

## Objetivo

Registrar factualmente a atualização local pós-merge, a abertura da aplicação na versão correta e a recalibração de um perfil em ambiente fictício/demo.

## Evidências observadas

1. Aplicação aberta com título `PredixAI Robô de Listas — V2.5.0-alpha.2`.
2. Cabeçalho e campo `Versão instalada` exibindo `2.5.0-alpha.2`.
3. Perfil novo denominado `RECALIBRAGEM 1366X768`.
4. Aplicação declarada no perfil: `TESTE CORRETOR FICTÍCIA`.
5. Tela detectada: `1366x768 | 100%`.
6. Coordenadas de `AÇÃO 1 / PARA CIMA` e `AÇÃO 2 / PARA BAIXO` registradas.
7. Confirmação visual de teste controlado das duas coordenadas.
8. Estado final da tela inicial: `Compatibilidade: perfil pronto`.

## Inventário das capturas

| Arquivo de origem no chat | SHA-256 | Evidência principal |
|---|---|---|
| `image-1784746863272.jpg` | `49314bc90b0aed5fdfd8102a3526bc83da918d419d756a7ca5fc3a4ada85c339` | criação do perfil e detecção 1366x768 |
| `image-1784746890377.jpg` | `467ff3195c1cbb26c982e2476ee1ea5141b14d1fdc1a6452e14cba87470baf9f` | tela de calibração aberta |
| `image-1784746937514.jpg` | `8bf20957e13b1685ea38d10626361aa0f19a843a94185aa62cc35abca45891d2` | duas coordenadas registradas em ambiente fictício/demo |
| `image-1784746953509.jpg` | `b244fc9060560870af24c72b534d6cd03eb153d5d97d9cb3510e9846251158c5` | bloqueio por teste pendente antes da validação |
| `image-1784746967611.jpg` | `455b28501349f576decf802856f8321a507736f215ffc4bd6f8714f2e8544a17` | confirmação explícita antes do teste controlado |
| `image-1784746981129.jpg` | `4a0a68500cc95010c7a50cd9fcfec5cde7fb1d1dcba2ca5c898238d848873a20` | mensagem de teste concluído |
| `image-1784746992821.jpg` | `6ffd5c1b719ae779cc74acbb3576346aeb51c50ff47c8c0220c93ff01f26a635` | perfil pronto na tela inicial |

## Resultado

```text
LOCAL_MAIN_UPDATE=PASS
LOCAL_VERSION_DISPLAY=PASS
DESKTOP_LAUNCHER=PASS
PROFILE_RECALIBRATION_1366X768=PASS
COORDINATE_CAPTURE=PASS
CONTROLLED_CLICK_TEST_IN_FICTITIOUS_OR_DEMO_ENVIRONMENT=PASS_REPORTED_BY_LEO
PROFILE_COMPATIBILITY=READY
LOCAL_EVIDENCE_RESULT=PASS
```

## Limites e interpretação

- As capturas sustentam a confirmação local e visual descrita acima.
- O teste foi relatado e mostrado em ambiente identificado como fictício/demo.
- Esta evidência não autoriza execução de listas, corretora real, conta real, saldo real, efeito financeiro ou modo LIVE.
- Os binários das imagens permanecem nas fontes da conversa; este relatório preserva nomes, hashes e achados factuais.

## Próxima missão normativa

O catálogo oficial define `LST-001 — Lists and Scheduling` como sucessor de `DAT-001`. A missão deve permanecer candidata e não iniciada até autorização humana explícita.

```text
NEXT_MISSION_CANDIDATE=LST-001
NEXT_MISSION_AUTHORIZED=NO
MODE_MAX=NULL_ONLY
REAL_CLICK_AUTHORIZED=NO
REAL_FINANCIAL_EFFECT=NO
LIVE_MODE_ARMED=NO
```
