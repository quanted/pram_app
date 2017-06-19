from django.template.loader import render_to_string
from . import links_left
import os

def drupal_2017_header(html):

    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_ubertool.html', {})
    return html

def drupal_2017_footer(html):

    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list()  # fills out 05ubertext_links_left_drupal.html
    #scripts and footer
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    #html += render_to_string('09epa_drupal_ubertool_scripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    return html