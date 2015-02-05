"""
.. module:: sip_model
   :synopsis: A useful module indeed.
"""

# Screening Imbibiton Program v1.0 (SIP)
from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('SIP Model')
import os
import requests

# Daily water intake rate for birds

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


class sip(object):
    def __init__(self, set_variables=True,run_methods=True,run_type = "single",chemical_name='', species_tested_bird='', species_tested_mammal='', bodyweight_quail=1, bodyweight_duck=1, bodyweight_bird_other=1, bodyweight_rat=1, bodyweight_tested_mammal_other=1, solubility=1, ld50_avian_water=1, ld50_mammal_water=1, bodyweight_assessed_bird=1, mineau_scaling_factor=1, bodyweight_assessed_mammal=1, noaec_duck=1, noaec_quail=1, noaec_other=1, Species_of_the_bird_NOAEC_CHOICES=1, noael_mammal_water=1,vars_dict=None):
        self.set_default_variables()
        self.jid = rest_funcs.gen_jid()
        if set_variables:
            if vars_dict != None:
                self.__dict__.update(vars_dict)
            else:
                self.set_variables(run_type, chemical_name, species_tested_bird, species_tested_mammal, bodyweight_quail, bodyweight_duck, bodyweight_bird_other, bodyweight_rat, bodyweight_tested_mammal_other, solubility, ld50_avian_water, ld50_mammal_water, bodyweight_assessed_bird, mineau_scaling_factor, bodyweight_assessed_mammal, noaec_duck, noaec_quail, noaec_other, Species_of_the_bird_NOAEC_CHOICES, noael_mammal_water)

    def set_default_variables(self):
        self.run_type = "single"
        self.chemical_name = ''
       # self.select_receptor()
        self.bodyweight_tested_bird = -1
        self.bodyweight_quail = -1
        self.bodyweight_duck = -1
        self.bodyweight_bird_other = -1
        self.bodyweight_rat = -1
        self.bodyweight_tested_mammal_other = -1
        self.species_tested_bird = None
        self.species_tested_mammal = None
        self.bodyweight_tested_mammal = -1
        self.solubility = -1
        self.ld50_avian_water = -1
        self.ld50_mammal_water = -1
        self.bodyweight_assessed_bird = -1
        self.mineau_scaling_factor = -1
        self.bodyweight_assessed_mammal = -1
        self.noael_avian_water = -1
        self.noael_mammal_water = -1

    def set_variables(self, run_type, chemical_name, species_tested_bird, species_tested_mammal, 
                bodyweight_quail, bodyweight_duck, bodyweight_bird_other, bodyweight_rat, bodyweight_tested_mammal_other, 
                solubility, ld50_avian_water, ld50_mammal_water, bodyweight_assessed_bird, mineau_scaling_factor, bodyweight_assessed_mammal, 
                noaec_duck, noaec_quail, noaec_other, Species_of_the_bird_NOAEC_CHOICES, noael_mammal_water):
        self.run_type = run_type
        self.chemical_name = chemical_name
        self.bodyweight_quail = bodyweight_quail
        self.bodyweight_duck = bodyweight_duck
        self.bodyweight_bird_other = bodyweight_bird_other
        self.bodyweight_rat = bodyweight_rat
        self.bodyweight_tested_mammal_other = bodyweight_tested_mammal_other
        self.species_tested_bird = species_tested_bird
        self.species_tested_mammal = species_tested_mammal
        if species_tested_bird =='178':
            self.bodyweight_tested_bird = self.bodyweight_quail
        elif species_tested_bird =='1580':
            self.bodyweight_tested_bird = self.bodyweight_duck
        else:
            self.bodyweight_tested_bird = self.bodyweight_bird_other
        if species_tested_mammal =='350':
            self.bodyweight_tested_mammal = self.bodyweight_rat
        else:
            self.bodyweight_tested_mammal = self.bodyweight_tested_mammal_other
        self.solubility = solubility
        self.ld50_avian_water = ld50_avian_water
        self.ld50_mammal_water = ld50_mammal_water
        self.bodyweight_assessed_bird = bodyweight_assessed_bird
        self.mineau_scaling_factor = mineau_scaling_factor
        self.bodyweight_assessed_mammal = bodyweight_assessed_mammal
        self.noaec_duck = noaec_duck
        self.noaec_quail = noaec_quail
        self.noaec_other = noaec_other
        if Species_of_the_bird_NOAEC_CHOICES == '1':
            self.noael_avian_water = self.noaec_quail
        elif Species_of_the_bird_NOAEC_CHOICES == '2':
            self.noael_avian_water = self.noaec_duck
        elif Species_of_the_bird_NOAEC_CHOICES == '3':
            self.noael_avian_water = self.noaec_other
        # else:
        #     try:
        #         self.noael_avian_water = noael_avian_water
        #     except ValueError:
        #         raise ValueError\
        #         ('self.noael_avian_water=%g is a non-physical value.' % self.bodyweight_assessed_bird)
        self.noael_mammal_water = noael_mammal_water

        all_dic = {"chemical_name":self.chemical_name, "bodyweight_tested_bird":self.bodyweight_tested_bird, "bodyweight_quail":self.bodyweight_quail, "bodyweight_duck":self.bodyweight_duck, "bodyweight_bird_other":self.bodyweight_bird_other, "bodyweight_rat":self.bodyweight_rat,
                   "bodyweight_tested_mammal_other":self.bodyweight_tested_mammal_other, "species_tested_bird":self.species_tested_bird, "species_tested_mammal":self.species_tested_mammal, "bodyweight_tested_mammal":self.bodyweight_tested_mammal, "solubility":self.solubility,
                   "ld50_avian_water":self.ld50_avian_water, "ld50_mammal_water":self.ld50_mammal_water, "bodyweight_assessed_bird":self.bodyweight_assessed_bird, "mineau_scaling_factor":self.mineau_scaling_factor, "bodyweight_assessed_mammal":self.bodyweight_assessed_mammal, "noael_avian_water":self.noael_avian_water, "noael_mammal_water":self.noael_mammal_water}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/sip/' + self.jid 
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)
        response = requests.post(url, data=data, headers=http_headers, timeout=60)  
        output_val = json.loads(response.content)['result']

        for key, value in output_val.items():
            setattr(self, key, value)

    def set_unit_testing_variables(self):
        self.fw_bird_out_expected = None
        self.fw_mamm_out_expected = None
        self.dose_bird_out_expected = None
        self.dose_mamm_out_expected = None
        self.at_bird_out_expected = None
        self.at_mamm_out_expected = None
        self.fi_bird_out_expected = None
        self.det_out_expected = None
        self.act_out_expected = None
        self.acute_bird_out_expected = None
        self.acuconb_out_expected = None
        self.acute_mamm_out_expected = None
        self.acuconm_out_expected = None
        self.chron_bird_out_expected = None
        self.chronconb_out_expected = None
        self.chron_mamm_out_expected = None
        self.chronconm_out_expected = None


