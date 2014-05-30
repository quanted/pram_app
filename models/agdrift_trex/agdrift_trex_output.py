from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def agdrift_trexOutputPage(request):
    from models.agdrift import agdrift_model,agdrift_tables
    from models.trex2 import trex2_model,trex2_tables
    import agdrift_trex_tables


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

    # Run AgDrift model
    agdrift_obj = agdrift_model.agdrift(True, True, 'single', drop_size, ecosystem_type, application_method, boom_height, orchard_type, rate_out[0], distance, aquatic_type, calculation_input, None)
    x_agdrif=agdrift_obj.x
    # Run T-REX2 model (using an output from AgDrift as an input)
    trex_obj = trex2_model.trex2('single', chem_name, use, formu_name, a_i, Application_type, seed_treatment_formulation_name, seed_crop, seed_crop_v, r_s, b_w, p_i, den, h_l, n_a, [agdrift_obj.init_avg_dep_foa*i for i in rate_out], day_out,
                                 ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird_sm, aw_bird_md, aw_bird_lg, 
                                 Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                                 tw_bird_ld50, tw_bird_lc50, tw_bird_NOAEC, tw_bird_NOAEL, x, ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm_sm, aw_mamm_md, aw_mamm_lg, tw_mamm,
                                 m_s_r_p)

    # Render output tables for each of the linked models
    html = agdrift_trex_tables.timestamp(agdrift_obj)
    html = html + agdrift_tables.table_all(agdrift_obj)
    html = html + trex2_tables.table_all(trex_obj)[0]

    # merge the two class instances into one instance
    def merge(ob1, ob2):
        """
        an object's __dict__ contains all its 
        attributes, methods, docstrings, etc.
        """
        ob1.__dict__.update(ob2.__dict__)
        return ob1
    
    agdrift_trex_obj = merge(agdrift_obj, trex_obj)
    agdrift_trex_obj.x_agdrif=x_agdrif
    agdrift_trex_obj.x_trex=trex_obj.x

    # Return the rendered output tables & merged model object to output.py
    return html, agdrift_trex_obj