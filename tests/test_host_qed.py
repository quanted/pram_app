import requests
import unittest
import numpy.testing as npt

test = {}

rooturl_qed = ["http://qed.epa.gov/ubertool/"]
rooturl_qedinternal = ["http://qedinternal.epa.gov/ubertool/"]
models = ["sip/", "stir/", "rice/", "terrplant/"]
pages = ["", "description"]

model_pages_qed = [r + m + p for r in rooturl_qed for m in models for p in pages]
print(model_pages_qed)

model_pages_qedinternal = [r + m + p for r in rooturl_qedinternal for m in models for p in pages]
print(model_pages_qedinternal)

class TestSipClient(unittest.TestCase):
    def setup(self):
        pass

    def test_qed(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_qed]
            #print(response.status_code)
            #npt.assert_array_equal(3, 3, '', True)
            npt.assert_array_equal(response, 200, '200 error', True)
        finally:
            pass
        return

    def test_qedinternal(self):
        try:
            response = [requests.get(m).status_code for m in model_pages_qedinternal]
            #print(response.status_code)
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
