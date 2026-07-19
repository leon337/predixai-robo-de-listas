# FND-001 — SAFE SERVER FOUNDATION

## Missão LEA-43

```text
BASE_MAIN_SHA=861db10366e3c9f20b8452535427755a273899a4
MODE=NULL_ONLY
IMPLEMENTATION_AUTHORIZED=YES
MERGE_AUTHORIZED=NO
```

## Objetivo

Criar um caminho novo, modular e reversível para o servidor local da Arquitetura V1.0, sem alterar o entrypoint Tkinter legado e sem permitir efeito externo.

## Componentes

- `server/contracts.py`: contratos versionados, estados, razão e capacidades;
- `server/config.py`: configuração tipada, bind local e modo `NULL` obrigatório;
- `server/adapters/null.py`: adaptador sem efeito externo;
- `server/audit.py`: auditoria estruturada em memória;
- `server/service.py`: autoridade de estado e capacidades;
- `server/app.py`: API FastAPI com saúde e capacidades;
- `tests/server/`: testes unitários, integração e provas negativas;
- `.github/workflows/validate-fnd-001.yml`: CI dedicado.

## API inicial

```text
GET /api/v1/health
GET /api/v1/capabilities
```

## Estados

```text
BOOTING
SAFE_IDLE
DEGRADED
STOPPED
```

## Segurança

A configuração rejeita qualquer modo diferente de `NULL`, qualquer bind que não seja loopback e portas privilegiadas. O snapshot de capacidades declara todos os efeitos externos como indisponíveis.

```text
EXTERNAL_EFFECTS=NO
REAL_CLICK=NO
BROKER_CONNECTION=NO
LIVE_MODE=NO
DATABASE=NO
SIGNAL_ENGINE=NO
```

## Testes previstos

1. configuração padrão local e `NULL_ONLY`;
2. rejeição de modo diferente de `NULL`;
3. rejeição de host externo e porta privilegiada;
4. saúde em `SAFE_IDLE` após startup;
5. correlação ponta a ponta entre `HealthResponse.trace_id` e o evento de auditoria correspondente;
6. capacidades fail-closed;
7. adaptador `NULL` sem efeito externo;
8. varredura do pacote novo contra imports e marcadores proibidos.

## Remediação LEA-44

```text
LEA_44_F01=REMEDIATED
LEA_44_F02=REMEDIATED
RETEST_REQUIRED=YES
MERGE_AUTHORIZED=NO
```

- `LEA-44-F01`: o serviço gera um único `trace_id` por leitura de saúde e o reutiliza na resposta e no evento `health_snapshot_returned`;
- `LEA-44-F02`: o manifesto registra PR #64, LEA-44, modo Draft, HEAD observado e estado de reteste;
- o teste de integração exige igualdade de `trace_id` e `reason_code` entre resposta e auditoria.

## Rollback

Reverter o PR da LEA-43. O entrypoint legado não é modificado e permanece disponível durante toda a FND-001.

## Limites

Sem banco, SQL, migrations, Android, OCR, motores de sinal, automação física, corretora ou LIVE.
