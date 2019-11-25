# Solving hunger in Africa: a global handbook

# Abstract
Despite recent technological improvements, there is still a large share of people who are starving. *“1 in 9 people in this world go to bed on an empty stomach”* (source: [World Food Program](https://www.wfp.org/zero-hunger)). The aim of this project is to propose a way to end starvation in Africa, one of the continents most affected by this hunger issue. To do so, we will tackle the problem from two different perspectives. On one hand, the analysis will show an estimatation of which African countries have food deficits. On the other hand, the investigation will give the reader a complete picture of the food availability across Europe. The FAO dataset will be intensively used as it contains useful information about net food supply for both Africa and Europe. The analysis section will then leave space to a more important chapter of our story: how to solve the uneven distribution of food? We would like to reallocate resources that otherwise would be end up as food waste from the richest European countries to the poorest African ones. This combined effort approach is a simple solution we think could potentially have a huge impact on many lives!


# Research questions
- [x] How can we quantify hunger in Africa in terms of kcal needed per capita per day? What are the regions that need the most help?

- [x] Can we make truthful predictions on African and European population for 2020 based on data we have until 2013? And what about food supply? Will our predictions be accurate? 

- [x] By analysing the time period 1960 to 2020, could it be possibile to assess if the African food situation actually improved and why? In this context, can we explain important changes in food availability observed by correlating them with historical facts? 

- [x] How Europe evolved from 1960 to 2020 in terms of food waste? 

- [x] How can we quantify food surplus in Europe? What are the regions characterised by the highest food waste rates?

To go:

- [ ] Can we produce a list of simple and highly nutrient-dense final products that can be shipped from Europe to Africa? 

- [ ] How can we define a consistent model to predict which European countries have to ship and how much should they individually contribute?

- [ ] Which countries can provide the resources to meet this plan (based on previously observed data)?

- [ ] If everyone does work together, can we solve hunger on this continent?


# Dataset
### FAO dataset
**Food balance**  
This section contains food supplies for every country in the world. As the documentation reports, a region supply is defined as: *“Production + imports - exports + changes in stocks (decrease or increase)”.*
We will use this database to analyze the amount of kcal/person/day for each African **and** European state in the food categories we are interested in.

### United Nations /DESA / Population Division 
**Population**
The dataset was retrieved at this [link](https://population.un.org/wpp/). This dataset was used to determine the male and female population for Europe and Africa from 1950 to 2020 with a granularity of 5 years. We will interpolate to obtain data with 1 year frequency.
All FAO’s dataset are in .csv so easy to parse and to work on. Same applies to United Nations dataset. The dimensions are overall manageable and no problems emerged.

### Geospatial data 
This dataset was retrieved from Kaggle at the following [link](https://www.kaggle.com/worldbank/world-development-indicators). The dataset contains the geometry of every country in the world. The dataset can be imported easily as it's a json file and also quite small. The Json file will be then converted to a GeoPandas Dataframe with geopandas (specialized library to work with geographical visualization).


### USDA Agricultural Research Service (ARS) Nutrition Facts Database  
(additional dataset found online)  
We will use this dataset to build the optimal diet. This dataset contains nutritional information for raw products, covering all those present in the FAO dataset. The information reported are per 100 g of servings. You can find this dataset in our `data` folder.

### Additional
[Estimated calories needed](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/): we will scrape this page to obtain information on the average calories needed for the African population


# Milestones up to milestone 2
#### 04/11/2019 
1. Elaborate a model by which we can calculate an ideal daily caloric intake for men and women. Goal would be to scrape the [Estimated calories webpage](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/) in order to obtain substantial data on estimated energy needs that we can then compute and adapt to our particular case.

2. Use data from POPULATION section (FAO Database) to extract current African population based on gender.

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
* An interactive geographical visualization of the poorest country in Africa in terms of lack of food.


# Milestone 2
The results we came up with are satisfactory as they accurately reproduce what was expected. They also allowed for interesting analysis.
We decided to conduct an analysis on Europe too as it's interesting to see how much spare food would be available for redistribution, as European countries are more likely to be able to provide help. 
Furthermore, it was decided to restrict further analysis to 2020 as the interest is in the contemporary situation.
Nine African countries were found to show an overall deficit in supply, meaning unlike other African countries, they are not capable of solving their issues themselves.  

# Milestones up to Milestone 3
Methodology: A proposal will be made how food could be redistributed from Europe to Africa, not countrywise. Even though a country might overall be in a surplus, it could potentially lack some macronutrient (making up for it with more of another one). As we are not only interested in supplying the necessary calories but also providing a healhty diet, the analysis will be continued with into the three macronutrients (Carbs, Proteins and Fat). Due to calories not being a tangible unit for most readers (especially when using orders of magnitude of Gigacalories), representative products for each macronutrient will be introduced to facilitate conveyance for a broader audience.

# Milestones up to milestone 3
#### Week 26/11-31/11:
1. Split the nutrition supply into macronutrients and analyze respective surplus and deficit
2. After obtaining such informations, we are able to choose which items are considered as "of interest" to represent the abstract notion of calories
#### Week 2/12-7/12:
3. We aggregate European and African countries and, by representing calories/macronutrients as food items, we decide how much of which food items Europe as a whole should provide to Africa
4. After deciding these quantities, we'll find which countries should provide and receive which food items and in what quantities, based on their surplus and deficits, respectively
#### Week 9/12-14/12*:
5. Come up with visualization methods for these informations, in order to catch the attention of the user
#### Weeks from 16/12-25/12*:
6. Develop a data story that presents the issue we want to solve, and propose our way to solve it

During all the weeks starting now (26/11) we'll be finding ways to interactively and interestingly show the results we come up with.
