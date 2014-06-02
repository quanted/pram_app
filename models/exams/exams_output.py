from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def examsOutputPage(request):
    import exams_model

    chem_name = request.POST.get('chemical_name')
    scenarios =request.POST.get('scenarios')
    farm =request.POST.get('farm_pond')
    mw = request.POST.get('molecular_weight')
    sol = request.POST.get('solubility')
    koc = request.POST.get('Koc')
    vp = request.POST.get('vapor_pressure')
    aem = request.POST.get('aerobic_aquatic_metabolism')
    anm = request.POST.get('anaerobic_aquatic_metabolism')
    aqp = request.POST.get('aquatic_direct_photolysis')
    tmper = request.POST.get('temperature')
    n_ph = float(request.POST.get('n_ph'))
    ph_out = []
    hl_out = []
    for i in range(int(n_ph)):
        j=i+1
        ph_temp = request.POST.get('ph'+str(j))
        ph_out.append(float(ph_temp))
        hl_temp = float(request.POST.get('hl'+str(j)))
        hl_out.append(hl_temp)  

    exams_obj = exams_model.exams(chem_name, scenarios, farm, mw, sol, koc, vp, aem, anm, aqp, tmper, n_ph, ph_out, hl_out)

    return exams_obj