import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup


#this testing routine accepts a list of models and pages (tabs
test = {}

servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
           "http://134.67.114.3/ubertool", "http://134.67.114.1/"]
models = ["sip/", "stir/", "rice/", "terrplant/", "trex2/", "therps/", "iec/",
          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
          "rice/", "kabam/", "pfam/", "sam/"]
pages = ["", "description", "input", "algorithms", "references", "qaqc",
         "batchinput", "history"]

model_pages = [s + m + p for s in servers for m in models for p in pages]
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
            response = [requests.get(m).history for m in model_pages]
            npt.assert_array_equal(response, "[<Response [302]>]",
                                   '302 temporary redirect', True)
        finally:
            pass
        return

    def test_qed_404(self):
        try:
            response = [requests.get(m) for m in model_pages]
            soup_content = [BeautifulSoup(r.content, "html.parser") for r in response]
            soup_N404s = [len(s.findAll('img',src='/static/images/404error.png')) for s in soup_content]
            boo404 = [s>0 for s in soup_N404s]
            npt.assert_array_equal(boo404, False, '404 error', True)
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
