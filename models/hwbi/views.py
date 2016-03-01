# """
# .. module:: views
#    :synopsis: A useful module indeed.
# """
#
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests


# ################ How model name appears on web page ################
header = 'HWBI'
# ####################################################################
#

def hwbi_view(request):
    html = render_to_string('index.html', {})
    response = HttpResponse()
    response.write(html)

    return response
