import unittest
import numpy.testing as npt
import unicodedata
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

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

qaqc_models = models_IO * len(servers) * len(qaqc_pages)


# print(model_pages)


class WaitForPageLoad(object):
    def __init__(self, browser):
        """
        :rtype: object
        """
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id
    
    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )

    def __exit__(self, *_):
        self.wait_for(self.page_has_loaded)

class TestQAQC(unittest.TestCase, WaitForPageLoad):
    def setup(self):
        pass

    def test_qaqc_form(self):
        try:  # need to repeat login, submit default inputs, and verify we land on output page
            current_pageID = [""] * len(qaqc_model_pages)  # pageID = url + <h2 class='model header' string>
            expected_pageID = [""] * len(qaqc_model_pages)
            browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
            # added the argument service_log_path=os.path.devnull to the function webdriver.PhantomJS()
            # to prevent PhantomJS from creating a ghostdriver.log in the directory of the python file
            # being executed.
            for idx, m in enumerate(qaqc_model_pages):
                expected_pageID[idx] = m + "/run : " + qaqc_models[idx] + " QAQC"
                browser.get(m)
                try:
                    # qaqcRunButton = browser.find_element_by_id('runQAQC')
                    # location = qaqcRunButton.location
                    # type(qaqcRunButton)
                    # qaqcRunButton.click()  # click on 'Run QAQC' button
                    # browser.implicitly_wait(5)
                    # browser.refresh()
                    # Process possible outcomes
                    with WaitForPageLoad(browser):
                        qaqcRunButton = browser.find_element_by_id('runQAQC')
                        qaqcRunButton.click()
                    if browser.current_url.__str__() != m + "/run":
                        current_pageID[idx] = str(browser.current_url) + " : Run QAQC failed"  # we did not arrive at expected url
                    elif browser.page_source.__contains__('File Not Found'):
                        current_pageID[idx] = str(browser.current_url) + " : File Not Found Page Error"
                    elif browser.page_source.__contains__(qaqc_models[idx] + " QAQC"):
                        # need to look for something else to determine whether the output tables are generated and presented
                        current_pageID[idx] = m + "/run : " + qaqc_models[idx] + " QAQC"
                    else:
                        current_pageID[idx] = str(browser.current_url) + " Unknown error"
                except:
                    current_pageID[idx] = m + " Unknown exception thrown"
            # create array comparison (assume h2/model h eader -tag- of interest is first in list)
            npt.assert_array_equal(current_pageID, expected_pageID, 'QAQC Failed', True)
        finally:
            browser.quit()
            pass
        return

    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main()
