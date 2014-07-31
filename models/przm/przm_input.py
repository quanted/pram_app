"""
.. module:: przm_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def przmInputPage(request, model='', header='', formData=None):
    import przm_parameters

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_jquery_qtip.html', {})
    html = html + render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('przm_ubertool_config_input.html', {})
    html = html + str(przm_parameters.PrzmInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('przm_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import przm_tooltips
        hasattr(przm_tooltips, 'tooltips')
        tooltips = przm_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html