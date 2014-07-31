"""
.. module:: przm_batchoutput
   :synopsis: A useful module indeed.
"""

from django.views.decorators.http import require_POST
from StringIO import StringIO
import przm_model, przm_tables
import csv
from threading import Thread
import Queue
from collections import OrderedDict
import logging
import przm_batchmodel
import datetime, time


def generate_batch_jid():
    ts = datetime.datetime.now()
    if(time.daylight):
        ts1 = datetime.timedelta(hours=-4)+ts
    else:
        ts1 = datetime.timedelta(hours=-5)+ts
    batch_jid = ts1.strftime('%Y%m%d%H%M%S%f')
    return batch_jid


@require_POST
def przmBatchOutputPage(request):
    thefile = request.FILES['upfile']
    batch_jid = generate_batch_jid()
    iter_html = przm_batchmodel.loop_html(thefile, batch_jid)
    
    logging.info(iter_html)
    # return iter_html, trex2_obj_all, batch_jid


# class przmBatchOutputPage(webapp.RequestHandler):
#     def post(self):
#         form = cgi.FieldStorage()
#         thefile = form['file-0']
#         przm_batchmodel.loop_html(thefile, generate_batch_jid())
#         templatepath = os.path.dirname(__file__) + '/../templates/'
#         ChkCookie = self.request.cookies.get("ubercookie")
#         html = template.render(templatepath + '04uberoutput_start.html', {
#                 'model':'przm',
#                 'model_attributes':'PRZM Batch Output'})
#         self.response.out.write(html)

# app = webapp.WSGIApplication([('/.*', przmBatchOutputPage)], debug=True)


# def main():
#     run_wsgi_app(app)

# if __name__ == '__main__':
#     main()
