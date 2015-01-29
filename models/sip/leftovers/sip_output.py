"""
.. module:: sip_output
   :synopsis: A useful module indeed.
"""

from django.views.decorators.http import require_POST

@require_POST
def sipOutputPage(request):
    import sip_model

    chemical_name = request.POST.get('chemical_name')
   # select_receptor = request.POST.get('select_receptor')
   # bodyweight_tested_bird = request.POST.get('body_weight_of_bird')
   # bodyweight_tested_mammal = request.POST.get('body_weight_of_mammal')
    solubility = request.POST.get('solubility')
    ld50_avian_water = request.POST.get('ld50_avian_water')
    ld50_mammal_water = request.POST.get('ld50_mammal_water')
    bodyweight_assessed_bird = request.POST.get('bodyweight_assessed_bird')
    # tw_bird = request.POST.get('body_weight_of_the_tested_bird')
    bodyweight_assessed_mammal = request.POST.get('bodyweight_assessed_mammal')
    # tw_mamm = request.POST.get('body_weight_of_the_tested_mammal')
    mineau_scaling_factor = request.POST.get('mineau_scaling_factor')
    noael_mammal_water = request.POST.get('NOAEL')
    noaec_duck = request.POST.get('NOAEC_d')
    noaec_quail = request.POST.get('NOAEC_q')
    noaec_other = request.POST.get('NOAEC_o')
    # noaec_o2 = request.POST.get('NOAEC_o2')
    Species_of_the_bird_NOAEC_CHOICES = request.POST.get('NOAEC_species')
    bodyweight_quail = request.POST.get('bodyweight_quail')
    bodyweight_duck = request.POST.get('bodyweight_duck')
    bodyweight_bird_other = request.POST.get('bodyweight_bird_other')
    bodyweight_rat = request.POST.get('bodyweight_rat')
    bodyweight_tested_mammal_other = request.POST.get('bodyweight_tested_mammal_other')
    species_tested_bird = request.POST.get('species_tested_bird')
    species_tested_mammal = request.POST.get('species_tested_mammal')

    sip_obj = sip_model.sip(True,True,'single',chemical_name, species_tested_bird, species_tested_mammal, bodyweight_quail, bodyweight_duck, bodyweight_bird_other, bodyweight_rat, bodyweight_tested_mammal_other, solubility, ld50_avian_water, ld50_mammal_water, bodyweight_assessed_bird, mineau_scaling_factor, bodyweight_assessed_mammal, noaec_duck, noaec_quail, noaec_other, Species_of_the_bird_NOAEC_CHOICES, noael_mammal_water)

    return sip_obj