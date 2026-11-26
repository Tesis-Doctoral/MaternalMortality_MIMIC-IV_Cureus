# Ficha del desenlace — muerte materna y morbilidad materna grave, MIMIC-IV

Ficha del desenlace según el framework por etapas ([StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction)). Modelos M1 y M2 del catálogo. Versión en inglés: [`outcome_card_smm.md`](outcome_card_smm.md). Las decisiones están fechadas en el libro de decisiones ([`./`](./)).

## 1. La pregunta

**A las 24 horas del ingreso para el parto, ¿el modelo predice una morbilidad materna que todavía no ha ocurrido o reconoce una morbilidad que ya está en curso?**

## 2. Identidad

| Campo | Valor |
|---|---|
| Escalera de desenlaces | Peldaño 1: muerte materna (M1). Peldaño 2: morbilidad materna grave, SMM (M2) |
| Fuente de datos | MIMIC-IV v3.1 (Beth Israel Deaconess Medical Center, 2008–2022), acceso acreditado por PhysioNet |
| Unidad y grupo | Hospitalización de parto; la paciente como unidad de agrupación (13.710 pacientes) |
| Población | Hospitalizaciones de parto que seguían en curso 24 horas después del ingreso: 19.383 |
| Punto de predicción (T) | Ingreso + 24 horas |
| Etiqueta principal | SMM: al menos uno de los 20 indicadores de los CDC (CIE-9-MC o CIE-10-MC/SCP) en la misma admisión: 445 eventos (2,30%) |
| Momento de los eventos | Presentes en T 150 (33,7%), indeterminados 10 (2,2%), incidentes documentados 114 (25,6%), sin fecha 171 (38,4%) |
| Etiquetas de sensibilidad | Dos o más indicadores; sin SMM solo renal; sin indicadores no agudos; falla renal por laboratorio después de T (C3) |

## 3. Puertas y resultados

Los criterios C1 y C2 se evalúan sobre el modelo ajustado una sola vez en toda su población (decisión del 22/11/2026). Valores de XGBoost con intervalos de 95% por *bootstrap* de pacientes.

| Puerta o criterio | Modelo principal (M2) | Indicadores | Decisión |
|---|---|---|---|
| P1 Definición | Pasa | Conteos de referencia reproducidos en cada notebook (`EXPECTED`) | — |
| P2 Fuga | Pasa | Sin grupos de diagnósticos de egreso; sin información posterior a T; ninguna paciente en ambos lados de una partición | — |
| P3 Tamaño de muestra | Pasa | Planeación (R² de Cox-Snell supuesto 0,030, 15% del máximo): se requerían 9.614 admisiones y 221 eventos. Reevaluación (R² observado fuera de muestra 0,0311): 9.112 y 209. Disponibles: 19.383 y 445. 32 parámetros (columnas después de la codificación *one-hot*, sin intercepto) | La muerte materna (M1, 3 eventos) no pasa: retorno R1 a la SMM |
| P4 C1 Eventos presentes | No cumple | AUROC 0,791 → 0,719 (0,686–0,750) en la población *landmark*; caída 0,072 (0,056–0,088); se conserva el 40% (30–51%) de la ganancia de AUPRC (se reporta; no decide C1) | — |
| P4 C2 Desenlace con tiempo | Cumple | SMM incidente documentada 0,765 (0,713–0,816); incidente estricta 0,784 (0,721–0,843) | — |
| P4 C3 Sesgo de detección | No cumple | Falla renal fechada con creatinina: 0,850 (0,822–0,872) en total, 0,628 (0,584–0,671) entre pacientes examinadas | — |
| P4 C4 Estabilidad | No cumple | AUROC temporal 0,747 (0,707–0,783); pendiente 0,83 (0,71–0,97); O/E 1,34 (1,15–1,52). El período de desarrollo pasa P3. Con la regla del framework 1.3 (AUROC temporal de 0,70 o más y pendiente entre 0,90 y 1,10): no cumple | — |
| **P4 Clasificación** | **Identificador temprano** | AUROC 0,791 (0,767–0,816); el 10% superior concentra el 51,4% de los eventos | Retornos R4 y R2 |

## 4. Retornos y reducción por tamaño de muestra

| Paso | Resultado | Decisión |
|---|---|---|
| R4 Laboratorios ampliados | AUROC 0,821; *landmark* 0,740, caída 0,081 (0,066–0,098), se conserva el 29% de la ganancia; C2 cumple (0,763; 0,776); C3 no cumple (0,861 → 0,643); C4 no cumple (temporal *landmark* 0,697, pendiente 0,73) | Sigue como identificador temprano: la ganancia venía de qué exámenes se pidieron |
| R2 Escalamiento de la atención después de T | 101 eventos en 19.268 partos; AUROC 0,763; *landmark* 0,765 (C1 cumple); C2 cumple; C4 **no evaluable** (46 eventos en el período de desarrollo; P3 exige 155). Componentes: ingreso a UCI 0,770 (90 eventos), ventilación mecánica 0,758 (38), indicador por procedimiento 0,702 (40), muerte menos de 10; 39 solo UCI, 10 solo procedimiento, 51 con dos o más | No pasa P3 (planeación 30.120 admisiones y 158 eventos; reevaluación 37.098 y 194) |
| Reducción en P3 (13 parámetros) | Pasa P3 (planeación 12.236 y 64; reevaluación 16.962 y 89); C1 cumple (*landmark* 0,752); XGBoost no cumple C2 (0,749, 0,692–0,798; la regresión logística, 0,764, y el ensamble, 0,763, sí lo cumplen); C4 **no evaluable** (P3 exige 71 eventos de desarrollo) | Señal exploratoria de predicción. Regla agregada después de la segunda clasificación, motivada por los resultados del escalamiento; conjunto reducido armado solo con la estructura y la frecuencia de los predictores ([`decision_G3_reduction_2026-11-09_es.md`](decision_G3_reduction_2026-11-09_es.md)) |

Los dos retornos permitidos (R4, R2) están usados. Paso de planeación de P3: `scripts/g3_planning_assumed_r2.py` → `data/outputs_g3_planning.txt`. Criterios sobre los modelos ajustados: notebook 10 ([`decision_G4_fitted_models_2026-11-22_es.md`](decision_G4_fitted_models_2026-11-22_es.md)).

## 5. Datos y condiciones de uso

Ningún dato a nivel de paciente sale de la base local. Los reportes de `data/` son agregados; se suprimen las celdas menores de 10. El uso está sujeto al PhysioNet Credentialed Health Data Use Agreement.
