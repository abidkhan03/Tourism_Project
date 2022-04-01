// Director field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".director-input-field"); //Fields wrapper
    var add_button = $(".add-director-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"> <div class="col-3 my-2"> <label class="form-label">Name</label>  <input type="text" class="form-control" name=""/></div>  <div class="col-3 my-2"> <label class="form-label">Address</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Year Of Experiance</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Qualification</label>  <input type="text" class="form-control" name=""/></div> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// Manager field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".manager-input-field"); //Fields wrapper
    var add_button = $(".add-manager-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"> <div class="col-3 my-2"> <label class="form-label">Name</label>  <input type="text" class="form-control" name=""/></div>  <div class="col-3 my-2"> <label class="form-label">Address</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Year Of Experiance</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Qualification</label>  <input type="text" class="form-control" name=""/></div> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// Partner field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".partner-input-field"); //Fields wrapper
    var add_button = $(".add-partner-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"> <div class="col-3 my-2"> <label class="form-label">Name</label>  <input type="text" class="form-control" name=""/></div>  <div class="col-3 my-2"> <label class="form-label">Address</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Year Of Experiance</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Qualification</label>  <input type="text" class="form-control" name=""/></div> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// owner field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".owner-input-field"); //Fields wrapper
    var add_button = $(".add-owner-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row">  <div class="col-lg-4 col-md-6 my-2"> <label for="" class="form-label">Name of Owner:</label> <input type="text" class="form-control" /> </div><div class="col-lg-2 col-md-6 my-2"><label for="" class="form-label">Owner % :</label><input type="text" class="form-control" /></div> <div class="col-lg-6 col-md-12 my-2"><label for="" class="form-label">Full Address of Owner:</label><input type="text" class="form-control" /></div><div class="col-lg-6 col-md-12 my-2"><label for="" class="form-label">Telegraphic Address of Owner:</label><input type="text" class="form-control" /> </div><div class="col-lg-3 col-md-6 my-2"> <label for="" class="form-label">Owner Telephone Number:</label> <input type="text" class="form-control" /></div><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// Hotel Manager field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".hotelManager-input-field"); //Fields wrapper
    var add_button = $(".add-hotelManager-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-4 col-md-6 my-2"> <label for="" class="form-label">Name of Manager:</label> <input type="text" class="form-control" /> </div> <div class="col-lg-2 col-md-6 my-2 text-nowrap"> <label for="" class="form-label">Manager % :</label> <input type="text" class="form-control" />  </div> <div class="col-lg-6 col-md-12 my-2"> <label for="" class="form-label">Manager Adress:</label> <input type="text" class="form-control" />  </div> <div class="col-lg-3 col-md-12 my-2"><label for="" class="form-label">Manager Telephone Number:</label><input type="text" class="form-control" /></div><a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// dining hall field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".diningHall-input-field"); //Fields wrapper
    var add_button = $(".add-diningHall-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// kitchen  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".kitchen-input-field"); //Fields wrapper
    var add_button = $(".add-kitchen-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// hotel Furniture and fixture forms addition

// bedroom  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".bedRoom-input-field"); //Fields wrapper
    var add_button = $(".add-bedRoom-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// common room  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".commonRoom-input-field"); //Fields wrapper
    var add_button = $(".add-commonRoom-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});

// corridors and Galleries  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".corridorsGallery-input-field"); //Fields wrapper
    var add_button = $(".add-corridorsGallery-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});

// bathrooms  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".bathrooms-input-field"); //Fields wrapper
    var add_button = $(".add-bathrooms-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});

// commonbathrooms  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".commonbathrooms-input-field"); //Fields wrapper
    var add_button = $(".add-commonbathrooms-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// commontoilets  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".commontoilets-input-field"); //Fields wrapper
    var add_button = $(".add-commontoilets-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-12 my-2"> <label for="" class="form-label">Furniture Type:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// cuisineServed  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".cuisineServed-input-field"); //Fields wrapper
    var add_button = $(".add-cuisineServed-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="col-lg-4 col-md-6 my-2"> <label for="" class="form-label"> Cuisine Name:</label> <input type="text" class="form-control" /> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// common bathrooms number  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".bathroomNo-input-field"); //Fields wrapper
    var add_button = $(".add-bathroomNo-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-md-6 my-2"> <label for="" class="form-label">Common Bathroom No. :</label> <input type="text" class="form-control" /> </div> <div class="col-md-6 my-2"> <label for="" class="form-label"> Floor No.:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});

// common toilet number  field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".toiletNo-input-field"); //Fields wrapper
    var add_button = $(".add-toiletNo-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-md-6 my-2"> <label for="" class="form-label"> Common Toilet No. :</label> <input type="text" class="form-control" /> </div> <div class="col-md-6 my-2"> <label for="" class="form-label"> Floor No.:</label> <input type="text" class="form-control" /> </div> <a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});