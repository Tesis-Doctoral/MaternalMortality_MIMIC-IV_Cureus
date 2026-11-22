# ¿Predictor o identificador temprano? Morbilidad materna grave en MIMIC-IV

> **Framework.** Este repositorio aplica el framework por etapas de la tesis para modelos de predicción clínica. El framework (etapas, puertas, criterios y literatura) y el catálogo de modelos con su estado están en [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction).

Código, SQL y salidas agregadas del artículo **"Predictor or Early Identifier? A Staged Framework for Clinical Prediction Models Applied to Severe Maternal Morbidity in MIMIC-IV"** (Cureus, 2026).

Autores: Emmanuel Gutiérrez Jiménez y José Duván Márquez Díaz — Departamento de Ingeniería de Sistemas, Universidad del Norte, Barranquilla, Colombia.

[English version](README.md)

> **Este repositorio no incluye datos a nivel de paciente.** MIMIC-IV requiere acceso acreditado (ver [Acceso a los datos](#acceso-a-los-datos)). Los archivos SQL solo contienen definiciones de esquema, lógica de cohorte y listas de códigos; las salidas de los notebooks en `data/` son conteos y métricas agregadas, con celdas menores de 10 suprimidas. No se publican valores de `subject_id`, `hadm_id` ni `stay_id`.

> **Estado (22/11/2026).** Los modelos M1 y M2 del catálogo del framework están completos. El notebook 10 evalúa los criterios de la puerta P4 sobre los modelos ajustados una sola vez en toda su población y aplica la puerta P3 a todo conjunto en el que se ajusta un modelo (decisión del 22/11/2026, [`docs/decision_G4_fitted_models_2026-11-22.md`](docs/decision_G4_fitted_models_2026-11-22.md)); resultados registrados en el libro de decisiones.

## Alcance

| Id en el catálogo | Modelo | Desenlace | Punto de predicción | Resultado |
|---|---|---|---|---|
| M1 | Muerte materna | Muerte en la hospitalización del parto | Ingreso + 24 h | No pasa P3 (3 eventos): solo viabilidad; retorno R1 a la SMM |
| M2 | Morbilidad materna grave (SMM) | Al menos uno de los 20 indicadores de los CDC | Ingreso + 24 h | **Identificador temprano** (falla C1, C3 y C4; cumple C2) |
| M2 · R4 | SMM con laboratorios ampliados | como M2 | como M2 | Identificador temprano: la ganancia venía de qué exámenes se pidieron |
| M2 · R2 | Escalamiento de la atención después de T | Ingreso a UCI, ventilación mecánica, indicador de SMM por procedimiento o muerte después de T | como M2 | Cumple C1 y C2; C4 no evaluable (46 eventos de desarrollo); no pasa P3 (101 eventos, 32 parámetros) |
| M2 · R2 reducido | como R2, 13 parámetros | como R2 | como M2 | Pasa P3; **señal exploratoria de predicción**: justo por debajo de C2 (0,749), C4 no evaluable |

Ficha del desenlace: [`docs/outcome_card_smm_es.md`](docs/outcome_card_smm_es.md). Libro de decisiones: [`docs/`](docs/) (un archivo por decisión, con fecha).

## Datos y población

MIMIC-IV v3.1 (Beth Israel Deaconess Medical Center, 2008–2022; fechas desplazadas por paciente). Hospitalizaciones de parto que seguían en curso 24 horas después del ingreso: **19.383 admisiones de 13.710 pacientes, 445 con SMM (2,30%)**. Solo el 25,6% de los eventos de SMM pudo fecharse después del punto de predicción (T = ingreso + 24 h).

| | |
|---|---|
| Predictores | Edad, cinco variables de registro, hemoglobina y creatinina hasta T, indicador de creatinina faltante (32 parámetros) |
| Algoritmos | Regresión logística L2 (referencia), bosque aleatorio, árboles extra, XGBoost (principal) y un ensamble apilado |
| Validación | Validación cruzada anidada agrupada por paciente (5 × 3 particiones, 3 repeticiones); recalibración dentro del entrenamiento; *bootstrap* de pacientes |
| Validación temporal | Desarrollo con admisiones con certeza anteriores a 2017, prueba única desde 2017 |

## Orden de ejecución

**SQL** (PostgreSQL 13; el encabezado de cada script indica sus requisitos):

| Orden | Carpeta | Crea | Etapa del framework |
|---|---|---|---|
| 1 | `sql/01_load_mimic_iv_schema/` | Esquema local de MIMIC-IV (ver su README) | E1 |
| 2 | `sql/02_cohort_mortality/` (`maternal_cohort_expanded.sql`, luego el resto) | Universo obstétrico y objetos base | E2 |
| 3 | `sql/03_cohort_smm/` (`smm_cohort.sql`, `smm_dataset.sql`) | Objetos base de la SMM | E2, E3 |
| 4 | `sql/04_labels/` (`01` a `06`, incluido `03b`) | Listas de códigos CDC, marca de parto, etiquetas, horizontes de muerte | E2, E3, E4 |
| 5 | `sql/05_predictors/` (`01`, `02`) | Predictores de la ventana de 24 horas y diccionario final | E6, E7 |
| 6 | `sql/06_audit_counts/` (opcional) | Conteos del flujo de la cohorte y tablas cruzadas (solo tablas temporales) | E4, P1 |
| 7 | `sql/07_timing_audit/` (`01` a `04`) | Momento de la evidencia de SMM, auditoría del fenotipo, etiqueta de escalamiento | E3, E4, R2 |

**Notebooks** (se ejecutan de principio a fin; cada sección nombra la etapa, puerta o criterio que atiende):

| Orden | Notebook | Crea (`data/`) | Etapa del framework |
|---|---|---|---|
| 1 | `01_patient_overlap.ipynb` | Solo conteos en consola | E5 |
| 2 | `02_grouped_validation_smm.ipynb` | `outputs_main.txt`, `outputs_modelA.txt` (muerte materna), sensibilidades `first_admission`, `any_obstetric`, `icd10_only`, `label_ge2`, `no_icu_24h`, `labs_extended`, `icu_vars` | E8, P3, R1, E9 |
| 3 | `03_resampling_comparison_smm.ipynb` | `outputs_resampling.txt` | E8 |
| 4 | `04_creatinine_indicator_sensitivity_smm.ipynb` | `outputs_no_indicator.txt` | E7, E9 |
| 5 | `05_era_temporal_validation_smm.ipynb` | `outputs_era_temporal.txt` | E9 |
| 6 | `06_smm_renal_only_sensitivity.ipynb` | `outputs_excl_renal_only.txt` | E3, E9 |
| 7 | `07_smm_timing_vs_prediction_time.ipynb` | `outputs_smm_timing.txt` | E3, E4 |
| 8 | `08_landmark_incident_smm.ipynb` | `outputs_landmark*.txt`, `outputs_incident_*.txt`, `outputs_aki_lab_incident*.txt`, `outputs_c3_labs_summary.txt`, `outputs_excl_nonacute.txt`, `outputs_richer_predictors_summary.txt`, `outputs_escalation*.txt`, `outputs_g3_escalation.txt`, `outputs_main_norace.txt`, `outputs_race_subgroups.txt` | E9, P4 (C1–C3), R4, R2, P3, reducción en P3, E10 |
| 9 | `09_temporal_validation_smm.ipynb` | `outputs_cut2017*.txt`, `outputs_cut2015.txt`, `outputs_temporal_summary.txt`, `outputs_temporal_predictors.txt` | E9, P4 (C4) |
| 10 | `10_g4_criteria_fitted_models_es.ipynb` (inglés: sin `_es`) | `outputs_g4_fitted_models.txt` (C1 y C2 con intervalos de 95%, componentes del escalamiento), `outputs_g3_fitted_subsets.txt` | P4 (C1, C2) sobre los modelos ajustados, P3 para todo conjunto ajustado |
| — | `scripts/g3_planning_assumed_r2.py` (no requiere la base de datos) | `outputs_g3_planning.txt` | P3, paso de planeación con un R² supuesto |

Los notebooks 01 a 09 están en inglés; el notebook 10 tiene versión en inglés y en español con el mismo código. Cada script SQL tiene una versión en español con el sufijo `_es` (mismas sentencias, comentarios traducidos).

## Mapa del framework

> **Nomenclatura.** Etapas E1 a E11 y puertas P1 a P4 (definición, fuga, tamaño de muestra y clasificación). Los archivos en inglés usan S1 a S11 y G1 a G4 para las mismas etapas y puertas.

| Etapa, puerta o retorno | Scripts y notebooks |
|---|---|
| E1 Gobierno y configuración | `sql/01_load_mimic_iv_schema/`; sección 1 de cada notebook |
| E2 Universo y población | `sql/02_cohort_mortality/maternal_cohort_expanded.sql`; `sql/04_labels/02_delivery_flag.sql`, `04_cohort_obstetric_flags.sql` |
| E3 Definición del desenlace | `sql/04_labels/01_smm_codes_official.sql`, `03_labels_same_admission.sql`; `sql/07_timing_audit/01_timing_flags_v3.sql`, `02_phenotype_audit_v3.sql`; notebook 07 |
| E4 Auditoría de conteos · P1 | `sql/06_audit_counts/`; `sql/04_labels/03b_reconcile_old_labels.sql`, `06_smm_death_overlap.sql`; verificación `EXPECTED` en cada notebook |
| E5 Unidad de análisis y solapamiento | notebook 01 |
| E6 Punto de predicción y ventana | `sql/05_predictors/01_predictors_24h.sql`; sección 3 de los notebooks 02 a 08 |
| P2 Puerta de fuga | aserciones en las funciones de validación cruzada (ningún paciente en ambos lados) |
| E7 Predictores | `sql/05_predictors/`; notebooks 04 y 05 |
| P3 Puerta de tamaño de muestra | planeación: `scripts/g3_planning_assumed_r2.py`; reevaluación: notebook 02 (modelo principal y muerte materna), notebook 08 sección 14 (escalamiento), notebook 10 sección 5 (todo conjunto ajustado) |
| R1 | muerte materna a SMM: `sql/04_labels/05_death_horizon_counts.sql`; notebook 02 |
| E8 Modelado, validación y métricas | notebook 02 (modelo principal); notebook 03 (desbalance de clases) |
| E9 Sensibilidad y robustez | notebooks 05, 06, 08 y 09 |
| P4 Puerta de clasificación | notebook 08 (C1, C2, C3), notebook 09 (C4), notebook 10 (C1 y C2 sobre los modelos ajustados) |
| R2 | `sql/07_timing_audit/03_escalation_counts.sql`, `04_escalation_label.sql`; notebook 08 secciones 11 y 14; notebook 09 |
| R4 | notebook 08 secciones 10 y 13; notebook 09 `cut2017_landmark_labs` |
| Reducción en P3 | notebook 08 secciones 15 y 16; notebook 09 sección 10; [`docs/decision_G3_reduction_2026-11-09.md`](docs/decision_G3_reduction_2026-11-09.md) |
| E10 De la clasificación a la acción | notebook 08 sección 12 (raza y etnia, subgrupos) |
| E11 Reporte | `data/outputs_*.txt`; `scripts/fig_cohort_funnel.py`, `scripts/fig_framework.py` |

Los scripts de la primera versión del análisis (`sql/02_cohort_mortality/` salvo `maternal_cohort_expanded.sql`, y `sql/03_cohort_smm/`) se conservan por trazabilidad; los grupos de diagnósticos de egreso que construyen se retiraron en la puerta P2.

## Libro de decisiones

| Fecha | Decisión | Archivo |
|---|---|---|
| 09/11/2026 | Regla nueva: reducción en P3 después de la segunda clasificación, con el conjunto reducido de predictores fijado antes de correrla | [`docs/decision_G3_reduction_2026-11-09.md`](docs/decision_G3_reduction_2026-11-09.md) |
| 11/11/2026 | Modelo principal según eventos por parámetro | [`docs/decision_primary_learner_EPP_2026-11-11.md`](docs/decision_primary_learner_EPP_2026-11-11.md) |
| 22/11/2026 | Criterios de P4 sobre los modelos ajustados; puerta P3 para todo conjunto en el que se ajusta un modelo; P3 en dos pasos (planeación y reevaluación); banda de tolerancia de C4 como sensibilidad; intervalos de 95% para toda cantidad de decisión | [`docs/decision_G4_fitted_models_2026-11-22_es.md`](docs/decision_G4_fitted_models_2026-11-22_es.md) |

## Instalación y ejecución

1. **Obtenga acceso acreditado a MIMIC-IV** (ver [Acceso a los datos](#acceso-a-los-datos)) y descargue la exportación CSV (v3.1).
2. **Cargue el esquema localmente** siguiendo `sql/01_load_mimic_iv_schema/README.md`. `docker-compose.yml` levanta PostgreSQL 13 y Jupyter; defina `MIMICIV_DATA_DIR` y `MIMICIV_CSV_DIR` en su `.env`.
3. **Construya las tablas** con los scripts SQL en el orden anterior.
4. **Defina sus credenciales:** copie `.env.example` a `.env` en la raíz del proyecto y escriba la contraseña de su base de datos. `.env` está excluido de git.
5. **Cree un entorno e instale las dependencias:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
6. **Ejecute los notebooks** en el orden anterior (Restart & Run All). La validación anidada con *bootstrap* es pesada (unos 10 a 15 minutos por validación cruzada).

Los archivos que se escriben en `data/` distintos de `outputs_*.txt` están cerca del nivel de paciente y están excluidos por `.gitignore`. No los suba al repositorio.

## Notas metodológicas

- La etiqueta de SMM es una clasificación de la admisión hecha con códigos CIE, que no tienen fecha para los diagnósticos y solo tienen fecha de calendario para los procedimientos. Las clases temporales del notebook 07 y de `sql/07_timing_audit/` ubican cada evento respecto a T cuando la evidencia lo permite; el 38,4% de los eventos no puede fecharse.
- Todas las particiones se agrupan por paciente. La imputación, el escalado, el ajuste de hiperparámetros, el ensamble y la recalibración se ajustan dentro de la parte de entrenamiento de cada partición.
- Un solo centro, sin validación externa; la validación temporal usa pacientes posteriores del mismo hospital.
- El reporte sigue TRIPOD+AI.

## Acceso a los datos

Este repositorio **no** incluye datos a nivel de paciente. MIMIC-IV está disponible en [PhysioNet](https://physionet.org/content/mimiciv/) para investigadores que completen el curso CITI "Data or Specimens Only Research", firmen el PhysioNet Credentialed Health Data Use Agreement y obtengan el acceso.

Referencia: Johnson AEW, Bulgarelli L, Shen L, et al. MIMIC-IV, a freely accessible electronic health record dataset. Sci Data. 2023;10:1. https://doi.org/10.1038/s41597-022-01899-x

## Cita

Por favor cite el artículo. La referencia completa (volumen, DOI) se agregará después de la publicación.

## Licencia

Licencia MIT (ver `LICENSE`).

## Contacto

Emmanuel Gutiérrez Jiménez — emmanuelg@uninorte.edu.co
