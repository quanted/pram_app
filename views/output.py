import importlib
import logging
import os

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from . import links_left
from ..models import model_handler
from ..REST import rest_funcs
#from ..models import sam.sam_tables.tablesmodule

print('qed.ubertool_app.views.output')

_UPDATED_MODELS = (
    'agdrift',
    'beerex',
    'earthworm',
    'exponential',
    'iec',
    'kabam',
    'loons',
    'rice',
    'sam',
    'sip',
    'stir',
    'trex',
    'terrplant',
    'therps',
)


def output_page_html(header, model, tables_html):
    """Generates HTML to fill '.articles_output' div on output page"""

    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': header})
    #html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
    #    'CONTACT_URL': os.environ['CONTACT_URL'],
    #    'MODEL': model,
    #    'PAGE': 'description'})

    #epa template header
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool"
    })
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_ubertool.html', {})

    #main body
    #need from css love from here
    #html += render_to_string('04uberoutput_start_drupal.html', {
    #    'TITLE': header + ' Output'})
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': header + ' Output',
        'TEXT_PARAGRAPH': tables_html
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model)

    #html += render_to_string('04uberoutput_start_drupal.html', {
    #    'TITLE': header + ' Output'})
    #html += tables_html
    ## if model is not "sam":
    ##
    ##     html += render_to_string('export.html', {})
    #html += render_to_string('04ubertext_end_drupal.html', {})
    #html += links_left.ordered_list(model, 'run_model')

    #css and scripts
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    #html += render_to_string('09epa_drupal_ubertool_scripts.html', {})

    #epa template footer
    html += render_to_string('10epa_drupal_footer.html', {})

    return html


def output_page_view(request, model='none', header=''):
    """
    Django view render method for model output pages.  This method is called 
    by output_page() method.
    """

    # If model is updated to be generic, use generic Model object
    # if not, use old method with '*_output' module
    if model in _UPDATED_MODELS:
        logging.info('=========== New Model Handler - Single Model Run ===========')
        print(request)
        model_obj = model_handler.model_input_post_receiver(request, model)

    # elif model in {'sam'}:
    #     logging.info('=========== New Model Handler FORTRAN ===========')
    #
    #     if model == 'sam':
    #         """
    #         SAM takes a long time to run relative to other models; therefore,
    #         it will not return model results on form submit, but will instead
    #         return a confirmation of model submission to the user. Model results
    #         will be available at a later time (e.g. from the History page).
    #         """
    #
    #         if request.POST['scenario_selection'] == '0':
    #             """ Custom Run """
    #             # Run SAM - no return expected
    #             jid = model_handler.modelInputPOSTReceiverFortran(request, model)
    #
    #             disclaimer_html = """
    #             <h3>Disclaimer:</h3>
    #             <p>Ecological risk calculations contained here should be used for
    #             no purpose other than quality assurance and peer review of the
    #             presented web applications. This web site is under development.
    #             It is available for the purposes of receiving feedback and quality
    #             assurance from personnel in the EPA Office of Chemical Safety and
    #             Pollution Prevention and from interested members of the ecological
    #             risk assessment community.</p>
    #             """
    #
    #             """ Generate Timestamp HTML from "*_tables" module """
    #             model_output_html = tablesmodule.timestamp()
    #             """ Generate Model input & output tables HTML from "*_tables" module """
    #
    #             try:
    #                 tables_output = tablesmodule.table_all(request, jid)
    #             except:
    #                 tables_output = tablesmodule.table_all(request, "20150402133114784000")
    #             model_output_html = disclaimer_html + model_output_html + tables_output
    #
    #             """ Render output page view HTML """
    #             html = output_page_html(header, model, model_output_html)
    #
    #         else:
    #             """ Pre-Canned Run """
    #             """ Generate Timestamp HTML from "*_tables" module """
    #             model_output_html = tablesmodule.timestamp()
    #             """ Generate Model input & output tables HTML from "*_tables" module """
    #             tables_output = tablesmodule.table_all(request)
    #
    #             model_output_html = model_output_html + tables_output
    #
    #             """ Render output page view HTML """
    #             html = output_page_html(header, model, model_output_html)
    #
    #         response = HttpResponse()
    #         response.write(html)
    #         return response
    #
    #     else:
    #         model_obj = model_handler.modelInputPOSTReceiverFortran(request, model)
    else:

        # TODO: This section should be removed as it is not used anymore...(pre-objectifying method)

        # All models that use the 'model_output.py' to format the inputs before sending to back end server
        # Dynamically import the model output module
        outputmodule = importlib.import_module('.' + model + '_output', 'ubertool_app.models.' + model)
        # Call '*_output' function; function name = 'model'OutputPage  (e.g. 'sipOutputPage')
        outputPageFunc = getattr(outputmodule, model + 'OutputPage')
        model_obj = outputPageFunc(request)

    logging.info(model_obj)

    if type(model_obj) is tuple:
        model_output_html = model_obj[0]
        model_obj = model_obj[1]
    else:
        # Dynamically import the model table module
        tablesmodule = importlib.import_module('.' + model + '_tables', 'ubertool_app.models.' + model)

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

    # TODO: this is only used for non-Pandas models, and is DEPRECATED and should be removed and not called
    def saveToMongoDB(model_obj):
        """
        Method to check if model run is to be saved to MongoDB.  If true,
        the fest_func method to save the model object instance is called
        """

        # Handle Trex, which is not objectified yet; therefore, not saved in MongoDB
        # if model != 'trex':
        if model not in {'terrplant', 'sip', 'stir', 'trex', }:
            logging.info("rest_funcs.save_model_object() called")
            # save_dic() rest_func method saves HTML & model object
            rest_funcs.save_dic(html, model_obj.__dict__, model, "single")

    # TODO: Remove this
    # Call method to save model object to Mongo DB
    # saveToMongoDB(model_obj)
    """ ============================================== """
    """ ============================================== """

    response = HttpResponse()
    response.write(html)
    return response


@require_POST
def output_page(request, model='none', header=''):
    """
    Django HTTP POST handler for output page.  Receives form data and
    validates it.  If valid it calls method to render the output page
    view.  If invalid, it returns the error to the model input page.
    This method maps to: '/ubertool/<model>/output'
    """
    #model_module_location = 'ubertool_app.models.' + model + '.' + model + '_input'
    model_views_location = 'ubertool_app.models.' + model + '.views'
    viewmodule = importlib.import_module(model_views_location)

    header = viewmodule.header

    model_parameters_location = 'ubertool_app.models.' + model + '.' + model + '_parameters'
    model_input_location = 'ubertool_app.models.' + model + '.' + model + '_input'
    parametersmodule = importlib.import_module(model_parameters_location)

    try:
        # Class name must be ModelInp, e.g. SipInp or TerrplantInp
        input_form = getattr(parametersmodule, model.title() + 'Inp')
        form = input_form(request.POST)  # bind user inputs to form object

        # Form validation testing
        if form.is_valid():
            # If form is valid return the output page view
            return output_page_view(request, model, header)

        else:
            # If Form is not valid, redraw Input page (this is the same as 'input.py', expect for 'form_data')
            logging.info(form.errors)
            input_module = importlib.import_module(model_input_location)

            # # Render input page view with POSTed values and show errors
            # html = render_to_string('01uberheader_main_drupal.html', {
            #     'SITE_SKIN': os.environ['SITE_SKIN'],
            #     'TITLE': header})
            # html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
            #     'CONTACT_URL': os.environ['CONTACT_URL'],
            #     'MODEL': model,
            #     'PAGE': 'input'})

            # epa template header
            html = render_to_string('01epa_drupal_header.html', {
                'SITE_SKIN': os.environ['SITE_SKIN'],
                'TITLE': u"\u00FCbertool"
            })
            html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
            html += render_to_string('03epa_drupal_section_title_ubertool.html', {})

            input_page_func = getattr(input_module,
                                      model + '_input_page')  # function name example: 'sip_input_page'
            html += input_page_func(request, model, header,
                                          form_data=request.POST)  # form_data contains the already POSTed form data

            # html += links_left.ordered_list(model, 'run_model')
            # html += render_to_string('06uberfooter.html', {})

            html += render_to_string('07ubertext_end_drupal.html', {})
            html += links_left.ordered_list(model)

            response = HttpResponse()
            response.write(html)
            return response

            # end form validation testing

    except Exception as e:
        logging.exception(e)
        logging.info("E X C E P T")

        return output_page_view(request, model, header)
