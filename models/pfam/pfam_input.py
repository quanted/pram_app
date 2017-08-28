"""
.. module:: pfam_input
   :synopsis: A useful module indeed.
"""
from django.template.loader import render_to_string
 

def pfamInputPage(request, model='', header='', formData=None):

    from . import pfam_parameters
 
    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_jquery_qtip.html', {})
    html = html + render_to_string('04uberinput_start_tabbed.html', {
            'model':model,
            'model_attributes': header+' Inputs'},
            request=request)
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
            'nav_dict': {
                'class_name': ['Chemical', 'Application', 'Location', "Floods", "Crop", "Physical", "Output"],
                'tab_label': ['Chemical', 'Application', 'Location', "Floods", "Crop", "Physical", "Output"]
                }
            })
    html = html + """<br><table class="input_table tab tab_Chemical">"""
    html = html + str(pfam_parameters.PFAMInp_chem(formData))
    html = html + """</table><table class="input_table tab tab_Application" style="display:none">
                                <tr><th colspan="2" scope="col"><label for="id_noa">Number of Applications:</label></th>
                                    <td colspan="3" scope="col"><select name="noa" id="id_noa">
                                        <option value="">Make a selection</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                        <option value="11">11</option>
                                        <option value="12">12</option>
                                        <option value="13">13</option>
                                        <option value="14">14</option>
                                        <option value="15">15</option>
                                        <option value="16">16</option>
                                        <option value="17">17</option>
                                        <option value="18">18</option>
                                        <option value="19">19</option>
                                        <option value="20">20</option>
                                        <option value="21">21</option>
                                        <option value="22">22</option>
                                        <option value="23">23</option>
                                        <option value="24">24</option>
                                        <option value="25">25</option>
                                        <option value="26">26</option>
                                        <option value="27">27</option>
                                        <option value="28">28</option>
                                        <option value="29">29</option>
                                        <option value="30">30</option>
                                    </td>
                                </tr>"""        
            
    html = html + """</table><table class="input_table tab tab_Location" style="display:none">"""    
    html = html + str(pfam_parameters.PFAMInp_loc(formData))
    html = html + """</table><table class="input_table tab tab_Floods" style="display:none">
                                <tr><th></th><th colspan="2" scope="col"><label for="id_nof">Number of Floods Events:</label></th>
                                    <td colspan="2" scope="col"><select name="nof" id="id_nof">
                                        <option value="">Make a selection</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </td>
                                </tr>
                                <tr><th></th><th colspan="2"><label for="id_date_f1">Date for Event 1:</label></th>
                                    <td colspan="2"><input type="text" name="date_f1" value="MM/DD" id="id_date_f1" /></td>
                                </tr>"""    

    html = html + """</table><table class="input_table tab tab_Crop" style="display:none">"""      
    html = html + str(pfam_parameters.PFAMInp_cro(formData))                
    html = html + """</table><table class="input_table tab tab_Physical" style="display:none">"""      
    html = html + str(pfam_parameters.PFAMInp_phy(formData))
    html = html + """</table><table class="input_table tab tab_Output" style="display:none">"""    
    html = html + str(pfam_parameters.PFAMInp_out(formData))     
                
    html = html + render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import pfam_tooltips
        hasattr(pfam_tooltips, 'tooltips')
        tooltips = pfam_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html