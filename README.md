# PredixAI Robô de Listas

> Painel operacional. A autoridade estruturada permanece em
> `PROJECT_RUNTIME_STATE.yaml`; o mapa de desenvolvimento permanece no Documento
> Mestre da Arquitetura V1.0.

## Estado atual

```text
VERSÃO_INSTALADA=V2.4.3-R1
DAT_001_VERSION_TARGET=V2.5.0-alpha.2
MAIN_HEAD=f0faa79c157cbfeae75b620eddb9ccade6000a36
MISSÃO_ATIVA=LEA-59 — DAT-001
REVISÃO=LEA-60 — PREPARADA E BLOQUEADA ATÉ O CANDIDATO
BRANCH=leonpcsn/dat-001-durable-state-legacy-migration
PR_DRAFT=PENDENTE
STATE_REVISION=36
ARQUITETURA_V1_CONGELADA=YES
MERGE_AUTORIZADO=NO
```

## Campanha

| Entrega ou gate | Estado |
|---|---|
| Documento Mestre e mapa canônico | ✅ integrados |
| requisitos, domínios, handoffs e ADRs | ✅ `218/218`, `16/16`, `12/12`, `18/18` |
| FND-001, FND-002 e FND-003 | ✅ integradas |
| DAT-001 — estado durável e migração legada | 🟨 em implementação na LEA-59 |
| LEA-60 — revisão independente | ⏳ preparada, aguardando HEAD final |
| LST-001 | ⛔ não autorizado |

## DAT-001

A entrega introduz somente persistência SQLite local V1: escritor único, versão
otimista, comandos idempotentes, eventos versionados em outbox atômico, migrations
reversíveis, backup/restore verificável e importação legada para staging.

Importação não significa cutover: os dados permanecem não autoritativos até uma
missão posterior expressamente autorizada. Nenhum banco de produção ou dado real
existente é alterado.

Validação Linux Mint prevista:

```bash
./scripts/local_validate_dat_001.sh --expected-commit <HEAD_EXATO_DO_PR_DRAFT>
```

```text
LOCAL_LINUX_MINT_TEST=⏳ AGUARDANDO EXECUÇÃO DO LEO
LOCAL_REPORT_TXT=⏳ AGUARDANDO EXECUÇÃO DO LEO
```

## Limites

```text
MODE_MAX=NULL_ONLY
PRODUCTION_DATABASE=NO
EXISTING_REAL_DATA_MUTATION=NO
IRREVERSIBLE_MIGRATION=NO
DESTRUCTIVE_MIGRATION=NO
LST_001_AUTHORIZED=NO
SIMULATED_MODE=NO
CONTROLLED_UI=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
REAL_FINANCIAL_EFFECT=NO
LIVE_MODE_ARMED=NO
MERGE_AUTHORIZED=NO
```

## Próxima ação

Validar o candidato, abrir PR Draft e fixar seu HEAD no GitHub e na LEA-60. O
builder deve parar antes da revisão, promoção ou merge.
