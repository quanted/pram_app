from django.template.loader import render_to_string


def stirInputPage(request, model='', header='', formData=None):
    import stir_parameters

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    # html = html + render_to_string('stir_ubertool_config_input.html', {})
    html = html + str(stir_parameters.StirInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # html = html + render_to_string('stir_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try :
        import stir_tooltips
        hasattr(stir_tooltips, 'tooltips')
        tooltips = stir_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html