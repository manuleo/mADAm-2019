---
layout: default
id_div: second_section
img: |
category: |
title: Europe to the rescue
description: |
---

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <h2>The surplus in 2020: A global view</h2>
        Determining recipient countries should be easy, one might think. Just consider the red ones, right? Yet what about unequal wealth distribution? A better-off person eating more than the calculated daily average means another person gets less. For this reason, a threshold of 300 calories in surplus was introduced to be on the safe side. This also entails more countries are being targeted to receive help. 
        Let us now list all the previously determined values for 2020 on a map. This yields the following:
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-5">
        <div id="map_world_diff" style="width: 100%; height: 700px"></div>
    </div>
    <div class="col-sm-12 col-md-3">
        The observations mainly coincide with what was expected. The results seem to be similar to the food supply situation, only minor changes for some countries can be detected. The degree of food deficit of Chad in Northern-Central Africa, for example, was mitigated by the fact that its population is very young, compared to other African nations. These small differences, however, are crucial when evaluating which countries are actually in need. Using a map for visualization further allows us to observe that mainly landlocked countries in Central Africa show a large food deficit. Considering that countries like Ethiopia, which are known to be prone to suffer from famines were also determined to be lacking in this analysis, confirming that the methodology and the datasets used should be accurate
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <h2>Which countries can help</h2>
        Let’s determine now which European countries would be most suitable for redistribution. Belgium boasts the highest surplus per capita (around 1350 kcal/capita/day). Just to put this into perspective: a Belgian person’s equivalent of food waste could help one person in every single deficient African country each to reach a healthy amount of calory intake. The following plot provides an overview of all countries. When redistributing food, most larger European countries have enough of a surplus to solely solve the hunger issue in Africa. However, if only one country starts to donate its entire surplus, the costs are assumed to be greater than if multiple countries decided to send a smaller amount each. On the other hand, the amount of European countries should be minimized in order to facilitate calculations and enable a proper analysis.
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8" >
        {% include gdp_surplus.html %}
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        In this case, <b> Germany, France, Italy, Spain,</b> and the <b>United Kingdom</b> were chosen. Even though Russia has the greatest surplus, it was not considered as its GDP is much smaller than the one of other European countries. Moreover, its vast extent and remote nature makes efficient endeavors of collecting remaining food unlikely. Spain was preferred over Poland due to more useful geographical position as well as better economic performance.
        <p>Let us now have a look at how to evaluate a specific redistribution.</p>
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<script>

var cal_world_ticks = {};
$.ajax({
    url: "json/cal_world/cal_world_ticks.json",
    async: false,
    dataType: 'json',
    success: function(data) {
        cal_world_ticks = data;
    }
});

colors5 = ["#d7191c","#fdae61", "#ffffbf", "#a6d96a", "#1a9641"]
load_map(cal_world_ticks, "json/cal_world/cal_world_2020.geojson", colors5, 'map_world_diff', [30.318462, 19.56871], 'Estimation of deficit/surplus', 'kcal / person / day', 3, -1, layergroupHolder, mapHolder);


</script>
