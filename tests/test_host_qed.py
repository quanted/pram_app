import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup
import mechanize # for populating and submitting input data forms
import unicodedata
from tabulate import tabulate
import linkcheck_helper

test = {}

servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
          "http://134.67.114.3/ubertool/", "http://134.67.114.1/ubertool/"]

models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
          "kabam/", "pfam/", "sam/", "therps/", "trex2/"]
#models = ["sip/", "stir/", "pfam/", "earthworm/"]

#The following list represents the model page titles to be checked (order of models
#needs to be the same as "models" list above)

models_IO = ["SIP", "STIR", "RICE", "TerrPlant", "IEC",
             "AgDrift", "AgDrift & T-REX", "AgDrift & T-HERPS", "Earthworm",
             "KABAM", "PFAM", "SAM", "T-Herps", "T-REX 1.5.2"]
#models_IO = ["SIP", "STIR", "PFAM", "Earthworm"]

pages = ["", "description", "input", "algorithms", "references", "qaqc",
         "batchinput", "history"]
#pages = ["description", "input"]

#redirect servers are those where user login for the input page is required
redirect_servers = ["http://qed.epa.gov/ubertool/", "http://134.67.114.3/ubertool/"]
redirect_pages = ["input"]

#following are lists of url's to be processed with tests below
model_pages = [s + m + p for s in servers for m in models for p in pages]
redirect_model_pages = [s + m + p for s in redirect_servers for m in models
                        for p in redirect_pages]
redirect_models = models_IO * len(redirect_servers)


class TestQEDHost(unittest.TestCase):
    """
    this testing routine accepts a list of servers where a group of models and pages (i.e.,tabs)
    are presented as web pages.  it is assumed that the complete set of models and related pages
    are present on each server. this routine performs a series of unit tests that ensure
    that the web pages are up and operational.
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    @staticmethod
    def test_qed_200():
        test_name = "Model page access "
        try:
            assert_error = False
            response = [requests.get(m).status_code for m in model_pages]
            try:
                npt.assert_array_equal(response, 200, '200 error', True)
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

    @staticmethod
    def test_qed_404():
        test_name = "Model page 404 "
        try:
            assert_error = False
            response = [requests.get(m) for m in model_pages]
            check_of404 = ["Ok"] * len(response)
            assume_no404 = [False] * len(response)  #assume no 404 in page html
            page_content = [BeautifulSoup(r.content, "html.parser") for r in response]
            find_N404s = [len(s.findAll('img',src='/static/images/404error.png')) for s in page_content]
            did_we_find404 = [s>0 for s in find_N404s]
            for item in did_we_find404:
                if item == True:
                    check_of404[item] = "Found 404"
            try:
                npt.assert_array_equal(did_we_find404, assume_no404, '404 error', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, model_pages, check_of404)
        return

    @staticmethod
    def test_qed_redirect():  #redirects occur on 'input' pages due to login requirement
        test_name = "Model Input Page Redirect "
        try:
            response = [requests.get(m) for m in redirect_model_pages]
            assert_error = False
            check_of302 = ["302 Failed"] * len(response)
            did_we_find302 = [False] * len(response)
            assume302 = [True] * len(response)  # we're expecting 302 as response history
            for idx, r in enumerate(response):
                for resp in r.history:
                    if resp.status_code == 302:
                        did_we_find302[idx] = True
                        check_of302[idx] = "Ok"
            try:
                npt.assert_array_equal(did_we_find302, assume302, '302 error', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, redirect_model_pages, check_of302)
        return

    @staticmethod
    def test_qed_authenticate_input():
        test_name = "Model Input Page Login Authentication "
        try: #need to login and then verify we land on input page
            current_page = [""] * len(redirect_model_pages)
            expected_page = [""] * len(redirect_model_pages)
            assert_error = False
            for idx, m in enumerate(redirect_model_pages) :
                br = mechanize.Browser()
                br.open(m)
                #step 1: login and authenticate
                br.select_form(name="auth")
                br["username"] = "betatester"
                br["password"] = "ubertool"
                br.submit()
                # Verify we have successfully logged in and are now on input page
                current_page[idx] = br.geturl()
                expected_page[idx] = m
            try:
                npt.assert_array_equal(expected_page, current_page, 'Login Failed', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, expected_page, current_page)
        return

    @staticmethod
    def test_qed_input_form():
        test_name = "Model Input Page Generation "
        try: #need to repeat login and then verify title of input page
            assert_error = False
            current_title = [""] * len(redirect_model_pages)
            expected_title = [""] * len(redirect_model_pages)
            for idx, m in enumerate(redirect_model_pages):
                br = mechanize.Browser()
                br.open(m)
                #step 1: login and authenticate
                br.select_form(name="auth")
                br["username"] = "betatester"
                br["password"] = "ubertool"
                response2 = br.submit()
                response2.get_data()
                #locate model input page title and verify it is as expected
                soup = BeautifulSoup(response2, "html.parser")
                tag = [a.find(text=True) for a in soup.findAll('h2', {'class': 'model_header'})]
                current_title[idx] = m.replace("input", "") + ": " + str(tag[0])
                expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Inputs"
                #create array comparison ((assume h2/model header -tag- of interest is first in list)
            try:
                npt.assert_array_equal(current_title, expected_title,'Wrong Input Page Title', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, expected_title, current_title)
        return

    @staticmethod
    def test_qed_output_form():
        test_name = "Model output generation "
        try:        #need to repeat login, submit default inputs, and verify we land on output page
            assert_error = False
            current_title = [""] * len(redirect_model_pages)
            expected_title = [""] * len(redirect_model_pages)
            for idx, m in enumerate(redirect_model_pages) :
                br = mechanize.Browser()
                response = br.open(m)
                #step 1: login and authenticate
                br.select_form(name="auth")
                br["username"] = "betatester"
                br["password"] = "ubertool"
                response2 = br.submit()
                response2.get_data()
                # Step 2: Select and submit input form (it will have default data in it  -  we just want to run with that for now)
                try:
                    br.form = list(br.forms())[0] # syntax for selecting form when form is unnamed
                    response3 = br.submit()  # use mechanize to post input data
                    response3.get_data()
                    #Verify we have successfully posted input data and that we have arrived at the output page
                    soup = BeautifulSoup(response3, "html.parser")
                    tag = [a.find(text=True) for a in soup.findAll('h2', {'class': 'model_header'})]
                    current_title[idx] = m.replace("input", "") + ": " + str(tag[0])
                    expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Output"
                except Exception:
                    current_title[idx] = m.replace("input", "") + ": " + "No " + redirect_models[idx] + " Output"
                    expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Output"
            try:
                #create array comparison (assume h2/model header -tag- of interest is first in list)
                npt.assert_array_equal(current_title, expected_title,'Submittal of Input Failed for one or more models', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, expected_title, current_title)
        return


# unittest will
# 1) call the setup method,
# 2) then call every method starting with "test",
# 3) then the teardown method
if __name__ == '__main__':
    unittest.main()
