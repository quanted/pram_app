import json
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests


def api_docs_view(request):
    html = render_to_string('index.html', {})
    response = HttpResponse()
    response.write(html)

    return response


def api_docs_json(request):
    url = os.environ['UBERTOOL_REST_SERVER'] + '/api/spec'
    api_json = requests.get(url)

    response = HttpResponse()
    response.write(api_json.content)

    return response
