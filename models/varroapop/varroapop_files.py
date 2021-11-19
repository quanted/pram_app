import importlib
import os

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
import requests

from ... views import links_left

#TODO: Set default value for rest_url when UBERTOOL_REST_SERVER is not set
rest_url = os.getenv('UBERTOOL_REST_SERVER', "")

## Below: proxy views to get session files from the R API

def files_input_view(request, sessionid):
    response = HttpResponse(requests.get(rest_url + '/rest/pram/varroapop/' + sessionid + '/input/'),
                        content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="varroapop_input.txt"'
    return response


def files_log_view(request, sessionid):
    response = HttpResponse(requests.get(rest_url + '/rest/pram/varroapop/' + sessionid + '/log/'),
                        content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="varroapop_log.txt"'
    return response


def files_results_view(request, sessionid):
    response =  HttpResponse(requests.get(rest_url + '/rest/pram/varroapop/' + sessionid + '/results/'),
                        content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="varroapop_results.txt"'
    return response
