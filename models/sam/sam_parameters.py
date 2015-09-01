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

    SCENARIO_CHOICES = (
        (1, 'Corn 1'),  #Atrazine
        (2, 'Corn 2'),  #Chlorpyrifos
        (3, 'Soybeans'),  #Chlorpyrifos
        (4, 'Corn 3'),  #Fipronil
        (5, 'Corn 4'),  #Metolachlor
        (0, 'Custom')
    )
    COEFFICIENT_CHOICES = (
        (1, 'Koc'),
        (2, 'Kd')
    )

    scenario_selection = forms.ChoiceField(
            choices = SCENARIO_CHOICES,
            label = 'Choose a Scenario')
    chemical_name = forms.CharField(
            required=False,
            widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
            initial="Atrazine")
    koc = forms.FloatField(
            required=False,
            label='Sorption Coefficient (mL/g)',
            initial=100,
            validators=[validation.validate_positive])
    coefficient = forms.ChoiceField(
            required=False,
            widget = forms.RadioSelect,
            choices = COEFFICIENT_CHOICES,
            initial = 1,
            label = '')
    soil_metabolism_hl = forms.FloatField(
            required=False,
            label='Soil Metabolism Halflife (days)',
            initial=123,
            validators=[validation.validate_positive])


class SamInp_app(forms.Form):
    CROP_CHOICES = (
        ("10 14 15 18", "Corn"),
        ("20 25 26 42", "Cotton"),
        ("40 42 45 48 14", "Soybeans"),
        ("50 56 58 15 45", "Wheat"),
        ("60 56 26 68", "Vegetables"),
        ("60 61", "Ground fruit"),
        ("70", "Orchards"),
        ("70", "Grapes, vineyards"),
        ("75", "Other trees"),
        ("80 48 18 58", "Other grains"),
        ("90", "Other row crops"),
        ("100", "Other crops"),
        ("110 150", "Pasture/hay/forage/grass"),

        # (0, "Choose up to 4 crops"),
        # (10, "Corn"),
        # #(14, "Corn/soybeans"),
        # #(15, "Corn/wheat"),
        # #(18, "Corn/grains"),
        # (20, "Cotton"),
        # #(25, "Cotton/wheat"),
        # #(26, "Cotton/vegetables"),
        # #(30, "Rice"),
        # (40, "Soybeans"),
        # #(42, "Soybeans/cotton"),
        # #(45, "Soybeans/wheat"),
        # #(48, "Soybeans/grains"),
        # (50, "Wheat"),
        # #(56, "Wheat/vegetables"),
        # #(58, "Wheat/grains"),
        # #(60, "Vegetables/ground fruit"),
        # (61, "Ground fruit"),
        # #(68, "Vegetables/grains"),
        # #(70, "Orchards/grapes"),
        # (75, "Other trees"),
        # (80, "Other grains"),
        # (90, "Other row crops"),
        # (100, "Other crops")
        # #(110, "Pasture/hay/forage"),
        # #(121, "Developed - open"),
        # #(122, "Developed - low"),
        # #(123, "Developed - med"),
        # #(124, "Developed - high"),
        # #(140, "Forest"),
        # #(150, "Grassland"),
        # #(160, "Shrubland"),
        # #(180, "Water"),
        # #(190, "Wetlands - woods"),
        # #(195, "Wetlands - herbaceous"),
        # #(200, "Miscellaneous land")
    )
    APP_METH_CHOICES = (
        (1, 'Ground'),
        (2, 'Foliar')
    )

    crop_list_no = forms.CharField(
            # This field is hidden by jQuery and holds the list of chosen crops
            required=False,
            widget=forms.Textarea({'cols': 20, 'rows': 1}))

    crop = forms.MultipleChoiceField (
            required=False,
            widget=forms.SelectMultiple(attrs={'size' : 4}),
            choices=CROP_CHOICES,
            label=mark_safe("Crop Groups<br>('Ctrl' to select multiple)"))
    # crop = forms.ChoiceField(
    #         required=False,
    #         choices=CROP_CHOICES,
    #         validators=[validation.validate_choicefield])
    try:
        crop_number = forms.FloatField(
            required=False,
            label='Total Number of Crops',
            initial=0,
            widget=forms.NumberInput(attrs={'readonly': 'true'}))
    except:
        crop_number = forms.FloatField(
            required=False,
            label='Total Number of Crops',
            initial=0,
            widget=forms.TextInput(attrs={'readonly': 'true'}))
    apps_per_year = forms.FloatField(
            required=False,
            label='Number of Applications per Year',
            initial=1,
            validators=[validation.validate_greaterthan0])
    application_method = forms.ChoiceField(
            required=False,
            choices=APP_METH_CHOICES)
    application_rate = forms.FloatField(
            required=False,
            label='Application Rate (kg/ha)',
            initial=1.3,
            validators=[validation.validate_positive])
    sim_date_1stapp = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'datePicker'}),
            label='First Application Date',
            initial="04/20/1984")


class SamInp_app_refine(forms.Form):
    REFINEMENT_CHOICES = (
        ('uniform', 'Uniform Application over Window'),
        ('uniform_step', 'Uniform Step Application over Window'),
        ('triangular', 'Triangular Application over Window')
    )

    refine = forms.ChoiceField(
            required=False,
            choices=REFINEMENT_CHOICES,
            label="Refinements",
            initial='uniform_step')
    refine_time_window1 = forms.FloatField(
            required=False,
            label='Time Window (days)',
            validators=[validation.validate_positive])
    refine_percent_applied1 = forms.FloatField(
            required=False,
            label='Percent Applied',
            validators=[validation.validate_positive])
    refine_time_window2 = forms.FloatField(				# jQuery hides onLoad
            required=False,
            label='Time Window #2 (days)',
            validators=[validation.validate_positive])
    refine_percent_applied2 = forms.FloatField(			# jQuery hides onLoad
            required=False,
            label='Percent Applied #2',
            validators=[validation.validate_positive])


class SamInp_sim(forms.Form):
    SIM_CHOICES = (
        ('eco', 'Eco'),
        ('dwr', 'DW Reservoirs'),
        ('dwf', 'DW Flowing')
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
    # SIM_STATE = (
    #     ('Illinois', 'Illinois'),
    #     ('Indiana', 'Indiana'),
    #     ('Kentucky', 'Kentucky'),
    #     ('Ohio', 'Ohio'),
    #     ('Ohio Valley', 'Ohio Valley'),
    #     ('Pennsylvania', 'Pennsylvania'),
    #     ('Tennessee', 'Tennessee'),
    #     ('West Virginia', 'West Virginia')
    # )

    # region = forms.ChoiceField(
    #         required=False,
    #         choices=SIM_STATE,
    #         label='State/Region')
    region = forms.CharField(
            required=False,
            label='State/Region',
            initial='Ohio River Valley',
            widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
    )
    sim_type = forms.ChoiceField(
            required=False,
            widget=forms.RadioSelect,
            choices=SIM_CHOICES)
    sim_date_start = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'datePicker'}),
            label='Start Date',
            initial="01/01/1984") #choices=SIM_DATE_START_CHOICES  This earliest possible start date
    sim_date_end = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'datePicker'}),
            label='End Date',
            initial="12/31/2013") #choices=SIM_DATE_END_CHOICES  6/2/2014 is latest possible end date
     #choices=SIM_DATE_1STAPP_CHOICES


class SamInp_output(forms.Form):

    # OUTPUT_TYPE_CHOICES = (
    # 	(1, '21-d Average Concentrations - 90th percentile'),
    # 	(2, '60-d Average Concentrations - 90th percentile'),
    # 	(3, 'Toxicity Threshold - Average Duration of Daily Exceedances'),
    # 	(4, 'Toxicity Threshold - Percentage of Days with Exceedances')
    # )
    OUTPUT_TYPE_CHOICES = (
        (1, 'Daily Concentrations'),
        (2, 'Time-Averaged Results'),
    )
    TIME_AVG_CHOICES = (
        (1, 'Time-Averaged Concentrations'),
        (2, 'Toxicity Threshold Exceedances'),
    )
    TIME_AVG_CONC_CHOICES = (
        (1, 'Daily time-average concentrations'),
        (2, 'Annual max time-average concentrations')
    )
    TOX_THRES_EXCEED_CHOICES = (
        (1, 'Frequency of exceeding threshold, by year'),
        (2, 'Frequency of exceeding threshold, by month'),
        (3, 'Average duration of exceedance (days), by year'),
        (4, 'Average duration of exceedance (days), by month')
    )
    OUTPUT_FORMAT_CHOICES = (
        (1, 'Generate CSVs'),
        (2, 'Generate Map'),
        (3, 'Plots / Histograms')
    )
    # OUTPUT_WORKER_CHOICES = (
    #     (1, '1 Worker'),
    #     (2, '2 Workers'),
    #     (4, '4 Workers'),
    #     (8, '8 Workers'),
    #     (16, '16 Workers')
    # )
    # OUTPUT_PROCESS_CHOICES = (
    #     (1, '1x Workers'),
    #     (2, '2x Workers'),
    #     (3, '3x Workers')
    # )

    # output_type = forms.ChoiceField(
    # 		required=False,
    # 		choices=OUTPUT_TYPE_CHOICES,
    # 		initial = 2,
    # 		label='Output Preference')
    output_type = forms.ChoiceField(
            required=False,
            choices=OUTPUT_TYPE_CHOICES,
            widget = forms.RadioSelect,
            initial = 2,
            label='Output Preference')
    output_avg_days = forms.IntegerField(
            required=False,
            label='Averaging Period (days)',
            initial=4,
            min_value=1,
            max_value=365)
    output_time_avg_option = forms.ChoiceField(
            required=False,
            label='',
            widget=forms.RadioSelect,
            initial=2,
            choices = TIME_AVG_CHOICES
    )
    output_time_avg_conc = forms.ChoiceField(
            required=False,
            widget=forms.Select(attrs={'size' : 2}),
            choices=TIME_AVG_CONC_CHOICES,
            initial=1,
            label='')
    output_tox_value = forms.FloatField(
            required=False,
            label=mark_safe('Threshold (&micro;g/L)'),
            initial=4)
    output_tox_thres_exceed = forms.ChoiceField(
            required=False,
            widget=forms.Select(attrs={'size' : 4}),
            choices=TOX_THRES_EXCEED_CHOICES,
            label='')
    output_format = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=OUTPUT_FORMAT_CHOICES,
            label='Output Format')
    # workers = forms.ChoiceField(
    #         required=False,
    #         choices=OUTPUT_WORKER_CHOICES,
    #         label='Number of Concurrent Processes (Workers)',
    #         initial=4)
    # processes = forms.ChoiceField(
    #         required=False,
    #         choices=OUTPUT_PROCESS_CHOICES,
    #         label='Total Number of Processes',
    #         initial=1)
    workers = forms.FloatField(
            required=False,
            label='Number of Concurrent Processes (Workers)',
            initial=16)
    processes = forms.FloatField(
            required=False,
            label='Number of Processes Multiplier',
            initial=1)

 
class SamInp(SamInp_chem, SamInp_app, SamInp_app_refine, SamInp_sim, SamInp_output):
    pass
