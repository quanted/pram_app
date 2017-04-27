"""
.. module:: agdrift_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from ubertool_app.models.forms import validation

Ecosystem_type_CHOICES=(('Aquatic Assessment','Aquatic Assessment'),
                        ('Terrestrial Assessment', 'Terrestrial Assessment'))
Application_method_CHOICES=(('Tier I Aerial','Tier I Aerial'),
                            ('Tier I Ground','Tier I Ground'),
                            ('Tier I Orchard/Airblast','Tier I Orchard/Airblast'))
Drop_size_distribution_aerial_CHOICES=(('Very Fine to Fine','Very Fine to Fine'),
                                ('Fine to Medium','Fine to Medium'),
                                ('Medium to Coarse','Medium to Coarse'),
                                ('Coarse to Very Coarse','Coarse to Very Coarse'))
Drop_size_distribution_ground_CHOICES=(('Very Fine to Fine','Very Fine to Fine'),
                                ('Fine to Medium/Coarse','Fine to Medium/Coarse'))
Boom_height_CHOICES=(('Low','Low'),
                     ('High','High'))

Orchard_CHOICES=(('Normal','Normal (Stone and Pome Fruit Vineyard)'),
                 ('Dense','Dense (Citrus, tall trees)'),
                 ('Sparse', 'Sparse (Young, dormant)'),
                 ('Vineyard', 'Vineyard'),
                 ('Orchard','Orchard'))
Terrestrial_type_CHOICES=(('Point Deposition','Point Deposition'),
                          ('User Defined Terrestrial Area','User Defined Terrestrial Area'))
Aquatic_type_CHOICES=(('EPA Defined Pond','EPA Defined Pond'),
                      ('EPA Defined Wetland', 'EPA Defined Wetland'),
                      ('User Defined Waterbody', 'User Defined Waterbody'))
Calculation_input_CHOICES=(('Distance','Distance to waterbody or field'),
                           ('Fraction','Fraction of applied'),
                           ('Initial Average Deposition (g/ha)','Initial Average Deposition (g/ha)'),
                           ('Initial Average Deposition (lb/ac)', 'Initial Average Deposition (lb/ac)'),
                           ('Initial Average Concentration (ng/L)', 'Initial Average Concentration (ng/L)'),
                           ('Initial Average Deposiion (mg/cm2)','Initial Average Deposition (mg/cm2)'))
Version_CHOICES = ( ('1.0','1.0'),
                   ('2.1.1', '2.1.1'),
                   ('3.0', '3.0'))
#Aquatic Assessment
#Waterbody_type_CHOICES=(('','Make a selection'),('EPA Pond','EPA Pond'),('Lake', 'Lake'), ('Watercourse', 'Watercourse')) #Aquatic Assessment
#Orchard_CHOICES=(('','Make a selection'),('Vineyard in leaf','Vineyard in leaf'),('Orchard or dormant vineyard','Orchard or dormant vineyard'))
#Waterbody_type_CHOICES=(('','Make a selection'),('EPA Pond','EPA Pond'),('Lake', 'Lake'), ('Watercourse', 'Watercourse')) #Aquatic Assessment

class AgdriftInp(forms.Form):

    version = forms.ChoiceField(
        label='Version',
        choices=Version_CHOICES,
        initial='2.1.1')
    chemical_name = forms.CharField(
        widget=forms.Textarea (attrs={'cols': 30, 'rows': 1}),
        label='Chemical Name',
        initial='Alachlor')
    pc_code = forms.CharField(
        widget=forms.Textarea (attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        initial='00')
    application_method = forms.ChoiceField(
        label='Application Method',
        choices=Application_method_CHOICES,
        initial='Tier I Aerial',
        validators=[validation.validate_choicefield])
    drop_size_aerial = forms.ChoiceField(
        label='Drop Size Distribution-Aerial',
        choices=Drop_size_distribution_aerial_CHOICES,
        initial='Fine to Medium',
        validators=[validation.validate_choicefield])
    drop_size_ground = forms.ChoiceField(
        label='Drop Size Distribution-Ground',
        choices=Drop_size_distribution_ground_CHOICES,
        initial='Very Fine to Fine',
        validators=[validation.validate_choicefield])
    boom_height = forms.ChoiceField(
        label='Boom height',
        choices=Boom_height_CHOICES,
        initial='High',
        validators=[validation.validate_choicefield])
    airblast_type = forms.ChoiceField(
        label='Orchard/Airblast Type',
        choices=Orchard_CHOICES,
        initial='Orchard',
        validators=[validation.validate_choicefield])
    ecosystem_type = forms.ChoiceField(
        label='Ecosystem type',
        choices=Ecosystem_type_CHOICES,
        initial='Aquatic Assessment',
        validators=[validation.validate_choicefield])
    aquatic_body_type = forms.ChoiceField(
        label='Aquatic Assessment Type',
        choices=Aquatic_type_CHOICES,
        initial='EPA Defined Pond',
        validators=[validation.validate_choicefield])
    terrestrial_field_type = forms.ChoiceField(
        label='Terrestrial Assessment Type',
        choices=Terrestrial_type_CHOICES,
        initial='Point Deposition',
        validators=[validation.validate_choicefield])
    epa_pond_width = forms.FloatField(
        label=mark_safe('EPA Defined Pond Width (ft)'),
        initial='208.7',
        disabled=True,
        validators=[validation.validate_greaterthan0])
    epa_pond_depth = forms.FloatField(
        label=mark_safe('EPA Defined Pond depth (ft)'),
        initial='6.56',
        disabled=True,
        validators=[validation.validate_greaterthan0])
    epa_wetland_width = forms.FloatField(
        label=mark_safe('EPA Defined Wetland Width (ft)'),
        initial='208.7',
        disabled=True,
        validators=[validation.validate_greaterthan0])
    epa_wetland_depth = forms.FloatField(
        label=mark_safe('EPA Defined Wetland depth (ft)'),
        initial='0.4921',
        disabled=True,
        validators=[validation.validate_greaterthan0])
    user_waterbody_width = forms.FloatField(
        label=mark_safe('User Defined Waterbody Width (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    user_waterbody_depth = forms.FloatField(
        label=mark_safe('User Defined Wtaerbody depth (ft)'),
        initial='6.56',
        validators=[validation.validate_greaterthan0])
    user_terrestrial_width = forms.FloatField(
        label=mark_safe('Downwind width of Terrestrial Area (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    application_rate = forms.FloatField(
        label=mark_safe('Active rate (lb/ac)'),
        initial='0.5',
        validators=[validation.validate_greaterthan0])
    calculation_input = forms.ChoiceField(
        label = 'Initial Input Type for Calculation',
        choices=Calculation_input_CHOICES,
        initial ='Distance',
        validators=[validation.validate_choicefield])
    downwind_distance = forms.FloatField(
        label=mark_safe('Distance to water body or terrestrial point from edge of field (ft)'),
        initial='225',
        validators=[validation.validate_integer, validation.validate_greaterthan0])
    user_frac_applied = forms.FloatField(
        label=mark_safe('Fraction applied'),
        initial='0.0314',
        validators=[validation.validate_range01])
    user_avg_dep_gha = forms.FloatField(
        label=mark_safe('Initial Average Deposition (g/ha)'),
        initial='8.82',
        validators=[validation.validate_greaterthan0])
    user_avg_dep_mgcm2 = forms.FloatField(
        label=mark_safe('Initial Average Deposition (mg/cm2)'),
        initial='6.56',
        validators=[validation.validate_greaterthan0])
    user_avg_dep_lbac = forms.FloatField(
        label=mark_safe('Initial Average Deposition (lb/ac)'),
        initial='6.56',
        validators=[validation.validate_greaterthan0])
    user_avg_conc_ngl = forms.FloatField(
        label=mark_safe('Initial Average Deposition (ng/L)'),
        initial='0.0079',
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
