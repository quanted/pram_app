"""
.. module:: earthworm_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from pram_app.models.forms import validation


class EarthwormInp(forms.Form):
    version = forms.ChoiceField(
        choices=(('1.0', '1.0'),),
        label='Version',
        initial='1.0')
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        initial='Earthworm Example',
        required=True)
    pc_code = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='055459')
    k_ow = forms.FloatField(
        label=mark_safe('Octanol to water partition coefficient K<sub>OW</sub>'),
        initial=57544,
        validators=[validation.validate_greaterthan0])
    l_f_e = forms.FloatField(
        label='Lipid fraction of earthworm L',
        initial=0.01,
        validators=[validation.validate_range01])
    c_s = forms.FloatField(
        label=mark_safe('Chemical concentration in soil C<sub>S</sub> (mol/m<sup>3</sup>)'),
        initial=0.055,
        validators=[validation.validate_greaterthan0])
    k_d = forms.FloatField(
        label=mark_safe('Soil partitioning coefficient K<sub>d</sub> (cm<sup>3</sup>/g)'),
        initial=69,
        validators=[validation.validate_greaterthan0])
    p_s = forms.FloatField(
        label=mark_safe('Bulk density of soil &#961;<sub>s</sub> (g/cm<sup>3</sup>)'),
        initial=1.7,
        validators=[validation.validate_greaterthan0])

# updated version of earthworm model uses EFED equation which does not include c_w, m_w, and p_e as inputs
# c_w = forms.FloatField(
# 		label = mark_safe('Chemical concentration in pore water of soil C<sub>W</sub> (mol/m<sup>3</sup>)'),
# 		initial = 0.000447,
# 		validators=[validation.validate_greaterthan0])
# m_w = forms.FloatField(
# 		label = mark_safe('Molecular weight of chemical MW (g/mol)'),
# 		initial = 406.9,
# 		validators=[validation.validate_greaterthan0])
# p_e = forms.FloatField(
# 		label = mark_safe('Density of earthworm &#961;<sub>E</sub> (kg/m<sup>3</sup>)'),
# 		initial = 1000,
# 		validators=[validation.validate_greaterthan0])
