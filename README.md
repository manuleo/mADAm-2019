# Solving hunger in Africa: a global handbook

# Abstract
Despite recent technological improvements, there is still a large share of people on this globe who are starving. *“1 in 9 people in this world go to bed on an empty stomach”* (source: [World Food Program](https://www.wfp.org/zero-hunger)). The aim of this project is to propose a way to end starvation in Africa, one of the continents most affected by this hunger issue. To do so, we’ll devise an appropriate daily nutritional input (according to some dietary guidelines) and come up with a set of food categories/products (through an analysis of food calories and nutrients) that combined will be able to accomplish this objective. We’ll use the FAO dataset (which has data about agricultural production amounts, producer prices, among other useful data) to determine which countries should provide which food items in order to solve this hunger issue at the lowest cost possible. This combined effort approach is a simple solution we think could potentially have a huge impact on many lives!


# Research questions
* How can we quantify hunger in Africa in terms of kcal needed per person per day? What are the regions that need the most help?
* What would be a good daily food plan to supply the correct amount of energy and solve this problem?
* Which countries can provide the resources to meet this plan (based on previously observed data)?
* If everyone does work together, can we solve hunger on this continent?


# Dataset
### FAO dataset
**Food balance**
This section contains food supplies for every country in the world. As the documentation reports, a region supply is defined as: *“Production + imports - exports + changes in stocks (decrease or increase)”.*
We will use this database to analyze the amount of kcal/person/day for each African state in the food categories we are interested in.
Population: used to determine the male and female population of each state we are interested in. 

**Producer Prices - Annual** 
This dataset includes information about production prices. We will use it to compute the ranking of the most suitable countries able to help Africa

All FAO’s data are in .csv so easy to parse and to work on.

### USDA Agricultural Research Service (ARS) Nutrition Facts Database
(additional dataset found online)
We will use this dataset to build the optimal diet. This dataset contains nutritional information for raw products, covering all those present in the FAO dataset. The information reported are per 100 g of servings. You can find this dataset in our `data` folder.

### Additional
[Estimated calories needed](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/): we will scrape this page to obtain information on the average calories needed for the African population


# Milestones up to milestone 2
#### 04/11/2019 
1. Elaborate a model by which we can calculate an ideal daily caloric intake for men and women. Goal would be to scrape the [Estimated calories webpage](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/) in order to obtain substantial data on estimated energy needs that we can then compute and adapt to our particular case.

2. Use data from POPULATION section (Fao Database) to extract current African population based on gender.

#### 11/11/2019
1. Compute for every region in Africa an estimation of kilocalories demand taking into account the composition of population.

2. Focus on FOOD BALANCE section (FAO Database) in order to retrieve data about African food supply (kcal/ per capita per day).

3. Given the data we gathered so far, we can now compute the amount of kilocalories we have to hit in order to fill the gap. For the sake of simplicity, we suggest to consider a share of 55% of carbohydrates, 25% of proteins and 20% of fat. In this context, we will also elaborate an analysis on the hunger issue on a country basis. 

#### 18/11/2019
1. We focus now on figuring out a feasible solution for the problem. The first step would be to come up with a draft diet based on simple products (chicken, meat, rice, etc..) that can fulfill the demand in each African country. 

2. The USDA ARS food dataset will be used to convert kilocalories (proteins, carbs and fat) into kg of final product we would have to deliver.

3. The above mentioned diet will be the basis for a more specific analysis on the nations (restricted to Europe, USA and China) more suitable to provide the resources. In particular, we are going to rank countries based on price/kg and internal supply of every product.

#### 25/11/2019
For the last week we will focus on visualizing the data in the best way and we are thinking about creating:
* An interactive geographical visualization of the poorest country in Africa in terms of lackness of food.
* An interactive heat map of the world by which the reader can easily see price and availability of every product in our proposed diet. 


# Questions for TAa
* We would need a more accurate dataset about African population based not only on gender but also on age. This would help us to increase the accuracy of our estimation of kilocalories needed. Could you recommend one to us?
* We would like to add some ways to rank most suitable countries that can provide food but rather than price/kg and internal supply we couldn’t come up with other ideas. Any suggestion on this?

