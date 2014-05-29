from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def stirOutputPage(request):
    import stir_model

    chemical_name = request.POST.get('chemical_name')
    application_rate = request.POST.get('application_rate')
    column_height = request.POST.get('column_height')
    spray_drift_fraction = request.POST.get('spray_drift_fraction')
    direct_spray_duration = request.POST.get('direct_spray_duration')
    molecular_weight = request.POST.get('molecular_weight')
    vapor_pressure = request.POST.get('vapor_pressure')
    avian_oral_ld50 = request.POST.get('avian_oral_ld50')
    body_weight_assessed_bird = request.POST.get('body_weight_assessed_bird')
    body_weight_tested_bird = request.POST.get('body_weight_tested_bird')
    mineau_scaling_factor = request.POST.get('mineau_scaling_factor')
    mammal_inhalation_lc50 = request.POST.get('mammal_inhalation_lc50')
    duration_mammal_inhalation_study = request.POST.get('duration_mammal_inhalation_study')
    body_weight_assessed_mammal = request.POST.get('body_weight_assessed_mammal')
    body_weight_tested_mammal = request.POST.get('body_weight_tested_mammal')
    mammal_oral_ld50 = request.POST.get('mammal_oral_ld50')

    sm = stir_model.StirModel(True,True,'single',chemical_name,application_rate,column_height,spray_drift_fraction,direct_spray_duration, 
            molecular_weight,vapor_pressure,avian_oral_ld50, body_weight_assessed_bird, body_weight_tested_bird, mineau_scaling_factor, 
            mammal_inhalation_lc50,duration_mammal_inhalation_study,body_weight_assessed_mammal, body_weight_tested_mammal, 
            mammal_oral_ld50)
    import logging
    logging.info(sm)
    return sm