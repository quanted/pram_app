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
    """
    This class includes tests of links referenced on the Ubertool MainPage
    Individual tests identify links that are included in different portions of
    the main page (e.g., left column, main article) and attempt to navigate to the
    link and verify that it is responding (as opposed to coming up with a dead link
    or a file not found, etc.
    """
    def setup(self):
        pass

    def teardown(self):
        pass

    @staticmethod
    def test_qed_bannerlinks():
        test_name = "Test of Ubertool Mainpage Banner Links "
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                div_tags_banner = soup_content.find_all('div', {'id': 'banner'})
                # assuming a single div/id by this name
                banner_links = div_tags_banner[0].find_all('a')
                if banner_links:
                    assert_error = False
                    link_url = [""] * len(banner_links)
                    status = [""] * len(banner_links)
                    link_url = linkcheck_helper.build_http_links(main_server, banner_links)
                    status = linkcheck_helper.status_chk(link_url)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except AssertionError:
                        assert_error = True
                    except Exception as e:
                        # handle any other exception
                        print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
             linkcheck_helper.write_report(test_name, assert_error, link_url, status)
        return

    @staticmethod
    def test_qed_headerrgtlinks():
        test_name = "Test of Ubertool Mainpage Righthand Header Links "
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                div_tags_header_rgt = soup_content.find_all('div', {'id': 'header_menu_r'})
                # assuming a single div/id by this name
                header_links = div_tags_header_rgt[0].find_all('a')
                if header_links:
                    assert_error = False
                    link_url = [""] * len(header_links)
                    status = [""] * len(header_links)
                    link_url = linkcheck_helper.build_http_links(main_server, header_links)
                    status = linkcheck_helper.status_chk(link_url)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except AssertionError:
                        assert_error = True
                    except Exception as e:
                        # handle any other exception
                        print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, link_url, status)
        return

    @staticmethod
    def test_qed_leftlinks():
        test_name = "Test of Ubertool Mainpage Left Column Links "
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                div_tags_left = soup_content.find_all('div', {'class': 'left'})
                # assuming a single div/class by this name
                left_links = div_tags_left[0].find_all('a')
                if left_links:
                    assert_error = False
                    link_url = [""] * len(left_links)
                    status = [""] * len(left_links)
                    link_url = linkcheck_helper.build_http_links(main_server, left_links)
                    status = linkcheck_helper.status_chk(link_url)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except AssertionError:
                        assert_error = True
                    except Exception as e:
                        # handle any other exception
                        print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, link_url, status)
        return

    @staticmethod
    def test_qed_mainpagelinks():
        test_name = "Test of Ubertool Mainpage Article Links "
        try:  # verify that all links on a model page (main article section) produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                div_tags_article = soup_content.find_all('div', {'class': 'articles'})
                # assuming a single div/class by this name
                article_links = div_tags_article[0].find_all('a')
                if article_links:
                    assert_error = False
                    link_url = [""] * len(article_links)
                    status = [""] * len(article_links)
                    link_url = linkcheck_helper.build_http_links(main_server, article_links)
                    status = linkcheck_helper.status_chk(link_url)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except AssertionError:
                        assert_error = True
                    except Exception as e:
                        # handle any other exception
                        print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, link_url, status)
        return

    @staticmethod
    def test_qed_rightlinks():
        test_name = "Test of Ubertool Mainpage Right Column Links "
        try:  # verify that all links on a model page produce status code of 200
            for main_server in servers:
                response = requests.get(main_server + "/ubertool")
                soup_content = BeautifulSoup(response.content, "html.parser")
                div_tags_right = soup_content.find_all('div', {'class': 'right'})
                # assuming a single div/class by this name
                right_links = div_tags_right[0].find_all('a')
                if right_links:
                    assert_error = False
                    link_url = [""] * len(right_links)
                    status = [""] * len(right_links)
                    link_url = linkcheck_helper.build_http_links(main_server, right_links)
                    status = linkcheck_helper.status_chk(link_url)
                    try:
                        npt.assert_array_equal(status, 200, '200 error', True)
                    except AssertionError:
                        assert_error = True
                    except Exception as e:
                        # handle any other exception
                        print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        except Exception as e:
            # handle any other exception
            print "Error '{0}' occured. Arguments {1}.".format(e.message, e.args)
        finally:
            linkcheck_helper.write_report(test_name, assert_error, link_url, status)
        return

if __name__ == '__main__':
    unittest.main()
