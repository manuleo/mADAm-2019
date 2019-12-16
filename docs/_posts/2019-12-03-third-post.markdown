---
layout: default
id_div: third_section
img: |
category: |
title: Third Try
description: |
---
### A second test with Vega
<div class="row">
  <div id="france-selector" class="col-sm-2 select-country vcenter">
    <img id="france-logo" class="svg" src="france_shape.svg" width="300px" height="300px"/>
    <p style="color:blue" class="country-name">France</p>
  </div>
</div>
<div id="toshow" class="row" style="display:none">
  Some text...
</div>

<script>

$("#france-selector").click(function() {
  $("#toshow").show();
});

</script>