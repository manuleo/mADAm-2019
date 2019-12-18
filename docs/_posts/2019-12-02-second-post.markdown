---
layout: default
id_div: second_section
img: |
category: |
title: Where we're at
description: |
---

<div class="row">
    <div class="col-sm-12 col-md-1"></div>
    <div class="col-sm-12 col-md-10">
        <h3>The surplus in 2020</h3>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et lobortis nulla, vitae aliquet massa. Aliquam ac ante consectetur, posuere purus eget, venenatis dui. Phasellus molestie consequat mauris, sit amet suscipit massa fringilla nec. Aliquam tincidunt vel leo sit amet fringilla. Ut molestie sem ut magna condimentum semper. Nulla bibendum libero consectetur nisi venenatis varius. Mauris vitae tellus ante. Nullam placerat, lacus id tincidunt tincidunt, enim metus vestibulum odio, eget egestas arcu tellus in dui. Nam maximus nunc mauris, ut pulvinar sem sodales in.
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
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et lobortis nulla, vitae aliquet massa. Aliquam ac ante consectetur, posuere purus eget, venenatis dui. Phasellus molestie consequat mauris, sit amet suscipit massa fringilla nec. Aliquam tincidunt vel leo sit amet fringilla. Ut molestie sem ut magna condimentum semper. Nulla bibendum libero consectetur nisi venenatis varius. Mauris vitae tellus ante. Nullam placerat, lacus id tincidunt tincidunt, enim metus vestibulum odio, eget egestas arcu tellus in dui. Nam maximus nunc mauris, ut pulvinar sem sodales in.
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
        Notes: 
        <ul>
            <li>Mention the 5 biggest balls to the right (Italy, Germany, United Kingdom, France, Spain) which are our selection</li>
            <li>Russia is big but small GDP</li>
        </ul>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et lobortis nulla, vitae aliquet massa. Aliquam ac ante consectetur, posuere purus eget, venenatis dui. Phasellus molestie consequat mauris, sit amet suscipit massa fringilla nec. Aliquam tincidunt vel leo sit amet fringilla. Ut molestie sem ut magna condimentum semper. Nulla bibendum libero consectetur nisi venenatis varius. Mauris vitae tellus ante. Nullam placerat, lacus id tincidunt tincidunt, enim metus vestibulum odio, eget egestas arcu tellus in dui. Nam maximus nunc mauris, ut pulvinar sem sodales in.
    </div>
    <div class="col-sm-12 col-md-1"></div>
</div>

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