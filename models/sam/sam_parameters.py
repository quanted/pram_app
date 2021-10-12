"""
.. module:: sam_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from pram_app.models.forms import validation

kd_CHOICES = (('0', 'Koc'), ('1', 'Kd'))
TYPE_CHOICES = (('eco', 'Eco'), ('dwr', 'Drinking Water'))


class SamInp_app():

    def __init__(self):
        self.html = self.application_table()

    @staticmethod
    def application_table():
        table = [("",
                  (("Crop Group",),)),
                 ("Application Timing",
                  (("Stage",), ("Offset",))),
                 ("Application Window",
                  (("Distribution",), ("Length 1",), ("% Applied",), ("Length 2",), ("% Applied",))),
                 ("Application Method",
                  (("Method",), ("Rate",), ("Efficiency",)))]

        # Add number-of-applications row
        html = """<table class="input_table tab tab_app tab_Application" border="0">"""
        html += """
                <tr><th colspan="1" scope="col"><label for="id_noa">Number of Applications:</label></th>
                    <td colspan="1" scope="col"><form id = "id_noa"><input name="napps" type="number" id="id_noa" min="1" max="20" value="1"></form>
                    </td>
                </tr>
                """

        # Set field width
        field_size = 10

        # Add super-header
        html += '<tr id="super_header">\n'
        for group, fields in table:
            html += "<th colspan='{}'>{}</th>\n".format(len(fields), group)
        html += "</tr>"

        # Add sub-header
        html += '<tr id="sub_header">\n'
        html += "\n".join(
            ("<th width='{}'>{}</th>".format(field_size, field[0]) for _, fields in table for field in fields))
        html += "</tr>"

        # Add first row
        html += "</tr></table>"

        return html

    def __str__(self):
        return self.html


class SamInp_chem(forms.Form):

    # Chemical
    simulation_name = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        initial="test")#initial="Mark Twain Atrazine 062217")

    chemical_name = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        initial='atrazine')  # Atrazine

    # watershed processes
    kd_flag = forms.ChoiceField(
        required=False,
        label='Soil Adsorption Coefficient Type',
        choices=kd_CHOICES,
        initial='1')

    koc = forms.FloatField(
        required=False,
        label='Soil Adsorption Coefficient (mL/g)',
        initial=75,
        validators=[validation.validate_positive])

    soil_hl = forms.FloatField(
        required=False,
        label='Surface Soil Halflife (days), 25C',
        initial=139,
        validators=[validation.validate_positive])

    # water body processes

    wc_metabolism_hl = forms.FloatField(
        required=False,
        label='Aquatic metabolism half life (days)',
        initial=277,
        validators=[validation.validate_positive])

    ben_metabolism_hl = forms.FloatField(
        required=False,
        label='Benthic metabolism half life (days)',
        initial=277,
        validators=[validation.validate_positive])

    aq_photolysis_hl = forms.FloatField(
        required=False,
        label='Aqueous photolysis half life (days)',
        initial=168,
        validators=[validation.validate_positive])

    hydrolysis_hl = forms.FloatField(
        required=False,
        label='Hydrolysis halflife (days), pH 7',
        initial=0,
        validators=[validation.validate_positive])


class SamInp_sim(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SamInp_sim, self).__init__(*args, **kwargs)
        self.fields['region'].initial = 'Mark Twain Demo'

    nhd_regions = ['01', '02', '03N', '03S', '03W', '04', '05', '06', '07', '08', '09',
               '10U', '10L', '11', '12', '13', '14', '15', '16', '17', '18', 'Mark Twain Demo']
    REGION_CHOICES = tuple(list(zip(nhd_regions, ("NHD Region {}".format(r) for r in nhd_regions))))
    # region_type = forms.CharField(max_length=10, choices=REGION_CHOICES)

    region = forms.ChoiceField(
        choices=REGION_CHOICES,
        label='Region',
        # initial='01'
    )
        # initial="mtb")

    sim_type = forms.ChoiceField(
        required=False,
        label='Simulation Type',
        choices=TYPE_CHOICES,
        disabled=True,
        initial='dwr',)

    sim_date_start = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'datePicker'}),
        label='Start Date',
        initial="01/01/2000")  # choices=SIM_DATE_START_CHOICES  This earliest possible start date

    sim_date_end = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'datePicker'}),
        label='End Date',
        initial="12/31/2015")


class SamInp_output():
    def __init__(self):
        self.html = self.endpoint_table()

    @staticmethod
    def endpoint_table():
        atrazine_defaults = [[3.4, "", ""],
                             [2650, 0.5, ""],
                             [360, 60, ""],
                             [1000, 0.5, ""],
                             [24, 80, ""],
                             [1, "", ""],
                             [4.6, "", ""]]

        header = ["Toxicity threshold", "Acute", "Chronic", "Overall (cancer)"]
        categories = [("Human health DWLOC (ug/L)", 'human'),
                      ("Freshwater Fish (Tox x LOC)", 'fw_fish'),
                      ("Freshwater Invertebrate (Tox x LOC)", 'fw_inv'),
                      ("Estuarine/Marine Fish (Tox x LOC)", 'em_fish'),
                      ("Estuarine/Marine Invertebrate (Tox x LOC)", 'em_inv'),
                      ("Aquatic nonvascular plant (Tox x LOC)", 'nonvasc_plant'),
                      ("Aquatic vascular plant (Tox x LOC)", 'vasc_plant')]

        # Add header
        html = """<table class="input_table tab tab_out tab_Output" border="0">"""
        html += '<tr id="header">'
        for heading in header:
            html += "<th>{}</th>".format(heading)
        html += "</tr>\n"

        # Build table
        defaults = atrazine_defaults
        for i, (category, tag) in enumerate(categories):
            row = defaults[i]
            html += "<tr><td>{}</td>".format(category) + \
                    '<td><input name="acute_{}" value="{}" disabled="disabled" type="text" size="5"></td>\n'.format(tag, row[0]) + \
                    '<td><input name="chronic_{}" value="{}" type="text" size="5"></td>\n'.format(tag, row[1])
            if not i:
                html += '<td><input name="overall_human" value="{}" type="text" size="5"></td></tr>\n'.format(defaults[0][2])
            else:
                pass

        html += "</table>"

        return html

    def __str__(self):
        return self.html


# class SamInp(SamInp_app, SamInp_chem, SamInp_sim, SamInp_output):
class SamInp(SamInp_sim):
    def __init__(self, *args, **kwargs):
        super(SamInp, self).__init__(*args, **kwargs)
        self.fields['region'].initial = 'Mark Twain Basin'
    #pass
