"""
.. module:: agdrift_therps_output
   :synopsis: A useful module indeed.
"""

from django.views.decorators.http import require_POST


@require_POST
def agdrift_therpsOutputPage(request):
    from ubertool_app.models.agdrift import agdrift_model,agdrift_tables
    from ubertool_app.models.therps import therps_model,therps_tables
    import agdrift_therps_tables


    # AgDrift Inputs
    drop_size = request.POST.get('drop_size')
    ecosystem_type = request.POST.get('ecosystem_type')
    application_method = request.POST.get('application_method')
    boom_height = request.POST.get('boom_height')
    orchard_type = request.POST.get('orchard_type')
    aquatic_type = request.POST.get('aquatic_type')
    distance = request.POST.get('distance')
    calculation_input = request.POST.get('calculation_input')

    # T-HERPS Inputs
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
    
    # Run AgDrift model
    agdrift_obj = agdrift_model.agdrift(True, True, 'single', drop_size, ecosystem_type, application_method, boom_height, orchard_type, a_r, distance, aquatic_type, calculation_input)
    agdrift_x=agdrift_obj.x
    # Run T-HERPS model (using an output from AgDrift as an input)
    therps_obj = therps_model.therps("single", chem_name, use, formu_name, a_i, h_l, n_a, i_a, a_r, avian_ld50, avian_lc50, avian_NOAEC, avian_NOAEL, 
                                     Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                                     bw_avian_ld50, bw_avian_lc50, bw_avian_NOAEC, bw_avian_NOAEL,
                                     mineau_scaling_factor, bw_herp_a_sm, bw_herp_a_md, bw_herp_a_lg, wp_herp_a_sm, wp_herp_a_md, 
                                     wp_herp_a_lg, c_mamm_a, c_herp_a)

    # Render output tables for each of the linked models
    html = agdrift_therps_tables.timestamp(agdrift_obj)
    html = html + agdrift_tables.table_all(agdrift_obj)
    html = html + therps_tables.table_all(therps_obj)[0]
    
    # merge the two class instances into one instance
    def merge(ob1, ob2):
        """
        an object's __dict__ contains all its 
        attributes, methods, docstrings, etc.
        """
        ob1.__dict__.update(ob2.__dict__)
        return ob1
    
    agdrift_therps_obj = merge(agdrift_obj, therps_obj)

    # Return the rendered output tables & merged model object to output.py
    return html, agdrift_therps_obj