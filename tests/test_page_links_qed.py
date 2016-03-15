import requests
from bs4 import BeautifulSoup
import numpy.testing as npt
import unittest
from tabulate import tabulate
import linkcheck_helper

#this routine scans the main ubertool page for url links and verifies that they respond
#these links are repeated (as a template of sorts) on all model pages; but tested here only

servers = ["http://qed.epa.gov", "http://qedinternal.epa.gov"]

class TestPageLinks(unittest.TestCase):
    def setup(self):
        pass

    def test_qed_bannerlinks(self):
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                divTagsBanner = soup_content.find_all('div', {'id': 'banner'})
                bannerLinks = divTagsBanner[0].find_all('a')
                if bannerLinks > 0:
                    linkUrl = [""] * len(bannerLinks)
                    status = [""] * len(bannerLinks)
                    report = [""] * len(bannerLinks)
                    linkUrl = linkcheck_helper.build_http_links(main_server, bannerLinks)
                    status = linkcheck_helper.status_chk(linkUrl)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except:
                        print "Error in one or more banner links"
                        report = linkcheck_helper.build_table(linkUrl, status)
                        headers = ["Banner Link URL", "Status Code"]
                        print tabulate(report, headers, tablefmt='grid')
        finally:
             pass
        return

    def test_qed_headerrgtlinks(self):
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                divTagsHeaderRgt = soup_content.find_all('div', {'id': 'header_menu_r'})
                headerLinks = divTagsHeaderRgt[0].find_all('a')
                if headerLinks > 0:
                    linkUrl = [""] * len(headerLinks)
                    status = [""] * len(headerLinks)
                    report = [""] * len(headerLinks)
                    linkUrl = linkcheck_helper.build_http_links(main_server, headerLinks)
                    status = linkcheck_helper.status_chk(linkUrl)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except:
                        print "Error in one or more header links"
                        report = linkcheck_helper.build_table(linkUrl, status)
                        headers = ["Header Link URL", "Status Code"]
                        print tabulate(report, headers, tablefmt='grid')
        finally:
            pass
        return

    def test_qed_leftlinks(self):
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                divTagsLeft = soup_content.find_all('div', {'class': 'left'})
                leftLinks = divTagsLeft[0].find_all('a')
                if leftLinks > 0:
                    linkUrl = [""] * len(leftLinks)
                    status = [""] * len(leftLinks)
                    report = [""] * len(leftLinks)
                    linkUrl = linkcheck_helper.build_http_links(main_server, leftLinks)
                    status = linkcheck_helper.status_chk(linkUrl)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except:
                        print "Error in one or more left links"
                        report = linkcheck_helper.build_table(linkUrl, status);
                        headers = ["Left Link URL", "Status Code"]
                        print tabulate(report, headers, tablefmt='grid')
        finally:
            pass
        return

    def test_qed_rightlinks(self):
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                divTagsRight = soup_content.find_all('div', {'class': 'right'})
                rightLinks = divTagsRight[0].find_all('a')
                if rightLinks > 0:
                    linkUrl = [""] * len(rightLinks)
                    status = [""] * len(rightLinks)
                    report = [""] * len(rightLinks)
                    linkUrl = linkcheck_helper.build_http_links(main_server, rightLinks);
                    status = linkcheck_helper.status_chk(linkUrl);
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except:
                        print "Error in one or more right links"
                        report = linkcheck_helper.build_table(linkUrl, status);
                        headers = ["Right Link URL", "Status Code"]
                        print tabulate(report, headers, tablefmt='grid')
        finally:
            pass
        return

    def test_qed_mainpagelinks(self):
        try:  # verify that all links on a model page (main article section) produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                divTagsArticle = soup_content.find_all('div', {'class': 'articles'})
                # assuming a single div/class by this name
                articleLinks = divTagsArticle[0].find_all('a')
                if articleLinks > 0:
                    linkUrl = [""] * len(articleLinks)
                    status = [""] * len(articleLinks)
                    report = [""] * len(articleLinks)
                    linkUrl = linkcheck_helper.build_http_links(main_server, articleLinks);
                    status = linkcheck_helper.status_chk(linkUrl);
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except:
                        print "Error in one or more main article links"
                        report = linkcheck_helper.build_table(linkUrl, status);
                        headers = ["Article Link URL", "Status Code"]
                        print tabulate(report, headers, tablefmt='grid')
        finally:
            pass
        return

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()
