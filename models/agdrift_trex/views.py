from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


################ How model name appears on web page ################
header = 'AgDrift & T-REX'
####################################################################

def agdrift_trexInputPage(request, model=''):
    import agdrift_trex_parameters,agdrift_trex_tooltips
    from models.trex2 import trex2_parameters

    html = render_to_string('04uberinput_start_tabbed.html', {
            'model': model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Agdrift', 'Chemical', 'Avian', 'Mammal'],
                'tab_label': ['Agdrift', 'Chemical', 'Avian', 'Mammal']
                }
            })
    html = html + """<br><table class="input_table tab tab_Agdrift" border="0">"""
    html = html + str(agdrift_trex_parameters.agdriftInp())
    html = html + """<br><table class="input_table tab tab_Chemical" border="0" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_chem())
    html = html + """</table><table class="input_table tab tab_Application tab_Chemical" border="0" style="display:none">
                                <tr><th colspan="2" scope="col"><label for="id_noa">Number of Applications:</label></th>
                                    <td colspan="3" scope="col"><select name="noa" id="id_noa">
                                        <option value="1"  selected>1</option></select>
                                    </td>
                                </tr>
                                <tr id="noa_header"><th width="18%">App#</th>
                                                                         <th width="18%" id="rate_head">Rate (lb ai/acre)</th>
                                                                         <th width="18%">Day of Application</th>
                                </tr>
                                <tr class="tab_noa1"><td><input name="jm1" type="text" size="5" value="1"/></td>
                                                     <td><input type="text" size="5" name="rate1" id="id_rate1" value="4"/></td>
                                                     <td><input type="text" size="5" name="day1" id="id_day1" value="0" disabled/></td>
                                </tr>""" 
    html = html + """</table><table class="input_table tab tab_Avian" border="0" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_bird())
    html = html + """</table><table class="input_table tab tab_Mammal" border="0" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_mammal())
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(agdrift_trex_tooltips, 'tooltips'):
        tooltips = agdrift_trex_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html


@require_POST
def agdrift_trexOutputPage(request):

    # AgDrift Inputs
    drop_size = request.POST.get('drop_size')
    ecosystem_type = request.POST.get('ecosystem_type')
    application_method = request.POST.get('application_method')
    boom_height = request.POST.get('boom_height')
    orchard_type = request.POST.get('orchard_type')
    aquatic_type = request.POST.get('aquatic_type')
    distance = request.POST.get('distance')
    calculation_input = request.POST.get('calculation_input')

    # T-REX Inputs
    chem_name = request.POST.get('chemical_name')
    use = request.POST.get('Use')
    formu_name = request.POST.get('Formulated_product_name')
    a_i = request.POST.get('percent_ai')
    a_i = float(a_i)/100
    Application_type = request.POST.get('Application_type')
    seed_crop = float(request.POST.get('seed_crop'))
    seed_crop_v = request.POST.get('seed_crop_v')
    p_i = request.POST.get('percent_incorporated')
    p_i = float(p_i)/100
    seed_treatment_formulation_name = request.POST.get('seed_treatment_formulation_name')
    den = request.POST.get('density_of_product')
    den = float(den)
    m_s_r_p = request.POST.get('maximum_seedling_rate_per_use')
    m_s_r_p = float(m_s_r_p)
    r_s = request.POST.get('row_sp') 
    r_s=float(r_s)
    b_w = request.POST.get('bandwidth')   #convert to ft
    b_w = float(b_w)/12

    if Application_type=='Seed Treatment':
       n_a = 1
    else:
       n_a = float(request.POST.get('noa'))
    
    rate_out = []
    day_out = [0]
    for i in range(int(n_a)):
       j=i+1
       rate_temp = request.POST.get('rate'+str(j))
       rate_out.append(float(rate_temp))
       # day_temp = float(request.POST.get('day'+str(j)))
       # day_out.append(day_temp)  
    h_l = request.POST.get('Foliar_dissipation_half_life')
    ld50_bird = request.POST.get('avian_ld50')
    lc50_bird = request.POST.get('avian_lc50')
    NOAEC_bird = float(request.POST.get('avian_NOAEC'))
    try:
        NOAEL_bird = float(request.POST.get('avian_NOAEL'))
    except:
        NOAEL_bird = 'N/A'
    aw_bird_sm = request.POST.get('body_weight_of_the_assessed_bird_small')
    aw_bird_sm = float(aw_bird_sm)  
    aw_bird_md = request.POST.get('body_weight_of_the_assessed_bird_medium')
    aw_bird_md = float(aw_bird_md) 
    aw_bird_lg = request.POST.get('body_weight_of_the_assessed_bird_large')
    aw_bird_lg = float(aw_bird_lg)       
    
    Species_of_the_tested_bird_avian_ld50 = request.POST.get('Species_of_the_tested_bird_avian_ld50')
    Species_of_the_tested_bird_avian_lc50 = request.POST.get('Species_of_the_tested_bird_avian_lc50')
    Species_of_the_tested_bird_avian_NOAEC = request.POST.get('Species_of_the_tested_bird_avian_NOAEC')
    Species_of_the_tested_bird_avian_NOAEL = request.POST.get('Species_of_the_tested_bird_avian_NOAEL')

    tw_bird_ld50 = float(request.POST.get('bw_avian_ld50'))
    tw_bird_lc50 = float(request.POST.get('bw_avian_lc50'))
    tw_bird_NOAEC = float(request.POST.get('bw_avian_NOAEC'))
    tw_bird_NOAEL = float(request.POST.get('bw_avian_NOAEL'))

    x = request.POST.get('mineau_scaling_factor')
    ld50_mamm = request.POST.get('mammalian_ld50')
    try:
        lc50_mamm = float(request.POST.get('mammalian_lc50'))
    except:
        lc50_mamm = 'N/A'
    NOAEC_mamm = request.POST.get('mammalian_NOAEC')
    NOAEC_mamm = float(NOAEC_mamm)
    NOAEL_mamm = request.POST.get('mammalian_NOAEL')

    aw_mamm_sm = request.POST.get('body_weight_of_the_assessed_mammal_small')
    aw_mamm_sm = float(aw_mamm_sm)  
    aw_mamm_md = request.POST.get('body_weight_of_the_assessed_mammal_medium')
    aw_mamm_md = float(aw_mamm_md) 
    aw_mamm_lg = request.POST.get('body_weight_of_the_assessed_mammal_large')
    aw_mamm_lg = float(aw_mamm_lg)               
    tw_mamm = request.POST.get('body_weight_of_the_tested_mammal')
    tw_mamm = float(tw_mamm) 


    return agdrift_trex_obj