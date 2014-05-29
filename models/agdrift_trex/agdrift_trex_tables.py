import datetime
from models.agdrift import agdrift_model,agdrift_tables
from models.trex2 import trex2_model,trex2_tables

#########################################################################
########################## Linking the models ###########################
#########################################################################

def merge(ob1, ob2):
        """
        an object's __dict__ contains all its 
        attributes, methods, docstrings, etc.
        """
        ob1.__dict__.update(ob2.__dict__)
        return ob1
        # merge the two class instances into one instance


agdrift_obj = agdrift_model.agdrift(True, True, 'single', drop_size, ecosystem_type, application_method, boom_height, orchard_type, rate_out[0], distance, aquatic_type, calculation_input, None)
x_agdrif=agdrift_obj.x
trex_obj = trex2_model.trex2('single', chem_name, use, formu_name, a_i, Application_type, seed_treatment_formulation_name, seed_crop, seed_crop_v, r_s, b_w, p_i, den, h_l, n_a, [agdrift_obj.init_avg_dep_foa*i for i in rate_out], day_out,
                             ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird_sm, aw_bird_md, aw_bird_lg, 
                             Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                             tw_bird_ld50, tw_bird_lc50, tw_bird_NOAEC, tw_bird_NOAEL, x, ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm_sm, aw_mamm_md, aw_mamm_lg, tw_mamm,
                             m_s_r_p)

#Note: If you need to rebuild the output page based on saved class, 
#variables named x_agdrif and x_trex in the class agdrift_trex_obj
#are x in their own instance (agdrift_obj.x, trex_obj.x).
agdrift_trex_obj = merge(agdrift_obj, trex_obj)
agdrift_trex_obj.x_agdrif=x_agdrif
agdrift_trex_obj.x_trex=trex_obj.x
logging.info(vars(agdrift_trex_obj))


#########################################################################
############################ Output Tables ##############################
#########################################################################

def timestamp(agdrift_trex_obj):
    st = datetime.datetime.strptime(agdrift_trex_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
    <b>Agdrift-Trex<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html
