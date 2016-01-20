import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup
import mechanize


#this testing routine accepts a list of servers where a group of models and pages (i.e.,tabs)
#are presented as web pages.  it is assumed that the complete set of models and related pages
#are present on each server. this routine performs a series of unit tests that ensure
#that the web pages are up and operational.

test = {}

servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
           "http://134.67.114.3/ubertool/", "http://134.67.114.1/ubertool/"]
#models = ["sip/", "stir/", "rice/", "terrplant/", "trex2/", "therps/", "iec/",
#          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
#          "rice/", "kabam/", "pfam/", "sam/"]
models = ["sip/", "stir/"]
#pages = ["", "description", "input", "algorithms", "references", "qaqc",
#         "batchinput", "history"]
pages = ["", "description", "input"]

redirect_servers = ["http://qed.epa.gov/ubertool/", "http://134.67.114.3/ubertool/"]
redirect_pages = ["input"]

model_pages = [s + m + p for s in servers for m in models for p in pages]
redirect_model_pages = [s + m + p for s in redirect_servers for m in models
                        for p in redirect_pages]
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
        try:
            for m in redirect_model_pages :
                #step 1: login and authenticate
                br = mechanize.Browser()
                response = br.open(m)
                expected_page = redirect_servers[0] + models[0] + pages[2]
                # try and extract list of forms from page
                for form in br.forms():
                   print '%r %r %s' % (form.name, form.attrs.get('id'), form.action)
                br.select_form(name="auth")
                br["username"] = "betatester"
                br["password"] = "ubertool"
                response2 = br.submit()
                response2.get_data()
                # Verify we have successfully logged in and are now on input page
                current_page = br.geturl()
                npt.assert_equal(expected_page, current_page,'Login Failed', True)
        finally:
            pass
        return

    def test_qed_authenticate_output(self):
        try:
            for m in redirect_model_pages :
                #step 1: login and authenticate
                br = mechanize.Browser()
                response = br.open(m)
                expected_page = redirect_servers[0] + models[0] + pages[2]
                # try and extract list of forms from page
                for form in br.forms():
                   print '%r %r %s' % (form.name, form.attrs.get('id'), form.action)
                br.select_form(name="auth")
                br["username"] = "betatester"
                br["password"] = "ubertool"
                response2 = br.submit()
                response2.get_data()
                # Verify we have successfully logged in and are now on input page
                current_page = br.geturl()
                npt.assert_equal(expected_page, current_page,'Login Failed', True)
                # Step 2: Select input form (it will have default data in it  -  we just want to run with that for now)
                br.form = list(br.forms())[0] # syntax for selecting form when form is unnamed
                response3 = br.submit()  # use mechanize to post input data
                #Verify we have successfully posted input data and that we have arrived at the output page
                current_page = br.geturl()
                expected_page = redirect_servers[0] + models[0] + "output"
                npt.assert_equal(expected_page, current_page,'Submittal of Input Failed', True)

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
