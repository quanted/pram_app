from django.template.loader import render_to_string


def oreInputPage(request, model='', header='', formData=None):
    import ore_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html = html + render_to_string('04uberinput_ore_start.html', {
        'model': model,
        'model_attributes': header + ' Inputs'})
    html = html + render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['ToxInp', 'CropTargetSel', 'OccHandler'],
            'tab_label': ['Toxicity & Exposure', 'Crop-Target Category Lookup', 'Exposure Scenario']
        }
    })
    html = html + str(ore_parameters.form(formData))
    html = html + render_to_string('04uberinput_ore_end.html', {'sub_title': 'Calculate Exposure'})

    return html
