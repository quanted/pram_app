"""
.. module:: sam_model
   :synopsis: A useful module indeed.
"""

from REST import auth_s3, rest_funcs
import json
import logging
logger = logging.getLogger('SAM Model')
import os
import requests
from collections import OrderedDict
import datetime

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


# def get_jid(run_type, chemical_name, koc, soil_metabolism_hl, crop, crop_number, noa, app_method, application_rate, refine, refine_time_window, refine_percent_applied, region, sim_type, sim_date_start, sim_date_end, sim_date_1stapp, output_type, output_tox, output_tox_value, output_format):
def get_jid(run_type):
    """
    Generate job ID and send inputs to JSON-RPC model server
    """
    all_dic = {
        # "run_type" : run_type,
        # "chemical_name" : chemical_name,
        # "koc" : koc,
        # "soil_metabolism_hl" : soil_metabolism_hl,
        # "crop" : crop,
        # "crop_number" : crop_number,
        # "noa" : noa,
        # "app_method" : app_method,
        # "application_rate" : application_rate,
        # "refine" : refine,
        # "refine_time_window" : refine_time_window,
        # "refine_percent_applied" : refine_percent_applied,
        # "region" : region,
        # "sim_type" : sim_type,
        # "sim_date_start" : sim_date_start,
        # "sim_date_end" : sim_date_end,
        # "sim_date_1stapp" : sim_date_1stapp,
        # "output_type" : output_type,
        # "output_tox" : output_tox,
        # "output_tox_value" : output_tox_value,
        # "output_format" : output_format,
    }
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
    # def __init__(self, run_type, chemical_name, koc, soil_metabolism_hl, crop, crop_number, noa, app_method, application_rate, refine, refine_time_window, refine_percent_applied, region, sim_type, sim_date_start, sim_date_end, sim_date_1stapp, output_type, output_tox, output_tox_value, output_format):

    #     # Create class lists for input variables
    #     self.run_type = run_type
    #     self.chemical_name = chemical_name
    #     self.koc = koc
    #     self.soil_metabolism_hl = soil_metabolism_hl
    #     self.crop = crop
    #     self.crop_number = crop_number
    #     self.noa = noa
    #     self.app_method = app_method
    #     self.application_rate = application_rate
    #     self.refine = refine
    #     self.refine_time_window = refine_time_window
    #     self.refine_percent_applied = refine_percent_applied
    #     self.region = region
    #     self.sim_type = sim_type
    #     self.sim_date_start = sim_date_start
    #     self.sim_date_end = sim_date_end
    #     self.sim_date_1stapp = sim_date_1stapp
    #     self.output_type = output_type
    #     self.output_tox = output_tox
    #     self.output_tox_value = output_tox_value
    #     self.output_format = output_format

    def __init__(self, run_type, scenario_selection):
        self.run_type = run_type
        self.scenario_selection = scenario_selection

        # self.final_res = get_jid(self.run_type, self.chemical_name, self.koc, self.soil_metabolism_hl, self.crop, self.crop_number, self.noa, self.app_method, self.application_rate, self.refine, self.refine_time_window, self.refine_percent_applied, self.region, self.sim_type, self.sim_date_start, self.sim_date_end, self.sim_date_1stapp, self.output_type, self.output_tox, self.output_tox_value, self.output_format)
        self.final_res = get_jid(self.run_type)

        self.jid = self.final_res[0]
        self.link = self.final_res[1][0]