"""
.. module:: iec_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


class IecInp(forms.Form):
    LC50 = forms.FloatField(
    		label=mark_safe('Enter LC<sub>50</sub> or LD<sub>50</sub>'),
    		initial='1',
    		validators=[validation.validate_greaterthan0])
    threshold = forms.FloatField(
    		label='Enter desired threshold',
    		initial='0.25',
    		validators=[validation.validate_greaterthan0, validation.validate_range01])
    dose_response = forms.FloatField(
    		label='Enter slope of dose-response',
    		initial=4.5,
    		validators=[validation.validate_greaterthan0])