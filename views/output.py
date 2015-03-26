from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import importlib
import linksLeft
import os
import logging

def outputPageHTML(header, model, tables_html):
    """Generates HTML to fill '.articles_output' div on output page"""

    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' Output'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model_attributes': header+' Output'})
    html = html + tables_html
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {'model':model})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    return html

def outputPageView(request, model='none', header=''):
    """
    Django view render method for model output pages.  This method is called 
    by outputPage() method.
    """

    # If model is updated to be generic, use generic Model object
    # if not, use old method with '*_output' module
    if model in {'terrplant', 'sip', 'stir'}:
        logging.info('=========== New Model Handler ===========')
        from models import model_handler
        model_obj = model_handler.modelInputPOSTReceiver(request, model)
    elif model in {'sam'}:
        logging.info('=========== New Model Handler FORTRAN ===========')
        from models import model_handler

        if model == 'sam':
            """
            SAM takes a long time to run relative to other models; therefore, 
            it will not return model results on form submit, but will instead 
            return a confirmation of model submission to the user. Model results 
            will be available at a later time (e.g. from the History page).
            """
            modelOutputHTML = model_handler.modelInputPOSTReceiverFortran(request, model)
            html = outputPageHTML(header, model, modelOutputHTML)

            response = HttpResponse()
            response.write(html)
            return response

        else:
            model_obj = model_handler.modelInputPOSTReceiverFortran(request, model)

    elif model == 'ore':
        import models.ore.ore_output
        model_obj = models.ore.ore_output.oreOutputPage(request)
    else:
        # Dynamically import the model output module
        outputmodule = importlib.import_module('.'+model+'_output', 'models.'+model)
        # Call '*_output' function; function name = 'model'OutputPage  (e.g. 'sipOutputPage')
        outputPageFunc = getattr(outputmodule, model+'OutputPage')
        model_obj = outputPageFunc(request)

    logging.info(model_obj)


    if type(model_obj) is tuple:
        modelOutputHTML = model_obj[0]
        model_obj = model_obj[1]
    else:
        # Dynamically import the model table module
        tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)

        # logging.info(model_obj.__dict__)
        """ Generate Timestamp HTML from "*_tables" module """
        modelOutputHTML = tablesmodule.timestamp(model_obj)
        """ Generate Model input & output tables HTML from "*_tables" module """
        tables_output = tablesmodule.table_all(model_obj)
        
        """ Append Timestamp & model input & output table's HTML """
        if type(tables_output) is tuple:
            modelOutputHTML = modelOutputHTML + tables_output[0]
        elif type(tables_output) is str or type(tables_output) is unicode:
            modelOutputHTML = modelOutputHTML + tables_output
        else:
            modelOutputHTML = "table_all() Returned Wrong Type"

    """ Render output page view HTML """
    html = outputPageHTML(header, model, modelOutputHTML)

    
    """ =============== To be removed =============== """
    """ ========= For Non-Pandas models only ========= """
    """ ============================================== """
    def saveToMongoDB(model_obj):
        """
        Method to check if model run is to be saved to MongoDB.  If true,
        the fest_func meothd to save the model object instance is called
        """

        from REST import rest_funcs

        # Handle Trex, which is not objectified yet; therefore, not saved in MongoDB
        # if model != 'trex':
        if model not in {'terrplant', 'sip', 'stir', 'trex'}:
            logging.info("rest_funcs.save_model_object() called")
            # save_dic() rest_func method saves HTML & model object
            rest_funcs.save_dic(html, model_obj.__dict__, model, "single")

    # Call method to save model object to Mongo DB
    saveToMongoDB(model_obj)
    """ ============================================== """
    """ ============================================== """

    response = HttpResponse()
    response.write(html)
    return response

@require_POST
def outputPage(request, model='none', header=''):
    """
    Django HTTP POST handler for output page.  Receives form data and
    validates it.  If valid it calls method to render the output page
    view.  If invalid, it returns the error to the model input page.
    This method maps to: '/ubertool/<model>/output'
    """

    viewmodule = importlib.import_module('.views', 'models.'+model)

    header = viewmodule.header

    parametersmodule = importlib.import_module('.'+model+'_parameters', 'models.'+model)

    try:
        # Class name must be ModelInp, e.g. SipInp or TerrplantInp
        inputForm = getattr(parametersmodule, model.title() + 'Inp')
        form = inputForm(request.POST) # bind user inputs to form object

        # Form validation testing
        if form.is_valid():
            # If form is valid return the output page view
            return outputPageView(request, model, header)

        else:
            # If not valid...
            logging.info(form.errors)
            inputmodule = importlib.import_module('.'+model+'_input', 'models.'+model)

            # Render input page view with POSTed values and show errors
            html = render_to_string('01uberheader.html', {
                    'site_skin' : os.environ['SITE_SKIN'],
                    'title': header+' Inputs'})
            html = html + render_to_string('02uberintroblock_wmodellinks.html', {
                    'site_skin' : os.environ['SITE_SKIN'],
                    'model':model,
                    'page':'input'})
            html = html + linksLeft.linksLeft()

            inputPageFunc = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
            html = html + inputPageFunc(request, model, header, formData=request.POST)  # formData contains the already POSTed form data

            html = html + render_to_string('06uberfooter.html', {'links': ''})
            
            response = HttpResponse()
            response.write(html)
            return response

        # end form validation testing

    except Exception, e:
        logging.exception(e)
        logging.info("E X C E P T")

        return outputPageView(request, model, header)