# -*- coding: utf-8 -*-
"""Spanish labels for the outputs of the notebooks of this repository (used by libraries/i18n.py when LANG = "es").

Keys are the English labels or lines. In a key, "#" stands for a number: "top #% of risk" matches "top 10% of risk", and
the numbers are put back in the same order in the translation. Learner codes (LR, RF, ET, XGB, Stack), analysis names
(main, landmark, escalation...), variable and column names of the database, hyperparameter names and library names are
not translated. RULES holds lines built from a pattern; {0}, {1}... are the translated groups.
"""

ES = {
    # ---------------------------------------------------------------- general words and column names
    "model": "modelo", "models": "modelos", "learner": "algoritmo", "base learner": "algoritmo base",
    "config": "configuración", "outer_fits": "ajustes externos", "times chosen": "veces elegida",
    "comparison": "comparación", "comparison (first minus second)": "comparación (primero menos segundo)",
    "model comparison (first minus second)": "modelo comparación (primero menos segundo)",
    "strategy": "estrategia", "stratum": "estrato", "analysis": "análisis", "subset": "subconjunto",
    "admissions": "admisiones", "events": "eventos", "patients": "pacientes", "deaths": "muertes", "n": "n",
    "prevalence": "prevalencia", "prev": "prev.", "adm": "adm.", "group": "grupo", "variable": "variable",
    "value": "valor", "total": "total", "note": "nota", "pattern": "patrón", "category": "categoría",
    "timing": "momento", "design": "diseño", "decile": "decil", "fold": "pliegue", "repeat": "repetición",
    "outcome": "desenlace", "role": "rol", "unit": "unidad", "source": "fuente", "fitted on": "ajustado en",
    "parameters": "parámetros", "admissions required": "admisiones requeridas", "events required": "eventos requeridos",
    "available n": "n disponible", "available events": "eventos disponibles", "n required": "n requerido",
    "n shrinkage": "n encogimiento", "n optimism": "n optimismo", "n risk(+#)": "n riesgo(±#)",
    "n risk(+-#)": "n riesgo(±#)", "max R2_CS": "R2_CS máx.", "R2_CS scenario": "escenario de R2_CS",
    "max P supported (n,R2)": "P máx. soportado (n, R2)", "R2_CS": "R2_CS",
    "train_adm": "adm. entren.", "train_pat": "pac. entren.", "train_events": "eventos entren.",
    "train_event_pat": "pac. con evento entren.", "test_adm": "adm. prueba", "test_pat": "pac. prueba",
    "test_events": "eventos prueba", "test_event_pat": "pac. con evento prueba", "shared_patients": "pacientes compartidos",
    "auroc": "AUROC", "auprc": "AUPRC", "brier": "Brier", "slope": "pendiente", "citl": "CITL", "oe": "O/E", "ece": "ECE",
    "sd_auroc_repeats": "DE AUROC entre repeticiones", "sd_auprc_repeats": "DE AUPRC entre repeticiones",
    "sens_top5%": "sens. 5% superior", "ppv_top5%": "VPP 5% superior", "sens_top10%": "sens. 10% superior",
    "ppv_top10%": "VPP 10% superior", "sens_top10": "sens. 10% superior", "mean predicted": "riesgo medio predicho",
    "mean predicted risk": "riesgo medio predicho", "observed/expected": "observados/esperados",
    "calibration slope": "pendiente de calibración", "LR_pred": "LR_pred", "LR_obs": "LR_obs",
    "Stack_pred": "Stack_pred", "Stack_obs": "Stack_obs", "AUROC drop": "caída del AUROC", "auroc drop": "caída del AUROC",
    "AUPRC gain kept": "ganancia del AUPRC conservada", "gain kept": "ganancia conservada",
    "AUROC full": "AUROC completo", "AUROC landmark": "AUROC landmark", "landmark auroc": "AUROC landmark",
    "AUROC diff": "dif. AUROC", "AUPRC diff": "dif. AUPRC", "C1": "C1", "C2": "C2", "C3": "C3", "C4": "C4", "G3": "G3",
    "met": "cumple", "not met": "no cumple", "passes": "pasa", "does NOT pass": "NO pasa", "not assessable": "no evaluable",
    "yes": "sí", "no": "no", "True": "Sí", "False": "No", "OK": "OK", "CHECK": "REVISAR", "n/a": "n/d",
    "before": "antes", "ambiguous": "ambiguo", "after": "después", "distinct admissions with the indicator": "admisiones distintas con el indicador",
    "indicator_name": "indicador", "has_dx": "con diagnóstico", "no diagnosis-based indicator": "sin indicador por diagnóstico",
    "with a diagnosis-based indicator": "con indicador por diagnóstico", "% of SMM": "% de la SMM",
    "admission_type": "tipo de admisión", "delivery": "parto", "other obstetric": "otra obstétrica",
    "at or after T": "en T o después", "before T (stay ended before the prediction point)": "antes de T (la estancia terminó antes del punto de predicción)",
    "escalation": "escalamiento", "icu_after": "UCI después", "vent_after": "ventilación después",
    "smm_proc_after": "procedimiento SMM después", "death_after": "muerte después", "with_smm_label": "con etiqueta SMM",
    "ICU only": "solo UCI", "death only": "solo muerte", "procedure only": "solo procedimiento",
    "two or more components": "dos o más componentes", "development (<#)": "desarrollo (<#)", "test (>=#)": "prueba (>=#)",
    "dev (events, prev %)": "desarrollo (eventos, prev. %)", "test (events, prev %)": "prueba (eventos, prev. %)",
    "train adm/pat/events": "entren. adm./pac./eventos", "test adm/pat/events": "prueba adm./pac./eventos",
    "CV AUROC, same block": "AUROC VC, mismo bloque", "CITL": "CITL", "O/E": "O/E", "AUROC": "AUROC", "AUPRC": "AUPRC",
    "with indicator": "con indicador", "without indicator": "sin indicador",
    "auroc with": "AUROC con", "auroc without": "AUROC sin", "auroc diff (without-with)": "dif. AUROC (sin-con)",
    "auprc with": "AUPRC con", "auprc without": "AUPRC sin", "auprc diff (without-with)": "dif. AUPRC (sin-con)",
    "brier with": "Brier con", "brier without": "Brier sin", "brier diff (without-with)": "dif. Brier (sin-con)",
    "slope with": "pendiente con", "slope without": "pendiente sin", "O/E with": "O/E con", "O/E without": "O/E sin",
    "auroc main": "AUROC main", "auprc main": "AUPRC main", "slope main": "pendiente main",
    "diff (no_admin_vars - main)": "dif. (no_admin_vars - main)", "diff (plus_era - main)": "dif. (plus_era - main)",
    "ICU admission within # h": "ingreso a UCI en las primeras # h", "no ICU within # h": "sin UCI en las primeras # h",
    "LR_auroc": "LR AUROC", "LR_auprc": "LR AUPRC", "Stack_auroc": "Stack AUROC", "Stack_auprc": "Stack AUPRC",
    "train (n, events) replicated": "entrenamiento (n, eventos) replicado", "train expected": "entrenamiento esperado",
    "test (n, events) replicated": "prueba (n, eventos) replicada", "test expected": "prueba esperada", "match": "coincide",
    "patients with >1 admission": "pacientes con >1 admisión", "% patients with >1 admission": "% de pacientes con >1 admisión",
    "median admissions per patient": "mediana de admisiones por paciente", "max admissions per patient": "máximo de admisiones por paciente",
    "positive admissions": "admisiones positivas", "event-bearing patients (unique)": "pacientes con evento (únicos)",
    "positive admissions per event-bearing patient: max": "admisiones positivas por paciente con evento: máximo",
    "# admission(s)": "# admisión(es)", "5 or more": "5 o más", "Model A": "Modelo A", "Model B": "Modelo B",
    "train admissions": "admisiones de entrenamiento", "test admissions": "admisiones de prueba",
    "train events": "eventos de entrenamiento", "test events": "eventos de prueba", "train patients": "pacientes de entrenamiento",
    "test patients": "pacientes de prueba", "test patients also in train": "pacientes de prueba también en entrenamiento",
    "% test patients also in train": "% de pacientes de prueba también en entrenamiento",
    "test admissions with patient in train": "admisiones de prueba con la paciente en entrenamiento",
    "% test admissions with patient in train": "% de admisiones de prueba con la paciente en entrenamiento",
    "positive test admissions whose patient is in train": "admisiones de prueba positivas cuya paciente está en entrenamiento",
    "positive test admissions whose patient has a positive admission in train": "admisiones de prueba positivas cuya paciente tiene una admisión positiva en entrenamiento",
    "event-bearing patients in train": "pacientes con evento en entrenamiento", "event-bearing patients in test": "pacientes con evento en prueba",
    "event-bearing patients in both": "pacientes con evento en ambos lados",
    "ideal": "ideal", "Logistic regression": "Regresión logística", "Stacked ensemble": "Ensamble apilado",
    "Mean predicted risk (decile)": "Riesgo medio predicho (decil)", "Observed SMM rate": "Tasa observada de SMM",

    # ---------------------------------------------------------------- report lines shared by notebooks 02-10
    "[#] Patients per outer partition (repeat # shown; every split verified to share no patient between training and test)":
        "[#] Pacientes por partición externa (se muestra la repetición #; se verificó que ninguna partición comparta pacientes entre entrenamiento y prueba)",
    "Across all # splits: test patients per fold ## event-bearing test patients per fold ## patients present on both sides: #":
        "En las # particiones: pacientes de prueba por pliegue ##, pacientes de prueba con evento por pliegue ##, pacientes en ambos lados: #",
    "[#] Discrimination and overall accuracy (mean over repeats; #% cluster-bootstrap CI)":
        "[#] Discriminación y exactitud global (media de las repeticiones; IC #% por bootstrap de conglomerados)",
    "prevalence = #  (AUPRC of a non-informative model equals the prevalence)":
        "prevalencia = #  (el AUPRC de un modelo sin información es igual a la prevalencia)",
    "[#] Calibration (slope ideal #; calibration-in-the-large ideal #; O/E ideal #; ECE with # quantile bins)":
        "[#] Calibración (pendiente ideal #; calibración global ideal #; O/E ideal #; ECE con # grupos por cuantiles)",
    "[#] Paired differences (same bootstrap samples); the last row compares the ensemble with XGBoost":
        "[#] Diferencias pareadas (mismas muestras bootstrap); la última fila compara el ensamble con XGBoost",
    "[#] Paired differences (same bootstrap samples)": "[#] Diferencias pareadas (mismas muestras bootstrap)",
    "[#] Events captured among the #% / #% of admissions with the highest predicted risk":
        "[#] Eventos captados en el #% / #% de las admisiones con mayor riesgo predicho",
    "[#] Net benefit (decision curve) at the stated threshold probabilities":
        "[#] Beneficio neto (curva de decisión) en las probabilidades umbral indicadas",
    "[#] Net benefit by threshold probability": "[#] Beneficio neto por probabilidad umbral",
    "Paired net-benefit differences:": "Diferencias pareadas de beneficio neto:",
    "[#] Performance by ICU admission within the first # h (same predictions, stratified evaluation)":
        "[#] Desempeño según ingreso a UCI en las primeras # h (mismas predicciones, evaluación estratificada)",
    "[#] Performance by ICU admission within the first # h (point estimates, same predictions)":
        "[#] Desempeño según ingreso a UCI en las primeras # h (estimaciones puntuales, mismas predicciones)",
    "[#] Calibration by decile of predicted risk (outer-test predictions; mean over repeats)":
        "[#] Calibración por decil de riesgo predicho (predicciones de prueba externa; media de las repeticiones)",
    "[#] Calibration by decile of predicted risk (mean over repeats)":
        "[#] Calibración por decil de riesgo predicho (media de las repeticiones)",
    "[#] Hyperparameters selected in the inner loops (out of # outer fits per learner)":
        "[#] Hiperparámetros elegidos en los ciclos internos (de # ajustes externos por algoritmo)",
    "[#] Hyperparameters chosen in the inner loops of the development set":
        "[#] Hiperparámetros elegidos en los ciclos internos del conjunto de desarrollo",
    "Repeats=# outer folds=# inner folds=# bootstrap B=# QUICK=False":
        "Repeticiones=#, pliegues externos=#, pliegues internos=#, bootstrap B=#, QUICK=False",
    "Repeats=# outer folds=# inner folds=# bootstrap B=# QUICK=True":
        "Repeticiones=#, pliegues externos=#, pliegues internos=#, bootstrap B=#, QUICK=True",
    "# admissions, # patients, # events (#%), numeric=# binary=# categorical=#":
        "# admisiones, # pacientes, # eventos (#%), numéricas=#, binarias=#, categóricas=#",
    "MODEL B -- Riley et al. criteria": "MODELO B -- criterios de Riley et al.",
    "observed (cross-validated LR)": "observado (LR con validación cruzada)",
    "15% of max (default)": "15% del máximo (por defecto)", "30% of max": "30% del máximo", "50% of max": "50% del máximo",
    "Eligible any obstetric admissions:": "Admisiones obstétricas elegibles de cualquier tipo:",
    "Dictionary roles ->": "Roles del diccionario ->",
    "Values set to missing by plausibility limits (count per variable):": "Valores llevados a faltante por los límites de plausibilidad (conteo por variable):",
    "R2_CS observed = mean over repeats of the Cox-Snell R2 of the out-of-fold logistic regression predictions":
        "R2_CS observado = media de las repeticiones del R2 de Cox-Snell de las predicciones fuera de muestra de la regresión logística",
    "-> gate G3 passes": "-> la puerta G3 pasa", "-> gate G3 does NOT pass": "-> la puerta G3 NO pasa",
    "-> gate G3 passes: # admissions available": "-> la puerta G3 pasa: # admisiones disponibles",
    "-> gate G3 does NOT pass: # admissions available": "-> la puerta G3 NO pasa: # admisiones disponibles",

    # ---------------------------------------------------------------- notebook 01
    "6.1 Hold-out 80/20 (replicated admission-level split)": "6.1 Reserva 80/20 (partición por admisión replicada)",
    "6.3a Hold-out: #,# random stratified 80/20 splits -- median (#th-#th percentile)":
        "6.3a Reserva: #.# particiones estratificadas aleatorias 80/20 -- mediana (percentil #-#)",
    "6.3a Hold-out: # random stratified 80/20 splits -- median (#th-#th percentile)":
        "6.3a Reserva: # particiones estratificadas aleatorias 80/20 -- mediana (percentil #-#)",
    "6.3b 5-fold CV: # repetitions -- median (#th-#th percentile); % = mean over folds, counts = summed over folds":
        "6.3b VC de 5 pliegues: # repeticiones -- mediana (percentil #-#); % = media de los pliegues, conteos = suma de los pliegues",
    "6.2 Model A: 5-fold CV, per fold": "6.2 Modelo A: VC de 5 pliegues, por pliegue",
    "6.2 Model B: 5-fold CV, per fold": "6.2 Modelo B: VC de 5 pliegues, por pliegue",
    "Model A - mortality (baseline label)": "Modelo A - mortalidad (etiqueta de la primera versión)",
    "Model B - SMM (baseline label)": "Modelo B - SMM (etiqueta de la primera versión)",

    # ---------------------------------------------------------------- notebook 03
    "[S1] After recalibration (Platt): discrimination and calibration; #% cluster-bootstrap intervals":
        "[S1] Después de la recalibración (Platt): discriminación y calibración; intervalos #% por bootstrap de conglomerados",
    "[S2] Before recalibration (raw probabilities of each algorithm); observed prevalence = #":
        "[S2] Antes de la recalibración (probabilidades originales de cada algoritmo); prevalencia observada = #",
    "[S3] Paired differences between strategies (same bootstrap samples)":
        "[S3] Diferencias pareadas entre estrategias (mismas muestras bootstrap)",
    "[S4] Configurations selected in the inner loops (per learner, out of # outer fits)":
        "[S4] Configuraciones elegidas en los ciclos internos (por algoritmo, de # ajustes externos)",
    "-- No weights, no resampling": "-- Sin pesos ni remuestreo", "-- Class weights only": "-- Solo pesos de clase",
    "-- SMOTENC only (no weights)": "-- Solo SMOTENC (sin pesos)",
    "unweighted": "sin pesos", "weighted": "con pesos", "smote": "SMOTENC",

    # ---------------------------------------------------------------- notebook 04
    "[#] Discrimination and Brier score with and without the indicator (paired; #% cluster-bootstrap intervals)":
        "[#] Discriminación y Brier con y sin el indicador (pareado; intervalos #% por bootstrap de conglomerados)",
    "[#] Calibration after recalibration (slope; observed/expected)": "[#] Calibración después de la recalibración (pendiente; observados/esperados)",
    "Calibration after recalibration (slope; observed/expected)": "Calibración después de la recalibración (pendiente; observados/esperados)",
    "[#] Creatinine availability that the indicator encodes (eligible deliveries)":
        "[#] Disponibilidad de la creatinina que codifica el indicador (partos elegibles)",
    "creatinine present: #% overall | #% without SMM | #% with SMM":
        "creatinina presente: #% en total | #% sin SMM | #% con SMM",
    "ICU within # h: #% | no ICU within # h: #%": "UCI en las primeras # h: #% | sin UCI en las primeras # h: #%",
    "[#] Hyperparameters selected in the inner loops, with indicator (out of # outer fits per learner)":
        "[#] Hiperparámetros elegidos en los ciclos internos, con indicador (de # ajustes externos por algoritmo)",
    "[#] Hyperparameters selected in the inner loops, without indicator (out of # outer fits per learner)":
        "[#] Hiperparámetros elegidos en los ciclos internos, sin indicador (de # ajustes externos por algoritmo)",

    # ---------------------------------------------------------------- notebook 05
    "[#] Eligible deliveries by anchor-year group and by ICD coding version (aggregate counts)":
        "[#] Partos elegibles por grupo de año de anclaje y por versión de la codificación CIE (conteos agregados)",
    "Admissions by anchor-year group (rows) and ICD coding version (columns)":
        "Admisiones por grupo de año de anclaje (filas) y versión de la codificación CIE (columnas)",
    "[#] Cross-validated performance by group (out-of-fold predictions of the main analysis; patients are in the same folds as notebooks #/#)":
        "[#] Desempeño con validación cruzada por grupo (predicciones fuera de muestra del análisis principal; las pacientes están en los mismos pliegues que en los notebooks #/#)",
    "O/E and slope come from probabilities calibrated on the whole development sample, so O/E far from # in one group means a calibration shift between groups.":
        "O/E y pendiente vienen de probabilidades calibradas con toda la muestra de desarrollo; un O/E lejos de # en un grupo indica un cambio de calibración entre grupos.",
    "[#] Temporal validation (rolling origin) and ICD-# -> ICD-# transition: models fitted only on the earlier block, scored on the later one":
        "[#] Validación temporal (origen móvil) y transición CIE-# -> CIE-#: modelos ajustados solo con el bloque anterior y evaluados en el posterior",
    "Patients with admissions in the later block are removed from the earlier block. Each model is tuned, stacked and recalibrated inside the earlier block only.":
        "Las pacientes con admisiones en el bloque posterior se retiran del anterior. Cada modelo se ajusta, apila y recalibra solo dentro del bloque anterior.",
    "Paired difference Stack - LR in the later block (#% patient-level cluster-bootstrap interval)":
        "Diferencia pareada Stack - LR en el bloque posterior (intervalo #% por bootstrap de pacientes)",
    "[#] Refits without the administrative variables that can reflect the era, and with the era added as a diagnostic":
        "[#] Reajustes sin las variables administrativas que pueden reflejar la época, y con la época agregada como diagnóstico",
    "AUROC (paired, #% patient-level cluster-bootstrap intervals for the differences)":
        "AUROC (pareado; intervalos #% por bootstrap de pacientes para las diferencias)",
    "AUPRC (paired, #% patient-level cluster-bootstrap intervals for the differences)":
        "AUPRC (pareado; intervalos #% por bootstrap de pacientes para las diferencias)",
    "Hyperparameters selected in the inner loops, main (out of # outer fits per learner)":
        "Hiperparámetros elegidos en los ciclos internos, main (de # ajustes externos por algoritmo)",
    "Hyperparameters selected in the inner loops, no_admin_vars (out of # outer fits per learner)":
        "Hiperparámetros elegidos en los ciclos internos, no_admin_vars (de # ajustes externos por algoritmo)",
    "Hyperparameters selected in the inner loops, plus_era (out of # outer fits per learner)":
        "Hiperparámetros elegidos en los ciclos internos, plus_era (de # ajustes externos por algoritmo)",
    "Eligible deliveries with missing era:": "Partos elegibles sin época:",
    "anchor_year_group values not in ERA_ORDER:": "valores de anchor_year_group que no están en ERA_ORDER:",

    # ---------------------------------------------------------------- notebook 07
    "T = admission time + # h; timing from the calendar date of each procedure-based SMM indicator (see the method table)":
        "T = hora de admisión + # h; momento según la fecha calendario de cada indicador de SMM por procedimiento (ver la tabla del método)",
    "[#] Category of every SMM admission (A to D); the last columns split by presence of a diagnosis-based indicator":
        "[#] Categoría de cada admisión con SMM (A a D); las últimas columnas separan según haya un indicador por diagnóstico",
    "Sum of categories: #  [OK]": "Suma de las categorías: #  [OK]", "Sum of categories: #  [CHECK]": "Suma de las categorías: #  [REVISAR]",
    "Reading: at least # SMM admissions (#%) had a procedure indicator certainly before T; # more (#%) cannot be ordered;":
        "Lectura: al menos # admisiones con SMM (#%) tenían un indicador por procedimiento con certeza antes de T; otras # (#%) no se pueden ordenar;",
    "# (#%) have procedure indicators only after T; # (#%) rest on diagnosis codes alone and cannot be placed in time.":
        "# (#%) tienen indicadores por procedimiento solo después de T; # (#%) dependen solo de códigos de diagnóstico y no se pueden ubicar en el tiempo.",
    "[#] Procedure-based indicators: admissions by timing of the indicator (an admission with the same indicator on different days can appear in":
        "[#] Indicadores por procedimiento: admisiones según el momento del indicador (una admisión con el mismo indicador en días distintos puede aparecer en",
    "several of the first three columns, so they need not add up to the last column, which counts each admission once)":
        "varias de las tres primeras columnas, por lo que no tienen que sumar la última, que cuenta cada admisión una vez)",
    "CONSISTENCY CHECKS": "VERIFICACIONES DE CONSISTENCIA",
    "[#] In-hospital deaths of the obstetric universe by timing relative to T": "[#] Muertes hospitalarias del universo obstétrico según su momento respecto a T",
    "Deaths: # (expected #); before T: # (expected #)  [OK]": "Muertes: # (esperadas #); antes de T: # (esperadas #)  [OK]",
    "SMM admissions among eligible delivery hospitalizations: #  (expected #) [OK]":
        "Admisiones con SMM entre las hospitalizaciones de parto elegibles: #  (esperadas #) [OK]",

    # ---------------------------------------------------------------- notebooks 08-10
    "ESCALATION AFTER T (RETURN R2) SUMMARY (QUICK=False); bootstrap B=#; counts below # shown as <#":
        "RESUMEN DEL ESCALAMIENTO DESPUÉS DE T (RETORNO R2) (QUICK=False); bootstrap B=#; conteos menores de # se muestran como <#",
    "[#] Components of the composite (an admission can have several)": "[#] Componentes del desenlace compuesto (una admisión puede tener varios)",
    "[#] Discrimination and calibration; C2 = AUROC >= # and lower #% limit >= #":
        "[#] Discriminación y calibración; C2 = AUROC >= # y límite inferior del #% >= #",
    "Overlap of the components among escalation events (an event can have several components)":
        "Superposición de los componentes entre los eventos de escalamiento (un evento puede tener varios componentes)",
    "RICHER PREDICTORS SUMMARY (QUICK=False); references: outputs_landmark, outputs_incident_documented, outputs_incident_strict":
        "RESUMEN DE LOS PREDICTORES AMPLIADOS (QUICK=False); referencias: outputs_landmark, outputs_incident_documented, outputs_incident_strict",
    "CRITERION C3 FOR THE EXTENDED LABORATORY MODEL (QUICK=False); bootstrap B=#":
        "CRITERIO C3 PARA EL MODELO CON LABORATORIOS AMPLIADOS (QUICK=False); bootstrap B=#",
    "RACE AND ETHNICITY SUMMARY (QUICK=False); bootstrap B=#; groups with < # events or non-events: counts only":
        "RESUMEN DE RAZA Y ETNIA (QUICK=False); bootstrap B=#; grupos con < # eventos o no eventos: solo conteos",
    "[#] Overall discrimination, with race minus without race (paired patient bootstrap)":
        "[#] Discriminación global, con raza menos sin raza (bootstrap pareado de pacientes)",
    "[#] Performance and calibration by racial and ethnic group": "[#] Desempeño y calibración por grupo racial y étnico",
    "Recorded race and ethnicity categories and the collapsed group (counts below # suppressed):":
        "Categorías de raza y etnia registradas y el grupo agrupado (conteos menores de # suprimidos):",
    "GATE G3 (RILEY CRITERIA) FOR THE OUTCOME OF RETURN R2 (QUICK=False)":
        "PUERTA G3 (CRITERIOS DE RILEY) PARA EL DESENLACE DEL RETORNO R2 (QUICK=False)",
    "SAMPLE-SIZE REDUCTION (G3) FOR ESCALATION (RETURN R2), QUICK=False, bootstrap B=#":
        "REDUCCIÓN POR TAMAÑO DE MUESTRA (G3) PARA EL ESCALAMIENTO (RETORNO R2), QUICK=False, bootstrap B=#",
    "Rule and reduced set: docs/decision_G3_reduction_#-#-#.md (fixed before this run)":
        "Regla y conjunto reducido: docs/decision_G3_reduction_#-#-#.md (fijados antes de esta corrida)",
    "EXPLORATORY (post hoc): WIDER XGBOOST GRID, REDUCED ESCALATION MODEL, QUICK=False, bootstrap B=#":
        "EXPLORATORIO (post hoc): MALLA DE XGBOOST AMPLIADA, MODELO DE ESCALAMIENTO REDUCIDO, QUICK=False, bootstrap B=#",
    "Criterion C1 (drop <= # and gain kept >= #/#), paired patient bootstrap":
        "Criterio C1 (caída <= # y ganancia conservada >= #/#), bootstrap pareado de pacientes",
    "C3: not applicable. C4: notebook #, section #.": "C3: no aplica. C4: notebook #, sección #.",
    "GATE G4 CRITERIA ON THE FITTED MODELS (no refitting inside subsets), QUICK=False, bootstrap B=#":
        "CRITERIOS DE LA PUERTA G4 SOBRE LOS MODELOS AJUSTADOS (sin reajustar en los subconjuntos), QUICK=False, bootstrap B=#",
    "Each model was fitted once on its whole population (patient-grouped nested cross-validation); every subset uses":
        "Cada modelo se ajustó una vez en toda su población (validación cruzada anidada y agrupada por paciente); cada subconjunto usa",
    "the same out-of-fold predictions. Counts below # are shown as <#.":
        "las mismas predicciones fuera de muestra. Los conteos menores de # se muestran como <#.",
    "GATE G3 FOR THE SUBSETS IN WHICH A MODEL IS FITTED (QUICK=False)":
        "PUERTA G3 PARA LOS SUBCONJUNTOS EN LOS QUE SE AJUSTA UN MODELO (QUICK=False)",
    "A model whose fitting set does not pass G3 is not evaluated for the criterion that needs it (reported as not assessable).":
        "Un modelo cuyo conjunto de ajuste no pasa G3 no se evalúa en el criterio que lo necesita (se reporta como no evaluable).",
    "TEMPORAL VALIDATION SUMMARY (QUICK=False)": "RESUMEN DE LA VALIDACIÓN TEMPORAL (QUICK=False)",
    "[#] Discrimination in the later period (mean over repeats; #% patient-level bootstrap CI)":
        "[#] Discriminación en el período posterior (media de las repeticiones; IC #% por bootstrap de pacientes)",
    "[#] Calibration in the later period (observed prevalence #; O/E > # = risk underestimated)":
        "[#] Calibración en el período posterior (prevalencia observada #; O/E > # = riesgo subestimado)",
    "CRITERION C4 (reduced escalation model): temporal AUROC >= # and #% interval of the slope includes #":
        "CRITERIO C4 (modelo de escalamiento reducido): AUROC temporal >= # y el intervalo del #% de la pendiente incluye #",
    "EXPLORATORY C4 (wider XGBoost grid): temporal AUROC >= # and #% interval of the slope includes #":
        "C4 EXPLORATORIO (malla de XGBoost ampliada): AUROC temporal >= # y el intervalo del #% de la pendiente incluye #",
    "PREDICTORS AND OUTCOME BY PERIOD, cut # (development vs test as analysed in cut#)":
        "PREDICTORES Y DESENLACE POR PERÍODO, corte # (desarrollo frente a prueba como se analizó en cut#)",
    "Values are n (%) unless stated; counts ## shown as <#; rare categories grouped.":
        "Los valores son n (%) salvo que se indique otra cosa; los conteos ## se muestran como <#; las categorías raras se agrupan.",
    "Values are n (%) unless stated; counts #-# shown as <#; rare categories grouped.":
        "Los valores son n (%) salvo que se indique otra cosa; los conteos #-# se muestran como <#; las categorías raras se agrupan.",
    "Laboratory variables added:": "Variables de laboratorio agregadas:", "main predictors:": "predictores principales:",
    "\nSMM deliveries by number of indicators (eligible):": "Partos con SMM según el número de indicadores (elegibles):",
    "SMM deliveries by number of indicators (eligible):": "Partos con SMM según el número de indicadores (elegibles):",
    "XGBoost configurations chosen in the inner loops (full population):": "Configuraciones de XGBoost elegidas en los ciclos internos (población completa):",
}

# Lines built from a pattern (group 0, 1...: translated recursively)
RULES = [
    (r"ANALYSIS (\S+): (.*)", "ANÁLISIS {0}: {1}"),
    (r"MODEL (\S+): # admissions, # events, parameters=#".replace("#", r"(\S+)"),
     "MODELO {0}: {1} admisiones, {2} eventos, parámetros={3}"),
    (r"TEMPORAL VALIDATION (\S+) \(cut (\d+)\), (.*)", "VALIDACIÓN TEMPORAL {0} (corte {1}), {2}"),
    (r"(QUICK=\w+), repeats=(\d+), bootstrap B=(\d+)", "{0}, repeticiones={1}, bootstrap B={2}"),
    (r"\[(\S+)\] first outer fold took (\S+) min -> projected total about (\S+) min",
     "[{0}] el primer pliegue externo tardó {1} min -> total proyectado de unos {2} min"),
    (r"\[(\S+)\] cross-validation finished in (\S+) min; every admission scored exactly once per repeat: (\w+)",
     "[{0}] validación cruzada terminada en {1} min; cada admisión evaluada exactamente una vez por repetición: {2}"),
    (r"\[(\S+)\] repeat (\S+) done \((\S+) min\)", "[{0}] repetición {1} terminada ({2} min)"),
    (r"\[(\S+)\] evaluated in (\S+) min", "[{0}] evaluado en {1} min"),
    (r"\[(\S+)\] not in memory: re-running the cross-validation without bootstrap",
     "[{0}] no está en memoria: se vuelve a correr la validación cruzada sin bootstrap"),
    (r"\[(.+)\] SKIPPED \(train events (\S+), test events (\S+)\)", "[{0}] OMITIDO (eventos de entrenamiento {1}, de prueba {2})"),
    (r"\[(.+)\] fitted in (\S+) min \(train adm (\S+), test adm (\S+)\)",
     "[{0}] ajustado en {1} min (adm. de entrenamiento {2}, de prueba {3})"),
    (r"bootstrap: 5 replicates took (\S+) s -> projected (\S+) min for B=(\S+)",
     "bootstrap: 5 réplicas tardaron {0} s -> proyectado {1} min para B={2}"),
    (r"\[aggregate report saved as (\S+)\s+\((\S+) characters\)\]", "[reporte agregado guardado como {0}  ({1} caracteres)]"),
    (r"(\S+): (\S+)\s+\(expected (\S+)\)\s+\[OK\]", "{0}: {1}  (esperado {2})  [OK]"),
    (r"(\S+): (\S+)\s+\(expected (\S+)\)\s+\[CHECK: differs from the audit counts\]",
     "{0}: {1}  (esperado {2})  [REVISAR: difiere de los conteos de la auditoría]"),
    (r"(\S+)\s+admissions=\s*(\d+)\s+patients=\s*(\d+)\s+events=\s*(\d+)\s+numeric=(\d+)\s+binary=(\d+)\s+categorical=(\d+)",
     "{0}: admisiones={1}, pacientes={2}, eventos={3}, numéricas={4}, binarias={5}, categóricas={6}"),
    (r"(\S+) \(label (\S+)\): n=(\S+) events=(\S+) prevalence=(\S+) candidate parameters P=(\S+) EPP=(\S+)",
     "{0} (etiqueta {1}): n={2}, eventos={3}, prevalencia={4}, parámetros candidatos P={5}, EPP={6}"),
    (r"(.+): n=(\S+), events=(\S+), prevalence=(\S+), candidate parameters P=(\S+), EPP=(\S+)",
     "{0}: n={1}, eventos={2}, prevalencia={3}, parámetros candidatos P={4}, EPP={5}"),
    (r"Model B \(SMM, eligible deliveries\)", "Modelo B (SMM, partos elegibles)"),
    (r"Model A \(in-hospital mortality, eligible deliveries; ASSUMED R2, no model trained\)",
     "Modelo A (mortalidad hospitalaria, partos elegibles; R2 SUPUESTO, sin modelo ajustado)"),
    (r"Eligible deliveries: (\S+) admissions, (\S+) patients, deaths in the same admission = (\S+)",
     "Partos elegibles: {0} admisiones, {1} pacientes, muertes en la misma admisión = {2}"),
    (r"Eligible obstetric \(any\): (\S+) admissions, (\S+) patients, deaths in the same admission = (\S+)",
     "Obstétricas elegibles (cualquiera): {0} admisiones, {1} pacientes, muertes en la misma admisión = {2}"),
    (r"Rule of thumb for context: (\S+) events per candidate parameter would need (\S+) deaths; (\S+) are available\.",
     "Regla práctica como contexto: {0} eventos por parámetro candidato exigirían {1} muertes; hay {2}."),
    (r"Development \(year_hi < (\S+)\): (\S+) admissions, (\S+) patients, (\S+) events \(prevalence (\S+)\)",
     "Desarrollo (year_hi < {0}): {1} admisiones, {2} pacientes, {3} eventos (prevalencia {4})"),
    (r"Discarded \(interval straddles (\S+)\): (\S+) admissions, (\S+) events",
     "Descartadas (el intervalo cruza {0}): {1} admisiones, {2} eventos"),
    (r"Test \(year_lo >= (\S+)\): (\S+) admissions; removed because the patient is in development: (\S+) \((\S+) events\)",
     "Prueba (year_lo >= {0}): {1} admisiones; retiradas porque la paciente está en desarrollo: {2} ({3} eventos)"),
    (r"Test analysed: (\S+) admissions, (\S+) patients, (\S+) events \(prevalence (\S+)\)",
     "Prueba analizada: {0} admisiones, {1} pacientes, {2} eventos (prevalencia {3})"),
    (r"WARNING: (\S+) has only (\S+) events; estimates will be unstable \(report as exploratory\)\.",
     "ADVERTENCIA: {0} tiene solo {1} eventos; las estimaciones serán inestables (reportar como exploratorio)."),
    (r"WARNING: (\S+) has only (\S+) events in the (\S+) set; report as exploratory\.",
     "ADVERTENCIA: {0} tiene solo {1} eventos en el conjunto de {2}; reportar como exploratorio."),
    (r"NOTE: (\S+) has (\S+) events \(< 100\): report as exploratory\.",
     "NOTA: {0} tiene {1} eventos (< 100): reportar como exploratorio."),
    (r"Hyperparameters selected in the inner loops, (\S+) \(out of (\S+) outer fits per learner\)",
     "Hiperparámetros elegidos en los ciclos internos, {0} (de {1} ajustes externos por algoritmo)"),
    (r"\[(\d)\] Hyperparameters selected in the inner loops, (\S+) \(out of (\S+) outer fits per learner\)",
     "[{0}] Hiperparámetros elegidos en los ciclos internos, {1} (de {2} ajustes externos por algoritmo)"),
    (r"=== strategy: (\S+) \((.+)\)", "=== estrategia: {0} ({1})"),
    (r"R2_CS observed \(cross-validated LR of the whole-period model\): (.*)",
     "R2_CS observado (LR con validación cruzada del modelo del período completo): {0}"),
    (r"Reduced set: (\S+) parameters \(maximum allowed (\S+)\)", "Conjunto reducido: {0} parámetros (máximo permitido {1})"),
    (r"Reduced set in the development period: (\S+) parameters \(maximum allowed (\S+)\)",
     "Conjunto reducido en el período de desarrollo: {0} parámetros (máximo permitido {1})"),
    (r"XGBoost grid: (\S+) configurations \(prespecified grid: (\S+)\); tuned inside inner folds only",
     "Malla de XGBoost: {0} configuraciones (malla preespecificada: {1}); ajustada solo dentro de los pliegues internos"),
    (r"With an SMM code: (\S+) of (\S+)", "Con un código de SMM: {0} de {1}"),
    (r"\[Model (\S)\] (.+)", "[Modelo {0}] {1}"),
    (r"\[(\d)\] Delivery hospitalizations not eligible at 24 h: (\S+) \(expected (\S+)\), with SMM (\S+) \(expected (\S+)\), with death (\S+) \(expected (\S+)\)\s+\[(\w+)\]",
     "[{0}] Hospitalizaciones de parto no elegibles a las 24 h: {1} (esperadas {2}), con SMM {3} (esperadas {4}), con muerte {5} (esperadas {6})  [{7}]"),
    (r"(ERA / TEMPORAL SENSITIVITY|CREATININE MISSINGNESS INDICATOR|RESAMPLING COMPARISON): SMM, eligible deliveries, (.*)",
     "{0}: SMM, partos elegibles, {1}"),
    (r"(\S+) \(cut (\S+)\)", "{0} (corte {1})"),
]
ES.update({
    "ERA / TEMPORAL SENSITIVITY": "SENSIBILIDAD A LA ÉPOCA Y AL TIEMPO",
    "CREATININE MISSINGNESS INDICATOR": "INDICADOR DE CREATININA FALTANTE", "RESAMPLING COMPARISON": "COMPARACIÓN DEL REMUESTREO",
    "Model A - mortality (baseline label)": "Modelo A - mortalidad (etiqueta de la primera versión)",
    "No weights, no resampling": "Sin pesos ni remuestreo", "Class weights only": "Solo pesos de clase", "SMOTENC only (no weights)": "Solo SMOTENC (sin pesos)",
    "test": "prueba", "train": "entrenamiento", "development": "desarrollo",
})

# Notebook 01 (tables) and the progress lines of the other notebooks
ES.update({
    "Tables of the first version, loaded": "Tablas de la primera versión, cargadas",
    "Model B - SMM (baseline label)": "Modelo B - SMM (etiqueta de la primera versión)",
    "positive admissions": "admisiones positivas", "expected positive admissions": "admisiones positivas esperadas",
    "check": "verificación", "CHECK: differs from expected count": "REVISAR: difiere del conteo esperado",
    "Replication of the first-version hold-out split": "Réplica de la partición de reserva de la primera versión",
    "train expected": "entrenamiento esperado", "test (n, events) replicated": "prueba (n, eventos) replicado",
    "test expected": "prueba esperado", "match": "coincide",
    "Compact summary of patient overlap (aggregates only)": "Resumen compacto del solapamiento de pacientes (solo agregados)",
    "patients with >1 admission (%)": "pacientes con >1 admisión (%)",
    "event-bearing patients (unique)": "pacientes con evento (únicas)",
    "hold-out replication matches expected sizes and events": "la réplica de la reserva coincide en tamaños y eventos",
    "hold-out: test patients also in train": "reserva: pacientes de prueba también en entrenamiento",
    "hold-out: test admissions with patient in train": "reserva: admisiones de prueba con la paciente en entrenamiento",
    "hold-out: positive test admissions whose patient is in train": "reserva: admisiones positivas de prueba con la paciente en entrenamiento",
    "hold-out: positive test admissions whose patient has a positive admission in train":
        "reserva: admisiones positivas de prueba con la paciente con una admisión positiva en entrenamiento",
    "hold-out: event-bearing patients train/test/both": "reserva: pacientes con evento entrenamiento/prueba/ambos",
    "5-fold CV: mean % test patients also in train": "VC de 5 pliegues: % medio de pacientes de prueba también en entrenamiento",
    "5-fold CV: mean % test admissions with patient in train": "VC de 5 pliegues: % medio de admisiones de prueba con la paciente en entrenamiento",
    "5-fold CV: positive test admissions whose patient is in train (sum of folds)":
        "VC de 5 pliegues: admisiones positivas de prueba con la paciente en entrenamiento (suma de pliegues)",
    "5-fold CV: positive test admissions whose patient has a positive admission in train (sum of folds)":
        "VC de 5 pliegues: admisiones positivas de prueba con la paciente con una admisión positiva en entrenamiento (suma de pliegues)",
    "simulation, 1000 hold-out splits: % test admissions with patient in train":
        "simulación, 1000 particiones de reserva: % de admisiones de prueba con la paciente en entrenamiento",
    "simulation, 1000 hold-out splits: positive test admissions whose patient is in train":
        "simulación, 1000 particiones de reserva: admisiones positivas de prueba con la paciente en entrenamiento",
    "Eligible any obstetric admissions: 1 | SMM: 1 | deaths: 1": "Admisiones obstétricas elegibles (cualquiera): 1 | SMM: 1 | muertes: 1",
    "anchor_year_group values not in ERA_ORDER: none": "valores de anchor_year_group fuera de ERA_ORDER: ninguno",
    "Eligible deliveries with missing era: 1": "Partos elegibles sin época: 1",
    "Eligible deliveries with timing flags: 1 (expected 1) [OK]": "Partos elegibles con marcas de tiempo: 1 (esperado 1) [OK]",
    "Strict incident events: 1": "Eventos incidentes estrictos: 1",
    "Laboratory AKI at or before T: 1;  after T: 1 (of which with an SMM code: 1)":
        "LRA por laboratorio en T o antes: 1;  después de T: 1 (de ellas con código de SMM: 1)",
    "ICU admission before T: 1 admissions (1 with SMM)": "Ingreso a UCI antes de T: 1 admisiones (1 con SMM)",
    "aki_lab_incident population: 1 admissions, 1 events (1%)": "Población aki_lab_incident: 1 admisiones, 1 eventos (1%)",
    "creatinine measured in the first 1 h: 1 admissions (1%), 1 events (1%)":
        "creatinina medida en las primeras 1 h: 1 admisiones (1%), 1 eventos (1%)",
    "of which eligible SMM deliveries: 1": "de ellas, partos elegibles con SMM: 1",
    "C3: not applicable. C4: notebook 1 section 1.": "C3: no aplica. C4: notebook 1, sección 1.",
    "Eligible deliveries: 1 (expected 1); with a year interval: 1": "Partos elegibles: 1 (esperado 1); con intervalo de año: 1",
    "escalation population: 1 (expected 1); events: 1 (expected 1)  [OK]":
        "población de escalamiento: 1 (esperado 1); eventos: 1 (esperado 1)  [OK]",
})
RULES += [
    (r"Dictionary roles -> (.*)", "Roles del diccionario -> {0}"),
    (r"Values set to missing by plausibility limits \(count per variable\): (.*)",
     "Valores puestos como faltantes por límites de plausibilidad (conteo por variable): {0}"),
    (r"(\{.*\}) configurations per strategy", "{0} configuraciones por estrategia"),
    (r"predictors with indicator\s*: (.*)", "predictores con indicador   : {0}"),
    (r"predictors without indicator\s*: (.*)", "predictores sin indicador   : {0}"),
    (r"main predictors: (.*)", "predictores de main: {0}"),
    (r"outer (\S+), inner (\S+), paired bootstrap B=(\S+), (QUICK=\S+)",
     "externos {0}, internos {1}, bootstrap pareado B={2}, {3}"),
    (r"outer (\S+), inner (\S+), bootstrap B=(\S+) \(groups, temporal\) / (\S+) \(paired refits\), (QUICK=\S+)",
     "externos {0}, internos {1}, bootstrap B={2} (grupos, temporal) / {3} (reajustes pareados), {4}"),
    (r"(QUICK=\S+)\s+outer=(\S+)\s+inner=(\S+)\s+B=(\S+)\s+trees=(\S+)",
     "{0}  externos={1}  internos={2}  B={3}  árboles={4}"),
    (r"with indicator\s*: numeric (.*) binary (.*) categorical (.*)", "con indicador: numéricas {0} binarias {1} categóricas {2}"),
    (r"without indicator\s*: numeric (.*) binary (.*) categorical (.*)", "sin indicador: numéricas {0} binarias {1} categóricas {2}"),
    (r"(main|no_admin_vars|plus_era)\s*: numeric (.*) binary (.*) categorical (.*)", "{0}: numéricas {1} binarias {2} categóricas {3}"),
    (r"Population of `(\S+)`: (\S+) admissions, (\S+) events \(main: (\S+) admissions, (\S+) events\)",
     "Población de `{0}`: {1} admisiones, {2} eventos (main: {3} admisiones, {4} eventos)"),
    (r"not measured:\s+(\S+) admissions, (\S+) events \((\S+)\)", "no medida: {0} admisiones, {1} eventos ({2})"),
    (r"Admissions that are SMM only because of non-acute codes: (\S+) \(expected (\S+) from query (\S+)\)\s+\[(\w+)\]",
     "Admisiones con SMM solo por códigos no agudos: {0} (esperadas {1} según la consulta {2})  [{3}]"),
    (r"Laboratory variables added: (.*)", "Variables de laboratorio agregadas: {0}"),
    (r"Rule and reduced set: (\S+) \(fixed before this run\)", "Regla y conjunto reducido: {0} (fijados antes de esta corrida)"),
    (r"(cut\d+): counts vs Q-T4 (\(.*\)) expected (\(.*\))\s+\[(\w+)\]", "{0}: conteos frente a Q-T4 {1}, esperados {2}  [{3}]"),
    (r"PREDICTORS AND OUTCOME BY PERIOD, cut (\S+) \(development vs test as analysed in (\S+)\)",
     "PREDICTORES Y DESENLACE POR PERÍODO, corte {0} (desarrollo frente a prueba como se analizó en {1})"),
    (r"(scikit-learn|xgboost|numpy|pandas|imbalanced-learn|scipy)\s+expected (\S+)\s+installed (\S+)\s+\[(\w+)\]",
     "{0}  esperada {1}  instalada {2}  [{3}]"),
]

# Stage S1 section of notebook 01
ES.update({
    "S1 · Configuration of this repository": "E1 · Configuración de este repositorio",
    "item": "ítem", "status": "estado", "fixed": "fijo", "rule": "regla", "info": "información",
    "data source": "fuente de datos", "database": "base de datos", "data use": "uso de los datos",
    "publication rule": "regla de publicación", "random seed": "semilla aleatoria", "reference counts": "conteos de referencia",
    "NOT INSTALLED": "NO INSTALADO", "INSTALL (requirements.txt)": "INSTALAR (requirements.txt)",
    "NO CONNECTION: check .env and that PostgreSQL is running": "SIN CONEXIÓN: revisar .env y que PostgreSQL esté activo",
    "MIMIC-IV v3.1 (PhysioNet), Beth Israel Deaconess Medical Center, 2008-2022; dates shifted per patient":
        "MIMIC-IV v3.1 (PhysioNet), Beth Israel Deaconess Medical Center, 2008-2022; fechas desplazadas por paciente",
    "local PostgreSQL copy of MIMIC-IV (schema mimiciv); credentials in .env (not versioned)":
        "copia local de MIMIC-IV en PostgreSQL (esquema mimiciv); credenciales en .env (no versionado)",
    "PhysioNet Credentialed Health Data Use Agreement and CITI training: research only; no re-identification; data not shared or redistributed":
        "Acuerdo de uso de datos acreditados de PhysioNet y curso CITI: solo investigación; sin reidentificación; los datos no se comparten ni se redistribuyen",
    "only aggregate outputs (data/outputs_*.txt); cells below 10 suppressed; no subject_id, hadm_id or stay_id published":
        "solo salidas agregadas (data/outputs_*.txt); celdas con menos de 10 suprimidas; no se publican subject_id, hadm_id ni stay_id",
    "20260101 (notebooks 03 to 10); notebook 02 replicates the first-version splits with seed 42":
        "20260101 (notebooks 03 a 10); el notebook 02 replica las particiones de la primera versión con la semilla 42",
    "frozen at the count audit (19,383 eligible deliveries, 445 with SMM) and reproduced by gate G1 in notebooks 03 to 10":
        "fijados en la auditoría de conteos (19.383 partos elegibles, 445 con SMM) y reproducidos por la puerta P1 en los notebooks 03 a 10",
})

# Maternal death (M1) section of notebook 01 and the G1 tables of notebooks 03 to 10
ES.update({
    "count": "conteo", "loaded": "cargado", "expected": "esperado", "result": "resultado",
    "reproduced": "reproducido", "DIFFERS": "DIFIERE",
    "rung": "peldaño", "definition": "definición", "where": "dónde",
    "eligible_deliveries": "partos elegibles", "smm": "SMM", "deaths": "muertes",
    "deaths_eligible_obstetric": "muertes en obstétricas elegibles", "deaths_eligible_deliveries": "muertes en partos elegibles",
    "S3 · Outcome ladder of the outcome card": "E3 · Escalera de desenlaces de la ficha del desenlace",
    "S4 · G1 — maternal death (M1): reference counts": "E4 · P1 — muerte materna (M1): conteos de referencia",
    "1 (ideal)": "1 (ideal)", "return R2": "retorno R2",
    "maternal death (M1)": "muerte materna (M1)", "severe maternal morbidity (M2)": "morbilidad materna severa (M2)",
    "escalation of care after 24 h": "escalamiento de la atención después de 24 h",
    "death in the same admission": "muerte en la misma admisión",
    "CDC indicators in the same admission (transfusion excluded)": "indicadores de los CDC en la misma admisión (sin transfusión)",
    "ICU admission, invasive ventilation, an SMM procedure or death after T": "ingreso a UCI, ventilación invasiva, un procedimiento de SMM o muerte después de T",
    "S3 and S4 in this notebook; gate G3 in notebook 03": "E3 y E4 en este notebook; puerta P3 en el notebook 03",
    "return R1; notebooks 03 to 10": "retorno R1; notebooks 03 a 10",
    "notebook 07": "notebook 07",
})

# Gate decision tables added to notebooks 03 to 10 (G1) and 03 (G3)
ES.update({
    "Gate G1: reference counts": "Puerta P1: conteos de referencia", "Gate G1 decision": "Decisión de la puerta P1",
    "G1 decision": "decisión P1", "decision": "decisión",
    "passes: continue to the analyses": "pasa: se sigue con los análisis",
    "does NOT pass: review the tables of sql/ before fitting any model": "NO pasa: revisar las tablas de sql/ antes de ajustar cualquier modelo",
    "Gate G3 decision, SMM model": "Decisión de la puerta P3, modelo de SMM",
    "candidate parameters P": "parámetros candidatos P", "events available": "eventos disponibles",
    "admissions available": "admisiones disponibles", "G3 decision": "decisión P3",
    "passes: the SMM model is developed and goes to gate G4": "pasa: el modelo de SMM se desarrolla y va a la puerta P4",
    "does NOT pass: reduce the parameters or take return R1": "NO pasa: reducir los parámetros o tomar el retorno R1",
    "Gate G3 decision, maternal death (model A)": "Decisión de la puerta P3, muerte materna (modelo A)",
    "deaths available": "muertes disponibles",
    "deaths required (assumed R2 = 50% of its maximum)": "muertes requeridas (R2 supuesto = 50% de su máximo)",
    "does NOT pass: maternal death is reported as feasibility; return R1 to SMM":
        "NO pasa: la muerte materna se reporta como factibilidad; retorno R1 a la SMM",
    "passes": "pasa",
})

# Notebook summaries
ES.update({
    "Notebook summary": "Resumen del notebook", "Notebook summary: gate G2": "Resumen del notebook: puerta P2",
    "maternal deaths among eligible deliveries (M1)": "muertes maternas entre los partos elegibles (M1)",
    "gate G1, maternal death counts": "puerta P1, conteos de muerte materna",
    "next step for M1": "siguiente paso para M1", "gate G3 in notebook 03": "puerta P3 en el notebook 03",
    "SMM admissions among eligible deliveries (M2)": "admisiones con SMM entre los partos elegibles (M2)",
    "SMM with a procedure certainly before T (category A)": "SMM con un procedimiento con certeza antes de T (categoría A)",
    "SMM that cannot be ordered (category B)": "SMM que no se puede ordenar en el tiempo (categoría B)",
    "SMM placed only after T (category C)": "SMM ubicada solo después de T (categoría C)",
    "SMM on diagnosis codes only, no time (category D)": "SMM solo por códigos de diagnóstico, sin hora (categoría D)",
    "gate G1, consistency checks": "puerta P1, verificaciones de consistencia",
    "consequence for the framework": "consecuencia para el framework",
    "part of the SMM is already present at T: landmark population and criterion C1 (notebook 07)":
        "parte de la SMM ya está presente en T: población landmark y criterio C1 (notebook 07)",
    "does NOT pass": "NO pasa",
    "Model B (SMM): test patients also in train, hold-out": "Modelo B (SMM): pacientes de prueba también en entrenamiento, reserva",
    "Model B (SMM): positive test admissions whose patient is in train, hold-out":
        "Modelo B (SMM): admisiones positivas de prueba con la paciente en entrenamiento, reserva",
    "Model A (death): positive test admissions whose patient is in train, hold-out":
        "Modelo A (muerte): admisiones positivas de prueba con la paciente en entrenamiento, reserva",
    "gate G2 with admission-level splits": "puerta P2 con particiones por admisión",
    "does NOT pass: the same patient is on both sides": "NO pasa: la misma paciente queda a ambos lados",
    "every split of notebooks 03 to 10 is grouped by patient (StratifiedGroupKFold)":
        "todas las particiones de los notebooks 03 a 10 se agrupan por paciente (StratifiedGroupKFold)",
    "gate G3, maternal death (M1)": "puerta P3, muerte materna (M1)",
    "does NOT pass: return R1 to SMM": "NO pasa: retorno R1 a la SMM",
    "eligible deliveries / SMM events": "partos elegibles / eventos de SMM",
    "gate G3, SMM (M2)": "puerta P3, SMM (M2)",
    "AUROC, XGBoost (95% CI)": "AUROC, XGBoost (IC 95%)", "AUROC, stacked ensemble (95% CI)": "AUROC, ensamble apilado (IC 95%)",
    "AUROC, logistic regression (95% CI)": "AUROC, regresión logística (IC 95%)", "AUPRC, XGBoost (95% CI)": "AUPRC, XGBoost (IC 95%)",
    "calibration slope, XGBoost (95% CI)": "pendiente de calibración, XGBoost (IC 95%)",
    "observed/expected, XGBoost (95% CI)": "observados/esperados, XGBoost (IC 95%)",
    "sensitivity analyses, AUROC XGBoost (min-max)": "análisis de sensibilidad, AUROC XGBoost (mín-máx)",
    "observed/expected of the raw risks, XGBoost with SMOTENC": "observados/esperados de los riesgos crudos, XGBoost con SMOTENC",
    "observed/expected of the raw risks, XGBoost without resampling": "observados/esperados de los riesgos crudos, XGBoost sin remuestreo",
    "AUROC XGBoost with the indicator (95% CI)": "AUROC XGBoost con el indicador (IC 95%)",
    "AUROC XGBoost without the indicator (95% CI)": "AUROC XGBoost sin el indicador (IC 95%)",
    "AUROC difference, XGBoost (without - with)": "diferencia de AUROC, XGBoost (sin - con)",
    "AUROC difference, logistic regression (without - with)": "diferencia de AUROC, regresión logística (sin - con)",
    "admissions / events after the exclusion": "admisiones / eventos después de la exclusión",
    "AUROC XGBoost, main": "AUROC XGBoost, main",
    "AUROC XGBoost, without the administrative variables": "AUROC XGBoost, sin las variables administrativas",
    "AUROC XGBoost, with the era as a predictor": "AUROC XGBoost, con la época como predictor",
    "criterion C4 used in the classification": "criterio C4 usado en la clasificación",
    "C1 landmark": "C1 landmark", "C2 documented incident": "C2 incidente documentada", "C2 strict incident": "C2 incidente estricta",
    "C3 laboratory AKI, incident": "C3 lesión renal aguda por laboratorio, incidente",
    "R4 extended laboratories": "R4 laboratorios ampliados", "R2 escalation of care": "R2 escalamiento de la atención",
    "R2 escalation, reduced set (G3)": "R2 escalamiento, conjunto reducido (P3)",
    "classification at gate G4": "clasificación en la puerta P4",
    "restated on the fitted models in notebook 10": "se establece sobre los modelos ajustados en el notebook 10",
    "class of the SMM model (M2)": "clase del modelo de SMM (M2)",
    "early identifier: surveillance and prioritization of review, not prevention":
        "identificador temprano: vigilancia y priorización de la revisión, no prevención",
    "decision record": "registro de la decisión",
})
RULES += [
    (r"AUROC (XGB|Stack|LR|RF|ET), (.+)", "AUROC {0}, {1}"),
    (r"AUROC XGBoost, (.+) \(95% CI\)", "AUROC XGBoost, {0} (IC 95%)"),
    (r"(cut\w+): AUROC XGBoost \(95% CI\)", "{0}: AUROC XGBoost (IC 95%)"),
    (r"(cut\w+): calibration slope XGBoost \(95% CI\)", "{0}: pendiente de calibración XGBoost (IC 95%)"),
    (r"(cut\w+): observed/expected XGBoost \(95% CI\)", "{0}: observados/esperados XGBoost (IC 95%)"),
    (r"C1, (\S+): AUROC XGBoost full -> landmark", "C1, {0}: AUROC XGBoost completo -> landmark"),
    (r"(\S+) -> (\S+) \(drop (\S+)\)", "{0} -> {1} (caída {2})"),
    (r"(\S+) \((\d+) analyses\)", "{0} ({1} análisis)"),
]

# In Spanish the gates are P1-P4 and the stages E1-E11 (in English G1-G4 and S1-S11)
import re as _re
_fix = lambda v: _re.sub(r"\bS(1[01]|[1-9])\b", r"E\1", _re.sub(r"\bG([1-4])\b", r"P\1", v))
ES = {k: _fix(v) for k, v in ES.items()}
RULES = [(p, _fix(r)) for p, r in RULES]

# Keys and translations are normalized as the lookup does: every number becomes "#" (literal numbers of a key, such as
# "5-fold", then match any number, and the numbers of the English line are put back in the same order).
_NUM = _re.compile(r"(?<![A-Za-z_])-?\d[\d,]*(?:\.\d+)?")
def _norm(k, v):
    nk = _NUM.sub("#", k)
    if "#" not in nk:                 # no number in the key: the translation is used as written
        return k, v
    # a comma right after a number belongs to the number in the English line ("3, binary"), so it is not repeated
    return nk, _NUM.sub("#", v).replace("#,", "#")
ES = dict(_norm(k, v) for k, v in ES.items())

# Notebook 11 (ROC curves and classification report of the SMM model) and libraries/figures.py
ES.update(dict(_norm(k, v) for k, v in {
    "Check: AUROC of each learner (mean of the repeats) against the article": "Verificación: AUROC de cada algoritmo (promedio de las repeticiones) frente al artículo",
    "AUROC article": "AUROC del artículo", "AUROC this run": "AUROC de esta corrida",
    "QUICK = True: the check is not meaningful; never use these figures": "QUICK = True: la verificación no tiene sentido; nunca usar estas figuras",
    "SMM, main analysis: patient-grouped cross-validation (out-of-fold, repeat 1)": "SMM, análisis principal: validación cruzada agrupada por paciente (fuera de muestra, repetición 1)",
    "Final model (XGBoost), top 10% of risk": "Modelo final (XGBoost), 10% de mayor riesgo",
    "Threshold metrics at the top 10% of risk (out-of-fold, repeat 1)": "Métricas en el corte del 10% de mayor riesgo (fuera de muestra, repetición 1)",
    "1 - specificity (false positive rate)": "1 - especificidad (tasa de falsos positivos)",
    "Sensitivity (true positive rate)": "Sensibilidad (tasa de verdaderos positivos)",
    "precision": "precisión", "recall": "sensibilidad (recall)", "f1-score": "F1", "accuracy": "exactitud", "macro avg": "promedio macro",
    "Metrics": "Métricas", "Classes": "Clases", "risk cut": "corte de riesgo", "Predicted label": "Clase predicha",
    "True label": "Clase real", "Confusion matrix": "Matriz de confusión",
    "TP": "VP", "FP": "FP", "FN": "FN", "TN": "VN", "F1": "F1", "sensitivity": "sensibilidad", "specificity": "especificidad",
    "PPV": "VPP", "NPV": "VPN",
    "admissions / SMM events": "admisiones / eventos de SMM", "check against the article": "verificación frente al artículo",
    "AUROC by learner (mean of the repeats)": "AUROC por algoritmo (promedio de las repeticiones)",
    "final model": "modelo final", "XGBoost (primary learner)": "XGBoost (algoritmo principal)",
    "XGBoost at the top 10% of risk: sensitivity / PPV": "XGBoost con el 10% de mayor riesgo: sensibilidad / VPP",
    "figures": "figuras",
}.items()))
