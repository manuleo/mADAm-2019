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
   For every European countries out of the five selected, domestic prices for specific items are found to be fairly different. In this context, the natural way to go is to redistribute food in the most economic-advantageous way as the goal of the project is not to penalize European countries for their food waste but rather create the condition for a <b>win-win scenario</b>. Consequently, a cost minimization is carried out using optimization methods (if interested, check out the <a href="#6_section" target="_blank">appendix</a>). Furthermore, a linearly increasing cost function with respect to the GDP is implemented yielding a higher cost if only one country was considered while also prefering to take from richer countries.
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
      This chord plot provides a general overview about how food could be redistributed with minimal expenditures. When hovering over a country's circle, its associated food flows will be highlighted. By selecting a specific country in the drop menu, you can reduce complexity and assess where this particular nation's food is meant to be allocated. <i>Note that the total amount of food sent/received corresponds to the extension of a country's circular arc.</i> 
      <i>Germany</i> and <i>France</i> were found to contribute the most, with each providing slightly more than 100,000 tons. This is mainly due to their higher GDP. In contrapposition, <i>Italy</i> and <i>Spain</i> are found to contribute the least and this again confirms the goodness of our hypothesis. It is trivial to see that Ethiopia would claim the highest share of food aid (1.3*10<sup>5</sup>tons) of all examined countries. Considering that a regular Ethiopian person is estimated to lack 125 kcal every day, the intermediate result is quite promising as it indicates that the extent of population is correctly taken into account.
    </p>
  </div>
  <div class="col-sm-12 col-md-2"></div>
</div>

<br/>

<div class="row">
  <div class="col-sm-12 col-md-2"></div>
  <div class="col-sm-12 col-md-3">
  In a final step, we move to a detailed view of what amount of each specific product should be shipped to every individual African country. By clicking on an individual country, its food to be received will be displayed. The products <b>Beef, Meat, Chicken, Oat and Tomatoes</b> are required the most in all countries in need. This can be explained by the fact that - compared to the other items - they have a lower cost per kcal of energy. Meat is used that much due to its high content in valuable proteins and fat, which other food items are mostly lacking. The respective shares of food aid are similar for all African countries, as their deficit was assumed to be comprised of the same lack of carbohydrates, fat and protein. 
  </div>
  <div class="col-sm-12 col-md-1" style="z-index:10; left: 40px; position: relative;">
    <select id="sun_countries">
      <option value="Europe" selected>All Europe</option>
      <option value="France">France</option>
      <option value="Germany">Germany</option>
      <option value="Italy">Italy</option>
      <option value="Spain">Spain</option>
      <option value="UK">United Kingdom</option>
    </select>
  </div>
  <div class="col-sm-12 col-md-4" id="sun_box">
    <div id="Europe_sun" style="display:none">
      {% include sunburst_EU.html %}
    </div>
    <div id="France_sun" style="display:none">
      {% include sunburst_fr.html %}
    </div>
    <div id="Germany_sun" style="display:none">
      {% include sunburst_ge.html %}
    </div>
    <div id="Italy_sun" style="display:none">
      {% include sunburst_it.html %}
    </div>
    <div id="Spain_sun" style="display:none">
      {% include sunburst_sp.html %}
    </div>
    <div id="UK_sun" style="display:none">
      {% include sunburst_uk.html %}
    </div>
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

  active_sun = "#Europe_sun";
  $(active_sun).show();
  $('#sun_countries').change(function(){

    $(active_sun).hide();
    active_sun = "#".concat($('#sun_countries').val(), "_sun");
    $(active_sun).show();
    
  })

});
</script>
