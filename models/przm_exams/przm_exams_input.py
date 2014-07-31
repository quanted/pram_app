"""
.. module:: przm_exams_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def przm_examsInputPage(request, model='', header='', formData=None):
    import przm_exams_parameters
    from models.przm import przm_parameters
    from models.exams import exams_parameters

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_jquery_qtip.html', {})
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model':'przm_exams', 
            'model_attributes':'PRZM-EXAMS Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['PRZM', 'EXAMS'],
                'tab_label': ['PRZM Inputs', 'EXAMS Inputs']
                }
            })
    html = html + """<br><table class="input_table tab tab_PRZM">"""
    html = html + str(przm_parameters.PrzmInp(formData))
    html = html + """</table><table class="input_table tab tab_EXAMS" style="display:none">"""
    html = html + str(exams_parameters.ExamsInp(formData))
    html = html + """
    </table><table class="input_table tab tab_EXAMS n_ph" style="display:none">
        <tr><th><label for="n_ph">Number of Different pH:</label></th>
            <td><select name="n_ph" id="n_ph">
                    <option value="">Make a selection</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                </select>
            </td>
        </tr>
    """ 
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import przm_exams_parameters_tooltips
        hasattr(trex2_tooltips, 'tooltips')
        tooltips = trex2_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html