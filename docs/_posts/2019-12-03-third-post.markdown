---
layout: default
id_div: third_section
img: |
category: |
title: Our solution
description: |
---

<div class="row">
  <div class="col-sm-1"></div>
  <div class="col-sm-4">
    <h3>The perfect diet</h3>
    Now, the exchange of calories is known. However, in what form should it be delivered? To reach a concrete and tangible recommendation on how to solve this issue, this is an essential question. For a well-balanced diet, a share of 55% carbohydrates, 25% proteins and 20% fat is recommended <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1479724/">recommended</a>. Secondly, products of varying food groups should be included. To this end, categories such as “Dairy and Egg Products” and “Legumes and Legume Products” were analyzed and searched to get the one product which most correctly fulfils the defined share. This would then be used as a representative product for its food category. By hovering over a data point, you will see the product's name and its composition of the three macronutrients projected onto the corresponding axis. 
  </div>
  <div class="col-sm-6">
    {% include 3d_macros.html %}
  </div>
  <div class="col-sm-1"></div>
</div>

<br/>

<div class="row">
  <div class="col-sm-1"></div>
  <div class="col-sm-10">
    <h3>The distribution plan</h3>
   For every European countries out of the five selected, the prices for the previously defined food items were determined (https://ec.europa.eu/info/food-farming-fisheries/farming/facts-and-figures/markets/prices/price-monitoring-sector/eu-prices-selected-representative-products_en) and (http://www.fao.org/faostat/en/#data/PP). As different countries have different domestic prices for specific items, a 
  </div>
  <div class="col-sm-1"></div>
</div>

<br/>

<div class="row">
  <div class="col-sm-1"></div>
  <div class="col-sm-1">
    <select id="chord_countries">
      <option value="Europe" selected>All Europe</option>
      <option value="France">France</option>
      <option value="Germany">Germany</option>
      <option value="Italy">Italy</option>
      <option value="Spain">Spain</option>
      <option value="UK">United Kingdom</option>
    </select>
  </div>
  <div class="col-sm-5" id="chord_box">
    <div id="Europe_chord">
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
  <div class="col-sm-3">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fermentum sit amet sapien sed lacinia. Pellentesque venenatis sem ornare, ornare tortor eu, vehicula leo. Integer congue vehicula tortor, eleifend placerat orci gravida aliquam. Duis tincidunt mi non massa tempor, ornare consectetur diam congue. Curabitur sit amet eleifend magna, vitae volutpat lacus. Praesent luctus libero tempus nisl ullamcorper tempus. Ut eros felis, porttitor a urna eu, placerat sodales tortor. In hac habitasse platea dictumst. Cras bibendum sem eu scelerisque rutrum. Maecenas sollicitudin dui id sapien interdum fermentum. Pellentesque ac convallis nibh, id lacinia lectus. </p>
  </div>
  <div class="col-sm-1"></div>
</div>


<!-- </script> -->

<script>
$(document).ready(function() {

  $(".bk-toolbar").parent().css('backgroundColor', '#f8f8f8');
  active_chord = "#Europe_chord";
  $('#chord_countries').change(function(){

    $(active_chord).hide();
    active_chord = "#".concat($('#chord_countries').val(), "_chord");
    $(active_chord).show();
    
  })
});
</script>
