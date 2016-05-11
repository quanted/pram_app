import os
import json
from django.http import HttpResponse
import auth_s3
import requests
import numpy as np
import ast
import logging
import datetime
import pytz
import warnings


# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
rest_url = os.environ['UBERTOOL_REST_SERVER']
rest_url_hwbi = os.environ['REST_SERVER_8']


class NumPyArrangeEncoder(json.JSONEncoder):
    """Helper class to convert dictionary to JSON when it contains a NumPy object"""
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()  # or map(int, obj)
        return json.JSONEncoder.default(self, obj)


class NumPyDecoder(json.JSONDecoder):
    def default(self, obj):
        if isinstance(obj, list):
            return np.array(obj)
        return json.JSONDecoder.default(self, obj)


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def gen_jid():
    """A function to generate JID"""
    ts = datetime.datetime.now(pytz.UTC)
    local_datetime = ts.astimezone(pytz.timezone('America/New_York'))
    jid = local_datetime.strftime('%Y%m%d%H%M%S%f')
    return jid


def django_error_json():
    return HttpResponse("{'error': 'Unused HTTP method'}", content_type="application/json")


def rest_proxy(request, model, jid=None):

    method = request.method

    if method == 'GET':
        response = rest_proxy_get(model)
    elif method == 'POST':
        try:
            data = json.loads(request.body)
        except TypeError:
            return django_error_json()
        response = rest_proxy_post(model, data, jid)
    else:
        return django_error_json()

    return HttpResponse(
        json.dumps(response.json()),
        content_type="application/json"
    )


def rest_proxy_post(model, data, jid):
    return requests.post(rest_url + '/rest/ubertool/' + model + '/' + jid, json=data, headers=http_headers, timeout=60)


def rest_proxy_get(model):
    return requests.get(rest_url + '/rest/ubertool/' + model)


def rest_proxy_hwbi(request, resource):
    response = requests.get(rest_url_hwbi + '/hwbi/rest/hwbi/locations/' + resource)
    return HttpResponse(json.dumps(response.json()), content_type="application/json")


def rest_proxy_hwbi_calc(request):

    method = request.method

    if method == 'GET':
        response = requests.get(rest_url_hwbi + '/hwbi/rest/hwbi/calc')
        return HttpResponse(response)
    elif method == 'POST':
        data = json.loads(request.body)
        response = requests.post(rest_url_hwbi + '/hwbi/rest/hwbi/calc', json=data)
        return HttpResponse(json.dumps(response.json()), content_type="application/json")


def save_dic(output_html, model_object_dict, model_name, run_type):
    """
    DEPRECATED: Use save_model_object(model_object_dict, model_name, run_type) instead
    :param output_html:
    :param model_object_dict:
    :param model_name:
    :param run_type:
    """
    warnings.warn("DEPRECATED: Use save_model_object(model_object_dict, model_name, run_type) instead",
                  DeprecationWarning)

    all_dic = {"model_name": model_name, "_id": model_object_dict['jid'], "run_type": run_type,
               "output_html": output_html, "model_object_dict": model_object_dict}
    data = json.dumps(all_dic, cls=NumPyArrangeEncoder)
    url = rest_url + '/save_history_html'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
    except:
        pass


def save_model_object(model_object_dict, model_name, run_type):
    """

    :param model_object_dict:
    :param model_name:
    :param run_type:
    """
    logging.info("save_model_object() called")

    all_dic = {"model_name": model_name, "_id": model_object_dict['jid'], "run_type": run_type}
    data = json.dumps(all_dic)
    url = rest_url + '/save_history'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
    except:
        pass


def batch_save_dic(output_html, model_object_dict, model_name, run_type, jid_batch, linksleft=''):
    """

    :param output_html:
    :param model_object_dict:
    :param model_name:
    :param run_type:
    :param jid_batch:
    :param linksleft:
    """
    from django.template.loader import render_to_string

    html_save = render_to_string('01uberheader.html', {
        'site_skin': os.environ['SITE_SKIN'],
        'title': 'Batch History'})
    html_save = html_save + render_to_string('02uberintroblock_wmodellinks.html', {
        'site_skin': os.environ['SITE_SKIN'],
        'model': model_name,
        'page': 'batchinput'})
    html_save = html_save + linksleft
    html_save = html_save + output_html
    html_save = html_save + render_to_string('06uberfooter.html', {'links': ''})

    all_dic = {"model_name": model_name, "_id": jid_batch, "run_type": run_type, "output_html": html_save,
               "model_object_dict": model_object_dict}
    data = json.dumps(all_dic, cls=NumPyArrangeEncoder)
    url = rest_url + '/save_history'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
    except:
        pass


def update_html(output_html, jid, model_name):
    """
    DEPRECATED: no replacement method as model's output page as HTML is no longer being stored in MongoDB
    :param output_html:
    :param jid:
    :param model_name:
    """
    warnings.warn(
        "DEPRECATED: no replacement method as model's output page as HTML is no longer being stored in MongoDB",
        DeprecationWarning)

    all_dic = {"model_name": model_name, "_id": jid, "output_html": output_html}
    data = json.dumps(all_dic)
    url = rest_url + '/update_html'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
    except:
        pass


def get_output_html(jid, model_name):
    """
    DEPRECATED: Use get_model_object(jid, model_name) instead

    function to retrieve html from MongoDB
    :param jid:
    :param model_name:
    :return:
    """
    warnings.warn("DEPRECATED: Use get_model_object(jid, model_name) instead", DeprecationWarning)

    all_dic = {"jid": jid, "model_name": model_name}
    data = json.dumps(all_dic)
    url = rest_url + '/get_html_output'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        if response:
            html_output = json.loads(response.content)['html_output']
        else:
            html_output = ""
    except:
        return "error"

    return html_output


def get_model_object(jid, model_name):
    """Retrieves JSON from MongoDB representing model (Python) object and returns it as Python dictionary
    :param jid:
    :param model_name:
    :return:
    """
    all_dic = {"jid": jid, "model_name": model_name}
    data = json.dumps(all_dic)
    url = rest_url + '/get_model_object'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        if response:
            model_object = json.loads(response.content)['model_object']
        else:
            model_object = ""

    except:
        return {"error": "error"}

    return model_object


def get_sam_huc_output(jid, huc12):
    """Retrieves JSON from MongoDB representing model (Python) object and returns it as Python dictionary
    :param jid:
    :param huc12:
    :return:
    """
    all_dic = {"jid": jid, "model_name": "sam", "huc12": huc12}
    data = json.dumps(all_dic)
    url = rest_url + '/get_sam_huc_output'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        if response:
            model_object = json.loads(response.content)['huc12_output']
        else:
            model_object = ""

    except:
        logging.exception(Exception)
        return "error"

    return model_object


def create_batchoutput_html(jid, model_name):
    """

    :param jid:
    :param model_name:
    :return:
    """
    all_dic = {"jid": jid, "model_name": model_name}
    data = json.dumps(all_dic)
    url = rest_url + '/get_przm_batch_output'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        if response:
            result = response.content
            result_dict = ast.literal_eval(result)['result']
            result_obj_all = []
            for i in result_dict:
                result_obj_temp = Struct(**i)
                result_obj_all.append(result_obj_temp)
        else:
            result_obj_all = []

    except:
        return "error"

    return result_obj_all


class UserHistory(object):
    def __init__(self, user_id, model_name):
        """
        Create an object to display history runs
        :param user_id:
        :param model_name:
        """
        import datetime
        self.user_id = user_id
        self.model_name = model_name
        self.all_dic = {"user_id": user_id, "model_name": model_name}
        self.data = json.dumps(self.all_dic)
        self.url = rest_url + '/user_history'
        self.user_id = []
        self.time_id = []
        self.jid = []
        self.run_type = []
        self.model_name = model_name

        try:
            self.response = requests.post(self.url, data=self.data, headers=http_headers, timeout=60)
        except:
            self.response = None

        # logging.info(self.response.content)

        if self.response:
            self.output_val = json.loads(self.response.content)['hist_all']
            self.total_num = len(self.output_val)
            # print self.output_val
            for element in self.output_val:

                try:
                    # Catch if any erroneous DB entries exist and ignore them

                    self.user_id.append(element['user_id'])

                    if model_name == 'sam':  # SAM changed "_id" to "jid" Mongo key
                        self.jid.append(element['jid'])
                        self.time_id.append(
                            datetime.datetime.strptime(element['jid'], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        self.jid.append(element['_id'])
                        self.time_id.append(
                            datetime.datetime.strptime(element['_id'], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%d %H:%M:%S'))

                    # Gennec doesn't have 'run_type' key
                    self.run_type.append(element['run_type'])

                except:
                    # Subtract erroneous entry from total number of entries
                    self.total_num -= 1

        else:
            self.total_num = 0
