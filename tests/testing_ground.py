import requests
from bs4 import BeautifulSoup
import unittest
import numpy.testing as npt
import unicodedata
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import os
import time
from tabulate import tabulate

phantomjs_path = "C://Python27//Lib//site-packages//selenium//webdriver//phantomjs//phantomjs-2.1.1-windows//bin//phantomjs.exe"

# this testing routine accepts a list of servers where a group of models and pages (i.e.,tabs)
# are presented as web pages.  it is assumed that the complete set of models and related pages
# are present on each server. this   routine performs a series of unit tests that ensure
# that the web pages are up and operational.

test = {}

# servers = ["http://127.0.0.1:8000/"]
main_server = "http://qed.epa.gov/ubertool/"
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

redirect_servers = ["http://qed.epa.gov/ubertool/", "http://134.67.114.3/ubertool/"]
redirect_pages = ["input"]
redirect_model_pages = [s + m + p for s in redirect_servers for m in models
                        for p in redirect_pages]
redirect_models = models_IO * len(redirect_servers)

qaqc_pages = ["qaqc"]
qaqc_model_pages = [s + m + p for s in servers for m in models for p in qaqc_pages]
qaqc_models = models_IO * len(servers) * len(qaqc_pages)


class WaitForPageLoad(object):  # ensures that a new page has fully loaded upon a click
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

    def test_qed_authenticate_input(self):
        try:  # verify successful login and that we land on input page url
            current_page = [""] * len(redirect_model_pages)
            expected_page = [""] * len(redirect_model_pages)
            table_rows = [""] * len(redirect_model_pages)
            for idx, m in enumerate(redirect_model_pages):
                browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
                browser.get(m)
                # login and authenticate
                username = browser.find_element_by_name("username")
                username.send_keys("betatester")
                password = browser.find_element_by_name("password")
                password.send_keys("ubertool")
                with WaitForPageLoad(browser):
                    LoginButton = browser.find_element_by_class_name("input_button")
                    LoginButton.click()
                # Verify we have successfully logged in and are now on input page
                current_page[idx] = str(browser.current_url)
                expected_page[idx] = m
                table_rows[idx] = [expected_page[idx], current_page[idx]]
            try:
                npt.assert_array_equal(expected_page, current_page, 'Login Test Failed', True)
            except:
                print "Login failed for one or more models"
                headers = ["expected", "actual/message"]
                print tabulate(table_rows, headers, tablefmt='grid')
        finally:
            browser.quit()
            pass
        return

    def test_qed_input_form(self):
        # verify input page contains expected content (e.g., input tables)
        try:
            current_page = [""] * len(redirect_model_pages)
            expected_page = [""] * len(redirect_model_pages)
            table_rows = [""] * len(redirect_model_pages)
            for idx, m in enumerate(redirect_model_pages):
                expected_page[idx] = m + " : " + redirect_models[idx] + " Inputs"
                browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
                browser.get(m)
                # login and authenticate
                username = browser.find_element_by_name("username")
                username.send_keys("betatester")
                password = browser.find_element_by_name("password")
                password.send_keys("ubertool")
                with WaitForPageLoad(browser):
                    LoginButton = browser.find_element_by_class_name("input_button")
                    LoginButton.click()
                # verify that login was successful by checking that inputs page is rendered
                if browser.page_source.__contains__(redirect_models[idx] + " Inputs"):
                    current_page[idx] = m + " : " + redirect_models[idx] + " Inputs"
                else:
                    current_page[idx] = m + " : " + redirect_models[idx] + " Input Submit Error"
                table_rows[idx] = [expected_page[idx], [current_page[idx]]]
            try:
                npt.assert_array_equal(expected_page, current_page, 'Input Form Submittal Failed', True)
            except:
                print "One or more models FAILED to produce QAQC results"
                headers = ["expected", "actual/message"]
                print tabulate(table_rows, headers, tablefmt='grid')
        finally:
            browser.quit()
            pass
        return

    def test_qed_output_form(self):
        try:  # verify that submission of input tables results in proper output page content
            current_title = [""] * len(redirect_model_pages)
            expected_title = [""] * len(redirect_model_pages)
            table_rows = [""] * len(redirect_model_pages)
            for idx, m in enumerate(redirect_model_pages):
                expected_title[idx] = m.replace("input", "") + " : " + redirect_models[idx] + " Output"
                browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
                browser.get(m)
                # step 1: login and authenticate
                username = browser.find_element_by_name("username")
                username.send_keys("betatester")
                password = browser.find_element_by_name("password")
                password.send_keys("ubertool")
                with WaitForPageLoad(browser):
                    LoginButton = browser.find_element_by_class_name("input_button")
                    LoginButton.click()  # use .click() for individual buttons and .submit() for form submittal
                # Step 2: Select and submit input form (it will have default data in it  -  we just want to run with that for now)
                with WaitForPageLoad(browser):
                    try:
                        # submit default dataset
                        found_input = browser.find_element_by_class_name("input_button").is_displayed()
                    except:
                        found_input = False
                    try:
                        found_submit = browser.find_element_by_class_name("submit input_button").is_displayed()
                    except:
                        found_submit = False
                    if found_input == True:
                        InputSubmitButton = browser.find_element_by_class_name("input_button")
                    elif found_submit:
                        InputSubmitButton = browser.find_element_by_class_name("submit input_button")
                    else:
                        pass
                        # use .click() for individual buttons and .submit() for form submittal
                    InputSubmitButton.submit()
                    if browser.page_source.__contains__("User Inputs"):
                        current_title[idx] = browser.current_url.replace("output", "") + " : " + redirect_models[
                            idx] + " Output"
                    elif browser.page_source.__contains__('File Not Found'):
                        current_title[idx] = browser.current_url.replace("output", "") + " : File Not Found Page Error"
                    else:
                        current_title[idx] = browser.current_url.replace("output", "") + " : Unknown Output Page Error"
                    pass
                # create array comparison for assertion test
                table_rows[idx] = [expected_title[idx], [current_title[idx]]]
            try:
                npt.assert_array_equal(expected_title, current_title, 'Submittal of Input Failed', True)
             except:
                print "One or more models FAILED to produce output"
                headers = ["expected", "actual/message"]
                print tabulate(table_rows, headers, tablefmt='grid')
        finally:
            browser.quit()
            pass
        return

    def test_qed_qaqc_form(self):
        try:  # need to repeat login, submit default inputs, and verify we land on output page
            current_pageID = [""] * len(qaqc_model_pages)  # pageID = url + <h2 class='model header' string>
            expected_pageID = [""] * len(qaqc_model_pages)
            table_rows = [""] * len(qaqc_model_pages)
            browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
            # added the argument service_log_path=os.path.devnull to the function webdriver.PhantomJS()
            # to prevent PhantomJS from creating a ghostdriver.log in the directory of the python file
            # being executed.
            for idx, m in enumerate(qaqc_model_pages):
                expected_pageID[idx] = m + "/run : " + qaqc_models[idx] + " QAQC"
                browser.get(m)
                try:
                    with WaitForPageLoad(browser):
                        qaqcRunButton = browser.find_element_by_id('runQAQC')
                        qaqcRunButton.click()
                    if browser.current_url.__str__() != m + "/run":
                        current_pageID[idx] = str(
                            browser.current_url) + " : Run QAQC failed"  # we did not arrive at expected url
                    elif browser.page_source.__contains__('File Not Found'):
                        current_pageID[idx] = str(browser.current_url) + " : File Not Found Page Error"
                    elif browser.page_source.__contains__("User Inputs"):
                        # check to see of string User Inputs appears on page
                        current_pageID[idx] = m + "/run : " + qaqc_models[idx] + " QAQC"
                    else:
                        current_pageID[idx] = str(browser.current_url) + " Unknown QAQC r un error"
                except:
                    current_pageID[idx] = m + " Unknown exception thrown"
            # create array comparison (assume h2/model h eader -tag- of interest is first in list)
                table_rows[idx] = [expected_pageID[idx], [current_pageID[idx]]]
            try:
                npt.assert_array_equal(expected_pageID, current_pageID, 'QAQC Failed', True)
            except:
                print "One or more models FAILED to produce QAQC results"
                headers = ["expected", "actual/message"]
                print tabulate(table_rows, headers, tablefmt='grid')
        finally:
            browser.quit()
            pass
        return

    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main()
