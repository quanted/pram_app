"""
.. module:: dust_batch_runner
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST


@require_POST
def dustOutputPage(request):
    import dust_model

    chemical_name = request.POST.get('chemical_name')
    label_epa_reg_no = request.POST.get('label_epa_reg_no')
    ar_lb = request.POST.get('application_rate')
    frac_pest_surface = request.POST.get('frac_pest_assumed_at_surface')
    dislodge_fol_res = request.POST.get('dislodgeable_foliar_residue')
    bird_acute_oral_study = request.POST.get('bird_acute_oral_study')
    bird_study_add_comm = request.POST.get('bird_study_add_comm')
    low_bird_acute_ld50 = request.POST.get('low_bird_acute_oral_ld50')
    test_bird_bw = request.POST.get('tested_bird_body_weight')
    mamm_acute_derm_study = request.POST.get('mamm_acute_derm_study')
    mamm_study_add_comm = request.POST.get('mamm_study_add_comm')
    #aviandermaltype = request.POST.get('aviandermaltype')
    mam_acute_derm_ld50 = request.POST.get('mamm_acute_derm_ld50')
    mam_acute_oral_ld50 = request.POST.get('mam_acute_oral_ld50')
    test_mam_bw = request.POST.get('tested_mamm_body_weight')
    mineau_scaling_factor = float(request.POST.get('mineau_scaling_factor'))
    
    dust_obj = dust_model.dust(True, False, 'single',chemical_name, label_epa_reg_no, ar_lb, frac_pest_surface, dislodge_fol_res, bird_acute_oral_study, bird_study_add_comm,
          low_bird_acute_ld50, test_bird_bw, mineau_scaling_factor, mamm_acute_derm_study, mamm_study_add_comm, mam_acute_derm_ld50, mam_acute_oral_ld50, test_mam_bw, None)
    
    return dust_obj