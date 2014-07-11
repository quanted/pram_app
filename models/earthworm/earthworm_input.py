"""
.. module:: earthworm_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def earthwormInputPage(request, model='', header=''):
    import earthworm_parameters,earthworm_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + str(earthworm_parameters.earthwormInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(earthworm_tooltips, 'tooltips'):
        tooltips = earthworm_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips })    
    
    return html