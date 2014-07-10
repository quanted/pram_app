from django.template.loader import render_to_string


def sipInputPage(request, model='', header='', formData=None):
    import sip_parameters

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('sip_ubertool_config_input.html', {})
    # if formData == None:
    #     html = html + str(sip_parameters.SIPInp())
    # else:
    #     html = html + str(sip_parameters.SIPInp(formData))
    html = html + str(sip_parameters.SIPInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html = html + render_to_string('sip_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import sip_tooltips
        hasattr(sip_tooltips, 'tooltips')
        tooltips = sip_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html