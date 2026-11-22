# Decision log entry — gate-G4 criteria on the fitted models, gate G3 for every fitted set (2026-11-22)

Spanish version: [`decision_G4_fitted_models_2026-11-22_es.md`](decision_G4_fitted_models_2026-11-22_es.md).

**Stage / gate:** G4 (criteria C1, C2 and C4) and G3. **Type of reason:** methodological (consistency between gates G3 and G4).
**Validated by:** Emmanuel Gutiérrez Jiménez (to be confirmed by the thesis supervisor). **Recorded before** notebook 10 was run.

## Context

Notebook 08 evaluated criteria C1 (landmark population) and C2 (documented and strict incident SMM) by **refitting** the full model, with its 32 parameters, inside each subset: 285, 114 and 83 events. The same happened in the development periods of the temporal validation (criterion C4, notebook 09): 209 events for the main model and 46 for escalation of care. Gate G3 had been applied only to the whole population of each outcome, so these fits were never checked against it. With 46 events, the development period of the escalation model is below what G3 requires for 32 parameters (194 events) and for the 13 of the reduced model (89 events).

## Rule (added to the framework on this date)

1. **A criterion of gate G4 that asks how a model behaves in part of its population is evaluated on the model fitted once on its whole population.** Its out-of-fold predictions are restricted to the subset; the model is not refitted there. This applies to C1 (landmark population) and C2 (outcome dated after the prediction point).
2. **Every set on which a model is fitted must pass gate G3.** This includes the development period of the temporal validation (C4). A criterion whose fit would need a set that does not pass G3 is reported as **not assessable**, not as met or not met.
3. **Every decision quantity is reported with its 95% interval** (patient bootstrap, paired between the full population and the subset when the criterion compares them).
4. The thresholds of Table 1 (fixed 2026-11-04) do not change.

## Analyses (single run)

Notebook `10_g4_criteria_fitted_models.ipynb`, same seed, folds, repeats and grids as notebooks 02 and 08, bootstrap B = 1,000:

- Four models fitted once each: main model (M2), return R4 (extended laboratory set), return R2 (escalation, 32 parameters) and return R2 after the sample-size reduction (13 parameters).
- C1 and C2 on their out-of-fold predictions; for escalation, also each component against admissions without escalation and the overlap of the components.
- G3 for the development periods of notebook 09 and, for reference, for the incident populations, with the observed Cox-Snell R² of the cross-validated logistic regression of each fitted model.

Outputs: `data/outputs_g4_fitted_models.txt` and `data/outputs_g3_fitted_subsets.txt`.

## What the earlier results become

The classifications of notebooks 08 and 09 are kept in their reports for traceability. The classification at gate G4 is restated with the results of notebook 10 and recorded below.

## Result

Run of 2026-11-22 with the software versions of the article (scikit-learn 1.6.1, XGBoost 3.0.2); full-population values reproduce notebook 02 (XGBoost AUROC 0.791). XGBoost, 95% patient-bootstrap intervals:

| Model | C1 | C2 | C4 | Classification |
|---|---|---|---|---|
| Main (M2) | Not met: landmark 0.719, drop 0.072 (0.056–0.088), gain kept 40% (30–51%) | **Met**: documented 0.765 (0.713–0.816), strict 0.784 (0.721–0.843) | Not met (development period passes G3) | Early identifier (unchanged) |
| R4 | Not met: landmark 0.740, drop 0.081, gain kept 29% | Met: 0.763 and 0.776 | Not met | Early identifier (unchanged) |
| R2 | Met: landmark 0.765, drop −0.003 | Met: 0.763 | **Not assessable** (46 events; G3 requires 155) | Fails G3 in the whole population (unchanged) |
| R2 reduced | Met: landmark 0.752, drop −0.004 | Not met: 0.749 (0.699–0.798) | **Not assessable** (46 events; G3 requires 71) | Exploratory signal of prediction (unchanged) |

Escalation components (32-parameter model): ICU admission 0.770, mechanical ventilation 0.758, procedure-based indicator 0.702; death fewer than 10 events. Reports: `data/outputs_g4_fitted_models.txt`, `data/outputs_g3_fitted_subsets.txt`.

## Related reporting changes recorded on the same date

- **Gate G3 in two steps.** Planning, before any candidate model is fitted, with an assumed Cox-Snell R² of 15% of its maximum (Riley et al.), and reassessment with the observed out-of-fold R² of the cross-validated penalized logistic regression. Both are reported; the decision is the same for every outcome (`scripts/g3_planning_assumed_r2.py` → `data/outputs_g3_planning.txt`).
- **Counting of candidate parameters.** Columns after one-hot encoding, one per category, without the intercept (32 for the main model; 13 for the reduced escalation model: 3 numerical, 5 binary, 5 race and ethnicity groups). The Riley criteria are applied as a minimum for every learner.
- **Criterion C4.** The classifications of the article keep the rule fixed on 2026-11-04 (95% CI of the slope includes 1). The tolerance band of framework version 1.1 (slope point estimate 0.90–1.10) is reported as a sensitivity analysis: no classification changes (main model 0.83; return R4, landmark, 0.73; escalation not assessable).
- **Intervals.** Every decision quantity is reported with its 95% interval (article, Table 4).
