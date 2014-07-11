"""
.. module:: agdrift_therps_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def agdrift_therpsInputPage(request, model='', header=''):
    import agdrift_therps_parameters,agdrift_therps_tooltips
    from models.trex2 import trex2_parameters

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model':model,
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Agdrift', 'Chemical', 'Avian', 'Herptile'],
                'tab_label': ['Agdrift', 'Chemical', 'Avian', 'Herptile']
                }
            })
    html = html + """<br><table class="input_table tab tab_Agdrift">"""
    html = html + str(agdrift_therps_parameters.agdriftInp())
    html = html + """<br><table class="input_table tab tab_Chemical" style="display:none">"""
    html = html + str(agdrift_therps_parameters.trexInp_chem())
    html = html + """</table><table class="input_table tab tab_Avian" style="display:none">"""
    html = html + str(agdrift_therps_parameters.trexInp_bird())
    html = html + """</table><table class="input_table tab tab_Herptile" style="display:none">"""
    html = html + str(agdrift_therps_parameters.trexInp_herp())
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(agdrift_therps_tooltips, 'tooltips'):
        tooltips = agdrift_therps_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html