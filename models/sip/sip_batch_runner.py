"""
.. module:: sip_batch_runner
   :synopsis: A useful module indeed.
"""

import numpy as np
import logging
import sys
sys.path.append("utils")
import json_utils
sys.path.append("./sip")
import sip_model

logger = logging.getLogger("SIPBatchRunner")

class SIPBatchRunner():
    
    def runSIPModel(self,config_properties,results_dict):
        if not results_dict:
            results_dict = {}
        #this is where properties are searched, converted as needed, and any available methods are called
        logger.info(config_properties)
        chemical_name = None
        if 'chemical_name' in config_properties:
            chemical_name = config_properties['chemical_name']
        solubility = None
        if 'solubility' in config_properties:
            solubility = config_properties['solubility']
        ld50_avian_water = None
        if 'ld50_avian_water' in config_properties:
            ld50_avian_water = config_properties['ld50_avian_water']
        noael_avian_water = None
        if 'avian_NOAEC' in config_properties:
            noael_avian_water = config_properties['avian_NOAEC']
        bodyweight_assessed_bird = None
        if 'bodyweight_tested_bird' in config_properties:
            bodyweight_assessed_bird = config_properties['bodyweight_tested_bird']
        bodyweight_quail = None
        if 'bodyweight_quail' in config_properties:
            bodyweight_quail = config_properties['bodyweight_quail']
        bodyweight_duck = None
        if 'bodyweight_duck' in config_properties:
            bodyweight_duck = config_properties['bodyweight_duck']
        bodyweight_bird_other = None
        if 'bodyweight_bird_other' in config_properties:
            bodyweight_bird_other = config_properties['bodyweight_bird_other']
        mineau_scaling_factor = None
        if 'mineau_scaling_factor' in config_properties:
            mineau_scaling_factor = config_properties['mineau_scaling_factor']
        ld50_mammal_water = None
        if 'ld50_mammal_water' in config_properties:
            ld50_mammal_water = config_properties['ld50_mammal_water']
        noael_mammal_water = None
        if 'noael_mammal_water' in config_properties:
            noael_mammal_water = config_properties['noael_mammal_water']
        bodyweight_assessed_mammal = None
        if 'bodyweight_assessed_mammal' in config_properties:
            bodyweight_assessed_mammal = config_properties['bodyweight_assessed_mammal']
        bodyweight_rat = None
        if 'bodyweight_rat' in config_properties:
            bodyweight_rat = config_properties['bodyweight_rat']
        bodyweight_tested_mammal_other = None
        if 'bodyweight_tested_mammal_other' in config_properties:
            bodyweight_rat = config_properties['bodyweight_tested_mammal_other']
        species_tested_mammal = None
        if 'species_tested_mammal' in config_properties:
            species_tested_mammal = config_properties['species_tested_mammal']
        species_tested_bird = None
        if 'species_tested_bird' in config_properties:
            species_tested_bird = config_properties['id_Species_of_the_tested_bird']
        noaec_duck = None
        if 'noaec_duck' in config_properties:
            noaec_duck = config_properties['noaec_duck']
        noaec_quail = None
        if 'noaec_quail' in config_properties:
            noaec_quail = config_properties['noaec_quail']
        noaec_other = None
        if 'noaec_other' in config_properties:
            noaec_other = config_properties['noaec_other']
        sip_obj = sip_model.sip(True,True,True,chemical_name, species_tested_bird, species_tested_mammal, bodyweight_quail, bodyweight_duck, bodyweight_bird_other, bodyweight_rat, bodyweight_tested_mammal_other, solubility, ld50_avian_water, ld50_mammal_water, bodyweight_assessed_bird, mineau_scaling_factor, bodyweight_assessed_mammal, noaec_duck, noaec_quail, noaec_other, Species_of_the_bird_NOAEC_CHOICES, noael_mammal_water)
        results_dict['sip'] = vars(sip_obj)
        return results_dict
