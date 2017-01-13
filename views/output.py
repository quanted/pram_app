from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import importlib
import links_left
import os
import logging

print('qed.ubertool_app.views.output')

_UPDATED_MODELS = (
    'agdrift',
    'beerex',
    'earthworm',
    'iec',
    'kabam',
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

    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': header})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL'],
        'MODEL': model,
        'PAGE': 'description'})
    html += render_to_string('04uberoutput_start_drupal.html', {
        'TITLE': header + ' Output'})
    html += tables_html
    # if model is not "sam":
    #     print " model: " + model
    #     html += render_to_string('export.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model, 'run_model')
    html += render_to_string('06uberfooter.html', {})

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
        from ubertool_app.models import model_handler
        model_obj = model_handler.modelInputPOSTReceiver(request, model)

    elif model in {'sam'}:
        logging.info('=========== New Model Handler FORTRAN ===========')
        from ubertool_app.models import model_handler

        if model == 'sam':
            """
            SAM takes a long time to run relative to other models; therefore, 
            it will not return model results on form submit, but will instead 
            return a confirmation of model submission to the user. Model results 
            will be available at a later time (e.g. from the History page).
            """

            import ubertool_app.models.sam.sam_tables as tablesmodule

            if request.POST['scenario_selection'] == '0':
                """ Custom Run """
                # Run SAM - no return expected
                jid = model_handler.modelInputPOSTReceiverFortran(request, model)

                disclaimer_html = """
                <h3>Disclaimer:</h3>
                <p>Ecological risk calculations contained here should be used for
                no purpose other than quality assurance and peer review of the
                presented web applications. This web site is under development.
                It is available for the purposes of receiving feedback and quality
                assurance from personnel in the EPA Office of Chemical Safety and
                Pollution Prevention and from interested members of the ecological
                risk assessment community.</p>
                """

                """ Generate Timestamp HTML from "*_tables" module """
                model_output_html = tablesmodule.timestamp()
                """ Generate Model input & output tables HTML from "*_tables" module """

                try:
                    tables_output = tablesmodule.table_all(request, jid)
                except:
                    tables_output = tablesmodule.table_all(request, "20150402133114784000")
                model_output_html = disclaimer_html + model_output_html + tables_output

                """ Render output page view HTML """
                html = output_page_html(header, model, model_output_html)

            else:
                """ Pre-Canned Run """
                """ Generate Timestamp HTML from "*_tables" module """
                model_output_html = tablesmodule.timestamp()
                """ Generate Model input & output tables HTML from "*_tables" module """
                tables_output = tablesmodule.table_all(request)

                model_output_html = model_output_html + tables_output

                """ Render output page view HTML """
                html = output_page_html(header, model, model_output_html)

            response = HttpResponse()
            response.write(html)
            return response

        else:
            model_obj = model_handler.modelInputPOSTReceiverFortran(request, model)

    elif model in {'ore'}:
        """ 
            TEMPORARY FOR ORE TESTING / DEVELOPMENT ON ECO
        """
        import ubertool_app.models.ore.ore_output
        tables_html = ubertool_app.models.ore.ore_output.oreOutputPage(request)

        html = render_to_string('01uberheader.html', {
            'site_skin': os.environ['SITE_SKIN'],
            'title': header + ' Output'})
        html += render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin': os.environ['SITE_SKIN'],
            'model': model,
            'page': 'output'})
        html += links_left.ordered_list()
        html += render_to_string('04uberoutput_start.html', {
            'model_attributes': header + ' Output'})
        html += tables_html
        html += render_to_string('export.html', {})
        html += render_to_string('04uberoutput_end.html', {'model': model})
        html += render_to_string('06uberfooter.html', {'links': ''})

        response = HttpResponse()
        response.write(html)
        return response

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

        from REST import rest_funcs

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

            # Render input page view with POSTed values and show errors
            html = render_to_string('01uberheader_main_drupal.html', {
                'SITE_SKIN': os.environ['SITE_SKIN'],
                'TITLE': header})
            html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
                'CONTACT_URL': os.environ['CONTACT_URL'],
                'MODEL': model,
                'PAGE': 'input'})

            input_page_func = getattr(input_module,
                                      model + '_input_page')  # function name example: 'sip_input_page'
            html += input_page_func(request, model, header,
                                          form_data=request.POST)  # form_data contains the already POSTed form data

            html += links_left.ordered_list(model, 'run_model')
            html += render_to_string('06uberfooter.html', {})

            response = HttpResponse()
            response.write(html)
            return response

            # end form validation testing

    except Exception, e:
        logging.exception(e)
        logging.info("E X C E P T")

        return output_page_view(request, model, header)
