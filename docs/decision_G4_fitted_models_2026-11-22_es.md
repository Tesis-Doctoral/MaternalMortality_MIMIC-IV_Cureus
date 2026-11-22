# Entrada del libro de decisiones — criterios de P4 sobre los modelos ajustados, puerta P3 para todo conjunto ajustado (22/11/2026)

Versión en inglés: [`decision_G4_fitted_models_2026-11-22.md`](decision_G4_fitted_models_2026-11-22.md).

**Etapa / puerta:** P4 (criterios C1, C2 y C4) y P3. **Tipo de razón:** metodológica (coherencia entre las puertas P3 y P4).
**Validada por:** Emmanuel Gutiérrez Jiménez (por confirmar con el director de la tesis). **Registrada antes** de correr el notebook 10.

## Contexto

El notebook 08 evaluó los criterios C1 (población *landmark*) y C2 (SMM incidente documentada y estricta) **volviendo a ajustar** el modelo completo, con sus 32 parámetros, dentro de cada subconjunto: 285, 114 y 83 eventos. Lo mismo ocurrió en los períodos de desarrollo de la validación temporal (criterio C4, notebook 09): 209 eventos para el modelo principal y 46 para el escalamiento de la atención. La puerta P3 se había aplicado solo a la población completa de cada desenlace, así que esos ajustes nunca se verificaron contra ella. Con 46 eventos, el período de desarrollo del escalamiento queda por debajo de lo que P3 exige para 32 parámetros (194 eventos) y para los 13 del modelo reducido (89 eventos).

## Regla (agregada al framework en esta fecha)

1. **Un criterio de la puerta P4 que pregunta cómo se comporta un modelo en una parte de su población se evalúa sobre el modelo ajustado una sola vez en toda su población.** Sus predicciones fuera de muestra se restringen al subconjunto; el modelo no se vuelve a ajustar allí. Aplica a C1 (población *landmark*) y C2 (desenlace fechado después del punto de predicción).
2. **Todo conjunto en el que se ajusta un modelo debe pasar la puerta P3.** Incluye el período de desarrollo de la validación temporal (C4). Un criterio cuyo ajuste necesitaría un conjunto que no pasa P3 se reporta como **no evaluable**, no como cumplido ni como no cumplido.
3. **Toda cantidad de decisión se reporta con su intervalo de 95%** (*bootstrap* de pacientes, pareado entre la población completa y el subconjunto cuando el criterio los compara).
4. Los umbrales de la Tabla 1 (fijados el 04/11/2026) no cambian.

## Análisis (una sola corrida)

Notebook `10_g4_criteria_fitted_models_es.ipynb`, con la misma semilla, particiones, repeticiones y grillas de los notebooks 02 y 08, *bootstrap* B = 1.000:

- Cuatro modelos, ajustados una vez cada uno: modelo principal (M2), retorno R4 (laboratorios ampliados), retorno R2 (escalamiento, 32 parámetros) y retorno R2 tras la reducción por tamaño de muestra (13 parámetros).
- C1 y C2 sobre sus predicciones fuera de muestra; para el escalamiento, además cada componente frente a las admisiones sin escalamiento y el solapamiento de los componentes.
- P3 para los períodos de desarrollo del notebook 09 y, como referencia, para las poblaciones incidentes, con el R² de Cox-Snell observado de la regresión logística con validación cruzada de cada modelo ajustado.

Salidas: `data/outputs_g4_fitted_models.txt` y `data/outputs_g3_fitted_subsets.txt`.

## Qué pasa con los resultados anteriores

Las clasificaciones de los notebooks 08 y 09 se conservan en sus reportes por trazabilidad. La clasificación en la puerta P4 se vuelve a establecer con los resultados del notebook 10 y se registra abajo.

## Resultado

Corrida del 22/11/2026 con las versiones de software del artículo (scikit-learn 1.6.1, XGBoost 3.0.2); los valores de la población completa reproducen el notebook 02 (AUROC de XGBoost 0,791). XGBoost, intervalos de 95% por *bootstrap* de pacientes:

| Modelo | C1 | C2 | C4 | Clasificación |
|---|---|---|---|---|
| Principal (M2) | No cumple: *landmark* 0,719, caída 0,072 (0,056–0,088), ganancia conservada 40% (30–51%) | **Cumple**: documentada 0,765 (0,713–0,816), estricta 0,784 (0,721–0,843) | No cumple (el período de desarrollo pasa P3) | Identificador temprano (sin cambio) |
| R4 | No cumple: *landmark* 0,740, caída 0,081, ganancia conservada 29% | Cumple: 0,763 y 0,776 | No cumple | Identificador temprano (sin cambio) |
| R2 | Cumple: *landmark* 0,765, caída −0,003 | Cumple: 0,763 | **No evaluable** (46 eventos; P3 exige 155) | No pasa P3 en la población completa (sin cambio) |
| R2 reducido | Cumple: *landmark* 0,752, caída −0,004 | No cumple: 0,749 (0,699–0,798) | **No evaluable** (46 eventos; P3 exige 71) | Señal exploratoria de predicción (sin cambio) |

Componentes del escalamiento (modelo de 32 parámetros): ingreso a UCI 0,770, ventilación mecánica 0,758, indicador por procedimiento 0,702; muerte, menos de 10 eventos. Reportes: `data/outputs_g4_fitted_models.txt`, `data/outputs_g3_fitted_subsets.txt`.

## Cambios de reporte registrados en la misma fecha

- **Puerta P3 en dos pasos.** Planeación, antes de ajustar cualquier modelo candidato, con un R² de Cox-Snell supuesto del 15% de su máximo (Riley et al.), y reevaluación con el R² observado fuera de muestra de la regresión logística penalizada con validación cruzada. Se reportan los dos; la decisión es la misma para todos los desenlaces (`scripts/g3_planning_assumed_r2.py` → `data/outputs_g3_planning.txt`).
- **Conteo de parámetros candidatos.** Columnas después de la codificación *one-hot*, una por categoría, sin el intercepto (32 en el modelo principal; 13 en el escalamiento reducido: 3 numéricos, 5 binarios y 5 grupos de raza y etnia). Los criterios de Riley se aplican como mínimo para todos los algoritmos.
- **Criterio C4.** Las clasificaciones del artículo mantienen la regla fijada el 04/11/2026 (el IC 95% de la pendiente incluye 1). La banda de tolerancia de la versión 1.1 del framework (estimación puntual de la pendiente entre 0,90 y 1,10) se reporta como análisis de sensibilidad: ninguna clasificación cambia (modelo principal 0,83; retorno R4, *landmark*, 0,73; escalamiento no evaluable).
- **Intervalos.** Toda cantidad de decisión se reporta con su intervalo de 95% (artículo, Tabla 4).
