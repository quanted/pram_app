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
import linkcheck_helper

phantomjs_path = "C://Python27//Lib//site-packages//selenium//webdriver//phantomjs//phantomjs-2.1.1-windows//bin//phantomjs.exe"

# this testing routine tests input and QAQC functionality of models;
# the input tests include login authentication, submittal of default inputs,
# and invocation of the QAQC
# Note: the login/input/output tests included here net the same results as those
# included in 'test_host_qed.py'; the difference is that "selenium/webdriver" is used here to
# navigate html whereas "mechanize" was used in test_host_qed.py; mechanize is for forms
# only and cannot handle button pushing (which is needed for the QAQC test)
# this routine accepts a list of url's where a group of models and pages (i.e.,tabs)
# are presented as web pages.  two url's represent the backend servers where the models
# reside; these servers are accessible directly or indirectly (via the two front end url's)

test = {}

# local server = ["http://127.0.0.1:8000/"]
servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
           "http://134.67.114.3/ubertool/", "http://134.67.114.1/ubertool/"]

#models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
#          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
#          "kabam/", "pfam/", "sam/", "therps/", "trex2/"]
models = ["sip/", "stir/", "pfam/", "earthworm/"] # this short list is used for debugging

# The following list represents the model output page titles to be checked (order of models
# needs to be the same as "models" list above
#models_io = ["SIP", "STIR", "RICE", "TerrPlant", "IEC",
#             "AgDrift", "AgDrift & T-REX", "AgDrift & T-HERPS", "Earthworm",
#             "KABAM", "PFAM", "SAM", "T-Herps", "T-REX 1.5.2"]
models_io = ["SIP", "STIR", "PFAM", "Earthworm"] # this short list is used for debugging

# these two servers require login/authentication for inputs
redirect_servers = ["http://qed.epa.gov/ubertool/", "http://134.67.114.3/ubertool/"]
redirect_pages = ["input"]  # user is redirected to login page for inputs
redirect_model_pages = [s + m + p for s in redirect_servers for m in models
                        for p in redirect_pages]
redirect_models = models_io * len(redirect_servers)

qaqc_pages = ["qaqc"]
qaqc_model_pages = [s + m + p for s in servers for m in models for p in qaqc_pages]
qaqc_models = models_io * len(servers) * len(qaqc_pages)

class WaitForPageLoad(object):
    """
    This class provides functionality to ensure that a web page has
    fully loaded upon a click/submit
    """

    def __init__(self, browser):
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
            'Timeout waiting for {}'.format(condition_function.__name__))

    def __exit__(self, *_):
        self.wait_for(self.page_has_loaded)


class TestQAQC(unittest.TestCase, WaitForPageLoad):
    """
    This set of methods represent unit tests for the Ubertool frontend (i.e., what the
    user sees as the web interface).  The tests include:
    1. Login verficcation for model input pages
    2. Verification that Login results in the input data form page loads
    3. Verification that defaults input data form is successfully submitted and
       that the output data is generated and displayed
    4. Automated QAQC run submittal and presentation of results
    Note: the first three tests here are also included in the "test_host_qed.py"
          code; the difference being that the selenium package is used here and
          the mechanize package is used in test_host_qed.py code
    """

    def setup(self):
        pass

    @staticmethod
    def test_qed_authenticate_input():
        try:  # verify successful login and that we land on input page url
            test_name = "Login Authentication "
            current_page = [""] * len(redirect_model_pages)
            expected_page = [""] * len(redirect_model_pages)
            assert_error = False
            for idx, m in enumerate(redirect_model_pages):
                browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
                browser.get(m)
                # login and authenticate
                username = browser.find_element_by_name("username")
                username.send_keys("betatester")
                password = browser.find_element_by_name("password")
                password.send_keys("ubertool")
                with WaitForPageLoad(browser):
                    login = browser.find_element_by_xpath("//form[@name='auth']")
                    login.submit()  # use .click() for individual buttons and .submit() for form submittal
                        #next two lines is alternative technique
                        #LoginButton = browser.find_element_by_class_name("input_button")
                        #LoginButton.click()
                # Verify we have successfully logged in and are now at input page url
                current_page[idx] = str(browser.current_url)
                expected_page[idx] = m
            try:
                npt.assert_array_equal(expected_page, current_page, 'Login Test Failed', True)
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
            browser.quit()
        return

    @staticmethod
    def test_qed_input_form():
        # verify input page contains expected content (we chk page title, e.g., 'SIP Inputs')
        # need to repeat login
        try:
            test_name = "Input Form URL "
            current_title = [""] * len(redirect_model_pages)
            expected_title = [""] * len(redirect_model_pages)
            assert_error = False
            for idx, m in enumerate(redirect_model_pages):
                expected_title[idx] = m + " : " + redirect_models[idx] + " Inputs"
                browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
                browser.get(m)
                # login and authenticate
                username = browser.find_element_by_name("username")
                username.send_keys("betatester")
                password = browser.find_element_by_name("password")
                password.send_keys("ubertool")
                with WaitForPageLoad(browser):
                    login = browser.find_element_by_xpath("//form[@name='auth']")
                    login.submit()  # use .click() for individual buttons and .submit() for form submittal
                # verify that login was successful by checking that inputs page title is rendered
                if browser.page_source.__contains__(redirect_models[idx] + " Inputs"):
                    current_title[idx] = m + " : " + redirect_models[idx] + " Inputs"
                else:
                    current_title[idx] = m + " : " + redirect_models[idx] + " Input Submit Error"
                # build array for reporting table
            try:
                npt.assert_array_equal(expected_title, current_title, 'Input Form Submittal Failed', True)
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
            browser.quit()
        return

    @staticmethod
    def test_qed_output_form():
        try:  # verify proper output page content, i.e., page title
              # need to repeat login, submit default inputs
            test_name = "Input Form Submittal and Output Generation "
            current_title = [""] * len(redirect_model_pages)
            expected_title = [""] * len(redirect_model_pages)
            assert_error = False
            for idx, m in enumerate(redirect_model_pages):
                expected_title[idx] = m.replace("input", "") + " : " + redirect_models[idx] + " Output"
                browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
                browser.get(m)
                # login and authenticate
                username = browser.find_element_by_name("username")
                username.send_keys("betatester")
                password = browser.find_element_by_name("password")
                password.send_keys("ubertool")
                with WaitForPageLoad(browser):
                    login = browser.find_element_by_xpath("//form[@name='auth']")
                    login.submit()  # use .click() for individual buttons and .submit() for form submittal
                # Locate and submit input form (using the default data for now)
                with WaitForPageLoad(browser):
                    locate_submit = browser.find_element_by_xpath("//div[@class='input_right']")
                    try:
                        form_submit = browser.find_element_by_xpath("//button[@class='input_button']")
                    except:
                        form_submit = browser.find_element_by_xpath("//button[@class='submit input_button']")
                    form_submit.submit()  # use .click() for individual buttons and .submit() for form submittal
                if browser.page_source.__contains__("User Inputs"):
                    current_title[idx] = browser.current_url.replace("output", "") + " : " + redirect_models[
                        idx] + " Output"
                elif browser.page_source.__contains__('File Not Found'):
                    current_title[idx] = browser.current_url.replace("output", "") + " : File Not Found Page Error"
                else:
                    current_title[idx] = browser.current_url.replace("output", "") + " : Unknown Output Page Error"
            try:
                npt.assert_array_equal(expected_title, current_title, 'Submittal of Input Failed', True)
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
            browser.quit()
        return

    @staticmethod
    def test_qed_qaqc_form():
        try:
            test_name = "QAQC Execution and Results Generation "
            current_page_id = [""] * len(qaqc_model_pages)  # pageID = url + <h2 class='model header' string>
            expected_page_id = [""] * len(qaqc_model_pages)
            assert_error = False
            browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
            # added the argument service_log_path=os.path.devnull to the function webdriver.PhantomJS()
            # to prevent PhantomJS from creating a ghostdriver.log in the directory of the python file
            # being executed.
            for idx, m in enumerate(qaqc_model_pages):
                expected_page_id[idx] = m + "/run : " + qaqc_models[idx] + " QAQC"
                browser.get(m)
                try:
                    with WaitForPageLoad(browser):
                        qaqc_run_button = browser.find_element_by_id('runQAQC')
                        qaqc_run_button.click()
                    if browser.current_url.__str__() != m + "/run":
                        current_page_id[idx] = str(
                            browser.current_url) + " : Run QAQC failed"  # we did not arrive at expected url
                    elif browser.page_source.__contains__('File Not Found'):
                        current_page_id[idx] = str(browser.current_url) + " : File Not Found Page Error"
                    elif browser.page_source.__contains__("User Inputs"):
                        # check to see of string User Inputs appears on page
                        current_page_id[idx] = m + "/run : " + qaqc_models[idx] + " QAQC"
                    else:
                        current_page_id[idx] = str(browser.current_url) + " Unknown QAQC run error"
                except:
                    current_page_id[idx] = m + " Unknown exception thrown"
                # build array for reporting table
            try:
                npt.assert_array_equal(expected_page_id, current_page_id, 'QAQC Failed', True)
            except AssertionError:
                assert_error = True
            except Exception as e:
                # handle any other exception
                print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, expected_page_id, current_page_id)
            browser.quit()
        return

    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main()
