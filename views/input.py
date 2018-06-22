import importlib
import os

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import iri_to_uri

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

    # viewmodule = importlib.import_module('.views', 'models.'+model)
    # inputmodule = importlib.import_module('.'+model+'_input', 'models.'+model)
    # header = viewmodule.header
    # get formatted model name and description for description page
    model = model.lstrip('/')
    header = get_model_header(model)
    input_module = get_model_input_module(model)
    print(model)
    try:
        print("trying")
        input_page_func = getattr(input_module, model + '_input_page')
        model_parameters_location = 'pram_app.models.' + model + '.' + model + '_parameters'
        # model_input_location = 'pram_app.models.' + model + '.' + model + '_input'
        parametersmodule = importlib.import_module(model_parameters_location)
        input_form = getattr(parametersmodule, model.title() + 'Inp')
    except Exception:
        input_page_func = coming_soon
    if (request.method == "POST"):
        form = input_form(request.POST)
        if (form.is_valid()):
            print("form is valid")
            return HttpResponseTemporaryRedirect('/pram/'+model+'/output/')
        else:
            form_data = request.POST

    # epa template header
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_pram.html', {})


    # function name example: 'sip_input_page'
    html += input_page_func(request, model, header, form_data)

    html += links_left.ordered_list(model, 'run_model')

    # css and scripts
    html += render_to_string('09epa_drupal_pram_css.html', {})
    html += render_to_string('09epa_drupal_pram_scripts.html', {})

    # epa template footer
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)
    return response


class HttpResponseTemporaryRedirect(HttpResponse):
    status_code = 307

    def __init__(self, redirect_to):
        HttpResponse.__init__(self)
        self['Location'] = iri_to_uri(redirect_to)



#generic coming soon function
def coming_soon(request, model, header, form_data):
    html = render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header,
        'TEXT_PARAGRAPH': "<h3> Page coming soon!</h3>"
    })
    html += render_to_string('04ubertext_end_drupal.html', {})
    return html

