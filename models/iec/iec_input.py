"""
.. module:: iec_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def iecInputPage(request, model='', header='', formData=None):
    import iec_parameters

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('iec_ubertool_config_input.html', {})
    html = html + str(iec_parameters.IecInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('iec_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import iec_tooltips
        hasattr(iec_tooltips, 'tooltips')
        tooltips = iec_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':{}})    

    return html