from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


################ How model name appears on web page ################
header = 'T-REX 1.5.2'
####################################################################

def trex2InputPage(request, model=''):
    import trex2_parameters,trex2_tooltips

    html = render_to_string('04uberinput_start_tabbed.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + """<a href="trex_input.html" class="TREX1"> Want to Use TREX 1.4.1?</a>"""
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Chemical', 'Avian', 'Mammal'],
                'tab_label': ['Chemical', 'Avian', 'Mammal']
                }
            })
    html = html + """<br><table class="input_table tab tab_Chemical">"""
    html = html + str(trex2_parameters.trexInp_chem())
    html = html + """</table><table class="input_table tab tab_Application tab_Chemical">
                                <tr><th colspan="2" scope="col"><label for="id_noa">Number of Applications:</label></th>
                                    <td colspan="3" scope="col"><select name="noa" id="id_noa">
                                        <option value="1">1</option><option value="2">2</option><option value="3" selected>3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option></select>
                                    </td>
                                </tr>
                                <tr id="noa_header">
                                    <th width="18%">App#</th>
                                    <th width="18%" id="rate_head">Rate (lb ai/acre)</th>
                                    <th width="18%">Day of Application</th>
                                </tr>
                                <tr class="tab_noa1">
                                    <td><input name="jm1" type="text" size="5" value="1"/></td>
                                    <td><input type="text" size="5" name="rate1" id="id_rate1" value="4"/></td>
                                    <td><input type="text" size="5" name="day1" id="id_day1" value="0" /></td>
                                </tr>""" 
    html = html + """</table><table class="input_table tab tab_Avian" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_bird())
    html = html + """</table><table class="input_table tab tab_Mammal" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_mammal())
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(trex2_tooltips, 'tooltips'):
        tooltips = trex2_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html


@require_POST
def trex2OutputPage(request):
    import trex2_model

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
    day_out = []
    for i in range(int(n_a)):
       j=i+1
       rate_temp = request.POST.get('rate'+str(j))
       rate_out.append(float(rate_temp))
       day_temp = float(request.POST.get('day'+str(j)))
       day_out.append(day_temp)  

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


    trex2_obj = trex2_model.trex2("single", chem_name, use, formu_name, a_i, Application_type, seed_treatment_formulation_name, seed_crop, seed_crop_v, r_s, b_w, p_i, den, h_l, n_a, rate_out, day_out,
                  ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird_sm, aw_bird_md, aw_bird_lg, 
                  Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                  tw_bird_ld50, tw_bird_lc50, tw_bird_NOAEC, tw_bird_NOAEL, x, ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm_sm, aw_mamm_md, aw_mamm_lg, tw_mamm,
                  m_s_r_p)

    return trex2_obj