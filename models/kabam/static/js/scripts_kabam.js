$(document).ready(function() {
    // Call function to setup tabbed nav
    uberNavTabs(
        ["Chemical", "Avian", "Mammal", "LargeFish", "MediumFish", "SmallFish", "Filterfeeders", "Invertebrates", "Zooplankton", "Phytoplankton", "Sediment", "Constants"],
        {   "isSubTabs":false  }
    );

    $('#id_phytoplankton_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_phytoplankton_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_phytoplankton_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_phytoplankton_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_phytoplankton_km').closest('tr').addClass('method_options').hide();
    $('#id_phytoplankton_kg').closest('tr').addClass('method_options').hide();
    $('#id_zoo_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_zoo_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_zoo_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_zoo_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_zoo_km').closest('tr').addClass('method_options').hide();
    $('#id_beninv_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_beninv_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_beninv_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_beninv_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_beninv_km').closest('tr').addClass('method_options').hide();
    $('#id_filterfeeders_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_filterfeeders_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_filterfeeders_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_filterfeeders_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_filterfeeders_km').closest('tr').addClass('method_options').hide();
    $('#id_sfish_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_sfish_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_sfish_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_sfish_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_sfish_km').closest('tr').addClass('method_options').hide();
    $('#id_mfish_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_mfish_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_mfish_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_mfish_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_mfish_km').closest('tr').addClass('method_options').hide();
    $('#id_lfish_k1_temp').closest('tr').addClass('method_options').hide();
    $('#id_lfish_k2_temp').closest('tr').addClass('method_options').hide();
    $('#id_lfish_kd_temp').closest('tr').addClass('method_options').hide();
    $('#id_lfish_ke_temp').closest('tr').addClass('method_options').hide();
    $('#id_lfish_km').closest('tr').addClass('method_options').hide();
    // $('#id_bw_quail').closest('tr').addClass('method_options2').hide();
    $('#id_bw_duck').closest('tr').addClass('method_options3').hide();
    $('#id_bw_other_bird').closest('tr').addClass('method_options4').hide();
    // $('#id_bw_rat').closest('tr').hide();
    $('#id_bw_other_mammal').closest('tr').hide();
    $('#id_mammalian_chronic_endpoint_unit').closest('tr').hide();
    
    $('#id_species_of_the_tested_mammal').change(function() {
        if ($(this).val() == "350"){
            $('#id_bw_rat').closest('tr').show();
            $('#id_bw_other_mammal').closest('tr').hide();
        }
        else{
           $('#id_bw_rat').closest('tr').hide();
           $('#id_bw_other_mammal').closest('tr').show();
       }
   });
    $('#id_species_of_the_tested_bird').change(function() {
       
        if ($(this).val() == "178"){
            $('#id_bw_quail').closest('tr').show();
            $('#id_bw_duck').closest('tr').hide();
            $('#id_bw_other_bird').closest('tr').hide();
        }
        else if ($(this).val() == "1580"){
            $('#id_bw_duck').closest('tr').show();
            $('#id_bw_quail').closest('tr').hide();
            $('#id_bw_other_bird').closest('tr').hide();
        }
        else{
           $('#id_bw_other_bird').closest('tr').show();
           $('#id_bw_duck').closest('tr').hide();
           $('#id_bw_quail').closest('tr').hide();
       }
   });
    $('#id_rate_constants').change(function() {
       $('tr[class^="method_options"]').hide();  
       if ($(this).val() == "b"){
        $('tr[class^="method_options"]').show();
    }
    else if ($(this).val() == "a"){
        $('tr[class^="method_options"]').hide();
    }    
    });

});