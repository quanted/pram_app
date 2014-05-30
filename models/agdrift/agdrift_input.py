from django.template.loader import render_to_string


def agdriftInputPage(request, model='', header=''):
    import agdrift_parameters,agdrift_tooltips

    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + str(agdrift_parameters.agdriftInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    if hasattr(agdrift_tooltips, 'tooltips'):
        tooltips = agdrift_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html