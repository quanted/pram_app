"""
.. module:: agdrift_therps_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def agdrift_therpsInputPage(request, model='', header='', formData=None):
    from models.agdrift import agdrift_parameters
    from models.therps import therps_parameters

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
    html = html + str(agdrift_parameters.AgdriftInp(formData))
    html = html + """<br><table class="input_table tab tab_Chemical" style="display:none">"""
    html = html + str(therps_parameters.therpsInp_chem(formData))
    html = html + """</table><table class="input_table tab tab_Avian" style="display:none">"""
    html = html + str(therps_parameters.therpsInp_bird(formData))
    html = html + """</table><table class="input_table tab tab_Herptile" style="display:none">"""
    html = html + str(therps_parameters.therpsInp_herp(formData))
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import agdrift_therps_tooltips
        hasattr(agdrift_therps_tooltips, 'tooltips')
        tooltips = agdrift_therps_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html