import os

import requests
from django.http import HttpResponse
from django.template.loader import render_to_string

rest_server = os.environ['UBERTOOL_REST_SERVER']


def api_docs_view(request):

    html = render_to_string('ubertool_api_index.html', {})
    response = HttpResponse()
    response.write(html)

    return response


def api_docs_json(request):
    # TODO: Change to: /ubertool/api/spec
    api_rest_url = rest_server + '/ubertool/api/spec'
    print(api_rest_url)
    url = api_rest_url
    api_json = requests.get(url)

    response = HttpResponse()
    response.write(api_json.content)

    return response
