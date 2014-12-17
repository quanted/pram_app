"""
.. module:: terrplant_batch_runner
   :synopsis: A useful module indeed.
"""

import numpy as np
import logging
import sys
sys.path.append("utils")
import json_utils
sys.path.append("./terrplant")
import terrplant_model

class TerrPlantBatchRunner():
    
    def runTerrPlantModel(self,config_properties,results_dict):
        if not results_dict:
            results_dict = {}
        #this is where properties are searched, converted as needed, and any available methods are called
        application_rate = None
        if 'application_lbs_rate' in config_properties:
            application_rate = config_properties['application_lbs_rate']
        incorporation_depth = None
        if 'incorporation_depth' in config_properties:
            incorporation_depth = config_properties['incorporation_depth']
        runoff_fraction = None
        if 'runoff' in config_properties:
            runoff_fraction = config_properties['runoff']
        drift_fraction = None
        if 'spray_drift' in config_properties:
            drift_fraction = config_properties['spray_drift']
        EC25_for_nonlisted_seedling_emergence_monocot = None
        if 'EC25_for_nonlisted_seedling_emergence_monocot' in config_properties:
            EC25_for_nonlisted_seedling_emergence_monocot = config_properties['EC25_for_nonlisted_seedling_emergence_monocot']
        EC25_for_nonlisted_seedling_emergence_dicot = None
        if 'NOAEC_for_listed_seedling_emergence_monocot' in config_properties:
            EC25_for_nonlisted_seedling_emergence_dicot = config_properties['NOAEC_for_listed_seedling_emergence_monocot']
        NOAEC_for_listed_seedling_emergence_monocot = None
        if 'EC25_for_nonlisted_seedling_emergence_dicot' in config_properties:
            NOAEC_for_listed_seedling_emergence_monocot = config_properties['EC25_for_nonlisted_seedling_emergence_dicot']
        NOAEC_for_listed_seedling_emergence_dicot = None
        if 'NOAEC_for_listed_vegetative_vigor_dicot' in config_properties:
            NOAEC_for_listed_seedling_emergence_dicot = config_properties['NOAEC_for_listed_vegetative_vigor_dicot']
        terr = terrplant_model.terrplant(True,True,application_rate,incorporation_depth,runoff_fraction,drift_fraction,EC25_for_nonlisted_seedling_emergence_monocot,EC25_for_nonlisted_seedling_emergence_dicot,NOAEC_for_listed_seedling_emergence_monocot,NOAEC_for_listed_seedling_emergence_dicot)
        results_dict['terrplant'] = vars(terr)
        return results_dict
