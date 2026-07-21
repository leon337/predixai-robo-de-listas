# PROMPT — REVISÃO CRÍTICA INDEPENDENTE FND-003 / LEA-55

## Cabeçalho obrigatório

```text
MISSION=LEA-55_FND-003_INDEPENDENT_CRITICAL_REVIEW
BUILDER_ISSUE=LEA-54
REVIEW_ISSUE=LEA-55
REPOSITORY=leon337/predixai-robo-de-listas
BASE_MAIN_SHA=4d62143e32ac289ba71dbd14e6da07fd7e938ec9
PULL_REQUEST=OBTER_DO_HANDOFF
REVIEW_HEAD=OBTER_DO_PR_DRAFT_E_FIXAR_EXTERNAMENTE
BRANCH=leonpcsn/fnd-003-identity-configuration-client-trust
MODE_MAX=NULL_ONLY
BUILDER_IS_REVIEWER=NO
MERGE_AUTHORIZED=NO
NEXT_INCREMENT_AUTHORIZED=NO
LIVE_MODE_ARMED=NO
```

## Missão do revisor

Revisar integralmente o diff `BASE_MAIN_SHA...REVIEW_HEAD`, o PR Draft, a LEA-54,
a LEA-55, o Documento Mestre e as evidências de CI. Não confiar apenas no relatório
do builder. O revisor deve ser diferente do builder e ancorar sua decisão no HEAD
exato.

## Escopo normativo

Confirmar rastreabilidade exclusiva a DOM-02, DOM-05, H-09,
PTM-V25-002/008/009/016/017, PTM-V27-020 e ADR-0001/0002/0003/0004/0008/0012.
Nenhum requisito, domínio, handoff ou ADR pode ser criado ou alterado.

## Verificações bloqueadoras

1. configuração resolvida na precedência defaults → JSON autorizado → ambiente;
2. somente `NULL` é aceito e toda configuração inválida falha fechada;
3. segredos não podem vir do JSON, aparecer em resposta, log, auditoria ou `repr`;
4. desafio de pareamento é local, aleatório, armazenado como hash, temporário,
   de uso único e não reutilizável;
5. identificadores de dispositivo e operador permanecem separados;
6. cliente não escolhe perfil elevado; sessão emitida é apenas `READ_ONLY`;
7. sessão é curta, rotativa e revogável; token anterior para de funcionar;
8. revogação de dispositivo encerra sessões existentes;
9. presença e reconexão não criam grant de comando;
10. capacidades identificadas continuam `NULL_ONLY`, sem clique, corretora, efeito
    externo, modo simulado, CONTROLLED_UI ou LIVE;
11. testes unitários, integração, regressão cumulativa e negativos de segurança
    são objetivos e exercitam comportamento, não apenas presença de texto;
12. executor Linux Mint protege alterações locais, fixa o commit, usa checkout
    isolado, testa e gera relatório TXT;
13. GitHub Actions do HEAD estão concluídas e aprovadas;
14. documentação, GitHub e Linear apontam para o mesmo candidato;
15. não há SQL, migration, banco, Android, OCR ou implementação de incremento futuro.

## Reprodução mínima

```bash
git diff --check 4d62143e32ac289ba71dbd14e6da07fd7e938ec9...<REVIEW_HEAD>
bash -n scripts/validate_fnd_003_local.sh
python3 -m compileall -q server tests
python3 -m pytest -q
ruff check server tests
mypy server --ignore-missing-imports
```

No Linux Mint, executar também:

```bash
./scripts/validate_fnd_003_local.sh --expected-commit <REVIEW_HEAD>
```

Se a evidência local do Leo não tiver sido fornecida, registrar exatamente
`⏳ AGUARDANDO EXECUÇÃO DO LEO`; não fabricar PASS.

## Saída obrigatória

```text
REVIEW_HEAD=
DECISION=PASS|PASS_WITH_CONDITIONS|FAIL
CRITICAL_FINDINGS=
MAJOR_FINDINGS=
MINOR_FINDINGS=
OPEN_BLOCKING_FINDINGS=
CI_RESULT=
LOCAL_LINUX_MINT_RESULT=
ARCHITECTURE_CHANGE=NO|YES
APPLICATION_SCOPE_OUTSIDE_FND_003=NO|YES
MERGE_AUTHORIZED=NO
NEXT_INCREMENT_AUTHORIZED=NO
NEXT_GATE=
```

Publicar a revisão no PR e na LEA-55. Não aprovar trabalho próprio, não promover o
PR para ready, não fazer merge e não autorizar DAT-001.
