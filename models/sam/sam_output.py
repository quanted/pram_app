"""
.. module:: sam_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def samOutputPage(request):
    import sam_model

    version_terrplant = request.POST.get('version_terrplant')

    # sam_obj = sam_model.sam(True,True,

    # return sam_obj