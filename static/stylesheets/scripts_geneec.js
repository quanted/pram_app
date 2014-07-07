$(document).ready(function() {

	//Input form validation method
    function isSci(txtValue) {
        var currVal = txtValue;
        if (currVal == '') {
           return false;
        }
        //Declare Regex  
        var rxNumberPattern = /^-?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?/;
        var dtArray = currVal.match(rxNumberPattern); // is format OK?
        if (dtArray == null) {
            return false;
        }
    return true;
    }

    $.validator.addMethod(
        "sciFormat",
        function (value, element) {
            return isSci(value)
        },
        "Wrong numeric format"
    );

    $.validator.addMethod('positiveNumber',
        function(value) {
            return Number(value) > 0;
        }, 'Positive number');

	$.validator.messages.required = 'Required';
                  
    var validator = $('form').validate({
        errorElement: "div",
        wrapper: "div",  // a wrapper around the error message
        ignore: 'input[type="button"],input[type="submit"]',
        rules: {
            application_rate: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            number_of_applications: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            interval_between_applications: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            Koc: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            aerobic_soil_metabolism: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            application_method: {
                required: true,
            },
            no_spray_drift: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            incorporation_depth: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            solubility: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            aerobic_aquatic_metabolism: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            hydrolysis: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            photolysis_aquatic_half_life: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
        }
    });

});