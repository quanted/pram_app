"""
.. module:: agdisp_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def agdisp_input_page(request, model='', header='', form_data=None):
    from . import agdisp_parameters

    html = render_to_string('04uberinput_start_drupal.html', {
            'MODEL': model,
            'TITLE': header},
            request=request)
    html += str(agdisp_parameters.AgdispInp(form_data))
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import agdisp_tooltips
    #     hasattr(agdisp_tooltips, 'tooltips')
    #     tooltips = agdisp_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
