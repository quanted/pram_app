"""
.. module:: geneec_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


applicationtarget_CHOICES = (('a','Short grass'),('b','Tall grass'),('c','Broad-leafed plants/small insects'),
                            ('d','Fruits/pods/seeds/large insects')) 
wet_in_CHOICES = (('Yes','Yes'),('No','No'))
applicationmethod_CHOICES = (('0','Pick an application method'),('a','Aerial Spray'),('b','Ground Spray'),
                         ('c','Airblast Spray (Orchard & Vineyard)'),('d','Granular (Non-Spray)'))
wet_in_CHOICES = (('Yes','Yes'),('No','No'))
aerial_size_dist_CHOICES=(('a','Very Fine to Fine'),('b','Fine to Medium (EFED Default)'),
                          ('c','Medium to Coarse'),('d','Coarse to Very Coarse')) 
ground_spray_CHOICES = (('a','Low Boom Ground Spray (20" or less)'),
                       ('b','High Boom Ground Spray (20-50"; EFED Default)')) 
spray_quality_CHOICES = (('a','Fine (EFED Default)'),
                        ('b','Medium-Coarse'))  
airblast_type_CHOICES = (('a','Orchards and Dormant Vineyards'),
                         ('b','Foliated Vineyards')) 


class GeneecInp(forms.Form):
    chemical_name = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}))
    application_target = forms.ChoiceField(
            choices=applicationtarget_CHOICES,
            initial='Short grass')        
    application_rate = forms.FloatField(
            label='Application rate (lbs a.i./A)',
            initial=4,
            validators=[validation.validate_greaterthan0])
    number_of_applications = forms.FloatField(
            label='Number of applications',
            initial=5,
            validators=[validation.validate_greaterthan0])
    interval_between_applications = forms.FloatField(
            label='Interval between applications (days)',
            initial=6,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    Koc = forms.FloatField(
            label=mark_safe('K<sub>OC</sub> (mL/g OC)'),
            initial=2,
            validators=[validation.validate_greaterthan0])
    aerobic_soil_metabolism = forms.FloatField(
            label='Aerobic soil metabolism half-life (days)',
            initial=7,
            validators=[validation.validate_greaterthan0, validation.validate_integer])    
    wet_in = forms.ChoiceField(
            choices=wet_in_CHOICES,
            initial='Yes')        
    
    application_method = forms.ChoiceField(
            choices=applicationmethod_CHOICES,
            initial='Pick an application method',
            validators=[validation.validate_choicefield])
    #A1
    aerial_size_dist = forms.ChoiceField(
            choices=aerial_size_dist_CHOICES,
            initial='Very Fine to Fine')
    #B1
    ground_spray_type = forms.ChoiceField(
            choices=ground_spray_CHOICES,
            initial='Low Boom Ground Spray (20" or less)')                                          
    #C1
    airblast_type = forms.ChoiceField(
            choices=airblast_type_CHOICES,
            initial='Orchards and Dormant Vineyards')    
    #B2    
    spray_quality = forms.ChoiceField(
            choices=spray_quality_CHOICES,
            initial='Fine (EFED Default)')
    no_spray_drift = forms.FloatField(
            label='Width of the no-spray zone (feet)',
            initial=12,
            validators=[validation.validate_greaterthan0, validation.validate_integer])    
    incorporation_depth = forms.FloatField(
            label='Incorporation Depth (inch)',
            initial=2,
            validators=[validation.validate_greaterthan0, validation.validate_integer])    
    solubility = forms.FloatField(
            label='Solubility (mg/L)',
            initial=3,
            validators=[validation.validate_greaterthan0])
    aerobic_aquatic_metabolism = forms.FloatField(
            label='Aerobic aquatic metabolism half-life (days)',
            initial=6,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    hydrolysis = forms.FloatField(
            label='Hydrolysis: pH=7/neutral half-life (days)',
            initial=10,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    photolysis_aquatic_half_life = forms.FloatField(
            label='Photolysis, aquatic half-life (days)',
            initial=11,
            validators=[validation.validate_greaterthan0, validation.validate_integer])