from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft
from REST import rest_funcs
import os

def historyPage(request, model='none', header='none'):
    """
    Django view render method for model's history page, showing 
    all of the user's previously saved model runs.
    """

    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' History'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'history'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberalgorithm_start.html', {
            'model_attributes': header+' User History'})
    
    # Conditional template loading
    if model == 'sam':
        html = html + render_to_string('history_query_sam.html', {'model' : model})
    else:
        html = html + render_to_string('history_query.html', {'model' : model})

    # """
    # rest_func method call to return user's model runs for the current model
    # rest_funcs.user_hist('user_id', 'model_name')
    # """
    # hist_obj = rest_funcs.user_hist('admin', model)
    # html = html + table_all(hist_obj)

    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response

def historyPageRevist(request, model='none', header='none'):
    """
    Renders the model output page for the specified previously-saved model run. 
    Queries MongoDB and returns model object formatted by model's 'tables' module
    """
    
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header
    import output

    jid = request.GET.get('jid')
    model_name = request.GET.get('model_name')
    print jid, model_name
    # html = rest_funcs.get_output_html(jid, model_name)


    if model_name == 'sam':
        """ 
        This is all temporary for development testing

        Load output (list of file lines) from Mongo and 
        write them to memory (StringIO) and send to user
        """
        import StringIO, logging

        # Retrieve model's MongoDB entry as Python dictionary
        model_dict = rest_funcs.get_model_object(jid, model_name)
        logging.info(model_dict)

        # Write output string from Mongo to file in memory
        output_str = model_dict['output']
        packet = StringIO.StringIO(output_str) #write to memory

        # html = output.outputPageHTML(header, model, output_tables)

        response = HttpResponse(packet.getvalue(), content_type='application/txt')
        response['Content-Disposition'] = 'attachment; filename=' + model_dict['filename']
        
        return response
    
    else:
        # Retrieve model's MongoDB entry as Python dictionary
        model_dict = rest_funcs.get_model_object(jid, model_name)
        # Recreate Python objext from Python dictionary
        model_obj = recreateModelObject(model_dict)

        # Try to generate HTML from model object instance
        try:
            output_tables = historyOutputTableRedraw(model, model_obj)
            
        # Throw errow and return error message if exception
        except Exception, e:
            import logging
            logging.exception(e)
            output_tables = """
            <br>
            <b>*** Error retrieving model run ***</b>
            """
            
        html = output.outputPageHTML(header, model, output_tables)

        response = HttpResponse()
        response.write(html)
        return response

def recreateModelObject(obj_as_dict):
    """
    Recreates model as Python object from Python dictionary
    """
    class ModelObj(object):
        def __init__(self, obj_as_dict):
            """
            Generic object whose attributes are derived from the 
            Python dictionary passed to the constructor
            """
            if isinstance(obj_as_dict, dict):
                for key, value in obj_as_dict.items():
                    setattr(self, key, value)

    # Return an instance of ModelObj
    return ModelObj(obj_as_dict)

def historyOutputTableRedraw(model, model_obj):
    """
    Redraw model's output page from retrieved MongoDB model object.  
    To allow for model versioning changes, the rendering of the 
    output page's tables are handled in model-specific modules.
    """
    
    try:
        """
        Check if model has 'version_history' module to handle different 
        versions of saved model objects
        """
        # Dynamically import the model's 'history' module
        historymodule = importlib.import_module('.'+model+'_version_history', 'models.'+model)
        """
        'history' module should contain a method called 
        'modelHistoryByVersion()' that returns HTML as string
        """
        modelOutputHTML = historymodule.modelHistoryByVersion(model_obj)

        return modelOutputHTML

    except ImportError, e:
        import logging
        logging.exception(e)
        """
        If no 'version_history' module for model, process model object
        using the model's current output page and 'tables' module
        """

        try:
            """
            Try to import model's 'tables' module and generate HTML tables
            """
            # Dynamically import the model's 'tables' module
            tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
            
            if type(model_obj) is tuple:
                modelOutputHTML = model_obj[0]
                model_obj = model_obj[1]
            else:
                modelOutputHTML = tablesmodule.timestamp(model_obj)
                
                tables_output = tablesmodule.table_all(model_obj)
                
                if type(tables_output) is tuple:
                    modelOutputHTML = modelOutputHTML + tables_output[0]
                elif type(tables_output) is str or type(tables_output) is unicode:
                    modelOutputHTML = modelOutputHTML + tables_output
                else:
                    modelOutputHTML = "table_all() Returned Wrong Type"

            return modelOutputHTML

        except ImportError, e:
            import logging
            logging.exception(e)

            return """
            <br>
            <b>*** Error retrieving model run ***</b>
            """

    except Exception, e:
        """
        Catch any other exceptions and return error message
        """
        import logging
        logging.exception(e)
        return """
                <br>
                <b>*** Error retrieving model run ***</b>
                """


#######################################################################################
########################## Generate History Page Tables ###############################
################################ From AJAX Call #######################################

def historyQueryAjax(request, model):
    """
    rest_func method call to return user's model runs for the current model
    rest_funcs.user_hist('user_id', 'model_name')
    Must return a valid HTML reponse
    """
    
    html = render_to_string('history_pagination.html', {'model' : model})

    """
    rest_func method call to return user's model runs for the current model
    rest_funcs.user_hist('user_id', 'model_name')
    """
    hist_obj = rest_funcs.user_hist('admin', model)
    html = html + table_all(hist_obj)

    response = HttpResponse()
    response.write(html)
    return response

def table_all(user_hist_obj):
    """HTML Table showing list of model runs"""

    table1_out = table_1(user_hist_obj)
    html_all = table1_out
    return html_all

def table_1(user_hist_obj):
    """Generates HTML for table_all()"""

    # #pre-table 1
    html = '''<table>
                <tr><th style="display:none">Model</th><th>Index</th><th>User</th><th>Time</th><th style="display:none">jid</th><th>Run Type</th><th>Link</th><tr><tbody id="itemContainer">
           '''
    for i in range(int(user_hist_obj.total_num)):
        if user_hist_obj.model_name == 'przm' and user_hist_obj.run_type[i]=='batch':
            history_revisit_link = 'history_revisit_batch.html'
        else:
            history_revisit_link = 'history/revisit'

        html = html + '''<form method="get" action=%s target="_blank">'''%(history_revisit_link)
        html = html + '''<tr id="%s"><td style="display:none"><input name="model_name" id="model_name" value=%s type="text"></td>'''%(i+1, user_hist_obj.model_name)
        html = html + "<td>%s</td>"%(i+1)
        html = html + "<td>%s</td>"%(user_hist_obj.user_id[i])
        html = html + "<td>%s</td>"%(user_hist_obj.time_id[i])
        html = html + '''<td style="display:none"><input name="jid" id="jid" value=%s type="text"></td>'''%(user_hist_obj.jid[i])
        try:
            # Geneec does not have 'run_type' key
            html = html + '''<td>%s</td>'''%(user_hist_obj.run_type[i].upper())
        except:
            html = html + '''<td>SINGLE</td>'''
        html = html + '''<td><input type="submit" value="View" class="input_button_%s" ></td></tr>'''%(i+1)
        html = html + "</form>"

    html = html + '''<tr style="display:none"><td id="total_num">%s</td></tr>'''%(user_hist_obj.total_num)
    html = html + '''
            </tbody></table><br>
            <div id="holder_pagination"></div>
        </div>
    '''
    return html