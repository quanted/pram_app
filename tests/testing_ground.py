import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup
#import mechanize  # for populating and submitting input data forms
import unicodedata
from selenium import webdriver
import os
phantomjs_path = "C://Python27//Lib//site-packages//selenium//webdriver//phantomjs//phantomjs-2.1.1-windows//bin//phantomjs.exe"

# this testing routine accepts a list of servers where a group of models and pages (i.e.,tabs)
# are presented as web pages.  it is assumed that the complete set of models and related pages
# are present on each server. this   routine performs a series of unit tests that ensure
# that the web pages are up and operational.

test = {}

# servers = ["http://127.0.0.1:8000/"]
servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
           "http://134.67.114.3/ubertool/", "http://134.67.114.1/ubertool/"]
# models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
#          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
#          "kabam/", "pfam/", "sam/", "therps/", "trex2/"]
models = ["sip/", "stir/", "pfam/", "earthworm/"]
# The following list represents the model page titles to be checked (order of models
# needs to be the same as "models" list above
# models_IO = ["SIP", "STIR", "RICE", "TerrPlant", "IEC",
#             "AgDrift", "AgDrift & T-REX", "AgDrift & T-HERPS", "Earthworm",
#             "KABAM", "PFAM", "SAM", "T-Herps", "T-REX 1.5.2"]
models_IO = ["SIP", "STIR", "PFAM", "Earthworm"]

qaqc_pages = ["qaqc"]
qaqc_model_pages = [s + m + p for s in servers for m in models for p in qaqc_pages]

qaqc_models = models_IO * len(servers)


# print(model_pages)

class TestQAQC(unittest.TestCase):
    def setup(self):
        pass

    def test_qaqc_form(self):
        try:  # need to repeat login, submit default inputs, and verify we land on output page
            current_title = [""] * len(qaqc_pages)
            expected_title = [""] * len(qaqc_pages)
            browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
            # added the argument service_log_path=os.path.devnull to the function webdriver.PhantomJS()
            # to prevent PhantomJS from creating a ghostdriver.log in the directory of the python file
            # being executed.
            for idx, m in enumerate(qaqc_model_pages):
                browser.get(m)
                # click on 'Run QAQC' button
                try:
                    linkElem = browser.find_element_by_id('runQAQC')
                    type(linkElem)
                    linkElem.click()
                except:
                    current_title[idx] = m.replace("qaqc", "") + ": " + "No " + qaqc_models[idx] + " qaqc"
                    expected_title[idx] = m.replace("qaqc", "") + ": " + qaqc_models[idx] + " qaqc"
                else:
                    # Verify we have successfully run qaqc and that we have qaqc results
                    browser.current_url
                    browser.title
                    #err = browser.find_element_by_tag_name('img')
                    #err = browser.find_elements_by_link_text('/static/images/404error.png')
                    soup = BeautifulSoup(browser.page_source, "html.parser")
                    tag = [a.find(text=True) for a in soup.findAll('h2', {'class': 'model_header'})]
                    current_title[idx] = browser.current_url
                    expected_title[idx] = m +
                    #current_title[idx] = m.replace("qaqc", "") + ": " + str(tag[0])
                    #expected_title[idx] = m.replace("qaqc", "") + ": " + redirect_models[idx] + " QAQC"
            # create array comparison (assume h2/model h eader -tag- of interest is first in list)
            npt.assert_array_equal(current_title, expected_title, 'QAQC Failed', True)
        finally:
            pass
        return

    def teardown(self):
        browser.quit()
        pass


if __name__ == '__main__':
    unittest.main()
