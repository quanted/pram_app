"""
.. module:: boilerplate_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def boilerplate_input_page(request, model='', header='', form_data=None):
    import boilerplate_parameters

    html = render_to_string('04uberinput_start_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_form.html', {
        'FORM': boilerplate_parameters.BoilerplateInp(form_data)})
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    try:
        import boilerplate_tooltips
        hasattr(boilerplate_tooltips, 'tooltips')
        tooltips = boilerplate_tooltips.tooltips
    except:
        tooltips = {}
    html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
