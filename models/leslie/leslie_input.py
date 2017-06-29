"""
.. module:: sip_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def leslie_input_page(request, model='', header='', form_data=None):
    from . import leslie_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_form.html', {
        'FORM': leslie_parameters.leslieInp(form_data)})
    html = html + """<table class="leslie" border="0">"""
    html = html + """<table class="no" border="0">"""
    html = html + render_to_string('leslie-input-jquery.html', {})
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})

    # Check if tooltips dictionary exists
    # try:
    #     import sip_tooltips
    #     hasattr(sip_tooltips, 'tooltips')
    #     tooltips = sip_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html