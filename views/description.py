from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import links_left
import os

print('qed.ubertool_app.views.description')

def get_model_header(model):

    model_views_location = 'ubertool_app.models.' + model + '.views'
    #import_module is py27 specific
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header
    return header


def get_model_description(model):
    model_views_location = 'ubertool_app.models.' + model + '.views'
    #import_module is py27 specific
    viewmodule = importlib.import_module(model_views_location)
    description = viewmodule.description
    return description


def description_page(request, model='none', header='none'):
    print(request.path)
    print('ubertool_app.views.description_page')

    #get formatted model name and description for description page
    model = model.lstrip('/')
    header = get_model_header(model)
    description = get_model_description(model)

    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': header + ' Description'})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL'],
        'MODEL': model,
        'PAGE': 'description'})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': header + ' Overview',
        'TEXT_PARAGRAPH': description})
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model)
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)
    return response
