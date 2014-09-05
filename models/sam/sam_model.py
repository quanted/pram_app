"""
.. module:: sam_model
   :synopsis: A useful module indeed.
"""

from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('SIP Model')
import os
import requests
from collections import OrderedDict
import datetime

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


def get_jid():
    all_dic = {"dummy_key":"dummy_value"}
    data = json.dumps(all_dic)
    logger.info(data)
    jid = rest_funcs.gen_jid()
    url=url_part1 + '/sam/' + jid 

    response = requests.post(url=url, data=data, headers=http_headers, timeout=60)
    output_val = json.loads(response.content)['result']
    return(jid, output_val)

def convert_dict_key(key):
    try:
        return int(key.split('_')[2])
    except:
        return key

class SAM(object):
    def __init__(self, dictionary):

        alphanum_key = lambda (key, value): convert_dict_key(key)
        dictionary_1 = sorted(dictionary.items(), key=alphanum_key)
        dictionary = OrderedDict(dictionary_1)

        # Create class lists for inputs
        self.chemical_name = []
        self.simType = []

        # for k, v in dictionary.items():
        #     setattr(self, k, v)
        #     if k.startswith('chemical_name'):
        #         self.useYears.append(v)
        #     elif k.startswith('koc'):
        #         self.tempflag.append(v)
        #     elif k.startswith('soil_metabolism_hl'):
        #         self.tempflag.append(v)
        #     elif k.startswith('crop_number'):
        #         self.tempflag.append(v)
        #     elif k.startswith('noa'):
        #         self.tempflag.append(v)
        #     elif k.startswith('application_method'):
        #         self.tempflag.append(v)
        #     elif k.startswith('application_rate'):
        #         self.tempflag.append(v)
        #     elif k.startswith('refine'):
        #         self.tempflag.append(v)
        #     elif k.startswith('refine_time_window'):
        #         self.tempflag.append(v)
        #     elif k.startswith('refine_percent_applied'):
        #         self.tempflag.append(v)
        #     elif k.startswith('state'):
        #         self.tempflag.append(v)
        #     elif k.startswith('sim_type'):
        #         self.tempflag.append(v)
        #     elif k.startswith('sim_date_start'):
        #         self.tempflag.append(v)
        #     elif k.startswith('sim_date_end'):
        #         self.tempflag.append(v)
        #     elif k.startswith('sim_date_1stapp'):
        #         self.tempflag.append(v)
        #     elif k.startswith('output_type'):
        #         self.tempflag.append(v)
        #     elif k.startswith('output_tox'):
        #         self.tempflag.append(v)
        #     elif k.startswith('output_tox_value'):
        #         self.tempflag.append(v)
        #     elif k.startswith('output_format'):
        #         self.tempflag.append(v)

        self.final_res=get_jid()
        self.jid = self.final_res[0]