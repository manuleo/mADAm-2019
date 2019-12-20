---
layout: default
id_div: fourth_section
img: |
category: |
title: Conclusion
description: |
---
<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-8">
   <p>
   <ul>
    <li> AO dataset </li>
Food balance
This section contains food supplies for every country in the world. As the documentation reports, a region supply is defined as: “Production + imports - exports + changes in stocks (decrease or increase)”. We will use this database to analyze the amount of kcal/person/day for each African and European state in the food categories we are interested in.

     <li> United Nations /DESA / Population Division  </li>
Population The dataset was retrieved at this link. This dataset was used to determine the male and female population for Europe and Africa from 1950 to 2020 with a granularity of 5 years. We will interpolate to obtain data with 1 year frequency. All FAO’s dataset are in .csv so easy to parse and to work on. Same applies to United Nations dataset. The dimensions are overall manageable and no problems emerged.

     <li>Geospatial data </li>
This dataset was retrieved from Kaggle at the following link. The dataset contains the geometry of every country in the world. The dataset can be imported easily as it's a json file and also quite small. The Json file will be then converted to a GeoPandas Dataframe with geopandas (specialized library to work with geographical visualization).

      <li>USDA Agricultural Research Service (ARS) Nutrition Facts Database (additional dataset found online)</li>
      We will use this dataset to build the optimal diet. This dataset contains nutritional information for raw products, covering all those present in the FAO dataset. The information reported are per 100 g of servings.

       <li>Additional </li>
       
Estimated calories needed: we scraped this <a href="https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/" target="_blank">website</a> to obtain information on the average calories needed for the African population
    </ul>
    </p>
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<div class="row">
</div>
