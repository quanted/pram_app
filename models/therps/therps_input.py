"""
.. module:: therps_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def therpsInputPage(request, model='', header=''):
    import therps_parameters,therps_tooltips

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model':'therps', 
            'model_attributes':'T-Herps Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Chemical', 'Avian', 'Herptile'],
                'tab_label': ['Chemical', 'Avian', 'Herptile']
                }
            })
    html = html + """<br><table class="input_table tab tab_Chemical" border="0">"""
    html = html + str(therps_parameters.trexInp_chem())
    html = html + """</table><table class="input_table tab tab_Avian" border="0" style="display:none">"""
    html = html + str(therps_parameters.trexInp_bird())
    html = html + """</table><table class="input_table tab tab_Herptile" border="0" style="display:none">"""
    html = html + str(therps_parameters.trexInp_herp())
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(therps_tooltips, 'tooltips'):
        tooltips = therps_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html