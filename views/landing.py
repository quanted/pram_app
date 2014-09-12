from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft
import os

def ecoLandingPage(request):
    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'views/main_text.txt'),'r')
    xx = text_file2.read()

    html = render_to_string('01uberheader_main.html', {
            'site_skin' : os.environ['SITE_SKIN']
            })
    html = html + render_to_string('02uberintroblock_nomodellinks.html', {'site_skin' : os.environ['SITE_SKIN']})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04ubertext_start_index.html', {
            'text_paragraph':xx
            })
    html = html + render_to_string('04ubertext_end.html',{})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response

def ubertoolLandingPage(request):
    html = render_to_string('00landing_page.html', {'title':'Ubertool'})

    response = HttpResponse()
    response.write(html)

    return response