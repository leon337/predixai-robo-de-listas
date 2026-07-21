# RELATÓRIO DE VALIDAÇÃO — FND-003 / LEA-54

## Escopo verificado

Implementação de configuração, identidade, pareamento, sessões, revogação,
presença e confiança de cliente sob `NULL_ONLY`, baseada em DOM-02, DOM-05, H-09,
seis requisitos e seis ADRs já aceitos.

## Evidência objetiva

```text
GITHUB_PR=71_DRAFT
FIRST_CANDIDATE_HEAD=f0c4d54552401c810a6d41ff78ce010c89bcd191
CI_REMEDIATION_HEAD=29274d5d1fdf1ecb8273718b2fa4b201232d9bcd
WORKFLOW_RUN_FND_003=29792919081
PYTEST=PASS_53_TESTS
RUFF_SERVER_AND_TESTS_SERVER=PASS
MYPY_SERVER=PASS
ALL_WORKFLOWS=PASS_11_OF_11
GIT_DIFF_CHECK=PASS
BASH_SYNTAX=PASS
PYTHON_COMPILEALL=PASS
AST_PARSE=PASS
```

O ambiente do builder não possuía FastAPI/Pytest instalados e não conseguiu baixar
dependências pela política de rede. Por isso, a execução Python foi comprovada no
GitHub Actions, não declarada como execução local do builder.

## Testes de segurança incluídos

- segredo ausente ou incorreto é rejeitado e não aparece em saída/auditoria;
- segredo em JSON é proibido;
- modo diferente de `NULL` é rejeitado;
- desafio expira e não pode ser reutilizado;
- operador e dispositivo são vinculados no desafio administrativo;
- cliente não consegue substituir a identidade vinculada nem pedir `ADMIN`;
- token antigo falha após rotação;
- sessão expirada e dispositivo revogado falham fechados;
- presença e reconexão permanecem sem grant;
- capacidades não habilitam clique, corretora, efeito externo ou LIVE.

## Limite da prova

```text
LOCAL_LINUX_MINT_TEST=NOT_EXECUTED_BY_BUILDER
LOCAL_LINUX_MINT_STATUS=⏳ AGUARDANDO EXECUÇÃO DO LEO
LOCAL_REPORT_TXT=⏳ AGUARDANDO EXECUÇÃO DO LEO
INDEPENDENT_REVIEW=NOT_EXECUTED_BY_BUILDER
MERGE=NOT_EXECUTED
```

## Decisão do builder

```text
BUILDER_VALIDATION=PASS
FND_003_STATUS=CANDIDATE_AWAITING_INDEPENDENT_REVIEW
MERGE_AUTHORIZED=NO
NEXT_INCREMENT_AUTHORIZED=NO
NEXT_GATE=LEA_55
```
