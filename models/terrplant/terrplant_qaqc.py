"""
.. module:: terrplant_qaqc
   :synopsis: Reads in CSV file containing model inputs and expected 
   outputs and converts them into each of their own DataFrames (2 total). 
   The DataFrames are converted to JSON strings and then concatenated 
   into one JSON string with base keys of 'inputs' and 'exp_out'. The JSON 
   is sent to the model_handler module to be sent to the backend model server.
"""

import os, json#, logging
import pandas as pd


def terrplantQaqc(model, csv_path):
    
    # Read QAQC csv and create a Pandas DataFrame with only the relevant columns for the input values
    pd_obj_inputs = pd.read_csv(csv_path, usecols=[1, 5], index_col=0, header=None, skiprows=1, skipfooter=46, engine='python', names=range(2))
    
    # Read QAQC csv and create a Pandas DataFrame with only the relevant columns for the expected output values
    pd_obj_exp_out = pd.read_csv(csv_path, usecols=[1, 5], index_col=0, header=None, skiprows=50, engine='python', names=range(2))
    
    return pd_obj_inputs, pd_obj_exp_out