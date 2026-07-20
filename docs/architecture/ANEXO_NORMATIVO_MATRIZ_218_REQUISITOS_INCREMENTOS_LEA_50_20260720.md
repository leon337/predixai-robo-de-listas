# ANEXO NORMATIVO — MATRIZ 218 REQUISITOS → INCREMENTOS

```text
DOCUMENT_TYPE=NORMATIVE_ANNEX
PARENT_AUTHORITY=DOCUMENTO_MESTRE
CAN_OVERRIDE_MASTER=NO
REQUIRED_FOR_MASTER_VALIDITY=YES
MISSION=LEA-50
STATUS=CANDIDATE_AWAITING_INDEPENDENT_RETEST
```

| REQUIREMENT_ID | PTM_SOURCE | DOMAIN | HANDOFF | ADR | MASTER_SECTION | IMPLEMENTATION_INCREMENT | TEST_FAMILY | LOCAL_TEST | LOCAL_EVIDENCE | ACCEPTANCE_GATE | VERSION |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PTM-V25-001 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0001, ADR-0002, ADR-0003 | DM-06, DM-07, DM-18 | FND-001 | T-CFG-*, T-DB-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-002 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0001, ADR-0002, ADR-0003 | DM-06, DM-07, DM-18 | FND-003 | T-CFG-*, T-DB-* | bash scripts/local_validate_fnd_003.sh | reports/local/FND-003_<COMMIT>.txt | FND-003_EXIT_PASS | V2.5.0-alpha.1 |
| PTM-V25-003 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0001, ADR-0002, ADR-0003 | DM-06, DM-07, DM-18 | DAT-001 | T-CFG-*, T-DB-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V25-004 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0001, ADR-0002, ADR-0003 | DM-06, DM-07, DM-18 | FND-001 | T-CFG-*, T-DB-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-005 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0001, ADR-0002, ADR-0003 | DM-06, DM-07, DM-18 | FND-001 | T-CFG-*, T-DB-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-006 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0001, ADR-0002, ADR-0003 | DM-06, DM-07, DM-18 | FND-001 | T-CFG-*, T-DB-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-007 | PTM_V2.5 | DOM-04 | H-01 | ADR-0001, ADR-0002 | DM-08 | LST-001 | T-LIST-*, T-E2E-* | bash scripts/local_validate_lst_001.sh | reports/local/LST-001_<COMMIT>.txt | LST-001_EXIT_PASS | V2.5.0-alpha.3 |
| PTM-V25-008 | PTM_V2.5 | DOM-05 | — | ADR-0004 | DM-09 | FND-003 | T-CFG-*, T-E2E-* | bash scripts/local_validate_fnd_003.sh | reports/local/FND-003_<COMMIT>.txt | FND-003_EXIT_PASS | V2.5.0-alpha.1 |
| PTM-V25-009 | PTM_V2.5 | DOM-05 | — | ADR-0004 | DM-09 | FND-003 | T-CFG-*, T-E2E-* | bash scripts/local_validate_fnd_003.sh | reports/local/FND-003_<COMMIT>.txt | FND-003_EXIT_PASS | V2.5.0-alpha.1 |
| PTM-V25-010 | PTM_V2.5 | DOM-06 | H-02 | ADR-0005 | DM-10, DM-15 | PRF-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_prf_001.sh | reports/local/PRF-001_<COMMIT>.txt | PRF-001_EXIT_PASS | V2.5.0-beta.1 |
| PTM-V25-011A | PTM_V2.5 | DOM-06 | H-02 | ADR-0005 | DM-10, DM-15 | PRF-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_prf_001.sh | reports/local/PRF-001_<COMMIT>.txt | PRF-001_EXIT_PASS | V2.5.0-beta.1 |
| PTM-V25-011B | PTM_V2.5 | DOM-06 | H-02 | ADR-0005 | DM-10, DM-15 | PRF-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_prf_001.sh | reports/local/PRF-001_<COMMIT>.txt | PRF-001_EXIT_PASS | V2.5.0-beta.1 |
| PTM-V25-011C | PTM_V2.5 | DOM-06 | H-02 | ADR-0005 | DM-10, DM-15 | PRF-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_prf_001.sh | reports/local/PRF-001_<COMMIT>.txt | PRF-001_EXIT_PASS | V2.5.0-beta.1 |
| PTM-V25-011D | PTM_V2.5 | DOM-06 | H-02 | ADR-0005 | DM-10, DM-15 | PRF-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_prf_001.sh | reports/local/PRF-001_<COMMIT>.txt | PRF-001_EXIT_PASS | V2.5.0-beta.1 |
| PTM-V25-012 | PTM_V2.5 | DOM-02, DOM-14 | — | ADR-0001, ADR-0003, ADR-0009 | DM-06, DM-15, DM-18 | FND-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-013 | PTM_V2.5 | DOM-02, DOM-14 | — | ADR-0001, ADR-0003, ADR-0009 | DM-06, DM-15, DM-18 | FND-001 | T-CFG-*, T-ADP-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-014A | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V25-014B | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V25-014C | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V25-014D | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V25-014E | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V25-015A | PTM_V2.5 | DOM-16 | H-11 | ADR-0012 | DM-17 | FND-002 | T-SEC-* | bash scripts/validate_fnd_002_local.sh | reports/local/FND-002_<COMMIT>.txt | FND-002_EXIT_PASS | V2.4.3-R1+fnd.002 |
| PTM-V25-015B | PTM_V2.5 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V25-015C | PTM_V2.5 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V25-015D | PTM_V2.5 | DOM-16 | H-11 | ADR-0012 | DM-17 | FND-001 | T-SEC-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V25-015E | PTM_V2.5 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V25-016 | PTM_V2.5 | DOM-02, DOM-03 | — | ADR-0002 | DM-06, DM-07 | FND-003 | T-CFG-*, T-DB-* | bash scripts/local_validate_fnd_003.sh | reports/local/FND-003_<COMMIT>.txt | FND-003_EXIT_PASS | V2.5.0-alpha.1 |
| PTM-V25-017 | PTM_V2.5 | DOM-02, DOM-05, DOM-16 | — | ADR-0004, ADR-0012 | DM-06, DM-09, DM-17 | FND-003 | T-CFG-*, T-SEC-* | bash scripts/local_validate_fnd_003.sh | reports/local/FND-003_<COMMIT>.txt | FND-003_EXIT_PASS | V2.5.0-alpha.1 |
| PTM-V25-018 | PTM_V2.5 | DOM-01, DOM-02, DOM-05 | — | ADR-0001, ADR-0010 | DM-05, DM-06, DM-09 | FND-001 | T-GOV-*, T-CFG-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-CFG-001 | PTM_V2.5 | DOM-02 | — | ADR-0012 | DM-06, DM-17 | FND-001 | T-CFG-*, T-SEC-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-CFG-002 | PTM_V2.5 | DOM-02 | — | ADR-0012 | DM-06, DM-17 | FND-001 | T-CFG-*, T-SEC-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-CFG-003 | PTM_V2.5 | DOM-02 | — | ADR-0012 | DM-06, DM-17 | FND-001 | T-CFG-*, T-SEC-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-CFG-004 | PTM_V2.5 | DOM-02 | — | ADR-0012 | DM-06, DM-17 | FND-001 | T-CFG-*, T-SEC-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-DB-001 | PTM_V2.5 | DOM-03 | H-11 | ADR-0002, ADR-0003, ADR-0013 | DM-07, DM-18, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-DB-002 | PTM_V2.5 | DOM-03 | H-11 | ADR-0002, ADR-0003, ADR-0013 | DM-07, DM-18, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-DB-003 | PTM_V2.5 | DOM-03 | H-11 | ADR-0002, ADR-0003, ADR-0013 | DM-07, DM-18, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-DB-004 | PTM_V2.5 | DOM-03 | H-11 | ADR-0002, ADR-0003, ADR-0013 | DM-07, DM-18, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-DB-005 | PTM_V2.5 | DOM-03 | H-11 | ADR-0002, ADR-0003, ADR-0013 | DM-07, DM-18, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-DOC-001 | PTM_V2.5 | DOM-01 | — | ADR-0018 | DM-05, DM-23 | FND-001 | T-GOV-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-LEG-001 | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-LEG-002 | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-LEG-003 | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-LEG-004 | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-LEG-005 | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-LEG-006 | PTM_V2.5 | DOM-03 | — | ADR-0002, ADR-0013 | DM-07, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| V25-LIST-001 | PTM_V2.5 | DOM-04 | H-01 | ADR-0001, ADR-0002 | DM-08 | LST-001 | T-LIST-*, T-E2E-* | bash scripts/local_validate_lst_001.sh | reports/local/LST-001_<COMMIT>.txt | LST-001_EXIT_PASS | V2.5.0-alpha.3 |
| V25-LIST-002 | PTM_V2.5 | DOM-04 | H-01 | ADR-0001, ADR-0002 | DM-08 | LST-001 | T-LIST-*, T-E2E-* | bash scripts/local_validate_lst_001.sh | reports/local/LST-001_<COMMIT>.txt | LST-001_EXIT_PASS | V2.5.0-alpha.3 |
| V25-LIST-003 | PTM_V2.5 | DOM-04 | H-01 | ADR-0001, ADR-0002 | DM-08 | LST-001 | T-LIST-*, T-E2E-* | bash scripts/local_validate_lst_001.sh | reports/local/LST-001_<COMMIT>.txt | LST-001_EXIT_PASS | V2.5.0-alpha.3 |
| V25-LIST-004 | PTM_V2.5 | DOM-04 | H-01 | ADR-0001, ADR-0002 | DM-08 | LST-001 | T-LIST-*, T-E2E-* | bash scripts/local_validate_lst_001.sh | reports/local/LST-001_<COMMIT>.txt | LST-001_EXIT_PASS | V2.5.0-alpha.3 |
| V25-QA-001 | PTM_V2.5 | DOM-16 | — | ADR-0018 | DM-20 | FND-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-QA-002 | PTM_V2.5 | DOM-04, DOM-14, DOM-16 | — | ADR-0009, ADR-0018 | DM-08, DM-15, DM-20 | LST-001 | T-E2E-* | bash scripts/local_validate_lst_001.sh | reports/local/LST-001_<COMMIT>.txt | LST-001_EXIT_PASS | V2.5.0-alpha.3 |
| V25-SEC-001 | PTM_V2.5 | DOM-16 | — | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | FND-001 | T-SEC-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-SRV-001 | PTM_V2.5 | DOM-01, DOM-02, DOM-03, DOM-05 | — | ADR-0001, ADR-0003, ADR-0004 | DM-05..DM-09, DM-18 | FND-001 | T-GOV-*, T-E2E-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-SRV-002 | PTM_V2.5 | DOM-01, DOM-02, DOM-03, DOM-05 | — | ADR-0001, ADR-0003, ADR-0004 | DM-05..DM-09, DM-18 | FND-001 | T-GOV-*, T-E2E-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-SRV-003 | PTM_V2.5 | DOM-01, DOM-02, DOM-03, DOM-05 | — | ADR-0001, ADR-0003, ADR-0004 | DM-05..DM-09, DM-18 | FND-001 | T-GOV-*, T-E2E-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| V25-SRV-004 | PTM_V2.5 | DOM-01, DOM-02, DOM-03, DOM-05 | — | ADR-0001, ADR-0003, ADR-0004 | DM-05..DM-09, DM-18 | FND-001 | T-GOV-*, T-E2E-* | bash scripts/local_validate_fnd_001.sh | reports/local/FND-001_<COMMIT>.txt | FND-001_EXIT_PASS | V2.4.3-R1+fnd.001 |
| PTM-V26-001 | PTM_V2.6 | DOM-11, DOM-13 | H-08 | ADR-0008, ADR-0009 | DM-13, DM-14 | ANA-001 | T-ANA-*, T-CMD-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-002 | PTM_V2.6 | DOM-07 | H-02, H-03 | ADR-0005, ADR-0014 | DM-10, DM-11 | OBS-001 | T-OBS-* | bash scripts/local_validate_obs_001.sh | reports/local/OBS-001_<COMMIT>.txt | OBS-001_EXIT_PASS | V2.6.0-alpha.1 |
| PTM-V26-003 | PTM_V2.6 | DOM-07 | H-02, H-03 | ADR-0005, ADR-0014 | DM-10, DM-11 | OBS-001 | T-OBS-* | bash scripts/local_validate_obs_001.sh | reports/local/OBS-001_<COMMIT>.txt | OBS-001_EXIT_PASS | V2.6.0-alpha.1 |
| PTM-V26-004 | PTM_V2.6 | DOM-08 | H-04 | ADR-0014 | DM-11 | CAP-001 | T-CAP-* | bash scripts/local_validate_cap_001.sh | reports/local/CAP-001_<COMMIT>.txt | CAP-001_EXIT_PASS | V2.6.0-alpha.2 |
| PTM-V26-005 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| PTM-V26-006 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| PTM-V26-007 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| PTM-V26-008 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| PTM-V26-009 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-010 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-011 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-012 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-013 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-014 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-015 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-016 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-017 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-018 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| PTM-V26-019 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| PTM-V26-020 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| PTM-V26-021 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| PTM-V26-022 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| PTM-V26-023 | PTM_V2.6 | DOM-03 | — | ADR-0002, ADR-0003 | DM-07, DM-18 | DAT-001 | T-DB-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V26-024 | PTM_V2.6 | DOM-16 | H-11 | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V26-025 | PTM_V2.6 | DOM-16 | H-11 | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V26-026 | PTM_V2.6 | DOM-16 | H-11 | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V26-027 | PTM_V2.6 | DOM-03 | — | ADR-0002, ADR-0003 | DM-07, DM-18 | DAT-001 | T-DB-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V26-028 | PTM_V2.6 | DOM-16 | H-11 | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-ANA-001 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-002 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-003 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-004 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-005 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-006 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-007 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-008 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-009 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-010 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-ANA-011 | PTM_V2.6 | DOM-11 | H-07 | ADR-0006, ADR-0017 | DM-13 | ANA-001 | T-ANA-* | bash scripts/local_validate_ana_001.sh | reports/local/ANA-001_<COMMIT>.txt | ANA-001_EXIT_PASS | V2.6.0-beta.2 |
| V26-API-001 | PTM_V2.6 | DOM-03, DOM-16 | — | ADR-0003, ADR-0012 | DM-07, DM-17, DM-18 | FND-002 | T-DB-*, T-SEC-* | bash scripts/validate_fnd_002_local.sh | reports/local/FND-002_<COMMIT>.txt | FND-002_EXIT_PASS | V2.4.3-R1+fnd.002 |
| V26-API-002 | PTM_V2.6 | DOM-03, DOM-16 | — | ADR-0003, ADR-0012 | DM-07, DM-17, DM-18 | FND-002 | T-DB-*, T-SEC-* | bash scripts/validate_fnd_002_local.sh | reports/local/FND-002_<COMMIT>.txt | FND-002_EXIT_PASS | V2.4.3-R1+fnd.002 |
| V26-CAP-001 | PTM_V2.6 | DOM-08 | H-04 | ADR-0014 | DM-11 | CAP-001 | T-CAP-* | bash scripts/local_validate_cap_001.sh | reports/local/CAP-001_<COMMIT>.txt | CAP-001_EXIT_PASS | V2.6.0-alpha.2 |
| V26-CAP-002 | PTM_V2.6 | DOM-08 | H-04 | ADR-0014 | DM-11 | CAP-001 | T-CAP-* | bash scripts/local_validate_cap_001.sh | reports/local/CAP-001_<COMMIT>.txt | CAP-001_EXIT_PASS | V2.6.0-alpha.2 |
| V26-CAP-003 | PTM_V2.6 | DOM-08 | H-04 | ADR-0014 | DM-11 | CAP-001 | T-CAP-* | bash scripts/local_validate_cap_001.sh | reports/local/CAP-001_<COMMIT>.txt | CAP-001_EXIT_PASS | V2.6.0-alpha.2 |
| V26-CAP-004 | PTM_V2.6 | DOM-08 | H-04 | ADR-0014 | DM-11 | CAP-001 | T-CAP-* | bash scripts/local_validate_cap_001.sh | reports/local/CAP-001_<COMMIT>.txt | CAP-001_EXIT_PASS | V2.6.0-alpha.2 |
| V26-MAP-001 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| V26-MAP-002 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| V26-MAP-003 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| V26-MAP-004 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| V26-MAP-005 | PTM_V2.6 | DOM-10 | H-06 | ADR-0017 | DM-12 | MAP-001 | T-MAP-* | bash scripts/local_validate_map_001.sh | reports/local/MAP-001_<COMMIT>.txt | MAP-001_EXIT_PASS | V2.6.0-beta.1 |
| V26-OBS-001 | PTM_V2.6 | DOM-07 | H-02, H-03 | ADR-0005, ADR-0014 | DM-10, DM-11 | OBS-001 | T-OBS-* | bash scripts/local_validate_obs_001.sh | reports/local/OBS-001_<COMMIT>.txt | OBS-001_EXIT_PASS | V2.6.0-alpha.1 |
| V26-OBS-002 | PTM_V2.6 | DOM-07 | H-02, H-03 | ADR-0005, ADR-0014 | DM-10, DM-11 | OBS-001 | T-OBS-* | bash scripts/local_validate_obs_001.sh | reports/local/OBS-001_<COMMIT>.txt | OBS-001_EXIT_PASS | V2.6.0-alpha.1 |
| V26-OBS-003 | PTM_V2.6 | DOM-07 | H-02, H-03 | ADR-0005, ADR-0014 | DM-10, DM-11 | OBS-001 | T-OBS-* | bash scripts/local_validate_obs_001.sh | reports/local/OBS-001_<COMMIT>.txt | OBS-001_EXIT_PASS | V2.6.0-alpha.1 |
| V26-OBS-004 | PTM_V2.6 | DOM-07 | H-02, H-03 | ADR-0005, ADR-0014 | DM-10, DM-11 | OBS-001 | T-OBS-* | bash scripts/local_validate_obs_001.sh | reports/local/OBS-001_<COMMIT>.txt | OBS-001_EXIT_PASS | V2.6.0-alpha.1 |
| V26-RPL-001 | PTM_V2.6 | DOM-16 | — | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-E2E-*, T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-RPL-002 | PTM_V2.6 | DOM-16 | — | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-E2E-*, T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-RPL-003 | PTM_V2.6 | DOM-16 | — | ADR-0012, ADR-0014, ADR-0018 | DM-17, DM-20 | SEC-001 | T-E2E-*, T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-SEC-001 | PTM_V2.6 | DOM-16 | H-11 | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-SEC-002 | PTM_V2.6 | DOM-16 | H-11 | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-SEC-003 | PTM_V2.6 | DOM-16 | H-11 | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V26-SIG-001 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-002 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-003 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-004 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-005 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-006 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-007 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-SIG-008 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13, DM-14 | SIG-001 | T-SIG-*, T-CMD-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-STR-001 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-STR-002 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-STR-003 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-STR-004 | PTM_V2.6 | DOM-12 | H-08 | ADR-0007 | DM-13 | SIG-001 | T-SIG-* | bash scripts/local_validate_sig_001.sh | reports/local/SIG-001_<COMMIT>.txt | SIG-001_EXIT_PASS | V2.6.0-rc.1 |
| V26-VAL-001 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| V26-VAL-002 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| V26-VAL-003 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| V26-VAL-004 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| V26-VAL-005 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| V26-VAL-006 | PTM_V2.6 | DOM-09 | H-05 | ADR-0014, ADR-0017 | DM-12 | VAL-001 | T-VAL-* | bash scripts/local_validate_val_001.sh | reports/local/VAL-001_<COMMIT>.txt | VAL-001_EXIT_PASS | V2.6.0-alpha.3 |
| PTM-V27-001 | PTM_V2.7 | DOM-13, DOM-15 | H-08..H-10 | ADR-0008, ADR-0011 | DM-14, DM-16 | CMD-001 | T-CMD-*, T-EXE-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| PTM-V27-002 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008, ADR-0009 | DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| PTM-V27-003 | PTM_V2.7 | DOM-14 | H-09, H-10 | ADR-0009 | DM-15 | CUI-001 | T-ADP-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| PTM-V27-004 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| PTM-V27-005 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| PTM-V27-006 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| PTM-V27-007 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| PTM-V27-008 | PTM_V2.7 | DOM-14 | H-09, H-10 | ADR-0005, ADR-0009 | DM-10, DM-15 | ADP-001 | T-ADP-* | bash scripts/local_validate_adp_001.sh | reports/local/ADP-001_<COMMIT>.txt | ADP-001_EXIT_PASS | V2.7.0-alpha.2 |
| PTM-V27-009 | PTM_V2.7 | DOM-14 | H-09, H-10 | ADR-0005, ADR-0009 | DM-10, DM-15 | CUI-001 | T-ADP-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| PTM-V27-010 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-011 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-012 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-013 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-014 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-015 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-016 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-017 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-018 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-019 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V27-020 | PTM_V2.7 | DOM-05, DOM-13 | H-09 | ADR-0004, ADR-0008 | DM-09, DM-14 | FND-003 | T-CMD-* | bash scripts/local_validate_fnd_003.sh | reports/local/FND-003_<COMMIT>.txt | FND-003_EXIT_PASS | V2.5.0-alpha.1 |
| PTM-V27-021 | PTM_V2.7 | DOM-14, DOM-15 | H-10 | ADR-0009 | DM-15, DM-16 | CUI-001 | T-ADP-*, T-EXE-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| PTM-V27-022 | PTM_V2.7 | DOM-15 | H-10, H-11 | ADR-0011 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-023 | PTM_V2.7 | DOM-15 | H-10, H-11 | ADR-0011 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-024 | PTM_V2.7 | DOM-15 | H-10, H-11 | ADR-0011 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-025 | PTM_V2.7 | DOM-15 | H-10, H-11 | ADR-0011 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-026 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V27-027 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V27-028 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V27-029 | PTM_V2.7 | DOM-03, DOM-15 | — | ADR-0002, ADR-0013 | DM-07, DM-16, DM-19 | DAT-001 | T-DB-*, T-REC-* | bash scripts/local_validate_dat_001.sh | reports/local/DAT-001_<COMMIT>.txt | DAT-001_EXIT_PASS | V2.5.0-alpha.2 |
| PTM-V27-030 | PTM_V2.7 | DOM-15 | H-11 | ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| PTM-V27-031 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0012, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| PTM-V27-032 | PTM_V2.7 | DOM-01 | H-12 | ADR-0009, ADR-0010 | DM-05, DM-14, DM-17, DM-22 | LIV-GATE-001 | T-GOV-*, T-SEC-* | bash scripts/local_validate_liv_gate_001.sh | reports/local/LIV-GATE-001_<COMMIT>.txt | LIV-GATE-001_EXIT_PASS | TBD_BY_FUTURE_CHANGE_CONTROL |
| V27-AUT-001 | PTM_V2.7 | DOM-13 | H-09 | ADR-0004, ADR-0008, ADR-0009 | DM-09, DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-AUT-002 | PTM_V2.7 | DOM-13 | H-09 | ADR-0004, ADR-0008, ADR-0009 | DM-09, DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-AUT-003 | PTM_V2.7 | DOM-13 | H-09 | ADR-0004, ADR-0008, ADR-0009 | DM-09, DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-AUT-004 | PTM_V2.7 | DOM-13 | H-09 | ADR-0004, ADR-0008, ADR-0009 | DM-09, DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-AUT-005 | PTM_V2.7 | DOM-13 | H-09 | ADR-0004, ADR-0008, ADR-0009 | DM-09, DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-AUT-006 | PTM_V2.7 | DOM-13 | H-09 | ADR-0004, ADR-0008, ADR-0009 | DM-09, DM-14, DM-15 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-CMD-001 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-CMD-002 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-CMD-003 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-CMD-004 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-CMD-005 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-CMD-006 | PTM_V2.7 | DOM-13 | H-08, H-09 | ADR-0008 | DM-14 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-EXE-001 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-EXE-002 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-EXE-003 | PTM_V2.7 | DOM-14 | H-10 | ADR-0009 | DM-15 | CUI-001 | T-ADP-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| V27-EXE-004 | PTM_V2.7 | DOM-14 | H-10 | ADR-0009 | DM-15 | CUI-001 | T-ADP-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| V27-EXE-005 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-EXE-006 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-EXE-007 | PTM_V2.7 | DOM-15 | H-10 | ADR-0011, ADR-0015, ADR-0016 | DM-16 | EXE-001 | T-EXE-*, T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-EXE-008 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-OBS-001 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | FND-002 | T-SEC-* | bash scripts/validate_fnd_002_local.sh | reports/local/FND-002_<COMMIT>.txt | FND-002_EXIT_PASS | V2.4.3-R1+fnd.002 |
| V27-OBS-002 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-OBS-003 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-OBS-004 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | FND-002 | T-SEC-* | bash scripts/validate_fnd_002_local.sh | reports/local/FND-002_<COMMIT>.txt | FND-002_EXIT_PASS | V2.4.3-R1+fnd.002 |
| V27-OBS-005 | PTM_V2.7 | DOM-16 | H-11 | ADR-0012 | DM-17 | SEC-001 | T-SEC-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-PRE-001 | PTM_V2.7 | DOM-13 | H-09 | ADR-0008, ADR-0016 | DM-14, DM-18 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-PRE-002 | PTM_V2.7 | DOM-13 | H-09 | ADR-0008, ADR-0016 | DM-14, DM-18 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-PRE-003 | PTM_V2.7 | DOM-13 | H-09 | ADR-0008, ADR-0016 | DM-14, DM-18 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-PRE-004 | PTM_V2.7 | DOM-13 | H-09 | ADR-0008, ADR-0016 | DM-14, DM-18 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-PRE-005 | PTM_V2.7 | DOM-13 | H-09 | ADR-0008, ADR-0016 | DM-14, DM-18 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-PRE-006 | PTM_V2.7 | DOM-13 | H-09 | ADR-0008, ADR-0016 | DM-14, DM-18 | CMD-001 | T-CMD-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-QA-001 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-QA-002 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-QA-003 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-QA-004 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-QA-005 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-QA-006 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-QA-007 | PTM_V2.7 | DOM-16 | H-12 | ADR-0010, ADR-0018 | DM-17, DM-20 | SEC-001 | T-SEC-*, T-E2E-* | bash scripts/local_validate_sec_001.sh | reports/local/SEC-001_<COMMIT>.txt | SEC-001_EXIT_PASS | V2.7.0-rc.1 |
| V27-REC-001 | PTM_V2.7 | DOM-15 | H-11 | ADR-0011, ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-REC-002 | PTM_V2.7 | DOM-15 | H-11 | ADR-0011, ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-REC-003 | PTM_V2.7 | DOM-15 | H-11 | ADR-0011, ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-REC-004 | PTM_V2.7 | DOM-15 | H-11 | ADR-0011, ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-REC-005 | PTM_V2.7 | DOM-15 | H-11 | ADR-0011, ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-REC-006 | PTM_V2.7 | DOM-15 | H-11 | ADR-0011, ADR-0016 | DM-16 | EXE-001 | T-REC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-SAF-001 | PTM_V2.7 | DOM-13 | H-09, H-12 | ADR-0008, ADR-0009, ADR-0010 | DM-14, DM-17 | CMD-001 | T-CMD-*, T-SEC-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |
| V27-SAF-002 | PTM_V2.7 | DOM-15 | H-10, H-12 | ADR-0015 | DM-16, DM-17 | EXE-001 | T-EXE-*, T-SEC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-SAF-003 | PTM_V2.7 | DOM-15 | H-10, H-12 | ADR-0015 | DM-16, DM-17 | EXE-001 | T-EXE-*, T-SEC-* | bash scripts/local_validate_exe_001.sh | reports/local/EXE-001_<COMMIT>.txt | EXE-001_EXIT_PASS | V2.7.0-beta.1 |
| V27-SAF-004 | PTM_V2.7 | DOM-16 | H-10, H-12 | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | CUI-001 | T-SEC-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| V27-SAF-005 | PTM_V2.7 | DOM-16 | H-10, H-12 | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | CUI-001 | T-SEC-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| V27-SAF-006 | PTM_V2.7 | DOM-14 | H-10 | ADR-0005, ADR-0009 | DM-10, DM-15 | CUI-001 | T-ADP-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| V27-SAF-007 | PTM_V2.7 | DOM-16 | H-10, H-12 | ADR-0009, ADR-0010, ADR-0012 | DM-15, DM-17 | CUI-001 | T-SEC-* | bash scripts/local_validate_cui_001.sh | reports/local/CUI-001_<COMMIT>.txt | CUI-001_EXIT_PASS | V2.7.0-cui.1 |
| V27-SAF-008 | PTM_V2.7 | DOM-13 | H-09, H-12 | ADR-0008, ADR-0009, ADR-0010 | DM-14, DM-17 | CMD-001 | T-CMD-*, T-SEC-* | bash scripts/local_validate_cmd_001.sh | reports/local/CMD-001_<COMMIT>.txt | CMD-001_EXIT_PASS | V2.7.0-alpha.1 |

```text
TOTAL_REQUIREMENTS=218
REQUIREMENTS_MAPPED=218
ORPHAN_REQUIREMENTS=0
DUPLICATE_REQUIREMENT_IDS=0
REQUIREMENTS_WITHOUT_INCREMENT=0
INCREMENTS_WITHOUT_NORMATIVE_BASIS=0
REQUIREMENTS_WITHOUT_TEST_FAMILY=0
REQUIREMENTS_WITHOUT_ACCEPTANCE_GATE=0
```
