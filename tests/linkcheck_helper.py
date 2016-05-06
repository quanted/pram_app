import requests


def build_http_links(root_url, href_list):
    # function receives root_url (e.g., http://qed.epa.gov) and a list of link references
    # from a qed page (representing e.g., the list of models, links to other sites, etc.)
    # function processes the list of link references and builds a complete url
    url_list = [""] * len(href_list)
    for idx, link in enumerate(href_list):
        url_list[idx] = link.get('href')
        if url_list[idx][0:5] == 'http:':
            url_list[idx] = url_list[idx]
        elif (url_list[idx][0] == '/'):
            url_list[idx] = root_url + url_list[idx]
        else:
            url_list[idx] = root_url + '/ubertool' + '/' + url_list[idx]
    return url_list

def status_chk(url_list):
    # function tests access status for a list of url's, returning a status report
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