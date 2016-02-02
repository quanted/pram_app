"""
.. module:: agdrift_model
   :synopsis: A useful module indeed.
"""

import os
from bisect import *
import logging
from REST import auth_s3, rest_funcs
logger = logging.getLogger('agdrift Model')
import json
import requests


# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


class agdrift(object):
    def __init__(self, set_variables=True, run_methods=True, run_type='single', drop_size = '', ecosystem_type = '',
                 application_method = '', boom_height = '', orchard_type = '', application_rate=1, distance=1,
                 aquatic_type='', calculation_input='', out_init_avg_dep_foa = 1, out_avg_depo_lbac = 1,
                 out_avg_depo_gha  = 1, out_deposition_ngl = 1, out_deposition_mgcm = 1, out_nasae = 1, out_y = 1,
                 out_x = 1, out_express_y = 1, vars_dict=None):
        self.set_default_variables()
        self.jid = rest_funcs.gen_jid()
        
        if set_variables:
            if vars_dict != None:
                self.__dict__.update(vars_dict)
            else:
                self.set_variables(run_type, drop_size, ecosystem_type, application_method, boom_height, orchard_type,
                                   application_rate, distance, aquatic_type, calculation_input, out_init_avg_dep_foa,
                                   out_avg_depo_gha, out_avg_depo_lbac, out_deposition_ngl, out_deposition_mgcm, out_nasae, out_y, out_x, out_express_y)

    def set_default_variables(self):
        #Currently used variables
        self.version_agdrift = ''
        self.run_type = "single"
        self.drop_size = ''
        self.ecosystem_type = '' 
        self.application_method = ''
        self.boom_height = ''
        self.orchard_type = ''
        self.application_rate = 1
        self.distance = 1
        self.aquatic_type = ''
        self.calculation_input = ''
        self.out_init_avg_dep_foa = -1
        self.out_avg_depo_lbac = -1
        self.out_avg_depo_gha  = -1
        self.out_deposition_ngl = -1
        self.out_deposition_mgcm = -1
        self.out_nasae = -1
        self.out_y = -1
        self.out_x = -1
        self.out_express_y = -1
        self.loop_indx = '1'

    def set_variables(self, run_type, drop_size, ecosystem_type, application_method, boom_height, orchard_type,
                      application_rate, distance, aquatic_type, calculation_input, out_init_avg_dep_foa, out_avg_depo_gha,
                      out_avg_depo_lbac, out_deposition_ngl, out_deposition_mgcm, out_nasae, out_y, out_x, out_express_y):
        self.run_type = run_type
        self.drop_size = drop_size
        self.ecosystem_type = ecosystem_type 
        self.application_method = application_method
        self.boom_height = boom_height
        self.orchard_type = orchard_type  
        self.application_rate = application_rate
        self.distance = distance
        self.aquatic_type = aquatic_type
        self.calculation_input = calculation_input
        self.out_init_avg_dep_foa = out_init_avg_dep_foa
        self.out_avg_depo_gha = out_avg_depo_gha
        self.out_avg_depo_lbac = out_avg_depo_lbac
        self.out_deposition_ngl = out_deposition_ngl
        self.out_deposition_mgcm = out_deposition_mgcm
        self.out_nasae = out_nasae
        self.out_y = out_y
        self.out_x = out_x
        self.out_express_y = out_express_y

        all_dic = {"drop_size":drop_size, "ecosystem_type":ecosystem_type, "application_method":application_method, 
                   "boom_height":boom_height, "orchard_type":orchard_type, "application_rate":application_rate, 
                   "distance":distance, "aquatic_type":aquatic_type, "calculation_input":calculation_input, 
                   "out_init_avg_dep_foa":out_init_avg_dep_foa, "out_avg_depo_gha":out_avg_depo_gha, "out_avg_depo_lbac":out_avg_depo_lbac,
                   "out_deposition_ngl":out_deposition_ngl, "out_deposition_mgcm":out_deposition_mgcm, "out_nasae":out_nasae, "out_y":out_y, "out_x":out_x,
                   "out_express_y":out_express_y}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/agdrift/' + self.jid 
        response = requests.post(url=url, data=data, headers=http_headers, timeout=60)
        output_val = json.loads(response.content)['result']
        for key, value in output_val.items():
            setattr(self, key, value)
