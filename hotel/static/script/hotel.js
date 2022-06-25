$(document).ready(function () {
    // $("#save_btn").hide();
    let x = 0;

    $("#add_owner").click(function (e) {
        e.preventDefault();
        console.log("add-button clicked");
        appendRowOwner();
        x++;
        // $("#save_btn").show();
    
    });

    $("#input_owner").on("click", ".deleteBtn", function (e) {
        e.preventDefault();
        let id = e.currentTarget.id;
        $('div[id='+id+']').remove();
        x--;
        // if(x === 0){
        //     $("#save_btn").hide();
        // }
    });

    // add manager button to increase the number of manager
    $("#add_manager").click(function (e) {
        e.preventDefault();
        console.log("add manager button clicked")
        appendRowManager();
        x++;
        // $("#save_btn").show();
    });

    $("#input_manager").on("click", ".deleteBtn", function (e) {
        e.preventDefault();
        let id = e.currentTarget.id;
        $('div[id='+id+']').remove();
        x--;
        // if(x === 0){
        //     $("#save_btn").hide();
        // }
    });

    // add bathrooms button to increase the number of bathrooms
    $("#add_bathroom").click(function (e) {
        e.preventDefault();
        appendRowBathroom();
        x++;
        // $("#save_btn").show();
    });

    $("#input_bathroom").on("click", ".deleteBtn", function (e) {
        e.preventDefault();
        let id = e.currentTarget.id;
        $('div[id='+id+']').remove();
        x--;
    });

    // add toilets button to increase the number of toilets
    $("#add_toilet").click(function (e) {
        e.preventDefault();
        appendRowToilet();
        x++;
        // $("#save_btn").show();
    });

    $("#input_toilet").on("click", ".deleteBtn", function (e) {
        e.preventDefault();
        let id = e.currentTarget.id;
        $('div[id='+id+']').remove();
        x--;
    });

// save button to save the form data to the database
$("#save_btn").click(function (e) {
    e.preventDefault();
    console.log("save button clicked");
    let formData = new FormData(document.querySelector('#test_form'));

    // create an object for the form data
    let form = {
        hotel_name : formData.get('hotel-name'),    
        establishment_year :formData.get('establishment-year'),
        commission_date :formData.get('commission-date'),
        telex_number :formData.get('telex-number'),
        telephone_no :formData.get('telephone-no'),
        hotel_address :formData.get('hotel-address'),
        telegraph_address :formData.get('telegraph-address'),
        province :formData.get('province'),
        town :formData.get('town'),
        street_no :formData.get('street-no'),
        ownership_nature :formData.get('ownership-nature'),

        owners : [],
        managers : [], 
        bathrooms : [],
        toilets : []
    };


    
    for(let i = 0; i < formData.getAll('ownerName[]').length; ++i) {

        form.owners.push({
            name : formData.getAll('ownerName[]')[i],
            ratio : formData.getAll('ownerRatio[]')[i],
            address : formData.getAll('ownerAddress[]')[i],
            telephone : formData.getAll('ownerTelephoneNo[]')[i],
            telegraph : formData.getAll('ownerTelegraphAddress[]')[i],
        });
    }

    for(let j = 0; j < formData.getAll('managerName[]').length; ++j){
        form.managers.push({
            managerName : formData.getAll('managerName[]')[j],
            managerRatio : formData.getAll('managerRatio[]')[j],
            managerAddress : formData.getAll('managerAddress[]')[j],
            managerTelephone : formData.getAll('managerTelephoneNo[]')[j],
        });
    }

    for(let i = 0; i < formData.getAll('commonBathroomNo[]').length; ++i) {

        form.bathrooms.push({
            bath_No : formData.getAll('commonBathroomNo[]')[i],
            floor_No : formData.getAll('bathroomFloorNo[]')[i],
        });
    }

    for(let i = 0; i < formData.getAll('commonToiletNo[]').length; ++i) {
            
            form.toilets.push({
                toilet_No : formData.getAll('commonToiletNo[]')[i],
                floor_No : formData.getAll('toiletFloorNo[]')[i],
            });
    }

    $.ajax({
        type: 'POST',
        url: window.state.hotel_form_url,
        headers: {'X-CSRFToken': window.state.token},
        data: JSON.stringify(form),
        success: function (data) {
            data.status == 1 ? alert("Data Submitted successfully") : alert("Data Submission failed"); 
        }
    });

});

    function appendRowOwner() {
        $("#input_owner").append(

            '<div id="'+x+'" class="col-md-12 my-2">'+
                '<div id="'+x+'" class="">'+
                    '<label id="'+x+'" for="" class="form-label">Fill the Information of Number of Owners you have</label>'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="form-group col-lg-4 col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Name of Owner:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="ownerName[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-2 col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Owner % :</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="ownerRatio[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-6 col-md-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Full Address of Owner:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="ownerAddress[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-6 col-md-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Telegraphic Address of Owner:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="ownerTelegraphAddress[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-3 col-md-6 my-2">'+
                            '<label for="" class="form-label">Owner Telephone Number:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="ownerTelephoneNo[]" />'+
                        '</div>'+
                        '<div id="'+x+'" class="form-group">'+
                            '<div id="'+x+'" class="col-sm-10">'+
                                '<button id="'+x+'" class="btn btn-danger deleteBtn">Remove</button>'+
                            '</div id="'+x+'">'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                '</div id="'+x+'">'+
            '</div id="'+x+'">'
        );
    }

    function appendRowManager() {
        $("#input_manager").append(

            '<div id="'+x+'" class="col-md-12 my-2">'+
                '<div id="'+x+'" class="">'+
                    '<label id="'+x+'" for="" class="form-label">Fill the Information of Number of Managers you have</label>'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="form-group col-lg-4 col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Name of Manager:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="managerName[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-2 col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Manager % :</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="managerRatio[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-6 col-md-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Full Address of Manager:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="managerAddress[]" />'+
                        '</div id="'+x+'">'+

                        '<div id="'+x+'" class="form-group col-lg-3 col-md-6 my-2">'+
                            '<label for="" class="form-label">Manager Telephone Number:</label>'+

                            '<input id="'+x+'" type="text" class="form-control" name="managerTelephoneNo[]" />'+
                        '</div>'+
                        '<div id="'+x+'" class="form-group">'+
                            '<div id="'+x+'" class="col-sm-10">'+
                                '<button id="'+x+'" class="btn btn-danger deleteBtn">Remove</button>'+
                            '</div id="'+x+'">'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                '</div id="'+x+'">'+
            '</div id="'+x+'">'
        );
    };

    function appendRowBathroom() {
        $("#input_bathroom").append(
            '<div id="'+x+'" class="col-md-12 my-2">'+
                '<div id="'+x+'" class="bathroomNo-input-field">'+
                    '<label id="'+x+'" for="" class="form-label">Give the Number of Common Bathroom with Floor Numbers</label>'  +
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Common Bathroom No.:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="commonBathroomNo[]" />'+
                        '</div id="'+x+'">'+
                        '<div id="'+x+'" class="col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Floor No.:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="bathroomFloorNo[]" />'+
                        '</div id="'+x+'">'+
                        '<div id="'+x+'" class="form-group">'+
                            '<div id="'+x+'" class="col-sm-10">'+
                                '<button id="'+x+'" class="btn btn-danger deleteBtn">Remove</button>'+
                            '</div id="'+x+'">'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                '</div id="'+x+'">'+
            '</div id="'+x+'">'
        );
    }

    function appendRowToilet() {
        $("#input_toilet").append(
            '<div id="'+x+'" class="col-md-12 my-2">'+
                '<div id="'+x+'" class="toiletNo-input-field">'+
                    '<label id="'+x+'" for="" class="form-label">Give the Number of Common Toilets with Floor Numbers</label>'  +
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Common Toilet No.:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="commonToiletNo[]" />'+
                        '</div id="'+x+'">'+
                        '<div id="'+x+'" class="col-md-6 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Floor No.:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="toiletFloorNo[]" />'+
                        '</div id="'+x+'">'+
                        '<div id="'+x+'" class="form-group">'+
                            '<div id="'+x+'" class="col-sm-10">'+
                                '<button id="'+x+'" class="btn btn-danger deleteBtn">Remove</button>'+
                            '</div id="'+x+'">'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                '</div id="'+x+'">'+
            '</div id="'+x+'">'
        );
    }

    function appendRowFurniture(){
        $("#input_furniture").append(
            '<div id="'+x+'" class="col-md-12 my-2">'+
                '<div id="'+x+'" class="bedRoom-input-field">'+
                    '<label id="'+x+'" for="" class="form-label">Give the Information of Furniture</label>'  +
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-lg-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Bedrooms Furniture Type:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="bedroom-type" />'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-lg-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Common Rooms Furniture Type:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="room-type" />'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-lg-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Corridors & Galleries Furniture Type:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="room-type" />'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-lg-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Attached Bathrooms Furniture Type:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="attachedBathroom[]" />'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-lg-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Common Bathrooms Furniture Type:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="commonBathroom[]" />'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+
                    '<div id="'+x+'" class="row">'+
                        '<div id="'+x+'" class="col-lg-12 my-2">'+
                            '<label id="'+x+'" for="" class="form-label">Common Toilets Furniture Type:</label>'+
                            '<input id="'+x+'" type="text" class="form-control" name="commonToilet[]" />'+
                        '</div id="'+x+'">'+
                    '</div id="'+x+'">'+

                '</div id="'+x+'">'+
            '</div id="'+x+'">'
        );
    }
});
