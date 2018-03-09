"""
.. module:: beerex_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from pram_app.models.forms import validation
from django.core import validators
from datetime import date

# SELECT_VERSION = (('1.0', '1.0'),)
RQEnableReQueen_CHOICES = (('true', 'yes'), ('false', 'no'))
RQScheduled_CHOICES = (('true', 'automatic'), ('false', 'scheduled'))
RQonce_CHOICES = (('true','once on date'), ('false', 'annually on date'))
enable_mites_CHOICES = (('true', 'yes'), ('false', 'no'))
ImmEnabled_CHOICES = (('true', 'yes'), ('false', 'no'))
ImmType_CHOICES = (('Logarithmic', 'logarithmic'), ('Exponential', 'exponential'), ('Polynomial', 'polynomial'),
                   ('Sine', 'sine', 'Cosine', 'cosine'), ("Tangent", "tangent"))


class VarroaPopInp(forms.Form):
    SimStart = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 3, 25),  # '03/25/2015
        input_formats=['%m/%d/%Y'],
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        #validators=[] #need to validate that it's within range of weather file
    SimEnd = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 8, 25),  # '03/25/2015
        input_formats=['%m/%d/%Y'],
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        #validators=[] #need to validate that it's within range of weather file
    ICQueenStrength = forms.FloatField(
        required=True,
        label='Queen strength (1-5)',
        initial=3.5,
        widget=forms.NumberInput(attrs={'id': 'form_ICQueenStrength', 'step': '0.1',
                                        'min': '1', 'max': '5'}),
        validators=[validators.MinValueValidator(1.0),validators.MaxValueValidator(5.0)])
    ICForagerLifespan = forms.IntegerField(
        required=True,
        label='Forager lifespan (days)',
        initial=7,
        widget=forms.NumberInput(attrs={'id': 'form_ICForagerLifespan', 'step': '1',
                                        'min': '4', 'max': '16'}),
        validators=[validators.MinValueValidator(4), validators.MaxValueValidator(16)])
    ICForagerProp = forms.FloatField(  #NOTE: need to get the right parameter name for VarroaPop
        required=True,
        label='Active forager proportion',
        initial=.3,
        widget=forms.NumberInput(attrs={'id': 'form_ICForagerProp', 'step': '0.01',
                                        'min': '0', 'max': '1'}),
        validators=[validation.validate_range01])
    ICWorkerAdult = forms.IntegerField(
        required=True,
        label='Initial worker adult population',
        initial=1000,
        validators = [validation.validate_greaterthan0])
    ICWorkerBrood = forms.IntegerField(
        required=True,
        label='Initial worker capped brood population',
        initial=5000,
        validators=[validation.validate_greaterthan0])
    ICWorkerLarave = forms.IntegerField(
        required=True,
        label='Initial worker larvae population',
        initial=3000,
        validators=[validation.validate_greaterthan0])
    ICWorkerEggs = forms.IntegerField(
        required=True,
        label='Initial worker egg population',
        initial=3000,
        validators=[validation.validate_greaterthan0])
    ICDroneAdult = forms.IntegerField(
        required=True,
        label='Initial drone adult population',
        initial=0,
        validators=[validation.validate_greaterthan0])
    ICDroneBrood = forms.IntegerField(
        required=True,
        label='Initial drone capped brood population',
        initial=0,
        validators=[validation.validate_greaterthan0])
    ICDroneLarave = forms.IntegerField(
        required=True,
        label='Initial drone larvae population',
        initial=100,
        validators=[validation.validate_greaterthan0])
    ICDroneEggs = forms.IntegerField(
        required=True,
        label='Initial drone egg population',
        initial=100,
        validators=[validation.validate_greaterthan0])
    RQEnableReQueen = forms.ChoiceField(
        required=True,
        label='Enable Re-queening?',
        choices=RQEnableReQueen_CHOICES,
        initial='yes',
        validators=[validation.validate_choicefield])
    RQScheduled = forms.ChoiceField(
        required=True,
        label='Re-queen on scheduled date or automatically?',
        choices=RQScheduled_CHOICES,
        initial='once on date',
        validators=[validation.validate_choicefield])
    RQReQueenDate = forms.DateField(
        required=True,
        label='Re-queening date',
        initial=date(2015,6,25),#'06/25/2015',
        input_formats=['%m/%d/%Y'],
        widget=forms.SelectDateWidget(years=(2015,)))
        #validators=[] #need to validate that it's between start and end dates
    RQonce = forms.ChoiceField(
        required=True,
        label='Re-queen once on date, or annually on date?',
        choices=RQonce_CHOICES,
        initial='once on date',
        validators=[validation.validate_choicefield])

class VarroaPopInpMites(forms.Form):
    enable_mites = forms.ChoiceField(
        required=True,
        label='Enable Varroa mites?',
        choices=enable_mites_CHOICES,
        initial='yes',
        validators=[validation.validate_choicefield])
    ImmEnabled = forms.ChoiceField(
        required=True,
        label='Enable Varroa mite immigration?',
        choices=ImmEnabled_CHOICES,
        initial='logarithmic',
        validators=[validation.validate_choicefield])
    ImmType = forms.ChoiceField(
        required=True,
        label='Mite immigration profile',
        choices=ImmType_CHOICES,
        initial='yes',
        validators=[validation.validate_choicefield])
    ImmStart = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 4, 25),  # '03/25/2015
        input_formats=['%m/%d/%Y'],
        widget=forms.SelectDateWidget(years=(2015,)))
    # validators=[] #need to validate that it's within range of weather file
    ImmEnd = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 8, 25),  # '03/25/2015
        input_formats=['%m/%d/%Y'],
        widget=forms.SelectDateWidget(years=(2015,)))
    # validators=[] #need to validate that it's within range of weather file
    TotalImmMites = forms.FloatField(
        required=False,
        label='Total # of mites immigrating',
        validators=[validation.validate_greaterthan0])
    PctImmMitesResistant = forms.FloatField(
        required=False,
        initial=10,
        label='Percent of mites resistant to miticide',
        validators=[validation.validate_range0100])
    ICWorkerAdultInfest = forms.FloatField(
        required=False,
        initial=0,
        label='Percent of worker adults infested',
        validators=[validation.validate_range0100])
