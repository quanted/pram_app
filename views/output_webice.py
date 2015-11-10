"""
Created on Tue Jan 03 13:30:41 2012
@author: Jon F.
"""

from django.template.loader import render_to_string
from django.http import HttpResponse
import linksLeft
import os

def ICETabletPage(requests):

    html = render_to_string('webice_ICETable.html', {})
    
    response = HttpResponse()
    response.write(html)
    return response

def webiceSSDOutputPage(requests):

    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': 'Web-ICE Output'})
    html = html + render_to_string('webiceSSD-jqueryOutput.html', {})
    html = html + render_to_string('02uberintroblock_wmodellinks.html',  {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':'webice',
            'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model':'webice', 
            'model_attributes':'Web-ICE v3.2.1 Output'})
    html = html + render_to_string('webiceSSDOutput.html', {})
    html = html + render_to_string('04uberwebice_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response

def webiceTNEOutputPage(requests):

    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': 'Web-ICE Output'})
    html = html + render_to_string('webiceTNE-jqueryOutput.html', {})
    html = html + render_to_string('02uberintroblock_wmodellinks.html',  {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':'webice',
            'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model':'webice', 
            'model_attributes':'Web-ICE v3.2.1 Output'})
    html = html + render_to_string('webiceTNEOutput.html', {})
    html = html + render_to_string('04uberwebice_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response

def webiceOutputPage(request):
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': 'Web-ICE Output'})
    html = html + render_to_string('webice-jqueryOutput.html', {})
    html = html + render_to_string('02uberintroblock_wmodellinks.html',  {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':'webice',
            'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model':'webice', 
            'model_attributes':'Web-ICE v3.2.1 Output'})
    html = html + render_to_string('webiceOutput.html', {})
    html = html + render_to_string('04uberwebice_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response