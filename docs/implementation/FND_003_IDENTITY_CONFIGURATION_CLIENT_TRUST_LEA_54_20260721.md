# FND-003 — Identity, Configuration and Client Trust

## Autoridade e limites

```text
BUILDER_ISSUE=LEA-54
REVIEW_ISSUE=LEA-55
BASE_MAIN_SHA=4d62143e32ac289ba71dbd14e6da07fd7e938ec9
BRANCH=leonpcsn/fnd-003-identity-configuration-client-trust
VERSION_TARGET=V2.5.0-alpha.1
MODE_MAX=NULL_ONLY
MERGE_AUTHORIZED=NO
```

Fundamento normativo: DOM-02 e DOM-05; H-09; requisitos PTM-V25-002,
PTM-V25-008, PTM-V25-009, PTM-V25-016, PTM-V25-017 e PTM-V27-020;
ADRs ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0008 e ADR-0012.

## Resultado testável

Um administrador local com segredo fornecido exclusivamente pelo ambiente cria um
desafio de pareamento temporário. O desafio é armazenado apenas como hash, expira e
só pode ser consumido uma vez. Dispositivo e operador possuem identificadores
separados. O cliente pareado recebe sessão curta, rotativa e revogável, sempre com
perfil `READ_ONLY` e sem grant implícito.

O cliente identificado pode consultar o snapshot de capacidades e registrar
presença. Presença ou reconexão nunca autorizam comando. Revogação do dispositivo
encerra suas sessões.

## Resolução de configuração e segredos

Precedência canônica:

```text
DEFAULTS
→ ARQUIVO_JSON_EXPLICITAMENTE_AUTORIZADO
→ VARIÁVEIS_DE_AMBIENTE
```

- o modo aceito permanece exclusivamente `NULL`;
- arquivo indicado por ambiente deve estar em `config/`;
- chaves desconhecidas causam falha fechada;
- segredos não são permitidos no JSON e não são registrados;
- `PREDIXAI_ADMIN_SECRET` existe apenas em memória como `SecretStr`;
- desabilitar identidade faz todos os endpoints da capacidade falharem fechados.

## Contratos adicionados

```text
POST /api/v1/identity/pairing/challenges
POST /api/v1/identity/pair
POST /api/v1/identity/sessions/renew
POST /api/v1/identity/presence
GET  /api/v1/identity/capabilities
POST /api/v1/identity/devices/{device_id}/revoke
```

Não foram adicionados banco, SQL, migrations, corretora, clique, modo simulado,
CONTROLLED_UI, LIVE ou efeito financeiro.

## Testes e evidência

As famílias de teste cobrem:

- resolução defaults → JSON → ambiente e rejeição de segredo em arquivo;
- desafio único e expirável;
- separação dispositivo/operador e sessão curta;
- rotação e revogação;
- presença sem autorização;
- rejeição de autoelevação de perfil;
- consulta identificada das capacidades `NULL_ONLY`;
- regressão cumulativa da suíte anterior;
- Ruff, Mypy e compilação.

Comando único previsto para Linux Mint, no repositório limpo:

```bash
./scripts/validate_fnd_003_local.sh --expected-commit <HEAD_EXATO_DO_PR_DRAFT>
```

O executor atualiza a referência remota, confirma repositório/branch/commit, cria
checkout temporário isolado, instala dependências, executa toda a suíte, validação
estática e smoke FND-003, gera `reports/local/FND_003_LOCAL_VALIDATION_*.txt` e
remove o checkout temporário. A cópia de trabalho original não é trocada.

Sem relatório produzido no Linux Mint do Leo:

```text
LOCAL_LINUX_MINT_TEST=⏳ AGUARDANDO EXECUÇÃO DO LEO
LOCAL_REPORT_TXT=⏳ AGUARDANDO EXECUÇÃO DO LEO
```

## Rollback e próximo gate

```text
ROLLBACK_BRANCH=git switch main
ROLLBACK_AFTER_MERGE=git revert <MERGE_COMMIT>
NEXT_GATE=INDEPENDENT_CRITICAL_REVIEW_LEA_55
NEXT_INCREMENT=DAT-001
NEXT_INCREMENT_AUTHORIZED=NO
```

O rollback por `git revert` é somente referência para decisão humana futura; este
builder não possui autorização de merge ou revert na `main`.
