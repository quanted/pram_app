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
            chemical_name: {
                required: true,
            },
            pc_code: {
                required : true,
            },
            use: {
                required: true,
            },
            application_method: {
                required: true,
            },
            application_form: {
                required: true,
            },
            solubility: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            application_rate: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            EC25_for_nonlisted_seedling_emergence_monocot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            EC25_for_nonlisted_seedling_emergence_dicot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            NOAEC_for_listed_seedling_emergence_monocot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            NOAEC_for_listed_seedling_emergence_dicot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            EC25_for_nonlisted_vegetative_vigor_monocot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            EC25_for_nonlisted_vegetative_vigor_dicot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            NOAEC_for_listed_vegetative_vigor_monocot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
            NOAEC_for_listed_vegetative_vigor_dicot: {
                required: true,
                sciFormat: true,
                positiveNumber: true
            },
        }
    });

});