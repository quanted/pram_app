"""
.. module:: sam_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def samOutputPage(request):
    import sam_model
    args={}
    for key in request.POST:
        args[key] = request.POST.get(key)
    args["run_type"] = "single"
    sam_obj = sam_model.SAM(args)
    return sam_obj