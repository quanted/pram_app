import requests
from bs4 import BeautifulSoup
import numpy.testing as npt
import unittest
from tabulate import tabulate
import linkcheck_helper


main_server = ["http://qed.epa.gov/ubertool/", "http://qedinternal.epa.gov/ubertool/"]
models = ["sip/", "stir/", "rice/", "terrplant/",  "iec/",
          "agdrift/", "agdrift_trex/", "agdrift_therps/", "earthworm/",
          "kabam/", "pfam/", "sam/", "therps/", "trex2/"]
#models = ["sip/", "stir/", "pfam/", "earthworm/"]
pages = ["descriptions","references"]

model_tab_pages = [s + m + p for s in main_server for m in models for p in pages]

class TestTabLinks(unittest.TestCase):
    def setup(self):
        pass

    def test_qed_mainpagelinks(self):
            try:  # verify that all links on a model page (main article section) produce status code of 200
                for page in model_tab_pages:
                    response = requests.get(page)
                    soup_content = BeautifulSoup(response.content, "html.parser")
                    divTagsArticle = soup_content.find_all('div', {'class': 'articles'})
                    # assuming a single div/class by this name
                    if len(divTagsArticle) > 0:
                        articleLinks = divTagsArticle[0].find_all('a')
                        if len(articleLinks) > 0:
                            linkUrl = [""] * len(articleLinks)
                            status = [""] * len(articleLinks)
                            report = [""] * len(articleLinks)
                            linkUrl = linkcheck_helper.build_http_links(page, articleLinks)
                            #linkUrl = self.build_http_links(main_server, articleLinks);
                            status = linkcheck_helper.status_chk(linkUrl)
                            try:
                                npt.assert_array_equal(status, 200, '200 error', True)
                            except:
                                print "Error in one or more main article links"
                                report = linkcheck_helper.build_table(linkUrl, status)
                                headers = ["Article Link URL", "Status Code"]
                                print tabulate(report, headers, tablefmt='grid')
            finally:
                pass
            return

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()