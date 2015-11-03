import requests
import unittest

test = {}

class TestSipClient(unittest.TestCase):
    def setup(self):
        pass

    def test_description(self):
        try:
            response = requests.get("http://qed.epa.gov/ubertool/sip")
            print(response.status_code)
            self.assertEqual(200, response.status_code)
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