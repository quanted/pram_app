"""
.. module:: geneec_output
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

@require_POST
def geneecOutputPage(request):
    import geneec_model
    chem_name = request.POST.get('chemical_name')
    application_target = request.POST.get('application_target')
    application_rate = request.POST.get('application_rate')
    number_of_applications = request.POST.get('number_of_applications')
    interval_between_applications = request.POST.get('interval_between_applications')
    Koc = request.POST.get('Koc')  
    aerobic_soil_metabolism = request.POST.get('aerobic_soil_metabolism')   
    wet_in = request.POST.get('wet_in')              
    application_method = request.POST.get('application_method')
    #A1
    aerial_size_dist = request.POST.get('aerial_size_dist')
    #B1
    ground_spray_type = request.POST.get('ground_spray_type')                                          
    #C1
    airblast_type = request.POST.get('airblast_type')  
    #B2    
    spray_quality = request.POST.get('spray_quality')
    
    no_spray_drift = request.POST.get('no_spray_drift')    
    incorporation_depth = request.POST.get('incorporation_depth')   
    solubility = request.POST.get('solubility')
    aerobic_aquatic_metabolism = request.POST.get('aerobic_aquatic_metabolism')
    hydrolysis = request.POST.get('hydrolysis')
    photolysis_aquatic_half_life = request.POST.get('photolysis_aquatic_half_life')
    
    if (application_method=='a' or application_method=='c'):
        incorporation_depth=0
    if (application_method=='d'):
        no_spray_drift=0     
    if  aerobic_aquatic_metabolism>0:
        hydrolysis_label='NA'
    else:
        hydrolysis_label=hydrolysis
           
################label selection###################################                    
    if application_method=='a':
        application_method_label='Aerial Spray'
        if aerial_size_dist=='a':
           aerial_size_dist_label='Very Fine to Fine'
           ground_spray_type_label='NA'
           spray_quality_label='NA'
           airblast_type_label='NA' 
        elif aerial_size_dist=='b':
           aerial_size_dist_label='Fine to Medium (EFED Default)'
           ground_spray_type_label='NA'
           spray_quality_label='NA'
           airblast_type_label='NA'
        elif aerial_size_dist=='c':
           aerial_size_dist_label='Medium to Coarse'
           ground_spray_type_label='NA'
           spray_quality_label='NA'
           airblast_type_label='NA'
        else:
           aerial_size_dist_label='Coarse to Very Coarse' 
           ground_spray_type_label='NA'
           spray_quality_label='NA'
           airblast_type_label='NA'
          
    elif application_method=='b':        
        application_method_label='Ground Spray'
        if ground_spray_type=='a':
            if spray_quality=='a':
                aerial_size_dist_label='NA' 
                ground_spray_type_label='Low Boom Ground Spray (20" or less)'
                spray_quality_label='Fine (EFED Default)'
                airblast_type_label='NA'
            else:
                aerial_size_dist_label='NA' 
                ground_spray_type_label='Low Boom Ground Spray (20" or less)'
                spray_quality_label='Medium-Coarse'
                airblast_type_label='NA'
        else:
            if spray_quality=='a':
                aerial_size_dist_label='NA' 
                ground_spray_type_label='High Boom Ground Spray (20-50"; EFED Default)'
                spray_quality_label='Fine (EFED Default)'
                airblast_type_label='NA'
            else:
                aerial_size_dist_label='NA' 
                ground_spray_type_label='High Boom Ground Spray (20-50"; EFED Default)'
                spray_quality_label='Medium-Coarse'
                airblast_type_label='NA'
    elif application_method=='c':
        application_method_label='Airblast Spray (Orchard & Vineyard)'
        if airblast_type=='a':
                aerial_size_dist_label='NA' 
                ground_spray_type_label='NA'
                spray_quality_label='NA'
                airblast_type_label='Orchards and Dormant Vineyards'
        else:
                aerial_size_dist_label='NA' 
                ground_spray_type_label='NA'
                spray_quality_label='NA'
                airblast_type_label='Foliated Vineyards'
    else:
        application_method_label='NA'
        aerial_size_dist_label='NA' 
        ground_spray_type_label='NA'
        spray_quality_label='NA'
        airblast_type_label='NA'
##########################################################################################                                        
    geneec_obj = geneec_model.geneec('single', chem_name, application_target, application_rate, number_of_applications, interval_between_applications, Koc, aerobic_soil_metabolism, wet_in, application_method, application_method_label, aerial_size_dist, ground_spray_type, airblast_type, spray_quality, no_spray_drift, incorporation_depth, solubility, aerobic_aquatic_metabolism, hydrolysis, photolysis_aquatic_half_life)
    return geneec_obj
