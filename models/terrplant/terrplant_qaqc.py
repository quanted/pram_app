"""
.. module:: terrplant_qaqc
   :synopsis: A useful module indeed.
"""

import terrplant_model
import os
import unittest
from StringIO import StringIO
import csv


path = os.path.join(os.environ['PROJECT_PATH'], 'models','terrplant','terrplant_qaqc_inputs.csv')
data = csv.reader(open(path))
version_terrplant = '1.2.2'
application_rate=[]
incorporation_depth=[]
runoff_fraction=[]
drift_fraction=[]
EC25_for_nonlisted_seedling_emergence_monocot=[]
EC25_for_nonlisted_seedling_emergence_dicot=[]
NOAEC_for_listed_seedling_emergence_monocot=[]
NOAEC_for_listed_seedling_emergence_dicot=[]
chemical_name = []
pc_code = []
use = []
application_method = []
application_form = []
solubility = []

EC25_for_nonlisted_seedling_emergence_monocot = []
NOAEC_for_listed_seedling_emergence_monocot = []
EC25_for_nonlisted_seedling_emergence_dicot = []
NOAEC_for_listed_seedling_emergence_dicot = []
EC25_for_nonlisted_vegetative_vigor_monocot = []
NOAEC_for_listed_vegetative_vigor_monocot = []
EC25_for_nonlisted_vegetative_vigor_dicot = []
NOAEC_for_listed_vegetative_vigor_dicot = []
nmsRQdry_results = []
lmsRQdry_results = []
ndsRQdry_results = []
ldsRQdry_results = []
nmsRQsemi_results = []
lmsRQsemi_results = []
ndsRQsemi_results = []
ldsRQsemi_results = []
nmsRQspray_results = []
lmsRQspray_results = []
ndsRQspray_results = []
ldsRQspray_results = []


data.next()
for row in data:
    chemical_name.append(str(row[0]))
    pc_code.append(str(row[1]))
    use.append(str(row[2]))
    application_method.append(str(row[3]))
    application_form.append(str(row[4]))
    solubility.append(float(row[5]))
    incorporation_depth.append(float(row[6]))
    application_rate.append(float(row[7]))
    drift_fraction.append(float(row[8]))
    runoff_fraction.append(float(row[9]))
    EC25_for_nonlisted_seedling_emergence_monocot.append(float(row[10]))
    NOAEC_for_listed_seedling_emergence_monocot.append(float(row[11]))
    EC25_for_nonlisted_seedling_emergence_dicot.append(float(row[12]))
    NOAEC_for_listed_seedling_emergence_dicot.append(float(row[13]))
    EC25_for_nonlisted_vegetative_vigor_monocot.append(float(row[14]))
    NOAEC_for_listed_vegetative_vigor_monocot.append(float(row[15]))
    EC25_for_nonlisted_vegetative_vigor_dicot.append(float(row[16]))
    NOAEC_for_listed_vegetative_vigor_dicot.append(float(row[17]))
    nmsRQdry_results.append(float(row[18]))
    lmsRQdry_results.append(float(row[19]))
    ndsRQdry_results.append(float(row[20]))
    ldsRQdry_results.append(float(row[21]))
    nmsRQsemi_results.append(float(row[22]))
    lmsRQsemi_results.append(float(row[23]))
    ndsRQsemi_results.append(float(row[24]))
    ldsRQsemi_results.append(float(row[25]))
    nmsRQspray_results.append(float(row[26]))
    lmsRQspray_results.append(float(row[27]))
    ndsRQspray_results.append(float(row[28]))
    ldsRQspray_results.append(float(row[29]))

terrplant_obj = terrplant_model.terrplant(True,True,version_terrplant,"qaqc",application_rate[0],EC25_for_nonlisted_seedling_emergence_monocot[0],runoff_fraction[0],drift_fraction[0],EC25_for_nonlisted_seedling_emergence_monocot[0],EC25_for_nonlisted_seedling_emergence_dicot[0],NOAEC_for_listed_seedling_emergence_monocot[0],NOAEC_for_listed_seedling_emergence_dicot[0],chemical_name[0],pc_code[0],use[0],application_method[0],application_form[0],solubility[0])
terrplant_obj.chemical_name_expected = chemical_name[0]
terrplant_obj.pc_code_expected = pc_code[0]
terrplant_obj.use_expected = use[0]
terrplant_obj.application_method_expected = application_method[0]
terrplant_obj.application_form_expected = application_form[0]
terrplant_obj.solubility_expected = solubility[0]

terrplant_obj.EC25_for_nonlisted_seedling_emergence_monocot_expected = EC25_for_nonlisted_seedling_emergence_monocot[0]
terrplant_obj.NOAEC_for_listed_seedling_emergence_monocot_expected = NOAEC_for_listed_seedling_emergence_monocot[0]
terrplant_obj.EC25_for_nonlisted_seedling_emergence_dicot_expected = EC25_for_nonlisted_seedling_emergence_dicot[0]
terrplant_obj.NOAEC_for_listed_seedling_emergence_dicot_expected = NOAEC_for_listed_seedling_emergence_dicot[0]
terrplant_obj.EC25_for_nonlisted_vegetative_vigor_monocot_expected = EC25_for_nonlisted_vegetative_vigor_monocot[0]
terrplant_obj.NOAEC_for_listed_vegetative_vigor_monocot_expected = NOAEC_for_listed_vegetative_vigor_monocot[0]
terrplant_obj.EC25_for_nonlisted_vegetative_vigor_dicot_expected = EC25_for_nonlisted_vegetative_vigor_dicot[0]
terrplant_obj.NOAEC_for_listed_vegetative_vigor_dicot_expected = NOAEC_for_listed_vegetative_vigor_dicot[0]
terrplant_obj.nmsRQdry_results_expected = nmsRQdry_results[0]
terrplant_obj.lmsRQdry_results_expected = lmsRQdry_results[0]
terrplant_obj.ndsRQdry_results_expected = ndsRQdry_results[0]
terrplant_obj.ldsRQdry_results_expected = ldsRQdry_results[0]
terrplant_obj.nmsRQsemi_results_expected = nmsRQsemi_results[0]
terrplant_obj.lmsRQsemi_results_expected = lmsRQsemi_results[0]
terrplant_obj.ndsRQsemi_results_expected = ndsRQsemi_results[0]
terrplant_obj.ldsRQsemi_results_expected = ldsRQsemi_results[0]
terrplant_obj.nmsRQspray_results_expected = nmsRQspray_results[0]
terrplant_obj.lmsRQspray_results_expected = lmsRQspray_results[0]
terrplant_obj.ndsRQspray_results_expected = ndsRQspray_results[0]
terrplant_obj.ldsRQspray_results_expected = ldsRQspray_results[0]