from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import links_left
import os


def qaqcRun(model):
    """
        Sets up and executes the model QAQC run.
        Returns: ModelQAQC object
    """
    qaqcmodule = importlib.import_module('.'+model+'_qaqc', 'models.'+model)

    #modelQAQC_obj = getattr(qaqcmodule, model+'_obj')      # Calling model object, e.g. 'sip_obj'
    csv_path = os.path.join(os.environ['PROJECT_PATH'], 'models', model, model+'_qaqc.csv')
    modelQAQC_function = getattr(qaqcmodule, model+'Qaqc')
    
    pandas_read_csv = modelQAQC_function(model, csv_path)

    # Read CSV and create an DataFrame for inputs and expected outputs
    pd_obj_inputs = pandas_read_csv[0]
    pd_obj_exp_out = pandas_read_csv[1]
    
    # Rename index column, renumber columns, and transpose the DataFrames
    # pd_obj_inputs.index.name = None
    # pd_obj_inputs.columns = pd_obj_inputs.columns - 1
    # pd_obj_exp_out.index.name = None
    # pd_obj_exp_out.columns = pd_obj_exp_out.columns - 1
    pd_obj_in_out_transpose = pd_obj_inputs.transpose()
    pd_obj_exp_out_transpose = pd_obj_exp_out.transpose()

    # logging.info(pd_obj_inputs)
    # logging.info(pd_obj_exp_out)

    # logging.info(pd_obj_in_out_transpose)
    # logging.info(pd_obj_exp_out_transpose)

    """
        The DataFrame is now in correct format to be converted to JSON, 
        but the dtypes for all columns is 'object' (text) because of 
        the transpose().  When the DataFrame is recreated on the backend 
        the dtypes will be properly inferred from read_json() method.
    """

    # Convert DataFrames to JSON strings
    json_inputs = pd_obj_in_out_transpose.to_json()
    json_exp_out = pd_obj_exp_out_transpose.to_json()
    
    # logging.info(json_inputs)
    # logging.info(json_exp_out)

    # Concatenate JSON strings under keys: "inputs" & "out_exp", respectively, 
    # adding 'run_type' : 'qaqc' to the JSON string
    json = '{"inputs":' + json_inputs + ',"out_exp":' + json_exp_out + ',"run_type":"qaqc"}'

    # logging.info(json)

    # Send JSON to model_handler module
    from models import model_handler
    # return model_handler.ModelQAQC(model, json)
    qaqc_output = model_handler.call_model_server(model, json)

    ModelList = model_handler.generate_model_object_list(qaqc_output)

    return ModelList


def qaqcRunView(request, model='none', runID=''):
    """
        View to render the QAQC output page HTML
    """

    viewmodule = importlib.import_module('.views', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = viewmodule.header

    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' QA/QC'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'qaqc'})
    html = html + links_left.ordered_list()
    html = html + render_to_string('04uberoutput_start.html', {
            'model':model,
            'model_attributes': header+' QAQC'})
    
    # Temporary logic to handle Pandas versions, else use old way
    if model in {'terrplant', 'sip', 'stir', 'trex2', 'therps', 'iec', 'agdrift', 
            'earthworm', 'rice', 'kabam'}:
        import logging
        logging.info('=========== New Model Handler - QAQC Run ===========')
        modelQAQC_obj = qaqcRun(model)

        html = html + tablesmodule.timestamp(modelQAQC_obj[0])

        qaqc_output_html = ""
        i = 0
        for model in modelQAQC_obj:
           qaqc_output_html += tablesmodule.table_all_qaqc(modelQAQC_obj[i])
           i += 1

        html = html + qaqc_output_html

    else:
        try:
            modelQAQC_obj = getattr(qaqcmodule, model+'_obj')      # Calling model object, e.g. 'sip_obj'

            html = html + tablesmodule.timestamp(modelQAQC_obj)
            html = html + tablesmodule.table_all_qaqc(modelQAQC_obj)

        except:
            html += ""
        
    try:
        rest_funcs.save_dic(html, modelQAQC_obj.__dict__, model, 'qaqc')
    except:
        pass
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {'sub_title': ''})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response


def qaqcPage(request, model='none'):
    """
        View to render QAQC page HTML for each model
    """

    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' QA/QC'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'qaqc'})
    html = html + links_left.ordered_list()
    html = html + render_to_string('04uberqaqc_start.html', {
            'model':model,
            'model_attributes': header+' QAQC'})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response