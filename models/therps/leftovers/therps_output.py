"""
.. module:: therps_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def therpsOutputPage(request):
    import therps_model

    chem_name = request.POST.get('chemical_name')
    use = request.POST.get('Use')
    formu_name = request.POST.get('Formulated_product_name')
    a_i = request.POST.get('percent_ai')
    a_i = float(a_i)/100
    a_r = request.POST.get('application_rate')
    a_r = float(a_r)         
    n_a = request.POST.get('number_of_applications')
    n_a = float(n_a)

    i_a = request.POST.get('interval_between_applications')
    i_a = float(i_a)
    h_l = request.POST.get('Foliar_dissipation_half_life')
    h_l = float(h_l)        
    avian_ld50 = float(request.POST.get('avian_ld50'))
    avian_lc50 = float(request.POST.get('avian_lc50'))
    avian_NOAEC = float(request.POST.get('avian_NOAEC'))
    avian_NOAEL = float(request.POST.get('avian_NOAEL'))

    Species_of_the_tested_bird_avian_ld50 = request.POST.get('Species_of_the_tested_bird_avian_ld50')
    Species_of_the_tested_bird_avian_lc50 = request.POST.get('Species_of_the_tested_bird_avian_lc50')
    Species_of_the_tested_bird_avian_NOAEC = request.POST.get('Species_of_the_tested_bird_avian_NOAEC')
    Species_of_the_tested_bird_avian_NOAEL = request.POST.get('Species_of_the_tested_bird_avian_NOAEL')

    bw_avian_ld50 = float(request.POST.get('bw_avian_ld50'))
    bw_avian_lc50 = float(request.POST.get('bw_avian_lc50'))
    bw_avian_NOAEC = float(request.POST.get('bw_avian_NOAEC'))
    bw_avian_NOAEL = float(request.POST.get('bw_avian_NOAEL'))

    mineau_scaling_factor = request.POST.get('mineau_scaling_factor')
    mineau_scaling_factor = float(mineau_scaling_factor)
    c_mamm_a = request.POST.get('body_weight_of_the_consumed_mammal_a')
    c_mamm_a = float(c_mamm_a)
    c_herp_a = request.POST.get('body_weight_of_the_consumed_herp_a')
    c_herp_a = float(c_herp_a)    

    bw_herp_a_sm = request.POST.get('BW_herptile_a_sm')
    bw_herp_a_sm = float(bw_herp_a_sm)
    bw_herp_a_md = request.POST.get('BW_herptile_a_md')
    bw_herp_a_md = float(bw_herp_a_md)
    bw_herp_a_lg = request.POST.get('BW_herptile_a_lg')
    bw_herp_a_lg = float(bw_herp_a_lg)

    wp_herp_a_sm = request.POST.get('W_p_a_sm')
    wp_herp_a_sm = float(wp_herp_a_sm)/100      
    wp_herp_a_md = request.POST.get('W_p_a_md')
    wp_herp_a_md = float(wp_herp_a_md)/100   
    wp_herp_a_lg = request.POST.get('W_p_a_lg')
    wp_herp_a_lg = float(wp_herp_a_lg)/100   
    

    therps_obj = therps_model.therps('single',chem_name, use, formu_name, a_i, h_l, n_a, i_a, a_r, avian_ld50, avian_lc50, avian_NOAEC, avian_NOAEL, 
                                     Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                                     bw_avian_ld50, bw_avian_lc50, bw_avian_NOAEC, bw_avian_NOAEL,
                                     mineau_scaling_factor, bw_herp_a_sm, bw_herp_a_md, bw_herp_a_lg, wp_herp_a_sm, wp_herp_a_md, 
                                     wp_herp_a_lg, c_mamm_a, c_herp_a)


    return therps_obj