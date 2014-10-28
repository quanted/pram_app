"""
.. module:: sam_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def samInputPage(request, model='', header='', formData=None):
    import sam_parameters

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Chemical Fate', 'Application', 'Simulation', 'Output Options'],
                'tab_label': ['Chemical', 'Application', 'Simulation', 'Output']
                }
            })
    html = html + """<br><table class="input_table tab tab_Chemical">"""
    html = html + str(sam_parameters.SamInp_chem(formData))
    html = html + """</table><table class="input_table tab tab_Application" style="display:none">"""
    html = html + str(sam_parameters.SamInp_app(formData))
    html = html + str(sam_parameters.SamInp_app_refine(formData))
    html = html + """</table><table class="input_table tab tab_Simulation" style="display:none">"""
    html = html + str(sam_parameters.SamInp_sim(formData))
    html = html + """</table><table class="input_table tab tab_Output" style="display:none">"""
    html = html + str(sam_parameters.SamInp_output(formData))
#    html = html + """<iframe src="http://134.67.114.4/maptest/" width="640" height="480"></iframe>"""
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import sam_parameters
        hasattr(sam_parameters, 'tooltips')
        tooltips = sam_parameters.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html
