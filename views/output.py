<<<<<<< HEAD
from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

import logging

def outputPage(request, model='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = viewmodule.header

    outputPageFunc = getattr(viewmodule, model+'OutputPage')      # function name = 'model'OutputPage  (e.g. 'sipOutputPage')
    model_obj = outputPageFunc(request)

    html = render_to_string('01uberheader.html', {'title': header+' Output'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model_attributes': header+' Output'})
    html = html + tablesmodule.timestamp(model_obj)
    try: # Check if table_all() returns string
        tables_output = tablesmodule.table_all(model_obj)
    except:
        pass
    try: # Check if table_all() returns tuple
        tables_output = tablesmodule.table_all(model_obj)[0]
    except TypeError: # Pass error to output page if fails
        tables_output = "table_all() Returned Wrong Type"
    html = html + tables_output
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    rest_funcs.save_dic(html, model_obj.__dict__, model, "single")

    response = HttpResponse()
    response.write(html)
    return response
=======
from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

import logging

def outputPage(request, model='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = viewmodule.header

    outputPageFunc = getattr(viewmodule, model+'OutputPage')      # function name = 'model'OutputPage  (e.g. 'sipOutputPage')
    model_obj = outputPageFunc(request)

    html = render_to_string('01uberheader.html', {'title': header+' Output'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'output'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model_attributes': header+' Output'})
    html = html + tablesmodule.timestamp(model_obj)
    try: # Check if table_all() returns string
        tables_output = tablesmodule.table_all(model_obj)
        html = html + tables_output
    except TypeError:
        try: # Check if table_all() returns tuple
            tables_output = tablesmodule.table_all(model_obj)[0]
            html = html + tables_output
        except TypeError: # Pass error to output page if fails
            tables_output = "table_all() Returned Wrong Type"
            html = html + tables_output
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    rest_funcs.save_dic(html, model_obj.__dict__, model, "single")

    response = HttpResponse()
    response.write(html)
    return response
>>>>>>> 437fa59a5ce1a032aea8a6cfbf450b5c7ce904b3
