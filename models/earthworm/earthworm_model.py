"""
.. module:: earthworm_model
   :synopsis: A useful module indeed.
"""

from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('earthworm Model')
import os
import requests

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']

class earthworm(object):
    def __init__(self, set_variables=True, run_methods=True,run_type='single',k_ow=1,l_f_e=1,c_s=1,k_d=1,p_s=1,c_w=1,m_w=1,p_e=1,vars_dict=None):
        self.set_default_variables()
        self.jid = rest_funcs.gen_jid()
        
        if set_variables:
            if vars_dict != None:
                self.__dict__.update(vars_dict)
            else:
                self.run_methods = run_methods
                self.k_ow = k_ow
                self.l_f_e = l_f_e
                self.c_s = c_s
                self.k_d = k_d
                self.p_s = p_s
                self.c_w = c_w
                self.m_w = m_w
                self.p_e = p_e

                all_dic = {"k_ow":self.k_ow, "l_f_e":self.l_f_e, "c_s":self.c_s, "k_d":self.k_d, "p_s":self.p_s, "c_w":self.c_w,
                           "m_w":self.m_w, "p_e":self.p_e}
                data = json.dumps(all_dic)
                self.jid = rest_funcs.gen_jid()
                url=url_part1 + '/earthworm/' + self.jid 
                response = requests.post(url=url, data=data, headers=http_headers, timeout=60)
                output_val = json.loads(response.content)['result']
                for key, value in output_val.items():
                    setattr(self, key, value)

    def set_default_variables(self):
        self.k_ow = -1
        self.l_f_e = -1
        self.c_s = -1
        self.k_d = -1
        self.p_s = -1
        self.c_w = -1
        self.m_w = -1
        self.p_e = -1
        self.earthworm_fugacity_out = -1
