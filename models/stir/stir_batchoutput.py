"""
.. module:: stir_batchoutput
   :synopsis: A useful module indeed.
"""

import logging

from django.views.decorators.http import require_POST


def read_batch_csv(csv):
    import pandas as pd

    logging.info("===== stir_batchoutput.read_batch_csv")
    pd_obj = pd.read_csv(csv, index_col=0, header=None, skiprows=1, 
        skip_footer=22, engine='python')
    logging.info("===== reading stir batch csv")
    logging.info(pd_obj)
    pd_obj = pd_obj.drop(labels=pd_obj.columns[range(4)], axis=1)
    pd_obj.index.name = None
    pd_obj.columns = pd_obj.columns - 5

    return pd_obj

@require_POST
def stirBatchOutputPage(request):
    
    logging.info("==== stir_batchoutput.stirBatchOutputPage")
    csv = request.FILES['upfile']
    pd_obj = read_batch_csv(csv)
    logging.info(pd_obj)

    return pd_obj