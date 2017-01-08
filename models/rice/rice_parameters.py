"""
.. module:: rice_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from ubertool_app.models.forms import validation

SELECT_VERSION = (('1.0', '1.0'),)


class RiceInp(forms.Form):
    version = forms.ChoiceField(
        choices=SELECT_VERSION,
        label='Version',
        initial='1.0')
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        initial='Fipronil')
    pc_code = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='00')
    mai = forms.FloatField(
        label='Mass of Applied Ingredient to Paddy (kg)',
        initial=0.056,
        validators=[validation.validate_greaterthan0])
    area = forms.FloatField(
        label=mark_safe('Area of the Rice Paddy (m<sup>2</sup>)'),
        initial=10000,
        validators=[validation.validate_greaterthan0])
    dsed = forms.FloatField(
        label='Sediment Depth (m)',
        initial=0.01,
        validators=[validation.validate_greaterthan0])
    pb = forms.FloatField(
        label=mark_safe('Bulk Density of Sediment, &#961;<sub>b</sub> (kg/m<sup>3</sup>)'),
        initial=1300,
        validators=[validation.validate_greaterthan0])
    dw = forms.FloatField(
        label='Water Column Depth (m)',
        initial=0.10,
        validators=[validation.validate_greaterthan0])
    osed = forms.FloatField(
        label=mark_safe('Porosity of Sediment, K<sub>d</sub>'),
        initial=0.509,
        validators=[validation.validate_greaterthan0])
    kd = forms.FloatField(
        label=mark_safe('Water-Sediment Partitioning Coefficient, K<sub>oc</sub> (L/kg)'),
        initial=727,
        validators=[validation.validate_greaterthan0])
