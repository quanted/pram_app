import importlib
import logging
import os
import requests
import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

from . import input
from . import links_left
from ..models import model_handler
from ..REST import rest_funcs

print('qed.pram_app.views.output')


def output_page_html(header, model, tables_html):
    """Generates HTML to fill '.articles_output' div on output page"""

    #epa template header
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_pram.html', {})

    #main body
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header + ' Output',
        'TEXT_PARAGRAPH': tables_html
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model)

    #css and scripts
    html += render_to_string('09epa_drupal_pram_css.html', {})
    #html += render_to_string('09epa_drupal_pram_scripts.html', {})

    #epa template footer
    html += render_to_string('10epa_drupal_footer.html', {})
    return html


def output_page_view(request, model='none', header=''):
    """
    Django view render method for model output pages.  This method is called 
    by output_page() method.
    """

    logging.info('=========== New Model Handler - Single Model Run ===========')
    print(request)
    model_obj = model_handler.model_input_post_receiver(request, model)
    #logging.info(model_obj)
    if type(model_obj) is tuple:
        model_output_html = model_obj[0]
        model_obj = model_obj[1]
    else:
        # Dynamically import the model table module
        tablesmodule = importlib.import_module('.' + model + '_tables', 'pram_app.models.' + model)
        # logging.info(model_obj.__dict__)
        """ Generate Timestamp HTML from "*_tables" module """
        model_output_html = tablesmodule.timestamp(model_obj)
        """ Generate Model input & output tables HTML from "*_tables" module """
        tables_output = tablesmodule.table_all(model_obj)
        """ Append Timestamp & model input & output table's HTML """
        if type(tables_output) is tuple:
            model_output_html = model_output_html + tables_output[0]
        elif type(tables_output) is str or type(tables_output) is unicode:
            model_output_html = model_output_html + tables_output
        else:
            model_output_html = "table_all() Returned Wrong Type"

    """ Render output page view HTML """
    html = output_page_html(header, model, model_output_html)
    response = HttpResponse()
    response.write(html)
    return response


@require_POST
def output_page(request, model='none', header=''):
    """
    Django HTTP POST handler for output page.  Receives form data which has been validated by input.py.
    Calls method to render the output.
    This method maps to: '/pram/<model>/output'
    """
    model_views_location = 'pram_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header

    if model == 'sam':
        task = {}
        try:
            inputs = request.POST.dict()
            if os.environ['IN_DOCKER'] == "False":
                task = requests.post('http://localhost:7777/rest/pram/sam/', data=inputs)
            else:
                task = requests.post('http://qed-nginx:7777/rest/pram/sam/', data=inputs)
            task_id = json.loads(task.content.decode(encoding="utf-8").replace("//", ""))
            return redirect('/pram/sam/output/status/' + task_id['task_id'])
        except Exception as ex:
            print("Error attempting to connect to flask endpoint for sam. " + str(ex))
            return redirect('/pram/sam/output/status/1234567890')
            # return redirect('/pram/sam/output/status/' + task_id['task_id'])

    else:
        return output_page_view(request, model, header)
