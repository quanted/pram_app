from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
 
import logging
@require_POST
def kabamOutputPage(request):
    import kabam_model

    chemical_name = request.POST.get('name')
    l_kow = float(request.POST.get('lkow'))
    k_oc = float(request.POST.get('Koc'))
    c_wdp_2 = float(request.POST.get('beec'))
    c_wdp = float(request.POST.get('beec')) / 1000000
    water_column_EEC = float(request.POST.get('weec'))
    c_wto = float(water_column_EEC) / 1000000
    mineau_scaling_factor = float(request.POST.get('sf'))
    x_poc = float(request.POST.get('cpoc'))
    x_doc = float(request.POST.get('cdoc'))
    c_ox = float(request.POST.get('cox'))
    w_t = float(request.POST.get('wt'))
    c_ss = float(request.POST.get('css'))
    oc = float(request.POST.get('oc'))/100
    k_ow = 10**(float(l_kow))
    Species_of_the_tested_bird = request.POST.get('Species_of_the_tested_bird')
    bw_quail = request.POST.get('bw_quail')
    bw_duck = request.POST.get('bw_duck')
    bwb_other = request.POST.get('bwb_other')
    avian_ld50 = float(request.POST.get('ald50'))
    avian_lc50 = float(request.POST.get('alc50'))
    avian_noaec = float(request.POST.get('aNOAEC'))
    m_species = request.POST.get('m_species')
    bw_rat=request.POST.get('bw_rat')
    bwm_other=request.POST.get('bwm_other')
#        print 'weight=', body_weight_of_the_tested_mamm_other
    mammalian_ld50 = float(request.POST.get('mld50'))
    mammalian_lc50 = float(request.POST.get('mlc50'))
    mammalian_chronic_endpoint = float(request.POST.get('m_chronic'))
#        body_weight_of_the_assessed_mamm = float(request.POST.get('bw_assess_m'))
    #diet_for_large_fish = request.POST.get('Diet_lfish')
    lf_p_sediment = float(request.POST.get('lfish_p_sediment'))/100
    lf_p_phytoplankton = float(request.POST.get('lfish_p_phyto'))/100
    lf_p_zooplankton = float(request.POST.get('lfish_p_zoo'))/100
    lf_p_benthic_invertebrates = float(request.POST.get('lfish_p_beninv'))/100
    lf_p_filter_feeders = float(request.POST.get('lfish_p_ff'))/100
    lf_p_small_fish = float(request.POST.get('lfish_p_sfish'))/100
    lf_p_medium_fish = float(request.POST.get('lfish_p_mfish'))/100
    #diet_for_medium_fish = request.POST.get('Diet_mfish')
    mf_p_sediment = float(request.POST.get('mfish_p_sediment'))
    #print type(mf_p_sediment)
    mf_p_sediment = float(mf_p_sediment)
    mf_p_phytoplankton = float(request.POST.get('mfish_p_phyto'))
    mf_p_zooplankton = float(request.POST.get('mfish_p_zoo'))
    mf_p_benthic_invertebrates = float(request.POST.get('mfish_p_beninv'))/100
    mf_p_filter_feeders = float(request.POST.get('mfish_p_ff'))
    mf_p_small_fish = float(request.POST.get('mfish_p_sfish'))/100
    #diet_for_small_fish = request.POST.get('Diet_sfish')
    sf_p_sediment = float(request.POST.get('sfish_p_sediment'))
    sf_p_phytoplankton = float(request.POST.get('sfish_p_phyto'))
    sf_p_zooplankton = float(request.POST.get('sfish_p_zoo'))/100
    sf_p_benthic_invertebrates = float(request.POST.get('sfish_p_beninv'))/100
    sf_p_filter_feeders = float(request.POST.get('sfish_p_ff'))
    #diet_for_filter_feeder = request.POST.get('Diet_ff')
    ff_p_sediment = float(request.POST.get('ff_p_sediment'))/100
    ff_p_phytoplankton = float(request.POST.get('ff_p_phyto'))/100
    ff_p_zooplankton = float(request.POST.get('ff_p_zoo'))/100
    ff_p_benthic_invertebrates = float(request.POST.get('ff_p_beninv'))
    #diet_for_invertebrates = request.POST.get('Diet_invert')
    beninv_p_sediment = float(request.POST.get('beninv_p_sediment'))/100
    beninv_p_phytoplankton = float(request.POST.get('beninv_p_phyto'))/100
    beninv_p_zooplankton = float(request.POST.get('beninv_p_zoo'))/100
    #diet_for_zooplankton = request.POST.get('Diet_zoo')
    zoo_p_sediment = float(request.POST.get('zoo_p_sediment'))
    zoo_p_phyto = float(request.POST.get('zoo_p_phyto'))/100
    #characteristics_sediment = request.POST.get('char_s')
    s_lipid = float(request.POST.get('s_lipid'))/100
    s_NLOM = float(request.POST.get('s_NLOM'))/100
    s_water = float(request.POST.get('s_water'))/100
    s_respire = request.POST.get('s_respire')
    #characteristics_phytoplankton = request.POST.get('char_phyto')
    v_lb_phytoplankton = float(request.POST.get('phyto_lipid'))/100
    v_nb_phytoplankton = float(request.POST.get('phyto_NLOM'))/100
    v_wb_phytoplankton = float(request.POST.get('phyto_water'))/100
    phyto_respire = request.POST.get('phyto_respire')
    #characteristics_zooplankton = request.POST.get('char_zoo')
    wb_zoo = float(request.POST.get('zoo_ww'))
    v_lb_zoo = float(request.POST.get('zoo_lipid'))/100
    v_nb_zoo = float(request.POST.get('zoo_NLOM'))/100
    v_wb_zoo = float(request.POST.get('zoo_water'))/100
    zoo_respire = request.POST.get('zoo_respire')
    #characteristics_benthic_invertebrates = request.POST.get('char_beninv')
    wb_beninv = float(request.POST.get('beninv_ww'))
    v_lb_beninv = float(request.POST.get('beninv_lipid'))/100
    v_nb_beninv = float(request.POST.get('beninv_NLOM'))/100
    v_wb_beninv = float(request.POST.get('beninv_water'))/100
    beninv_respire = request.POST.get('beninv_respire')
    #characteristics_ff = request.POST.get('char_ff')
    wb_ff = float(request.POST.get('ff_ww'))
    v_lb_ff = float(request.POST.get('ff_lipid'))/100
    v_nb_ff = float(request.POST.get('ff_NLOM'))/100
    v_wb_ff = float(request.POST.get('ff_water'))/100
    ff_respire = request.POST.get('ff_respire')
    #characteristics_smfish = request.POST.get('char_sfish')
    wb_sf = float(request.POST.get('sfish_ww'))
    v_lb_sf = float(request.POST.get('sfish_lipid'))/100
    v_nb_sf = float(request.POST.get('sfish_NLOM'))/100
    v_wb_sf = float(request.POST.get('sfish_water'))/100
    sfish_respire = request.POST.get('sfish_respire')
    #characteristics_medfish = request.POST.get('char_mfish')
    wb_mf = float(request.POST.get('mfish_ww'))
    v_lb_mf = float(request.POST.get('mfish_lipid'))/100
    v_nb_mf = float(request.POST.get('mfish_NLOM'))/100
    v_wb_mf = float(request.POST.get('mfish_water'))/100
    mfish_respire = request.POST.get('mfish_respire')
    #characteristics_larfish = request.POST.get('char_lfish')
    wb_lf = float(request.POST.get('lfish_ww'))
    v_lb_lf = float(request.POST.get('lfish_lipid'))/100
    v_nb_lf = float(request.POST.get('lfish_NLOM'))/100
    v_wb_lf = float(request.POST.get('lfish_water'))/100
    lfish_respire = request.POST.get('lfish_respire')
    rate_constants = request.POST.get('rate_c')
    # phytoplankton growth rate constant
    kg_phytoplankton = 0.1
    # phytoplankton diet uptake rate constant
    kd_phytoplankton = 0
    #phytoplankton fecal elimination rate constant  
    ke_phytoplankton = 0
    # fraction of respiratory ventilation involving overlying water
    mo_phytoplankton = 1
    # fraction of respiratory ventilation involving pore water
    mp_phytoplankton = 0    
    # rate constant for pesticide metabolic transformation
    km_phytoplankton = 0
     # rate constant for pesticide metabolic transformation
    km_zoo = 0

    # k_bw_phytoplankton = 0
    # k_bw_zoo = 0
    # k_bw_beninv = 0
    # k_bw_ff = 0
    # k_bw_sf = 0
    # k_bw_mf = 0
    # k_bw_lf = 0
    # cb_phytoplankton_v = 0
    # cb_zoo_v = 0
    # cb_beninv_v = 0
    # cb_ff_v = 0
    # cb_sf_v = 0
    # cb_mf_v = 0
    # cb_lf_v = 0
    k1_phytoplankton = float(request.POST.get('phyto_k1'))
    k2_phytoplankton = float(request.POST.get('phyto_k2'))
    kd_phytoplankton = float(request.POST.get('phyto_kd'))
    ke_phytoplankton = float(request.POST.get('phyto_ke'))
    km_phytoplankton = float(request.POST.get('phyto_km'))
    k1_zoo = float(request.POST.get('zoo_k1'))
    k2_zoo = float(request.POST.get('zoo_k2'))
    kd_zoo = float(request.POST.get('zoo_kd'))
    ke_zoo = float(request.POST.get('zoo_ke'))
    km_zoo = float(request.POST.get('zoo_km'))
    k1_beninv = float(request.POST.get('beninv_k1'))
    k2_beninv = float(request.POST.get('beninv_k2'))
    kd_beninv = float(request.POST.get('beninv_kd'))
    ke_beninv = float(request.POST.get('beninv_ke'))
    km_beninv = float(request.POST.get('beninv_km'))
    k1_ff = float(request.POST.get('ff_k1'))
    k2_ff = float(request.POST.get('ff_k2'))
    kd_ff = float(request.POST.get('ff_kd'))
    ke_ff = float(request.POST.get('ff_ke'))
    km_ff = float(request.POST.get('ff_km'))
    k1_sf = float(request.POST.get('sfish_k1'))
    k2_sf = float(request.POST.get('sfish_k2'))
    kd_sf = float(request.POST.get('sfish_kd'))
    ke_sf = float(request.POST.get('sfish_ke'))
    km_sf = float(request.POST.get('sfish_km'))
    k1_mf = float(request.POST.get('mfish_k1'))
    k2_mf = float(request.POST.get('mfish_k2'))
    kd_mf = float(request.POST.get('mfish_kd'))
    ke_mf = float(request.POST.get('mfish_ke'))
    km_mf = float(request.POST.get('mfish_km'))
    k1_lf = float(request.POST.get('lfish_k1'))
    k2_lf = float(request.POST.get('lfish_k2'))
    kd_lf = float(request.POST.get('lfish_kd'))
    ke_lf = float(request.POST.get('lfish_ke'))
    km_lf = float(request.POST.get('lfish_km'))

    # else: # calculate values for rate constants
    #     k_bw_phytoplankton = kabam_model.k_bw_phytoplankton_f(v_lb_phytoplankton, v_nb_phytoplankton, k_ow, v_wb_phytoplankton)
    #     k1_phytoplankton = k1_phytoplankton_f(k_ow)
    #     k2_phytoplankton = k2_phytoplankton_f(k_ow, k1_phytoplankton, k_bw_phytoplankton)
    #     k_bw_zoo = k_bw_zoo_f(v_lb_zoo, k_ow, v_nb_zoo, v_wb_zoo)
    #     k1_zoo = k1_zoo_f(k_ow, wb_zoo, c_ox)
    #     k2_zoo = k2_zoo_f(k_bw_zoo, k1_zoo)
    #     kd_zoo = kd_zoo_f(k_ow, wb_zoo, w_t)               
    #     ke_zoo = ke_zoo_f(k_ow, wb_zoo, v_lb_zoo, v_nb_zoo, zoo_p_sediment, s_lipid, s_NLOM, zoo_p_phyto, v_lb_phytoplankton, v_nb_phytoplankton, s_water, v_wb_phytoplankton, w_t, v_wb_zoo)
    #     k_bw_beninv = k_bw_beninv_f(v_lb_beninv, k_ow, v_nb_beninv, v_wb_beninv)                
    #     k1_beninv = k1_beninv_f(k_ow, wb_beninv, c_ox)        
    #     k2_beninv = k2_beninv_f(k1_beninv, k_bw_beninv)                
    #     kd_beninv = kd_beninv_f(k_ow, wb_beninv, w_t)                
    #     ke_beninv = ke_beninv_f(k_ow, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, wb_beninv, w_t, v_lb_beninv, v_nb_beninv, v_wb_beninv)
    #     k_bw_ff = k_bw_ff_f(v_lb_ff, k_ow, v_nb_ff, v_wb_ff)                
    #     k1_ff = k1_ff_f(k_ow, wb_ff, c_ox)
    #     k2_ff = k2_ff_f(k1_ff, k_bw_ff)                
    #     kd_ff = kd_ff_f(k_ow, wb_ff, w_t, c_ss, c_ox)
    #     ke_ff = ke_ff_f(k_ow, ff_p_sediment, v_lb_ff, v_nb_ff, v_wb_ff, ff_p_phytoplankton,  c_ss, c_ox, s_lipid, v_lb_phytoplankton, ff_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, wb_ff, w_t)
    #     k_bw_sf = k_bw_sf_f(v_lb_sf, k_ow, v_nb_sf, v_wb_sf)                
    #     k1_sf = k1_sf_f(k_ow, wb_sf, c_ox)
    #     k2_sf = k2_sf_f(k1_sf, k_bw_sf)
    #     kd_sf = kd_sf_f(k_ow, wb_sf, w_t, c_ss, c_ox)
    #     ke_sf = ke_sf_f(k_ow, v_lb_sf, v_nb_sf, v_wb_sf, c_ox, ff_p_sediment, s_lipid, ff_p_phytoplankton, ff_p_zooplankton, s_NLOM, v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, c_ss, wb_ff,  wb_sf, w_t, v_nb_beninv, v_nb_ff, sf_p_sediment, sf_p_phytoplankton, v_lb_phytoplankton, sf_p_benthic_invertebrates, v_lb_beninv, sf_p_zooplankton, v_lb_zoo, v_wb_beninv, v_wb_ff, sf_p_filter_feeders, v_lb_ff)
    #     k_bw_mf = k_bw_mf_f(v_lb_mf, k_ow, v_nb_mf, v_wb_mf)                
    #     k1_mf = k1_mf_f(k_ow, wb_mf, c_ox)
    #     k2_mf = k2_mf_f(k1_mf, k_bw_mf) 
    #     kd_mf = kd_mf_f(k_ow, wb_mf, w_t, c_ss, c_ox)
    #     ke_mf = ke_mf_f(k_ow, v_lb_mf, v_nb_mf, v_wb_mf, wb_mf, w_t, s_lipid, v_lb_phytoplankton, v_lb_beninv, v_lb_zoo,  v_lb_ff, v_lb_sf, s_NLOM,  v_nb_phytoplankton, v_nb_beninv,  v_nb_zoo,  v_nb_ff, v_nb_sf, mf_p_sediment, s_water, mf_p_phytoplankton, v_wb_phytoplankton, mf_p_benthic_invertebrates, v_wb_beninv, mf_p_zooplankton, v_wb_zoo, mf_p_filter_feeders, v_wb_ff, mf_p_small_fish, v_wb_sf)
    #     k_bw_lf = k_bw_lf_f(v_lb_lf, k_ow, v_nb_lf, v_wb_lf)
    #     k1_lf = k1_lf_f(k_ow, wb_lf, c_ox)
    #     k2_lf = k2_lf_f(k1_lf, k_bw_lf)
    #     kd_lf = kd_lf_f(k_ow, wb_lf, w_t, c_ss, c_ox)
    #     ke_lf = ke_lf_f(k_ow, v_lb_lf, v_nb_lf, v_wb_lf, wb_lf, s_lipid, lf_p_sediment, v_lb_phytoplankton, lf_p_phytoplankton, v_lb_beninv, v_lb_zoo, lf_p_benthic_invertebrates, lf_p_zooplankton, lf_p_filter_feeders, v_lb_ff, v_lb_sf, lf_p_small_fish, s_water, lf_p_medium_fish, v_nb_mf, v_wb_phytoplankton, v_wb_beninv, v_wb_zoo, v_wb_ff, v_wb_sf, wb_mf, w_t, mf_p_sediment, s_NLOM, mf_p_phytoplankton, v_nb_phytoplankton, v_lb_mf, v_wb_mf, mf_p_benthic_invertebrates, v_nb_beninv, mf_p_zooplankton, v_nb_zoo, mf_p_filter_feeders, v_nb_ff, mf_p_small_fish, v_nb_sf)

    # cb_phytoplankton_v = cb_phytoplankton_f(k1_phytoplankton, c_wdp, c_wto, k2_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_ow, x_doc, x_poc)   
    # cb_zoo_v = cb_zoo_f(k_ow, wb_zoo, w_t, k1_phytoplankton, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wdp, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, oc, x_poc, x_doc, v_lb_phytoplankton, v_nb_phytoplankton, v_wb_phytoplankton, k_bw_phytoplankton, zoo_p_phyto, zoo_p_sediment)
    # cb_beninv_v = cb_beninv_f(x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv)
    # cb_ff_v = cb_ff_f(k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, w_t, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates)
    # cb_sf_v = cb_sf_f(wb_sf, k1_sf, k2_sf, kd_sf, ke_sf, sf_p_benthic_invertebrates, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, sf_p_phytoplankton, sf_p_sediment, sf_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates, sf_p_filter_feeders)
    # cb_mf_v = cb_mf_f(k1_mf, k2_mf, kd_mf, ke_mf, wb_mf, mf_p_sediment, mf_p_phytoplankton, mf_p_zooplankton, mf_p_benthic_invertebrates, mf_p_filter_feeders, mf_p_small_fish, wb_sf, k1_sf, k2_sf, kd_sf, ke_sf, sf_p_benthic_invertebrates, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, sf_p_phytoplankton, sf_p_sediment, sf_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates, sf_p_filter_feeders)
    # cb_lf_v = cb_lf_f(kd_lf, k2_lf, ke_lf, k1_lf, wb_lf, wb_mf, lf_p_sediment, lf_p_phytoplankton, lf_p_zooplankton, lf_p_benthic_invertebrates, k1_mf, k2_mf, kd_mf, ke_mf, mf_p_sediment, mf_p_phytoplankton, mf_p_zooplankton, lf_p_filter_feeders, lf_p_small_fish, lf_p_medium_fish, mf_p_benthic_invertebrates, mf_p_filter_feeders, mf_p_small_fish, wb_sf, k1_sf, k2_sf, kd_sf, ke_sf, sf_p_benthic_invertebrates, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, sf_p_phytoplankton, sf_p_sediment, sf_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates, sf_p_filter_feeders)


    #     k_bw_phytoplankton = k_bw_phytoplankton_f(v_lb_phytoplankton, v_nb_phytoplankton, k_ow, v_wb_phytoplankton)
    #     k1_phytoplankton = k1_phytoplankton_f(k_ow)
    #     k2_phytoplankton = k2_phytoplankton_f(k_ow, k1_phytoplankton, k_bw_phytoplankton)
    #     k_bw_zoo = k_bw_zoo_f(v_lb_zoo, k_ow, v_nb_zoo, v_wb_zoo)
    #     k1_zoo = k1_zoo_f(k_ow, wb_zoo, c_ox)
    #     k2_zoo = k2_zoo_f(k_bw_zoo, k1_zoo)
    #     kd_zoo = kd_zoo_f(k_ow, wb_zoo, w_t)               
    #     ke_zoo = ke_zoo_f(k_ow, wb_zoo, v_lb_zoo, v_nb_zoo, zoo_p_sediment, s_lipid, s_NLOM, zoo_p_phyto, v_lb_phytoplankton, v_nb_phytoplankton, s_water, v_wb_phytoplankton, w_t, v_wb_zoo)
    #     k_bw_beninv = k_bw_beninv_f(v_lb_beninv, k_ow, v_nb_beninv, v_wb_beninv)                
    #     k1_beninv = k1_beninv_f(k_ow, wb_beninv, c_ox)        
    #     k2_beninv = k2_beninv_f(k1_beninv, k_bw_beninv)                
    #     kd_beninv = kd_beninv_f(k_ow, wb_beninv, w_t)                
    #     ke_beninv = ke_beninv_f(k_ow, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, wb_beninv, w_t, v_lb_beninv, v_nb_beninv, v_wb_beninv)
    #     k_bw_ff = k_bw_ff_f(v_lb_ff, k_ow, v_nb_ff, v_wb_ff)                
    #     k1_ff = k1_ff_f(k_ow, wb_ff, c_ox)
    #     k2_ff = k2_ff_f(k1_ff, k_bw_ff)                
    #     kd_ff = kd_ff_f(k_ow, wb_ff, w_t, c_ss, c_ox)
    #     ke_ff = ke_ff_f(k_ow, ff_p_sediment, v_lb_ff, v_nb_ff, v_wb_ff, ff_p_phytoplankton,  c_ss, c_ox, s_lipid, v_lb_phytoplankton, ff_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, wb_ff, w_t)
    #     k_bw_sf = k_bw_sf_f(v_lb_sf, k_ow, v_nb_sf, v_wb_sf)                
    #     k1_sf = k1_sf_f(k_ow, wb_sf, c_ox)
    #     k2_sf = k2_sf_f(k1_sf, k_bw_sf)
    #     kd_sf = kd_sf_f(k_ow, wb_sf, w_t, c_ss, c_ox)
    #     ke_sf = ke_sf_f(k_ow, v_lb_sf, v_nb_sf, v_wb_sf, c_ox, ff_p_sediment, s_lipid, ff_p_phytoplankton, ff_p_zooplankton, s_NLOM, v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, c_ss, wb_ff,  wb_sf, w_t, v_nb_beninv, v_nb_ff, sf_p_sediment, sf_p_phytoplankton, v_lb_phytoplankton, sf_p_benthic_invertebrates, v_lb_beninv, sf_p_zooplankton, v_lb_zoo, v_wb_beninv, v_wb_ff, sf_p_filter_feeders, v_lb_ff)
    #     k_bw_mf = k_bw_mf_f(v_lb_mf, k_ow, v_nb_mf, v_wb_mf)                
    #     k1_mf = k1_mf_f(k_ow, wb_mf, c_ox)
    #     k2_mf = k2_mf_f(k1_mf, k_bw_mf) 
    #     kd_mf = kd_mf_f(k_ow, wb_mf, w_t, c_ss, c_ox)
    #     ke_mf = ke_mf_f(k_ow, v_lb_mf, v_nb_mf, v_wb_mf, wb_mf, w_t, s_lipid, v_lb_phytoplankton, v_lb_beninv, v_lb_zoo,  v_lb_ff, v_lb_sf, s_NLOM,  v_nb_phytoplankton, v_nb_beninv,  v_nb_zoo,  v_nb_ff, v_nb_sf, mf_p_sediment, s_water, mf_p_phytoplankton, v_wb_phytoplankton, mf_p_benthic_invertebrates, v_wb_beninv, mf_p_zooplankton, v_wb_zoo, mf_p_filter_feeders, v_wb_ff, mf_p_small_fish, v_wb_sf)
    #     k_bw_lf = k_bw_lf_f(v_lb_lf, k_ow, v_nb_lf, v_wb_lf)
    #     k1_lf = k1_lf_f(k_ow, wb_lf, c_ox)
    #     k2_lf = k2_lf_f(k1_lf, k_bw_lf)
    #     kd_lf = kd_lf_f(k_ow, wb_lf, w_t, c_ss, c_ox)
    #     ke_lf = ke_lf_f(k_ow, v_lb_lf, v_nb_lf, v_wb_lf, wb_lf, s_lipid, lf_p_sediment, v_lb_phytoplankton, lf_p_phytoplankton, v_lb_beninv, v_lb_zoo, lf_p_benthic_invertebrates, lf_p_zooplankton, lf_p_filter_feeders, v_lb_ff, v_lb_sf, lf_p_small_fish, s_water, lf_p_medium_fish, v_nb_mf, v_wb_phytoplankton, v_wb_beninv, v_wb_zoo, v_wb_ff, v_wb_sf, wb_mf, w_t, mf_p_sediment, s_NLOM, mf_p_phytoplankton, v_nb_phytoplankton, v_lb_mf, v_wb_mf, mf_p_benthic_invertebrates, v_nb_beninv, mf_p_zooplankton, v_nb_zoo, mf_p_filter_feeders, v_nb_ff, mf_p_small_fish, v_nb_sf)
        
    # cb_phytoplankton_v = cb_phytoplankton_f(k1_phytoplankton, c_wdp, c_wto, k2_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_ow, x_doc, x_poc)   
    # cb_zoo_v = cb_zoo_f(k_ow, wb_zoo, w_t, k1_phytoplankton, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wdp, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, oc, x_poc, x_doc, v_lb_phytoplankton, v_nb_phytoplankton, v_wb_phytoplankton, k_bw_phytoplankton, zoo_p_phyto, zoo_p_sediment)
    # cb_beninv_v = cb_beninv_f(x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv)
    # cb_ff_v = cb_ff_f(k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, w_t, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates)
    # cb_sf_v = cb_sf_f(wb_sf, k1_sf, k2_sf, kd_sf, ke_sf, sf_p_benthic_invertebrates, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, sf_p_phytoplankton, sf_p_sediment, sf_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates, sf_p_filter_feeders)
    # cb_mf_v = cb_mf_f(k1_mf, k2_mf, kd_mf, ke_mf, wb_mf, mf_p_sediment, mf_p_phytoplankton, mf_p_zooplankton, mf_p_benthic_invertebrates, mf_p_filter_feeders, mf_p_small_fish, wb_sf, k1_sf, k2_sf, kd_sf, ke_sf, sf_p_benthic_invertebrates, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, sf_p_phytoplankton, sf_p_sediment, sf_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates, sf_p_filter_feeders)
    # cb_lf_v = cb_lf_f(kd_lf, k2_lf, ke_lf, k1_lf, wb_lf, wb_mf, lf_p_sediment, lf_p_phytoplankton, lf_p_zooplankton, lf_p_benthic_invertebrates, k1_mf, k2_mf, kd_mf, ke_mf, mf_p_sediment, mf_p_phytoplankton, mf_p_zooplankton, lf_p_filter_feeders, lf_p_small_fish, lf_p_medium_fish, mf_p_benthic_invertebrates, mf_p_filter_feeders, mf_p_small_fish, wb_sf, k1_sf, k2_sf, kd_sf, ke_sf, sf_p_benthic_invertebrates, ff_p_phytoplankton, ff_p_sediment, ff_p_zooplankton, k1_ff, k2_ff, kd_ff, ke_ff, wb_ff, sf_p_phytoplankton, sf_p_sediment, sf_p_zooplankton, x_poc, x_doc, k_ow, k1_beninv, k2_beninv, kd_beninv, ke_beninv, wb_beninv, c_ox, w_t, k1_phytoplankton, c_wdp, k1_zoo, k2_zoo, kd_zoo, ke_zoo, c_wto, k2_phytoplankton, kd_phytoplankton, ke_phytoplankton, kg_phytoplankton, km_phytoplankton, mo_phytoplankton, mp_phytoplankton, k_oc, v_wb_beninv, oc, k_bw_phytoplankton, zoo_p_sediment, zoo_p_phyto, wb_zoo, beninv_p_sediment, s_lipid, beninv_p_phytoplankton, v_lb_phytoplankton, beninv_p_zooplankton, v_lb_zoo, s_NLOM,  v_nb_phytoplankton, v_nb_zoo, s_water, v_wb_phytoplankton, v_wb_zoo, v_lb_beninv, v_nb_beninv, ff_p_benthic_invertebrates, sf_p_filter_feeders)



    kabam_obj = kabam_model.kabam(
        True,True,'single',chemical_name,l_kow,k_oc,c_wdp,water_column_EEC,c_wto,mineau_scaling_factor,x_poc,x_doc,c_ox,w_t,c_ss,oc,k_ow,
        Species_of_the_tested_bird,bw_quail,bw_duck,bwb_other,avian_ld50,avian_lc50,avian_noaec,m_species,bw_rat,bwm_other,mammalian_ld50,mammalian_lc50,mammalian_chronic_endpoint,
        lf_p_sediment,lf_p_phytoplankton,lf_p_zooplankton,lf_p_benthic_invertebrates,lf_p_filter_feeders,lf_p_small_fish,lf_p_medium_fish,
        mf_p_sediment,mf_p_phytoplankton,mf_p_zooplankton,mf_p_benthic_invertebrates,mf_p_filter_feeders,mf_p_small_fish,
        sf_p_sediment,sf_p_phytoplankton,sf_p_zooplankton,sf_p_benthic_invertebrates,sf_p_filter_feeders,
        ff_p_sediment,ff_p_phytoplankton,ff_p_zooplankton,ff_p_benthic_invertebrates,
        beninv_p_sediment,beninv_p_phytoplankton,beninv_p_zooplankton,
        zoo_p_sediment,zoo_p_phyto,
        s_lipid,s_NLOM,s_water,
        v_lb_phytoplankton,v_nb_phytoplankton,v_wb_phytoplankton,wb_zoo,v_lb_zoo,v_nb_zoo,v_wb_zoo,wb_beninv,v_lb_beninv,v_nb_beninv,v_wb_beninv,wb_ff,v_lb_ff,v_nb_ff,v_wb_ff,wb_sf,v_lb_sf,v_nb_sf,v_wb_sf,wb_mf,v_lb_mf,v_nb_mf,v_wb_mf,wb_lf,v_lb_lf,v_nb_lf,v_wb_lf,
        kg_phytoplankton,kd_phytoplankton,ke_phytoplankton,mo_phytoplankton,mp_phytoplankton,km_phytoplankton,km_zoo,
        k1_phytoplankton,k2_phytoplankton,
        k1_zoo,k2_zoo,kd_zoo,ke_zoo,k1_beninv,k2_beninv,kd_beninv,ke_beninv,km_beninv,
        k1_ff,k2_ff,kd_ff,ke_ff,km_ff,k1_sf,k2_sf,kd_sf,ke_sf,km_sf,k1_mf,k2_mf,kd_mf,ke_mf,km_mf,k1_lf,k2_lf,kd_lf,ke_lf,km_lf,
        rate_constants,s_respire,phyto_respire,zoo_respire,beninv_respire,ff_respire,sfish_respire,mfish_respire,lfish_respire, None)

        # cb_phytoplankton_v,cb_zoo_v,cb_beninv_v,cb_ff_v,cb_sf_v,cb_mf_v,cb_lf_v   ***Removed from kabam_obj above***

    return kabam_obj