"""
.. module:: rice_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def riceOutputPage(request):
    """ Handles rice output parameters.

    Longer description.

    :param request: asdf.
    :type request: str.
    :param model: asdf.
    :type model: str.
    :param header: asdf.
    :type header: str.
    :returns: html code.
    :raises: errors.
    """
    
    import rice_model

    version_rice = request.POST.get('version_rice')
    chemical_name = request.POST.get('chemical_name')
    mai = request.POST.get('mai')
    dsed = request.POST.get('dsed')
    a = request.POST.get('area')
    pb = request.POST.get('pb')
    dw = request.POST.get('dw')
    osed = request.POST.get('osed')
    kd = request.POST.get('Kd')

    rice_obj = rice_model.rice(True,True,version_rice,'single',chemical_name, mai, dsed, 
        a, pb, dw, osed, kd)

    import logging
    logging.info(rice_obj)
    return rice_obj
