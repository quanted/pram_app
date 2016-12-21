$(document).ready(function() {
  
    // Add 'dividers' between table sections
    $('#id_log_kow, #id_adult_contact_ld50, #id_empirical_residue, #id_lw1_jelly').closest('tr').before('<tr><td colspan="2"></td></tr>');

    // onChange functions
    $('#id_application_method').change(function() {

        if ($(this).val() == "soil application") {
            $('#id_log_kow').show();
            $('#id_koc').show();
        }
        else {
            $('#id_log_kow').hide();
            $('#id_koc').hide();
        }


        if ($(this).val() == "tree trunk"){
            $('#id_mass_tree_vegetation').show();
        }
        else{
            $('#id_mass_tree_vegetation').hide();
        }
    });


    $('#id_empirical_residue').change(function() {
        if ($(this).val() == "yes"){
            $('#id_empirical_pollen').show();
            $('#id_empirical_nectar').show();
            $('#id_empirical_jelly').show();
        }
        else{
            $('#id_empirical_pollen').hide();
            $('#id_empirical_nectar').hide();
            $('#id_empirical_jelly').hide();
        }
    });

});