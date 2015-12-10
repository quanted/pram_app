import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup


#this testing routine accepts a list of models and pages (tabs
test = {}

rooturl_qed = ["http://qed.epa.gov/ubertool/"]
rooturl_qedinternal = ["http://qedinternal.epa.gov/ubertool/"]
rooturl_ippublic = ["http://134.67.114.3/ubertool"]
rooturl_ipintranet = ["http://134.67.114.1/"]
rooturl_test = ["http://google.com"]

models = ["asdf", "sip/", "stir/", "rice/", "terrplant/", "trex2/", "therps/", "iec/",
          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
          "rice/", "kabam/", "pfam/", "sam/"]
pages = ["", "description", "input", "algorithms", "references", "qaqc",
         "batchinput", "history"]

model_pages_qed = [r + m + p for r in rooturl_qed for m in models for p in pages]
#print(model_pages_qed)

model_pages_qedinternal = [r + m + p for r in rooturl_qedinternal for m in models for p in pages]
#print(model_pages_qedinternal)

model_pages_ipintranet = [r + m + p for r in rooturl_ipintranet for m in models for p in pages]

model_pages_ippublic = [r + m + p for r in rooturl_ippublic for m in models for p in pages]

class TestQEDHost(unittest.TestCase):
    def setup(self):
        pass

    def test_url(self):
        try:
            re = [requests.get(m).status_code, "http://googl.com"]
            print re
        finally:
            pass
        return

    def test_qed_200(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_qed]
            npt.assert_array_equal(response, 200, '200 error', True)
        finally:
            pass
        return

    def test_qed_redirect(self):
        try:
            response = [requests.get(m).is_redirect for m in model_pages_qed]
            resp = [requests.get(m).status_code for m in model_pages_qed]
            npt.assert_array_equal(response, False, '302 error', True)
        finally:
            pass
        return

    def test_qed_404(self):
        try:
            response = [requests.get(m) for m in model_pages_qed]
            soup_content = [BeautifulSoup(r.content, "html.parser") for r in response]
            soup_N404s = [len(s.findAll('img',src='/static/images/404error.png')) for s in soup_content]
            boo404 = [s>0 for s in soup_N404s]
            npt.assert_array_equal(boo404, False, '404 error', True)
        finally:
            pass
        return

    def test_qedinternal(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_qedinternal]
            print(response)
            #npt.assert_array_equal(3, 3, '', True)
            npt.assert_array_equal(response, 200, '200 error', True)
        finally:
            pass
        return

    def test_ipintranet(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_ipintranet]
            print(response)
            #npt.assert_array_equal(3, 3, '', True)
            npt.assert_array_equal(response, 200, '200 error', True)
        finally:
            pass
        return

    def test_ippublic(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_ippublic]
            print(response)
            #npt.assert_array_equal(3, 3, '', True)
            npt.assert_array_equal(response, 200, '200 error', True)
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
