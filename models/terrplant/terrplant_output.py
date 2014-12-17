"""
.. module:: terrplant_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def terrplantOutputPage(request):
    import terrplant_model

    version_terrplant = request.POST.get('version_terrplant')
    incorporation_depth = request.POST.get('incorporation')
    application_rate = request.POST.get('application_rate')
    drift_fraction = request.POST.get('drift_fraction')
    runoff_fraction = request.POST.get('runoff_fraction')
    EC25_for_nonlisted_seedling_emergence_monocot = request.POST.get('EC25_for_nonlisted_seedling_emergence_monocot')
    NOAEC_for_listed_seedling_emergence_monocot = request.POST.get('EC25_for_nonlisted_seedling_emergence_dicot')
    EC25_for_nonlisted_seedling_emergence_dicot = request.POST.get('NOAEC_for_listed_seedling_emergence_monocot')
    NOAEC_for_listed_seedling_emergence_dicot = request.POST.get('NOAEC_for_listed_seedling_emergence_dicot')
    #fill out terrplant object with yet to be used data
    chemical_name = request.POST.get('chemical_name')
    # terr.chemical_name = chemical_name
    pc_code = request.POST.get('pc_code')
    # terr.pc_code = pc_code
    use = request.POST.get('use')
    # terr.use = use
    application_method = request.POST.get('application_method')
    # terr.application_method = application_method
    application_form = request.POST.get('application_form')
    # terr.application_form = application_form
    solubility = request.POST.get('solubility')
    # terr.solubility = solubility
    terr = terrplant_model.terrplant(True,True,version_terrplant,"single",application_rate,incorporation_depth,runoff_fraction,drift_fraction,EC25_for_nonlisted_seedling_emergence_monocot,EC25_for_nonlisted_seedling_emergence_dicot,NOAEC_for_listed_seedling_emergence_monocot,NOAEC_for_listed_seedling_emergence_dicot,chemical_name,pc_code,use,application_method,application_form,solubility)

    EC25_for_nonlisted_vegetative_vigor_monocot = request.POST.get('EC25_for_nonlisted_vegetative_vigor_monocot')
    terr.EC25_for_nonlisted_vegetative_vigor_monocot = EC25_for_nonlisted_vegetative_vigor_monocot
    NOAEC_for_listed_vegetative_vigor_monocot = request.POST.get('EC25_for_nonlisted_vegetative_vigor_dicot')
    terr.NOAEC_for_listed_vegetative_vigor_monocot = NOAEC_for_listed_vegetative_vigor_monocot
    EC25_for_nonlisted_vegetative_vigor_dicot = request.POST.get('NOAEC_for_listed_vegetative_vigor_monocot')
    terr.EC25_for_nonlisted_vegetative_vigor_dicot = EC25_for_nonlisted_vegetative_vigor_dicot
    NOAEC_for_listed_vegetative_vigor_dicot = request.POST.get('NOAEC_for_listed_vegetative_vigor_dicot')
    terr.NOAEC_for_listed_vegetative_vigor_dicot = NOAEC_for_listed_vegetative_vigor_dicot

    return terr