from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

################ How model name appears on web page ################
header = 'TerrPlant'
####################################################################

def terrplantInputPage(request, model=''):
    import terrplant_parameters,terrplant_tooltips

    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('terrplant_ubertool_config_input.html', {})  
    html = html + str(terrplant_parameters.TerrPlantInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html = html + render_to_string('terrplant_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    if hasattr(terrplant_tooltips, 'tooltips'):
        tooltips = terrplant_tooltips.tooltips
    else:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})    

    return html


@require_POST
def terrplantOutputPage(request):
    import terrplant_model

    version_terrplant = request.POST.get('version_terrplant')
    I = request.POST.get('incorporation')
    A = request.POST.get('application_rate')
    D = request.POST.get('drift_fraction')
    R = request.POST.get('runoff_fraction')
    nms = request.POST.get('EC25_for_nonlisted_seedling_emergence_monocot')
    nds = request.POST.get('EC25_for_nonlisted_seedling_emergence_dicot')
    lms = request.POST.get('NOAEC_for_listed_seedling_emergence_monocot')
    lds = request.POST.get('NOAEC_for_listed_seedling_emergence_dicot')
    #fill out terrplant object with yet to be used data
    chemical_name = request.POST.get('chemical_name')
    # terr.chemical_name = chemical_name
    pc_code = request.POST.get('pc_code')
    # terr.pc_code = pc_code
    use = request.POST.get('use')
    # terr.use = use
    application_method = request.POST.get('application_method')
    # terr.application_method = application_method
    application_form = request.POST.get('application_form')
    # terr.application_form = application_form
    solubility = request.POST.get('solubility')
    # terr.sol = sol
    terr = terrplant_model.terrplant(True,True,version_terrplant,"single",A,I,R,D,nms,lms,nds,lds,chemical_name,pc_code,use,application_method,application_form,solubility)

    nmv = request.POST.get('EC25_for_nonlisted_vegetative_vigor_monocot')
    terr.nmv = nmv
    ndv = request.POST.get('EC25_for_nonlisted_vegetative_vigor_dicot')
    terr.ndv = ndv
    lmv = request.POST.get('NOAEC_for_listed_vegetative_vigor_monocot')
    terr.lmv = lmv
    ldv = request.POST.get('NOAEC_for_listed_vegetative_vigor_dicot')
    terr.ldv = ldv

    return terr