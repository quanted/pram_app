"""
.. module:: agdrift_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from pram_app.models.forms import validation

Ecosystem_type_CHOICES=(('aquatic_assessment','Aquatic Assessment'),
                        ('terrestrial_assessment', 'Terrestrial Assessment'))
Application_method_CHOICES=(('tier_1_aerial','Tier I Aerial'),
                            ('tier_1_ground','Tier I Ground'),
                            ('tier_1_airblast','Tier I Airblast'))
Drop_size_distribution_aerial_CHOICES=(('very_fine_to_fine','Very Fine to Fine'),
                                ('fine_to_medium','Fine to Medium'),
                                ('medium_to_coarse','Medium to Coarse'),
                                ('coarse_to_very_coarse','Coarse to Very Coarse'))
Drop_size_distribution_ground_CHOICES=(('very_fine','Very Fine'),
                                ('fine_to_medium-coarse','Fine to Medium/Coarse'))
Boom_height_CHOICES=(('low','Low'),
                     ('high','High'))

Orchard_CHOICES=(('normal','Normal (Stone and Pome Fruit Vineyard)'),
                 ('dense','Dense (Citrus, tall trees)'),
                 ('sparse', 'Sparse (Young, dormant)'),
                 ('vineyard', 'Vineyard'),
                 ('orchard','Orchard'))
Terrestrial_type_CHOICES=(('epa_defined_terrestrial','EPA Defined Terrestrial (Point Deposition)'),
                          ('user_defined_terrestrial','User Defined Terrestrial'))
Aquatic_type_CHOICES=(('epa_defined_pond','EPA Defined Pond'),
                      ('epa_defined_wetland', 'EPA Defined Wetland'),
                      ('user_defined_pond', 'User Defined Pond'),
                      ('user_defined_wetland', 'User Defined Wetland'))
Calculation_input_CHOICES=(('distance_to_point_or_area_ft','Distance to point, waterbody, or field (ft)'),
                           ('fraction_of_applied','Fraction of applied'),
                           ('initial_deposition_gha','Initial Pt/Avg Deposition (g/ha)'),
                           ('initial_deposition_lbac', 'Initial Pt/Avg Deposition (lb/ac)'),
                           ('initial_deposition_mgcm2','Initial Pt/Avg Deposition (mg/cm2)'),
                           ('initial_concentration_ngL', 'Initial Average Concentration (ng/L)'))
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
        #show_hidden_initial= False,
        initial='2.1.1')
    chemical_name = forms.CharField(
        widget=forms.Textarea (attrs={'cols': 30, 'rows': 1}),
        label='Chemical Name',
        #show_hidden_initial=False,
        initial='Alachlor')
    pc_code = forms.CharField(
        widget=forms.Textarea (attrs={'cols': 20, 'rows': 1}),
        label='PC Code',
        #show_hidden_initial=False,
        initial='00')
    application_method = forms.ChoiceField(
        label='Application Method',
        choices=Application_method_CHOICES,
        #show_hidden_initial=False,
        initial='Tier I Aerial',
        validators=[validation.validate_choicefield])
    drop_size_aerial = forms.ChoiceField(
        label='Drop Size Distribution-Aerial',
        choices=Drop_size_distribution_aerial_CHOICES,
        #show_hidden_initial=False,
        initial='Fine to Medium',
        validators=[validation.validate_choicefield])
    drop_size_ground = forms.ChoiceField(
        label='Drop Size Distribution-Ground',
        choices=Drop_size_distribution_ground_CHOICES,
        initial='Very Fine',
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
        label='Assessment type',
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
        initial='EPA Defined Terrestrial (Point Deposition)',
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
    user_pond_width = forms.FloatField(
        label=mark_safe('User Defined Pond Width (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    user_pond_depth = forms.FloatField(
        label=mark_safe('User Defined Pond Depth (ft)'),
        initial='6.56',
        validators=[validation.validate_greaterthan0])
    user_wetland_width = forms.FloatField(
        label=mark_safe('User Defined Wetland Width (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    user_wetland_depth = forms.FloatField(
        label=mark_safe('User Defined Wetland Depth (ft)'),
        initial='0.4921',
        validators=[validation.validate_greaterthan0])
    user_terrestrial_width = forms.FloatField(
        label=mark_safe('Downwind width of Terrestrial Area (ft)'),
        initial='208.7',
        validators=[validation.validate_greaterthan0])
    application_rate = forms.FloatField(
        label=mark_safe('Application rate (lb/ac)'),
        initial='0.5',
        validators=[validation.validate_greaterthan0])
    calculation_input = forms.ChoiceField(
        label = 'Initial Input Type for Calculation',
        choices=Calculation_input_CHOICES,
        initial ='Distance to point, waterbody, or field (ft)',
        validators=[validation.validate_choicefield])
    downwind_distance = forms.FloatField(
        label=mark_safe('Distance to waterbody or field (ft)'),
        initial='225',
        validators=[validation.validate_integer, validation.validate_positive])
    user_frac_applied = forms.FloatField(
        label=mark_safe('Fraction of applied'),
        initial='0.0314',
        validators=[validation.validate_range01])
    user_avg_dep_gha = forms.FloatField(
        label=mark_safe('Initial Pt/Avg Deposition (g/ha)'),
        initial='8.82',
        validators=[validation.validate_greaterthan0])
    user_avg_dep_mgcm2 = forms.FloatField(
        label=mark_safe('Initial Pt/Avg Deposition (mg/cm2)'),
        initial='0.0005',
        validators=[validation.validate_greaterthan0])
    user_avg_dep_lbac = forms.FloatField(
        label=mark_safe('Initial Pt/Avg Deposition (lb/ac)'),
        initial='0.005',
        validators=[validation.validate_greaterthan0])
    user_avg_conc_ngl = forms.FloatField(
        label=mark_safe('Initial Average Concentration (ng/L)'),
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
