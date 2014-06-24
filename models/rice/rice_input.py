"""
.. module:: rice_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def riceInputPage(request, model='', header=''):
    """ handle rice input """
    import rice_parameters

    html = render_to_string('04uberinput_start.html', {
            'model':model,
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('rice_ubertool_config_input.html', {})
    html = html + str(rice_parameters.RiceInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html = html + render_to_string('rice_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import rice_tooltips
        hasattr(rice_tooltips, 'tooltips')
        tooltips = rice_tooltips.tooltips
    except:
        tooltips = {}   
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html
