$(document).ready(function() {
  
    // Add 'dividers' between table sections
    $('#id_chemical_name, #id_ld50_mammal_water, #id_noael_mammal_water, #id_ld50_avian_water, #id_noaec_duck').closest('tr').before('<tr><td colspan="2"></td></tr>');
    // Default 'readonly' inputs
    $('#id_bodyweight_tested_mammal, #id_noael_bodyweight_tested_mammal, #id_bodyweight_tested_bird').prop('readonly', true);
    // onChange functions
    $('#id_ld50_species_tested_mammal').change(function() {
        if ($(this).val() == "350"){
            $('#id_bodyweight_tested_mammal').prop('readonly', true).val('350');
        }
        else{
           $('#id_bodyweight_tested_mammal').prop('readonly', false);
        }
    });
    $('#id_noael_species_tested_mammal').change(function() {
        if ($(this).val() == "350"){
            $('#id_noael_bodyweight_tested_mammal').prop('readonly', true).val('350');
        }
        else{
           $('#id_noael_bodyweight_tested_mammal').prop('readonly', false);
        }
    });
    $('#id_species_tested_bird').change(function() {
        if ($(this).val() == "178"){
            $('#id_bodyweight_tested_bird').prop('readonly', true).val('178');
        }
        else if ($(this).val() == "1580"){
            $('#id_bodyweight_tested_bird').prop('readonly', true).val('1580');
        }
        else{
           $('#id_bodyweight_tested_bird').prop('readonly', false);
        }
    });

});