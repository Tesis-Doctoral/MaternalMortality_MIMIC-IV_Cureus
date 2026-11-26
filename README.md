# Predictor or early identifier? Severe maternal morbidity in MIMIC-IV

> **Framework.** This repository applies the thesis's staged framework for clinical prediction models. The framework (stages, gates, criteria and literature) and the catalogue of models with their status are in [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction).

Code, SQL and aggregate outputs for the article **"Predictor or Early Identifier? A Staged Framework for Clinical Prediction Models Applied to Severe Maternal Morbidity in MIMIC-IV"** (Cureus, 2026).

Authors: Emmanuel Gutiérrez Jiménez and José Duván Márquez Díaz — Systems Engineering Department, Universidad del Norte, Barranquilla, Colombia.

[Versión en español](README_es.md)

> **No patient-level data are included in this repository.** MIMIC-IV requires credentialed access (see [Data access](#data-access)). The SQL files contain only schema definitions, cohort logic and code lists; the notebooks' outputs in `data/` are aggregate counts and metrics, with cells below 10 suppressed. No `subject_id`, `hadm_id` or `stay_id` values are published.

> **Status (2026-11-26).** Models M1 and M2 of the framework catalogue are complete and the Spanish notebooks have been run. The notebooks follow the order of the framework: notebook 01 starts with governance and configuration (S1) and with the ideal outcome, maternal death (M1). Notebook 10 evaluates the gate-G4 criteria on the models fitted once on their whole population and applies gate G3 to every set in which a model is fitted (decision of 2026-11-22, [`docs/decision_G4_fitted_models_2026-11-22.md`](docs/decision_G4_fitted_models_2026-11-22.md)); results recorded in the decision log. Under framework 1.3 (C1 is decided only by the drop in AUROC; C4 requires a temporal AUROC of 0.70 or more and a calibration slope between 0.90 and 1.10; the class formerly called "neither" is now "insufficient signal"), the classes of M1 and M2 do not change.

## Scope

| Id in the catalogue | Model | Outcome | Prediction point | Result |
|---|---|---|---|---|
| M1 | Maternal death | Death in the delivery hospitalization | Admission + 24 h | Fails G3 (3 events): feasibility only; return R1 to SMM |
| M2 | Severe maternal morbidity (SMM) | At least one of the 20 CDC indicators | Admission + 24 h | **Early identifier** (fails C1, C3 and C4; meets C2) |
| M2 · R4 | SMM, extended laboratory set | as M2 | as M2 | Early identifier: the gain came from which tests were ordered |
| M2 · R2 | Escalation of care after T | ICU admission, mechanical ventilation, procedure-based SMM indicator or death after T | as M2 | Meets C1 and C2; C4 not assessable (46 development events); fails G3 (101 events, 32 parameters) |
| M2 · R2 reduced | as R2, 13 parameters | as R2 | as M2 | Passes G3; **exploratory signal of prediction**: just below C2 (0.749), C4 not assessable |

Outcome card: [`docs/outcome_card_smm.md`](docs/outcome_card_smm.md). Decision log: [`docs/`](docs/) (one file per decision, dated).

## Data and population

MIMIC-IV v3.1 (Beth Israel Deaconess Medical Center, 2008–2022; dates shifted per patient). Delivery hospitalizations still in hospital 24 hours after admission: **19,383 admissions of 13,710 patients, 445 with SMM (2.30%)**. Only 25.6% of the SMM events could be dated after the prediction point (T = admission + 24 h).

| | |
|---|---|
| Predictors | Age, five registration variables, hemoglobin and creatinine up to T, creatinine missingness indicator (32 parameters) |
| Learners | L2 logistic regression (reference), random forest, extra trees, XGBoost (primary) and a stacked ensemble |
| Validation | Nested cross-validation grouped by patient (5 outer × 3 inner folds, 3 repeats); recalibration inside training; patient bootstrap |
| Temporal validation | Development on admissions certainly before 2017, single test from 2017 onward |

## Run order

**SQL** (PostgreSQL 13; the header of each script lists its prerequisites):

| Order | Folder | Creates | Framework stage |
|---|---|---|---|
| 1 | `sql/01_load_mimic_iv_schema/` | Local MIMIC-IV schema (see its README) | S1 |
| 2 | `sql/02_cohort_mortality/` (`maternal_cohort_expanded.sql`, then the rest) | Obstetric universe and base objects | S2 |
| 3 | `sql/03_cohort_smm/` (`smm_cohort.sql`, `smm_dataset.sql`) | SMM base objects | S2, S3 |
| 4 | `sql/04_labels/` (`01` to `06`, including `03b`) | CDC code lists, delivery flag, labels, death horizons | S2, S3, S4 |
| 5 | `sql/05_predictors/` (`01`, `02`) | Predictors in the 24-hour window and final dictionary | S6, S7 |
| 6 | `sql/06_audit_counts/` (optional) | Cohort-flow and cross-tabulation counts (temporary tables only) | S4, G1 |
| 7 | `sql/07_timing_audit/` (`01` to `04`) | Timing of the SMM evidence, phenotype audit, escalation label | S3, S4, R2 |
| 8 | `sql/08_tables/` (`01`, `02`; optional) | Table 1 of the article and availability of each predictor (Supplement 2); read-only | S7, S11 |

**Notebooks** (run top to bottom; each section names the stage, gate or criterion it serves):

| Order | Notebook | Creates (`data/`) | Framework stage |
|---|---|---|---|
| 1 | `01_smm_timing_vs_prediction_time.ipynb` | `outputs_smm_timing.txt` | S1, S2, S3, S4, G1 (includes M1: outcome ladder and maternal death counts) |
| 2 | `02_patient_overlap.ipynb` | Console counts only | S5, G2 |
| 3 | `03_grouped_validation_smm.ipynb` | `outputs_main.txt`, `outputs_modelA.txt` (maternal death), sensitivities `first_admission`, `any_obstetric`, `icd10_only`, `label_ge2`, `no_icu_24h`, `labs_extended`, `icu_vars` | S6, S7, G3, R1, S8, S9 |
| 4 | `04_resampling_comparison_smm.ipynb` | `outputs_resampling.txt` | S8 |
| 5 | `05_creatinine_indicator_sensitivity_smm.ipynb` | `outputs_no_indicator.txt` | S9 (S7) |
| 6 | `06_smm_renal_only_sensitivity.ipynb` | `outputs_excl_renal_only.txt` | S9 (S3) |
| 7 | `07_landmark_incident_smm.ipynb` | `outputs_landmark*.txt`, `outputs_incident_*.txt`, `outputs_aki_lab_incident*.txt`, `outputs_c3_labs_summary.txt`, `outputs_excl_nonacute.txt`, `outputs_richer_predictors_summary.txt`, `outputs_escalation*.txt`, `outputs_g3_escalation.txt`, `outputs_main_norace.txt`, `outputs_race_subgroups.txt`, `outputs_main_rerun12.txt` and `outputs_landmark_rerun12.txt` (section 12: same models with bootstrap B = 300) | S9, G4 (C1–C3), R4, R2, G3, sample-size reduction, S10 |
| 8 | `08_era_temporal_validation_smm.ipynb` | `outputs_era_temporal.txt` | S9 (C4, exploratory) |
| 9 | `09_temporal_validation_smm.ipynb` | `outputs_cut2017*.txt`, `outputs_cut2015.txt`, `outputs_temporal_summary.txt`, `outputs_temporal_predictors.txt` | S9, G4 (C4) |
| 10 | `10_g4_criteria_fitted_models.ipynb` | `outputs_g4_fitted_models.txt` (C1 and C2 with 95% intervals, escalation components), `outputs_g3_fitted_subsets.txt` | G4 (C1, C2) on the fitted models, G3 for every fitted set, S10, S11 |
| 11 | `11_roc_confusion_main_smm.ipynb` (complement, added after the article) | `outputs_11_roc_confusion_main.txt` and `figures/11_*.png`: ROC curve of each learner (one subplot each) and classification report + confusion matrix of XGBoost; reruns only the main analysis of notebook 03 and checks it against the article | S8 (figures only) |
| — | `scripts/g3_planning_assumed_r2.py` (no database needed) | `outputs_g3_planning.txt` | G3, planning step with an assumed R² |

Every notebook has an English and a Spanish version (`_es`) with the same code; only `LANG` in the first cell differs. Each section starts with the code of the stage, gate or criterion and a result → action table, and its output shows the decision taken; each notebook ends with a "Notebook summary". The Spanish notebooks show their tables and messages in Spanish (`libraries/i18n.py`, `libraries/i18n_es.py`) and also write a Spanish copy of each report (`data/outputs_*_es.txt`); the English reports `data/outputs_*.txt` cited by the article are written exactly as before. Every SQL script has a Spanish version with the suffix `_es` (same statements, translated comments).

## Framework map

> **Nomenclature.** Stages S1 to S11 and gates G1 to G4 (definition, leakage, sample-size and classification). The Spanish files use E1 to E11 and P1 to P4 for the same stages and gates.

| Stage, gate or return | Scripts and notebooks |
|---|---|
| S1 Governance and configuration | `sql/01_load_mimic_iv_schema/`; section S1 of notebook 01 (source, data use agreement, seed, software and publication rule); section 1 of every notebook |
| S2 Universe and population | `sql/02_cohort_mortality/maternal_cohort_expanded.sql`; `sql/04_labels/02_delivery_flag.sql`, `04_cohort_obstetric_flags.sql` |
| S3 Outcome definition | `sql/04_labels/01_smm_codes_official.sql`, `03_labels_same_admission.sql`; `sql/07_timing_audit/01_timing_flags_v3.sql`, `02_phenotype_audit_v3.sql`; notebook 01 |
| S4 Count audit · G1 | `sql/06_audit_counts/`; `sql/04_labels/03b_reconcile_old_labels.sql`, `06_smm_death_overlap.sql`; notebook 01; `EXPECTED` check in every notebook |
| S5 Unit of analysis and overlap | notebook 02 |
| S6 Prediction point and window | `sql/05_predictors/01_predictors_24h.sql`; section 3 of notebooks 03 to 08 |
| G2 Leakage gate | notebook 02 (patient overlap under admission-level splitting); assertions in the cross-validation functions (no patient on both sides) |
| S7 Predictors | `sql/05_predictors/`; notebooks 05 and 08 |
| G3 Sample-size gate | planning: `scripts/g3_planning_assumed_r2.py`; reassessment: notebook 03 (main model and maternal death), notebook 07 section 14 (escalation), notebook 10 section 5 (every fitted set) |
| R1 | maternal death to SMM: `sql/04_labels/05_death_horizon_counts.sql`; notebook 03 |
| S8 Modeling, validation and metrics | notebook 03 (main model); notebook 04 (class imbalance) |
| S9 Sensitivity and robustness | notebooks 06, 07, 08 and 09 |
| G4 Classification gate | notebook 07 (C1, C2, C3), notebook 09 (C4), notebook 10 (C1 and C2 on the fitted models) |
| R2 | `sql/07_timing_audit/03_escalation_counts.sql`, `04_escalation_label.sql`; notebook 07 sections 11 and 14; notebook 09 |
| R4 | notebook 07 sections 10 and 13; notebook 09 `cut2017_landmark_labs` |
| Sample-size reduction | notebook 07 sections 15 and 16; notebook 09 section 10; [`docs/decision_G3_reduction_2026-11-09.md`](docs/decision_G3_reduction_2026-11-09.md) |
| S10 From classification to action | notebook 07 section 12 (race and ethnicity, subgroups) |
| S11 Reporting | `data/outputs_*.txt`; `sql/08_tables/`; `scripts/fig_cohort_funnel.py`, `scripts/fig_framework.py`; summary at the end of every notebook |

Scripts of the first version of the analysis (`sql/02_cohort_mortality/` except `maternal_cohort_expanded.sql`, and `sql/03_cohort_smm/`) are kept for traceability; the discharge-diagnosis groups they build were removed at gate G2.

## Decision log

| Date | Decision | File |
|---|---|---|
| 2026-11-09 | New rule: sample-size reduction after the second classification, with the reduced predictor set fixed before the run | [`docs/decision_G3_reduction_2026-11-09.md`](docs/decision_G3_reduction_2026-11-09.md) |
| 2026-11-11 | Primary learner by events per parameter | [`docs/decision_primary_learner_EPP_2026-11-11.md`](docs/decision_primary_learner_EPP_2026-11-11.md) |
| 2026-11-22 | Gate-G4 criteria on the fitted models; gate G3 for every set in which a model is fitted; G3 in two steps (planning and reassessment); C4 tolerance band as sensitivity; 95% intervals for every decision quantity | [`docs/decision_G4_fitted_models_2026-11-22.md`](docs/decision_G4_fitted_models_2026-11-22.md) |
| 2026-11-23 | Framework 1.3: C1 is decided only by the drop in AUROC (the share of the AUPRC gain kept is reported but does not decide); C4 with a temporal AUROC of 0.70 or more and a calibration slope between 0.90 and 1.10; the class "neither" is called "insufficient signal". The classes of M1 and M2 do not change | [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction) |

## Installation and execution

1. **Get credentialed access to MIMIC-IV** (see [Data access](#data-access)) and download the CSV export (v3.1).
2. **Load the schema locally** following `sql/01_load_mimic_iv_schema/README.md`. `docker-compose.yml` starts PostgreSQL 13 and Jupyter; set `MIMICIV_DATA_DIR` and `MIMICIV_CSV_DIR` in your `.env`.
3. **Build the tables** with the SQL scripts in the order above.
4. **Set your credentials:** copy `.env.example` to `.env` in the project root and fill in your database password. `.env` is git-ignored.
5. **Create an environment and install dependencies:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
6. **Run the notebooks** in the order above (Restart & Run All). The nested validation with bootstrap is computationally heavy (about 10–15 minutes per cross-validation).

Files written into `data/` other than `outputs_*.txt` are patient-level-adjacent and excluded by `.gitignore`. Do not commit them.

## Methodological notes

- The SMM label is an admission-level classification from ICD codes, which carry no date for diagnoses and only a calendar date for procedures. The timing classes of notebook 01 and `sql/07_timing_audit/` place each event relative to T where the evidence allows; 38.4% of the events cannot be dated.
- All splits are grouped by patient. Imputation, scaling, tuning, stacking and recalibration are fitted inside the training part of each fold.
- Single center, no external validation; the temporal validation uses later patients of the same hospital.
- Reporting follows TRIPOD+AI: the checklist submitted with the article is [`article/TRIPOD-AI_checklist.pdf`](article/TRIPOD-AI_checklist.pdf) (editable: `article/TRIPOD-AI_checklist.docx`). It is kept as submitted, so that it matches the published article.

## Data access

This repository does **not** include patient-level data. MIMIC-IV is available through [PhysioNet](https://physionet.org/content/mimiciv/) to researchers who complete the CITI "Data or Specimens Only Research" course, sign the PhysioNet Credentialed Health Data Use Agreement and are granted access.

Reference: Johnson AEW, Bulgarelli L, Shen L, et al. MIMIC-IV, a freely accessible electronic health record dataset. Sci Data. 2023;10:1. https://doi.org/10.1038/s41597-022-01899-x

## Citation

Please cite the article. The full reference (volume, DOI) will be added after publication.

## License

MIT License (see `LICENSE`).

## Contact

Emmanuel Gutiérrez Jiménez — emmanuelg@uninorte.edu.co
