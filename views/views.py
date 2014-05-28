from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
from collections import OrderedDict
import os
import logging


##################################################################################
############################## Model Page Views ##################################
##################################################################################

def descriptionPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    text_file2 = open('models/'+model+'/'+model+'_text.txt','r')
    xx = text_file2.read()
    html = render_to_string('01uberheader.html', {'title': header+' Description'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'description'})
    html = html + linksLeft()
    html = html + render_to_string('04ubertext_start.html', {
            'model_attributes': header+' Overview',
            'text_paragraph':xx})
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''}) 
    
    response = HttpResponse()
    response.write(html)
    return response

def algorithmPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    text_file1 = open('models/'+model+'/'+model+'_algorithm.txt','r')
    x = text_file1.read()
    html = render_to_string('01uberheader.html', {'title': header+' Algorithms'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'algorithm'})
    html = html + linksLeft()
    html = html + render_to_string('04uberalgorithm_start.html', {
            'model_attributes': header+' Algorithms', 
            'text_paragraph':x})
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response

def referencesPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    text_file1 = open('models/'+model+'/'+model+'_references.txt','r')
    x = text_file1.read()
    html = render_to_string('01uberheader.html', {'title': header+' References'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'references'})
    html = html + linksLeft()
    html = html + render_to_string('04uberreferences_start.html', {
            'model_attributes': header+' References', 
            'text_paragraph':x})
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response

def inputPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    html = render_to_string('01uberheader.html', {'title': header+' Inputs'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'input'})
    html = html + linksLeft()

    inputPageFunc = getattr(viewmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    html = html + inputPageFunc(request, model)

    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response

def outputPage(request, model='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = viewmodule.header

    outputPageFunc = getattr(viewmodule, model+'OutputPage')      # function name = 'model'OutputPage  (e.g. 'sipOutputPage')
    model_obj = outputPageFunc(request)

    html = render_to_string('01uberheader.html', {'title': header+' Output'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'output'})
    html = html + linksLeft()
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

def qaqcPage(request, model='none'):
    viewmodule = importlib.import_module('.'+model+'_qaqc', 'models.'+model)
    tablesmodule = importlib.import_module('.'+model+'_tables', 'models.'+model)
    from REST import rest_funcs
    header = importlib.import_module('.views', 'models.'+model).header

    modelQAQC_obj = getattr(viewmodule, model+'_obj')      # Calling model object, e.g. 'sip_obj'

    html = render_to_string('01uberheader.html', {'title': header+' QA/QC'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'qaqc'})
    html = html + linksLeft()
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

def batchInputPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header
    
    html = render_to_string('01uberheader.html', {'title': header+' Batch'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'batchinput'})
    html = html + linksLeft()
    html = html + render_to_string('04uberbatchinput.html', {
            'model': model,
            'model_attributes': header+' Batch Run'})
    html = html + render_to_string('04uberbatchinput_jquery.html', {'model':model, 'header':header})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response

def batchOutputPage(request, model='none', header='none'):
    importlib.import_module('.'+model+'_model', 'models.'+model)
    viewmodule = importlib.import_module('.'+model+'_batchoutput', 'models.'+model)
    from REST import rest_funcs
    header = importlib.import_module('.views', 'models.'+model).header
    linksleft = linksLeft()

    html = render_to_string('04uberbatch_start.html', {
            'model': model,
            'model_attributes': header+' Batch Output'})

    batchOutputPageFunc = getattr(viewmodule, model+'BatchOutputPage')  # function name = 'model'BatchOutputPage  (e.g. 'sipBatchOutputPage')
    batchOutputTuple = batchOutputPageFunc(request)
    html = html + batchOutputTuple[0]
    html = html + render_to_string('export.html', {})
    html = html + render_to_string('04uberoutput_end.html', {})

    model_all = batchOutputTuple[1]
    jid_batch = batchOutputTuple[2]
    rest_funcs.batch_save_dic(html, [x.__dict__ for x in model_all], model, 'batch', jid_batch[0], linksleft)

    response = HttpResponse()
    response.write(html)
    return response

def historyPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header
    from history import history_tables
    from REST import rest_funcs

    html = render_to_string('01uberheader.html', {'title': header+' History'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'history'})
    html = html + linksLeft()
    html = html + render_to_string('04uberalgorithm_start.html', {
            'model_attributes': header+' User History'})
    html = html + render_to_string('history_pagination.html', {})   

    hist_obj = rest_funcs.user_hist('admin', model)
    html = html + history_tables.table_all(hist_obj)

    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)
    return response

def historyPageRevist(request):
    from REST import rest_funcs

    jid = request.GET.get('jid')
    model_name = request.GET.get('model_name')
    print jid, model_name
    html = rest_funcs.get_output_html(jid, model_name)

    response = HttpResponse()
    response.write(html)
    return response

#######################################################################################
############################## Page Segments (01-06) ##################################
#######################################################################################

# 03ubertext_links_left:
def linksLeft():
    link_dict = OrderedDict([
        ('Terrestrial Models', OrderedDict([
                ('TerrPlant', 'terrplant'),
                ('SIP', 'sip'),
                ('STIR', 'stir'),
                ('DUST', 'dust'),
                ('T-Rex', 'trex2'),
                ('T-Herps', 'therps'),
                ('IEC', 'iec'),
                ('AgDrift', 'agdrift'),
                ('Agdrift-T-Rex', 'agdrift_trex'),
                ('Agdrift-T-Herps', 'agdrift_therps'),
                ('Earthworm', 'earthworm'),
            ])
        ),
        ('Aquatic Models', OrderedDict([
                ('RICE', 'rice'),
                ('GENEEC', 'geneec'),
                ('Kabam', 'kabam'),
                ('PRZM', 'przm'),
                ('PRZM 5', 'przm5'),
                ('EXAMS', 'exams'),
                ('PFAM', 'pfam'),
                ('PRZM-EXAMS', 'przm_exams'),
                ('VVWM', 'vvwm'),
                ('Surface Water Calculator', 'swc'),
            ])
        ),
        ('&uuml;bertool', OrderedDict([
                ('Chemical Selection', 'select_chemical'),
                ('Use/Label/Site Data', 'site_data'),
                ('Pesticide Properties', 'pesticide_properties'),
                ('Exposure Concentrations', 'exposure_concentrations'),
                ('Aquatic Toxicity', 'aquatic_toxicity'),
                ('Terrestrial Toxicity', 'terrestrial_toxicity'),
                ('Ecosystem Inputs', 'ecosystem_inputs'),
                ('Run &uuml;bertool', 'run_ubertool'),
                ('Saved Runs', 'user'),
            ])
        ),
        ('Coming Soon', OrderedDict([
                ('Downstream Dilution Model', 'ddm'),
                ('SuperPRZM', 'superprzm'),
                ('SAM', 'sam'),
            ])
        ),
    ])

    html = render_to_string('03ubertext_links_left.html', {'link_dict': link_dict})
    return html


#######################################################################################
################################## Landing Pages ######################################
#######################################################################################

def ecoLandingPage(request):
    text_file2 = open('views/main_text.txt','r')
    xx = text_file2.read()

    html = render_to_string('01uberheader_main.html', {})
    html = html + render_to_string('02uberintroblock_nomodellinks.html', {})
    html = html + linksLeft()
    html = html + render_to_string('04ubertext_start_index.html', {
            'text_paragraph':xx
            })
    html = html + render_to_string('04ubertext_end.html',{})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response

def ubertoolLandingPage(request):
    html = render_to_string('00landing_page.html', {'title':'Ubertool'})

    response = HttpResponse()
    response.write(html)

    return response

#######################################################################################
################################ HTTP Error Pages #####################################
#######################################################################################

def fileNotFound(request):
    html = render_to_string('01uberheader.html', {'title': 'Error'})
    html = html + render_to_string('02uberintroblock_nomodellinks.html', {'title2':'File not found'})
    html = html + linksLeft()
    html = html + render_to_string('04ubertext_start.html', {
            'model_attributes': 'File Not Found',
            'text_paragraph': ""})
    html = html + """ <img src="/static/images/404error.png" width="300" height="300">"""
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response