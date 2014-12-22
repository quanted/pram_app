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
    incorporation_depth = request.POST.get('incorporation_depth')
    application_rate = request.POST.get('application_rate')
    drift_fraction = request.POST.get('drift_fraction')
    runoff_fraction = request.POST.get('runoff_fraction')
    ec25_nonlisted_seedling_emergence_monocot = request.POST.get('ec25_nonlisted_seedling_emergence_monocot')
    noaec_listed_seedling_emergence_monocot = request.POST.get('ec25_nonlisted_seedling_emergence_dicot')
    ec25_nonlisted_seedling_emergence_dicot = request.POST.get('noaec_listed_seedling_emergence_monocot')
    noaec_listed_seedling_emergence_dicot = request.POST.get('noaec_listed_seedling_emergence_dicot')
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
    terr = terrplant_model.terrplant(True,True,version_terrplant,"single",application_rate,incorporation_depth,
        runoff_fraction,drift_fraction,ec25_nonlisted_seedling_emergence_monocot,ec25_nonlisted_seedling_emergence_dicot,
        noaec_listed_seedling_emergence_monocot,noaec_listed_seedling_emergence_dicot,chemical_name,pc_code,use,
        application_method,application_form,solubility)

    ec25_nonlisted_vegetative_vigor_monocot = request.POST.get('ec25_nonlisted_vegetative_vigor_monocot')
    terr.ec25_nonlisted_vegetative_vigor_monocot = ec25_nonlisted_vegetative_vigor_monocot
    noaec_listed_vegetative_vigor_monocot = request.POST.get('ec25_nonlisted_vegetative_vigor_dicot')
    terr.noaec_listed_vegetative_vigor_monocot = noaec_listed_vegetative_vigor_monocot
    ec25_nonlisted_vegetative_vigor_dicot = request.POST.get('noaec_listed_vegetative_vigor_monocot')
    terr.ec25_nonlisted_vegetative_vigor_dicot = ec25_nonlisted_vegetative_vigor_dicot
    noaec_listed_vegetative_vigor_dicot = request.POST.get('noaec_listed_vegetative_vigor_dicot')
    terr.noaec_listed_vegetative_vigor_dicot = noaec_listed_vegetative_vigor_dicot

    return terr