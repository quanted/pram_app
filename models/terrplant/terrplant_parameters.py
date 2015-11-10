# -*- coding: utf-8 -*-
"""
.. module:: terrplant_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


SELECT_INCORPORATION = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))

SELECT_DRIFT = (('0.01','0.01'),('0.05','0.05'),('0','0'))

SELECT_RUN = (('0.01','0.01'),('0.02','0.02'),('0.05','0.05'))

SELECT_VERSION = (('1.2.2','1.2.2'),)

class TerrplantInp(forms.Form):
    version_terrplant = forms.ChoiceField(
            choices=SELECT_VERSION, 
            label='Version',
            initial='1.2.2')
    chemical_name = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            label='Chemical Name',
            initial='Terrplant Example',
            validators=[validators.validate_slug])
    pc_code = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), 
            label='PC Code',
            initial='90501',
            validators=[validators.validate_slug])
    use = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), 
            label='Use',
            initial='Corn',
            validators=[validators.validate_slug])
    application_method = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), 
            label='Application Method',
            initial='Ground',
            validators=[validators.validate_slug])
    application_form = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), 
            label='Application Form',
            initial='Spray',
            validators=[validators.validate_slug])
    solubility = forms.FloatField(
            label='Solubility (ppm)',
            initial=240,
            validators=[validation.validate_positive])
    incorporation_depth = forms.ChoiceField(
            choices=SELECT_INCORPORATION, 
            label='Incorporation Depth (in)')    
    application_rate = forms.FloatField(
            label='Application rate (lbs ai/A)',
            initial=4)    
    drift_fraction = forms.ChoiceField(
            choices=SELECT_DRIFT, 
            label='Drift Fraction',
            initial=0.01,
            validators=[validation.validate_positive])
    runoff_fraction = forms.ChoiceField(
            choices=SELECT_RUN, 
            label='Runoff Fraction',
            initial=0.05)
    ec25_nonlisted_seedling_emergence_monocot = forms.FloatField(
            label=mark_safe('EC<sub>25</sub> for Non-listed Seedling Emergence Monocot (lbs ai/A)'),
            initial=0.0067,
            validators=[validation.validate_positive])
    ec25_nonlisted_seedling_emergence_dicot = forms.FloatField(
            label=mark_safe('EC<sub>25</sub> for Non-listed Seedling Emergence Dicot (lbs ai/A)'),
            initial=0.034,
            validators=[validation.validate_positive])
    noaec_listed_seedling_emergence_monocot = forms.FloatField(
            label=mark_safe('noaec for Non-listed Seedling Emergence Monocot (lbs ai/A)'),
            initial=0.0023,
            validators=[validation.validate_positive])
    noaec_listed_seedling_emergence_dicot = forms.FloatField(
            label=mark_safe('noaec for Non-listed Seedling Emergence Dicot (lbs ai/A)'),
            initial=0.019,
            validators=[validation.validate_positive])
    ec25_nonlisted_vegetative_vigor_monocot = forms.FloatField(
            label=mark_safe('EC<sub>25</sub> for Non-listed Vegetative Vigor Monocot (lbs ai/A)'),
            initial=0.068,
            validators=[validation.validate_positive])
    ec25_nonlisted_vegetative_vigor_dicot = forms.FloatField(
            label=mark_safe('EC<sub>25</sub> for Non-listed Vegetative Vigor Dicot (lbs ai/A)'),
            initial=1.4,
            validators=[validation.validate_positive])
    noaec_listed_vegetative_vigor_monocot = forms.FloatField(
            label=mark_safe('noaec for Non-listed Vegetative Vigor Monocot (lbs ai/A)'),
            initial=0.037,
            validators=[validation.validate_positive])
    noaec_listed_vegetative_vigor_dicot = forms.FloatField(
            label=mark_safe('noaec for Non-listed Vegetative Vigor Dicot (lbs ai/A)'),
            initial=0.67,
            validators=[validation.validate_positive])
