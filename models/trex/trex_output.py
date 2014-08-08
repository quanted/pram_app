# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def trexOutputPage(request):

    import trex_model

    chem_name = request.POST.get('chemical_name')
    use = request.POST.get('Use')
    formu_name = request.POST.get('Formulated_product_name')
    a_i = request.POST.get('percent_ai')
    a_i = float(a_i)/100
    Application_type = request.POST.get('Application_type')
    p_i = request.POST.get('percent_incorporated')
    p_i = float(p_i)/100
    a_r = request.POST.get('application_rate')
    a_r = float(a_r)        
    a_r_l = request.POST.get('application_rate_l')
    a_r_l=float(a_r_l)        
    seed_treatment_formulation_name = request.POST.get('seed_treatment_formulation_name')
    den = request.POST.get('density_of_product')
    den = float(den)
    m_s_r_p = request.POST.get('maximum_seedling_rate_per_use')
    m_s_r_p = float(m_s_r_p)
    a_r_p = request.POST.get('application_rate_per_use')
    a_r_p = float(a_r_p)
    r_s = request.POST.get('row_sp') 
    r_s=float(r_s)
    b_w = request.POST.get('bandwidth')   #convert to ft
    b_w = float(b_w)/12
    n_a = request.POST.get('number_of_applications')
    a_t = request.POST.get('Application_target')
    if a_t=='Short grass':
       para=240       #coefficient used to estimate initial conc.
    elif a_t=='Tall grass':
       para=110
    elif a_t=='Broad-leafed plants/small insects':
       para=135
    elif a_t=='Fruits/pods/seeds/large insects':
       para=15
    i_a = request.POST.get('interval_between_applications')
    h_l = request.POST.get('Foliar_dissipation_half_life')
    ld50_bird = request.POST.get('avian_ld50')
    lc50_bird = request.POST.get('avian_lc50')
    NOAEC_bird = request.POST.get('avian_NOAEC')
    NOAEC_bird = float(NOAEC_bird)
    NOAEL_bird = request.POST.get('avian_NOAEL')
    NOAEL_bird = float(NOAEL_bird)
    
#        bird_type = request.POST.get('Bird_type')        
    aw_bird = request.POST.get('body_weight_of_the_assessed_bird')
    aw_bird = float(aw_bird)        
    tw_bird = request.POST.get('body_weight_of_the_tested_bird')
    tw_bird = float(tw_bird)        
    x = request.POST.get('mineau_scaling_factor')
    ld50_mamm = request.POST.get('mammalian_ld50')
    lc50_mamm = request.POST.get('mammalian_lc50')
    lc50_mamm=float(lc50_mamm)        
    NOAEC_mamm = request.POST.get('mammalian_NOAEC')
    NOAEC_mamm = float(NOAEC_mamm)
    NOAEL_mamm = request.POST.get('mammalian_NOAEL')
#        mammal_type = request.POST.get('Mammal_type')                
#        if mammal_type =='Herbivores and insectivores':
#           mf_w_mamm=0.8       #coefficient used to estimate initial conc.
#        elif mammal_type=='Granivores':
#           mf_w_mamm=0.1 
#        if bird_type =='Herbivores and insectivores':
#           mf_w_bird=0.8       #coefficient used to estimate initial conc.
#        elif bird_type=='Granivores':
#           mf_w_bird=0.1            
    aw_mamm = request.POST.get('body_weight_of_the_assessed_mammal')
    aw_mamm = float(aw_mamm)                
    tw_mamm = request.POST.get('body_weight_of_the_tested_mammal')
    tw_mamm = float(tw_mamm) 
    
    #mf_w_mamm = request.POST.get('mass_fraction_of_water_in_the_mammal_food')
    #mf_w_bird = request.POST.get('mass_fraction_of_water_in_the_bird_food')
    
    
    html = """
    <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <table>
              <tr>
                <th scope="col">Inputs</div></th>
                <th scope="col">Value</div></th>
                <th scope="col">Inputs</div></th>
                <th scope="col">Value</div></th>                            
              </tr>
              <tr>
                <td>Chemical name</td>
                <td>%s</td>
                <td>Use</td>
                <td>%s</td>                          
              </tr>
              <tr>
                <td>Formulated procuct name</td>
                <td>%s</td>
                <td>Percentage active ingredient</td>
                <td>%s%%</td>  
              </tr>
              <tr>
                <td>Application type</td>
                <td>%s</td>
                <td>Percentage incorporated</td>
                <td>%s%%</td>
              </tr>
              <tr>
                <td>Application rate (lbs a.i./A)</td>
                <td>%s</td>                            
                <td>Liquid application rate (fl oz/A)</td>                            
                <td>%s</td>
              </tr>
              <tr>
                <td>Seed treatment formulation name</td>
                <td>%s</td>
                <td>Density of product (lbs/gal)</td>
                <td>%s</td>
              </tr>
              <tr>
                <td>Maximum seeding rate per use (lbs/A)</td>
                <td>%s</td>
                <td>Application rate per use (fl oz/cwt)</td>
                <td>%s</td>
              </tr>                              
              <tr>
                <td>Row spacing (inch)</td>
                <td>%s</td>
                <td>Bandwidth (inch)</td>
                <td>%s</td>
              </tr>                              
              <tr>
                <td>Number of applications</td>
                <td>%s</td>
                <td>Application target</td>
                <td>%s</td>
              </tr>                              
              <tr>                            
                <td>Interval between applications (days)</td>
                <td>%s</td>
                <td>Foliar dissipation half-life (days)</td>
                <td>%s</td>
              </tr>                              
              <tr>                            
                <td>Avian LD50 (mg/kg-bw)</td>
                <td>%s</td>
                <td>Avian LC50 (mg/kg-diet)</td>
                <td>%s</td>
              </tr>    
              <tr>                            
                <td>Avian NOAEC (mg/kg-diet)</td>
                <td>%s</td>
                <td>Avian NOAEL (mg/kg-bw)</td>
                <td>%s</td>
              </tr>    
              <tr>                            
                <td>Body weight of assessed bird (g)</td>
                <td>%s</td>
                <td>Body weight of tested bird (g)</td>
                <td>%s</td>                                                   
              </tr>    
              <tr>
                <td>Mineau scaling factor</td>
                <td>%s</td>
                <td>Mammalian LD50 (mg/kg-bw)</td>
                <td>%s</td>                                                    
              </tr>    
              <tr>                            
                <td>Mammalian LC50 (mg/kg-diet)</td>
                <td>%s</td>
                <td>Mammalian NOAEC (mg/kg-diet)</td>
                <td>%s</td>                                                                             
              </tr>    
              <tr>
                <td>Mammalian NOAEL (mg/kg-bw)</td>
                <td>%s</td>
                <td>Body weight of assessed mammal (g)</td>
                <td>%s</td>
              </tr>                           
              <tr>
                <td>Body weight of tested mammal (g)</td>
                <td>%s</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>                            
              </tr>                                                              
            </table>
        </div>
    """%( chem_name, use, formu_name, 100*a_i, Application_type, 100*p_i, a_r, a_r_l, seed_treatment_formulation_name, den, m_s_r_p, a_r_p, 
         r_s, b_w, n_a, a_t, i_a, h_l, ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird, tw_bird, x, ld50_mamm, 
         lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm, tw_mamm)                          

    html = html + """
    <br>
    <H3 class="out_1 collapsible" id="section1"><span></span>Model Outputs</H3>
        <div class="out_">
            <table>
              <tr>
                <th scope="col">Outputs</div></th>
                <th scope="col">Value</div></th>                            
              </tr>
              <tr>
                <td>Dietary-based EECs for %s</td>
                <td>%0.2E</td>
              </tr>
              <tr>
                <td>Avian dose-based acute EECs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>                      
              <tr>
                <td>Avian dose-based acute EECs (Granivores)</td>
                <td>%0.2E</td>                            
              </tr>  
              <tr>
                <td>Avian dose-based acute RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>
              <tr>
                <td>Avian dose-based acute RQs (Granivores)</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>
                <td>Avian diet-based acute RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>
              <tr>
                <td>Avian diet-based chronic RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>
                <td>Mammalian dose-based acute EECs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr> 
              <tr>
                <td>Mammalian dose-based acute EECs (Granivores)</td>
                <td>%0.2E</td>                            
              </tr>                            
              <tr>
                <td>Mammalian dose-based acute RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>
                <td>Mammalian dose-based acute RQs (Granivores)</td>
                <td>%0.2E</td>                            
              </tr> 
              <tr>
                <td>Mammalian dose-based chronic RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                           
              </tr>                                                                                                        
              <tr>
                <td>Mammalian dose-based chronic RQs (Granivores)</td>
                <td>%0.2E</td>                            
              </tr>                                                   
              <tr>                            
                <td>Mammalian diet-based acute RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>
              <tr>                            
                <td>Mammalian diet-based chronic RQs for %s (Herbivores and insectivores)</td>
                <td>%0.2E</td>                            
              </tr>                                                 
              <tr>                            
                <td>Avian LD50<sup>-2</sup> for row/band/in-furrow granular application</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Avian LD50<sup>-2</sup> for row/band/in-furrow liquid application</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Avian LD50<sup>-2</sup> for broadcast granular application</td>
                <td>%0.2E</td>                            
              </tr> 
              <tr>                            
                <td>Avian LD50<sup>-2</sup> for broadcast liquid application</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Mammalian LD50<sup>-2</sup> for row/band/in-furrow granular application</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Mammalian LD50<sup>-2</sup> for row/band/in-furrow liquid application</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Mammalian LD50<sup>-2</sup> for broadcast granular application</td>
                <td>%0.2E</td>                            
              </tr> 
              <tr>                            
                <td>Mammalian LD50<sup>-2</sup> for broadcast liquid application</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Seed treatment avian acute RQs (method 1)</td>
                <td>%0.2E</td>                            
              </tr>
              <tr>                            
                <td>Seed treatment avian acute RQs (method 2)</td>
                <td>%0.2E</td>                            
              </tr>
              <tr>                            
                <td>Seed treatment avian chronic RQs</td>
                <td>%0.2E</td>                            
              </tr>                          
              <tr>                            
                <td>Seed treatment mammalian acute RQs (method 1)</td>
                <td>%0.2E</td>                            
              </tr>
              <tr>                            
                <td>Seed treatment mammalian acute RQs (method 2)</td>
                <td>%0.2E</td>                            
              </tr> 
              <tr>                            
                <td>Seed treatment mammalian chronic RQs</td>
                <td>%0.2E</td>                            
              </tr>                           
            </table>
        </div>
    """ %(   a_t, trex_model.EEC_diet(trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l), a_t, trex_model.EEC_dose_bird(trex_model.EEC_diet, aw_bird, trex_model.fi_bird, 0.8, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l), 
            trex_model.EEC_dose_bird_g(trex_model.EEC_diet, aw_bird, trex_model.fi_bird, 0.1, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l), a_t, 
            trex_model.ARQ_dose_bird(trex_model.EEC_dose_bird, trex_model.EEC_diet, aw_bird, trex_model.fi_bird, trex_model.at_bird, ld50_bird, tw_bird, x, 0.8, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            trex_model.ARQ_dose_bird_g(trex_model.EEC_dose_bird, trex_model.EEC_diet, aw_bird, trex_model.fi_bird, trex_model.at_bird, ld50_bird, tw_bird, x, 0.1, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            a_t, trex_model.ARQ_diet_bird(trex_model.EEC_diet, lc50_bird, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l), a_t, trex_model.CRQ_diet_bird(trex_model.EEC_diet, NOAEC_bird, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            a_t, trex_model.EEC_dose_mamm(trex_model.EEC_diet, aw_mamm, trex_model.fi_mamm, 0.8, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l), trex_model.EEC_dose_mamm_g(trex_model.EEC_diet, aw_mamm, trex_model.fi_mamm, 0.1, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),                                      
            a_t, trex_model.ARQ_dose_mamm(trex_model.EEC_dose_mamm, trex_model.at_mamm, aw_mamm, ld50_mamm, tw_mamm, 0.8, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            trex_model.ARQ_dose_mamm_g(trex_model.EEC_dose_mamm, trex_model.at_mamm, aw_mamm, ld50_mamm, tw_mamm, 0.1, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            a_t, trex_model.CRQ_dose_mamm(trex_model.EEC_diet, trex_model.EEC_dose_mamm, trex_model.ANOAEL_mamm, NOAEL_mamm, aw_mamm, tw_mamm, 0.8, n_a, i_a, a_r, a_i, para, h_l),
            trex_model.CRQ_dose_mamm_g(trex_model.EEC_diet, trex_model.EEC_dose_mamm, trex_model.ANOAEL_mamm, NOAEL_mamm, aw_mamm, tw_mamm, 0.1, n_a, i_a, a_r, a_i, para, h_l),
            a_t, trex_model.ARQ_diet_mamm(trex_model.EEC_diet, lc50_mamm, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            a_t, trex_model.CRQ_diet_mamm(trex_model.EEC_diet, NOAEC_mamm, trex_model.C_0, n_a, i_a, a_r, a_i, para, h_l),
            trex_model.LD50_rg_bird(Application_type, a_r, a_i, p_i, r_s, b_w, aw_bird, trex_model.at_bird, ld50_bird, tw_bird, x), trex_model.LD50_rl_bird(Application_type, a_r_l, a_i, p_i, b_w, aw_bird, trex_model.at_bird, ld50_bird, tw_bird, x),
            trex_model.LD50_bg_bird(Application_type, a_r, a_i, p_i, b_w, aw_bird, trex_model.at_bird, ld50_bird, tw_bird,x),trex_model.LD50_bl_bird(Application_type, a_r_l, a_i, p_i, b_w, aw_bird, trex_model.at_bird, ld50_bird, tw_bird,x),
            trex_model.LD50_rg_mamm(Application_type, a_r, a_i, p_i, r_s, b_w, aw_mamm, trex_model.at_mamm, ld50_mamm, tw_mamm), trex_model.LD50_rl_mamm(Application_type, a_r_l, a_i, p_i, b_w, aw_mamm, trex_model.at_mamm, ld50_mamm, tw_mamm),
            trex_model.LD50_bg_mamm(Application_type, a_r, a_i, p_i, b_w, aw_mamm, trex_model.at_mamm, ld50_mamm, tw_mamm),trex_model.LD50_bl_mamm(Application_type, a_r_l, a_i, p_i, b_w, aw_mamm, trex_model.at_mamm, ld50_mamm, tw_mamm),
            trex_model.sa_bird_1(a_r_p, a_i, den, trex_model.at_bird,trex_model.fi_bird, ld50_bird, aw_bird, tw_bird, x),trex_model.sa_bird_2(a_r_p, a_i, den, m_s_r_p, trex_model.at_bird, ld50_bird, aw_bird, tw_bird, x),
            trex_model.sc_bird(a_r_p, a_i, den, NOAEC_bird),trex_model.sa_mamm_1(a_r_p, a_i, den, trex_model.at_mamm, trex_model.fi_mamm, ld50_mamm, aw_mamm, tw_mamm),
            trex_model.sa_mamm_2(a_r_p, a_i, den, m_s_r_p, trex_model.at_mamm, ld50_mamm, aw_mamm, tw_mamm),trex_model.sc_mamm(a_r_p, a_i, den, NOAEC_mamm))


    trex_obj = html

    return trex_obj
    # chem_name, use, formu_name, a_i, Application_type, p_i, a_r, a_r_l, seed_treatment_formulation_name, den, m_s_r_p, a_r_p, r_s, b_w, n_a, a_t, i_a, h_l, ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird, tw_bird, x, ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm, tw_mamm