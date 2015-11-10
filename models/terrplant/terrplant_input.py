"""
.. module:: terrplant_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def terrplantInputPage(request, model='', header='', formData=None):
    import terrplant_parameters
    
    # html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('terrplant_ubertool_config_input.html', {})  
    html = html + str(terrplant_parameters.TerrplantInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html = html + render_to_string('terrplant_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import terrplant_tooltips
        hasattr(terrplant_tooltips, 'tooltips')
        tooltips = terrplant_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html
