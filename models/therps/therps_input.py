"""
.. module:: therps_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def therps_input_page(request, model='', header='', form_data=None):
    import therps_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_tabbed_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['Chemical', 'Avian', 'Herptile'],
            'tab_label': ['Chemical', 'Avian', 'Herptile']
        }
    })
    html += """<br><table class="input_table tab tab_Chemical" border="0">"""
    html += str(therps_parameters.therpsInp_chem(form_data))
    html += """</table><table class="input_table tab tab_Avian" border="0" style="display:none">"""
    html += str(therps_parameters.therpsInp_bird(form_data))
    html += """</table><table class="input_table tab tab_Herptile" border="0" style="display:none">"""
    html += str(therps_parameters.therpsInp_herp(form_data))
    html += render_to_string('04uberinput_tabbed_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import therps_tooltips
    #     hasattr(therps_tooltips, 'tooltips')
    #     tooltips = therps_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
