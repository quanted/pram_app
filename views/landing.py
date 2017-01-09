from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import links_left
import os
#import secret
from django.conf import settings


def eco_landing_redirect(request):
    return redirect('/ubertool')


def eco_landing_page_new(request):
    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'ubertool_app/views/landing_text.txt'), 'r')
    xx = text_file2.read()

    html = render_to_string('01epa_drupal_header.html', {})
    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': u"\u00FCbertool"
    #})
    html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('04uber_drupal_frog_intro.html', {})
    html += links_left.ordered_list()
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': u"\u00FCbertool",
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('04ubertext_end_drupal.html', {})

    #html += render_to_string('06uberfooter.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def eco_landing_page(request):
    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'ubertool_app/views/landing_text.txt'), 'r')
    xx = text_file2.read()

    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02uberintroblock_nomodellinks_drupal.html', {})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': u"\u00FCbertool",
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list()
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)

    return response