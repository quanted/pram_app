"""
.. module:: terrplant_model
   :synopsis: A useful module indeed.
"""
from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('Terrplant Model')
import os
import requests

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']

class terrplant(object):
    def __init__(self, set_variables=True, run_methods=True, version_terrplant='1.2.2', 
            run_type = "single", application_rate=1, incorporation_depth=1, runoff_fraction=1, 
            drift_fraction=1, ec25_nonlisted_seedling_emergence_monocot=1, ec25_nonlisted_seedling_emergence_dicot=1, 
            noaec_listed_seedling_emergence_monocot=1, noaec_listed_seedling_emergence_dicot=1,
            chemical_name='', pc_code='', use='', application_method='', application_form='', solubility=1, 
            vars_dict=None,):
        self.set_default_variables()
        # self.jid = rest_funcs.gen_jid()

        if set_variables:
            if vars_dict != None:
                self.__dict__.update(vars_dict)
            else:
                self.set_variables(version_terrplant, run_type, application_rate, incorporation_depth, 
                    runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, 
                    ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, 
                    noaec_listed_seedling_emergence_dicot, chemical_name, pc_code, use , application_method, 
                    application_form, solubility)

    def set_default_variables(self):
        #Currently used variables
        self.incorporation_depth = 1
        self.application_rate = 1
        self.drift_fraction = 1
        self.runoff_fraction = 1
        self.ec25_nonlisted_seedling_emergence_monocot = 1
        self.noaec_listed_seedling_emergence_monocot = 1
        self.ec25_nonlisted_seedling_emergence_dicot = 1
        self.noaec_listed_seedling_emergence_dicot = 1
        self.run_type = "single"
        #Variables in the input page
        self.version_terrplant = ''
        self.chemical_name = ''
        self.pc_code = ''
        self.use = ''
        self.application_method = ''
        self.application_form = ''
        self.solubility = 1
        self.ec25_nonlisted_vegetative_vigor_monocot = 1
        self.noaec_listed_vegetative_vigor_monocot = 1
        self.ec25_nonlisted_vegetative_vigor_dicot = 1
        self.noaec_listed_vegetative_vigor_dicot = 1

    def set_variables(self, version_terrplant, run_type, application_rate, incorporation_depth, runoff_fraction, 
            drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot,
            noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot, chemical_name,
            pc_code, use, application_method, application_form, solubility):
        self.version_terrplant = version_terrplant
        self.run_type = run_type
        self.application_rate = application_rate
        self.incorporation_depth = incorporation_depth
        self.runoff_fraction = runoff_fraction
        self.drift_fraction = drift_fraction
        self.ec25_nonlisted_seedling_emergence_monocot = ec25_nonlisted_seedling_emergence_monocot
        self.ec25_nonlisted_seedling_emergence_dicot = ec25_nonlisted_seedling_emergence_dicot
        self.noaec_listed_seedling_emergence_monocot = noaec_listed_seedling_emergence_monocot
        self.noaec_listed_seedling_emergence_dicot = noaec_listed_seedling_emergence_dicot
        self.chemical_name = chemical_name
        self.pc_code = pc_code
        self.use = use
        self.application_method = application_method
        self.application_form = application_form
        self.solubility = solubility

        all_dic = {"version_terrplant":self.version_terrplant, "run_type":self.run_type, "application_rate":self.application_rate, 
                    "incorporation_depth":self.incorporation_depth, "runoff_fraction":self.runoff_fraction, "drift_fraction":self.drift_fraction,
                    "ec25_nonlisted_seedling_emergence_monocot":self.ec25_nonlisted_seedling_emergence_monocot, 
                    "ec25_nonlisted_seedling_emergence_dicot":self.ec25_nonlisted_seedling_emergence_dicot, 
                    "noaec_listed_seedling_emergence_monocot":self.noaec_listed_seedling_emergence_monocot, 
                    "noaec_listed_seedling_emergence_dicot":self.noaec_listed_seedling_emergence_dicot, "chemical_name":self.chemical_name,
                    "pc_code":self.pc_code, "use":self.use, "application_method":self.application_method, "application_form":self.application_form, 
                    "solubility":self.solubility}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/terrplant/' + self.jid
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        print response
        logging.info(response)
        output_val = json.loads(response.content)['result']
        for key, value in output_val.items():
            setattr(self, key, value)
