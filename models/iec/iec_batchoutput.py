# # -*- coding: utf-8 -*-
from django.views.decorators.http import require_POST
import csv
import iec_model, iec_tables
import logging
from threading import Thread
import Queue
from collections import OrderedDict

logger = logging.getLogger('IECBatchPage')
dose_response = []
LC50 = []
threshold = []

######Pre-defined outputs########
z_score_f_out = []
F8_f_out = []
chance_f_out = []
jid_all = []
jid_batch = []
iec_obj_all = []
iec_obj_temp = []

def html_table(row_inp,iter):
    logger.info("iteration: " + str(iter))
    dose_response.append(float(row_inp[0]))
    LC50.append(float(row_inp[1]))
    threshold.append(float(row_inp[2]))

    Input_header="""<div class="out_">
                        <br><H3>Batch Calculation of Iteration %s</H3>
                    </div>"""%(iter)

    iec_obj_temp = iec_model.iec(True,True, 'batch',dose_response[iter-1],LC50[iter-1],threshold[iter-1])
    iec_obj_temp.loop_indx = str(iter)
    z_score_f_out.append(iec_obj_temp.z_score_f_out)
    F8_f_out.append(iec_obj_temp.F8_f_out)
    chance_f_out.append(iec_obj_temp.chance_f_out)
    jid_all.append(iec_obj_temp.jid)
    iec_obj_all.append(iec_obj_temp)    
    if iter == 1:
        jid_batch.append(iec_obj_temp.jid)
    table_all_out = iec_tables.table_all(iec_obj_temp)
    html_table_temp = Input_header + table_all_out + "<br>"

    return html_table_temp
                
def loop_html(thefile):
    reader = csv.reader(thefile.file.read().splitlines())
    header = reader.next()
    logger.info(header)
    i=1
    iter_html_temp=""
    for row in reader:
        iter_html_temp = iter_html_temp +html_table(row,i)
        i=i+1

    sum_html = iec_tables.table_all_sum(dose_response,LC50,threshold,
                    z_score_f_out, F8_f_out, chance_f_out)
    return sum_html+iter_html_temp

@require_POST
def iecBatchOutputPage(request):
    thefile = request.FILES['upfile']
    iter_html=loop_html(thefile)

    return iter_html, iec_obj_all, jid_batch
