"""
.. module:: iec_model
   :synopsis: A useful module indeed.
"""

import json
import os
import requests

from pram_app.REST import rest_funcs

# Set HTTP header
http_headers = rest_funcs.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']

class iec(object):
    def __init__(self, set_variables=True,run_methods=True,run_type='single',dose_response=1,lc50=1,threshold=1,vars_dict=None):
        self.set_default_variables()
        self.jid = rest_funcs.gen_jid()
        if set_variables:
            if vars_dict is not None:
                self.__dict__.update(vars_dict)
            else:
                self.set_variables(run_type,dose_response,lc50,threshold)

    def __str__(self):
        string_rep = ''
        string_rep = string_rep + "dose_response = {0:.2e}".format(self.dose_response)
        string_rep = string_rep + "lc50 = {0:.2e}".format(self.lc50)
        string_rep = string_rep + "threshold = {0:.2e}".format(self.threshold)
        return string_rep


    def set_default_variables(self):
        self.run_type = "single"
        self.dose_response = 1
        self.lc50 = 1
        self.threshold = 1
        #
        #"_out" need to be added to ea. fun. as expection catching
        #

    def set_variables(self, run_type, dose_response, lc50, threshold):
        self.run_type = run_type
        self.dose_response = dose_response
        self.lc50 = lc50
        self.threshold = threshold

        all_dic = {"dose_response":self.dose_response, "lc50":self.lc50, "threshold":self.threshold}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/iec/' + self.jid 
        response = requests.post(url=url, data=data, headers=http_headers, timeout=60)
        output_val = json.loads(response.content)['result']
        for key, value in output_val.items():
            setattr(self, key, value)

    def set_unit_testing_variables(self):
        z_score_f_out_expected = None
        F8_f_out_expected = None
        chance_f_out_expected = None


