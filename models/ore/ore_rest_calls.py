"""
Created on Tue Apr 23 2014

@author: J. Flaishans
"""
import ore_xls_writer
from django.template.loader import render_to_string
from django.http import HttpResponse
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

    # logging.info(json.loads(response.content)['result'])
    return json.loads(response.content)['result']

def category_query(request):
    """ Fill Exposure Scenario tab inputs based on chosen Crop/Target Category """

    url = url_part1 + '/ore/category'

    crop_category = request.POST['crop_category']
    # print crop_category
    # print request.POST

    all_dic = {
        'crop_category': crop_category
    }
    try:
        es_type_filter = request.POST.getlist('es_type_filter[]')
        # print es_type_filter
        all_dic['es_type_filter'] = es_type_filter
        es_type = request.POST['es_type']
        # print es_type
        all_dic['es_type'] = es_type

    except Exception, e:
        logging.exception(e)
        pass

    data = json.dumps(all_dic)
    # print data

    response = requests.post(url, data=data, headers=http_headers, timeout=60)
    # print response.content

    # Return ResponseObject with JSON from DB query (response.content['results'] = worker activities)
    return HttpResponse(
        response.content,
        content_type="application/json"
    )

def output_query(request):

    url = url_part1 + '/ore/output'

    data = request.body  #  Where Django stores POSTed JSON

    response = requests.post(url, data=data, headers=http_headers, timeout=60)
    output = json.loads(response.content)

    html = render_to_string('ore_output.html', {
        'input': output['result']['input'],
        'output': output['result']['output']
    })

    return HttpResponse(
        json.dumps( {
            'input': output['result']['input'],
            'output': output['result']['output'],
            'html': html
        } ),
        content_type="application/json"
    )

def output_export(request):
    """

    :param request:
    :return: HttpResponse (type=Application/json)
    """

    from django.http import HttpResponse

    # formatted_data = { 'input': {}, 'output': {} }
    # # print request.POST
    # data = dict(request.POST)
    # # print data.items()
    # for k, v in data.items():
    #     print k, v
    #     k_split = k.split('.')
    #     formatted_data['output'][k_split[0] + k_split[1]] = {}
    #     formatted_data['output'][k_split[0] + k_split[1]][k_split[2]] = v
    #
    # print formatted_data

    data = json.loads(request.body)

    temp_path_name = ore_xls_writer.generate_xlsx(data)

    if temp_path_name is not None:
        # output.seek(0)  # Move to beginning of file

        # content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        # response = HttpResponse(output.read(), content_type='application/vnd.ms-excel')
        # response = HttpResponse(output, content_type='application/vnd.ms-excel')
        # response['Content-Disposition'] = 'attachment; filename="ore.xlsx"'
        # return response
        return HttpResponse(
            json.dumps( {
                'link': temp_path_name,
            } ),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps( {
                'error': 'Error processing request.',
            } ),
            content_type="application/json"
        )


def output_download(request):

    link = request.POST.get('link')

    if link is not None or link != '':

        xlsx_path = os.path.join(os.environ['PROJECT_PATH'], 'models', 'ore', 'static', 'ore', str(link), 'ore.xlsx')
        file_xlsx = open(xlsx_path, "rb")  # open Excel file (read-binary mode)
        response = HttpResponse(
            file_xlsx.read(),
            content_type='application/vnd.ms-excel'
        )
        response['Content-Disposition'] = 'attachment; filename="ore.xlsx"'
        return response

    else:
        return HttpResponse(
            json.dumps( {
                'error': 'Error processing request.',
            } ),
            content_type="application/json"
        )