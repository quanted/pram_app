from django.template.loader import render_to_string


def sipInputPage(request, model='', header=''):
    import sip_parameters,sip_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('sip_ubertool_config_input.html', {})
    html = html + str(sip_parameters.SIPInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html = html + render_to_string('sip_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    if hasattr(sip_tooltips, 'tooltips'):
        tooltips = sip_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html