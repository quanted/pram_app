from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

def qaqcPage(request, model='none'):
    viewmodule = importlib.import_module('.'+model+'_qaqc', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = importlib.import_module('.views', 'models.'+model).header

    modelQAQC_obj = getattr(viewmodule, model+'_obj')      # Calling model object, e.g. 'sip_obj'

    html = render_to_string('01uberheader.html', {'title': header+' QA/QC'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'qaqc'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberoutput_start.html', {
            'model':model,
            'model_attributes': header+' QAQC'})
    html = html + tablesmodule.timestamp(modelQAQC_obj)
    html = html + tablesmodule.table_all_qaqc(modelQAQC_obj)
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {'sub_title': ''})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    rest_funcs.save_dic(html, modelQAQC_obj.__dict__, model, 'qaqc')

    response = HttpResponse()
    response.write(html)
    return response