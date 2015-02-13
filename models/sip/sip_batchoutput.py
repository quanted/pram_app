"""
.. module:: sip_batchoutput
   :synopsis: A useful module indeed.
"""

from django.views.decorators.http import require_POST
import logging


def read_batch_csv(csv):
    import pandas as pd

    pd_obj = pd.read_csv(csv, index_col=1, header=None, skiprows=1, skip_footer=32, engine='python')
    logging.info(pd_obj)
    pd_obj = pd_obj.drop(labels=pd_obj.columns[range(4)], axis=1)
    pd_obj.index.name = None
    pd_obj.columns = pd_obj.columns - 5

    return pd_obj

@require_POST
def sipBatchOutputPage(request):
    
    csv = request.FILES['upfile']
    pd_obj = read_batch_csv(csv)


    return pd_obj