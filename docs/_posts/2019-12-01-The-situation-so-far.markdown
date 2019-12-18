---
layout: default
id_div: first_section
img: |
category: |
title: The situation so far
description: |
---

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <h3>How much does each continent have?</h3>

        Africa and Europe’s historical food situation was thoroughly analyzed. Based on past values, data was predicted and analyzed for the upcoming year 2020 in order to be as close to reality as possible. The following maps show the food that was supplied by each continent. 
        <!--I think needs some more text; map text balance a bit off-->
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-6">
        <div id="map_africa_supply" style="width: 100%; height: 700px;"></div>
    </div>
    <div class ="col-sm-12 col-md-4">
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fermentum sit amet sapien sed lacinia. Pellentesque venenatis sem ornare, ornare tortor eu, vehicula leo. Integer congue vehicula tortor, eleifend placerat orci gravida aliquam. Duis tincidunt mi non massa tempor, ornare consectetur diam congue. Curabitur sit amet eleifend magna, vitae volutpat lacus. Praesent luctus libero tempus nisl ullamcorper tempus. Ut eros felis, porttitor a urna eu, placerat sodales tortor. In hac habitasse platea dictumst. Cras bibendum sem eu scelerisque rutrum. Maecenas sollicitudin dui id sapien interdum fermentum. Pellentesque ac convallis nibh, id lacinia lectus. 
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fermentum sit amet sapien sed lacinia. Pellentesque venenatis sem ornare, ornare tortor eu, vehicula leo. Integer congue vehicula tortor, eleifend placerat orci gravida aliquam. Duis tincidunt mi non massa tempor, ornare consectetur diam congue. Curabitur sit amet eleifend magna, vitae volutpat lacus. Praesent luctus libero tempus nisl ullamcorper tempus. Ut eros felis, porttitor a urna eu, placerat sodales tortor. In hac habitasse platea dictumst. Cras bibendum sem eu scelerisque rutrum. Maecenas sollicitudin dui id sapien interdum fermentum. Pellentesque ac convallis nibh, id lacinia lectus. 
        </p>
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-4">
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fermentum sit amet sapien sed lacinia. Pellentesque venenatis sem ornare, ornare tortor eu, vehicula leo. Integer congue vehicula tortor, eleifend placerat orci gravida aliquam. Duis tincidunt mi non massa tempor, ornare consectetur diam congue. Curabitur sit amet eleifend magna, vitae volutpat lacus. Praesent luctus libero tempus nisl ullamcorper tempus. Ut eros felis, porttitor a urna eu, placerat sodales tortor. In hac habitasse platea dictumst. Cras bibendum sem eu scelerisque rutrum. Maecenas sollicitudin dui id sapien interdum fermentum. Pellentesque ac convallis nibh, id lacinia lectus. 
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fermentum sit amet sapien sed lacinia. Pellentesque venenatis sem ornare, ornare tortor eu, vehicula leo. Integer congue vehicula tortor, eleifend placerat orci gravida aliquam. Duis tincidunt mi non massa tempor, ornare consectetur diam congue. Curabitur sit amet eleifend magna, vitae volutpat lacus. Praesent luctus libero tempus nisl ullamcorper tempus. Ut eros felis, porttitor a urna eu, placerat sodales tortor. In hac habitasse platea dictumst. Cras bibendum sem eu scelerisque rutrum. Maecenas sollicitudin dui id sapien interdum fermentum. Pellentesque ac convallis nibh, id lacinia lectus. 
        </p>
    </div>
    <div class ="col-sm-12 col-md-6">
        <div id="map_europe_supply" style="width: 100%; height: 700px"></div>
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <h3>How much does each continent need?</h3>
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <h3>How much is Africa lacking and how much can Europe help?</h3>

        Subtracting demand from the supply, deficits in case of negative results could be determined. In order to get an impression of how both continents evolved over time, have a look at these animations.
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<br>

<div class="row" style="text-align:center">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-5">
        {% include cal_diff_africa.html %}
    </div>
    <div class="col-sm-12 col-md-5" style="border-left: solid;border-left-color: #e3e3e3;">
        {% include cal_diff_europe.html %}
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-5"></div>
    <div class="col-sm-12 col-md-5" style="height:20pt; border-left: solid;border-left-color: #e3e3e3;"></div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-5">
        Various events can be put into context here, for example, the famine in Ethiopia in the ’80s, where Ethiopia figured among the countries with the highest deficit per capita. Looking at the more recent years, this animation already suggests that only by smart redistribution, Africa could sustain its own food demand. However, having the capabilities and know-how to efficiently set up a food aid operation is harder than it seems. European countries, on the other hand, have a lot more experience in this field, and they are expected to have an even higher amount of excess food, making it easier to provide for this whole operation.
    </div>
    <div class="col-sm-12 col-md-5" style="border-left: solid;border-left-color: #e3e3e3;">
        Surprisingly, all European countries boast an overall surplus in the food supply, with the exception being Albania which was slightly deficient during the first few years of our investigation (‘60s). Another significant occurrence can be detected during the aftermath of Yugoslavia’s disintegration (insert Wikipedia link maybe?) in 1992, where ex-member states like Croatia, Bosnia & Herzegovina and former Macedonia’s nourishment status deteriorated drastically, causing a temporary shortage of nutrition. Most of the other countries, however, have constantly shown a surplus of around 1000 kcal per day and per person, meaning a third of European food does not end up being consumed - in other words: food waste.
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

<script>

var africa_ticks_supply = {};
$.ajax({
    url: "json/africa_supply/africa_supply_ticks.json",
    async: false,
    dataType: 'json',
    success: function(data) {
        africa_ticks_supply = data;
    }
});

var europe_ticks_supply = {};
$.ajax({
    url: "json/europe_supply/europe_supply_ticks.json",
    async: false,
    dataType: 'json',
    success: function(data) {
        europe_ticks_supply = data;
    }
});

layergroupHolder = {};
mapHolder = {}

colors1 = ["#f1eef6","#d0d1e6", "#a6bddb", "#74a9cf", "#2b8cbe", "#045a8d"]
load_map(africa_ticks_supply, "json/africa_supply/africa_supply_", colors1, 'map_africa_supply', [2.318462, 19.56871], 'African Food Supply', 'kcal / persona / day', 3, 1, layergroupHolder, mapHolder);

colors2 = ["#fff7fb","#ece7f2", "#d0d1e6", "#a6bddb", "#74a9cf", "#3690c0", "#0570b0", "#045a8d", "#023858"]
load_map(europe_ticks_supply, "json/europe_supply/europe_supply_", colors2, 'map_europe_supply', [54.5260, 15.2551], 'European Food Supply', 'kcal / persona / day', 4, 2, layergroupHolder, mapHolder);

</script>