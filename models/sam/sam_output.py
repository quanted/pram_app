"""
.. module:: sam_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def samOutputPage(request):
    import sam_model
    
    # chemical_name = request.POST.get('chemical_name')
    # koc = request.POST.get('koc')
    # soil_metabolism_hl = request.POST.get('soil_metabolism_hl')
    # crop = request.POST.get('crop')
    # crop_number = request.POST.get('crop_number')
    # noa = request.POST.get('noa')
    # app_method = request.POST.get('application_method')
    # application_rate = request.POST.get('application_rate')
    # refine = request.POST.get('refine')
    # refine_time_window = request.POST.get('refine_time_window')
    # refine_percent_applied = request.POST.get('refine_percent_applied')
    # region = request.POST.get('region')
    # sim_type = request.POST.get('sim_type')
    # sim_date_start = request.POST.get('sim_date_start')
    # sim_date_end = request.POST.get('sim_date_end')
    # sim_date_1stapp = request.POST.get('sim_date_1stapp')
    # output_type = request.POST.get('output_type')
    # output_tox = request.POST.get('output_tox')
    # output_tox_value = request.POST.get('output_tox_value')
    # output_format = request.POST.get('output_format')
    scenario_selection = request.POST.get('scenario_selection')

    # sam_obj = sam_model.SAM("single", chemical_name, koc, soil_metabolism_hl, crop, crop_number, noa, app_method, application_rate, refine, refine_time_window, refine_percent_applied, region, sim_type, sim_date_start, sim_date_end, sim_date_1stapp, output_type, output_tox, output_tox_value, output_format)
    sam_obj = sam_model.SAM("single", scenario_selection)

    return sam_obj