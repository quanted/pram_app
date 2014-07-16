"""
.. module:: pfam_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


weather_CHOICES=(('0','Make a selection'),('wTest','test1'))

class PFAMInp_chem(forms.Form):
    wat_hl = forms.FloatField(
            label='Water Column Half life (days)',
            initial=30,
            validators=[validation.validate_greaterthan0])
    wat_t = forms.FloatField(
            label=mark_safe('@Temperature (&#8451)'),
            initial=20,
            validators=[validation.validate_range0100])
    ben_hl = forms.FloatField(
            label='Benthic Compartment Half Life (days)',
            initial=65,
            validators=[validation.validate_greaterthan0])
    ben_t = forms.FloatField(
            label=mark_safe('@Temperature (&#8451)'),
            initial=20,
            validators=[validation.validate_range0100])
    unf_hl = forms.FloatField(
            label='Unflooded Soil Half Life (days)',
            initial=61,
            validators=[validation.validate_greaterthan0])
    unf_t = forms.FloatField(
            label=mark_safe('@Temperature (&#8451)'),
            initial=20,
            validators=[validation.validate_range0100])
    aqu_hl = forms.FloatField(
            label='Aqueous Near-Surface Photolysis Half Life (days)',
            initial=2.5,
            validators=[validation.validate_greaterthan0])
    aqu_t = forms.FloatField(
            label=mark_safe('@Degrees Latitude'),
            initial=40,
            validators=[validation.validate_degrees_latitude])
    hyd_hl = forms.FloatField(
            label='Hydrolysis Half Life (days)',
            initial=79,
            validators=[validation.validate_greaterthan0])
    mw = forms.FloatField(
            label='Molecular Weight (g/mol)',
            initial=202,
            validators=[validation.validate_greaterthan0])
    vp = forms.FloatField(
            label='Vapor Pressure (torr)',
            initial=1.3e-6,
            validators=[validation.validate_greaterthan0])
    sol = forms.FloatField(
            label='Solubility (mg/l)',
            initial=100,
            validators=[validation.validate_greaterthan0])
    koc = forms.FloatField(
            label='Koc (ml/g)',
            initial=50,
            validators=[validation.validate_greaterthan0])
    hea_h = forms.FloatField(
            label='Heat of Henry (J/mol)',
            initial=20000,
            validators=[validation.validate_greaterthan0])
    hea_r_t = forms.FloatField(
            label=mark_safe('Henry Reference Temperature (&#8451)'),
            initial=20,
            validators=[validation.validate_range0100])
    
class PFAMInp_loc(forms.Form):
    weather= forms.ChoiceField(
            label='Weather File',
            choices=weather_CHOICES,
            initial='Make a selection',
            validators=[validation.validate_choicefield])
    wea_l = forms.FloatField(
            label='@Latitude (for Photolysis Calculations)',
            initial=28,
            validators=[validation.validate_degrees_latitude])
    
class PFAMInp_cro(forms.Form):
    zero_height_ref= forms.DateField(
            label='Zero Height Reference (MM/DD)',
            input_formats=['%m/%d'],
            initial='04/01')
    days_zero_full = forms.IntegerField(
            label='Days from Zero Height to Full Height',
            initial=60,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    days_zero_removal = forms.IntegerField(
            label='Days from Zero Height to Removal',
            initial=150,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    max_frac_cov = forms.FloatField(
            label='Maximum Fractional Area Coverage',
            initial=0.99,
            validators=[validation.validate_range01])
    
class PFAMInp_phy(forms.Form):
    mas_tras_cof = forms.FloatField(
            label='Mass Transfer Coefficient (m/s)',
            initial=1e-8,
            validators=[validation.validate_greaterthan0])
    leak = forms.FloatField(
            label='Leakage (m/d)',
            initial=0,
            validators=[validation.validate_positive])
    ref_d = forms.FloatField(
            label='Reference Depth (m)',
            initial=0.1,
            validators=[validation.validate_greaterthan0])
    ben_d = forms.FloatField(
            label='Benthic Depth (m)',
            initial=0.05,
            validators=[validation.validate_greaterthan0])
    ben_por = forms.FloatField(
            label='Benthic Porosity',
            initial=0.5,
            validators=[validation.validate_greaterthan0])
    dry_bkd = forms.FloatField(
            label=mark_safe('Dry Bulk Density (g/cm<sup>3</sup>)'),
            initial=1.35,
            validators=[validation.validate_greaterthan0])
    foc_wat = forms.FloatField(
            label='Foc Water Column on SS',
            initial=0.04,
            validators=[validation.validate_greaterthan0])
    foc_ben = forms.FloatField(
            label='Foc Benthic',
            initial=0.01,
            validators=[validation.validate_greaterthan0])
    ss = forms.FloatField(
            label='SS (mg/L)',
            initial=30,
            validators=[validation.validate_greaterthan0])
    wat_c_doc = forms.FloatField(
            label='Water column DOC (mg/L)',
            initial=5.0,
            validators=[validation.validate_greaterthan0])
    chl = forms.FloatField(
            label='Chlorophyll, CHL (mg/L)',
            initial=0.005,
            validators=[validation.validate_greaterthan0])
    dfac = forms.FloatField(
            label='Dfac',
            initial=1.19,
            validators=[validation.validate_greaterthan0])
    q10 = forms.FloatField(
            label='Q10',
            initial=2,
            validators=[validation.validate_range0100])

class PFAMInp_out(forms.Form):
    area_app = forms.FloatField(
            label=mark_safe('Area of Application (m<sup>2</sup>)'),
            initial=20000,
            validators=[validation.validate_greaterthan0])


# Combined Form Classes for Validation
class PfamInp(PFAMInp_chem, PFAMInp_loc, PFAMInp_cro, PFAMInp_phy, PFAMInp_out):
    pass
