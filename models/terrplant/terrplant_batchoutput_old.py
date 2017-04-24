"""
.. module:: terrplant_batchoutput
   :synopsis: A useful module indeed.
"""

import Queue
import csv
import logging
from collections import OrderedDict
from threading import Thread

import terrplant_model
import terrplant_tables
from django.views.decorators.http import require_POST

application_rate=[]
incorporation_depth=[]
runoff_fraction=[]
drift_fraction=[]
ec25_nonlisted_seedling_emergence_monocot=[]
ec25_nonlisted_seedling_emergence_dicot=[]
noaec_listed_seedling_emergence_monocot=[]
noaec_listed_seedling_emergence_dicot=[]

######Pre-defined outputs########
rundry_out = []
runsemi_out = []
spray_out = []
totaldry_out = []
totalsemi_out = []
nms_rq_dry_out = []
LOCnmsdry_out = []
nms_rq_semi_out = []
LOCnmssemi_out = []
nms_rq_spray_out = []
LOCnmsspray_out = []
lms_rq_dry_out = []
LOClmsdry_out = []
lms_rq_semi_out = []
LOClmssemi_out = []
lms_rq_spray_out = []
LOClmsspray_out = []
nds_rq_dry_out = []
LOCndsdry_out = []
nds_rq_semi_out = []
LOCndssemi_out = []
nds_rq_spray_out = []
LOCndsspray_out = []
lds_rq_dry_out = []
LOCldsdry_out = []
lds_rq_semi_out = []
LOCldssemi_out = []
lds_rq_spray_out = []
LOCldsspray_out = []

jid_all = []
jid_batch = []
terr_all = []
all_threads = []
out_html_all = {}
job_q = Queue.Queue()
thread_count = 10

logger = logging.getLogger("TerrPlantBatchOutput")

def html_table(row_inp_all):
    while True:
        row_inp_temp_all = row_inp_all.get()
        if row_inp_temp_all is None:
            break
        else:
            row_inp = row_inp_temp_all[0]
            iter = row_inp_temp_all[1]

            A_temp=float(row_inp[0])
            application_rate.append(A_temp)
            I_temp=float(row_inp[1])
            incorporation_depth.append(I_temp)
            R_temp=float(row_inp[2])
            runoff_fraction.append(R_temp)
            D_temp=float(row_inp[3])
            drift_fraction.append(D_temp)
            nms_temp=float(row_inp[4])
            ec25_nonlisted_seedling_emergence_monocot.append(nms_temp)
            lms_temp=float(row_inp[5])        
            ec25_nonlisted_seedling_emergence_dicot.append(lms_temp)
            nds_temp=float(row_inp[6])   
            noaec_listed_seedling_emergence_monocot.append(nds_temp)
            lds_temp=float(row_inp[7])
            noaec_listed_seedling_emergence_dicot.append(lds_temp)
            terr = terrplant_model.terrplant(True,True,"batch",A_temp,I_temp,R_temp,D_temp,nms_temp,lms_temp,nds_temp,lds_temp)
            logger.info("===============")
            rundry_temp=terr.rundry_results
            rundry_out.append(rundry_temp)
            runsemi_temp=terr.runsemi_results
            runsemi_out.append(runsemi_temp)
            spray_temp=terr.spray_results
            spray_out.append(spray_temp)
            totaldry_temp=terr.totaldry_results
            totaldry_out.append(totaldry_temp)
            totalsemi_temp=terr.totalsemi_results
            totalsemi_out.append(totalsemi_temp)
            nms_rq_dry_temp=terr.nms_rq_dry_results
            nms_rq_dry_out.append(nms_rq_dry_temp)
            LOCnmsdry_temp=terr.LOCnmsdry_results
            LOCnmsdry_out.append(LOCnmsdry_temp)
            nms_rq_semi_temp=terr.nms_rq_semi_results
            nms_rq_semi_out.append(nms_rq_semi_temp)
            LOCnmssemi_temp=terr.LOCnmssemi_results
            LOCnmssemi_out.append(LOCnmssemi_temp)
            nms_rq_spray_temp=terr.nms_rq_spray_results
            nms_rq_spray_out.append(nms_rq_spray_temp)
            LOCnmsspray_temp=terr.LOCnmsspray_results
            LOCnmsspray_out.append(LOCnmsspray_temp)
            lms_rq_dry_temp=terr.lms_rq_dry_results
            lms_rq_dry_out.append(lms_rq_dry_temp)
            LOClmsdry_temp=terr.LOClmsdry_results
            LOClmsdry_out.append(LOClmsdry_temp)
            lms_rq_semi_temp=terr.lms_rq_semi_results
            lms_rq_semi_out.append(lms_rq_semi_temp)
            LOClmssemi_temp=terr.LOClmssemi_results
            LOClmssemi_out.append(LOClmssemi_temp)
            lms_rq_spray_temp=terr.lms_rq_spray_results
            lms_rq_spray_out.append(lms_rq_spray_temp)
            LOClmsspray_temp=terr.LOClmsspray_results
            LOClmsspray_out.append(LOClmsspray_temp)
            nds_rq_dry_temp=terr.nds_rq_dry_results
            nds_rq_dry_out.append(nds_rq_dry_temp)
            LOCndsdry_temp=terr.LOCndsdry_results
            LOCndsdry_out.append(LOCndsdry_temp)
            nds_rq_semi_temp=terr.nds_rq_semi_results
            nds_rq_semi_out.append(nds_rq_semi_temp)
            LOCndssemi_temp=terr.LOCndssemi_results
            LOCndssemi_out.append(LOCndssemi_temp)
            nds_rq_spray_temp=terr.nds_rq_spray_results
            nds_rq_spray_out.append(nds_rq_spray_temp)
            LOCndsspray_temp=terr.LOCndsspray_results
            LOCndsspray_out.append(LOCndsspray_temp)
            lds_rq_dry_temp=terr.lds_rq_dry_results
            lds_rq_dry_out.append(lds_rq_dry_temp)
            LOCldsdry_temp=terr.LOCldsdry_results
            LOCldsdry_out.append(LOCldsdry_temp)
            lds_rq_semi_temp=terr.lds_rq_semi_results
            lds_rq_semi_out.append(lds_rq_semi_temp)
            LOCldssemi_temp=terr.LOCldssemi_results
            LOCldssemi_out.append(LOCldssemi_temp)
            lds_rq_spray_temp=terr.lds_rq_spray_results
            lds_rq_spray_out.append(lds_rq_spray_temp)
            LOCldsspray_temp=terr.LOCldsspray_results
            LOCldsspray_out.append(LOCldsspray_temp)

            jid_all.append(terr.jid)
            terr_all.append(terr)    
            if iter == 1:
                jid_batch.append(terr.jid)

            batch_header = """
                <div class="out_">
                    <br><H3>Batch Calculation of Iteration %s:</H3>
                </div>
                """%(iter)

            html_temp = terrplant_tables.table_all(terr)

            out_html_temp = batch_header + html_temp
            out_html_all[iter]=out_html_temp

                
def loop_html(thefile):
    reader = csv.reader(thefile.file.read().splitlines())
    header = reader.next()
    # logger.info(header)
    i=1
    ####Create a job queue and add each row of batch temeplate file as a task into it
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

    html_timestamp = terrplant_tables.timestamp("", jid_batch[0])
    out_html_all_sort = OrderedDict(sorted(out_html_all.items()))
    sum_html = terrplant_tables.table_all_sum(terrplant_tables.sumheadings, terrplant_tables.tmpl, application_rate, incorporation_depth, runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot, 
                    rundry_out, runsemi_out, spray_out, totaldry_out, totalsemi_out, 
                    nms_rq_dry_out, nms_rq_semi_out, nms_rq_spray_out, 
                    lms_rq_dry_out, lms_rq_semi_out, lms_rq_spray_out, 
                    nds_rq_dry_out, nds_rq_semi_out, nds_rq_spray_out, 
                    lds_rq_dry_out, lds_rq_semi_out, lds_rq_spray_out)

    return  html_timestamp + sum_html + "".join(out_html_all_sort.values())


@require_POST
def terrplantBatchOutputPage(request):
    thefile = request.FILES['upfile']
    iter_html=loop_html(thefile)

    return iter_html, terr_all, jid_batch