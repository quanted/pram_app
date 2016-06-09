"""
.. module:: sam_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def sam_input_page(request, model='', header='', form_data=None):
    import sam_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_tabbed_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['Chemical Fate', 'Application', 'Simulation', 'Output Options'],
            'tab_label': ['Chemical', 'Application', 'Simulation', 'Output']
        }
    })
    html += """<br><table class="input_table tab tab_Chemical">"""
    html += str(sam_parameters.SamInp_chem(form_data))
    html += """</table><table class="input_table tab tab_Application" style="display:none">"""
    html += str(sam_parameters.SamInp_app(form_data))
    html += str(sam_parameters.SamInp_app_refine(form_data))
    html += """</table><table class="input_table tab tab_Simulation" style="display:none">"""
    html += str(sam_parameters.SamInp_sim(form_data))
    html += """</table><table class="input_table tab tab_Output" style="display:none">"""
    html += str(sam_parameters.SamInp_output(form_data))
    html += render_to_string('04uberinput_tabbed_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import sam_parameters
    #     hasattr(sam_parameters, 'tooltips')
    #     tooltips = sam_parameters.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
