# Tracks
* Joao: explode and counter-explode the nutrition values
* Manuel: extract African countries from population - age and match with nutrition data
* Riccardo/Dario: extract kcal from Food Balance + try to predict up to 2015 (2020) 

Specific idea: we have kcal/group_year/day after merge between nutrition and population -> we can divide with the number of people in each group
and we achieve kcal/persona/day in each group -> we can compare this data with FAO directly

General idea: we have kcal/persona/day from FAO, we can obtain kcal/year by multiply per people in each country and 365. In the other group
we sum and multiply per 365 and we have kcal/year total needed
