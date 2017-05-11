import requests
import unittest
import numpy.testing as npt
import linkcheck_helper

test = {}

servers = ["https://qedinternal.epa.gov/ubertool/","http://127.0.0.1:8000/ubertool/"]

models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
          "agdrift/", "earthworm/", "beerex/",
          "kabam/", "sam/", "therps/", "trex/"]
#models = ["sip/", "stir/", "pfam/", "earthworm/"]

#The following list represents the model page titles to be checked (order of models
#needs to be the same as "models" list above)

models_IO = ["SIP", "STIR", "RICE", "TerrPlant", "IEC",
             "AgDrift", "AgDrift & T-REX", "AgDrift & T-HERPS", "Earthworm",
             "KABAM", "PFAM", "SAM", "T-Herps", "T-REX 1.5.2"]
#models_IO = ["SIP", "STIR", "PFAM", "Earthworm"]

pages = ["", "description", "input", "algorithms", "references", "qaqc"]
         #"batchinput", "history"]

#following are lists of url's to be processed with tests below
model_pages = [s + m + p for s in servers for m in models for p in pages]


class TestUbertoolPages(unittest.TestCase):
    """
    this testing routine accepts a list of pages and performs a series of unit tests that ensure
    that the web pages are up and operational on the server.
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    @staticmethod
    def test_qed_200():
        test_name = "Model page access for ubertool models \n"
        try:
            #returns array of status codes for each page
            response = [requests.get(m).status_code for m in model_pages]
            n_tests = len(response)
            response_200s = [200]*n_tests
            #find which tests failed and pass to another documentation function
            assert_error = False
            try:
                npt.assert_array_equal(response, response_200s, '200 error', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, model_pages, response)
        return

# unittest will
# 1) call the setup method,
# 2) then call every method starting with "test",
# 3) then the teardown method
if __name__ == '__main__':
    unittest.main()