"""
.. module:: stir_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation

SELECT_RECEPTOR = (('Avian', 'Avian'), ('Mammalian', 'Mammalian'), ('Both', 'Both'))
SELECT_HEIGHT = (('3.3', '3.3'), ('1', '1'))
SELECT_DURATION = (('1.5', '1.5'), ('0.5', '0.5'))
SELECT_VERSION = (('1.0', '1.0'),)


class StirInp(forms.Form):
    version_stir = forms.ChoiceField(
        choices=SELECT_VERSION,
        label='Version',
        initial='1.0')
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        label='Chemical Name',
        initial='STIR Example')
    # validators=[validators.validate_slug]) chokes on spaces
    pc_code = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='055459',
        validators=[validators.validate_slug])
    application_rate = forms.FloatField(
        label='Pesticide Application Rate (lbs ai/A)',
        initial=0.107,
        validators=[validation.validate_positive])
    column_height = forms.ChoiceField(
        label='Direct Spray Column Height (m)',
        choices=SELECT_HEIGHT,
        initial='3.3')
    spray_drift_fraction = forms.FloatField(
        label='Fraction of Spray Inhaled',
        initial=0.9,
        validators=[validation.validate_range01])
    direct_spray_duration = forms.ChoiceField(
        label='Direct Spray Inhalation Duration (min)',
        choices=SELECT_DURATION,
        initial='1.5')
    molecular_weight = forms.FloatField(
        label='Molecular Weight (g/mol)',
        initial=308.14,
        validators=[validation.validate_positive])
    vapor_pressure = forms.FloatField(
        label='Vapor Pressure (torr)',
        initial=9e-8,
        validators=[validation.validate_positive])
    avian_oral_ld50 = forms.FloatField(
        label=mark_safe('Lowest Avian Oral LD<sub>50</sub> (mg/kg-bw)'),
        initial=2292,
        validators=[validation.validate_positive])
    body_weight_assessed_bird = forms.FloatField(
        label='Body Weight of Assessed Bird (kg)',
        initial=0.02,
        validators=[validation.validate_positive])
    body_weight_tested_bird = forms.FloatField(
        label='Body Weight of Tested Bird (kg)',
        initial=0.178,
        validators=[validation.validate_positive])
    mineau_scaling_factor = forms.FloatField(
        label='Chemical Specific Mineau Scaling Factor',
        initial='1.15',
        validators=[validation.validate_greaterthanequalto1])
    mammal_inhalation_lc50 = forms.FloatField(
        label=mark_safe('Lowest Mammal (Rat) Inhalation LC<sub>50</sub> (mg/L)'),
        initial=3.38,
        validators=[validation.validate_positive])
    duration_mammal_inhalation_study = forms.FloatField(
        label='Duration of Mammal (Rat) Inhalation Study (hr)',
        initial=4,
        validators=[validation.validate_positive])
    body_weight_assessed_mammal = forms.FloatField(
        label='Body Weight of Assessed Mammal (kg)',
        initial=0.015,
        validators=[validation.validate_positive])
    body_weight_tested_mammal = forms.FloatField(
        label='Body Weight of Tested Mammal (kg)',
        initial=0.35,
        validators=[validation.validate_positive])
    mammal_oral_ld50 = forms.FloatField(
        label=mark_safe('Lowest Mammal (Rat) Oral LD<sub>50</sub> (mg/kg-bw)'),
        initial=5000,
        validators=[validation.validate_positive])
