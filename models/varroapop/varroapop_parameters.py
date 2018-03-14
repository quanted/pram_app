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
RQScheduled_CHOICES = (('true', 'scheduled'), ('false', 'automatic'))
RQonce_CHOICES = (('true', 'once on date'), ('false', 'annually on date'))
enable_mites_CHOICES = (('true', 'yes'), ('false', 'no'))
ImmEnabled_CHOICES = (('true', 'yes'), ('false', 'no'))
ImmType_CHOICES = (('Logarithmic', 'logarithmic'), ('Exponential', 'exponential'), ('Polynomial', 'polynomial'),
                   ('Sine', 'sine'), ('Cosine', 'cosine'), ('Tangent', 'tangent'))
enable_pesticides_CHOICES = (('true', 'yes'), ('false', 'no'))


class VarroapopInp_colony(forms.Form):
    SimStart = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 3, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        #validators=[] #need to validate that it's within range of weather file
    SimEnd = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 8, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        #validators=[] #need to validate that it's within range of weather file
    ICQueenStrength = forms.FloatField(
        required=True,
        label='Queen strength (1-5)',
        initial=3.5,
        widget=forms.NumberInput(attrs={'id': 'form_ICQueenStrength', 'step': '0.1'}),
        validators=[validation.validate_range(min=1,max=5)])
    ICForagerLifespan = forms.IntegerField(
        required=True,
        label='Forager lifespan (days)',
        initial=7,
        widget=forms.NumberInput(attrs={'id': 'form_ICForagerLifespan', 'step': '1'}),
        validators=[validation.validate_range(min=4,max=16)])
    ICForagerProp = forms.FloatField(  # NOTE: need to get the right parameter name for VarroaPop
        required=True,
        label='Active forager proportion',
        initial=.3,
        widget=forms.NumberInput(attrs={'id': 'form_ICForagerProp', 'step': '0.01'}),
        validators=[validation.validate_range01])
    ICWorkerAdult = forms.IntegerField(
        required=True,
        label='Initial worker adult population',
        initial=1000,
        validators = [validation.validate_positive])
    ICWorkerBrood = forms.IntegerField(
        required=True,
        label='Initial worker capped brood population',
        initial=5000,
        validators=[validation.validate_positive])
    ICWorkerLarave = forms.IntegerField(
        required=True,
        label='Initial worker larvae population',
        initial=3000,
        validators=[validation.validate_positive])
    ICWorkerEggs = forms.IntegerField(
        required=True,
        label='Initial worker egg population',
        initial=3000,
        validators=[validation.validate_positive])
    ICDroneAdult = forms.IntegerField(
        required=True,
        label='Initial drone adult population',
        initial=0,
        validators=[validation.validate_positive])
    ICDroneBrood = forms.IntegerField(
        required=True,
        label='Initial drone capped brood population',
        initial=0,
        validators=[validation.validate_positive])
    ICDroneLarave = forms.IntegerField(
        required=True,
        label='Initial drone larvae population',
        initial=100,
        validators=[validation.validate_positive])
    ICDroneEggs = forms.IntegerField(
        required=True,
        label='Initial drone egg population',
        initial=100,
        validators=[validation.validate_positive])
    RQEnableReQueen = forms.ChoiceField(
        required=True,
        label='Enable Re-queening?',
        choices=RQEnableReQueen_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    RQScheduled = forms.ChoiceField(
        required=True,
        label='Re-queen on scheduled date or automatically?',
        choices=RQScheduled_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield],
        disabled=True)
    RQReQueenDate = forms.DateField(
        required=True,
        label='Re-queening date',
        initial=date(2015,6,25),#'06/25/2015',
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        #validators=[] #need to validate that it's between start and end dates
    RQonce = forms.ChoiceField(
        required=True,
        label='Re-queen once on date, or annually on date?',
        choices=RQonce_CHOICES,
        initial='true',
        validators=[validation.validate_choicefield],
        disabled=True)

class VarroapopInp_mites(forms.Form):
    enable_mites = forms.ChoiceField(
        required=True,
        label='Enable Varroa mites?',
        choices=enable_mites_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    ImmEnabled = forms.ChoiceField(
        required=True,
        label='Enable Varroa mite immigration?',
        choices=enable_mites_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield],
        disabled=True)
    ImmType = forms.ChoiceField(
        required=True,
        label='Mite immigration profile',
        choices=ImmType_CHOICES,
        initial='Logarithmic',
        validators=[validation.validate_choicefield],
        disabled=True)
    ImmStart = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 4, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        #validators=[] #need to validate that it's within range of weather file
    ImmEnd = forms.DateField(
        required=True,
        label='Simulation start date',
        initial=date(2015, 8, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(years=(2015,)),
        disabled=True)
        # validators=[] #need to validate that it's within range of weather file
    TotalImmMites = forms.FloatField(
        required=False,
        label='Total # of mites immigrating',
        validators=[validation.validate_positive],
        disabled=True)
    PctImmMitesResistant = forms.FloatField(
        required=False,
        initial=10,
        label='Percent of mites resistant to miticide',
        validators=[validation.validate_range0100],
        disabled=True)
    ICWorkerAdultInfest = forms.FloatField(
        required=False,
        initial=0,
        label='Percent of worker adults infested',
        validators=[validation.validate_range0100],
        disabled=True)

class VarroapopInp_pesticide(forms.Form):
    enable_pesticides = forms.ChoiceField(
        required=True,
        label='Enable pesticide application?',
        choices=enable_pesticides_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        initial='VarroaPop Example',
        disabled=True)

# Combined Form Classes for Validation
class VarroapopInp(VarroapopInp_colony, VarroapopInp_mites, VarroapopInp_pesticide):
    pass
