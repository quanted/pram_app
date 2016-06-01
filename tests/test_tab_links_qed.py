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
    """
    this routine tests url links on individual model page tabs; including the description
    and references tabs  -- other links on the model page (e.g., left column, right column)
    are not unique to models and are tested in test_page_links_qed.py
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    @staticmethod
    def test_qed_mainpagelinks():
        try:  # verify that all links on a model page (main article section) produce status code of 200
            test_name = "Model Mainpage Article Links "
            for page in model_tab_pages:
                response = requests.get(page)
                soup_content = BeautifulSoup(response.content, "html.parser")
                div_tag_article = soup_content.find_all('div', {'class': 'articles'})
                # assuming a single div/class by this name
                if div_tag_article:
                    article_links = div_tag_article[0].find_all('a')
                    if article_links:
                        link_url = [""] * len(article_links)
                        status = [""] * len(article_links)
                        link_url = linkcheck_helper.build_http_links(page, article_links)
                        status = linkcheck_helper.status_chk(link_url)
                        try:
                            npt.assert_array_equal(status, 200, '200 error', True)
                        except AssertionError:
                            assert_error = True
                        except Exception as e:
                            # handle any other exception
                            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
                        finally:
                            linkcheck_helper.write_report(test_name, assert_error, link_url, status)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        return

if __name__ == '__main__':
    unittest.main()