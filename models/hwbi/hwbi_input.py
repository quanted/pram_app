"""
.. module:: hwbi_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def hwbiInputPage(request, model='', header='', formData=None):
    import hwbi_parameters

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('hwbi_ubertool_config_input.html', {})
    html = html + str(hwbi_parameters.IecInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('hwbi_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import hwbi_tooltips
        hasattr(hwbi_tooltips, 'tooltips')
        tooltips = hwbi_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':{}})    

    return html