# Entrada del libro de decisiones — regla nueva del framework «reducción en P3» (09/11/2026)

Versión en inglés: [`decision_G3_reduction_2026-11-09.md`](decision_G3_reduction_2026-11-09.md).

> Nota de nomenclatura (11/11/2026): en el artículo y el código en inglés, la puerta P3 es la puerta de tamaño de muestra G3, P4 la puerta de clasificación G4 y la etapa E7 es S7; esta regla se llama *sample-size reduction* (reducción por tamaño de muestra). La entrada conserva los códigos usados cuando se registró. Archivo renombrado el 13/11/2026 desde `decision_P3_reduction_2026-11-09.md`; la regla se registró por primera vez el 09/11/2026 (commit c761e64), antes de correr el análisis.

**Etapa / puerta:** P3 (tamaño de muestra), después de la segunda clasificación en P4. **Tipo de razón:** metodológica.
**Validada por:** Emmanuel Gutiérrez Jiménez (por confirmar con el director de la tesis).

## Contexto
El retorno R2 (escalamiento de la atención después de T, 101 eventos en 19.268 partos) cumplió todos los
criterios aplicables de la puerta P4 (C1, C2, C4; C3 no aplica), pero no pasó la puerta P3: con 32 parámetros
candidatos y el R² de Cox-Snell observado de 0,0077, el criterio de encogimiento de Riley et al. exigía 37.098
admisiones; los datos soportan como máximo 16 parámetros. Los dos retornos permitidos (R4, R2) ya estaban usados.

## Regla nueva (agregada al framework en esta fecha, después de la segunda clasificación)
Cuando un modelo cumple todos los criterios aplicables de la puerta P4 pero no pasa la puerta P3, se permite una
**reducción en P3** antes de reportar: el modelo se reajusta una sola vez con un conjunto reducido de predictores
cuyo número de parámetros no supera el máximo que soportan los datos, elegido con reglas fijadas en la ficha del
desenlace y **nunca** por la asociación de un predictor con el desenlace. El modelo reducido debe pasar entonces
P3 y clasificarse de nuevo en P4 con los mismos umbrales. Una reducción en P3 no es un retorno y no cuenta dentro
del límite de dos. Alternativa a la reducción: ampliar los datos (más años, otro centro u otra base de datos).

## Conjunto reducido de predictores para el escalamiento (fijado antes de cualquier corrida)
- Numéricos: edad al ingreso, hemoglobina, creatinina (el mismo preprocesamiento del modelo principal).
- Binarios: creatinina faltante; seguro Medicaid (frente a otro); idioma inglés (frente a otro o faltante);
  tipo de admisión URGENT (frente a otro); lugar de admisión PHYSICIAN REFERRAL (frente a otro).
- Categórico: raza y etnia en cinco grupos — blanca, negra, hispana o latina, asiática, otra o desconocida
  (prefijo del valor registrado: WHITE*, BLACK*, HISPANIC* o SOUTH AMERICAN, ASIAN*, todo lo demás).
- Parámetros esperados: 3 + 5 + 5 = 13 (la corrida se detiene si el conteo supera 16).

## Análisis y criterios fijados de antemano (umbrales de la Tabla 1, fijados el 04/11/2026)
Una sola corrida, XGBoost como modelo principal, la misma validación cruzada anidada agrupada por paciente,
*bootstrap* B = 300.
- **P3:** criterios de Riley et al. con el P reducido y el R² de Cox-Snell observado de la regresión logística
  reducida con validación cruzada; pasa si el n requerido es como máximo 19.268.
- **C2:** AUROC ≥ 0,75 con límite inferior del IC 95% ≥ 0,70 (el escalamiento es el desenlace fechado después de T).
- **C1:** población *landmark* (se retira la SMM presente o indeterminada en T): el AUROC cae 0,05 o menos y se
  conservan al menos dos tercios de la ganancia de AUPRC sobre la prevalencia.
- **C3:** no aplica (el desenlace no depende de exámenes de laboratorio).
- **C4:** desarrollo con certeza antes de 2017 y una sola prueba desde 2017: AUROC temporal ≥ 0,70 y el intervalo
  de 95% de la pendiente de calibración incluye 1. AUROC temporal < 0,65 → ninguno.
- **Clasificación:** pasa P3, C1, C2 y C4 → candidato a predictor (pendiente de validación externa); si no, el
  resultado del escalamiento queda como señal exploratoria. El resultado se reporta sea cual sea, indicando que la
  regla se agregó después de la segunda clasificación.

Código: notebooks/07_landmark_incident_smm.ipynb sección 15; notebooks/09_temporal_validation_smm.ipynb sección 10.
Salidas: data/outputs_escalation_reduced_summary.txt; data/outputs_cut2017_escalation_reduced.txt.

## Resultado (registrado después de la única corrida, 09/11/2026)
- Conjunto reducido: 13 parámetros. **P3: pasa** (R² de Cox-Snell observado 0,0069; se requieren 16.962
  admisiones y 89 eventos; hay 19.268 y 101).
- **C1: cumple** (AUROC *landmark* de XGBoost 0,754 frente a 0,749; se conserva la ganancia de AUPRC).
- **C2: no cumple** con el modelo principal (AUROC de XGBoost 0,749, 0,692–0,798); lo cumplen la regresión
  logística (0,764, 0,707–0,812) y el ensamble apilado (0,763, 0,703–0,811). Los algoritmos no difirieron de forma
  significativa (XGBoost − RL −0,016, −0,041 a 0,009); el ensamble no cumplió la regla de adopción (+0,015, −0,004 a 0,035).
- **C4: no cumple** con XGBoost (AUROC temporal 0,699, 0,620–0,778; pendiente 0,88, 0,51–1,25; O/E 1,55); lo
  cumplen la regresión logística (0,712, pendiente 0,95) y el ensamble (0,740, pendiente 1,09).
- **Clasificación:** señal exploratoria de predicción (en el límite), limitada ahora por la precisión de las
  estimaciones y no por el tamaño de muestra. Se reporta como se obtuvo; el modelo principal no se cambió.
Salidas: data/outputs_escalation_reduced*.txt, data/outputs_escalation_landmark_reduced.txt,
data/outputs_cut2017_escalation_reduced.txt.
