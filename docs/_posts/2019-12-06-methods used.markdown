---
layout: default
id_div: fourth_section
img: |
category: |
title: Datasets used
description: |
---
<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-8">
   <p>
   <ul>
     <li> <b>FAO dataset</b> <br>
This section contains food supplies for every country in the world. As the documentation reports, a region supply is defined as <i> Production + imports - exports + changes </i> in stocks (decrease or increase)”. We will use this database to analyze the amount of <i> kcal/person/day </i> for each African and European state in the food categories we are interested in.</li>
     <br>
     <li> <b>United Nations /DESA / Population Division</b> <br>
Population The dataset was retrieved at this <a href="https://population.un.org/wpp/" target="_blank">link</a>. This dataset was used to determine the male and female population for Europe and Africa from 1950 to 2020 with a granularity of 5 years. We will interpolate to obtain data with 1 year frequency. All FAO datasets are in <i> .csv </i>, so it is easy to parse and to work on. Same applies to United Nations dataset. The dimensions were overall manageable and no problems emerged.</li>
     <br>
     <li> <b>Geospatial data </b><br>
This dataset was retrieved from Kaggle at the following <a href="https://www.kaggle.com/worldbank/world-development-indicators" target="_blank">link</a> . The dataset contains the geometry of every country in the world. The dataset can be imported easily as it's a json file and also quite small. The json file will be then converted to a GeoPandas Dataframe with <i> geopandas </i> (specialized library to work with geographical visualization).</li>
     <br>
      <li> <b>USDA Agricultural Research Service (ARS) Nutrition Facts Database (additional dataset found online) </b> <br>
      We will use this dataset to build the optimal diet. This dataset contains nutritional information for raw products, covering all those present in the FAO dataset. The information reported are per 100 g of servings.</li>
     <br>
       <li> <b> Additional </b><br>     
Estimated calories needed: we scraped this <a href="https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/" target="_blank">website</a> to obtain information on the average calories needed for the African population. </li>
    </ul>
    </p>
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<div class="row">
</div>

