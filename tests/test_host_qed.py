import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup
import mechanize # for populating and submitting input data forms
import unicodedata


#this testing routine accepts a list of servers where a group of models and pages (i.e.,tabs)
#are presented as web pages.  it is assumed that the complete set of models and related pages
#are present on each server. this   routine performs a series of unit tests that ensure
#that the web pages are up and operational.

test = {}

#servers = ["http://127.0.0.1:8000/"]
servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
          "http://134.67.114.3/ubertool/", "http://134.67.114.1/ubertool/"]
#models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
#          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
#          "kabam/", "pfam/", "sam/", "therps/", "trex2/"]
models = ["sip/", "stir/", "pfam/", "earthworm/"]
#The following list represents the model page titles to be checked (order of models
#needs to be the same as "models" list above
#models_IO = ["SIP", "STIR", "RICE", "TerrPlant", "IEC",
#             "AgDrift", "AgDrift & T-REX", "AgDrift & T-HERPS", "Earthworm",
#             "KABAM", "PFAM", "SAM", "T-Herps", "T-REX 1.5.2"]
models_IO = ["SIP", "STIR", "PFAM", "Earthworm"]
#pages = ["", "description", "input", "algorithms", "references", "qaqc",
#         "batchinput", "history"]
pages = ["", "description", "input"]

redirect_servers = ["http://qed.epa.gov/ubertool/", "http://134.67.114.3/ubertool/"]
redirect_pages = ["input"]
qaqc_pages = ["qaqc"]

model_pages = [s + m + p for s in servers for m in models for p in pages]
redirect_model_pages = [s + m + p for s in redirect_servers for m in models
                        for p in redirect_pages]
qaqc_model_pages = [s + m + p for s in servers for m in models for p in qaqc_pages]
#upper_models = [str.upper(m)[:-1] for m in models]

redirect_models = models_IO * len(redirect_servers)
qaqc_models = models_IO * len(servers)
#print(model_pages)

class TestQEDHost(unittest.TestCase):
    def setup(self):
        pass

    def test_qed_200(self):
        try:
            response = [requests.get(m).status_code for m in model_pages]
            npt.assert_array_equal(response, 200, '200 error', True)
        finally:
            pass
        return

    def test_qed_qaqc_form(self):
        try:#need to repeat login, submit default inputs, and verify we land on output page
            current_title = [""] * len(qaqc_pages)
            expected_title = [""] * len(qaqc_pages)
            for idx, m in enumerate(qaqc_model_pages) :
                br = mechanize.Browser()
                response = br.open(m)
                # click on 'Run QAQC' button
                try:
                    br.click("<p >runQAQC</p>")
                except:
                    current_title[idx] = m.replace("qaqc", "") + ": " + "No " + qaqc_models[idx] + " qaqc"
                    expected_title[idx] = m.replace("qaqc", "") + ": " + qaqc_models[idx] + " qaqc"
                else:
                    response3 = br.submit()  # use mechanize to click on 'Run QAQC' button
                    response3.get_data()
                    #Verify we have successfully run qaqc and that we have qaqc results
                    soup = BeautifulSoup(response3, "html.parser")
                    tag = [a.find(text=True) for a in soup.findAll('h2', {'class': 'model_header'})]
                    current_title[idx] = m.replace("input", "") + ": " + str(tag[0])
                    expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Output"
            #create array comparison (assume h2/model h eader -tag- of interest is first in list)
            npt.assert_array_equal(current_title, expected_title,'QAQC Failed', True)
        finally:
            pass
        return

    def test_qed_redirect(self):
        try:
            response = [requests.get(m) for m in redirect_model_pages]
            boo302 = [False] * len(response)
            boocheck = [True] * len(response)
            urllist_302s = [""] * len(response)
            for i in range(len(response)):
                for resp in response[i].history:
                    if resp.status_code == 302:
                        boo302[i] = True
                        urllist_302s[i] = resp.url
            npt.assert_array_equal(boo302, boocheck, '302 error', True)
        finally:
            pass
        return

    def test_qed_authenticate_input(self):
        try: #need to login and then verify we land on input page
            current_page = [""] * len(redirect_model_pages)
            expected_page = [""] * len(redirect_model_pages)
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
            npt.assert_array_equal(expected_page, current_page, 'Login Failed', True)
        finally:
            pass
        return

    def test_qed_input_form(self):
        try: #need to repeat login and then verify title of input page
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
                #locate model page title and verify it is as expected
                soup = BeautifulSoup(response2, "html.parser")
                tag = [a.find(text=True) for a in soup.findAll('h2', {'class': 'model_header'})]
                current_title[idx] = m.replace("input", "") + ": " + str(tag[0])
                expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Inputs"
                #create array comparison ((assume h2/model header -tag- of interest is first in list)
            npt.assert_array_equal(current_title, expected_title,'Wrong Input Page Title', True)
        finally:
            pass
        return

    def test_qed_output_form(self):
        try:#need to repeat login, submit default inputs, and verify we land on output page
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
                except:
                    current_title[idx] = m.replace("input", "") + ": " + "No " + redirect_models[idx] + " Output"
                    expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Output"
                else:
                    response3 = br.submit()  # use mechanize to post input data
                    response3.get_data()
                    #Verify we have successfully posted input data and that we have arrived at the output page
                    soup = BeautifulSoup(response3, "html.parser")
                    tag = [a.find(text=True) for a in soup.findAll('h2', {'class': 'model_header'})]
                    current_title[idx] = m.replace("input", "") + ": " + str(tag[0])
                    expected_title[idx] = m.replace("input", "") + ": " + redirect_models[idx] + " Output"
            #create array comparison (assume h2/model h eader -tag- of interest is first in list)
            npt.assert_array_equal(current_title, expected_title,'Submittal of Input Failed', True)
        finally:
            pass
        return

    def test_qed_404(self):
        try:
            response = [requests.get(m) for m in model_pages]
            urllist_404s = [""] * len(response)
            boo_check = [False] * len(response)
            soup_content = [BeautifulSoup(r.content, "html.parser") for r in response]
            soup_N404s = [len(s.findAll('img',src='/static/images/404error.png')) for s in soup_content]
            boo404 = [s>0 for s in soup_N404s]
            npt.assert_array_equal(boo404, boo_check, '404 error', True)
        finally:
            pass
        return

    def teardown(self):
        pass

# unittest will
# 1) call the setup method,
# 2) then call every method starting with "test",
# 3) then the teardown method
if __name__ == '__main__':
    unittest.main()
