# ANEXO A — APÊNDICE 01

## Grafo de imports, símbolos principais e schema JSON do legado

## 1. Controle

```text
DOCUMENT_STATUS=DRAFT_PARTIAL
PARENT_DOCUMENT=ANEXO_A_INVENTARIO_FACTUAL_LEGADO_PTP-GOV.6_20260716.md
REPOSITORY=leon337/predixai-robo-de-listas
SOURCE_BRANCH=main
SOURCE_COMMIT=0e2d7e98d863769be32a8bcb8b93684a61674aa3
CODE_CHANGED=NO
RUNTIME_EXECUTED=NO
```

## 2. Grafo direto de imports internos

```text
app/main.py
└── dependência externa: pynput

app/bootstrap_v21.py
└── main

app/bootstrap_v22.py
└── main

app/bootstrap_v22_entry.py
├── main
└── bootstrap_v22

app/bootstrap_v23.py
├── main
└── bootstrap_v22

app/bootstrap_v231.py
└── main

app/bootstrap_v232.py
├── main
├── bootstrap_v22
└── execution_preflight

app/bootstrap_v233.py
├── main
├── bootstrap_v22
└── version_info

app/bootstrap_v233_runtime.py
├── main
└── version_info

app/bootstrap_v242.py
├── main
└── config_safety

app/bootstrap_v243.py
├── main
└── diagnostics_tools

app/bootstrap_v23_entry.py
├── main
├── bootstrap_v22_entry
├── bootstrap_v23
├── bootstrap_v231
├── bootstrap_v232
├── bootstrap_v233
├── bootstrap_v233_runtime
├── bootstrap_v242
├── bootstrap_v243
└── runtime_guard
```

Módulos utilitários sem dependência interna relevante confirmada:

```text
version_info
execution_preflight
runtime_guard
config_safety
diagnostics_tools
```

## 3. Conclusão arquitetural do grafo

```text
GRAPH_SHAPE=STAR_AROUND_MAIN_WITH_ORDERED_MONKEY_PATCH_CHAIN
INTERNAL_LAYERING=NOT_EXPLICIT
DOMAIN_UI_EXECUTION_SEPARATION=NO
PATCH_ORDER_IS_BEHAVIORAL_DEPENDENCY=YES
CIRCULAR_IMPORT_EVIDENCE=NOT_CONFIRMED
```

Classificação: `SUBSTITUIR` o mecanismo de composição, mantendo comportamentos úteis como requisitos de regressão.

Certeza: alta para o grafo direto observado.

Risco: alto.

Motivos:

- quase todos os patches dependem diretamente de `main`;
- métodos da classe principal são substituídos em runtime;
- o resultado final depende da ordem de `install_patch()`;
- UI, domínio, persistência e execução permanecem ligados à mesma classe.

## 4. Símbolos principais confirmados

### 4.1 `app/main.py`

Classes:

- `Signal`;
- `ScheduleList`;
- `CoordinateProfile`;
- `PredixAIRoboListas`.

Responsabilidades observadas na classe principal:

- inicialização Tkinter;
- estilos e navegação;
- seleção de perfil e lista;
- criação, edição, exclusão e calibração de perfis;
- criação, edição, duplicação e exclusão de listas;
- criação e remoção de sinais;
- persistência JSON e migração de schemas anteriores;
- preparação e execução de sessão;
- thread de execução;
- pausa, cancelamento, histórico e resumo;
- captura de coordenadas;
- movimentação do mouse;
- teste real das duas coordenadas;
- clique agendado real.

Função de entrada:

- `main()`.

### 4.2 Utilitários

| Módulo | Símbolos confirmados |
|---|---|
| `version_info.py` | `read_app_version` |
| `execution_preflight.py` | `ScheduledSignal`, `split_signals_by_time` |
| `runtime_guard.py` | `DiagnosticResult`, `SingleInstanceLock`, `configure_logging`, `run_startup_diagnostics` |
| `config_safety.py` | `ConfigSafetyManager` |
| `diagnostics_tools.py` | `DiagnosticItem`, `read_version`, `collect_diagnostics`, `diagnostic_summary`, `export_diagnostic_report`, `open_path`, `run_installer`, `diagnostics_as_json` |

### 4.3 Patches

| Módulo | Responsabilidades/símbolos centrais confirmados |
|---|---|
| `bootstrap_v21.py` | rótulo e seleção de listas; `install_patch` |
| `bootstrap_v22.py` | listas independentes, schema JSON 4, histórico estruturado, exportação/gestão de listas; `install_patch` |
| `bootstrap_v22_entry.py` | ativação, exclusão e tela de perfis; `install` |
| `bootstrap_v23.py` | direção, agenda, cartões de listas e histórico mestre-detalhe; patch da classe principal |
| `bootstrap_v231.py` | eventos de pausa/parada, controles e loop de execução; `install_patch` |
| `bootstrap_v232.py` | payload de sessão, preflight, início/parada e status `EXPIRADA`; `install_patch` |
| `bootstrap_v233.py` | shell com versão e histórico responsivo |
| `bootstrap_v233_runtime.py` | título final baseado em `VERSION`; `install_patch` |
| `bootstrap_v242.py` | wrappers `_safe_load` e `_safe_save`; `install_patch` |
| `bootstrap_v243.py` | `show_tools`, `show_about` e extensão do shell; `install_patch` |
| `bootstrap_v23_entry.py` | `install` e `run` |

Este índice é funcional e preliminar. A contagem numérica integral de todos os métodos locais e funções aninhadas permanece pendente.

## 5. Modelo JSON schema 4

Arquivo operacional:

`config/config_predixai_robo_listas.json`

### 5.1 Campos de topo

```text
version
active_profile_id
active_list_id
profiles
lists
legacy_history
session_history
```

### 5.2 Perfil

```text
id
name
application
monitor
resolution
scale
coordinates
updated_at
validated
lists
```

No schema 4, `lists` dentro do perfil é gravado vazio; as listas ficam na coleção de topo.

### 5.3 Coordenadas

```text
coordinates.LARANJA = {x, y} | null
coordinates.CINZA   = {x, y} | null
```

Semântica factual:

- `LARANJA` corresponde a `PARA_CIMA` no loop de execução;
- `CINZA` corresponde a `PARA_BAIXO`;
- a validação do perfil depende de resolução, escala, presença das coordenadas e teste de cliques.

### 5.4 Lista

```text
id
name
date_str
description
created_at
updated_at
archived
signals
```

### 5.5 Sinal

```text
id
date_str
time_str
direction
status
```

Direções confirmadas:

```text
PARA_CIMA
PARA_BAIXO
```

Status observados:

```text
AGENDADO
EXECUTANDO
CLIQUE_ENVIADO
EXPIRADO
CANCELADO
ERRO
```

### 5.6 Sessão estruturada

```text
id
started_at
finished_at
profile_id
profile_name
list_id
list_name
list_date
status
events
```

Status de sessão observados na UI e patches:

```text
EM_EXECUÇÃO
FINALIZADO
EXPIRADA
CANCELADO
ENCERRADO
INTERROMPIDO
ERRO
```

### 5.7 Evento de sessão

```text
at
status
detail
```

## 6. Classificação do schema JSON

| Parte | Classificação | Certeza | Risco | Destino preliminar |
|---|---|---|---|---|
| identificadores de perfil/lista/sinal/sessão | REUTILIZAR | Alta | Baixo | entidades e contratos futuros |
| perfis, resolução e escala | ADAPTAR | Alta | Médio | environment/application/monitor profiles |
| coordenadas LARANJA/CINZA | ADAPTAR | Alta | Crítico | click targets geométricos, sem autorização de execução |
| listas e sinais | ADAPTAR | Alta | Médio | lists, list items e schedules |
| histórico de sessão/eventos | ADAPTAR | Alta | Médio | runtime sessions e transitions |
| JSON como fonte global definitiva | SUBSTITUIR | Alta | Alto | persistência futura do servidor, após arquitetura aprovada |
| `legacy_history` textual | ADAPTAR | Alta | Médio | migração ou retenção histórica controlada |

Nenhum SQL ou migration foi produzido.

## 7. Dois caminhos de clique real confirmados

### 7.1 Teste de calibração

`app/main.py::_test_both_coordinates`:

- solicita confirmação em diálogo;
- movimenta o cursor para `LARANJA` e `CINZA`;
- envia um clique esquerdo em cada ponto;
- marca o perfil como validado.

### 7.2 Execução agendada

`app/main.py::_execution_loop`, posteriormente substituído por `app/bootstrap_v231.py::execution_loop`:

- aguarda o horário do sinal;
- escolhe `LARANJA` ou `CINZA` pela direção;
- movimenta o cursor;
- envia clique esquerdo;
- registra `CLIQUE_ENVIADO` com X e Y.

Classificação dos dois caminhos: `DESCONTINUAR` no baseline V2.5 e manter bloqueados até autorização explícita de etapa futura.

```text
CALIBRATION_REAL_CLICK=BLOCKED
SCHEDULED_REAL_CLICK=BLOCKED
REAL_CLICK_EXECUTED_DURING_AUDIT=NO
```

## 8. Matriz de versão documental

| Fonte | Valor/alcance observado | Situação |
|---|---|---|
| `PROJECT_STATE.md` | `V2.4.3-R1` | autoridade de estado atual |
| `VERSION` | `2.4.3` | versão lida pelo runtime |
| `app/version_info.py` | lê `VERSION` | coerente |
| `app/bootstrap_v233.py` | exibe versão lida | coerente |
| `app/bootstrap_v233_runtime.py` | ajusta título com versão lida | coerente |
| `README.md` | declara `1.0.0` | desatualizado |
| `CHANGELOG.md` | termina em `2.3.3` | incompleto para 2.4.1–2.4.3 |

Conclusão:

```text
RUNTIME_VERSION_CONSISTENCY=PASS
README_VERSION_CONSISTENCY=FAIL
CHANGELOG_VERSION_COVERAGE=FAIL
```

Classificação de `README.md`: `SUBSTITUIR`.

Classificação de `CHANGELOG.md`: `ADAPTAR` por complemento histórico, sem reescrever eventos sem evidência.

## 9. Pendências remanescentes

```text
ALL_NESTED_FUNCTIONS_COUNT=PENDING
ALL_METHODS_COUNT=PENDING
IMPORT_GRAPH_DYNAMIC_VALIDATION=PENDING
CIRCULAR_IMPORT_RUNTIME_TEST=NOT_EXECUTED
JSON_REAL_SAMPLE_VALIDATION=NOT_EXECUTED
JSON_FIELD_OPTIONALITY_MATRIX=PENDING
STATUS_TRANSITION_MATRIX=PENDING
README_CORRECTION=PENDING
CHANGELOG_COMPLETION=PENDING
```

## 10. Gate do apêndice

```text
DIRECT_IMPORT_GRAPH=PASS_PRELIMINARY
CORE_SYMBOL_INDEX=PASS_PRELIMINARY
JSON_SCHEMA_4_INVENTORY=PASS_PRELIMINARY
REAL_CLICK_PATHS=PASS
VERSION_DIVERGENCE_MATRIX=PASS
APPENDIX_COMPLETE=PASS_PRELIMINARY
```
