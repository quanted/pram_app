from django.template.loader import render_to_string


def przmInputPage(request, model='', header=''):
    import przm_parameters,przm_tooltips

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_jquery_qtip.html', {})
    html = html + render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('przm_ubertool_config_input.html', {})
    html = html + str(przm_parameters.PRZMInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('przm_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    if hasattr(przm_tooltips, 'tooltips'):
        tooltips = przm_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html