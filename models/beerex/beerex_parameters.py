"""
.. module:: beerex_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation

application_method_CHOICES = (('soil application', 'soil application'), ('tree trunk', 'tree trunk'),
                              ('foliar spray', 'foliar spray'), ('seed treatment', 'seed treatment'))
empirical_residue_CHOICES = (('yes', 'yes'), ('no', 'no'))
# SELECT_VERSION = (('1.0', '1.0'),)


class beerexInp_chemical(forms.Form):
    # version = forms.ChoiceField(
    #     choices=SELECT_VERSION,
    #     label='Version',
    #     initial='1.0')
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        initial='Beerex Example',
        required=True)
    crop_type = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        label='Crop Type',
        initial='corn',
        required=False)
    application_method = forms.ChoiceField(
        required=True,
        label='Pesticide application method',
        choices=application_method_CHOICES,
        initial='soil application',
        validators=[validation.validate_choicefield])
    log_kow = forms.FloatField(
        required=False,
        label='Log K<sub>OW</sub> for soil application method (@ 21&deg;C)',
        initial=0.56820172,
        validators=[validation.validate_greaterthan0])
    koc = forms.FloatField(
        required=False,
        label='K<sub>OC</sub> for soil application method (L/kg)',
        initial=318,
        validators=[validation.validate_greaterthan0])
    application_rate = forms.FloatField(
        required=True,
        label=mark_safe('Pesticide application rate (lb a.i./A)'),
        initial=3.0,
        validators=[validation.validate_greaterthan0])
    mass_tree_vegetation = forms.FloatField(
        required=False,
        label='Mass of tree vegetation for tree trunk application method (kg-wet weight)',
        initial=856.2,
        validators=[validation.validate_greaterthan0])


class beerexInp_toxicity(forms.Form):
    adult_contact_ld50 = forms.FloatField(
        required=True,
        label='Adult contact LD50 (ug a.i./bee)',
        initial=0.043,
        validators=[validation.validate_positive])
    adult_oral_ld50 = forms.ChoiceField(
        required=True,
        label='Adult oral LD50 (ug a.i./bee)',
        initial=0.0039,
        validators=[validation.validate_greaterthan0])
    adult_oral_noael = forms.FloatField(
        required=True,
        label='Adult oral NOAEL (ug a.i./bee)',
        initial=0.00016,
        validators=[validation.validate_greaterthan0])
    larval_ld50 = forms.FloatField(
        required=True,
        label='Larval LD50 (ug a.i./bee)',
        initial=0.005,
        validators=[validation.validate_greaterthan0])
    larval_noael = forms.FloatField(
        required=True,
        label='Larval NOAEL (ug a.i./bee)',
        initial=0.0018,
        validators=[validation.validate_greaterthan0])
    empirical_residue = forms.ChoiceField(
        required=True,
        label='Empirical data for pesticide residue in pollen, nectar, or jelly',
        choices=empirical_residue_CHOICES,
        initial='no',
        validators=[validation.validate_choicefield])
    empirical_pollen = forms.FloatField(
        required=False,
        label='Empirical data of pesticide residue in pollen (ug a.i./mg)',
        initial=0.034,
        validators=[validation.validate_greaterthan0])
    empirical_nectar = forms.FloatField(
        required=False,
        label='Empirical data of pesticide residue in nectar (ug a.i./mg)',
        initial=0.27,
        validators=[validation.validate_greaterthan0])
    empirical_jelly = forms.FloatField(
        required=False,
        label='Empirical data of pesticide residue in jelly (ug a.i./mg)',
        initial=0.0006,
        validators=[validation.validate_greaterthan0])


class beerexInp_exposure(forms.Form):
    lw1_jelly = forms.FloatField(
        required=True,
        label='Larval worker day 1 jelly consumption rate (mg/day)',
        initial=1.9,
        validators=[validation.validate_greaterthan0])
    lw2_jelly = forms.FloatField(
        required=True,
        label='Larval worker day 2 jelly consumption rate (mg/day)',
        initial=9.4,
        validators=[validation.validate_greaterthan0])
    lw3_jelly = forms.FloatField(
        required=True,
        label='Larval worker day 3 jelly consumption rate (mg/day)',
        initial=19,
        validators=[validation.validate_greaterthan0])
    lw4_nectar = forms.FloatField(
        required=True,
        label='Larval worker day 4 nectar consumption rate (mg/day)',
        initial=60,
        validators=[validation.validate_greaterthan0])
    lw4_pollen = forms.FloatField(
        required=True,
        label='Larval worker day 4 pollen consumption rate (mg/day)',
        initial=1.8,
        validators=[validation.validate_greaterthan0])
    lw5_nectar = forms.FloatField(
        required=True,
        label='Larval worker day 5 nectar consumption rate (mg/day)',
        initial=120,
        validators=[validation.validate_greaterthan0])
    lw5_pollen = forms.FloatField(
        required=True,
        label='Larval worker day 5 pollen consumption rate (mg/day)',
        initial=3.6,
        validators=[validation.validate_greaterthan0])
    ld6_nectar = forms.FloatField(
        required=True,
        label='Larval worker day 6 nectar consumption rate (mg/day)',
        initial=130,
        validators=[validation.validate_greaterthan0])
    ld6_pollen = forms.FloatField(
        required=True,
        label='Larval worker day 6 pollen consumption rate (mg/day)',
        initial=3.6,
        validators=[validation.validate_greaterthan0])
    lq1_jelly = forms.FloatField(
        required=True,
        label='Larval queen day 1 jelly consumption rate (mg/day)',
        initial=1.9,
        validators=[validation.validate_greaterthan0])
    lq2_jelly = forms.FloatField(
        required=True,
        label='Larval queed day 2 jelly consumption rate (mg/day)',
        initial=9.4,
        validators=[validation.validate_greaterthan0])
    lq3_jelly = forms.FloatField(
        required=True,
        label='Larval queen day 3 jelly consumption rate (mg/day)',
        initial=23,
        validators=[validation.validate_greaterthan0])
    lq4_jelly = forms.FloatField(
        required=True,
        label='Larval queen day 4 jelly consumption rate (mg/day)',
        initial=141,
        validators=[validation.validate_greaterthan0])
    aw_cell_nectar = forms.FloatField(
        required=True,
        label='Adult worker cell nectar consumption rate (mg/day)',
        initial=60,
        validators=[validation.validate_greaterthan0])
    aw_cell_pollen = forms.FloatField(
        required=True,
        label='Adult worker cell pollen consumption rate (mg/day)',
        initial=6.65,
        validators=[validation.validate_greaterthan0])
    aw_brood_nectar = forms.FloatField(
        required=True,
        label='Adult worker brood nectar consumption rate (mg/day)',
        initial=140,
        validators=[validation.validate_greaterthan0])
    aw_brood_pollen = forms.FloatField(
        required=True,
        label='Adult worker brood pollen consumption rate (mg/day)',
        initial=9.6,
        validators=[validation.validate_greaterthan0])
    aw_comb_nectar = forms.FloatField(
        required=True,
        label='Adult worker comb nectar consumption rate (mg/day)',
        initial=60,
        validators=[validation.validate_greaterthan0])
    aw_comb_pollen = forms.FloatField(
        required=True,
        label='Adult worker comb pollen consumption rate (mg/day)',
        initial=1.7,
        validators=[validation.validate_greaterthan0])
    aw_fpollen_nectar = forms.FloatField(
        required=True,
        label='Adult pollen forager nectar consumption rate (mg/day)',
        initial=43.5,
        validators=[validation.validate_greaterthan0])
    aw_fpollen_pollen = forms.FloatField(
        required=True,
        label='Adult pollen forager pollen consumption rate (mg/day)',
        initial=0.041,
        validators=[validation.validate_greaterthan0])
    aw_fnectar_nectar = forms.FloatField(
        required=True,
        label='Adult nectar forager nectar consumption rate (mg/day)',
        initial=292,
        validators=[validation.validate_greaterthan0])
    aw_fnectar_pollen = forms.FloatField(
        required=True,
        label='Adult nectar forager pollen consumption rate (mg/day)',
        initial=0.041,
        validators=[validation.validate_greaterthan0])
    aw_winter_nectar = forms.FloatField(
        required=True,
        label='Adult worker winter nectar consumption rate (mg/day)',
        initial=29,
        validators=[validation.validate_greaterthan0])
    aw_winter_pollen = forms.FloatField(
        required=True,
        label='Adult worker winter pollen consumption rate (mg/day)',
        initial=2,
        validators=[validation.validate_greaterthan0])
    ad_nectar = forms.FloatField(
        required=True,
        label='Adult drone nectar consumption rate (mg/day)',
        initial=235,
        validators=[validation.validate_greaterthan0])
    ad_pollen = forms.FloatField(
        required=True,
        label='Adult drone pollen consumption rate (mg/day)',
        initial=0.0002,
        validators=[validation.validate_greaterthan0])
    aq_jelly = forms.FloatField(
        required=True,
        label='Adult queen jelly consumption rate (mg/day)',
        initial=525,
        validators=[validation.validate_greaterthan0])


class beerexInp(beerexInp_chemical, beerexInp_exposure, beerexInp_toxicity):
    pass
