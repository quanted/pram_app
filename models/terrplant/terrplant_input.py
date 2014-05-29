from django.template.loader import render_to_string


def terrplantInputPage(request, model='', header=''):
    import terrplant_parameters,terrplant_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('terrplant_ubertool_config_input.html', {})  
    html = html + str(terrplant_parameters.TerrPlantInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html = html + render_to_string('terrplant_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    if hasattr(terrplant_tooltips, 'tooltips'):
        tooltips = terrplant_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html