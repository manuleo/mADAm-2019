---
layout: default
id_div: first_section
img: |
category: |
title: A history of food distribution
description: |
---

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <h2>How much does each continent have?</h2>
         As a starting point, looking at the total food supply every year in each country already enables a solid overview about the dynamics. More specifically, Africa and Europe’s historical food situation was thoroughly analyzed. Based on past values, data was predicted for the upcoming year <b> 2020 </b> in order to be as close to reality as possible.
        The following maps show the food that was supplied by each continent for every year since 1960. 
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-5">
        <div id="map_africa_supply" style="width: 100%; height: 600px;"></div>
    </div>
    <div class ="col-sm-12 col-md-3" >
        <p>
            In Africa, there is a clear <b> disparity </b> between North African countries and their sub-Saharan counterparts, which started to take form in the 70's. Currently, all of the former ones command a supply of <b>more than 3000 kcal per person per day</b> except for Sudan. To put this into context: A man at the age of 20 is expected to have at least 3000 kcal per day to safely avoid malnutrition. Simply judging by the change in color over the years, it can be stated that overall, there already was some improvement in most nations, especially after the year 2000. *Some of the states were not listed in the FAO dataset and are consequently blank*. 

        </p>
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-3">
        <p>
            As expected, most of the European countries show a <b>stable</b> food supply situation, with values being more homogeneous than on the African continent. Interestingly, <b> Belgium, Austria,</b> and <b> Italy </b> are provided with the highest amount per capita. Impacts of historical events can be seen when simulating a time series using the sliders. For example, a sharp drop in Eastern Europe can be observed in the years following the dissolution of the Soviet Union. Furthermore, a correlation with a nation’s Gross Domestic Product (GDP) can be assumed.
        </p>
        <p>
            *Again, a few countries were not included in the dataset (mostly recenly established nations) and are left blank with no values assigned to them*.
        </p>
    </div>
    <div class ="col-sm-12 col-md-5">
        <div id="map_europe_supply" style="width: 100%; height: 600px"></div>
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <h2>How much does each continent need?</h2>
            In order to deduce a country’s demand, it would seem natural to just look at the population size multiplied by an average person’s daily need. However, this methodology would not account for different <b> demographic compositions </b>.
According to this <a href="https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/" target="_blank">(source)</a>, there are discrepancies between varying age groups and their respective nutritional requirements. Hovering over the plot will show how the highest caloric need is addressed by males and females in their 20s and 30s.
        
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-5">
        {% include gender.html %}
    </div>
    <div class="col-sm-12 col-md-3">
            By multiplying this data with the same demographic age-range information, a much preciser number for national food demand is obtained. This takes situations into account where a nation’s population composition differs substantially to others. For example, during war periods the male population would significantly be reduced. Additionally, the age-sex-pyramid often shows higher shares of young people and babies, who evidently need less than an adult person.
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-8">
        <h2>How much is Africa lacking and how much can Europe help?</h2>
        Subtracting demand from the supply, deficits for the case of negative results could be determined. Move the sliders to get insight on the food surplus's evolution over time!
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

<div class="row" style="text-align:center">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-4" style="border-right: solid;border-right-color: #e3e3e3;">
        <div>
            {% include cal_diff_africa.html %}
        </div>
    </div>
    <div class="col-sm-12 col-md-4">
        <div>
            {% include cal_diff_europe.html %}
        </div>
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-4" style="border-right: solid;border-right-color: #e3e3e3; height:20pt"></div>
    <div class="col-sm-12 col-md-4"></div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-2"></div>
    <div class="col-sm-12 col-md-4" style="border-right: solid;border-right-color: #e3e3e3;">
        Various events can be put into context here, for example, the famine in Ethiopia in the ’80s, where Ethiopia figured among the countries with the highest deficit per capita. Looking at the more recent years, this animation already suggests that only by smart redistribution, <b> Africa </b> could <b> sustain its own food demand </b>. However, having the capabilities and know-how to efficiently set up a food aid operation is harder than it seems. European countries, on the other hand, have a lot more experience in this field, and they are expected to have an even higher amount of excess food, making it easier to provide for this whole operation. Ever since 2001, more than half of the examined countries show a net surplus. As of 2019, all of the countries in red were determined to be either war-riddled or politically fragile. Exceptions to the rule are Namibia and Eswatini, both of which boast a relatively high GDP per capita (ranked 10th and 11th for the African continent, respectively). Thus, the only explanation would be inequality amongst the population or insufficient distribution of available resources.
    </div>
    <div class="col-sm-12 col-md-4">
        Surprisingly, <b> all </b> European countries boast an overall <b> surplus </b> in the food supply, with the exception being Albania which was slightly deficient during the first few years of our investigation (‘60s). Another significant occurrence can be detected during the aftermath of <a href="https://en.wikipedia.org/wiki/Breakup_of_Yugoslavia" target="_blank">Yugoslavia’s disintegration</a>
        in 1992, where ex-member states like Croatia, Bosnia & Herzegovina and former Macedonia’s nourishment status deteriorated drastically, causing a temporary shortage of nutrition. Most of the other countries, however, have constantly shown a surplus of around 1000 kcal per day and per person, meaning a third of European food does not end up being consumed - in other words: food waste.
    </div>
    <div class="col-sm-12 col-md-2"></div>
</div>

<br>

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

// colors1 = ["#f1eef6","#d0d1e6", "#a6bddb", "#74a9cf", "#2b8cbe", "#045a8d"]
colors1 = ["#d0d1e6", "#a6bddb", "#74a9cf", "#3690c0", "#0570b0", "#034e7b"]
// colors1 = ["#ccece6", "#99d8c9", "#66c2a4", "#41ae76", "#238b45", "#005824"]
load_map(africa_ticks_supply, "json/africa_supply/africa_supply_", colors1, 'map_africa_supply', [0.318462, 22.56871], 'African Food Supply', 'kcal / person / day', 3, 1, layergroupHolder, mapHolder);

// colors2 = ["#fff7fb","#ece7f2", "#d0d1e6", "#a6bddb", "#74a9cf", "#3690c0", "#0570b0", "#045a8d", "#023858"]
colors2 = ["#d0d1e6", "#a6bddb", "#74a9cf", "#3690c0", "#0570b0", "#034e7b"]
// colors2 = ["#ccece6", "#99d8c9", "#66c2a4", "#41ae76", "#238b45", "#005824"]
load_map(europe_ticks_supply, "json/europe_supply/europe_supply_", colors2, 'map_europe_supply', [52.5260, 25.2551], 'European Food Supply', 'kcal / person / day', 3, 2, layergroupHolder, mapHolder);

</script>
