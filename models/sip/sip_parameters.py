"""
.. module:: sip_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from pram_app.models.forms import validation

Species_of_the_tested_bird_CHOICES = (('178', 'Northern bobwhite quail'), ('1580', 'Mallard duck'), ('1', 'Other'))
Species_of_the_tested_mamm_CHOICES = (('350', 'Laboratory rat'), ('1', 'Other'))
SELECT_VERSION = (('1.0', '1.0'),)


class SipInp(forms.Form):
    version = forms.ChoiceField(
        choices=SELECT_VERSION,
        label='Version',
        initial='1.0')
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        initial='SIP Example',
        required=True)
    pc_code = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='055459')
    solubility = forms.FloatField(
        required=True,
        label=mark_safe('Solubility (in water at 25&deg;C; mg/L)'),
        initial=0.128,
        validators=[validation.validate_greaterthan0])
    ld50_mammal_water = forms.FloatField(
        required=True,
        label=mark_safe('Mammalian LD<sub>50</sub> (mg/kg-bw)'),
        initial=5000,
        validators=[validation.validate_greaterthan0])
    ld50_species_tested_mammal = forms.ChoiceField(
        required=True,
        label='Mammalian test species',
        choices=Species_of_the_tested_mamm_CHOICES,
        initial='350',
        validators=[validation.validate_choicefield])
    ld50_bodyweight_tested_mammal_other = forms.FloatField(
        required=True,
        label='Body weight (g) of mammalian species',
        initial=350,
        validators=[validation.validate_greaterthan0])
    noael_mammal_water = forms.FloatField(
        required=True,
        label='Mammalian NOAEL (mg/kg-bw)',
        initial=20,
        validators=[validation.validate_positive])
    noael_species_tested_mammal = forms.ChoiceField(
        required=True,
        label='Mammalian test species',
        choices=Species_of_the_tested_mamm_CHOICES,
        initial='350',
        validators=[validation.validate_choicefield])
    noael_bodyweight_tested_mammal_other = forms.FloatField(
        required=True,
        label='Body weight (g) of mammalian species',
        initial=350,
        validators=[validation.validate_greaterthan0])
    # bodyweight_assessed_mammal = forms.FloatField(
    #         required=True,
    #         label='Body weight of assessed mammal (g)',
    #         initial=1000,
    #         validators=[validation.validate_greaterthan0])
    ld50_avian_water = forms.FloatField(
        required=True,
        label=mark_safe('Avian LD<sub>50</sub> (mg/kg-bw)'),
        initial=2292,
        validators=[validation.validate_positive])
    ld50_species_tested_bird = forms.ChoiceField(
        required=True,
        label=mark_safe('Avian test species'),
        choices=Species_of_the_tested_bird_CHOICES,
        initial='178',
        validators=[validation.validate_choicefield])
    ld50_bodyweight_tested_bird_other = forms.FloatField(
        required=True,
        label='Body weight (g) of avian species',
        initial=178,
        validators=[validation.validate_greaterthan0])
    # bodyweight_assessed_bird = forms.FloatField(
    #         required=True,
    #         label='Body weight of assessed bird (g)',
    #         initial=20,
    #         validators=[validation.validate_greaterthan0])
    mineau_scaling_factor = forms.FloatField(
        required=True,
        label='Mineau scaling factor',
        initial=1.15,
        validators=[validation.validate_greaterthanequalto1])

    noaec_duck = forms.FloatField(
        required=True,
        label='Mallard duck NOAEC (mg/kg-diet)',
        initial=465,
        validators=[validation.validate_positive])
    noaec_quail = forms.FloatField(
        required=True,
        label='Northern bobwhite quail NOAEC (mg/kg-diet)',
        initial=435,
        validators=[validation.validate_positive])
    noaec_bird_other_1 = forms.FloatField(
        required=False,
        label='NOAEC (mg/kg-diet) for other bird species',
        validators=[validation.validate_positive])
    noaec_bodyweight_bird_other_1 = forms.FloatField(
        required=False,
        label='Body weight (g) of other avian species',
        validators=[validation.validate_positive])
    noaec_bird_other_2 = forms.FloatField(
        required=False,
        label='NOAEC (mg/kg-diet) for 2nd other bird species',
        validators=[validation.validate_positive])
    noaec_bodyweight_bird_other_2 = forms.FloatField(
        required=False,
        label='Body weight (g) of 2nd other avian species',
        validators=[validation.validate_positive])
