"""
.. module:: exams_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


scenario_select = (('0','Select a scenario'),('CA Almonds MLRA-17', 'CA Almonds MLRA-17'), ('CA Citrus   MLRA-17', 'CA Citrus   MLRA-17'), ('CA Cotton   MLRA-17', 'CA Cotton   MLRA-17'), ('CA Grape  MLRA-17', 'CA Grape  MLRA-17'), ('CA Lettuce  MLRA-14', 'CA Lettuce  MLRA-14'), ('CA Onions MLRA-17', 'CA Onions MLRA-17'), ('CA Tomato MLRA-17', 'CA Tomato MLRA-17'), ('FL Avocado MLRA-156A', 'FL Avocado MLRA-156A'), ('FL Cabbage   MLRA-155', 'FL Cabbage   MLRA-155'), ('FL Carrots MLRA-156B', 'FL Carrots MLRA-156B'), ('FL Citrus   MLRA-156A', 'FL Citrus   MLRA-156A'), ('FL Cucumber   MLRA-156A', 'FL Cucumber   MLRA-156A'), ('FL Peppers MLRA-156A', 'FL Peppers MLRA-156A'), ('FL Strawberry   MLRA-155', 'FL Strawberry   MLRA-155'), ('FL Sugarcane   MLRA-156A', 'FL Sugarcane   MLRA-156A'), ('FL Tomato   MLRA-155', 'FL Tomato   MLRA-155'), ('FL Turf  MLRA-155', 'FL Turf  MLRA-155'), ('GA Onions MLRA-153A/133A', 'GA Onions MLRA-153A/133A'), ('GA Peach   MLRA-133A', 'GA Peach   MLRA-133A'), ('GA Pecan   MLRA-133A', 'GA Pecan   MLRA-133A'), ('ID Potato   MLRA-11B', 'ID Potato   MLRA-11B'), ('IL Corn   MLRA-108', 'IL Corn   MLRA-108'), ('KS Sorghum   MLRA-112', 'KS Sorghum   MLRA-112'), ('LA Sugarcane   MLRA-131', 'LA Sugarcane   MLRA-131'), ('ME Potato   MLRA-146', 'ME Potato   MLRA-146'), ('MI Asparagus MLRA-96', 'MI Asparagus MLRA-96'), ('MI Beans MLRA-99', 'MI Beans MLRA-99'), ('MI Cherry   MLRA-96', 'MI Cherry   MLRA-96'), ('MN Sugarbeet   MLRA-56', 'MN Sugarbeet   MLRA-56'), ('MS Corn   MLRA-134', 'MS Corn   MLRA-134'), ('MS Cotton   MLRA-134', 'MS Cotton   MLRA-134'), ('MS Soybean   MLRA-134', 'MS Soybean   MLRA-134'), ('NC Apple   MLRA-130', 'NC Apple   MLRA-130'), ('NC Corn - E   MLRA-153A', 'NC Corn - E   MLRA-153A'), ('NC Cotton   MLRA-133A', 'NC Cotton   MLRA-133A'), ('NC Peanut   MLRA-153A', 'NC Peanut   MLRA-153A'), ('NC Sweet Potato MLRA-133', 'NC Sweet Potato MLRA-133'), ('NC Tobacco   MLRA-133A', 'NC Tobacco   MLRA-133A'), ('ND Canola   MLRA-55A', 'ND Canola   MLRA-55A'), ('ND Wheat   MLRA-56', 'ND Wheat   MLRA-56'), ('NY Grape   MLRA-100/101', 'NY Grape   MLRA-100/101'), ('OH Corn   MLRA-111', 'OH Corn   MLRA-111'), ('OR Apple   MLRA-2', 'OR Apple   MLRA-2'), ('OR Christmas Trees  MLRA-2', 'OR Christmas Trees  MLRA-2'), ('OR Filberts   MLRA-2', 'OR Filberts   MLRA-2'), ('OR Grass Seed   MLRA-2', 'OR Grass Seed   MLRA-2'), ('OR Hops   MLRA-2', 'OR Hops   MLRA-2'), ('OR Mint   MLRA-2', 'OR Mint   MLRA-2'), ('PA Apple   MLRA-148', 'PA Apple   MLRA-148'), ('PA Corn   MLRA-148', 'PA Corn   MLRA-148'), ('PA Turf  MLRA-148', 'PA Turf  MLRA-148'), ('PR Coffee MLRA-270', 'PR Coffee MLRA-270'))
farm_select = (('No','No'), ('Yes','Yes'))

class ExamsInp(forms.Form):
    chemical_name = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            initial="Forchlorfenuron")
    scenarios = forms.ChoiceField(
            choices=scenario_select,
            label='Standard OPP/EFED Scenarios',
            initial='PA Turf  MLRA-148',
            validators=[validation.validate_choicefield])
    farm_pond = forms.ChoiceField(
            choices=farm_select,
            label='Farm pond (no flow)')
    molecular_weight = forms.FloatField(
            label='Molecular weight (g/mol)',
            initial=248,
            validators=[validation.validate_positive]) 
    solubility = forms.FloatField(
            label='Solubility(mg/L)',
            initial=39,
            validators=[validation.validate_positive])
    Koc = forms.FloatField(
            label='Aquatic Sediment Koc (mL/g)',
            initial=3526,
            validators=[validation.validate_positive])
    vapor_pressure = forms.FloatField(
            label='Vapor Pressure (torr)',
            initial="3.50e-10",
            validators=[validation.validate_positive])
    aerobic_aquatic_metabolism = forms.FloatField(
            label='Aerobic aquatic metabolism (days)',
            initial=1156,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    anaerobic_aquatic_metabolism = forms.FloatField(
            label='Anaerobic aquatic metabolism (days)',
            initial=226,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    aquatic_direct_photolysis = forms.FloatField(
            label='Aquatic Direct Photolysis (days)',
            initial=143,
            validators=[validation.validate_greaterthan0, validation.validate_integer])
    temperature = forms.FloatField(
            label=mark_safe('Test Temperature (<sup>o</sup>C)'),
            initial=25,
            validators=[validation.validate_range0100])