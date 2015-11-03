import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):
        #create a firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        #go to qed
        self.driver.get("http://qed.epa.gov/ubertool/sip")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)

