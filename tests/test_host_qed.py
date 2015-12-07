import requests
import unittest
import numpy.testing as npt
from bs4 import BeautifulSoup


#this testing routine accepts a list of models and pages (tabs
test = {}

rooturl_qed = ["http://qed.epa.gov/ubertool/"]
rooturl_qedinternal = ["http://qedinternal.epa.gov/ubertool/"]
#models = ["asdf/", "sip/", "stir/", "rice/", "terrplant/", "trex2/", "therps/", "iec/",
 #         "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
  #        "rice/", "kabam/", "pfam/", "sam/"]
models = ["asdf/", "sip/"]
pages = ["", "description", "input", "algorithms", "references", "qaqc",
         "batchinput", "history"]

model_pages_qed = [r + m + p for r in rooturl_qed for m in models for p in pages]
#print(model_pages_qed)

model_pages_qedinternal = [r + m + p for r in rooturl_qedinternal for m in models for p in pages]
#print(model_pages_qedinternal)

class TestQEDHost(unittest.TestCase):
    def setup(self):
        pass

    def test_qed(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_qed]
            print(response)
            #print(response.status_code)
            #npt.assert_array_equal(3, 3, '', True)
            npt.assert_array_equal(response, 200, '200 error', True)
        finally:
            pass
        return

    def test_qed_404(self):
        try:
            response = [requests.get(m) for m in model_pages_qed]
            #print(response[6].content)
            #beautiful soup to check the web page content
            #soup = BeautifulSoup(r) for r in response.content
            #vectorize
            soup_content = [BeautifulSoup(r.content, "html.parser") for r in response]
            #soup = BeautifulSoup(response[15].content, "html.parser")
            #print (response[3].content)
            soup_N404s = [len(s.findAll('img',src='/static/images/404error.png')) for s in soup_content]
            #boo404 = (len(soup_content.findAll('img',src='/static/images/404error.png'))>0)
            boo404 = [s>0 for s in soup_N404s]
            # print boo404
            npt.assert_array_equal(boo404, True)
            #soup.find('/static/images/404error.png')
            #soup.find('/static/images/404error.png')
            #if ErrorFound:
            #    print (response)
            #boolean
            #npt.assert_array_equal(response, '/static/images/404error.png', '404 error', True)
            #npt.assert_array_equal(response, 200, '200 error', True)
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

    def teardown(self):
        pass

# unittest will
# 1) call the setup method,
# 2) then call every method starting with "test",
# 3) then the teardown method
if __name__ == '__main__':
    unittest.main()
