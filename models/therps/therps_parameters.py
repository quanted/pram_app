"""
.. module:: therps_parameters
   :synopsis: A useful module indeed.
"""
from django import forms

from ubertool_app.models.forms import validation

Species_of_the_tested_bird_CHOICES = (
    ('Bobwhite quail', 'Bobwhite quail'), ('Mallard duck', 'Mallard duck'), ('Other', 'Other'))
SELECT_VERSION = (('1.0', '1.0'),)


class therpsInp_chem(forms.Form):
    version = forms.ChoiceField(
        choices=SELECT_VERSION,
        label='Version',
        initial='1.0')
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        initial='T-Herps Example')
    pc_code = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='00')
    use = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        initial='Dried shelled beans (except soybeans)')
    formu_name = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        initial='NA')
    percent_act_ing = forms.FloatField(
        label='% a.i. (%)',
        initial=100,
        validators=[validation.validate_range0100])
    foliar_diss_hlife = forms.FloatField(
        label='Foliar dissipation half-life (days)',
        initial=35,
        validators=[validation.validate_range_1_365])
    num_apps = forms.FloatField(
        label='Number of applications',
        initial=2,
        validators=[validation.validate_integer])
    app_interval = forms.FloatField(
        label='Interval between applications (days)',
        initial=7,
        validators=[validation.validate_integer])
    application_rate = forms.FloatField(
        label='Application rate (lbs a.i./A)',
        initial=0.18,
        validators=[validation.validate_positive])


class therpsInp_bird(forms.Form):
    ld50_bird = forms.FloatField(
        label='Avian LD50 (mg/kg-bw)',
        initial=2000,
        validators=[validation.validate_positive])
    species_of_the_tested_bird_avian_ld50 = forms.ChoiceField(
        label='Test species (for Avian LD50)',
        choices=Species_of_the_tested_bird_CHOICES,
        initial='Bobwhite quail')
    tw_bird_ld50 = forms.FloatField(
        label='Weight (g)',
        initial='178',
        validators=[validation.validate_positive])
    lc50_bird = forms.FloatField(
        label='Avian LC50 (mg/kg-diet)',
        initial=2457,
        validators=[validation.validate_positive])
    species_of_the_tested_bird_avian_lc50 = forms.ChoiceField(
        label='Test species (for Avian LC50)',
        choices=Species_of_the_tested_bird_CHOICES,
        initial='Bobwhite quail')
    tw_bird_lc50 = forms.FloatField(
        label='Weight (g)',
        initial='178',
        validators=[validation.validate_positive])
    noaec_bird = forms.FloatField(
        label='Avian NOAEC (mg/kg-diet)',
        initial=100,
        validators=[validation.validate_positive])
    species_of_the_tested_bird_avian_noaec = forms.ChoiceField(
        label='Test species (for Avian NOAEC)',
        choices=Species_of_the_tested_bird_CHOICES,
        initial='Bobwhite quail')
    tw_bird_noaec = forms.FloatField(
        label='Weight (g)',
        initial='178',
        validators=[validation.validate_positive])
    noael_bird = forms.FloatField(
        label='Avian NOAEL (mg/kg-bw)',
        initial=7.8,
        validators=[validation.validate_positive])
    species_of_the_tested_bird_avian_noael = forms.ChoiceField(
        label='Test species (for Avian NOAEL)',
        choices=Species_of_the_tested_bird_CHOICES,
        initial='Bobwhite quail')
    tw_bird_noael = forms.FloatField(
        label='Weight (g)',
        initial='178',
        validators=[validation.validate_positive])
    # Species_of_the_tested_bird = forms.ChoiceField(
    # label='Species of the tested bird', choices=Species_of_the_tested_bird_CHOICES, initial='Bobwhite quail')
    # body_weight_of_the_tested_bird=forms.FloatField(
    # label='Body weight of the tested bird (g)', initial=178)
    mineau_sca_fact = forms.FloatField(
        label='Mineau scaling factor',
        initial=1.15,
        validators=[validation.validate_greaterthanequalto1])


class therpsInp_herp(forms.Form):
    aw_herp_sm = forms.FloatField(
        label='Body weight of assessed small herptile (g)',
        initial=2.0,
        validators=[validation.validate_positive])
    awc_herp_sm = forms.FloatField(
        label="Water content of the assessed small herptile's diet (%)",
        initial=85,
        validators=[validation.validate_range0100])
    aw_herp_md = forms.FloatField(
        label='Body weight of assessed medium herptile (g)',
        initial=20,
        validators=[validation.validate_positive])
    awc_herp_md = forms.FloatField(
        label="Water content of the assessed medium herptile's diet (%)",
        initial=85,
        validators=[validation.validate_range0100])
    aw_herp_lg = forms.FloatField(
        label='Body weight of assessed large herptile (g)',
        initial=200,
        validators=[validation.validate_positive])
    awc_herp_lg = forms.FloatField(
        label="Water content of the assessed large herptile's diet (%)",
        initial=85,
        validators=[validation.validate_range0100])
    bw_frog_prey_mamm = forms.FloatField(
        label='Weight of the mammal consumed by assessed frog (g)',
        initial=15,
        validators=[validation.validate_positive])
    bw_frog_prey_herp = forms.FloatField(
        label='Weight of the herptile  consumed by assessed frog (g)',
        initial=15,
        validators=[validation.validate_positive])


class TherpsInp(therpsInp_chem, therpsInp_bird, therpsInp_herp):
    pass
