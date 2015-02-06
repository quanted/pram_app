"""
.. module:: sip_qaqc
   :synopsis: Reads in CSV file containing model inputs and expected 
   outputs and converts them into each of their own DataFrames (2 total). 
   The DataFrames are converted to JSON strings and then concatenated 
   into one JSON string with base keys of 'inputs' and 'exp_out'. The JSON 
   is sent to the model_handler module to be sent to the backend model server.
"""

import os, json#, logging
import pandas as pd


def sipQaqc(model, csv_path):
    """
        Read in QAQC CSV as Pandas DataFrame, removing 
        any uneeded columns, setting the index_col name 
        to None, and renumbering the data columns.
    """
    
    # Read QAQC csv and create a Pandas DataFrame with only the relevant columns for the input values
    pd_obj_inputs = pd.read_csv(csv_path, index_col=0, header=None, skiprows=1, skipfooter=32, engine='python')
    pd_obj_inputs = pd_obj_inputs.drop(labels=pd_obj_inputs.columns[range(4)], axis=1)
    pd_obj_inputs.index.name = None
    pd_obj_inputs.columns = pd_obj_inputs.columns - 5
    
    # Read QAQC csv and create a Pandas DataFrame with only the relevant columns for the expected output values
    pd_obj_exp_out = pd.read_csv(csv_path, index_col=0, header=None, skiprows=33, engine='python')
    pd_obj_exp_out = pd_obj_exp_out.drop(labels=pd_obj_exp_out.columns[range(4)], axis=1)
    pd_obj_exp_out.index.name = None
    pd_obj_exp_out.columns = pd_obj_exp_out.columns - 5

    return pd_obj_inputs, pd_obj_exp_out