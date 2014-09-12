"""
.. module:: rice_qaqc
   :synopsis: A useful module indeed.
"""

import rice_model
import os
import unittest
from StringIO import StringIO
import csv


data = csv.reader(open(os.path.join(os.environ['PROJECT_PATH'], 'models','rice','rice_qaqc_inputs.csv')))
version_rice="1.0"
chemical_name=[]
mai=[]
a=[]
dsed=[]
pb=[]
dw=[]
osed=[]
kd=[]
#####Pre-defined outputs########
msed=[]
vw=[]
mai1=[]
cw=[]

data.next()
for row in data:
    chemical_name.append(str(row[0]))
    mai.append(float(row[1]))
    a.append(float(row[2]))  
    dsed.append(float(row[3]))
    pb.append(float(row[4]))
    dw.append(float(row[5]))
    osed.append(float(row[6]))        
    kd.append(float(row[7]))    
    msed.append(float(row[8]))
    vw.append(float(row[9]))
    mai1.append(float(row[10]))
    cw.append(float(row[11])) 

out_fun_Msed=[]
out_fun_Vw=[]
out_fun_Mai1=[]            
out_fun_Cw=[]            

rice_obj = rice_model.rice(True,True,
            version_rice,"qaqc",chemical_name[0], 
            mai[0], dsed[0], a[0], pb[0], dw[0], osed[0], kd[0])

rice_obj.chemical_name_expected=chemical_name[0]
rice_obj.msed_expected=msed[0]
rice_obj.vw_expected=vw[0]
rice_obj.mai1_expected=mai1[0]
rice_obj.cw_expected=cw[0]

