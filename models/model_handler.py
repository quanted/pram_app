"""
.. module:: model_handler
   :synopsis: The model_handler module prepares the model inputs 
   to be sent to the backend model server as well as creating a 
   Model object consisting of the inputs, outputs, and other 
   model-specific attributes such as 'run_type' and 'user' who 
   ran the model.  This generic Model object is the communication 
   backbone between the frontend and backend / model server.  If 
   a model requires specific treatment for frontend-backend 
   communication, this module can be bypassed by creating a 
   "*_model" module in the model's module directory.
"""

from ubertool_app.REST import auth_s3, rest_funcs
import os
import json
import re
import logging


# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


class Model(object):
    def __init__(self, run_type, jid, pd_obj_in, pd_obj_out):
        """
        Generic Python 'Model' object created from two Pandas
        DataFrame objects, one for inputs and one for outputs.
        """

        self.pd_obj_in = pd_obj_in
        self.pd_obj_out = pd_obj_out
        self.jid = jid
        self.run_type = run_type

        # Set object attributes to model inputs and outputs
        """
        Set each column of the DataFrames as object attribute with
        a value equal to the first row's value
        """
        for col in self.pd_obj_in:
            setattr(self, self.pd_obj_in[col].name, self.pd_obj_in[col].iloc[0])
        for col in self.pd_obj_out:
            setattr(self, self.pd_obj_out[col].name, self.pd_obj_out[col].iloc[0])


class ModelFortran(object):
    def __init__(self, run_type, jid, inputs, outputs):
        """
            Generic Python 'Model' object created from two Pandas 
            DataFrame objects, one for inputs and one for outputs.
        """

        self.inputs = inputs
        self.outputs = outputs
        self.jid = jid
        self.run_type = run_type

        # Set object attributes to model inputs and outputs
        """
            Set inputs and outputs as model object attributes
        """
        for k, v in self.inputs:
            setattr(self, k, v)
        for k, v in self.outputs:
            setattr(self, k, v)


def call_model_server(model, args):
    """
        Sends model input parameters (args) to model 
        backend server and returns the 'response'.  
        'args' can be type == 'dict' or 'string' (valid 
        JSON string).
    """

    # If 'args' is a Python dictionary, dump it to a JSON string
    if type(args) == dict:
        data = json.dumps(args)
    else:
        data = args

    # POST JSON to model server through rest proxy
    response = rest_funcs.rest_proxy_post(model, data, rest_funcs.gen_jid())

    return response


def replace_nans(encoded):
    regex = re.compile(r'\bNaN\b')
    return regex.sub('null', encoded)


def create_dataframe(response):
    import pandas as pd

    logging.info("=========== model_handler.create_dataframe")
    # Load 'inputs' key from JSON response to Pandas DataFrame
    logging.info("=========== inputs")
    #deserialize the serialized string objects coming back from the back end
    dict_obj_in = response.json()['inputs']
    json_obj_in = replace_nans(json.dumps(dict_obj_in))
    pd_obj_in = pd.read_json(json_obj_in)
    # Load 'outputs' key from JSON response to Pandas DataFrame
    logging.info("=========== outputs")
    dict_obj_out = response.json()['outputs']
    json_obj_out = replace_nans(json.dumps(dict_obj_out))
    pd_obj_out = pd.read_json(json_obj_out)
    logging.info("=========== dataframes created")
    return pd_obj_in, pd_obj_out


def modelInputPOSTReceiver(request, model):
    """
        Converts the POSTed data from the model's input page form
        to a Python dictionary and passes it to the Model object where
        it is to be converted to JSON and passed to the backend server.
    """

    logging.info("=========== model_handler.modelInputPOSTReceiver")
    args = {"inputs": {}}
    for key in request.POST:
        args["inputs"][key] = {"0": request.POST.get(key)}
    args["run_type"] = "single"
    logging.info("model:")
    logging.info(model)
    logging.info("args:")
    logging.info(args)

    response = call_model_server(model, args)

    logging.info("=========== returned from back end")
    jid = response.json()['_id']
    logging.info("job id = " + str(jid))
    run_type = response.json()['run_type']
    logging.info("run_type = " + run_type)
    dataframes = create_dataframe(response)

    model_obj = Model(run_type, jid, dataframes[0], dataframes[1])

    return model_obj


def modelInputPOSTReceiverFortran(request, model):
    """
        Converts the POSTed data from the model's input page form 
        to a Python dictionary and passes it to the Model object where
        it is to be converted to JSON and passed to the backend server. 
        
        ==> FORTAN version <==
    """

    args = {"inputs": {}}
    for key in request.POST:
        args["inputs"][key] = request.POST.get(key)
    args["run_type"] = "single"

    response = call_model_server(model, args)

    if model in {'sam'}:
        logging.info(response.json()['outputs'])

        return str(response.json()['outputs'])

    else:

        jid = response.json()['_id']
        run_type = response.json()['run_type']
        # dataframes = create_dataframe(response)

        model_obj = ModelFortran(run_type, jid, args['inputs'], response['inputs'])

        return model_obj


class ModelQAQC(object):
    def __init__(self, run_type, jid, pd_obj_in, pd_obj_out, pd_obj_exp):
        """
            Generic Python 'Model' object created from two Pandas 
            DataFrame objects, one for inputs and one for outputs.
        """

        logging.info("=========== model_handler.ModelQAQC")
        self.pd_obj_in = pd_obj_in
        self.pd_obj_out = pd_obj_out
        self.pd_obj_exp = pd_obj_exp
        self.jid = jid
        self.run_type = run_type

        for col in self.pd_obj_in:
            setattr(self, self.pd_obj_in[col].name, self.pd_obj_in[col].iloc[0])
        for col in self.pd_obj_out:
            setattr(self, self.pd_obj_out[col].name, self.pd_obj_out[col].iloc[0])
        for col in self.pd_obj_exp:
            setattr(self, self.pd_obj_exp[col].name, self.pd_obj_exp[col].iloc[0])


def generate_model_object_list(response):
    """
        Loops over the input and output DataFrames creating 
        a Python object 'Model' for each model run and appends
        the object to a Python list.  Returns the list of objects.
    """

    logging.info("=========== model_handler.generate_model_object_list")
    ModelList = []

    run_type = response.json()['run_type']
    jid = response.json()['_id']

    import pandas as pd
    # Load 'inputs' key from JSON response to Pandas DataFrame
    pd_obj_in = pd.io.json.read_json(json.dumps(response.json()['inputs']))
    # Load 'outputs' key from JSON response to Pandas DataFrame
    pd_obj_out = pd.io.json.read_json(json.dumps(response.json()['outputs']))

    if run_type == "qaqc":
        pd_obj_exp = pd.io.json.read_json(json.dumps(response.json()['exp_out']))

    no_of_runs = len(pd_obj_out.index)
    logging.info(no_of_runs)

    logging.info(pd_obj_out)

    i = 0
    while (i < no_of_runs):
        logging.info(i)
        run_list = range(no_of_runs)
        del run_list[i]

        logging.info(run_list)

        pd_obj_in_slice = pd_obj_in.drop(run_list)
        pd_obj_out_slice = pd_obj_out.drop(run_list)
        if run_type == "batch":
            model_obj = Model(run_type, jid, pd_obj_in_slice, pd_obj_out_slice)
        elif run_type == "qaqc":
            pd_obj_exp_slice = pd_obj_exp.drop(run_list)
            model_obj = ModelQAQC(run_type, jid, pd_obj_in_slice, pd_obj_out_slice, pd_obj_exp_slice)

        ModelList.append(model_obj)
        i += 1

    return ModelList
