"""
.. module:: iec_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def iec_input_page(request, model='', header='', form_data=None):
    from . import iec_parameters

    html = render_to_string('04uberinput_start_drupal.html', {
        'MODEL': model,
        'TITLE': header},
        request=request)
    html += render_to_string('04uberinput_form.html', {
        'FORM': iec_parameters.IecInp(form_data)})
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import iec_tooltips
    #     hasattr(iec_tooltips, 'tooltips')
    #     tooltips = iec_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': {}})

    return html
