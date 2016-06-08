from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
import importlib
import links_left
import os
import secret
from django.conf import settings
from django.shortcuts import redirect


def inputPage(request, model='none', header='none'):

    # If on public server, test user authentication
    if settings.AUTH:
        if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
            if not request.user.is_authenticated():
                return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    viewmodule = importlib.import_module('.views', 'models.'+model)
    inputmodule = importlib.import_module('.'+model+'_input', 'models.'+model)
    header = viewmodule.header

    # import logging

    # if formData != None:
    #     logging.info("===================== N O N E ==========================")
    #     html = render_to_string('01uberheader.html', {'title': header+' Inputs'})
    #     html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'input'})
    #     html = html + ordered_list.ordered_list()

    #     inputPageFunc = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    #     html = html + inputPageFunc(request, model, header, formData)

    #     html = html + render_to_string('06uberfooter.html', {'links': ''})
        
    #     response = HttpResponse()
    #     response.write(html)
    #     return response

    # VALIDATE FORM HERE IF FORM IS POSTED TO THIS VIEW
    # if request.method == "POST":
    #     parametersmodule = importlib.import_module('.'+model+'_parameters', 'models.'+model)
    #     inputForm = getattr(parametersmodule, model.upper() + 'Inp')
        
    #     logging.info(inputForm)
    #     form = inputForm(request.POST)
        
    #     logging.info(form)
        
    #     if form.is_valid():
    #         outputmodule = importlib.import_module('.'+model+'_output', 'models.'+model)
    #         return outputmodule(request)
    #     else:
    #         html = render_to_string('01uberheader.html', {'title': header+' Inputs'})
    #         html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'input'})
    #         html = html + ordered_list.ordered_list()

    #         inputPageFunc = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    #         html = html + inputPageFunc(request, model, header, formData=request.POST)

    #         html = html + render_to_string('06uberfooter.html', {'links': ''})
            
    #         response = HttpResponse()
    #         response.write(html)
    #         return response
    
    # else:
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': header+' Inputs'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'model':model,
            'page':'input'})
    html = html + links_left.ordered_list()

    inputPageFunc = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    html = html + inputPageFunc(request, model, header)

    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response