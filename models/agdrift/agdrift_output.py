from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def agdriftOutputPage(request):
    import agdrift_model

    drop_size = request.POST.get('drop_size')
    ecosystem_type = request.POST.get('ecosystem_type')
    application_method = request.POST.get('application_method')
    boom_height = request.POST.get('boom_height')
    orchard_type = request.POST.get('orchard_type')
    application_rate = request.POST.get('application_rate')
    aquatic_type = request.POST.get('aquatic_type')
    distance = request.POST.get('distance')
    calculation_input = request.POST.get('calculation_input')
    
    agdrift_obj = agdrift_model.agdrift(True, True, 'single', drop_size, ecosystem_type, application_method, boom_height, orchard_type, application_rate, distance, aquatic_type, calculation_input, None)

    return agdrift_obj