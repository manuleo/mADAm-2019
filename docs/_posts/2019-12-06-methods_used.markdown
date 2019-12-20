---
layout: default
id_div: six_section
img: |
category: |
title: Appendix
description: |
---
<!--A comment for Manuel-->
<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <h2>Datasets used </h2>
        <ul>
            <li> <a href="http://www.fao.org/faostat/en/#data" target="_blank"><b>FAO dataset</b></a> <br>
                This dataset contains the
                following sub-dataset, which are used:
                <ul>
                    <li>
                        <b>Food balance:</b>
                        This section contains food supplies for every country in the world. As the documentation
                        reports, a region supply is defined as: “Production + imports - exports + changes in stocks
                        (decrease or increase)”.
                        We will use this database to analyze the amount of kcal/person/day for each African *and*
                        European state in the food categories we are interested in.
                    </li>
                    <li>
                        <b>Prices:</b>
                        We used FAO dataset to obtain prices of the food items analysed in
                        our diet. In this context, FAO did not contain all the prices needed.
                    </li>
                    <li>
                        <b>GDP:</b>
                        GDP was retrieved and used in order to obtain an overview on how much each
                        European country should contribute to the cause.
                    </li>
                </ul>
                <br>
            </li>
            <li>
                <a href="https://population.un.org/wpp/" target="_blank"><b>United Nations Population Dataset</b></a> <br>
                This dataset was used to determine the male and female population for Europe and Africa from 1950 to
                2020 with a granularity of 5 years. We will interpolate to obtain data with 1 year frequency.
            </li>
            <br>
            <li> <a href="https://fdc.nal.usda.gov/USDA" target="_blank"><b>Agricultural Research Service (ARS) Nutrition Facts Database</b></a> <br>
                Used to build the optimal diet. This dataset contains nutritional information
                for raw products. The information reported are per
                100 g of servings.
            </li>
            <br>
            <li><a
                    href="https://ec.europa.eu/info/food-farming-fisheries/farming/facts-and-figures/markets/prices/price-monitoring-sector/eu-prices-selected-representative-products_en"
                    target="_blank"><b>European Commission dataset</b></a><br>
                This dataset is used to get domestic food prices for items whose prices were not
                included in the FAO dataset. In the end, the majority of the prices came from this dataset.
            </li>
            <br>
            <li>
                <b>Additional</b>
                <br>
                Estimated calories needed: we scraped this <a
                    href="https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/" target="_blank">website</a>
                to obtain information on the average calories needed for the African
                population.
            </li>
        </ul>
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <p>
            <h2>Methods </h2>
            <h3>Recurrent Neural Networks (RNN)</h3>
            This widely used machine learning method was used to predict data up until the year 2020, as FAO only
            provides information until 2013. The RNN were preferred over a simple linear regression because the latter
            does not take into account intermittent outliers like periods of war or polticial instability. Additionally,
            the mostly exponential growth of food supply was not considered in this method. Also, giving the short avaibility of data (only about 50 datapoints for each country), using the feeback provided by the RNN improved the accuracy of the model exponentially. The RNN was fitted using all the data from the past, but an additional <i>time window</i> method was implemented. This method uses as datapoint to predict the next year supply not only the past history (already embedded in the model), but also a time span of the last 10 years datapoints, in order to fit better the time-series behavior of the recent history.
            <a href="https://www.tensorflow.org/tutorials/structured_data/time_series" target="_blank">Tensorflow</a>'s
            tutorial was used and adapted to fit this model.
            <h3>Convex Optimization </h3>
            Two minimizations were carried out.
            <br>
            The first tackled the issue of minimizing the amount of food that has to
            be delivered by the five chosen european contries. While minimizing, the demand constraints had to be
            respected as well as the constraints on food availability of each European country. The objective function
            to be minimized was a <b>quadratic non-negative weighted sum of food [kcal/year]</b>. More spefically, the weights
            were designed to take into account both the GDP of a country and the food availability [kcal/year]. The
            modelling choice is justified by the fact that a rich country with a large surplus should contribute more
            than a relatively poor country with less possibilities. The problem we want to model is a <b> Quadratic
            Program with Linear Constraints (QP) </b>. The choice of a quadratic objective function is due the fact
            that we will need to evenely distribute the resources and this means that weights will have to increase
            quadratically with the amount of food given away. It makes sense to say that the more a country gives away
            of its surplus, the less the same country should contribute further if other countries didn't countribute at
            all yet.
            <br>
            The second optimization concerned the composition of the diet, which is one of the <b>key steps</b> of our
            analysis. We decided to compute the amount of product by minimizing the actual costs of shipments that every
            European country had to meet. In order to model the problem we needed to define an objective function which
            in this case was the <b>non-negative weighted sum of products' cost</b>.
            The problem we want to model is a <b>Linear Program</b>.
        </p>
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>


<script>
    $(document).ready(function () {

        $("#six_section").removeClass("content-section-b");
        $("#six_section").addClass("content-section-black");
    });

</script>
