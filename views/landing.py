from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import links_left
import os
import secret
from django.conf import settings


def eco_landing_redirect(request):
    return redirect('/ubertool')


def eco_landing_page(request):
    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'views/landing_text.txt'), 'r')
    xx = text_file2.read()

    html = render_to_string('01uberheader_main_drupal.html', {
        'site_skin': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02uberintroblock_nomodellinks_drupal.html', {
        'site_skin': os.environ['SITE_SKIN']}
     )
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': u"\u00FCbertool",
        'text_paragraph': xx
    })
    html += render_to_string('04ubertext_end.html', {})
    html += links_left.ordered_list()
    html += render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response


def ubertool_landing_page(request):
    if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
        html = render_to_string('00landing_page_qed_slides_public.html', {'title': 'Ubertool'})
    else:
        html = render_to_string('00landing_page_qed_slides.html', {'title': 'Ubertool'})

    response = HttpResponse()
    response.write(html)

    return response
