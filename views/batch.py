from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft
import os
import logging


def batchRun(request, model):
    """
        Sets up and executes model batch run.
        Returns: ModelBatch object
    """
    batchoutputmodule = importlib.import_module('.'+model+'_batchoutput', 'models.'+model)

    batchOutputPageFunc = getattr(batchoutputmodule, model+'BatchOutputPage')  # function name = 'model'BatchOutputPage  (e.g. 'sipBatchOutputPage')

    dataFrame = batchOutputPageFunc(request)
    dataFrame = dataFrame.transpose()

    logging.info(dataFrame)

    # Convert DataFrame to JSON string
    json_inputs = dataFrame.to_json()

    # Add 'run_type' : 'batch' to the JSON string
    json = '{"inputs":' + json_inputs + ',"run_type":"batch"}'

    # logging.info(json)

    # Send JSON to model_handler module
    from models import model_handler
    batch_output = model_handler.call_model_server(model, json)

    ModelList = model_handler.generate_model_object_list(batch_output)

    return ModelList


def batchOutputPage(request, model='none', header='none'):

    viewmodule = importlib.import_module('.views', 'models.'+model)
    
    from REST import rest_funcs
    header = viewmodule.header
    linksleft = linksLeft.linksLeft()

    html = render_to_string('04uberbatch_start.html', {
            'model': model,
            'model_attributes': header+' Batch Output'})

    
    # Temporary logic to handle Pandas verions, else use old way
    if model in {'terrplant', 'sip'}:
        # New way
        modelBatch_obj = batchRun(request, model)

        tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)

        html = html + tablesmodule.timestamp(modelBatch_obj[0])

        batch_output_html = ""
        i = 0
        for model in modelBatch_obj:
           batch_output_html += tablesmodule.table_all(modelBatch_obj[i])
           i += 1

        html = html + batch_output_html
        html = html + render_to_string('export.html', {})
        html = html + render_to_string('04uberoutput_end.html', {})

    elif model == 'przm':
        # PRZM way
        logging.info(batchOutputTuple)
        html = html + ''

    else:
        # Old way
        batchoutputmodule = importlib.import_module('.'+model+'_batchoutput', 'models.'+model)
        batchOutputPageFunc = getattr(batchoutputmodule, model+'BatchOutputPage')  # function name = 'model'BatchOutputPage  (e.g. 'sipBatchOutputPage')
        batchOutputTuple = batchOutputPageFunc(request)

        html = html + batchOutputTuple[0]
        html = html + render_to_string('export.html', {})
        html = html + render_to_string('04uberoutput_end.html', {})

        model_all = batchOutputTuple[1]
        jid_batch = batchOutputTuple[2]
        
        try:
            rest_funcs.batch_save_dic(html, [x.__dict__ for x in model_all], model, 'batch', jid_batch[0], linksleft)
        except:
            pass

    response = HttpResponse()
    response.write(html)
    return response


def batchInputPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header
    
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' Batch'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'batchinput'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberbatchinput.html', {
            'model': model,
            'model_attributes': header+' Batch Run'})
    if model == 'przm':
        html = html + render_to_string('04uberbatchinput_jquery_przm_batch.html', {'model':model, 'header':header})
    else:
        html = html + render_to_string('04uberbatchinput_jquery.html', {'model':model, 'header':header})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response