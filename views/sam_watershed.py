from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import importlib
import os
from django.conf import settings
from . import links_left
# from pisces_app import views

def get_model_header(model):

    model_views_location = 'ubertool_app.models.' + model + '.views'
    #import_module is py27 specific
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header
    return header

def watershed_page(request, model='pisces', header='none'):
    model = model.lstrip('/')
    header = get_model_header(model)
    x = render_to_string('sam_watershed_map.html')

    """ Returns the html of the references page for pisces. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': header + ' Watershed Output',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    html += links_left.ordered_list(model, 'watershedmap')
    html += render_to_string('10epa_drupal_footer.html', {})


    response = HttpResponse()
    response.write(html)
    return response