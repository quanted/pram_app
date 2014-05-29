from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

################ How model name appears on web page ################
header = 'IEC'
####################################################################

def iecInputPage(request, model=''):
    import iec_parameters

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('iec_ubertool_config_input.html', {})
    html = html + str(iec_parameters.iecInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('iec_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    # if hasattr(iec_tooltips, 'tooltips'):
    #     tooltips = iec_tooltips.tooltips
    # else:
    #     tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':{}})    

    return html


@require_POST
def iecOutputPage(request):
    import iec_model

    LC50 = float(request.POST.get('LC50'))
    threshold = float(request.POST.get('threshold'))
    dose_response = float(request.POST.get('dose_response'))
    iec_obj = iec_model.iec(True,True,'single',dose_response, LC50, threshold, None)
    return iec_obj
