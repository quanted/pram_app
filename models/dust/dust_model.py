"""
.. module:: dust_batch_runner
   :synopsis: A useful module indeed.
"""

from REST import auth_s3, rest_funcs
import json
import logging
import os
import requests

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


class dust(object):
    def __init__(self, set_variables=True, run_methods=True, run_type='single', chemical_name='', label_epa_reg_no='', ar_lb=1, frac_pest_surface=1, dislodge_fol_res=1,  bird_acute_oral_study="", bird_study_add_comm="",
              low_bird_acute_ld50=1, test_bird_bw=1, mineau_scaling_factor=1, mamm_acute_derm_study='', mamm_study_add_comm='',  mam_acute_derm_ld50=1, mam_acute_oral_ld50=1, test_mam_bw=1, vars_dict=None):
        self.set_default_variables()
        self.jid = rest_funcs.gen_jid()

        if set_variables:
            if vars_dict != None:
                self.__dict__.update(vars_dict)
            else:
                self.set_variables(run_type, chemical_name, label_epa_reg_no, ar_lb, frac_pest_surface, dislodge_fol_res,  bird_acute_oral_study, bird_study_add_comm,
              low_bird_acute_ld50, test_bird_bw, mineau_scaling_factor, mamm_acute_derm_study, mamm_study_add_comm,  mam_acute_derm_ld50, mam_acute_oral_ld50, test_mam_bw)


    def set_default_variables(self):
        #Currently used variables
        self.run_type = "single"
        self.chemical_name=''
        self.label_epa_reg_no=''
        self.ar_lb=1
        self.frac_pest_surface=1
        self.dislodge_fol_res=1
        self.bird_acute_oral_study=1
        self.bird_study_add_comm=''
        self.low_bird_acute_ld50=1
        self.test_bird_bw=1
        self.mineau_scaling_factor=1
        self.mamm_acute_derm_study=''
        self.mamm_study_add_comm=''
        #self.aviandermaltype=1
        self.mam_acute_derm_ld50=1
        self.mam_acute_oral_ld50=1
        self.test_mam_bw=1


    def set_variables(self, run_type, chemical_name, label_epa_reg_no, ar_lb, frac_pest_surface, dislodge_fol_res, bird_acute_oral_study, bird_study_add_comm,
              low_bird_acute_ld50, test_bird_bw, mineau_scaling_factor, mamm_acute_derm_study, mamm_study_add_comm, mam_acute_derm_ld50, mam_acute_oral_ld50, test_mam_bw):
        self.run_type = run_type
        self.chemical_name=chemical_name
        self.label_epa_reg_no=label_epa_reg_no
        self.ar_lb=ar_lb
        self.frac_pest_surface=frac_pest_surface
        self.dislodge_fol_res=dislodge_fol_res
        self.bird_acute_oral_study=bird_acute_oral_study
        self.bird_study_add_comm=bird_study_add_comm
        self.low_bird_acute_ld50=low_bird_acute_ld50
        self.test_bird_bw=test_bird_bw
        self.mineau_scaling_factor=mineau_scaling_factor
        self.mamm_acute_derm_study=mamm_acute_derm_study
        self.mamm_study_add_comm=mamm_study_add_comm
        #self.aviandermaltype=aviandermaltype
        self.mam_acute_derm_ld50=mam_acute_derm_ld50
        self.mam_acute_oral_ld50 = mam_acute_oral_ld50
        self.test_mam_bw=test_mam_bw

        all_dic = {"chemical_name":self.chemical_name, "label_epa_reg_no":self.label_epa_reg_no, 
                   "ar_lb":self.ar_lb, "frac_pest_surface":self.frac_pest_surface, "dislodge_fol_res":self.dislodge_fol_res, 
                   "bird_acute_oral_study":self.bird_acute_oral_study, "bird_study_add_comm":self.bird_study_add_comm, 
                   "low_bird_acute_ld50":self.low_bird_acute_ld50, "test_bird_bw":self.test_bird_bw, 
                   "mineau_scaling_factor":self.mineau_scaling_factor, "mamm_acute_derm_study":self.mamm_acute_derm_study, 
                   "mamm_study_add_comm":self.mamm_study_add_comm, "mam_acute_derm_ld50":self.mam_acute_derm_ld50, 
                   "mam_acute_oral_ld50":self.mam_acute_oral_ld50, "test_mam_bw":self.test_mam_bw}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/dust/' + self.jid 
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        output_val = json.loads(response.content)['result']
        for key, value in output_val.items():
            setattr(self, key, value)

