import requests
from tabulate import tabulate


def build_http_links(root_url, href_list):
    # function receives root_url (e.g., http://qed.epa.gov) and a list of link references
    # from a qed page (representing e.g., the list of models, links to other sites, etc.)
    # function processes the list of link references and builds a complete url
    url_list = [""] * len(href_list)
    for idx, link in enumerate(href_list):
        url_list[idx] = link.get('href')
        if not url_list[idx]:  #check to ensure a link is actually populated
            url_list[idx] = "No link available"
        elif url_list[idx][0:4] == 'http':
            url_list[idx] = url_list[idx]
        elif (url_list[idx][0] == '/'):
            url_list[idx] = root_url + url_list[idx]
        else:
            url_list[idx] = root_url + '/ubertool' + '/' + url_list[idx]
    return url_list

def status_chk(url_list):
    # function tests access status for a list of url's, returning a status per url
    status = [200] * len(url_list)
    for idx, link in enumerate(url_list):
        try:
            status[idx] = requests.get(link).status_code
        except:
            status[idx] = 999
    return status

def build_table(list1, list2):
    # function builds a two column table containing url's and status codes
    report = [""] * len(list1)
    for idx, item in enumerate(list1):
        report[idx] = [list1[idx], list2[idx]]
    return report

def write_report(test_name, assert_error, col1, col2):
    if assert_error:
        print test_name + "Test failed for one or more instances"
        report = build_table(col1, col2)
        headers = ["expected", "actual"]
        print tabulate(report, headers, tablefmt='grid')
    else:
        print test_name + "Test completed successfully"
        report = build_table(col1, col2)
        headers = ["expected", "actual url or status"]
        print tabulate(report, headers, tablefmt='grid')
    return