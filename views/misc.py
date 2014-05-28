from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

#######################################################################################
################################ HTTP Error Pages #####################################
#######################################################################################

def fileNotFound(request):
    html = render_to_string('01uberheader.html', {'title': 'Error'})
    html = html + render_to_string('02uberintroblock_nomodellinks.html', {'title2':'File not found'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04ubertext_start.html', {
            'model_attributes': 'File Not Found',
            'text_paragraph': ""})
    html = html + """ <img src="/static/images/404error.png" width="300" height="300">"""
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response