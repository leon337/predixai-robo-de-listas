# AVISO DE SUPERSESSÃO — PRIMEIRO RETESTE PTM V2.7

## LEA-17 / PR #37

```text
DOCUMENT_STATUS=NORMATIVE_REVIEW_NOTICE
SUPERSEDED_DOCUMENT=docs/history/reviews/REVISAO_CRITICA_RETESTE_PTM_V2.7_LEA-17_20260717.md
SUPERSEDED_REVIEWED_HEAD=510e6a1e19ac6b3dc4778797b3f003fcd9d20afb
SUPERSEDED_RESULT=PASS_PRELIMINARY
SUPERSEDED_RESULT_IS_FINAL=NO
DOCUMENTAL_READY_FOR_MERGE=NO
```

O primeiro relatório de reteste foi produzido antes da chegada completa da revisão automatizada solicitada para o mesmo HEAD. Quatro achados posteriores invalidaram seu uso como gate final:

1. a restrição contra resultado monetário real deve aplicar-se a toda classe de alvo;
2. `CONTROLLED_UI` precisa de contrato normativo próprio de estado, comando, autorização, adaptador e recibo;
3. restart no mesmo boot deve impedir a reutilização de comandos anteriores sem depender do relógio de parede;
4. o vínculo operacional da revisão deve ser renovado após as correções.

```text
PTM_V2_7_CRITICAL_RETEST_01=SUPERSEDED
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=2
REMEDIATION_REQUIRED=YES
```

O gate final somente poderá ser fornecido por um segundo relatório independente emitido após:

- correção da política de ambiente controlado;
- publicação do adendo `CONTROLLED_UI` e recovery temporal;
- sincronização dos documentos vivos;
- novo reteste do HEAD resultante.
