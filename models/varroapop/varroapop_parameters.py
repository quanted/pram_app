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
application_type_CHOICES = (('Foliar spray', 'Foliar spray'), ('Soil', 'Soil'), ('Seed treatment', 'Seed treatment'))
VTEnable_CHOICES = (('true', 'yes'), ('false', 'no'))
NeedResourcesToLive_CHOICES = (('true', 'yes'), ('false', 'no'))
SupPollenEnable_CHOICES = (('true', 'yes'), ('false', 'no'))
SupNectarEnable_CHOICES = (('true', 'yes'), ('false', 'no'))


class VarroapopInp_colony(forms.Form):
    SimStart = forms.DateField(
        label='Simulation start date',
        initial=date(2015, 3, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(years=tuple(range(1991,2016))),
        validators=[validation.validate_date_range(min=date(1991,1,1),max=date(2015,12,31))])
    SimEnd = forms.DateField(
        label='Simulation start date',
        initial=date(2015, 8, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(years=tuple(range(1991, 2016))),
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    ICQueenStrength = forms.FloatField(
        label='Queen strength (1-5)',
        initial=3.5,
        widget=forms.NumberInput(attrs={'id': 'form_ICQueenStrength', 'step': '0.1'}),
        validators=[validation.validate_range(min=1,max=5)])
    ICForagerLifespan = forms.IntegerField(
        label='Forager lifespan (days)',
        initial=7,
        widget=forms.NumberInput(attrs={'id': 'form_ICForagerLifespan', 'step': '1'}),
        validators=[validation.validate_range(min=4,max=16)])
    ForagerMaxProp = forms.FloatField(
        label='Active forager proportion',
        initial=.3,
        widget=forms.NumberInput(attrs={'id': 'form_ICForagerProp', 'step': '0.01'}),
        validators=[validation.validate_range01])
    ICWorkerAdult = forms.IntegerField(
        label='Initial worker adult population',
        initial=1000,
        validators = [validation.validate_positive])
    ICWorkerBrood = forms.IntegerField(
        label='Initial worker capped brood population',
        initial=5000,
        validators=[validation.validate_positive])
    ICWorkerLarave = forms.IntegerField(
        label='Initial worker larvae population',
        initial=3000,
        validators=[validation.validate_positive])
    ICWorkerEggs = forms.IntegerField(
        label='Initial worker egg population',
        initial=3000,
        validators=[validation.validate_positive])
    ICDroneAdult = forms.IntegerField(
        label='Initial drone adult population',
        initial=0,
        validators=[validation.validate_positive])
    ICDroneBrood = forms.IntegerField(
        label='Initial drone capped brood population',
        initial=0,
        validators=[validation.validate_positive])
    ICDroneLarave = forms.IntegerField(
        label='Initial drone larvae population',
        initial=100,
        validators=[validation.validate_positive])
    ICDroneEggs = forms.IntegerField(
        label='Initial drone egg population',
        initial=100,
        validators=[validation.validate_positive])
    RQEnableReQueen = forms.ChoiceField(
        label='Enable Re-queening?',
        choices=RQEnableReQueen_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    RQScheduled = forms.ChoiceField(
        label='Re-queen on scheduled date or automatically?',
        choices=RQScheduled_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    RQReQueenDate = forms.DateField(
        label='Re-queening date',
        initial=date(2015,6,25),#'06/25/2015',
        widget=forms.SelectDateWidget(years=tuple(range(1991,2016))),
        validators=[validation.validate_date_range(min=date(1991,1,1),max=date(2015,12,31))])
    RQonce = forms.ChoiceField(
        label='Re-queen once on date, or annually on date?',
        choices=RQonce_CHOICES,
        initial='true',
        validators=[validation.validate_choicefield])

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('SimStart')
        end_date = cleaned_data.get('SimEnd')
        requeen_date = cleaned_data.get('RQReQueenDate')
        requeen_enabled = cleaned_data.get('RQEnableReQueen')
        scheduled = cleaned_data.get('RQScheduled')
        if(requeen_enabled == 'true' and scheduled == 'true'):
            if(not(start_date <= requeen_date <= end_date)):
                self.add_error('RQReQueenDate', 'Requeening date should be between simulation start and end dates')


class VarroapopInp_mites(forms.Form):
    enable_mites = forms.ChoiceField(
        label='Enable Varroa mites?',
        choices=enable_mites_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    ICWorkerAdultInfest = forms.FloatField(
        initial=0,
        label='Percent of worker adults infested',
        validators=[validation.validate_range0100])
    ICWorkerBroodInfest = forms.FloatField(
        initial=0,
        label='Percent of worker brood infested',
        validators=[validation.validate_range0100])
    ICDroneAdultInfest = forms.FloatField(
        initial=0,
        label='Percent of drone adults infested',
        validators=[validation.validate_range0100])
    ICDroneBroodInfest = forms.FloatField(
        initial=0,
        label='Percent of drone brood infested',
        validators=[validation.validate_range0100])
    ICWorkerMiteOffspring = forms.FloatField(
        initial=0,
        label='Offspring per mite on workers',
        validators=[validation.validate_positive])
    ICWorkerMiteSurvivorship = forms.FloatField(
        initial=0,
        label='Mite survivorship on workers (%)',
        validators=[validation.validate_range0100])
    ICDroneMiteOffspring = forms.FloatField(
        initial=0,
        label='Offspring per mite on drones',
        validators=[validation.validate_positive])
    ICDroneMiteSurvivorship = forms.FloatField(
        initial=0,
        label='Mite survivorship on drones (%)',
        validators=[validation.validate_range0100])
    ImmEnabled = forms.ChoiceField(
        label='Enable Varroa mite immigration?',
        choices=enable_mites_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    ImmType = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'mite_imm'}),
        label='Mite immigration profile',
        choices=ImmType_CHOICES,
        initial='Logarithmic',
        validators=[validation.validate_choicefield])
    ImmStart = forms.DateField(
        label='Immigration start date',
        initial=date(2015, 4, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(attrs={'class': 'mite_imm'}, years=tuple(range(1991,2016))))
        #validators=[] #need to validate that it's within range of weather file
    ImmEnd = forms.DateField(
        label='Immigration end date',
        initial=date(2015, 8, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(attrs={'class': 'mite_imm'},years=tuple(range(1991,2016))))
        # validators=[] #need to validate that it's within range of weather file
    TotalImmMites = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'mite_imm'}),
        label='Total # of mites immigrating',
        initial=0,
        validators=[validation.validate_positive])
    PctImmMitesResistant = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'mite_imm'}),
        initial='10',
        label='Percent of mites resistant to miticide',
        validators=[validation.validate_range0100])
    VTEnable = forms.ChoiceField(
        label='Enable Varroa mite treatment?',
        choices= VTEnable_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    VTTreatmentStart = forms.DateField(
        label='Miticide start date',
        initial=date(2015, 7, 25),  # '03/25/2015
        widget=forms.SelectDateWidget(attrs={'class': 'mite_treat'}, years=tuple(range(1991,2016))))
    # validators=[] #need to validate that it's within range of weather file
    VTTreatmentDuration = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'mite_treat'}),
        initial='30',
        label='Miticide duration (days)',
        validators=[validation.validate_positive])
    VTMortality = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'mite_treat'}),
        initial='10',
        label='Miticide treatment mite mortality (%)',
        validators=[validation.validate_range0100])
    InitMitePctPresistant = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'mite_treat'}),
        initial='10',
        label='Mites resistant to miticide (%)',
        validators=[validation.validate_range0100])


class VarroapopInp_chemical(forms.Form):
    enable_pesticides = forms.ChoiceField(
        label='Enable pesticide application?',
        choices=enable_pesticides_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    chemical_name = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        initial='VarroaPop Example')
    application_type = forms.ChoiceField(
        label='Application method',
        choices=application_type_CHOICES,
        initial='Foliar spray',
        validators=[validation.validate_choicefield])
    foliar_enable = forms.ChoiceField(
        widget=forms.HiddenInput,
        choices= (('true', 'true'), ('false', 'false')),
        initial='false',
        validators=[validation.validate_choicefield])
    soil_enable = forms.ChoiceField(
        widget=forms.HiddenInput,
        choices=(('true', 'true'), ('false', 'false')),
        initial='false',
        validators=[validation.validate_choicefield])
    seed_enable = forms.ChoiceField(
        widget=forms.HiddenInput,
        choices=(('true', 'true'), ('false', 'false')),
        initial='false',
        validators=[validation.validate_choicefield])
    ar_lb = forms.FloatField(  #crosswalk name - rename for VP EAppRate
        widget= forms.TextInput(attrs={'class':'foliar'}),
        initial='1.0',
        label='Application rate (lbs a.i./A)',
        validators=[validation.validate_positive])
    FoliarAppDate = forms.DateField(
        label='Application date',
        initial=date(2015,4,25),
        widget=forms.SelectDateWidget(attrs={'class': 'foliar'}, years=tuple(range(1991,2016))), # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991,1,1),max=date(2015,12,31))])
    FoliarForageBegin= forms.DateField(
        label='Exposure start date',
        initial=date(2015,4,25),
        widget=forms.SelectDateWidget(attrs={'class': 'foliar'}, years=tuple(range(1991,2016))), # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991,1,1),max=date(2015,12,31))])
    FoliarForageEnd= forms.DateField(
        label='Exposure end date',
        initial=date(2015,5,25),
        widget=forms.SelectDateWidget(attrs={'class': 'foliar'}, years=tuple(range(1991,2016))), # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991,1,1),max=date(2015,12,31))])
    AIContactFactor = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'foliar'}),
        initial='1.0',
        label='Contact dose factor',  # TODO Units??
        validators=[validation.validate_positive])
    SoilForageBegin = forms.DateField(
        label='Exposure start date',
        initial=date(2015, 4, 25),
        widget=forms.SelectDateWidget(attrs={'class': 'soil'}, years=tuple(range(1991, 2016))),  # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    SoilForageEnd = forms.DateField(
        label='Exposure end date',
        initial=date(2015, 5, 25),
        widget=forms.SelectDateWidget(attrs={'class': 'soil'}, years=tuple(range(1991, 2016))),  # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    l_kow = forms.FloatField( # crosswalk name - rename for VP AIKOW and un log transform (?)
        widget=forms.TextInput(attrs={'class': 'soil'}),
        initial='1.0',
        label='log Kow',
        validators=[validation.validate_positive])
    k_oc = forms.FloatField(  # crosswalk name - rename for VP AIKOC
        widget=forms.TextInput(attrs={'class': 'soil'}),
        initial='1.0',
        label='Koc (ml/g OC)',
        validators=[validation.validate_positive])
    Theta = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'soil'}),
        initial='.20',
        label='Volumetric soil water content ('+u'\u03B8'+')',
        validators=[validation.validate_range0100])
    P = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'soil'}),
        initial='1.0',
        label='Soil bulk density (g/cm3)',
        validators=[validation.validate_positive])
    Foc = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'soil'}),
        initial='0.2',
        label='Soil fraction of organic carbon (foc)',
        validators=[validation.validate_range0100])
    SeedForageBegin = forms.DateField(
        label='Exposure start date',
        initial=date(2015, 4, 25),  # '06/25/2015',
        widget=forms.SelectDateWidget(attrs={'class': 'seed'}, years=tuple(range(1991, 2016))),  # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    SeedForageEnd = forms.DateField(
        label='Exposure end date',
        initial=date(2015, 5, 25),  # '06/25/2015',
        widget=forms.SelectDateWidget(attrs={'class': 'seed'}, years=tuple(range(1991, 2016))),  # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    ESeedConcentration = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'seed'}),
        initial='25',
        label='Active ingredient concentration (ug/g)',
        validators=[validation.validate_positive])
    AIHalfLife = forms.FloatField(
        initial='25',
        label='In-hive half-life (days)',
        validators=[validation.validate_positive])
    AIAdultLD50 = forms.FloatField(
        initial='2.0',
        label='Adult LD50 (mg/bee)',
        validators=[validation.validate_positive])
    AIAdultSlope = forms.FloatField(
        initial='1',
        label='Slope of adult diet dose-response curve',
        validators=[validation.validate_positive])
    AILarvaLD50 = forms.FloatField(
        initial='2.0',
        label='Larva LD50 (mg/bee)',
        validators=[validation.validate_positive])
    AILarvaSlope = forms.FloatField(
        initial='1',
        label='Slope of larva diet dose-response curve',
        validators=[validation.validate_positive])
    AIAdultLD50Contact = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'foliar'}),
        initial='2.0',
        label='Adult LC50 (mg/bee)',  # TODO check units
        validators=[validation.validate_positive])
    AIAdultSlopeContact = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'foliar'}),
        initial='1',
        label='Slope of adult contact response curve',
        validators=[validation.validate_positive])


class VarroapopInp_resources(forms.Form):
    InitColPollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='100',
        label='Initial colony pollen (g)',
        validators=[validation.validate_positive])
    InitColNectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='100',
        label='Initial colony nectar (g)',
        validators=[validation.validate_positive])
    MaxColPollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='10000',
        label='Maximum colony pollen (g)',
        validators=[validation.validate_positive])
    MaxColNectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='10000',
        label='Maximum colony nectar (g)',
        validators=[validation.validate_positive])
    NeedResourcesToLive = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'resources'}),
        label='Require pollen/nectar for survival?',
        choices=NeedResourcesToLive_CHOICES,
        initial='true',
        validators=[validation.validate_choicefield])
    IPollenTrips = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='5',
        label='Number of pollen trips per forager per day',
        validators=[validation.validate_positive])
    INectarTrips = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='10',
        label='Number of nectar trips per forager per day',
        validators=[validation.validate_positive])
    IPollenLoad = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='15',
        label='Mass of a forager pollen load (mg/bee)',
        validators=[validation.validate_positive])
    INectarLoad = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'resources'}),
        initial='30',
        label='Mass of a forager nectar load (mg/bee)',
        validators=[validation.validate_positive])
    SupPollenEnable = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'resources'}),
        label='Supplemental pollen feeding?',
        choices=SupPollenEnable_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    SupPollenAmount = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'sup_pol'}),
        initial='30',
        label='Amount of supplemental pollen (g)',
        validators=[validation.validate_positive])
    SupPollenBegin = forms.DateField(
        label='Supplemental pollen start date',
        initial=date(2015, 4, 25),  # '06/25/2015',
        widget=forms.SelectDateWidget(attrs={'class': 'sup_pol'}, years=tuple(range(1991, 2016))),
        # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    SupPollenEnd = forms.DateField(
        label='Supplemental pollen end date',
        initial=date(2015, 5, 25),  # '06/25/2015',
        widget=forms.SelectDateWidget(attrs={'class': 'sup_pol'}, years=tuple(range(1991, 2016))),
        # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    SupNectarEnable = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'resources'}),
        label='Supplemental nectar feeding?',
        choices=SupNectarEnable_CHOICES,
        initial='false',
        validators=[validation.validate_choicefield])
    SupNectarAmount = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'sup_nec'}),
        initial='30',
        label='Amount of supplemental nectar (g)',
        validators=[validation.validate_positive])
    SupNectarBegin = forms.DateField(
        label='Supplemental nectar start date',
        initial=date(2015, 4, 25),  # '06/25/2015',
        widget=forms.SelectDateWidget(attrs={'class': 'sup_nec'}, years=tuple(range(1991, 2016))),
        # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    SupNectarEnd = forms.DateField(
        label='Supplemental nectar end date',
        initial=date(2015, 5, 25),  # '06/25/2015',
        widget=forms.SelectDateWidget(attrs={'class': 'sup_nec'}, years=tuple(range(1991, 2016))),
        # TODO set up a clean function check
        validators=[validation.validate_date_range(min=date(1991, 1, 1), max=date(2015, 12, 31))])
    CL4Pollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='1.8',
        label='Pollen consumption - larvae day 4 (mg/day)',
        validators=[validation.validate_positive])
    CL4Nectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='58',
        label='Nectar consumption - larvae day 4 (mg/day)',
        validators=[validation.validate_positive])
    CL5Pollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='3.6',
        label='Pollen consumption - larvae day 5 (mg/day)',
        validators=[validation.validate_positive])
    CL5Nectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='116',
        label='Nectar consumption - larvae day 5 (mg/day)',
        validators=[validation.validate_positive])
    CLDPollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='2.5',
        label='Pollen consumption - drone larvae (mg/day)',
        validators=[validation.validate_positive])
    CLDNectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='100',
        label='Nectar consumption - drone larvae (mg/day)',
        validators=[validation.validate_positive])
    CA13Pollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='5.0',
        label='Pollen consumption - adults days 1-3 (mg/day)',
        validators=[validation.validate_positive])
    CA13Nectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='60',
        label='Nectar consumption - adults days 1-3 (mg/day)',
        validators=[validation.validate_positive])
    CA410Pollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='5.0',
        label='Pollen consumption - adults days 4-10 (mg/day)',
        validators=[validation.validate_positive])
    CA410Nectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='140',
        label='Nectar consumption - adults days 4-10 (mg/day)',
        validators=[validation.validate_positive])
    CA1120Pollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='1.7',
        label='Pollen consumption - adults days 11-20 (mg/day)',
        validators=[validation.validate_positive])
    CA1120Nectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='60',
        label='Nectar consumption - adults days 11-20 (mg/day)',
        validators=[validation.validate_positive])
    CADPollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='0',
        label='Pollen consumption - drone adults (mg/day)',
        validators=[validation.validate_positive])
    CADNectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='100',
        label='Nectar consumption - drone adults (mg/day)',
        validators=[validation.validate_positive])
    CForagerPollen = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='0',
        label='Pollen consumption - foragers (mg/day)',
        validators=[validation.validate_positive])
    CForagerNectar = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'consumption'}),
        initial='292',
        label='Nectar consumption - foragers (mg/day)',
        validators=[validation.validate_positive])


# Combined Form Classes for Validation
class VarroapopInp(VarroapopInp_colony, VarroapopInp_mites, VarroapopInp_chemical, VarroapopInp_resources):
    pass

