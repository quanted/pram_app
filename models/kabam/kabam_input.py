"""
.. module:: kabam_input
   :synopsis: A useful module indeed.
"""
from django.template.loader import render_to_string


def kabam_input_page(request, model='', header='', form_data=None):
    from . import kabam_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_tabbed_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['Chemical', 'Avian', 'Mammal', 'LargeFish', 'MediumFish', 'SmallFish', 'Filterfeeders',
                           'Invertebrates', 'Zooplankton', 'Phytoplankton', 'Sediment', 'Constants'],
            'tab_label': ['Chemical', 'Avian', 'Mammal', 'Large Fish', 'Medium Fish', 'Small Fish', 'Filter feeders',
                          'Invertebrates', 'Zooplankton', 'Phytoplankton', 'Sediment', 'Constants']
        }
    })
    html += """<br><table class="input_table tab tab_Chemical" border="0">"""
    html += str(kabam_parameters.KabamInp_chem(form_data))
    html += """</table><table class="input_table tab tab_Avian" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_bird(form_data))
    html += """</table><table class="input_table tab tab_Mammal" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_mammal(form_data))
    html += """</table><table class="input_table tab tab_LargeFish" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_lfish(form_data))
    html += """</table><table class="input_table tab tab_MediumFish" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_mfish(form_data))
    html += """</table><table class="input_table tab tab_SmallFish" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_sfish(form_data))
    html += """</table><table class="input_table tab tab_Filterfeeders" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_ff(form_data))
    html += """</table><table class="input_table tab tab_Invertebrates" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_invert(form_data))
    html += """</table><table class="input_table tab tab_Zooplankton" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_zoo(form_data))
    html += """</table><table class="input_table tab tab_Phytoplankton" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_phyto(form_data))
    html += """</table><table class="input_table tab tab_Sediment" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_sed(form_data))
    html += """</table><table class="input_table tab tab_Constants" border="0" style="display:none">"""
    html += str(kabam_parameters.KabamInp_constants(form_data))
    html += render_to_string('04uberinput_tabbed_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import kabam_tooltips
    #     hasattr(kabam_tooltips, 'tooltips')
    #     tooltips = kabam_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
