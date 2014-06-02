from django.template.loader import render_to_string


def examsInputPage(request, model='', header=''):
    import exams_parameters
              
    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start.html', {
            'model':'exams', 
            'model_attributes':'EXAMS Inputs'})
    html = html + str(exams_parameters.EXAMSInp())
    html = html + """
    </table>
    <table class="n_ph" align="center">
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
                <option value="10">10</option></select>
            </td>
        </tr>
    """ 
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import exams_tooltips
        hasattr(exams_tooltips, 'tooltips')
        tooltips = exams_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html