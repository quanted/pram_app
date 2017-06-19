"""
.. module:: beerex_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def beerex_input_page(request, model='', header='', form_data=None):
    from . import beerex_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_form.html', {
        'FORM': beerex_parameters.BeerexInp(form_data)})
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import beerex_tooltips
    #     hasattr(beerex_tooltips, 'tooltips')
    #     tooltips = beerex_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
