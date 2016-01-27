import os
import json
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
url_part1 = os.environ['UBERTOOL_REST_SERVER']


###########################A class helps dictionary to be converted to JSON when it contains numpy element################################ 
class NumPyArangeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist() # or map(int, obj)
        return json.JSONEncoder.default(self, obj)

class NumPyDecoder(json.JSONDecoder):
    def default(self, obj):
        if isinstance(obj, list):
            return np.array(obj)
        return json.JSONDecoder.default(self, obj)
        
class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)


###########################A function to generate JID################################ 
def gen_jid():
    ts = datetime.datetime.now(pytz.UTC)
    #localDatetime = ts.astimezone(pytz.timezone('US/Eastern'))
    localDatetime = ts.astimezone(pytz.timezone('America/New_York'))
    jid = localDatetime.strftime('%Y%m%d%H%M%S%f')
    return jid

###########################function to save a single run to MongoDB################################ 
def save_dic(output_html, model_object_dict, model_name, run_type):
    """
    DEPRECATED: Use save_model_object(model_object_dict, model_name, run_type) instead
    """
    warnings.warn("DEPRECATED: Use save_model_object(model_object_dict, model_name, run_type) instead", DeprecationWarning)

    all_dic = {"model_name": model_name, "_id": model_object_dict['jid'], "run_type": run_type, "output_html": output_html, "model_object_dict": model_object_dict}
    data = json.dumps(all_dic, cls=NumPyArangeEncoder)
    url = url_part1 + '/save_history_html'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)
        response = requests.post(url, data=data, headers=http_headers, timeout=60)   
    except:
        pass

###########################function to save a single run to MongoDB################################ 
def save_model_object(model_object_dict, model_name, run_type):

    logging.info("save_model_object() called")

    all_dic = {"model_name":model_name, "_id":model_object_dict['jid'], "run_type":run_type}
    data = json.dumps(all_dic)
    url = url_part1 + '/save_history'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)   
    except:
        pass

###########################function to save batch runs to MongoDB################################ 
def batch_save_dic(output_html, model_object_dict, model_name, run_type, jid_batch, linksleft=''):
    from django.template.loader import render_to_string
    
    html_save = render_to_string('01uberheader.html', {
                'site_skin' : os.environ['SITE_SKIN'],
                'title': 'Batch History'})
    html_save = html_save + render_to_string('02uberintroblock_wmodellinks.html', {
                'site_skin' : os.environ['SITE_SKIN'],
                'model':model_name,
                'page':'batchinput'})
    html_save = html_save + linksleft
    html_save = html_save + output_html
    html_save = html_save + render_to_string('06uberfooter.html', {'links': ''})
    
    all_dic = {"model_name":model_name, "_id":jid_batch, "run_type":run_type, "output_html":html_save, "model_object_dict":model_object_dict}
    data = json.dumps(all_dic, cls=NumPyArangeEncoder)
    url = url_part1 + '/save_history'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)   
    except:
        pass
###########################function to update html saved in MongoDB################################ 
def update_html(output_html, jid, model_name):
    """
    DEPRECATED: no replacement method as model's output page as HTML is no longer being stored in MongoDB
    """
    warnings.warn("DEPRECATED: no replacement method as model's output page as HTML is no longer being stored in MongoDB", DeprecationWarning)

    all_dic = {"model_name":model_name, "_id":jid, "output_html":output_html}
    data = json.dumps(all_dic)
    url = url_part1 + '/update_html'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)   
    except:
        pass
###########################function to retrieve html from MongoDB################################

def get_output_html(jid, model_name):
    """
    DEPRECATED: Use get_model_object(jid, model_name) instead
    """
    warnings.warn("DEPRECATED: Use get_model_object(jid, model_name) instead", DeprecationWarning)

    all_dic = {"jid":jid, "model_name":model_name}
    data = json.dumps(all_dic)
    url = url_part1 + '/get_html_output'
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

###########################function to retrieve model object from MongoDB################################
def get_model_object(jid, model_name):
    """Retrieves JSON from MongoDB representing model (Python) object and returns it as Python dictionary"""
    all_dic = {"jid": jid, "model_name": model_name}
    data = json.dumps(all_dic)
    url = url_part1 + '/get_model_object'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)   
        if response:
            model_object = json.loads(response.content)['model_object']
        else:
            model_object = ""

    except:
        return { "error": "error" }

    return model_object

###########################function to retrieve model object from MongoDB################################
def get_sam_huc_output(jid, huc12):
    """Retrieves JSON from MongoDB representing model (Python) object and returns it as Python dictionary"""
    all_dic = {"jid": jid, "model_name": "sam", "huc12": huc12}
    data = json.dumps(all_dic)
    url = url_part1 + '/get_sam_huc_output'
    try:
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        if response:
            model_object = json.loads(response.content)['huc12_output']
        else:
            model_object =""

    except:
        logging.exception(Exception)
        return "error"

    return model_object

###########################function to retrieve html from MongoDB################################
def create_batchoutput_html(jid, model_name):
    all_dic = {"jid":jid, "model_name":model_name}
    data = json.dumps(all_dic)
    url = url_part1 + '/get_przm_batch_output'
    try:
        # response = urlfetch.fetch(url=url, payload=data, method=urlfetch.POST, headers=http_headers, deadline=60)   
        response = requests.post(url, data=data, headers=http_headers, timeout=60)   
        if response:
            result = response.content
            result_dict = ast.literal_eval(result)['result']
            result_obj_all = []
            for i in result_dict:
                result_obj_temp = Struct(**i)
                result_obj_all.append(result_obj_temp)
        else:
            result_obj_all =[]

    except:
        return "error"

    return result_obj_all

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)


###########################################################



###########################################################

###########################creat an object to display history runs################################ 
class user_hist(object):
    def __init__(self, user_id, model_name):
        import datetime
        self.user_id = user_id
        self.model_name = model_name
    ########call the function################# 
        self.all_dic = {"user_id": user_id, "model_name":model_name}
        self.data = json.dumps(self.all_dic)
        self.url = url_part1 + '/user_history'
        self.user_id = []
        self.time_id = []
        self.jid = []
        self.run_type = []
        self.model_name = model_name

        try:
            # self.response = urlfetch.fetch(url=self.url, payload=self.data, method=urlfetch.POST, headers=http_headers, deadline=60)
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
                        self.time_id.append(datetime.datetime.strptime(element['jid'], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        self.jid.append(element['_id'])
                        self.time_id.append(datetime.datetime.strptime(element['_id'], '%Y%m%d%H%M%S%f').strftime('%Y-%m-%d %H:%M:%S'))
                    
                    # Gennec doesn't have 'run_type' key
                    self.run_type.append(element['run_type'])

                except:
                    # Subtract erroneous entry from total number of entries
                    self.total_num = self.total_num - 1
                    
        else:
            self.total_num = 0

