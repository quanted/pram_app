"""
.. module:: iec_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def iecOutputPage(request):
    import iec_model

    lc50 = float(request.POST.get('lc50'))
    threshold = float(request.POST.get('threshold'))
    dose_response = float(request.POST.get('dose_response'))
    iec_obj = iec_model.iec(True,True,'single',dose_response, lc50, threshold, None)
    return iec_obj
