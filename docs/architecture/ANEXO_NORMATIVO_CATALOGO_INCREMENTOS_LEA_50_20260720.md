# ANEXO NORMATIVO — CATÁLOGO DE INCREMENTOS

```text
DOCUMENT_TYPE=NORMATIVE_ANNEX
PARENT_AUTHORITY=DOCUMENTO_MESTRE
CAN_OVERRIDE_MASTER=NO
REQUIRED_FOR_MASTER_VALIDITY=YES
MISSION=LEA-50
STATUS=CANDIDATE_AWAITING_INDEPENDENT_RETEST
```

## 01. FND-001 — Safe Server Foundation

```text
ID=FND-001
NOME=Safe Server Foundation
OBJETIVO=Estabelecer autoridade modular local, contratos v1, configuração fail-closed, estados mínimos, auditoria e adaptador NULL.
RESULTADO_TESTÁVEL=Servidor local entra em SAFE_IDLE e prova ausência de efeito externo.
ESCOPO=DOM-01, DOM-02, DOM-16; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=ARCHITECTURE_V1_FROZEN
DOMÍNIOS=DOM-01, DOM-02, DOM-16
HANDOFFS=H-11
REQUISITOS=PTM-V25-001,PTM-V25-004,PTM-V25-005,PTM-V25-006,PTM-V25-012,PTM-V25-013,PTM-V25-015D,PTM-V25-018,V25-CFG-001,V25-CFG-002,V25-CFG-003,V25-CFG-004,V25-DOC-001,V25-QA-001,V25-SEC-001,V25-SRV-001,V25-SRV-002,V25-SRV-003,V25-SRV-004
ADRS=ADR-0001,ADR-0002,ADR-0003,ADR-0004,ADR-0009,ADR-0010,ADR-0012,ADR-0018
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=INTEGRATED
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-ADP-*,T-CFG-*,T-DB-*,T-E2E-*,T-GOV-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→FND-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_fnd_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/FND-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=acoplamento ao legado; configuração permissiva
GATE_DE_SAÍDA=FND-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.4.3-R1+fnd.001
PRÓXIMO_INCREMENTO=FND-002
```

## 02. FND-002 — Safe Runtime Read Model

```text
ID=FND-002
NOME=Safe Runtime Read Model
OBJETIVO=Expor snapshot, auditoria e diagnóstico somente leitura sem mutar o runtime.
RESULTADO_TESTÁVEL=Consultas versionadas preservam contagem e estado da auditoria.
ESCOPO=DOM-03, DOM-16; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=FND-001
DOMÍNIOS=DOM-03, DOM-16
HANDOFFS=H-11
REQUISITOS=PTM-V25-015A,V26-API-001,V26-API-002,V27-OBS-001,V27-OBS-004
ADRS=ADR-0003,ADR-0012
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=INTEGRATED
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-DB-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→FND-002 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/validate_fnd_002_local.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/FND-002_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=efeito colateral em leitura; exposição excessiva
GATE_DE_SAÍDA=FND-002_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.4.3-R1+fnd.002
PRÓXIMO_INCREMENTO=FND-003
```

## 03. FND-003 — Identity, Configuration and Client Trust

```text
ID=FND-003
NOME=Identity, Configuration and Client Trust
OBJETIVO=Completar configuração resolvida, identidade, segredos, pareamento, revogação e presença humana sob autoridade do servidor.
RESULTADO_TESTÁVEL=Cliente identificado e revogável consulta capacidades sem obter grant implícito.
ESCOPO=DOM-02, DOM-05; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=FND-002
DOMÍNIOS=DOM-02, DOM-05
HANDOFFS=H-09
REQUISITOS=PTM-V25-002,PTM-V25-008,PTM-V25-009,PTM-V25-016,PTM-V25-017,PTM-V27-020
ADRS=ADR-0001,ADR-0002,ADR-0003,ADR-0004,ADR-0008,ADR-0012
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=CANDIDATE_NOT_AUTHORIZED
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-CFG-*,T-CMD-*,T-DB-*,T-E2E-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→FND-003 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_fnd_003.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/FND-003_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=segredo em log; cache virar autoridade
GATE_DE_SAÍDA=FND-003_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.5.0-alpha.1
PRÓXIMO_INCREMENTO=DAT-001
```

## 04. DAT-001 — Durable State and Legacy Migration

```text
ID=DAT-001
NOME=Durable State and Legacy Migration
OBJETIVO=Introduzir persistência V1, escritor único, eventos, backup, restore e importação idempotente do legado.
RESULTADO_TESTÁVEL=Estado durável restaura com integridade e rollback comprovado.
ESCOPO=DOM-03; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=FND-003
DOMÍNIOS=DOM-03
HANDOFFS=H-11
REQUISITOS=PTM-V25-003,PTM-V25-014A,PTM-V25-014B,PTM-V25-014C,PTM-V25-014D,PTM-V25-014E,PTM-V26-023,PTM-V26-027,PTM-V27-029,V25-DB-001,V25-DB-002,V25-DB-003,V25-DB-004,V25-DB-005,V25-LEG-001,V25-LEG-002,V25-LEG-003,V25-LEG-004,V25-LEG-005,V25-LEG-006
ADRS=ADR-0001,ADR-0002,ADR-0003,ADR-0013
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-CFG-*,T-DB-*,T-REC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→DAT-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_dat_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/DAT-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=perda de dados; migration irreversível
GATE_DE_SAÍDA=DAT-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.5.0-alpha.2
PRÓXIMO_INCREMENTO=LST-001
```

## 05. LST-001 — Lists and Scheduling

```text
ID=LST-001
NOME=Lists and Scheduling
OBJETIVO=Implementar listas, itens, revisões e agendamentos independentes de análise e execução.
RESULTADO_TESTÁVEL=CRUD e importação preservam revisão e nunca iniciam observação automaticamente.
ESCOPO=DOM-04; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=DAT-001
DOMÍNIOS=DOM-04
HANDOFFS=H-01
REQUISITOS=PTM-V25-007,V25-LIST-001,V25-LIST-002,V25-LIST-003,V25-LIST-004,V25-QA-002
ADRS=ADR-0001,ADR-0002,ADR-0009,ADR-0018
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-E2E-*,T-LIST-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→LST-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_lst_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/LST-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=lista acionar efeito; importação ambígua
GATE_DE_SAÍDA=LST-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.5.0-alpha.3
PRÓXIMO_INCREMENTO=PRF-001
```

## 06. PRF-001 — Profiles, ROIs and Logical Geometry

```text
ID=PRF-001
NOME=Profiles, ROIs and Logical Geometry
OBJETIVO=Versionar perfis, monitor, ROIs, âncoras, calibração e identidade lógica do alvo.
RESULTADO_TESTÁVEL=Perfil incompatível falha fechado e coordenada isolada não autoriza ação.
ESCOPO=DOM-06; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=LST-001
DOMÍNIOS=DOM-06
HANDOFFS=H-02
REQUISITOS=PTM-V25-010,PTM-V25-011A,PTM-V25-011B,PTM-V25-011C,PTM-V25-011D
ADRS=ADR-0005
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-ADP-*,T-CFG-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→PRF-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_prf_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/PRF-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=drift geométrico; coordenada tratada como identidade
GATE_DE_SAÍDA=PRF-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.5.0-beta.1
PRÓXIMO_INCREMENTO=OBS-001
```

## 07. OBS-001 — Authorized Observation Session

```text
ID=OBS-001
NOME=Authorized Observation Session
OBJETIVO=Criar lifecycle de sessão vinculado a lista, perfil e fonte visual autorizada.
RESULTADO_TESTÁVEL=Perda de identidade da fonte degrada a sessão e bloqueia captura.
ESCOPO=DOM-07; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=PRF-001
DOMÍNIOS=DOM-07
HANDOFFS=H-02, H-03
REQUISITOS=PTM-V26-002,PTM-V26-003,V26-OBS-001,V26-OBS-002,V26-OBS-003,V26-OBS-004
ADRS=ADR-0005,ADR-0014
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-OBS-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→OBS-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_obs_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/OBS-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=fonte errada; sessão órfã
GATE_DE_SAÍDA=OBS-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.6.0-alpha.1
PRÓXIMO_INCREMENTO=CAP-001
```

## 08. CAP-001 — Frame Capture and Provenance

```text
ID=CAP-001
NOME=Frame Capture and Provenance
OBJETIVO=Capturar frames com hash, origem, sequência, ROI, linhagem e retenção.
RESULTADO_TESTÁVEL=Frame sem proveniência é rejeitado antes da validação.
ESCOPO=DOM-08; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=OBS-001
DOMÍNIOS=DOM-08
HANDOFFS=H-04
REQUISITOS=PTM-V26-004,V26-CAP-001,V26-CAP-002,V26-CAP-003,V26-CAP-004
ADRS=ADR-0014
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-CAP-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→CAP-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_cap_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/CAP-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=retenção excessiva; frame sem linhagem
GATE_DE_SAÍDA=CAP-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.6.0-alpha.2
PRÓXIMO_INCREMENTO=VAL-001
```

## 09. VAL-001 — Visual Quality Gate

```text
ID=VAL-001
NOME=Visual Quality Gate
OBJETIVO=Aplicar checks explícitos de qualidade, elegibilidade, blockers e caps conservadores.
RESULTADO_TESTÁVEL=FAIL ou UNKNOWN impede extração.
ESCOPO=DOM-09; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=CAP-001
DOMÍNIOS=DOM-09
HANDOFFS=H-05
REQUISITOS=PTM-V26-005,PTM-V26-006,V26-VAL-001,V26-VAL-002,V26-VAL-003,V26-VAL-004,V26-VAL-005,V26-VAL-006
ADRS=ADR-0014,ADR-0017
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-VAL-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→VAL-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_val_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/VAL-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=falso positivo; UNKNOWN promovido a PASS
GATE_DE_SAÍDA=VAL-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.6.0-alpha.3
PRÓXIMO_INCREMENTO=MAP-001
```

## 10. MAP-001 — Estimated Data Extraction

```text
ID=MAP-001
NOME=Estimated Data Extraction
OBJETIVO=Extrair dados estimados com mapping versionado, incerteza e linhagem.
RESULTADO_TESTÁVEL=Mapping incompatível bloqueia snapshot analítico.
ESCOPO=DOM-10; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=VAL-001
DOMÍNIOS=DOM-10
HANDOFFS=H-06
REQUISITOS=PTM-V26-007,PTM-V26-008,V26-MAP-001,V26-MAP-002,V26-MAP-003,V26-MAP-004,V26-MAP-005
ADRS=ADR-0017
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-MAP-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→MAP-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_map_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/MAP-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=OCR tratado como verdade; mapping incompatível
GATE_DE_SAÍDA=MAP-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.6.0-beta.1
PRÓXIMO_INCREMENTO=ANA-001
```

## 11. ANA-001 — Deterministic Engines A-H

```text
ID=ANA-001
NOME=Deterministic Engines A-H
OBJETIVO=Executar motores A-H determinísticos sobre snapshot elegível e imutável.
RESULTADO_TESTÁVEL=Replay idêntico produz resultados equivalentes sem efeito físico.
ESCOPO=DOM-11; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=MAP-001
DOMÍNIOS=DOM-11
HANDOFFS=H-07; H-08
REQUISITOS=PTM-V26-001,PTM-V26-009,PTM-V26-010,PTM-V26-011,PTM-V26-012,PTM-V26-013,PTM-V26-014,PTM-V26-015,PTM-V26-016,PTM-V26-017,PTM-V26-018,V26-ANA-001,V26-ANA-002,V26-ANA-003,V26-ANA-004,V26-ANA-005,V26-ANA-006,V26-ANA-007,V26-ANA-008,V26-ANA-009,V26-ANA-010,V26-ANA-011
ADRS=ADR-0006,ADR-0008,ADR-0009,ADR-0017
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-ANA-*,T-CMD-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→ANA-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_ana_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/ANA-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=não determinismo; motor contornar blocker
GATE_DE_SAÍDA=ANA-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.6.0-beta.2
PRÓXIMO_INCREMENTO=SIG-001
```

## 12. SIG-001 — Strategy and Signal Lifecycle

```text
ID=SIG-001
NOME=Strategy and Signal Lifecycle
OBJETIVO=Implementar estratégia explicável, candidatos, arbitragem, sinais, expiração e invalidação.
RESULTADO_TESTÁVEL=Sinal auditável expira e nunca autoexecuta.
ESCOPO=DOM-12; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=ANA-001
DOMÍNIOS=DOM-12
HANDOFFS=H-08
REQUISITOS=PTM-V26-019,PTM-V26-020,PTM-V26-021,PTM-V26-022,V26-SIG-001,V26-SIG-002,V26-SIG-003,V26-SIG-004,V26-SIG-005,V26-SIG-006,V26-SIG-007,V26-SIG-008,V26-STR-001,V26-STR-002,V26-STR-003,V26-STR-004
ADRS=ADR-0007
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-CMD-*,T-SIG-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→SIG-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_sig_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/SIG-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=sinal virar comando; expiração inconsistente
GATE_DE_SAÍDA=SIG-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.6.0-rc.1
PRÓXIMO_INCREMENTO=CMD-001
```

## 13. CMD-001 — Command, Grant and Policy Engine

```text
ID=CMD-001
NOME=Command, Grant and Policy Engine
OBJETIVO=Separar sinal, comando imutável, grant humano, revogação, revalidação e policy engine.
RESULTADO_TESTÁVEL=Comando sem grant válido é rejeitado com reason_code.
ESCOPO=DOM-13; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=SIG-001
DOMÍNIOS=DOM-13
HANDOFFS=H-08, H-09; H-08..H-10; H-09; H-09, H-12
REQUISITOS=PTM-V27-001,PTM-V27-002,PTM-V27-004,PTM-V27-005,PTM-V27-006,PTM-V27-007,V27-AUT-001,V27-AUT-002,V27-AUT-003,V27-AUT-004,V27-AUT-005,V27-AUT-006,V27-CMD-001,V27-CMD-002,V27-CMD-003,V27-CMD-004,V27-CMD-005,V27-CMD-006,V27-PRE-001,V27-PRE-002,V27-PRE-003,V27-PRE-004,V27-PRE-005,V27-PRE-006,V27-SAF-001,V27-SAF-008
ADRS=ADR-0004,ADR-0008,ADR-0009,ADR-0010,ADR-0011,ADR-0016
MODO_MÁXIMO=NULL_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-CMD-*,T-EXE-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→CMD-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_cmd_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/CMD-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=grant implícito; revalidação omitida
GATE_DE_SAÍDA=CMD-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.7.0-alpha.1
PRÓXIMO_INCREMENTO=ADP-001
```

## 14. ADP-001 — Allowlisted Target and Simulated Adapter

```text
ID=ADP-001
NOME=Allowlisted Target and Simulated Adapter
OBJETIVO=Resolver alvo lógico allowlisted e habilitar adaptadores NULL e SIMULATED declarados.
RESULTADO_TESTÁVEL=Alvo desconhecido bloqueia dispatch e simulação não produz efeito externo.
ESCOPO=DOM-14; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=CMD-001
DOMÍNIOS=DOM-14
HANDOFFS=H-09, H-10
REQUISITOS=PTM-V27-008
ADRS=ADR-0005,ADR-0009
MODO_MÁXIMO=SIMULATED
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-ADP-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→ADP-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_adp_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/ADP-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=alvo incorreto; elevação silenciosa de modo
GATE_DE_SAÍDA=ADP-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.7.0-alpha.2
PRÓXIMO_INCREMENTO=EXE-001
```

## 15. EXE-001 — Simulated Dispatch, Receipt and Recovery

```text
ID=EXE-001
NOME=Simulated Dispatch, Receipt and Recovery
OBJETIVO=Implementar intent-before-effect simulado, serialização, idempotência, timeout, retry, circuito, recibo e recovery.
RESULTADO_TESTÁVEL=Fluxo simulado reconcilia recibo e restart não reenvia automaticamente.
ESCOPO=DOM-15; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=ADP-001
DOMÍNIOS=DOM-15
HANDOFFS=H-10; H-10, H-11; H-10, H-12; H-11
REQUISITOS=PTM-V27-010,PTM-V27-011,PTM-V27-012,PTM-V27-013,PTM-V27-014,PTM-V27-015,PTM-V27-016,PTM-V27-017,PTM-V27-018,PTM-V27-022,PTM-V27-023,PTM-V27-024,PTM-V27-025,PTM-V27-030,V27-EXE-001,V27-EXE-002,V27-EXE-005,V27-EXE-006,V27-EXE-007,V27-REC-001,V27-REC-002,V27-REC-003,V27-REC-004,V27-REC-005,V27-REC-006,V27-SAF-002,V27-SAF-003
ADRS=ADR-0011,ADR-0015,ADR-0016
MODO_MÁXIMO=SIMULATED
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-EXE-*,T-REC-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→EXE-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_exe_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/EXE-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=duplicidade; timeout presumido como ausência de efeito
GATE_DE_SAÍDA=EXE-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.7.0-beta.1
PRÓXIMO_INCREMENTO=SEC-001
```

## 16. SEC-001 — Containment, Observability and Cumulative Simulation

```text
ID=SEC-001
NOME=Containment, Observability and Cumulative Simulation
OBJETIVO=Completar redaction, auditoria, métricas, tracing, kill switch, provas negativas e E2E simulado acumulado.
RESULTADO_TESTÁVEL=Kill switch domina fila e suíte cumulativa prova efeito financeiro real ausente.
ESCOPO=DOM-16; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=EXE-001
DOMÍNIOS=DOM-16
HANDOFFS=H-11; H-12
REQUISITOS=PTM-V25-015B,PTM-V25-015C,PTM-V25-015E,PTM-V26-024,PTM-V26-025,PTM-V26-026,PTM-V26-028,PTM-V27-019,PTM-V27-026,PTM-V27-027,PTM-V27-028,PTM-V27-031,V26-RPL-001,V26-RPL-002,V26-RPL-003,V26-SEC-001,V26-SEC-002,V26-SEC-003,V27-EXE-008,V27-OBS-002,V27-OBS-003,V27-OBS-005,V27-QA-001,V27-QA-002,V27-QA-003,V27-QA-004,V27-QA-005,V27-QA-006,V27-QA-007
ADRS=ADR-0009,ADR-0010,ADR-0012,ADR-0014,ADR-0018
MODO_MÁXIMO=SIMULATED
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-E2E-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→SEC-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_sec_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/SEC-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=bypass de contenção; evidência incompleta
GATE_DE_SAÍDA=SEC-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.7.0-rc.1
PRÓXIMO_INCREMENTO=CUI-001
```

## 17. CUI-001 — Controlled UI Capability

```text
ID=CUI-001
NOME=Controlled UI Capability
OBJETIVO=Adicionar resolução e adaptador CONTROLLED_UI somente em alvo próprio/controlado, com allowlist, confirmação e contenção.
RESULTADO_TESTÁVEL=Harness controlado executa UI sem corretora, saldo ou ordem real.
ESCOPO=DOM-14, DOM-16; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=SEC-001
DOMÍNIOS=DOM-14, DOM-16
HANDOFFS=H-09, H-10; H-10; H-10, H-12
REQUISITOS=PTM-V27-003,PTM-V27-009,PTM-V27-021,V27-EXE-003,V27-EXE-004,V27-SAF-004,V27-SAF-005,V27-SAF-006,V27-SAF-007
ADRS=ADR-0005,ADR-0009,ADR-0010,ADR-0012
MODO_MÁXIMO=CONTROLLED_UI
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-ADP-*,T-EXE-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→CUI-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_cui_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/CUI-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=alvo não autorizado; confusão com LIVE
GATE_DE_SAÍDA=CUI-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=V2.7.0-cui.1
PRÓXIMO_INCREMENTO=LIV-GATE-001
```

## 18. LIV-GATE-001 — Future LIVE_GATED Change Control

```text
ID=LIV-GATE-001
NOME=Future LIVE_GATED Change Control
OBJETIVO=Manter o modo financeiro real bloqueado até missão futura técnica, comercial, jurídica, regulatória e humana.
RESULTADO_TESTÁVEL=Change control registra decisão; nenhum runtime LIVE é armado automaticamente.
ESCOPO=DOM-01, DOM-16; contratos e testes vinculados
FORA_DE_ESCOPO=escopo posterior; efeito financeiro real; elevação silenciosa de modo
DEPENDE_DE=CUI-001
DOMÍNIOS=DOM-01, DOM-16
HANDOFFS=H-12
REQUISITOS=PTM-V27-032
ADRS=ADR-0009,ADR-0010
MODO_MÁXIMO=LIVE_GATED_CAPABILITY_ONLY
SITUAÇÃO_ATUAL=BLOCKED_BY_PREDECESSOR
CRITÉRIOS_DE_ENTRADA=PREDECESSORS_PASS + HUMAN_MISSION_AUTHORIZATION + EXPECTED_MAIN_SHA_MATCH
ENTREGAS=implementação pequena; contratos; documentação; evidências; script local do incremento
TESTES_UNITÁRIOS=T-GOV-*,T-SEC-* unitários do incremento
TESTES_DE_INTEGRAÇÃO=handoffs afetados + contratos versionados
TESTES_DE_REGRESSÃO=toda suíte anterior sem remoção, desativação ou ignore oportunista
TESTE_CUMULATIVO=fluxo FND-001→LIV-GATE-001 até a fronteira autorizada
TESTE_LOCAL_DO_LEO=script fail-closed fixa repositório, commit, versão, testes e relatório
COMANDO_ÚNICO_LOCAL=bash scripts/local_validate_liv_gate_001.sh --expected-commit <CANDIDATE_HEAD>
EVIDÊNCIAS=CI; revisão independente; reports/local/LIV-GATE-001_<COMMIT>.txt (não versionado)
ROLLBACK=reverter PR do incremento; restaurar tag/commit predecessor; executar regressão cumulativa
RISCOS=autorização implícita; conflito regulatório
GATE_DE_SAÍDA=LIV-GATE-001_EXIT_PASS:UNIT=PASS;INTEGRATION=PASS;REGRESSION=PASS;CUMULATIVE=PASS;SECURITY_NEGATIVE=PASS;CI=PASS;INDEPENDENT_REVIEW=PASS;LOCAL_LINUX_MINT=PASS;LOCAL_REPORT=PROVIDED;TECHNICAL_DEBT=PASS
VERSÃO_PREVISTA=TBD_BY_FUTURE_CHANGE_CONTROL
PRÓXIMO_INCREMENTO=NONE_AUTOMATIC
```
