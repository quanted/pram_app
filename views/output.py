from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft
import inspect
import logging

def outputPage(request, model='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    outputmodule = importlib.import_module('.'+model+'_output', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = viewmodule.header

    outputPageFunc = getattr(outputmodule, model+'OutputPage')      # function name = 'model'OutputPage  (e.g. 'sipOutputPage')
    model_obj = outputPageFunc(request)

    if type(model_obj) is tuple:
        modelOutputHTML = model_obj[0]
        model_obj = model_obj[1]
    else:
        # logging.info(model_obj.__dict__)
        modelOutputHTML = tablesmodule.timestamp(model_obj)
        
        tables_output = tablesmodule.table_all(model_obj)
        
        if type(tables_output) is tuple:
            modelOutputHTML = tables_output[0]
        elif type(tables_output) is str or type(tables_output) is unicode:
            modelOutputHTML = tables_output
        else:
            modelOutputHTML = "table_all() Returned Wrong Type"


    # Render output page view
    html = render_to_string('01uberheader.html', {'title': header+' Output'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model_attributes': header+' Output'})
    html = html + modelOutputHTML
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    rest_funcs.save_dic(html, model_obj.__dict__, model, "single")


    response = HttpResponse()
    response.write(html)
    return response