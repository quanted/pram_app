import importlib
import os

from django.http import HttpResponse
from django.template.loader import render_to_string

from . import links_left

print('qed.ubertool_app.views.algorithms')

def get_model_header(model):

    model_views_location = 'ubertool_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header
    return header

def get_model_algorithm(model):
    model_views_location = 'ubertool_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)
    algorithm = viewmodule.algorithm
    return algorithm

def algorithm_page(request, model='none', header='none'):
    print(request.path)
    print('ubertool_app.views.algorithm_page')

    #get formatted model name and description for description page
    model = model.lstrip('/')
    header = get_model_header(model)
    algorithm = get_model_algorithm(model)

    #epa template header
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_ubertool.html', {})

    #main body
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header + ' Algorithms',
        'TEXT_PARAGRAPH': algorithm
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, 'algorithms')

    #css and scripts
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    #html += render_to_string('09epa_drupal_ubertool_scripts.html', {})

    #epa template footer
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)
    return response

