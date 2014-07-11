"""
.. module:: dust_batch_runner
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def dustInputPage(request, model='', header=''):
    import dust_parameters,dust_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('dust_ubertool_config_input.html', {})
    html = html + str(dust_parameters.DustInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('dust_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    if hasattr(dust_tooltips, 'tooltips'):
        tooltips = dust_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html