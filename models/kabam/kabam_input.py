"""
.. module:: kabam_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def kabamInputPage(request, model='', header=''):
    import kabam_parameters,kabam_tooltips
 
    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Chemical', 'Avian', 'Mammal', 'LargeFish', 'MediumFish', 'SmallFish', 'Filterfeeders', 'Invertebrates', 'Zooplankton', 'Phytoplankton', 'Sediment', 'Constants'],
                'tab_label': ['Chemical', 'Avian', 'Mammal', 'Large Fish', 'Medium Fish', 'Small Fish', 'Filter feeders', 'Invertebrates', 'Zooplankton', 'Phytoplankton', 'Sediment', 'Constants']
                }
            })
    html = html + """<br><table class="input_table tab tab_Chemical" border="0">"""
    html = html + str(kabam_parameters.KabamInp_chem())
    html = html + """</table><table class="input_table tab tab_Avian" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_bird())
    html = html + """</table><table class="input_table tab tab_Mammal" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_mammal())
    html = html + """</table><table class="input_table tab tab_LargeFish" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_lfish())
    html = html + """</table><table class="input_table tab tab_MediumFish" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_mfish())
    html = html + """</table><table class="input_table tab tab_SmallFish" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_sfish())
    html = html + """</table><table class="input_table tab tab_Filterfeeders" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_ff())
    html = html + """</table><table class="input_table tab tab_Invertebrates" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_invert())
    html = html + """</table><table class="input_table tab tab_Zooplankton" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_zoo())
    html = html + """</table><table class="input_table tab tab_Phytoplankton" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_phyto())
    html = html + """</table><table class="input_table tab tab_Sediment" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_sed())
    html = html + """</table><table class="input_table tab tab_Constants" border="0" style="display:none">"""
    html = html + str(kabam_parameters.KabamInp_constants())
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(kabam_tooltips, 'tooltips'):
        tooltips = kabam_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html