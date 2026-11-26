# Decision log entry — primary learner chosen by events per parameter (2026-11-11)

Spanish version: [`decision_primary_learner_EPP_2026-11-11_es.md`](decision_primary_learner_EPP_2026-11-11_es.md).

**Stage:** S8 (modeling, validation and metrics); decision D16. **Type of reason:** methodological.
**Status:** proposed by the first author; to be validated by the thesis supervisor.
**Scope:** prospective. It applies to outcomes analysed **after** this date (perinatal and neonatal outcomes
of the thesis). It does **not** change the primary model of the SMM article, which stays XGBoost as prespecified.

## Lesson that motivates it
In the reduced escalation model (101 events, 13 parameters, 7.8 events per parameter), logistic regression
was the most accurate and the most stable learner (AUROC 0.764; SD across repeats 0.0075), while XGBoost was
lower and less stable (0.749; SD 0.020), and a wider XGBoost grid made it worse (0.744; SD 0.030;
data/outputs_escalation_reduced_xgbgrid_summary.txt). Flexible learners need many more events per parameter
than regression (van der Ploeg, Austin, Steyerberg, BMC Med Res Methodol 2014;14:137).

## Rule
The primary learner is fixed in the outcome card **before** any model is fitted, from the events per candidate
parameter (EPP) of the development data:
- **EPP below 20:** penalized logistic regression is the primary model; tree-based learners and the ensemble are
  comparisons.
- **EPP of 20 or more:** the primary model is the best base learner of a preliminary run, as before; the ensemble
  is adopted only if it outperforms that learner consistently (unchanged D16 rule).
The threshold of 20 is a convention to be confirmed by the supervisor before the first outcome that uses it.
