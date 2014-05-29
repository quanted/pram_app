# -*- coding: utf-8 -*-
from django.views.decorators.http import require_POST
import csv
import earthworm_model, earthworm_tables
import logging
from threading import Thread
import Queue
from collections import OrderedDict
logger = logging.getLogger("SIPBatchOutput")

######Pre-defined inputs########
Kow=[]
L=[]
Cs=[]
Kd=[]
Ps=[]
Cw=[]
MW=[]
Pe=[]

######Pre-defined outputs########
Ce_out=[]

jid_all = []
jid_batch = []
earthworm_all = []
all_threads = []
out_html_all = {}
job_q = Queue.Queue()
thread_count = 10

logger = logging.getLogger("earthwormBatchOutput")

def html_table(row_inp_all):
    while True:
        row_inp_temp_all = row_inp_all.get()
        if row_inp_temp_all is None:
            break
        else:
            row_inp = row_inp_temp_all[0]
            iter = row_inp_temp_all[1]


            Kow_temp=float(row_inp[0])
            Kow.append(Kow_temp)
            L_temp=float(row_inp[1])
            L.append(L_temp)
            Cs_temp=float(row_inp[2])
            Cs.append(Cs_temp)
            Kd_temp=float(row_inp[3])
            Kd.append(Kd_temp)
            Ps_temp=float(row_inp[4])
            Ps.append(Ps_temp)
            Cw_temp=float(row_inp[5])        
            Cw.append(Cw_temp)
            MW_temp=float(row_inp[6])   
            MW.append(MW_temp)
            Pe_temp=float(row_inp[7])
            Pe.append(Pe_temp)
    
            earth = earthworm_model.earthworm(True,True,Kow_temp,L_temp,Cs_temp,Kd_temp,Ps_temp,Cw_temp,MW_temp,Pe_temp)
            logger.info("===============")
            Ce_temp=earth.earthworm_fugacity_out
            Ce_out.append(Ce_temp)

            jid_all.append(earth.jid)
            earthworm_all.append(earth)    
            if iter == 1:
                jid_batch.append(earth.jid)

            batch_header = """
                <div class="out_">
                    <br><H3>Batch Calculation of Iteration %s:</H3>
                </div>
                """%(iter)

            html_temp = earthworm_tables.table_all_batch(earthworm_tables.pvuheadings,earthworm_tables.sumheadings,earthworm_tables.tmpl, earth)
            out_html_temp = batch_header + html_temp
            out_html_all[iter]=out_html_temp


                
def loop_html(thefile):
    reader = csv.reader(thefile.file.read().splitlines())
    header = reader.next()
    # logger.info(header)
    ####Create a job queue and add each row of batch temeplate file as a task into it
    i=1
    for row in reader:
        job_q.put([row, i])
        i=i+1

    all_threads = [Thread(target=html_table, args=(job_q, )) for j in range(thread_count)]
    for x in all_threads:
        x.start()
    for x in all_threads:
        job_q.put(None)
    for x in all_threads:
        x.join()


    html_timestamp = earthworm_tables.timestamp("", jid_batch[0])
    out_html_all_sort = OrderedDict(sorted(out_html_all.items()))
    sum_html = earthworm_tables.table_all_sum(earthworm_tables.sumheadings, earthworm_tables.tmpl, Kow, L, Cs, Kd, Ps, Cw, MW, Pe, 
                    Ce_out)
    
    return  html_timestamp + sum_html + "".join(out_html_all_sort.values())


@require_POST
def earthwormBatchOutputPage(request):
    thefile = request.FILES['upfile']
    iter_html=loop_html(thefile)

    return iter_html, earthworm_all, jid_batch
