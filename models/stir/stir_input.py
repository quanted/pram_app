from django.template.loader import render_to_string


def stirInputPage(request, model='', header=''):
    import stir_parameters,stir_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('stir_ubertool_config_input.html', {})
    html = html + str(stir_parameters.StirInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('stir_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    if hasattr(stir_tooltips, 'tooltips'):
        tooltips = stir_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html