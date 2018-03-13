import importlib
import os

from django.http import HttpResponse
from django.template.loader import render_to_string

from . import links_left

#import secret

print('qed.pram_app.views.input')

def get_model_header(model):

    model_views_location = 'pram_app.models.' + model + '.views'
    #import_module is py27 specific
    viewmodule = importlib.import_module(model_views_location)
    header = viewmodule.header
    return header

def get_model_input_module(model):

    model_module_location = 'pram_app.models.' + model + '.' + model + '_input'
    # import_module is py27 specific
    model_input_module = importlib.import_module(model_module_location)
    return model_input_module

def input_page(request, model='none', header='none', form_data=None):

    print(request.path)
    print('pram_app.views.input_page')
    # If on public server, test user authentication
    # if settings.AUTH:
    #     if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
    #         if not request.user.is_authenticated():
    #             return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    #viewmodule = importlib.import_module('.views', 'models.'+model)
    #inputmodule = importlib.import_module('.'+model+'_input', 'models.'+model)
    #header = viewmodule.header
    #get formatted model name and description for description page
    model = model.lstrip('/')
    header = get_model_header(model)
    input_module = get_model_input_module(model)

    #epa template header
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_pram.html', {})

    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': header})
    #html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
    #    'CONTACT_URL': os.environ['CONTACT_URL'],
    #    'MODEL': model,
    #    'PAGE': 'input'})

    # function name example: 'sip_input_page'
    input_page_func = getattr(input_module, model + '_input_page')
    html += input_page_func(request, model, header, form_data)

    html += links_left.ordered_list(model, 'run_model')

    #css and scripts
    html += render_to_string('09epa_drupal_pram_css.html', {})
    html += render_to_string('09epa_drupal_pram_scripts.html', {})

    #epa template footer
    html += render_to_string('10epa_drupal_footer.html', {})
    
    response = HttpResponse()
    response.write(html)
    return response


def input_page_old(request, model='none', header='none'):
    print(request.path)
    print('pram_app.views.input_page')
    # If on public server, test user authentication
    # if settings.AUTH:
    #     if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
    #         if not request.user.is_authenticated():
    #             return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # viewmodule = importlib.import_module('.views', 'models.'+model)
    # inputmodule = importlib.import_module('.'+model+'_input', 'models.'+model)
    # header = viewmodule.header
    # get formatted model name and description for description page
    model = model.lstrip('/')
    header = get_model_header(model)
    input_module = get_model_input_module(model)

    # import logging

    # if formData != None:
    #     logging.info("===================== N O N E ==========================")
    #     html = render_to_string('01uberheader.html', {'title': header+' Inputs'})
    #     html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'input'})
    #     html = html + ordered_list.ordered_list()

    #     input_page_func = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    #     html = html + input_page_func(request, model, header, formData)

    #     html = html + render_to_string('06uberfooter.html', {'links': ''})

    #     response = HttpResponse()
    #     response.write(html)
    #     return response

    # VALIDATE FORM HERE IF FORM IS POSTED TO THIS VIEW
    # if request.method == "POST":
    #     parametersmodule = importlib.import_module('.'+model+'_parameters', 'models.'+model)
    #     inputForm = getattr(parametersmodule, model.upper() + 'Inp')

    #     logging.info(inputForm)
    #     form = inputForm(request.POST)

    #     logging.info(form)

    #     if form.is_valid():
    #         outputmodule = importlib.import_module('.'+model+'_output', 'models.'+model)
    #         return outputmodule(request)
    #     else:
    #         html = render_to_string('01uberheader.html', {'title': header+' Inputs'})
    #         html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'input'})
    #         html = html + ordered_list.ordered_list()

    #         input_page_func = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    #         html = html + input_page_func(request, model, header, formData=request.POST)

    #         html = html + render_to_string('06uberfooter.html', {'links': ''})

    #         response = HttpResponse()
    #         response.write(html)
    #         return response

    # else:


    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': header})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL'],
        'MODEL': model,
        'PAGE': 'input'})

    # function name example: 'sip_input_page'
    input_page_func = getattr(input_module, model + '_input_page')
    html += input_page_func(request, model, header)

    html += links_left.ordered_list(model, 'run_model')
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)
    return response
