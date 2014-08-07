"""
.. module:: sam_model
   :synopsis: A useful module indeed.
"""

from REST import auth_s3#, rest_funcs
import json
import logging
logger = logging.getLogger('SIP Model')
import os
import requests
import datetime

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']