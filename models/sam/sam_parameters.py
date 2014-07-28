"""
.. module:: sam_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.template import Context, Template
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation


class SamInp_chem(forms.Form):
    chemical_name = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 1}), initial="Chemical X")
    koc = forms.FloatField(required=True,label='Koc (mL/g)', initial=2)
    soil_metabolism_hl = forms.FloatField(required=True,label='Soil Metabolism Halflife (days)', initial=45)


class SamInp_app(forms.Form):
	CROP_CHOICES = (
		(10, "Corn"),
		(14, "Corn/soybeans"),
		(15, "Corn/wheat"),
		(18, "Corn/grains"),
		(20, "Cotton"),
		(25, "Cotton/wheat"),
		(26, "Cotton/vegetables"),
		(30, "Rice"),
		(40, "Soybeans"),
		(42, "Soybeans/cotton"),
		(45, "Soybeans/wheat"),
		(48, "Soybeans/grains"),
		(50, "Wheat"),
		(56, "Wheat/vegetables"),
		(58, "Wheat/grains"),
		(60, "Vegetables/ground fruit"),
		(61, "Ground fruit"),
		(68, "Vegetables/grains"),
		(70, "Orchards/grapes"),
		(75, "Other trees"),
		(80, "Other grains"),
		(90, "Other row crops"),
		(100, "Other crops"),
		(110, "Pasture/hay/forage"),
		(121, "Developed - open"),
		(122, "Developed - low"),
		(123, "Developed - med"),
		(124, "Developed - high"),
		(140, "Forest"),
		(150, "Grassland"),
		(160, "Shrubland"),
		(180, "Water"),
		(190, "Wetlands - woods"),
		(195, "Wetlands - herbaceous"),
		(200, "Miscellaneous land")
	)
	APP_METH_CHOICES = (
		(1, 'Ground'),
		(2, 'Foliar')
	)

	crop = forms.ChoiceField(choices=CROP_CHOICES)
	crop_number = forms.FloatField(required=True, label='Total Number of Crops', initial=1)
	noa = forms.FloatField(required=True, label='Total Number of Applications', initial=4)
	application_method = forms.ChoiceField(choices=APP_METH_CHOICES)
	application_rate = forms.FloatField(required=True, label='Application Rate (kg/ha)', initial=0.75)


class SamInp_app_refine(forms.Form):
	REFINEMENT_CHOICES = (
		(1, 'Uniform Application over Window'),
		(2, 'Uniform Step Application over Window'),
		(3, 'Triangular Application over Window')
	)

	refine = forms.ChoiceField(choices=REFINEMENT_CHOICES, label="Refinements")
	refine_time_window = forms.FloatField(required=False, label='Time Window (days)') # jQuery hides onLoad
	refine_percent_applied = forms.FloatField(required=False, label='Percent Applied') # jQuery hides onLoad


class SamInp_sim(forms.Form):
	SIM_CHOICES = (
		(1, 'Eco'),
		(2, 'DW Reservoirs'),
		(3, 'DW Flowing')
	)
	SIM_DATE_START_CHOICES = (
		(1, 'Thursday, January 1, 1970'),
	)
	SIM_DATE_END_CHOICES = (
		(1, 'Monday, December 31, 2012'),
	)
	SIM_DATE_1STAPP_CHOICES = (
		(1, 'Monday, April 20, 1970'),
	)
	SIM_STATE = (
		('Illinois', 'Illinois'),
		('Indiana', 'Indiana'),
		('Kentucky', 'Kentucky'),
		('Ohio', 'Ohio'),
		('Ohio Valley', 'Ohio Valley'),
		('Pennsylvania', 'Pennsylvania'),
		('Tennessee', 'Tennessee'),
		('West Virginia', 'West Virginia')
	)

	state = forms.ChoiceField(choices=SIM_STATE, label='Sate/Region')
	sim_type = forms.ChoiceField(widget=forms.RadioSelect, choices=SIM_CHOICES)
	sim_date_start = forms.DateField(widget=forms.DateInput(attrs={'class': 'datePicker'}), label='Start Date', initial="01/01/1970") #choices=SIM_DATE_START_CHOICES
	sim_date_end = forms.DateField(widget=forms.DateInput(attrs={'class': 'datePicker'}), label='End Date', initial="12/31/2012") #choices=SIM_DATE_END_CHOICES
	sim_date_1stapp = forms.DateField(widget=forms.DateInput(attrs={'class': 'datePicker'}), label='First Application Date', initial="01/01/1970") #choices=SIM_DATE_1STAPP_CHOICES


class SamInp_output(forms.Form):
	OUTPUT_TYPE_CHOICES = (
		(1, 'Daily Concentrations'),
		(2, '30-day Maximum Concentrations'),
		(3, 'Toxicity Threshold Exceedances')
	)
	TOX_PERIOD_CHOICES = (
		(1, '30-d'),
		(2, 'Annual')
	)
	OUTPUT_FORMAT_CHOICES = (
		(1, 'Generate Table'),
		(2, 'Generate Map')
	)

	output_type = forms.ChoiceField(choices=OUTPUT_TYPE_CHOICES, label='Output Preference')
	output_tox = forms.ChoiceField(choices=TOX_PERIOD_CHOICES, label='Threshold Time Period')
	output_tox_value = forms.FloatField(required=False, label=mark_safe('Threshold (&micro;g/L)')) # jQuery hides onLoad
	output_format = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OUTPUT_FORMAT_CHOICES, label='Output Format')


class SamInp(SamInp_chem, SamInp_app, SamInp_app_refine, SamInp_sim, SamInp_output):
	pass