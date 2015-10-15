"""
.. module:: hwbi_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def hwbiOutputPage(request):
    import hwbi_model

    LC50 = float(request.POST.get('LC50'))
    threshold = float(request.POST.get('threshold'))
    dose_response = float(request.POST.get('dose_response'))
    hwbi_obj = hwbi_model.hwbi(True,True,'single',dose_response, LC50, threshold, None)
    return hwbi_obj
