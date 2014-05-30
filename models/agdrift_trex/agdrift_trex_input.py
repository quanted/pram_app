from django.template.loader import render_to_string


def agdrift_trexInputPage(request, model='', header=''):
    import agdrift_trex_parameters,agdrift_trex_tooltips
    from models.trex2 import trex2_parameters

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model': model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Agdrift', 'Chemical', 'Avian', 'Mammal'],
                'tab_label': ['Agdrift', 'Chemical', 'Avian', 'Mammal']
                }
            })
    html = html + """<br><table class="input_table tab tab_Agdrift" border="0">"""
    html = html + str(agdrift_trex_parameters.agdriftInp())
    html = html + """<br><table class="input_table tab tab_Chemical" border="0" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_chem())
    html = html + """</table><table class="input_table tab tab_Application tab_Chemical" border="0" style="display:none">
                                <tr><th colspan="2" scope="col"><label for="id_noa">Number of Applications:</label></th>
                                    <td colspan="3" scope="col"><select name="noa" id="id_noa">
                                        <option value="1"  selected>1</option></select>
                                    </td>
                                </tr>
                                <tr id="noa_header"><th width="18%">App#</th>
                                                                         <th width="18%" id="rate_head">Rate (lb ai/acre)</th>
                                                                         <th width="18%">Day of Application</th>
                                </tr>
                                <tr class="tab_noa1"><td><input name="jm1" type="text" size="5" value="1"/></td>
                                                     <td><input type="text" size="5" name="rate1" id="id_rate1" value="4"/></td>
                                                     <td><input type="text" size="5" name="day1" id="id_day1" value="0" disabled/></td>
                                </tr>""" 
    html = html + """</table><table class="input_table tab tab_Avian" border="0" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_bird())
    html = html + """</table><table class="input_table tab tab_Mammal" border="0" style="display:none">"""
    html = html + str(trex2_parameters.trexInp_mammal())
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(agdrift_trex_tooltips, 'tooltips'):
        tooltips = agdrift_trex_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html