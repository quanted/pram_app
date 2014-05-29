from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

################ How model name appears on web page ################
header = 'Earthworm'
####################################################################

def earthwormInputPage(request, model=''):
    import earthworm_parameters
    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('earthworm_ubertool_config_input.html', {})
    html = html + str(earthworm_parameters.earthwormInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('earthworm_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    # if hasattr(earthworm_tooltips, 'tooltips'):
    #     tooltips = earthworm_tooltips.tooltips
    # else:
    #     tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':{}})    
    return html


@require_POST
def earthwormOutputPage(request):
    import earthworm_model
    k_ow = float(request.POST.get('k_ow'))
    l_f_e = float(request.POST.get('l_f_e'))
    c_s = float(request.POST.get('c_s'))
    k_d = float(request.POST.get('k_d'))
    p_s = float(request.POST.get('p_s'))
    c_w = float(request.POST.get('c_w'))
    m_w = float(request.POST.get('m_w'))
    p_e = float(request.POST.get('p_e'))
    
    earthworm_obj = earthworm_model.earthworm(True,True,'single', k_ow,l_f_e,c_s,k_d,p_s,c_w,m_w,p_e)
    return earthworm_obj
