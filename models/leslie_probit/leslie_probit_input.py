"""
.. module:: sip_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def leslie_probit_input_page(request, model='', header='', form_data=None):
    from . import leslie_probit_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_tabbed_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['chem', 'dose', 'popu'],
            'tab_label': ['Chemical', 'Dose Response', 'Leslie Matrix']
        }
    })
    html += """<br><table class="input_table tab tab_chem" border="0">"""
    html += str(leslie_probit_parameters.leslie_probit_chem())
    html += """</table><table class="input_table tab tab_dose" border="0" style="display:none">"""
    html += str(leslie_probit_parameters.leslie_probit_dose())
    html += """</table><table class="input_table tab tab_popu" border="0" style="display:none">"""
    html += str(leslie_probit_parameters.leslie_probit_popu())

    html += """<table class="input_table tab tab_popu leslie" border="0" style="display:none">"""
    html += """<table class="input_table tab tab_popu no" border="0" style="display:none">"""
    html += render_to_string('leslie_probit_input_jquery.html', {})
    html += render_to_string('04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
    html += render_to_string('04uberinput_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})

    return html
