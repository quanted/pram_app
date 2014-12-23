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
ec25_nonlisted_seedling_emergence_monocot=[]
ec25_nonlisted_seedling_emergence_dicot=[]
noaec_listed_seedling_emergence_monocot=[]
noaec_listed_seedling_emergence_dicot=[]
chemical_name = []
pc_code = []
use = []
application_method = []
application_form = []
solubility = []

ec25_nonlisted_seedling_emergence_monocot = []
noaec_listed_seedling_emergence_monocot = []
ec25_nonlisted_seedling_emergence_dicot = []
noaec_listed_seedling_emergence_dicot = []
ec25_nonlisted_vegetative_vigor_monocot = []
noaec_listed_vegetative_vigor_monocot = []
ec25_nonlisted_vegetative_vigor_dicot = []
noaec_listed_vegetative_vigor_dicot = []
nms_rq_dry_results = []
lms_rq_dry_results = []
nds_rq_dry_results = []
lds_rq_dry_results = []
nms_rq_semi_results = []
lms_rq_semi_results = []
nds_rq_semi_results = []
lds_rq_semi_results = []
nms_rq_spray_results = []
lms_rq_spray_results = []
nds_rq_spray_results = []
lds_rq_spray_results = []


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
    ec25_nonlisted_seedling_emergence_monocot.append(float(row[10]))
    noaec_listed_seedling_emergence_monocot.append(float(row[11]))
    ec25_nonlisted_seedling_emergence_dicot.append(float(row[12]))
    noaec_listed_seedling_emergence_dicot.append(float(row[13]))
    ec25_nonlisted_vegetative_vigor_monocot.append(float(row[14]))
    noaec_listed_vegetative_vigor_monocot.append(float(row[15]))
    ec25_nonlisted_vegetative_vigor_dicot.append(float(row[16]))
    noaec_listed_vegetative_vigor_dicot.append(float(row[17]))
    nms_rq_dry_results.append(float(row[18]))
    lms_rq_dry_results.append(float(row[19]))
    nds_rq_dry_results.append(float(row[20]))
    lds_rq_dry_results.append(float(row[21]))
    nms_rq_semi_results.append(float(row[22]))
    lms_rq_semi_results.append(float(row[23]))
    nds_rq_semi_results.append(float(row[24]))
    lds_rq_semi_results.append(float(row[25]))
    nms_rq_spray_results.append(float(row[26]))
    lms_rq_spray_results.append(float(row[27]))
    nds_rq_spray_results.append(float(row[28]))
    lds_rq_spray_results.append(float(row[29]))

terrplant_obj = terrplant_model.terrplant(True,True,version_terrplant,"qaqc",application_rate[0],ec25_nonlisted_seedling_emergence_monocot[0],runoff_fraction[0],drift_fraction[0],ec25_nonlisted_seedling_emergence_monocot[0],ec25_nonlisted_seedling_emergence_dicot[0],noaec_listed_seedling_emergence_monocot[0],noaec_listed_seedling_emergence_dicot[0],chemical_name[0],pc_code[0],use[0],application_method[0],application_form[0],solubility[0])
terrplant_obj.chemical_name_expected = chemical_name[0]
terrplant_obj.pc_code_expected = pc_code[0]
terrplant_obj.use_expected = use[0]
terrplant_obj.application_method_expected = application_method[0]
terrplant_obj.application_form_expected = application_form[0]
terrplant_obj.solubility_expected = solubility[0]

terrplant_obj.ec25_nonlisted_seedling_emergence_monocot_expected = ec25_nonlisted_seedling_emergence_monocot[0]
terrplant_obj.noaec_listed_seedling_emergence_monocot_expected = noaec_listed_seedling_emergence_monocot[0]
terrplant_obj.ec25_nonlisted_seedling_emergence_dicot_expected = ec25_nonlisted_seedling_emergence_dicot[0]
terrplant_obj.noaec_listed_seedling_emergence_dicot_expected = noaec_listed_seedling_emergence_dicot[0]
terrplant_obj.ec25_nonlisted_vegetative_vigor_monocot_expected = ec25_nonlisted_vegetative_vigor_monocot[0]
terrplant_obj.noaec_listed_vegetative_vigor_monocot_expected = noaec_listed_vegetative_vigor_monocot[0]
terrplant_obj.ec25_nonlisted_vegetative_vigor_dicot_expected = ec25_nonlisted_vegetative_vigor_dicot[0]
terrplant_obj.noaec_listed_vegetative_vigor_dicot_expected = noaec_listed_vegetative_vigor_dicot[0]
terrplant_obj.nms_rq_dry_results_expected = nms_rq_dry_results[0]
terrplant_obj.lms_rq_dry_results_expected = lms_rq_dry_results[0]
terrplant_obj.nds_rq_dry_results_expected = nds_rq_dry_results[0]
terrplant_obj.lds_rq_dry_results_expected = lds_rq_dry_results[0]
terrplant_obj.nms_rq_semi_results_expected = nms_rq_semi_results[0]
terrplant_obj.lms_rq_semi_results_expected = lms_rq_semi_results[0]
terrplant_obj.nds_rq_semi_results_expected = nds_rq_semi_results[0]
terrplant_obj.lds_rq_semi_results_expected = lds_rq_semi_results[0]
terrplant_obj.nms_rq_spray_results_expected = nms_rq_spray_results[0]
terrplant_obj.lms_rq_spray_results_expected = lms_rq_spray_results[0]
terrplant_obj.nds_rq_spray_results_expected = nds_rq_spray_results[0]
terrplant_obj.lds_rq_spray_results_expected = lds_rq_spray_results[0]