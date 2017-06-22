"""
.. module:: sam_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe

from ubertool_app.models.forms import validation


class SamInp_app():
    def __init__(self):
        self.html = self.application_table()

    @staticmethod
    def application_table():
        table = [("",
                  (("Crop Group",),)),
                 ("Application Timing",
                  (("Crop Stage",), ("Offset (days)",))),
                 ("Application Window",
                  (("Distribution",), ("Length 1",), ("% Applied",), ("Length 2",), ("% Applied",))),
                 ("Application Method",
                  (("Method",), ("Rate",), ("Efficiency",)))]

        # Add number-of-applications row
        html = """<table class="input_table tab tab_app tab_Application" border="0">"""
        html += """
                <tr><th colspan="1" scope="col"><label for="id_noa">Number of Applications:</label></th>
                    <td colspan="1" scope="col"><form id = "id_noa"><input type="number" id="id_noa" min="1" max="20" value="1"></form>
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
        initial="Simulation X")

    chemical_name = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        initial="Chemical A")  # Atrazine

    # watershed processes
    koc = forms.FloatField(
        required=False,
        label='Sorption Coefficient (mL/g)',
        initial=100,
        validators=[validation.validate_positive])

    kd_flag = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=((0, 'Koc'), (1, 'Kd')),
        initial=1,
        label='')

    soil_hl = forms.FloatField(
        required=False,
        label='Surface Soil Halflife (days), 25C',
        initial=10,
        validators=[validation.validate_positive])

    # water body processes

    wc_metabolism_hl = forms.FloatField(
        required=False,
        label='Aquatic metabolism half life (days)',
        initial=100,
        validators=[validation.validate_positive])

    ben_metabolism_hl = forms.FloatField(
        required=False,
        label='Benthic metabolism half life (days)',
        initial=100,
        validators=[validation.validate_positive])

    aq_photolysis_hl = forms.FloatField(
        required=False,
        label='Aqueous photolysis half life (days)',
        initial=100,
        validators=[validation.validate_positive])

    hydrolysis_hl = forms.FloatField(
        required=False,
        label='Hydrolysis halflife (days), pH 7',
        initial=100,
        validators=[validation.validate_positive])


class SamInp_sim(forms.Form):
    nhd_regions = ['01', '02', '03N', '03S', '03W', '04', '05', '06', '07', '08', '09',
                   '10U', '10L', '11', '12', '13', '14', '15', '16', '17', '18']

    REGION_CHOICES = [("mtb", "Mark Twain Basin")] + \
                     list(zip(nhd_regions, ("NHD Region {}".format(r) for r in nhd_regions)))

    TYPE_CHOICES = (('eco', 'Eco'), ('dwr', 'Drinking Water'), ('dwf', 'ESA'))

    region = forms.ChoiceField(
        required=False,
        label='Region',
        choices=REGION_CHOICES,
        initial="Mark Twain Basin")

    sim_type = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=TYPE_CHOICES)

    sim_date_start = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'datePicker'}),
        label='Start Date',
        initial="01/01/1984")  # choices=SIM_DATE_START_CHOICES  This earliest possible start date

    sim_date_end = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'datePicker'}),
        label='End Date',
        initial="12/31/2013")


class SamInp_output():
    def __init__(self):
        self.html = self.endpoint_table()

    @staticmethod
    def endpoint_table():
        header = ["Toxicity threshold", "Acute", "Chronic", "Overall (cancer)"]
        categories = ["Human health DWLOC (ug/L)",
                      "Freshwater Fish (Tox x LOC)",
                      "Freshwater Invertebrate (Tox x LOC)",
                      "Estuarine/Marine Fish (Tox x LOC)",
                      "Estuarine/Marine Invertebrate (Tox x LOC)",
                      "Aquatic nonvascular plant (Tox x LOC)",
                      "Aquatic vascular plant (Tox x LOC)"]

        # Add header
        html = """<table class="input_table tab tab_out tab_Output" border="0">"""
        html += '<tr id="header">'
        for heading in header:
            html += "<th>{}</th>".format(heading)
        html += "</tr>\n"

        for i, category in enumerate(categories):
            html += "<tr><td>{}</td>".format(category) + \
                    '<td><input name="acute" disabled="disabled" type="text" size="5"></td>\n' + \
                    '<td><input name="chronic" type="text" size="5"></td>\n'
            if not i:
                html += '<td><input name="overall" type="text" size="5"></td></tr>\n'
            else:
                pass

        html += "</table>"

        return html

    def __str__(self):
        return self.html


class SamInp(SamInp_app, SamInp_chem, SamInp_sim, SamInp_output):
    pass
