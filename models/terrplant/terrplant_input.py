"""
.. module:: terrplant_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def terrplant_input_page(request, model='', header='', form_data=None):
    import terrplant_parameters

    html = render_to_string('04uberinput_start_drupal.html', {
        'MODEL': model,
        'TITLE': header})

    #input form
    html += render_to_string('04uberinput_form.html', {
        'FORM': terrplant_parameters.TerrplantInp(form_data)})
    html += render_to_string('04uberinput_end_drupal.html', {})

    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import terrplant_tooltips
    #     hasattr(terrplant_tooltips, 'tooltips')
    #     tooltips = terrplant_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
