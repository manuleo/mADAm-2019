---
layout: default
id_div: six_section
img: |
category: |
title: Appendix
description: |
---
<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-8">
   <p>
    <h2>Datasets used </h2>
   <ul>
     <li> <b>FAO dataset</b> <br>
This <a href="http://www.fao.org/faostat/en/#data" target="_blank">section</a>  contains food supplies for every country in the world. As the documentation reports, a region supply is defined as <i> Production + imports - exports + changes </i> in stocks (decrease or increase)”. We will use this database to analyze the amount of <i> kcal/person/day </i> for each African and European state in the food categories we are interested in. Furthermore it contained information about every country's GDP</li>
     <br>
     <li> <b>United Nations /DESA / Population Division</b> <br>
The dataset was retrieved at this <a href="https://population.un.org/wpp/" target="_blank">link</a>. This dataset was used to determine the male and female population for Europe and Africa from 1950 to 2020 with a granularity of 5 years. We will interpolate to obtain data with 1 year frequency. All FAO datasets are in <i> .csv </i>, so it is easy to parse and to work on. Same applies to United Nations dataset. The dimensions were overall manageable and no problems emerged.</li>
     <br>
     <li> <b>Geospatial data </b><br>
This dataset was retrieved from Kaggle at the following <a href="https://www.kaggle.com/worldbank/world-development-indicators" target="_blank">link</a> . The dataset contains the geometry of every country in the world. The dataset can be imported easily as it's a json file and also quite small. The json file will be then converted to a GeoPandas Dataframe with <i> geopandas </i> (specialized library to work with geographical visualization).</li>
     <br>
      <li> <b>USDA Agricultural Research Service (ARS) Nutrition Facts Database (additional dataset found online) </b> <br>
      We will use this dataset to build the optimal diet. This dataset contains nutritional information for raw products, covering all those present in the FAO dataset. The information reported are per 100 g of servings.</li>
     <br>
     <li> <b>European Commission dataset</b> <br>
       This dataset (<a href="https://ec.europa.eu/info/food-farming-fisheries/farming/facts-and-figures/markets/prices/price-monitoring-sector/eu-prices-selected-representative-products_en"  target="_blank">link</a>) was used to get domestic food prices for items whose prices were not included in the FAO dataset.
     </li>
     <br>
       <li> <b> Additional </b><br>     
Estimated calories needed: we scraped this <a href="https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/" target="_blank">website</a> to obtain information on the average calories needed for the African population. </li>
    </ul>
    </p>
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-8">
   <p>
    <h2>Methods </h2>
    <h3>Convex Optimization  </h3>
    Two minimizations were carried out. The first tackled the issue of minimizing the amount of food that has to be delivered by the five chosen european contries. While minimizing, the demand constraints had to be respected as well as the constraints on food availability of each European country. The objective function to be minimized was a quadratic non-negative weighted sum of food [kcal/year]. More spefically, the weights were designed to take into account both the GDP of a country and the food availability [kcal/year]. The modelling choice is justified by the fact that a rich country with a large surplus should contribute more than a relatively poor country with less possibilities. The problem we want to model is a <b> Quadratic Program with Linear Constraints (QP) </b>. The choice of a quadratic objective function is due the fact that we will need to evenely distribute the resources and this means that weights will have to increase quadratically with the amount of food given away. It makes sense to say that the more a country gives away of its surplus, the less the same country should contribute further if other countries didn't countribute at all yet.
    In particular:
- $Y$ is a matrix in $R^{mxn}$ in which $m$ is the number of European countries and $n$ is the number of African countries. Each entry $y_{ij}$ of the matrix $Y\in{R^{mxn}}$ is the amount [kcal/year] of kilocalories that the European country $i\in{1,...,m}$ will have to send to the African country $j\in{1,...,n}$
- The weights will be in the interval $[-1,1]$. Initally we normalize the GWP per capita of every european country. Afterwards, we will calculate the gwp_inverse = (1-gwp_normalized). The final weight is computed by multiplying the food surplus for gwp_inverse. The number obtained will be the measure by which the logic "The richest gives more" is respected. We will name the weights $w\in{R^{mx1}}$.
- The objective function is $\sum_{i=1}^{m}\sum_{j=1}^{n}{w_jy_{ij}^2 + w_jy_{ij}}$
- The constraints can be considered a restriction on the value that our decision variable will assume. By restricting the feasibile set we will impose the following limits: 
  - non-negativity of food [kcal/year] sent
  - supply and demand must be met according to European country surplus and African countries deficit.
  - even distribution of resources

       </p>
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>


<script>
$(document).ready(function() {

  $("#six_section").removeClass("content-section-b");
  $("#six_section").addClass("content-section-black");
});

</script>
