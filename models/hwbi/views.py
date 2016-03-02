# """
# .. module:: views
#    :synopsis: A useful module indeed.
# """
#
# ################ How model name appears on web page ################
# header = 'HWBI'
# ####################################################################
#
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests


def hwbi_view(request):
    html = render_to_string('index.html', {})
    response = HttpResponse()
    response.write(html)

    return response
