---
layout: default
id_div: third_section
img: |
category: |
title: Our solution
description: |
---

<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-8">
    <h2>The perfect diet</h2>
   Now, the exchange of calories is known. However, in what form should it be delivered? To reach a concrete and tangible recommendation on how to solve this issue, this is an essential question. For a well-balanced diet, a share of <b> 55% carbohydrates, 25% proteins </b> and <b> 20% fat </b> is <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1479724/" target="_blank">recommended</a>. Secondly, products of varying food groups should be included.
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-3">
   To this end, a ranking system was introduced to analyze all listed food items based on their previously defined composition              suitability. In doing so, the list of products to be considered could be reduced to 13 items to be used for further analysis.
   The food categories consequently considered are the following ones:
    <ul>
  <li>Beef Products</li>
  <li>Cereal Grains and Pasta</li>
  <li>Fruits and Fruit Juices</li>
  <li>Poultry Products</li>
  <li>Legumes and Legume Products</li>
  <li>Vegetables and Vegetable Products</li>
</ul>
   Selecting a data point in the plot on the right will allow you to see the product's name and its composition of the three macronutrients projected onto the corresponding axis. 
  </div>
  <div class="col-sm-12 col-md-5">
    {% include 3d_macros.html %}
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-8">
    <h2>The distribution plan</h2>
   For every European countries out of the five selected, the prices for the previously defined food items were established by <a href="http://www.fao.org/faostat/en/#data/PP"  target="_blank">FAO</a> data and a dataset from the <a href="https://ec.europa.eu/info/food-farming-fisheries/farming/facts-and-figures/markets/prices/price-monitoring-sector/eu-prices-selected-representative-products_en"  target="_blank">European Commission</a>. As different countries show different domestic prices for specific items, a cost minimization was carried out using convex optimization methods. Furthermore, a linearly increasing cost function with respect to the GDP was implemented yielding a higher cost if only one country was considered while also prefering to take from richer countries.
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-1" style="z-index:10;">
    <select id="chord_countries">
      <option value="Europe" selected>All Europe</option>
      <option value="France">France</option>
      <option value="Germany">Germany</option>
      <option value="Italy">Italy</option>
      <option value="Spain">Spain</option>
      <option value="UK">United Kingdom</option>
    </select>
  </div>
  <div class="col-sm-12 col-md-4" id="chord_box" style="margin-left: -50pt">
    <div id="Europe_chord" style="display:none">
      {% include chord.html %}
    </div>
    <div id="France_chord" style="display:none">
      {% include chord_fr.html %}
    </div>
    <div id="Germany_chord" style="display:none">
      {% include chord_ge.html %}
    </div>
    <div id="Italy_chord" style="display:none">
      {% include chord_it.html %}
    </div>
    <div id="Spain_chord" style="display:none">
      {% include chord_es.html %}
    </div>
    <div id="UK_chord" style="display:none">
      {% include chord_uk.html %}
    </div>
  </div>
  <div class="col-sm-12 col-md-3" style="position: absolute;left: 800pt;">
    <p>
      This chord plot provides a general overview about how food could be redistributed with minimal expenditures. When hovering over a country's circle, its associated food flows will be highlighted. By selecting a specific country in the drop menu, you can reduce complexity and assess where this particular nation's food is meant to be allocated. Note that the total amount of food sent/received corresponds to the extension of a country's circular arc. 
      Germany and France were found to contribute the most, with each providing slightly more than 100,000 tons. This is mainly due to their higher GDP. On the other end, it's trivial to see that Ethiopia would claim the highest share of food aid of all examined countries.
    </p>
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>


<!-- </script> -->

<script>
$(document).ready(function() {

  $(".bk-toolbar").parent().css('backgroundColor', '#f8f8f8');
  active_chord = "#Europe_chord";
  $(active_chord).show();
  $('#chord_countries').change(function(){

    $(active_chord).hide();
    active_chord = "#".concat($('#chord_countries').val(), "_chord");
    $(active_chord).show();
    
  })
});
</script>
