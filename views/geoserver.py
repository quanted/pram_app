from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import importlib
import requests
import logging
import json
import os


def test_page(request):

    # orv_huc12_json = requests.get(
    #     "http://134.67.114.4/geoserver/rest/workspaces/cite/datastores/huc12s05/featuretypes/huc12s05.json",
    #     auth=('admin', 'geoserver')
    # ).json()
    # logging.info(orv_huc12_json)

    html = render_to_string('geoserver.html', {})

    response = HttpResponse()
    response.write(html)

    return response

@require_POST
def sam_huc_query(request, jid):
    # "20150402133114784000"
    from REST import rest_funcs

    print jid

    geoserver_post_dict = json.loads(request.body)
    huc12_id =  geoserver_post_dict['features'][0]['properties']['huc12']
    print huc12_id
    #                                          jid                  huc12
    sam_out = rest_funcs.get_sam_huc_output(jid, huc12_id)

    # sam_json = json.dumps(sam_out['output'])

    print sam_out
    print type(sam_out)

    try:
        html = render_to_string('geoserver_details.html', {"sam_out": sam_out[0]['model_object_dict']['output']})
    except:
        html = "SAM is still processing the spatial data...please wait..."

    response = HttpResponse()
    response.write(html)

    return response

@require_POST
def sam_done_query(request, jid):

    from REST import rest_funcs
    request = rest_funcs.get_model_object(jid, "sam")

    # print request

    if request == None:
        html = "working"
    else:
        try:
            if request['output'] == '':
                html = "working, first process finished"
            else:
                html = "done"
        except:
            html = "working, first process finished"

    response = HttpResponse()
    response.write(html)

    return response