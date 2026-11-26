# Outcome card — maternal death and severe maternal morbidity, MIMIC-IV

Outcome card following the staged framework ([StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction)). Models M1 and M2 of the catalogue. Spanish version: [`outcome_card_smm_es.md`](outcome_card_smm_es.md). Decisions are dated in the decision log ([`./`](./)).

## 1. The question

**At 24 hours after admission for delivery, does the model predict maternal morbidity that has not happened yet, or does it recognize morbidity already under way?**

## 2. Identity

| Field | Value |
|---|---|
| Outcome ladder | Rung 1: maternal death (M1). Rung 2: severe maternal morbidity, SMM (M2) |
| Data source | MIMIC-IV v3.1 (Beth Israel Deaconess Medical Center, 2008–2022), credentialed access through PhysioNet |
| Unit and group | Delivery hospitalization; patient as grouping unit (13,710 patients) |
| Population | Delivery hospitalizations still in hospital 24 hours after admission: 19,383 |
| Prediction point (T) | Admission + 24 hours |
| Main label | SMM: at least one of the 20 CDC indicators (ICD-9-CM or ICD-10-CM/PCS) in the same admission: 445 events (2.30%) |
| Timing of the events | Present at T 150 (33.7%), indeterminate 10 (2.2%), documented incident 114 (25.6%), undated 171 (38.4%) |
| Sensitivity labels | Two or more indicators; without renal-only SMM; without non-acute indicators; laboratory AKI after T (C3) |

## 3. Gates and results

Criteria C1 and C2 are evaluated on the model fitted once on its whole population (decision of 2026-11-22). Values are XGBoost with 95% patient-bootstrap intervals.

| Gate or criterion | Main model (M2) | Indicators | Decision |
|---|---|---|---|
| G1 Definition | Passes | Reference counts reproduced in every notebook (`EXPECTED`) | — |
| G2 Leakage | Passes | No discharge-diagnosis groups; no information after T; no patient on both sides of a split | — |
| G3 Sample size | Passes | Planning (assumed Cox-Snell R² 0.030, 15% of the maximum): 9,614 admissions and 221 events required. Reassessment (observed out-of-fold R² 0.0311): 9,112 and 209. Available: 19,383 and 445. 32 parameters (columns after one-hot encoding, no intercept) | Maternal death (M1, 3 events) fails: return R1 to SMM |
| G4 C1 Events present | Not met | AUROC 0.791 → 0.719 (0.686–0.750) in the landmark population; drop 0.072 (0.056–0.088); 40% (30–51%) of the AUPRC gain kept (reported; does not decide C1) | — |
| G4 C2 Outcome with time | Met | Documented incident SMM 0.765 (0.713–0.816); strict incident 0.784 (0.721–0.843) | — |
| G4 C3 Detection bias | Not met | Renal failure dated by creatinine: 0.850 (0.822–0.872) overall, 0.628 (0.584–0.671) among tested patients | — |
| G4 C4 Stability | Not met | Temporal AUROC 0.747 (0.707–0.783); slope 0.83 (0.71–0.97); O/E 1.34 (1.15–1.52). Development period passes G3. With the rule of framework 1.3 (temporal AUROC of 0.70 or more and slope between 0.90 and 1.10): not met | — |
| **G4 Classification** | **Early identifier** | AUROC 0.791 (0.767–0.816); top 10% holds 51.4% of the events | Returns R4 and R2 |

## 4. Returns and sample-size reduction

| Step | Result | Decision |
|---|---|---|
| R4 Extended laboratory set | AUROC 0.821; landmark 0.740, drop 0.081 (0.066–0.098), 29% of the gain kept; C2 met (0.763; 0.776); C3 not met (0.861 → 0.643); C4 not met (landmark temporal 0.697, slope 0.73) | Remains an early identifier: the gain came from which tests were ordered |
| R2 Escalation of care after T | 101 events in 19,268 deliveries; AUROC 0.763; landmark 0.765 (C1 met); C2 met; C4 **not assessable** (46 events in the development period; G3 requires 155). Components: ICU admission 0.770 (90 events), mechanical ventilation 0.758 (38), procedure-based indicator 0.702 (40), death fewer than 10; 39 ICU only, 10 procedure only, 51 two or more | Fails G3 (planning 30,120 admissions and 158 events; reassessment 37,098 and 194) |
| Sample-size reduction (13 parameters) | Passes G3 (planning 12,236 and 64; reassessment 16,962 and 89); C1 met (landmark 0.752); XGBoost C2 not met (0.749, 0.692–0.798; logistic regression 0.764 and ensemble 0.763 met it); C4 **not assessable** (G3 requires 71 development events) | Exploratory signal of prediction. Rule added after the second classification, prompted by the escalation results; reduced set built only from the structure and frequency of the predictors ([`decision_G3_reduction_2026-11-09.md`](decision_G3_reduction_2026-11-09.md)) |

Both permitted returns (R4, R2) are used. G3 planning step: `scripts/g3_planning_assumed_r2.py` → `data/outputs_g3_planning.txt`. Criteria on the fitted models: notebook 10 ([`decision_G4_fitted_models_2026-11-22.md`](decision_G4_fitted_models_2026-11-22.md)).

## 5. Data and conditions of use

No patient-level data leave the local database. Reports in `data/` are aggregates; cells below 10 are suppressed. Use is subject to the PhysioNet Credentialed Health Data Use Agreement.
