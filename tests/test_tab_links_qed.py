import requests
from bs4 import BeautifulSoup
import numpy.testing as npt
import unittest
from tabulate import tabulate
import test_page_links_qed

test_page_links_qed
main_server = "http://qed.epa.gov/ubertool/"
#servers = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/",
#           "http://134.67.114.3/ubertool/", "http://134.67.114.1/ubertool/"]
#models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
#          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
#          "kabam/", "pfam/", "sam/", "therps/", "trex2/"]
models = ["sip/", "stir/", "pfam/", "earthworm/"]
#pages = ["", "description", "input", "algorithms", "references", "qaqc",
#         "batchinput", "history"]
pages = ["", "description", "references"]

model_tab_pages = [s + m + p for s in main_server for m in models for p in pages]

class TestTabLinks(unittest.TestCase):
    def setup(self):
        pass

    def test_qed_mainpagelinks(self):
        for page in model_tab_pages:
            try:  # verify that all links on a model page (main article section) produce status code of 200
                response = requests.get(page)
                soup_content = BeautifulSoup(response.content, "html.parser")
                divTagsArticle = soup_content.find_all('div', {'class': 'articles'})
                # assuming a single div/class by this name
                articleLinks = divTagsArticle[0].find_all('a')
                linkUrl = [""] * len(articleLinks)
                status = [""] * len(articleLinks)
                report = [""] * len(articleLinks)
                linkUrl = self.build_http_links(main_server, articleLinks);
                status = self.status_chk(linkUrl);
                try:
                    npt.assert_array_equal(status, 200, '200 error', True)
                except:
                    print "Error in one or more main article links"
                    report = self.build_table(linkUrl, status);
                    headers = ["Article Link URL", "Status Code"]
                    print tabulate(report, headers, tablefmt='grid')
            finally:
                pass
            return

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()