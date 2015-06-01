"""
Created on Tue Apr 23 2014

@author: J. Flaishans
"""
from django.template.loader import render_to_string
import requests
from REST import auth_s3
import json
import os, logging

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']

def rest_call(query):
    """ Call to backend server to query DB """
    url = url_part1 + '/ore/load/' + query
    all_dic = {
        'query': query
    }
    data = json.dumps(all_dic)

    response = requests.get(url, data=data, headers=http_headers, timeout=60)

    logging.info(json.loads(response.content)['result'])
    return json.loads(response.content)['result']

def category_query(request):
    """ Fill Exposure Scenario tab inputs based on chosen Crop/Target Category """

    from django.http import HttpResponse

    url = url_part1 + '/ore/category'

    crop_category = request.POST['crop_category']
    print crop_category
    print request.POST

    all_dic = {
        'crop_category': crop_category
    }
    try:
        es_type_filter = request.POST.getlist('es_type_filter[]')
        print es_type_filter
        all_dic['es_type_filter'] = es_type_filter
        es_type = request.POST['es_type']
        print es_type
        all_dic['es_type'] = es_type

    except Exception, e:
        logging.exception(e)
        pass

    data = json.dumps(all_dic)
    print data

    response = requests.post(url, data=data, headers=http_headers, timeout=60)

    # print response.content

    # Return ResponseObject with JSON from DB query (response.content['results'] = worker activities)
    return HttpResponse(
        response.content,
        content_type="application/json"
    )

def output_query(request):

    from django.http import HttpResponse

    url = url_part1 + '/ore/output'
    print request.body

    data = request.body  #  Where Django stores POSTed JSON

    response = requests.post(url, data=data, headers=http_headers, timeout=60)

    html = render_to_string('ore_output.html', {
        'input': {
            'dermal': True,
            'inhal': True,
        },
        'output': {
            'mix_loader': [['Mixing/Loading', 'Corn, Field crop, high-acreage', '100', '220 [SL/No G]', '0.219 [No-R]', '2', '1200', '1.65', '30', '0.00658', '3800']],
            'applicator': [['Applicator', 'Corn, Field crop, high-acreage', '100', '2.06 [EC]', '0.043 [EC]', '2', '1200', '0.0156', '3200', '0.000148', '170000']],
            'flagger': [['Flagger', 'Corn, Field crop, high-acreage', '100', '11 [EC]', '0.35 [No-R]', '2', '350', '0.0241', '2100', '0.00306', '8200']]
        }
    })

    return HttpResponse(
        html,
        # content_type="application/json"
    )
