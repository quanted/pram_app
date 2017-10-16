import importlib
import os

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from ... views import links_left


def olanding_page(header, model):
    html = olanding_html(header, model)
    response = HttpResponse(html)
    return response


def olanding_html(header, model):
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_ubertool.html', {})
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += render_to_string('sam_output_landing.html', {})

    html += links_left.ordered_list(model)
    html += render_to_string('09epa_drupal_ubertool_css.html', {})

    html += render_to_string('10epa_drupal_footer.html', {})
    return html

