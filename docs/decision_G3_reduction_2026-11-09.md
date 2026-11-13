# Decision log entry — new framework rule "P3 reduction" (2026-11-09)

> Nomenclature note (2026-11-11): in the English article and code, gate P3 is the sample-size gate G3, P4 the classification gate G4, and stage E7 is S7; this rule is named the *sample-size reduction*. The entry below keeps the codes used when it was recorded. File renamed on 2026-11-13 from `decision_P3_reduction_2026-11-09.md`; the rule was first committed on 2026-11-09 (commit c761e64), before the analysis was run.

**Stage / gate:** P3 (sample size), after the second P4 classification. **Type of reason:** methodological.
**Validated by:** Emmanuel Gutiérrez Jiménez (to be confirmed by the thesis supervisor).

## Context
Return R2 (escalation of care after T, 101 events in 19,268 deliveries) met every applicable criterion of
gate P4 (C1, C2, C4; C3 not applicable) but failed gate P3: with 32 candidate parameters and the observed
Cox-Snell R2 of 0.0077, the shrinkage criterion of Riley et al. required 37,098 admissions; the data
support at most 16 parameters. The two permitted returns (R4, R2) were already used.

## New rule (added to the framework on this date, after the second classification)
When a model meets every applicable criterion of gate P4 but fails gate P3, one **P3 reduction** is allowed
before reporting: the model is refitted once with a reduced predictor set whose number of parameters does
not exceed the maximum supported by the data, chosen by rules fixed in the outcome card and **never** by the
association of a predictor with the outcome. The reduced model must then pass P3 and be classified again at
P4 with the same thresholds. A P3 reduction is not a return and does not count toward the limit of two.
Alternative to the reduction: enlarging the data (more years, another centre or database).

## Reduced predictor set for escalation (fixed before any run)
- Numerical: age at admission, hemoglobin, creatinine (same preprocessing as the main model).
- Binary: creatinine missing; insurance Medicaid (vs other); language English (vs other or missing);
  admission type URGENT (vs other); admission location PHYSICIAN REFERRAL (vs other).
- Categorical: race and ethnicity in five groups — White, Black, Hispanic or Latina, Asian, Other or unknown
  (prefix of the recorded value: WHITE*, BLACK*, HISPANIC* or SOUTH AMERICAN, ASIAN*, everything else).
- Expected parameters: 3 + 5 + 5 = 13 (the run stops if the count exceeds 16).

## Prespecified analyses and criteria (thresholds of Table 1, fixed 2026-11-04)
Single run, XGBoost as primary model, same nested cross-validation grouped by patient, bootstrap B = 300.
- **P3:** Riley et al. criteria with the reduced P and the observed Cox-Snell R2 of the reduced
  cross-validated logistic regression; passes if the required n is at most 19,268.
- **C2:** AUROC >= 0.75 with lower 95% limit >= 0.70 (escalation is the outcome dated after T).
- **C1:** landmark population (SMM present or indeterminate at T removed): AUROC falls by 0.05 or less and at
  least two thirds of the AUPRC gain over prevalence are kept.
- **C3:** not applicable (the outcome does not depend on laboratory testing).
- **C4:** development certainly before 2017, single test from 2017 onward: temporal AUROC >= 0.70 and the
  95% interval of the calibration slope includes 1. Temporal AUROC < 0.65 -> neither.
- **Classification:** passes P3, C1, C2 and C4 -> predictor candidate (pending external validation);
  otherwise the escalation result remains an exploratory signal. The result is reported whatever it is,
  stating that the rule was added after the second classification.

Code: notebooks/08_landmark_incident_smm.ipynb section 15; notebooks/09_temporal_validation_smm.ipynb section 10.
Outputs: data/outputs_escalation_reduced_summary.txt; data/outputs_cut2017_escalation_reduced.txt.

## Result (recorded after the single run, 2026-11-09)
- Reduced set: 13 parameters. **P3: passed** (observed Cox-Snell R2 0.0069; 16,962 admissions and 89 events
  required; 19,268 and 101 available).
- **C1: met** (XGBoost landmark AUROC 0.754 vs 0.749; AUPRC gain kept).
- **C2: not met** by the primary model (XGBoost AUROC 0.749, 0.692-0.798); met by logistic regression
  (0.764, 0.707-0.812) and the stacked ensemble (0.763, 0.703-0.811). Learners did not differ significantly
  (XGBoost - LR -0.016, -0.041 to 0.009); the ensemble did not meet the adoption rule (+0.015, -0.004 to 0.035).
- **C4: not met** by XGBoost (temporal AUROC 0.699, 0.620-0.778; slope 0.88, 0.51-1.25; O/E 1.55); met by
  logistic regression (0.712, slope 0.95) and the ensemble (0.740, slope 1.09).
- **Classification:** exploratory signal of prediction (borderline), now limited by the precision of the
  estimates rather than by sample size. Reported as obtained; the primary model was not changed.
Outputs: data/outputs_escalation_reduced*.txt, data/outputs_escalation_landmark_reduced.txt,
data/outputs_cut2017_escalation_reduced.txt.
