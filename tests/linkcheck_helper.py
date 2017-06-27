import datetime
import requests
import time
from tabulate import tabulate


def build_table(list1, list2):
    # function builds a two column table containing url's and status codes
    report = [""] * len(list1)
    for idx, item in enumerate(list1):
        report[idx] = [list1[idx], list2[idx]]
    return report

def write_report(test_name, assert_error, col1, col2, start_time):
    try:
        if assert_error:
            test_out = test_name + "Test failed for one or more instances"
            print(test_out)
            report = build_table(col1, col2)
            headers = ["expected", "actual"]
            print(tabulate(report, headers, tablefmt='grid'))
        else:

            report = build_table(col1, col2)
            headers = ["expected", "actual url or status"]
            print(tabulate(report, headers, tablefmt='grid'))
    except:
        print('report error in test')
    finally:
        end_time = datetime.datetime.utcnow()
        print(str(end_time))
        print("Time elapsed = " + str((end_time-start_time).seconds) + " seconds")
    return