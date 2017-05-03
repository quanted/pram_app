"""
.. module:: iec_qaqc
   :synopsis: Reads in CSV file containing model inputs and expected 
   outputs and converts them into each of their own DataFrames (2 total). 
   The DataFrames are converted to JSON strings and then concatenated 
   into one JSON string with base keys of 'inputs' and 'exp_out'. The JSON 
   is sent to the model_handler module to be sent to the backend model server.
"""

import pandas as pd

def iecQaqc(model, csv_path):
    """
        Read in QAQC CSV as Pandas DataFrame, removing 
        any uneeded columns, setting the index_col name 
        to None, and renumbering the data columns.
    """
    
    # Read QAQC csv and create a Pandas DataFrame with only the relevant columns for the input values
    pd_obj_inputs = pd.read_csv(csv_path, index_col=0, header=None, skiprows=1, skipfooter=46, engine='python')
    pd_obj_inputs = pd_obj_inputs.drop(labels=pd_obj_inputs.columns[range(4)], axis=1)
    pd_obj_inputs.index.name = None
    pd_obj_inputs.columns = pd_obj_inputs.columns - 5
    
    # Read QAQC csv and create a Pandas DataFrame with only the relevant columns for the expected output values
    pd_obj_exp_out = pd.read_csv(csv_path, index_col=0, header=None, skiprows=50, engine='python')
    pd_obj_exp_out = pd_obj_exp_out.drop(labels=pd_obj_exp_out.columns[range(4)], axis=1)
    pd_obj_exp_out.index.name = None
    pd_obj_exp_out.columns = pd_obj_exp_out.columns - 5

    return pd_obj_inputs, pd_obj_exp_out


# def set_globals(**kwargs):
#     for argname in kwargs:
#         globals()['%s_in' % argname] = kwargs[argname]
           
# class TestCase_z_score_f_out(unittest.TestCase):
#     def setUp(self):
#         self.iec_obj = iec_object_in
#     def testz_score_f_out_in(self):
#         out_fun_z_score_f.append(self.iec_obj.z_score_f_out)
#         testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("Z_score_f",self.iec_obj.z_score_f_out,fun)
#         self.assertEqual(round(fun,3),round(self.z_score_f_out,3),testFailureMessage)

# class TestCase_F8_f_out(unittest.TestCase):
#     def setUp(self):
#         self.iec_obj = iec_object_in
#     def testF8_f_out_in(self):
#         out_fun_F8_f.append(self.iec_obj.F8_f_out)
#         testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("F8_f",self.iec_obj.F8_f_out,fun)
#         self.assertEqual(round(fun,3),round(self.F8_f_out,3),testFailureMessage)
            
# class TestCase_chance_f_out(unittest.TestCase):
#     def setUp(self):
#         self.iec_obj = iec_object_in
#     def testchance_f_out_in(self):
#         out_fun_chance_f.append(self.iec_obj.chance_f_out)
#         testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("Chance_f",self.iec_obj.chance_f_out,fun)
#         self.assertEqual(round(fun,3),round(self.chance_f_out,3),testFailureMessage)
                        
# def suite(TestCaseName, **kwargs):
#     suite = unittest.TestSuite()
#     set_globals(**kwargs)
#     suite.addTest(unittest.makeSuite(TestCaseName))
#     stream = StringIO()
#     runner = unittest.TextTestRunner(stream=stream, verbosity=2)
#     result = runner.run(suite)
#     stream.seek(0)
#     test_out=stream.read()
#     return test_out

# iec_obj = iec_model.iec(True,True,'qaqc',dose_response[0],lc50[0],threshold[0])
# iec_obj.set_unit_testing_variables()

# iec_obj.z_score_f_out_expected = z_score_f_out[0]
# iec_obj.F8_f_out_expected = F8_f_out[0]
# iec_obj.chance_f_out_expected = chance_f_out[0]

# test_suite_z_score_f_out = suite(TestCase_z_score_f_out, iec_obj=iec_obj)
# test_suite_F8_f_out = suite(TestCase_F8_f_out, iec_obj=iec_obj)
# test_suite_chance_f_out = suite(TestCase_chance_f_out, iec_obj=iec_obj)

