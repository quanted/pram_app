import requests
import unittest
import numpy.testing as npt

test = {}

rooturl = ["http://qed.epa.gov/ubertool/"]
models = ["sip/", "stir/"]
pages = [""]

model_pages = [r + m + p for r in rooturl for m in models for p in pages]
print(model_pages)

class TestSipClient(unittest.TestCase):
    def setup(self):
        pass

    def test_description(self):
        try:
            response = [requests.get(m).status_code for m in model_pages]
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
