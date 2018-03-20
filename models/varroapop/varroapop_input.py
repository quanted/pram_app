"""
.. module:: beerex_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

from . import varroapop_parameters


def varroapop_input_page(request, model='', header='', form_data=None):

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_tabbed_drupal.html', {
        'MODEL': model,
        'TITLE': header},
        request=request)
    html += render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['Colony', 'Mites', 'Chemical', 'Resources'],
            'tab_label': ['Colony', 'Mites', 'Chemical', 'Resources']
        }
    })
    html += """<br><table class="input_table tab tab_Colony">"""
    html += str(varroapop_parameters.VarroapopInp_colony(form_data))
    html += """</table><table class="input_table tab tab_Mites" style="display:none">"""
    html += str(varroapop_parameters.VarroapopInp_mites(form_data))
    html += """</table><table class="input_table tab tab_Chemical" style="display:none">"""
    html += str(varroapop_parameters.VarroapopInp_chemical(form_data))
    html += """</table><table class="input_table tab tab_Resources" style="display:none">"""
    html += str(varroapop_parameters.VarroapopInp_resources(form_data))
    html += render_to_string('04uberinput_tabbed_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import varroapop_tooltips
    #     hasattr(varroapop_tooltips, 'tooltips')
    #     tooltips = varroapop_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
