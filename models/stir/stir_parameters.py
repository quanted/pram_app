"""
.. module:: stir_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


SELECT_RECEPTOR = (('Avian','Avian'),('Mammalian','Mammalian'),('Both','Both'))

SELECT_HEIGHT = (('3.3','3.3'),('1','1'))

SELECT_DURATION = (('1.5','1.5'),('0.5','0.5'))


class StirInp(forms.Form):


    chemical_name = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            label='Chemical Name',
            initial='Quinoxyfen',
            validators=[validators.validate_slug])
    application_rate = forms.FloatField(
            label='Pesticide Application Rate (lbs ai/A)',
            initial=0.107,
            validators=[validation.validate_positive])
    column_height = forms.ChoiceField(
            label='Direct Spray Column Height',
            choices=SELECT_HEIGHT,
            initial='3.3')    
    spray_drift_fraction = forms.FloatField(
            label='Fraction of Spray Inhaled',
            initial=0.9,
            validators=[validation.validate_range01])
    direct_spray_duration = forms.ChoiceField(
            label='Direct Spray Inhalation Duration', 
            choices=SELECT_DURATION,
            initial='1.5')
    molecular_weight = forms.FloatField(
            label='Molecular Weight',
            initial=308.14,
            validators=[validation.validate_positive])   
    vapor_pressure = forms.FloatField(
            label='Vapor Pressure',
            initial=9e-8,
            validators=[validation.validate_positive])
    avian_oral_ld50 = forms.FloatField(
            label=mark_safe('Lowest Avian Oral LD<sub>50</sub>'),
            initial=2292,
            validators=[validation.validate_positive])
    body_weight_assessed_bird = forms.FloatField(
            label='Body Weight of Assessed Bird',
            initial=0.02,
            validators=[validation.validate_positive])
    body_weight_tested_bird = forms.FloatField(
            label='Body Weight of Tested Bird',
            initial=0.178,
            validators=[validation.validate_positive])
    mineau_scaling_factor = forms.FloatField(
            label='Chemical Specific Mineau Scaling Factor',
            initial='1.15',
            validators=[validation.validate_greaterthanequalto1])
    mammal_inhalation_lc50 = forms.FloatField(
            label=mark_safe('Lowest Mammal (Rat) Inhalation LC<sub>50</sub>'),
            initial=3.38,
            validators=[validation.validate_positive])
    duration_mammal_inhalation_study = forms.FloatField(
            label='Duration of Mammal (Rat) Inhalation Study',
            initial=4,
            validators=[validation.validate_positive])
    body_weight_assessed_mammal = forms.FloatField(
            label='Body Weight of Assessed Mammal',
            initial=0.015,
            validators=[validation.validate_positive])
    body_weight_tested_mammal = forms.FloatField(
            label='Body Weight of Tested Mammal',
            initial=0.35,
            validators=[validation.validate_positive])
    mammal_oral_ld50 = forms.FloatField(
            label=mark_safe('Lowest Mammal (Rat) Oral LD<sub>50</sub>'),
            initial=5000,
            validators=[validation.validate_positive])

    # def is_valid(self):
    #     print "I ran!"
    #     valid = super(StirInp, self).is_valid()
    #     print valid
    #     if not valid:
    #         print "MODEL NOT VALID"
    #         return False

    #     else:
    #         print "MODEL VALID"
    #         return True