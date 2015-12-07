"""
.. module:: earthworm_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def earthwormInputPage(request, model='', header='', formData=None):
    import earthworm_parameters
    html = render_to_string('04uberinput_start.html', {
        'model': model, 'model_attributes': header+' Inputs'})
    html = html + str(earthworm_parameters.EarthwormInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import earthworm_tooltips
        hasattr(earthworm_tooltips, 'tooltips')
        tooltips = earthworm_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})
    return html
