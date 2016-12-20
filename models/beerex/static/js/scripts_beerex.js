$(document).ready(function() {
  
    // Add 'dividers' between table sections
    $('#id_log_kow, #id_adult_contact_ld50, #id_empirical_residue, #id_lw1_jelly').closest('tr').before('<tr><td colspan="2"></td></tr>');
    // Default 'readonly' inputs
    $('#id_log_kow, #id_koc, #id_mass_tree_vegetation, #id_empirical_pollen, #id_empirical_nectar, #id_empirical_jelly').prop('readonly', true);
    // onChange functions
    $('#id_application_method').change(function() {
        if ($(this).val() == "soil application"){
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