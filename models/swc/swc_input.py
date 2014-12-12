"""
.. module:: swc_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def swcInputPage(request, model='', header='', formData=None):
    import swc_parameters
    from models.przm5 import przm5_parameters
    from models.vvwm import vvwm_parameters
    
    # html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = render_to_string('04uberinput_start_tabbed.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('swc-jquery.html', {})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Chemical', 'Applications', 'CropLand', 'Runoff', 'WaterBody'],
                'tab_label': ['Chemical', 'Applications', 'Crop/Land', 'Runoff', 'Water Body']
                }
            })
    html = html + """<br><table class="input_table tab tab_Chemical">"""
    html = html + str(przm5_parameters.przm5Inp_chem(formData))
    html = html + str(vvwm_parameters.vvwmInp_chem())
    html = html + """</table><table class="input_table tab tab_Chemical0">"""
    html = html + str(przm5_parameters.przm5Inp_chem0(formData))
    html = html + """</table><table class="input_table tab tab_Chemical1" style="display:none">
                        <tr><th colspan="2">Degradate 1</th></tr>
                        """
    html = html + str(przm5_parameters.przm5Inp_chem1(formData))
    html = html + """</table><table class="input_table tab tab_Chemical_MCF1" style="display:none">
                        <tr><th colspan="2">Molar Conversion Factors (Degradate 1)</th></tr>
                        """
    html = html + str(przm5_parameters.przm5Inp_mcf1(formData))
    html = html + """</table><table class="input_table tab tab_Chemical2" style="display:none">
                        <tr><th colspan="2">Degradate 2</th></tr>
                        """
    html = html + str(przm5_parameters.przm5Inp_chem2(formData))
    html = html + """</table><table class="input_table tab tab_Chemical_MCF2" style="display:none">
                        <tr><th colspan="2">Molar Conversion Factors (Degradate 2)</th></tr>
                        """
    html = html + str(przm5_parameters.przm5Inp_mcf2(formData))
    html = html + """</table><table class="input_table tab tab_Applications" style="display:none">"""
    html = html + str(przm5_parameters.przm5Inp_appl(formData))
    html = html + """
                    <tr>
                        <th width="55px">Day</th>
                        <th width="56px">Month</th>
                        <th width="68px">Year</th>
                        <th width="74px">Amount (kg/hA)</th>
                        <th width="104px">Application Method</th>
                        <th width="74px">Depth (cm)</th>
                        <th width="68px">Eff.</th>
                        <th width="75px">Drift/T</th>
                    </tr>
                    
                    """
    # html = html + template.render (templatepath + 'vvwm_weatherfile.html', {})
    html = html + """</table><table class="input_table tab tab_CropLand" style="display:none">"""
    html = html + str(vvwm_parameters.vvwmInp_cropland(formData))
    html = html + str(przm5_parameters.przm5Inp_cropland(formData))
    html = html + """</table><table class="input_table tab tab_Runoff" style="display:none">"""
    html = html + str(przm5_parameters.przm5Inp_runoff(formData))
    html = html + """</table><table class="input_table tab tab_WaterBody" style="display:none">"""
    html = html + str(przm5_parameters.przm5Inp_waterbody(formData))
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})

    # Check if tooltips dictionary exists
    try:
        import swc_tooltips
        hasattr(swc_tooltips, 'tooltips')
        tooltips = swc_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html