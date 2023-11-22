// star slider 
$(document).ready(function() {
  var slider = $("#slider-star").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-star").val(), $("#max-star").val()],
    slide: function(event, ui) {
      $("#min-star").val(ui.values[0]);
      $("#max-star").val(ui.values[1]);
    }
  });

  $("#myForm").submit(function() {
    slider.slider("values", 0, $("#min-star").val());
    slider.slider("values", 1, $("#max-star").val());
  });
});


// ar slider 
$(document).ready(function() {
  var slider = $("#slider-ar").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-ar").val(), $("#max-ar").val()],
    slide: function(event, ui) {
      $("#min-ar").val(ui.values[0]);
      $("#max-ar").val(ui.values[1]);
    }
  });

  $("#myForm").submit(function() {
    slider.slider("values", 0, $("#min-ar").val());
    slider.slider("values", 1, $("#max-ar").val());
  });
}); 


// od slider 
$(document).ready(function() {
  var slider = $("#slider-od").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-od").val(), $("#max-od").val()],
    slide: function(event, ui) {
      $("#min-od").val(ui.values[0]);
      $("#max-od").val(ui.values[1]);
    }
  });

  $("#myForm").submit(function() {
    slider.slider("values", 0, $("#min-od").val());
    slider.slider("values", 1, $("#max-od").val());
  });
});


// cs slider 
$(document).ready(function() {
  var slider = $("#slider-cs").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-cs").val(), $("#max-cs").val()],
    slide: function(event, ui) {
      $("#min-cs").val(ui.values[0]);
      $("#max-cs").val(ui.values[1]);
    }
  });

  $("#myForm").submit(function() {
    slider.slider("values", 0, $("#min-cs").val());
    slider.slider("values", 1, $("#max-cs").val());
  });
});


// hp slider 
$(document).ready(function() {
  var slider = $("#slider-hp").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-hp").val(), $("#max-hp").val()],
    slide: function(event, ui) {
      $("#min-hp").val(ui.values[0]);
      $("#max-hp").val(ui.values[1]);
    }
  });

  $("#myForm").submit(function() {
    slider.slider("values", 0, $("#min-hp").val());
    slider.slider("values", 1, $("#max-hp").val());
  });
});


 