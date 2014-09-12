"""
.. module:: rice_model
   :synopsis: A useful module indeed.
"""

from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('Rice Model')
import os
import requests

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


class rice(object):
    def __init__(self, set_variables=True,run_methods=True,version_rice="1.0",
                run_type = "single",chemical_name='', 
                mai=1, dsed=1, a=1, pb=1, dw=1, osed=1, kd=1, 
                vars_dict=None):
        self.set_default_variables()
        self.jid = rest_funcs.gen_jid()

        if set_variables:
            if vars_dict != None:
                self.__dict__.update(vars_dict)
            else:
                self.set_variables(version_rice,run_type,chemical_name,mai,dsed,a,pb,dw,osed,kd)

    def set_default_variables(self):
        self.version_rice = ''
        self.run_type = "single"
        self.chemical_name = ''
        self.mai = -1
        self.dsed = -1
        self.a = -1
        self.pb = -1
        self.dw = -1
        self.osed = -1
        self.kd = -1

    def set_variables(self,version_rice,run_type,chemical_name,mai,dsed,a,pb,dw,osed,kd):
        self.version_rice = version_rice
        self.run_type = run_type
        self.chemical_name = chemical_name
        self.mai = mai
        self.dsed = dsed
        self.a = a
        self.pb = pb
        self.dw = dw
        self.osed = osed
        self.kd = kd
        all_dic = {"version_rice":self.version_rice,"run_type":self.run_type,"chemical_name":self.chemical_name,
            "mai":self.mai, "dsed":self.dsed, "a":self.a, "pb":self.pb, "dw":self.dw,"osed":self.osed, "kd":self.kd}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/rice/' + self.jid 
        #response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url=url, data=data, headers=http_headers, timeout=60) 
        output_val = json.loads(response.content)['result']
        for key, value in output_val.items():
            setattr(self, key, value)

