# ANEXO NORMATIVO — POLÍTICAS DE EXECUÇÃO INCREMENTAL

```text
DOCUMENT_TYPE=NORMATIVE_ANNEX
PARENT_AUTHORITY=DOCUMENTO_MESTRE
CAN_OVERRIDE_MASTER=NO
REQUIRED_FOR_MASTER_VALIDITY=YES
MISSION=LEA-50
STATUS=CANDIDATE_AWAITING_INDEPENDENT_RETEST
```

## Testes cumulativos

```text
ETAPA_1=TESTAR_1
ETAPA_2=TESTAR_1+TESTAR_2+INTEGRAR_1_2+FLUXO_1_2
ETAPA_3=TESTAR_1_2_3+INTEGRAÇÕES_AFETADAS+FLUXO_1_2_3
ETAPA_N=TESTAR_N+REGRESSÃO_1_A_N-1+INTEGRAÇÕES_AFETADAS+FLUXO_1_A_N

STAGE_N_CAN_ADVANCE_ONLY_IF=
STAGES_1_TO_N_PASS
AND CUMULATIVE_INTEGRATION_PASS
AND LOCAL_TEST_PASS
AND TECHNICAL_DEBT_GATE_PASS
```

Nenhum teste antigo pode ser removido, desabilitado ou ignorado para promover um incremento.

## Gate de conclusão

```text
CODE_COMPLETE=YES
UNIT_TESTS=PASS
INTEGRATION_TESTS=PASS
PREVIOUS_STAGE_REGRESSION=PASS
CUMULATIVE_FLOW_TEST=PASS
SECURITY_NEGATIVE_TESTS=PASS
CI=PASS
INDEPENDENT_CRITICAL_REVIEW=PASS
LOCAL_LINUX_MINT_TEST=PASS
LOCAL_REPORT_TXT=PROVIDED
GITHUB_LINEAR_SYNC=PASS
TECHNICAL_DEBT_GATE=PASS
```

## Sincronização local

Cada missão deve publicar `scripts/local_validate_<incremento>.sh` fail-closed. O comando único deve confirmar repositório, commit e versão esperados; proteger alterações locais; atualizar por fast-forward; preparar dependências; executar testes novos, regressão e fluxo cumulativo; permitir inspeção da entrega; gerar TXT; mostrar PASS/FAIL; preservar rollback; e manter backup/relatório fora do Git.

```text
LOCAL_SYNC_COMMAND=bash scripts/local_validate_<incremento>.sh --expected-commit <CANDIDATE_HEAD>
EXPECTED_COMMIT=FIXADO_NO_HEAD_CANDIDATO
EXPECTED_VERSION=CATÁLOGO_DO_INCREMENTO
TEST_COMMAND=DEFINIDO_NA_MISSÃO_DO_INCREMENTO
REPORT_PATH=reports/local/<incremento>_<commit>.txt
ROLLBACK_COMMAND=bash scripts/local_validate_<incremento>.sh --rollback-to <PREDECESSOR_SHA>
EXPECTED_RESULT=PASS_WITH_REPORT
MISSING_REAL_LOCAL_EVIDENCE=⏳_AGUARDANDO_EXECUÇÃO_DO_LEO
```

O Leo não cria branch, commit, push, PR, stash nem resolve divergências no fluxo normal.

## Versionamento

| Tipo | Regra |
|---|---|
| incremento funcional | avança pre-release previsto após todos os gates |
| correção | preserva incremento e adiciona patch/remediation |
| remediação | novo HEAD na mesma missão, sem promoção automática |
| release candidata | tag candidata somente após CI, revisão e teste local |
| release integrada | versão após merge autorizado e recibo pós-merge |
| versão local | commit e versão confirmados pelo relatório TXT |

FND-001 e FND-002 preservam seus IDs e a versão operacional histórica `V2.4.3-R1`; os sufixos `+fnd.001` e `+fnd.002` são referências de evidência, não renumeração retroativa.

```text
VERSION
TAG_CANDIDATE
COMMIT_SHA
PR
LINEAR_ISSUE
REQUIREMENTS_COVERED
TEST_RESULTS
LOCAL_REPORT
ROLLBACK_REFERENCE
```

## Dívida técnica

Toda dívida deve existir no Linear com risco, origem, impacto, responsável, gate de correção e decisão explícita. Teste quebrado, contrato temporário oculto, bypass, TODO crítico, dependência injustificada, falha de integração, documentação divergente, legado não isolado ou defeito que invalide o próximo incremento bloqueia avanço.

```text
CRITICAL_OR_BLOCKING_TECHNICAL_DEBT=BLOCKS_ADVANCE
SILENT_DEBT=PROHIBITED
TECHNICAL_DEBT_GATE=PASS_REQUIRED
```

## Capacidades e autorização humana

```text
NULL_ONLY→SIMULATED→CONTROLLED_UI→LIVE_GATED
REAL_FINANCIAL_EFFECT=NO
BROKER_CONNECTION=NO
REAL_CLICK=NO
LIVE_MODE_ARMED=NO
```

Cada mudança de capacidade exige missão própria, revisão crítica independente e autorização humana. `LIVE_GATED` é change control futuro, não etapa automática.
