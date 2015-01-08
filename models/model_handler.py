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

from REST import auth_s3
import os, logging

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']

class Model(object):
    def __init__(self, run_type, jid, pd_obj_in, pd_obj_out):
        """
            Generic Model object created from Requests Response object 
            received from the backend model server or JSON.
        """

        self.pd_obj_in = pd_obj_in
        self.pd_obj_out = pd_obj_out
        self.jid = jid
        self.run_type = run_type

        # Set object attributes to model inputs and outputs
        # if self.run_type == 'single':
        """
            Set each column of the DataFrames as object attribute with
            a value equal to the first row's value
        """
        logging.info("'SINGLE' run")
        for col in self.pd_obj_in:
            setattr(self, self.pd_obj_in[col].name, self.pd_obj_in[col].iloc[0])
        for col in self.pd_obj_out:
            setattr(self, self.pd_obj_out[col].name, self.pd_obj_out[col].iloc[0])

        # elif self.response.json()['run_type'] == 'batch':
        #     """
        #         Set each column of the DataFrames as object attribute (ListType) 
        #         with a value equal to the each row's value
        #     """
        #     logging.info("Not a 'SINGLE' run")
        #     for col in pd_obj:
        #         logging.info(col)
        #         # Create empty list for each model output attribute
        #         # self.
        #         # setattr(self, pd_obj[col].name, [])
        #         i = 0
        #         # logging.info(pd_obj[col].iteritems())
        #         for row in pd_obj[col]:
        #             logging.info(row)
        #             self.pd_obj[col].name.append(row)
        #             i += 1
        #     for col in pd_obj_out:
        #         setattr(self, pd_obj_out[col].name, pd_obj_out[col][0])      
 

def call_model_server(model, args):
    """
        Sends model input parameters (args) to model 
        backend server and returns the 'response'.  
        'args' can be type == 'dict' or 'string' (valid 
        JSON string).
    """

    from REST import rest_funcs
    import json, requests

    # If 'args' is a Python dictionary, dump it to a JSON string
    if type(args) == dict:
        data = json.dumps(args)
    else:
        data = args
    
    jid = rest_funcs.gen_jid()
    
    url = url_part1 + '/' + model + '/' + jid
    # POST JSON to model server
    response = requests.post(url, data=data, headers=http_headers, timeout=60)

    # logging.info(json.dumps(response.json()))
    # logging.info(type(json.loads(json.dumps(response.json()))))

    return response


def create_dataframe(response):
        import pandas as pd
        import json
        # Load 'inputs' key from JSON response to Pandas DataFrame
        pd_obj_in = pd.io.json.read_json(json.dumps(response.json()['inputs']))
        # Load 'outputs' key from JSON response to Pandas DataFrame
        pd_obj_out = pd.io.json.read_json(json.dumps(response.json()['outputs']))

        return pd_obj_in, pd_obj_out


def modelInputPOSTReceiver(request, model):
    """
        Converts the POSTed data from the model's input page form 
        to a Python dictonary and passes it to the Model object where  
        it is to be converted to JSON and passed to the backend server.
    """

    args = { "inputs" : {} }
    for key in request.POST:
        args["inputs"][key] = {"0" : request.POST.get(key)}
    args["run_type"] = "single"

    response = call_model_server(model, args)

    jid = response.json()['_id']
    run_type = response.json()['run_type']
    dataframes = create_dataframe(response)

    model_obj = Model(run_type, jid, dataframes[0], dataframes[1])

    return model_obj


class ModelQAQC(object):
    def __init__(self, model="", json=""):
        """
            Generic Model object for QAQC model runs consisting of 
            the model's input, output, and expected output values 
            as well as other model run specific information.
        """

        self.model = model
        self.json = json
        self.call_model_server()

    def call_model_server(self):
        """
            Sends JSON from "*_qaqc" model module to the backend 
            server.  The JSON string is formatted such 
            that it can be converted to a Pandas DataFrame.
        """

        from REST import rest_funcs
        import json, requests

        self.jid = rest_funcs.gen_jid()
        # url = url_part1 + '/terrplant/' + self.jid
        url = url_part1 + '/' + self.model + '/' + self.jid
        # POST JSON to model server
        response = requests.post(url, data=self.json, headers=http_headers, timeout=60)

        # logging.info(json.dumps(response.json()['inputs']))
        # logging.info(json.dumps(response.json()['outputs']))
        # logging.info(json.dumps(response.json()['exp_out']))
        # logging.info(json.dumps(response.json()))

        logging.info("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        import pandas as pd
        # Load 'inputs' key from JSON response to Pandas DataFrame
        pd_obj = pd.io.json.read_json(json.dumps(response.json()['inputs']))
        # Load 'outputs' key from JSON response to Pandas DataFrame
        pd_obj_out = pd.io.json.read_json(json.dumps(response.json()['outputs']))
        # Load 'exp_out' key from JSON response to Pandas DataFrame
        pd_obj_exp = pd.io.json.read_json(json.dumps(response.json()['exp_out']))

        """
            Set each column of the DataFrames as object attribute with
            a value equal to the first row's value
        """
        for col in pd_obj:
            setattr(self, pd_obj[col].name, pd_obj[col][0])
        for col in pd_obj_out:
            setattr(self, pd_obj_out[col].name, pd_obj_out[col][0])
        for col in pd_obj_exp:
            setattr(self, pd_obj_exp[col].name, pd_obj_exp[col][0])


# class ModelList(object):
#     def __init__(self, model_obj_list):
#         """

#         """

#         self.model_obj_list = []

#         self.add_to_list(model_obj_list)

#     def add_to_list(self, model_obj_list):
#         """

#         """
        
#         # self.model_obj_list = self.model_obj_list.append(model_obj)

#         return self.model_obj_list


def generate_model_object_list(response):
    """
        Extracts each model run out from batch run.
    """

    ModelList = []

    run_type = response.json()['run_type']
    jid = response.json()['_id']

    import pandas as pd
    import json
    # Load 'inputs' key from JSON response to Pandas DataFrame
    pd_obj_in = pd.io.json.read_json(json.dumps(response.json()['inputs']))
    # Load 'outputs' key from JSON response to Pandas DataFrame
    pd_obj_out = pd.io.json.read_json(json.dumps(response.json()['outputs']))

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
        model_obj = Model(run_type, jid, pd_obj_in_slice, pd_obj_out_slice)

        logging.info(model_obj.solubility)
        logging.info(model_obj.out_rundry)

        ModelList.append(model_obj)
        i += 1

    return ModelList