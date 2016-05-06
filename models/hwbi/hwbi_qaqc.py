"""
.. module:: hwbi_qaqc
   :synopsis: A useful module indeed.
"""
import importlib
import os
from django.http import HttpResponse
from django.template.loader import render_to_string


PROJECT_ROOT = os.environ['PROJECT_PATH']


def qaqcRunView(request, model="hwbi"):
    """
        View to render the QAQC output page HTML
    """
    uber_views_module = importlib.import_module('views', '..')
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    html = render_to_string('01uberheader.html', {
            'site_skin': os.environ['SITE_SKIN'],
            'title': header+' QA/QC'})
    html = html + render_to_string('hwbi/02uberintroblock_wmodellinks.html', {
            'site_skin': os.environ['SITE_SKIN'],
            'model': model,
            'page': 'qaqc'})
    html = html + uber_views_module.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model':model,
            'model_attributes': header+' QAQC'})
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {'sub_title': ''})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response
