"""
.. module:: therps_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


Species_of_the_tested_bird_CHOICES=(('Bobwhite quail','Bobwhite quail'),('Mallard duck','Mallard duck'),('Other','Other'))
 
class therpsInp_chem(forms.Form):    
    chemical_name = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            initial='T-Herps Example')
    Use = forms.CharField(
            max_length=255,
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            initial='Dried shelled beans (except soybeans)')   
    Formulated_product_name = forms.CharField(
            max_length=255,
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            initial='NA')    
    percent_ai=forms.FloatField(
            label='% a.i. (%)',
            initial=100,
            validators=[validation.validate_range0100])
    Foliar_dissipation_half_life = forms.FloatField(
            label='Foliar dissipation half-life (days)',
            initial=35,
            validators=[validation.validate_range_1_365])
    number_of_applications = forms.FloatField(
            label='Number of applications',
            initial=2,
            validators=[validation.validate_integer])
    interval_between_applications = forms.FloatField(
            label='Interval between applications (days)',
            initial=7,
            validators=[validation.validate_integer])
    application_rate = forms.FloatField(
            label='Application rate (lbs a.i./A)',
            initial=0.18,
            validators=[validation.validate_positive])

class therpsInp_bird(forms.Form):    
    avian_ld50 = forms.FloatField(
            label='Avian LD50 (mg/kg-bw)',
            initial=2000,
            validators=[validation.validate_positive])
    Species_of_the_tested_bird_avian_ld50 = forms.ChoiceField(
            label='Test species (for Avian LD50)',
            choices=Species_of_the_tested_bird_CHOICES,
            initial='Bobwhite quail')
    bw_avian_ld50 = forms.FloatField(
            label='Weight (g)',
            initial= '178',
            validators=[validation.validate_positive])
    avian_lc50 = forms.FloatField(
            label='Avian LC50 (mg/kg-diet)',
            initial=2457,
            validators=[validation.validate_positive])
    Species_of_the_tested_bird_avian_lc50 = forms.ChoiceField(
            label='Test species (for Avian LC50)',
            choices=Species_of_the_tested_bird_CHOICES,
            initial='Bobwhite quail')
    bw_avian_lc50 = forms.FloatField(
            label='Weight (g)',
            initial= '178',
            validators=[validation.validate_positive])
    avian_NOAEC = forms.FloatField(
            label='Avian NOAEC (mg/kg-diet)',
            initial=100,
            validators=[validation.validate_positive])
    Species_of_the_tested_bird_avian_NOAEC = forms.ChoiceField(
            label='Test species (for Avian NOAEC)',
            choices=Species_of_the_tested_bird_CHOICES,
            initial='Bobwhite quail')
    bw_avian_NOAEC = forms.FloatField(
            label='Weight (g)',
            initial= '178',
            validators=[validation.validate_positive])
    avian_NOAEL = forms.FloatField(
            label='Avian NOAEL (mg/kg-bw)',
            initial=7.8,
            validators=[validation.validate_positive])
    Species_of_the_tested_bird_avian_NOAEL = forms.ChoiceField(
            label='Test species (for Avian NOAEL)',
            choices=Species_of_the_tested_bird_CHOICES,
            initial='Bobwhite quail')
    bw_avian_NOAEL = forms.FloatField(
            label='Weight (g)',
            initial= '178',
            validators=[validation.validate_positive])
    # Species_of_the_tested_bird = forms.ChoiceField(
            # label='Species of the tested bird', choices=Species_of_the_tested_bird_CHOICES, initial='Bobwhite quail')
    # body_weight_of_the_tested_bird=forms.FloatField(
            # label='Body weight of the tested bird (g)', initial=178)
    mineau_scaling_factor = forms.FloatField(
            label='Mineau scaling factor',
            initial=1.15,
            validators=[validation.validate_greaterthanequalto1])

class therpsInp_herp(forms.Form):    
    BW_herptile_a_sm = forms.FloatField(
            label='Body weight of assessed small herptile (g)',
            initial=2.0,
            validators=[validation.validate_positive])
    W_p_a_sm = forms.FloatField(
            label="Water content of the assessed small herptile's diet (%)",
            initial=85,
            validators=[validation.validate_range0100])
    BW_herptile_a_md = forms.FloatField(
            label='Body weight of assessed medium herptile (g)',
            initial=20,
            validators=[validation.validate_positive])
    W_p_a_md = forms.FloatField(
            label="Water content of the assessed medium herptile's diet (%)",
            initial=85,
            validators=[validation.validate_range0100])
    BW_herptile_a_lg = forms.FloatField(
            label='Body weight of assessed large herptile (g)',
            initial=200,
            validators=[validation.validate_positive])
    W_p_a_lg = forms.FloatField(
            label="Water content of the assessed large herptile's diet (%)",
            initial=85,
            validators=[validation.validate_range0100])
    body_weight_of_the_consumed_mammal_a = forms.FloatField(
            label='Weight of the mammal consumed by assessed frog (g)',
            initial=15,
            validators=[validation.validate_positive])
    body_weight_of_the_consumed_herp_a = forms.FloatField(
            label='Weight of the herptile  consumed by assessed frog (g)',
            initial=15,
            validators=[validation.validate_positive])


class TherpsInp(therpsInp_chem, therpsInp_bird, therpsInp_herp):
    pass