// star slider 

// $( function() {
//     var minStarInput = $( "#min-star" );
//     var maxStarInput = $( "#max-star" );

//     $( "#slider-star" ).slider({
//         range: true,
//         min: 0,
//         max: 10,
//         step: 0.1,
//         values: [ 0, 10 ],
//         type: "GET",
//         slide: function( event, ui ) {
//         minStarInput.val( ui.values[ 0 ] );
//         maxStarInput.val( ui.values[ 1 ] );
//         }
//     });

//     minStarInput.on( "input", function() {
//         var minStar = $( this ).val();
//         var maxStar = parseFloat( maxStarInput.val() );

//         if ( minStar && ( minStar >= 0 && minStar <= 10 ) && (!maxStar || minStar <= maxStar ) ) {
//         $( "#slider-star" ).slider( "values", 0, minStar );
//         }
//     });

//     maxStarInput.on( "input", function() {
//         var minStar = parseFloat( minStarInput.val() );
//         var maxStar = $( this ).val();

//         if ( maxStar && ( maxStar >= 0 && maxStar <= 10 ) && (!minStar || minStar <= maxStar ) ) {
//         $( "#slider-star" ).slider( "values", 1, maxStar );
//         }
//     });
// } );
//



// ar slider 
// $( function() {
//     var minArInput = $( "#min-ar" );
//     var maxArInput = $( "#max-ar" );
  
//     $( "#slider-ar" ).slider({
//       range: true,
//       min: 0,
//       max: 10,
//       step: 0.1,
//       values: [ 0, 10 ],
//       type: "GET",
//       slide: function( event, ui ) {
//         minArInput.val( ui.values[ 0 ] );
//         maxArInput.val( ui.values[ 1 ] );
//       }
//     });
  
//     minArInput.on( "input", function() {
//       var minAr = $( this ).val();
//       var maxAr = parseFloat( maxArInput.val() );
  
//       if ( minAr && ( minAr >= 0 && minAr <= 10 ) && (!maxAr || minAr <= maxAr ) ) {
//         $( "#slider-ar" ).slider( "values", 0, minAr );
//       }
//     });
  
//     maxArInput.on( "input", function() {
//       var minAr = parseFloat( minArInput.val() );
//       var maxAr = $( this ).val();
  
//       if ( maxAr && ( maxAr >= 0 && maxAr <= 10 ) && (!minAr || minAr <= maxAr ) ) {
//         $( "#slider-ar" ).slider( "values", 1, maxAr );
//       }
//     });
//   } );
// // 

// // od slider 
// $( function() { var minOdInput = $( "#min-od" ); var maxOdInput = $( "#max-od" );
//   $( "#slider-od" ).slider({
//     range: true,
//     min: 0,
//     max: 10,
//     step: 0.1,
//     values: [ 0, 10 ],
//     type: "GET",
//     slide: function( event, ui ) {
//       minOdInput.val( ui.values[ 0 ] );
//       maxOdInput.val( ui.values[ 1 ] );
//     }
//   });

//   minOdInput.on( "input", function() {
//     var minOd = $( this ).val();
//     var maxOd = parseFloat( maxOdInput.val() );

//     if ( minOd && ( minOd >= 0 && minOd <= 10 ) && (!maxOd || minOd <= maxOd ) ) {
//       $( "#slider-od" ).slider( "values", 0, minOd );
//     }
//   });

//   maxOdInput.on( "input", function() {
//     var minOd = parseFloat( minOdInput.val() );
//     var maxOd = $( this ).val();

//     if ( maxOd && ( maxOd >= 0 && maxOd <= 10 ) && (!minOd || minOd <= maxOd ) ) {
//       $( "#slider-od" ).slider( "values", 1, maxOd );
//     }
//   });

//   } );
// //


// // cs slider 
// $( function() { var minCsInput = $( "#min-cs" ); var maxCsInput = $( "#max-cs" );

//   $( "#slider-cs" ).slider({
//     range: true,
//     min: 0,
//     max: 10,
//     step: 0.1,
//     values: [ 0, 10 ],
//     type: "GET",
//     slide: function( event, ui ) {
//       minCsInput.val( ui.values[ 0 ] );
//       maxCsInput.val( ui.values[ 1 ] );
//     }
//   });

//   minCsInput.on( "input", function() {
//     var minCs = $( this ).val();
//     var maxCs = parseFloat( maxCsInput.val() );

//     if ( minCs && ( minCs >= 0 && minCs <= 10 ) && (!maxCs || minCs <= maxCs ) ) {
//       $( "#slider-cs" ).slider( "values", 0, minCs );
//     }
//   });

//   maxCsInput.on( "input", function() {
//     var minCs = parseFloat( minCsInput.val() );
//     var maxCs = $( this ).val();

//     if ( maxCs && ( maxCs >= 0 && maxCs <= 10 ) && (!minCs || minCs <= maxCs ) ) {
//       $( "#slider-cs" ).slider( "values", 1, maxCs );
//     }
//   });

//   } ); 
// //


// // hp slider 
// $( function() { var minHpInput = $( "#min-hp" ); var maxHpInput = $( "#max-hp" );

//   $( "#slider-hp" ).slider({
//     range: true,
//     min: 0,
//     max: 10,
//     step: 0.1,
//     values: [ 0, 10 ],
//     type: "GET",
//     slide: function( event, ui ) {
//       minHpInput.val( ui.values[ 0 ] );
//       maxHpInput.val( ui.values[ 1 ] );
//     }
//   });

//   minHpInput.on( "input", function() {
//     var minHp = $( this ).val();
//     var maxHp = parseFloat( maxHpInput.val() );

//     if ( minHp && ( minHp >= 0 && minHp <= 10 ) && (!maxHp || minHp <= maxHp ) ) {
//       $( "#slider-hp" ).slider( "values", 0, minHp );
//     }
//   });

//   maxHpInput.on( "input", function() {
//     var minHp = parseFloat( minHpInput.val() );
//     var maxHp = $( this ).val();

//     if ( maxHp && ( maxHp >= 0 && maxHp <= 10 ) && (!minHp || minHp <= maxHp ) ) {
//       $( "#slider-hp" ).slider( "values", 1, maxHp );
//     }
//   });

//   } ); 
  
//////////////////////////////////////////////
// star slider 
$(document).ready(function() {
  // Set up slider with initial values from input fields
  var slider = $("#slider-star").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-star").val(), $("#max-star").val()],
    slide: function(event, ui) {
      // Update input fields while sliding
      $("#min-star").val(ui.values[0]);
      $("#max-star").val(ui.values[1]);
    }
  });

  // Update slider values before submitting the form
  $("#myForm").submit(function() {
    // Update slider values from input fields
    slider.slider("values", 0, $("#min-star").val());
    slider.slider("values", 1, $("#max-star").val());
  });
});




// ar slider 
$(document).ready(function() {
  // Set up slider with initial values from input fields
  var slider = $("#slider-ar").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-ar").val(), $("#max-ar").val()],
    slide: function(event, ui) {
      // Update input fields while sliding
      $("#min-ar").val(ui.values[0]);
      $("#max-ar").val(ui.values[1]);
    }
  });

  $("#myForm").submit(function() {
    // Update slider values from input fields
    slider.slider("values", 0, $("#min-ar").val());
    slider.slider("values", 1, $("#max-ar").val());
  });
}); 



// od slider 
$(document).ready(function() {
  // Set up slider with initial values from input fields
  var slider = $("#slider-od").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-od").val(), $("#max-od").val()],
    slide: function(event, ui) {
      // Update input fields while sliding
      $("#min-od").val(ui.values[0]);
      $("#max-od").val(ui.values[1]);
    }
  });

  // Update slider values before submitting the form
  $("#myForm").submit(function() {
    // Update slider values from input fields
    slider.slider("values", 0, $("#min-od").val());
    slider.slider("values", 1, $("#max-od").val());
  });
});






// cs slider 
$(document).ready(function() {
  // Set up slider with initial values from input fields
  var slider = $("#slider-cs").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-cs").val(), $("#max-cs").val()],
    slide: function(event, ui) {
      // Update input fields while sliding
      $("#min-cs").val(ui.values[0]);
      $("#max-cs").val(ui.values[1]);
    }
  });

  // Update slider values before submitting the form
  $("#myForm").submit(function() {
    // Update slider values from input fields
    slider.slider("values", 0, $("#min-cs").val());
    slider.slider("values", 1, $("#max-cs").val());
  });
});


// hp slider 
$(document).ready(function() {
  // Set up slider with initial values from input fields
  var slider = $("#slider-hp").slider({
    range: true,
    min: 0,
    max: 10,
    step: 0.1,
    type: "GET",
    values: [$("#min-hp").val(), $("#max-hp").val()],
    slide: function(event, ui) {
      // Update input fields while sliding
      $("#min-hp").val(ui.values[0]);
      $("#max-hp").val(ui.values[1]);
    }
  });

  // Update slider values before submitting the form
  $("#myForm").submit(function() {
    // Update slider values from input fields
    slider.slider("values", 0, $("#min-hp").val());
    slider.slider("values", 1, $("#max-hp").val());
  });
});
