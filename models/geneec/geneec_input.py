"""
.. module:: geneec_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def geneecInputPage(request, model='', header='', formData=None):
    import geneec_parameters

    # html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('geneec_ubertool_config_input.html', {})
    html = html + str(geneec_parameters.GeneecInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('geneec_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import geneec_tooltips
        hasattr(geneec_tooltips, 'tooltips')
        tooltips = geneec_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':{}})
    return html

