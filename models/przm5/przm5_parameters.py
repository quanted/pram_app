"""
.. module:: przm5_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


#Chemical tab
class przm5Inp_chem(forms.Form):
    # deg_choice = ((0,'None'), (1,'Degradate 1'), (2,'Degradate 2'))
    # deg_check = forms.ChoiceField(
            # label='Degradate', choices=deg_choice, initial='None')
    koc_check_choice = ((1,'Koc'), (0,'Kd'))
    koc_check = forms.ChoiceField(
            label='Sorption Coefficient Type',
            choices=koc_check_choice,
            initial='Koc')
    Koc_0 = forms.FloatField(
            label='Sorption Coefficient (mL/g)',
            initial=200,
            validators=[validation.validate_positive])
    soilHalfLife_0 = forms.FloatField(
            label='Soil Halflife (day)',
            initial=100,
            validators=[validation.validate_positive])
    # Below was changed by Jon F. (soilHalfLife_ref  -> soilHalfLifeRef)
    soilHalfLifeRef_0 = forms.FloatField(
            label=mark_safe('Soil Reference Temp (&deg;C)'),
            initial=25,
            validators=[validation.validate_positive])
    foliarHalfLife_0 = forms.FloatField(
            label='Foliar Halflife (day)',
            initial=44,
            validators=[validation.validate_positive])

class przm5Inp_chem0(forms.Form):
    deg_choice = (('0','None'), ('1','1 Degradate'), ('2','2 Degradates'))
    deg_check = forms.ChoiceField(
            label='Number of Degradates?',
            choices=deg_choice,
            initial=0)

class przm5Inp_chem1(forms.Form):
    #Degradate 1
    Koc_1 = forms.FloatField(
            required=False,
            label='Sorption Coefficient (mL/g)',
            initial=200)
    # unit_1 = ((1,'Koc'),(0,'Kd'))
    # sorp_K_unit_1 = forms.ChoiceField(
            # required=False,label='Sorption Coefficient Type',choices=unit_1)
    soilHalfLife_1 = forms.FloatField(
            required=False,
            label='Soil Halflife (day)',
            initial=100)
    soilHalfLifeRef_1 = forms.FloatField(
            required=False,
            label=mark_safe('Soil Reference Temp (&deg;C)'),
            initial=25)
    foliarHalfLife_1 = forms.FloatField(
            required=False,
            label='Foliar Halflife (day)',
            initial=44)

class przm5Inp_mcf1(forms.Form):
    # Molar Conversion Factors 1
    convertSoil1 = forms.FloatField(
            required=False,
            label='Soil',
            initial=0.70)
    convert_Foliar1 = forms.FloatField(
            required=False,
            label='Foliar',
            initial=0.82)

class przm5Inp_chem2(forms.Form):
    #Degradate 2
    Koc_2 = forms.FloatField(
            required=False,
            label='Sorption Coefficient (mL/g)',
            initial=200)
    # unit_2 = ((1,'Koc'),(0,'Kd'))
    # sorp_K_unit_2 = forms.ChoiceField(
            # required=False,label='Sorption Coefficient Type',choices=unit_2)
    soilHalfLife_2 = forms.FloatField(
            required=False,
            label='Soil Halflife (day)',
            initial=100)
    soilHalfLifeRef_2 = forms.FloatField(
            required=False,
            label=mark_safe('Soil Reference Temp (&deg;C)'),
            initial=25)
    foliarHalfLife_2 = forms.FloatField(
            required=False,
            label='Foliar Halflife (day)',
            initial=44)

class przm5Inp_mcf2(forms.Form):
    # Molar Conversion Factors 2

    # Removed because this isn't in the SWC anymore
    deg2_srcSel = ((1,'Degradate 1'),(0,'Parent'))
    deg2_source = forms.ChoiceField(
            required=False,
            choices=deg2_srcSel,
            label='Source of Degradate 2',
            initial=1)
    convertSoil2 = forms.FloatField(
            required=False,
            label='Soil',
            initial=0.80)
    convert_Foliar2 = forms.FloatField(
            required=False,
            label='Foliar')

#Application tab
class przm5Inp_appl(forms.Form):
    # water_body_type_check = forms.CharField(initial='Pond')
    # Eff = forms.FloatField(
         # label='Eff.', initial=0.95)
    # spray = forms.FloatField(
         # label='Drift/T', initial=0.05)

    app_date_type_choice = (('0','Absolute Dates'),('1','Relative Dates'))
    app_date_type = forms.ChoiceField(
            label='Choose Way of Entering Application Dates',
            choices=app_date_type_choice)
    app_nOpt =(('0','Select Value'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),
             ('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),
             ('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),
             ('31','31'),('32','23'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),
             ('41','41'),('42','24'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48'),('49','49'),('50','50'))
    noa = forms.ChoiceField(
            choices=app_nOpt,
            label='Number of Applications',
            initial='',
            validators=[validation.validate_choicefield])
    specifyYearsSel = (('1','Yes'), ('0','No'))
    specifyYears = forms.ChoiceField(
            required=False,
            label='Specify Years?',
            choices=specifyYearsSel,
            initial='0')
    pond_res_customSel = ((1,'Pond'), (2,'Reservoir'), (3,'Custom'))
    pond_res_custom = forms.ChoiceField(
            required=False,
            label='Enter Eff. & Drift/T for',
            choices=pond_res_customSel,
            initial=1)

#Crop/land tab
class przm5Inp_cropland(forms.Form):
    dvf_choice = (('0','Make a Selection'), ('test.dvf','test.dvf'))
    dvf_file = forms.ChoiceField(
            label='Weather File',
            choices=dvf_choice,
            initial='test.dvf',
            validators=[validation.validate_choicefield])
    Emerge_text=forms.CharField(
            label='Emerge (DD/MM)',
            initial='16/02')
    Mature_text=forms.CharField(
            label='Mature (DD/MM)',
            initial='05/05')
    Harvest_text=forms.CharField(
            label='Harvest (DD/MM)',
            initial='12/05')
    pfac = forms.FloatField(
            label='Pan Factor',
            initial=0.79,
            validators=[validation.validate_positive])
    snowmelt = forms.FloatField(
            label='Snowmelt Factor',
            initial=0.00,
            validators=[validation.validate_positive])
    evapDepth = forms.FloatField(
            label='Evaportation Depth',
            initial=17.5,
            validators=[validation.validate_positive])
    rootDepth = forms.FloatField(
            label='Root Depth (cm)',
            initial=12,
            validators=[validation.validate_positive])
    canopyCover = forms.FloatField(
            label='Canopy Cover (%)',
            initial=90,
            validators=[validation.validate_range0100])
    canopyHeight = forms.FloatField(
            label='Canopy Height (cm)',
            initial=30,
            validators=[validation.validate_positive])
    canopyHoldup = forms.FloatField(
            label='Canopy Holdup (cm)',
            initial=0.25,
            validators=[validation.validate_positive])
    irr_choice = ((0,'None'), (1,'Over Canopy'), (2,'Under Canopy'))
    irflag = forms.ChoiceField(
            label='Irrigation',
            choices=irr_choice,
            initial='None')
    # temp_choice = ((0,'No'), (1,'Yes'))
    # tempflag = forms.ChoiceField(
            # label='Simulate Temperature', choices=temp_choice, initial='No')
    fleach = forms.FloatField(
            label='Extra Water Fraction',
            initial=0.96,
            validators=[validation.validate_range01])
    depletion = forms.FloatField(
            label='Allowed Depletion',
            initial=0.97,
            validators=[validation.validate_positive])
    rateIrrig = forms.FloatField(
            label='Max Rate',
            initial=0.98,
            validators=[validation.validate_positive])
    # albedo = forms.FloatField(
            # label='Albedo', initial=0.40)
    # bcTemp = forms.FloatField(
            # label='Lower BC Temperature', initial=23)
    post_choice = ((1,'Surface Applied'), (2,'Removed'), (3,'Left as Foliage'))
    PestDispHarvest = forms.ChoiceField(
            label='Post-Harvest Foliage',
            choices=post_choice,
            initial='Surface Applied')


#Runoff tab
class przm5Inp_runoff(forms.Form):
    uslek = forms.FloatField(
            label='USLE K',
            initial=0.37,
            validators=[validation.validate_positive])
    uslels = forms.FloatField(
            label='USLE LS',
            initial=1.34,
            validators=[validation.validate_positive])
    uslep = forms.FloatField(
            label='USLE P',
            initial=0.5,
            validators=[validation.validate_positive])
    ireg = forms.FloatField(
            label='IREG',
            initial=1,
            validators=[validation.validate_positive])
    slope = forms.FloatField(
            label='Slope (%)',
            initial=6,
            validators=[validation.validate_range0100])
    NumberOfFactors_choice = ((26,26), (27,27))
    # NumberOfFactors = forms.ChoiceField(
            # label='No. of Time-Varing Factors', choices=NumberOfFactors_choice, initial=26)
    rDepthBox = forms.FloatField(
            label='R-Depth (cm)',
            initial=2.0,
            validators=[validation.validate_positive])
    rDeclineBox = forms.FloatField(
            label='R-Decline (1/cm)',
            initial=1.55,
            validators=[validation.validate_positive])
    rBypassBox = forms.FloatField(
            label='Efficiency',
            initial=0.266,
            validators=[validation.validate_positive])
    eDepthBox = forms.FloatField(
            label='E-Depth (cm)',
            initial=0.1,
            validators=[validation.validate_positive])
    eDeclineBox = forms.FloatField(
            label='E-Decline (1/cm)',
            initial=0,
            validators=[validation.validate_positive])


#Water Body tab
class przm5Inp_waterbody(forms.Form):
    fieldSize = forms.FloatField(
            label='Area of Field (ha.)',
            initial=10,
            validators=[validation.validate_positive])
    hydlength = forms.FloatField(
            label='Hydraulic Length (m)',
            initial=356.8,
            validators=[validation.validate_positive])


# Combined Form Classes for Validation
class Przm5Inp( przm5Inp_chem, przm5Inp_chem0, przm5Inp_chem1, przm5Inp_mcf1,
                przm5Inp_chem2, przm5Inp_mcf2, przm5Inp_appl, przm5Inp_cropland,
                przm5Inp_runoff, przm5Inp_waterbody):
    pass