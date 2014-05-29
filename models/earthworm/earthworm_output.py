from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def earthwormOutputPage(request):
    import earthworm_model
    k_ow = float(request.POST.get('k_ow'))
    l_f_e = float(request.POST.get('l_f_e'))
    c_s = float(request.POST.get('c_s'))
    k_d = float(request.POST.get('k_d'))
    p_s = float(request.POST.get('p_s'))
    c_w = float(request.POST.get('c_w'))
    m_w = float(request.POST.get('m_w'))
    p_e = float(request.POST.get('p_e'))
    
    earthworm_obj = earthworm_model.earthworm(True,True,'single', k_ow,l_f_e,c_s,k_d,p_s,c_w,m_w,p_e)
    
    return earthworm_obj