from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


################ How model name appears on web page ################
header = 'AgDrift'
####################################################################

def agdriftInputPage(request, model=''):
    import agdrift_parameters,agdrift_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + str(agdrift_parameters.agdriftInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(agdrift_tooltips, 'tooltips'):
        tooltips = agdrift_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html


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