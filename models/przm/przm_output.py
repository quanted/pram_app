"""
.. module:: przm_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

import logging

@require_POST
def przmOutputPage(request):
    import przm_model
    
    form = request.POST
    logging.info(form)
    
    args={}
    for key in form:
        args[key] = request.POST.get(key)
    args["run_type"] = "single"

    logging.info(args)

    przm_obj = przm_model.przm(args)
    # logger.info(vars(przm_obj))

    return przm_obj