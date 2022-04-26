"""
Django routing functions to Flask
"""

import requests
import os
from django.http import Http404, HttpResponse


def flask_proxy(request, flask_url):
    if os.environ["IN_DOCKER"] == "True":
        proxy_url = os.environ.get('UBERTOOL_REST_SERVER') + "/rest/" + flask_url
    else:
        proxy_url = "http://localhost:7777" + "/rest/" + flask_url
    method = str(request.method)
    print("Django to Flask proxy method: " + method + " url: " + proxy_url)
    if method == "POST":
        flask_request = requests.request("post", proxy_url, data=request.POST)
        content_disposition = flask_request.headers["Content-Disposition"]
        response =  HttpResponse(flask_request, content_type = flask_request.headers["Content-Type"],
                                headers={'Content-Disposition': content_disposition)
        return response
    elif method == "GET":
        flask_request = requests.request("get", proxy_url)
        content_disposition = flask_request.headers["Content-Disposition"]
        response =  HttpResponse(flask_request, content_type = flask_request.headers["Content-Type"],
                                headers={'Content-Disposition': content_disposition)
        return response
    else:
        print("Django to Flask proxy url invalid.")
        raise Http404
