# Entrada del libro de decisiones — algoritmo principal elegido por eventos por parámetro (11/11/2026)

Versión en inglés: [`decision_primary_learner_EPP_2026-11-11.md`](decision_primary_learner_EPP_2026-11-11.md).

**Etapa:** E8 (modelado, validación y métricas); decisión D16. **Tipo de razón:** metodológica.
**Estado:** propuesta por el primer autor; por validar con el director de la tesis.
**Alcance:** prospectivo. Se aplica a los desenlaces analizados **después** de esta fecha (desenlaces perinatales y
neonatales de la tesis). **No** cambia el modelo principal del artículo de SMM, que sigue siendo XGBoost, como se
fijó de antemano.

## Lección que la motiva
En el modelo reducido de escalamiento (101 eventos, 13 parámetros, 7,8 eventos por parámetro), la regresión
logística fue el algoritmo más preciso y más estable (AUROC 0,764; DE entre repeticiones 0,0075), mientras que
XGBoost quedó más bajo y fue menos estable (0,749; DE 0,020), y una grilla más amplia de XGBoost lo empeoró
(0,744; DE 0,030; data/outputs_escalation_reduced_xgbgrid_summary.txt). Los algoritmos flexibles necesitan muchos
más eventos por parámetro que la regresión (van der Ploeg, Austin, Steyerberg, BMC Med Res Methodol 2014;14:137).

## Regla
El algoritmo principal se fija en la ficha del desenlace **antes** de ajustar cualquier modelo, según los eventos por
parámetro candidato (EPP) de los datos de desarrollo:
- **EPP menor que 20:** la regresión logística penalizada es el modelo principal; los algoritmos de árboles y el
  ensamble son comparaciones.
- **EPP de 20 o más:** el modelo principal es el mejor algoritmo base de una corrida preliminar, como antes; el
  ensamble se adopta solo si supera a ese algoritmo de forma consistente (regla D16 sin cambios).
El umbral de 20 es una convención que el director debe confirmar antes del primer desenlace que la use.
