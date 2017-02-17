"""
.. module:: agdrift_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from ubertool_app.models.forms import validation

Ecosystem_type_CHOICES=(('0','Make a selection'),
                        ('Aquatic Assessment','Aquatic Assessment'),
                        ('Terrestrial Assessment', 'Terrestrial Assessment'))
Application_method_CHOICES=(('0','Make a selection'),
                            ('Tier I Aerial','Tier I Aerial'),
                            ('Tier I Ground','Tier I Ground'),
                            ('Tier I Orchard/Airblast','Tier I Orchard/Airblast'))
Drop_size_distribution_CHOICES=(('0','Make a selection'),
                                ('Very fine to fine','Very fine to fine'),
                                ('Fine to Medium','Fine to Medium'),
                                ('Medium to Coarse','Medium to Coarse'),
                                ('Coarse to Very Coarse','Coarse to Very Coarse'))
Boom_height_CHOICES=(('0','Make a selection'),
                     ('Low','Low'),
                     ('High','High'))

Orchard_CHOICES=(('0','Make a selection'),
                 ('Normal','Normal (Stone and Pome Fruit Vineyard)'),
                 ('Dense','Dense (Citrus, tall trees)'),
                 ('Sparse', 'Sparse (Young, dormant)'),
                 ('Vineyard', 'Vineyard'),
                 ('Orchard','Orchard'))
Terrestrial_type_CHOICES=(('0','Make a selection'),
                          ('EPA Defined Terrestrial','EPA Defined Terrestrial'),
                          ('User Defined Terrestrial','User Defined Terrestrial'))
Aquatic_type_CHOICES=(('0','Make a selection'),
                      ('EPA Defined Pond','EPA Defined Pond'),
                      ('EPA Defined Wetland', 'EPA Defined Wetland'))
Calculation_input_CHOICES=(('0','Make a selection'),
                           ('Distance','Distance to waterbody or field'),
                           ('Fraction','Fraction of applied'),
                           ('Initial Average Deposition (g/ha)','Initial Average Deposition (g/ha)'),
                           ('Initial Average Deposition (lb/ac)', 'Initial Average Deposition (lb/ac)'),
                           ('Initial Average Concentration (ng/L)', 'Initial Average Concentration (ng/L)'),
                           ('Initial Average Deposiion (mg/cm2)','Initial Average Deposition (mg/cm2)'))
SELECT_VERSION = (('1.0','1.0'),)
#Aquatic Assessment
#Waterbody_type_CHOICES=(('','Make a selection'),('EPA Pond','EPA Pond'),('Lake', 'Lake'), ('Watercourse', 'Watercourse')) #Aquatic Assessment
#Orchard_CHOICES=(('','Make a selection'),('Vineyard in leaf','Vineyard in leaf'),('Orchard or dormant vineyard','Orchard or dormant vineyard'))
#Waterbody_type_CHOICES=(('','Make a selection'),('EPA Pond','EPA Pond'),('Lake', 'Lake'), ('Watercourse', 'Watercourse')) #Aquatic Assessment

class AgdriftInp(forms.Form):

    version = forms.ChoiceField(
        choices=SELECT_VERSION,
        label='Version',
        initial='1.2.2')
    chemical_name = forms.CharField(
        widget=forms.Textarea (attrs={'cols': 30, 'rows': 1}),
        label='Chemical Name',
        initial='Alachlor')
    pc_code = forms.CharField(
        widget=forms.Textarea (attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='00')
    ecosystem_type = forms.ChoiceField(
        label='Ecosystem type',
        choices=Ecosystem_type_CHOICES,
        initial='Aquatic Assessment',
        validators=[validation.validate_choicefield])
    application_method = forms.ChoiceField(
        label='Application Method',
        choices=Application_method_CHOICES,
        initial='Tier I Aerial',
        validators=[validation.validate_choicefield])
    aquatic_body_type = forms.ChoiceField(
        label='Aquatic Assessment Type',
        choices=Aquatic_type_CHOICES,
        initial='EPA Defined Pond',
        validators=[validation.validate_choicefield])
    drop_size = forms.ChoiceField(
        label='Drop Size Distribution',
        choices=Drop_size_distribution_CHOICES,
        initial='Medium to Coarse',
        validators=[validation.validate_choicefield])
    application_rate = forms.FloatField(
        label=mark_safe('Active rate (lb/ac)'),
        initial='0.5',
        validators=[validation.validate_greaterthan0])
    boom_height = forms.ChoiceField(
        label='Boom height',
        choices=Boom_height_CHOICES,
        initial='High',
        validators=[validation.validate_choicefield])
    airblast_type = forms.ChoiceField(
        label='Orchard type',
        choices=Orchard_CHOICES,
        initial='Orchard',
        validators=[validation.validate_choicefield])
    calculation_input = forms.ChoiceField(
        label = 'Toolbox Input Type',
        choices=Calculation_input_CHOICES,
        initial ='Distance',
        validators=[validation.validate_choicefield])
    downwind_distance = forms.FloatField(
        label=mark_safe('Distance to water body or terrestrial point from edge of field (ft)'),
        initial='225',
        validators=[validation.validate_integer, validation.validate_greaterthan0])
    user_pond_width = forms.FloatField(
        label=mark_safe('Pond Width (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    user_pond_depth = forms.FloatField(
        label=mark_safe('Pond depth (ft)'),
        initial='6.56',
        validators=[validation.validate_greaterthan0])
    user_wetland_width = forms.FloatField(
        label=mark_safe('Wetland Width (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    user_wetland_depth = forms.FloatField(
        label=mark_safe('Wetland depth (ft)'),
        initial='0.4921',
        validators=[validation.validate_greaterthan0])
    terrestrial_field_type = forms.ChoiceField(
        label='Terrestrial Field type',
        choices=Terrestrial_type_CHOICES,
        initial='EPA Defined Terrestrial',
        validators=[validation.validate_choicefield])
    user_terrestrial_width = forms.FloatField(
        label=mark_safe('Downwind width of Area (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
#    extending_settings = forms.ChoiceField(
            # label='Optional settings', choices=Extended_settings_CHOICES, initial='Make a selection')
 #   init_avg_dep_foa = forms.FloatField(
            # label=mark_safe('Fraction of applied'))
 #   avg_depo_gha = forms.FloatField(
            # label=mark_safe('Initial Average Deposition (g/ha)'))
 #   avg_depo_lbac = forms.FloatField(
            # label=mark_safe('Initial Average Deposition (lb/ac)'))
 #   deposition_ngL = forms.FloatField(
            # label=mark_safe('Initial Average Concentration (ng/L)'))
 #   deposition_mgcm = forms.FloatField(
            # label=mark_safe('Initial Average Deposiion (mg/cm2)'))
