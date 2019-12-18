---
layout: default
id_div: second_section
img: |
category: |
title: Europe to the resuce
description: |
---

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <h3>The surplus in 2020: A global view</h3>
        Let us now list all the previously determined values for 2020 on a map. This yields the following:
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br/>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <div id="map_world_diff" style="width: 100%; height: 700px"></div>
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br/>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <h3>Which countries can help</h3>
        Let’s determine now what European would be most suitable for redistribution. Belgium boasts the highest surplus per capita (around 1350 kcal/capita/day). Just to put this into perspective: a Belgian person’s equivalent of food waste could help one person in every single deficient African country each to reach a healthy amount of calory intake. The following map provides an overview of all countries. When redistributing food, most larger European countries have enough of a surplus to solely solve the hunger issue in Africa. However, if only one country starts to donate its entire surplus, the costs are assumed to be greater than if multiple countries decided to send a smaller amount each. On the other hand, the amount of European countries should be minimized in order to facilitate calculations and enable a proper analysis, . 
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br/>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-7">
        {% include scatter_gdp_surplus.html %}
    </div>
    <div class="col-sm-12 col-md-3" style="border-left:solid thin #eee; height: 600px">
        In this case, Germany, France, Italy, Spain, and the United Kingdom were chosen. Even though Russia has the greatest surplus, it was not considered as its GDP is much smaller than the one of other European countries. Moreover, its vast extent and remote nature makes efficient endeavors of collecting remaining food unlikely. Spain was preferred over Poland due to more useful geographical position as well as better economic performance.
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        Let us now have a look at how to evaluate a specific redistribution.
    </div>
    <div class="col-sm-12 col-md-1"></div>
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
load_map(cal_world_ticks, "json/cal_world/cal_world_2020.geojson", colors5, 'map_world_diff', [30.318462, 19.56871], 'Estimation deficit/surplus', 'kcal / persona / day', 3, -1, layergroupHolder, mapHolder);


</script>
