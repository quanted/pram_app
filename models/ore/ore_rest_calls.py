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
    output = json.loads(response.content)

    # html = render_to_string('ore_output.html', {
    #     'output': {
    #         'mix_loader': {
    #             'activity': "Mixing/Loading",
    #             'app_equip': 'Aerial',
    #             'crop_target': "Corn[field crop, high acreage]",
    #             'loc_dermal': '100',
    #             'loc_inhal': '100',
    #             'app_rate': '2',
    #             'app_rate_unit': 'lb ai/A',
    #             'area_treated': '1200',
    #             'area_treated_unit': 'acre',
    #             'dermal_unit_exp': ['220 [SL/No G]', '37.6 [SL/G]'],
    #             'inhal_unit_exp': ['0.219 [No-R]', '0.219 [No-R]'],
    #             'dermal_dose': ['1.65', '0.282'],
    #             'dermal_moe': ['30', '180'],
    #             'inhal_dose': ['0.00658', '0.00658'],
    #             'inhal_moe': ['3800', '3800']
    #         },
    #         'applicator': {
    #             'activity': "Aerial Application",
    #             'app_equip': 'Aerial',
    #             'crop_target': "Corn[field crop, high acreage]",
    #             'loc_dermal': '100',
    #             'loc_inhal': '100',
    #             'app_rate': '2',
    #             'app_rate_unit': 'lb ai/A',
    #             'area_treated': '1200',
    #             'area_treated_unit': 'acre',
    #             'dermal_unit_exp': ['2.06 [EC]'],
    #             'inhal_unit_exp': ['0.043 [EC]'],
    #             'dermal_dose': ['0.0156'],
    #             'dermal_moe': ['3200'],
    #             'inhal_dose': ['0.000148'],
    #             'inhal_moe': ['170000']
    #         },
    #         'flagger': {
    #             'activity': "Flagging for Aerial Applications",
    #             'app_equip': 'Aerial',
    #             'crop_target': "Corn[field crop, high acreage]",
    #             'loc_dermal': '100',
    #             'loc_inhal': '100',
    #             'app_rate': '2',
    #             'app_rate_unit': 'lb ai/A',
    #             'area_treated': '350',
    #             'area_treated_unit': 'acre',
    #             'dermal_unit_exp': ['11 [EC]'],
    #             'inhal_unit_exp': ['0.35 [No-R]'],
    #             'dermal_dose': ['0.0156'],
    #             'dermal_moe': ['3200'],
    #             'inhal_dose': ['0.000148'],
    #             'inhal_moe': ['170000']
    #         }
    #     }
    # })

    html = render_to_string('ore_output.html', {
        'output': output['result']
    })

    return HttpResponse(
        html,
        # content_type="application/json"
    )
