from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
import numpy as np
import json

@require_POST
def pfamOutputPage(request):
    import pfam_model,pfam_tables

    ######Chemical#######        
    wat_hl = request.POST.get('wat_hl')
    wat_t = request.POST.get('wat_t')
    ben_hl = request.POST.get('ben_hl')
    ben_t = request.POST.get('ben_t')
    unf_hl = request.POST.get('unf_hl')
    unf_t = request.POST.get('unf_t')
    aqu_hl = request.POST.get('aqu_hl')
    aqu_t = request.POST.get('aqu_t')
    hyd_hl = request.POST.get('hyd_hl')
    mw = request.POST.get('mw')
    vp = request.POST.get('vp')
    sol = request.POST.get('sol')
    koc = request.POST.get('koc')
    hea_h = request.POST.get('hea_h')
    hea_r_t = request.POST.get('hea_r_t')
    ######Application#######        
    noa = request.POST.get('noa')
    mm_out = np.zeros(shape=(int(noa),1))
    dd_out = np.zeros(shape=(int(noa),1))
    ma_out = np.zeros(shape=(int(noa),1))
    sr_out = np.zeros(shape=(int(noa),1))
    for i in range(int(noa)):
        j=i+1
        mm_temp = request.POST.get('mm'+str(j))
        mm_out[i,] = int(mm_temp) 
        dd_temp = request.POST.get('dd'+str(j))
        dd_out[i,] = int(dd_temp)         
        ma_temp = request.POST.get('ma'+str(j))
        ma_out[i,] = ma_temp   
        sr_temp = request.POST.get('sr'+str(j))
        sr_out[i,] = sr_temp
                  
    ######Location#######        
    weather = request.POST.get('weather')
    wea_l = request.POST.get('wea_l')
    ######Floods#######    
    nof = request.POST.get('nof')
    date_f1 = request.POST.get('date_f1')
    nod_out = np.zeros(shape=(int(nof),1))
    fl_out = np.zeros(shape=(int(nof),1))
    wl_out = np.zeros(shape=(int(nof),1))
    ml_out = np.zeros(shape=(int(nof),1))
    to_out = np.zeros(shape=(int(nof),1))
    for k in range(int(nof)):
        jj=k+1
        if (jj==1):
            nod_out[k,] = int(0)
        else:                
            nod_temp = request.POST.get('nod'+str(jj))
            nod_out[k,] = int(nod_temp) 
        fl_temp = request.POST.get('fl'+str(jj))
        fl_out[k,] = fl_temp         
        wl_temp = request.POST.get('wl'+str(jj))
        wl_out[k,] = wl_temp   
        ml_temp = request.POST.get('ml'+str(jj))
        ml_out[k,] = ml_temp  
        to_temp = request.POST.get('to'+str(jj))
        to_out[k,] = to_temp                  
    ######Crop#######    
    zero_height_ref = request.POST.get('zero_height_ref')
    days_zero_full = request.POST.get('days_zero_full')
    days_zero_removal = request.POST.get('days_zero_removal')
    max_frac_cov = request.POST.get('max_frac_cov')
    ######Physical#######    
    mas_tras_cof = request.POST.get('mas_tras_cof')
    leak = request.POST.get('leak')
    ref_d = request.POST.get('ref_d')
    ben_d = request.POST.get('ben_d')
    ben_por = request.POST.get('ben_por')
    dry_bkd = request.POST.get('dry_bkd')
    foc_wat = request.POST.get('foc_wat')
    foc_ben = request.POST.get('foc_ben')
    ss = request.POST.get('ss')
    wat_c_doc = request.POST.get('wat_c_doc')
    chl = request.POST.get('chl')
    dfac = request.POST.get('dfac')
    q10 = request.POST.get('q10')
    ######Output#######  
    area_app = request.POST.get('area_app')
    
    pfam_obj=pfam_model.pfam(wat_hl,wat_t,ben_hl,ben_t,unf_hl,unf_t,aqu_hl,aqu_t,hyd_hl,mw,vp,sol,koc,hea_h,hea_r_t,
                        noa,dd_out.tolist(),mm_out.tolist(),ma_out.tolist(),sr_out.tolist(),weather, wea_l,
                        nof,date_f1,nod_out.tolist(),fl_out.tolist(),wl_out.tolist(),ml_out.tolist(),to_out.tolist(),
                        zero_height_ref,days_zero_full,days_zero_removal,max_frac_cov,mas_tras_cof,leak,ref_d,ben_d,
                        ben_por,dry_bkd,foc_wat,foc_ben,ss,wat_c_doc,chl,dfac,q10,area_app)
    
    x_date1=json.dumps(pfam_obj.final_res[1][1]) 
    x_re_v_f = [float(i) for i in pfam_obj.final_res[1][2]]
    x_re_c_f = [float(i) for i in pfam_obj.final_res[1][3]]
    setattr(pfam_obj, "x_date1", x_date1)
    setattr(pfam_obj, "x_re_v_f", x_re_v_f)
    setattr(pfam_obj, "x_re_c_f", x_re_c_f)

    x_date2=json.dumps(pfam_obj.final_res[1][4]) 
    x_water = [float(i) for i in pfam_obj.final_res[1][5]]
    x_water_level = [float(i) for i in pfam_obj.final_res[1][6]]
    x_ben_tot = [float(i) for i in pfam_obj.final_res[1][7]]
    x_ben_por = [float(i)*1000000 for i in pfam_obj.final_res[1][8]]
    setattr(pfam_obj, "x_date2", x_date2)
    setattr(pfam_obj, "x_water", x_water)
    setattr(pfam_obj, "x_water_level", x_water_level)
    setattr(pfam_obj, "x_ben_tot", x_ben_tot)
    setattr(pfam_obj, "x_ben_por", x_ben_por)


    html = pfam_tables.timestamp(pfam_obj)
    html = html + pfam_tables.table_all(pfam_obj)
    html = html + render_to_string('pfam-output.html', {})

    return html, pfam_obj