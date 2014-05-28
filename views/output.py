from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

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
    html = html + tablesmodule.table_all(model_obj)
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    rest_funcs.save_dic(html, model_obj.__dict__, model, "single")

    response = HttpResponse()
    response.write(html)
    return response