"""
.. module:: sam_tables
   :synopsis: A useful module indeed.
"""
from django.template import Context, Template
from django.utils.safestring import mark_safe
import time
import datetime
from django.template.loader import render_to_string
import sam_parameters


def timestamp(sam_obj="", batch_jid=""):
    if sam_obj:
        st = datetime.datetime.strptime(sam_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
    <b>Spatial Aquatic Model (SAM) Beta<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def getheaderpvu():
    headings = ["Parameter", "Value", "Units"]
    return headings

def getheaderpv():
    headings = ["Parameter", "Value"]
    return headings

def gethtmlrowsfromcols(data, headings):
    columns = [data[heading] for heading in headings]

    # get the length of the longest column
    max_len = len(max(columns, key=len))

    for col in columns:
        # padding the short columns with None
        col += [None,] * (max_len - len(col))

    # Then rotate the structure...
    rows = [[col[i] for col in columns] for i in range(max_len)]
    return rows

def getdjtemplate():
    dj_template ="""
    <table class="out_">
    {# headings #}
        <tr>
        {% for heading in headings %}
            <th colspan={{ th_span|default:'1' }}>{{ heading }}</th>
        {% endfor %}
        </tr>
    
    {% if sub_headings %}
        <tr>
        {% for sub_heading in sub_headings %}
            <th>{{ sub_heading }}</th>
        {% endfor %}
        </tr>
    {% endif %}
    {# data #}
    {% for row in data %}
    <tr>
        {% for val in row %}
        <td>{{ val|default:''|safe }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    </table>
    """
    return dj_template

pvuheadings = getheaderpvu()
pvheadings = getheaderpv()

djtemplate = getdjtemplate()
tmpl = Template(djtemplate)
 
########################
# Table Initialization #
########################
def gett1data(sam_obj):
    
    if (sam_obj.scenario_selection == '1'):
        scenario = 'Atrazine - Corn'
        chemical_name = 'Atrazine'
        koc = '100'
        soil_hl = '123'
    elif (sam_obj.scenario_selection == '2'):
        scenario = 'Chlorpyrifos - Corn'
        chemical_name = 'Chlorpyrifos'
        koc = '6040'
        soil_hl = '109'
    elif (sam_obj.scenario_selection == '3'):
        scenario = 'Chlorpyrifos - Soybeans'
        chemical_name = 'Chlorpyrifos'
        koc = '6040'
        soil_hl = '109'
    elif (sam_obj.scenario_selection == '4'):
        scenario = 'Fipronil - Corn'
        chemical_name = 'Fipronil'
        koc = '727'
        soil_hl = '128'
    elif (sam_obj.scenario_selection == '5'):
        scenario = 'Metolachlor - Corn'
        chemical_name = 'Metolachlor'
        koc = '181'
        soil_hl = '49'
    else:
        scenario = 'n/a'
        chemical_name = 'n/a'
        koc = 'n/a'
        soil_hl = 'n/a'    

    data = {
        "Parameter": ['Scenario', 'Chemical Name', 'Koc', 'Soil Metabolism Halflife'],
        "Value": [scenario, chemical_name, koc, soil_hl],
        "Units": ['', '', 'mL/g', 'days']
    }
    # data = {
    #     "Parameter": ['Chemical Name', 'Koc', 'Soil Metabolism Halflife'],
    #     "Value": ['%s' % sam_obj.chemical_name, sam_obj.koc, '%s' % sam_obj.soil_metabolism_hl],
    #     "Units": ['', 'mL/g', 'days']
    # }
    return data

def gett2data(sam_obj):
    # Convert tuple into dictionary
    # CROP_CHOICES = dict(sam_parameters.SamInp_app.CROP_CHOICES)
    
    # try:
    #     app_method = sam_parameters.SamInp_app.APP_METH_CHOICES[int(sam_obj.app_method) - 1][1]
    # except:
    #     app_method = ""

    # try:
    #     refine = sam_parameters.SamInp_app_refine.REFINEMENT_CHOICES[int(sam_obj.refine) - 1][1]
    # except:
    #     refine = ""
    no_of_crops = '4'
    app_meth = 'Ground'
    if (sam_obj.scenario_selection == '1'):
        crop = 'Corn, Corn/grains, Corn/wheat, Corn/soybeans'
        noa = '1500'
        app_rate = '1.3'
        refinements = 'Uniform Step Application over Window'
        time_win = '7'
        percent_app = '50'
        time_win2 = '43'
        percent_app2 = '50'
    elif (sam_obj.scenario_selection == '2'):
        crop = 'Corn, Corn/grains, Corn/wheat, Corn/soybeans'
        noa = '900'
        app_rate = '1.1'
        refinements = 'Uniform Application over Window'
        time_win = '30'
        percent_app = '100'
    elif (sam_obj.scenario_selection == '3'):
        crop = 'Soybeans, Soybeans/grains, Soybeans/wheat, Soybeans/cotton'
        noa = '1260'
        app_rate = '1.1'
        refinements = 'Uniform Application over Window'
        time_win = '42'
        percent_app = '100'
    elif (sam_obj.scenario_selection == '4'):
        crop = 'Corn, Corn/grains, Corn/wheat, Corn/soybeans'
        noa = '1500'
        app_rate = '0.1'
        refinements = 'Uniform Step Application over Window'
        time_win = '7'
        percent_app = '50'
        time_win2 = '43'
        percent_app2 = '50'
    elif (sam_obj.scenario_selection == '5'):
        crop = 'Corn, Corn/grains, Corn/wheat, Corn/soybeans'
        noa = '1500'
        app_rate = '1.05'
        refinements = 'Uniform Step Application over Window'
        time_win = '7'
        percent_app = '50'
        time_win2 = '43'
        percent_app2 = '50'
    else:
        crop = 'n/a'
        no_of_crops = 'n/a'
        noa = 'n/a'
        app_meth = 'n/a'
        app_rate = 'n/a'
        refinements = 'n/a'
        time_win = 'n/a'
        percent_app = 'n/a'
    
    if (refinements == 'Uniform Step Application over Window'):
        data = {
            "Parameter": ['Crop(s)', 'Total Number of Crops', 'Total Number of Applications',
                            'Application method', 'Application Rate', 'Refinements',
                            'Time Window #1', 'Percent Applied #1', 'Time Window #2', 'Percent Applied #2' ],
            "Value": [crop, no_of_crops, noa,
                        app_meth, app_rate, refinements,
                        time_win, percent_app, time_win2, percent_app2 ],
            "Units": ['', '', '', '', 'kg/ha', '', 'days', '%', 'days', '%']
        }
    else:
        data = {
            "Parameter": ['Crop', 'Total Number of Crops', 'Total Number of Applications',
                            'Application method', 'Application Rate', 'Refinements',
                            'Time Window', 'Percent Applied' ],
            "Value": [crop, no_of_crops, noa,
                        app_meth, app_rate, refinements,
                        time_win, percent_app ],
            "Units": ['', '', '', '', 'kg/ha', '', 'days', '%']
        }
    # data = {
    #     "Parameter": ['Crop', 'Total Number of Crops', 'Total Number of Applications',
    #                     'Application method', 'Application Rate', 'Refinements',
    #                     'Time Window', 'Percent Applied' ],
    #     "Value": ['%s' % CROP_CHOICES[int(sam_obj.crop)], sam_obj.crop_number, '%s' % sam_obj.noa,
    #                 '%s' % app_method, sam_obj.application_rate, '%s' % refine,
    #                 '%s' % sam_obj.refine_time_window, sam_obj.refine_percent_applied ],
    #     "Units": ['', '', '', '', 'kg/ha', '', 'days', '']
    # }
    return data

def gett3data(sam_obj):
    # try:
    #     sim_type = sam_parameters.SamInp_sim.SIM_CHOICES[int(sam_obj.sim_type) - 1][1]
    # except:
    #     sim_type = ""
    
    data = {
        "Parameter": ['Sate/Region', 'Simulation Type', 'Start Date', 'End Date', 'First Application Date'],
        "Value": [ 'Ohio Valley', 'Eco', '01/01/1984', '12/31/2013', '04/20/1984' ]
    }

    # data = {
    #     "Parameter": ['Sate/Region', 'Simulation Type', 'Start Date', 'End Date', 'First Application Date'],
    #     "Value": ['%s' % sam_obj.region, sim_type,
    #                 '%s' % sam_obj.sim_date_start, '%s' % sam_obj.sim_date_end, '%s' % sam_obj.sim_date_1stapp ]
    # }
    return data

def gett4data(sam_obj):
    # try:
    #     output_type = sam_parameters.SamInp_output.OUTPUT_TYPE_CHOICES[int(sam_obj.output_type) - 1][1]
    # except:
    #     output_type = ""

    # try:
    #     output_tox = sam_parameters.SamInp_output.TOX_PERIOD_CHOICES[int(sam_obj.output_tox) - 1][1]
    # except:
    #     output_tox = ""

    data = {
        "Parameter": ['Output Preference', '', '', '', 'Threshold Time Period', mark_safe('Threshold (&micro;g/L)'), 'Output Format'],
        "Value": ['21-d Average Concentrations - 90th percentile',
                    '60-d Average Concentrations - 90th percentile',
                    'Toxicity Threshold - Average Duration of Daily Exceedances',
                    'Toxicity Threshold - Percentage of Days with Exceedances',
                    '30-d, Annual', '4', 'CSVs & Map'],
    }

    # data = {
    #     "Parameter": ['Output Preference', 'Threshold Time Period', 'Threshold', 'Output Format'],
    #     "Value": ['%s' % output_type, output_tox, '%s' % sam_obj.output_tox_value, '%s' % sam_obj.output_format],
    #     "Units": ['', '', mark_safe('&micro;g/L'), '']
    # }
    return data


###################
# Table Formating #
###################
def table_1(sam_obj):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs:</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Chemical Properties</H4>
                <div class="out_ container_output">
        """
        tdata = gett1data(sam_obj)
        trows = gethtmlrowsfromcols(tdata,pvuheadings)
        html = html + tmpl.render(Context(dict(data=trows, headings=pvuheadings)))
        html = html + """
                </div>
        """
        return html

def table_2(sam_obj):
        html = """
            <H4 class="out_1 collapsible" id="section2"><span></span>Application</H4>
                <div class="out_ container_output">
        """
        tdata = gett2data(sam_obj)
        trows = gethtmlrowsfromcols(tdata,pvuheadings)
        html = html + tmpl.render(Context(dict(data=trows, headings=pvuheadings)))
        html = html + """
                </div>
        """
        return html

def table_3(sam_obj):
        html = """
            <H4 class="out_1 collapsible" id="section2"><span></span>Simulation</H4>
                <div class="out_ container_output">
        """
        tdata = gett3data(sam_obj)
        trows = gethtmlrowsfromcols(tdata,pvheadings)
        html = html + tmpl.render(Context(dict(data=trows, headings=pvheadings)))
        html = html + """
                </div>
        """
        return html

def table_4(sam_obj):
        html = """
            <H4 class="out_1 collapsible" id="section2"><span></span>Output Settings</H4>
                <div class="out_ container_output">
        """
        tdata = gett4data(sam_obj)
        trows = gethtmlrowsfromcols(tdata,pvheadings)
        html = html + tmpl.render(Context(dict(data=trows, headings=pvheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_all(sam_obj):

    html = table_1(sam_obj)
    html = html + table_2(sam_obj)
    html = html + table_3(sam_obj)
    html = html + table_4(sam_obj)
    
    if (sam_obj.scenario_selection == '1'):
        link = 'https://s3.amazonaws.com/super_przm/postprocessed/Atrazine_corn.zip'
        scenario = 'atrazine_corn'
    elif (sam_obj.scenario_selection == '2'):
        link = 'https://s3.amazonaws.com/super_przm/postprocessed/Chlorpyrifos_corn.zip'
        scenario = 'chlorpyrifos_corn'
    elif (sam_obj.scenario_selection == '3'):
        link = 'https://s3.amazonaws.com/super_przm/postprocessed/Chlorpyrifos_soybeans.zip'
        scenario = 'chlorpyrifos_soybeans'
    elif (sam_obj.scenario_selection == '4'):
        link = 'https://s3.amazonaws.com/super_przm/postprocessed/Fipronil_corn.zip'
        scenario = 'fipronil_corn'
    elif (sam_obj.scenario_selection == '5'):
        link = 'https://s3.amazonaws.com/super_przm/postprocessed/Metolachlor_corn.zip'
        scenario = 'metolachlor_corn'
    else:
        link = ''
        scenario = 'atrazine_corn'

    html = html + """
    <br>
    <H3 class="out_3 collapsible" id="section1"><span></span>Model Outputs</H3>
    <div class="out_3">
        <H4 class="out_1 collapsible" id="section1"><span></span>Download Model Output</H4>
            <div class="out_ container_output">
                <table class="out_">
                    <tr>
                        <th scope="col">Outputs</div></th>
                        <th scope="col">Value</div></th>                            
                    </tr>
                    <tr>
                        <td>Simulation is finished. Please download your file from here</td>
                        <td><a href=%s>Link</a></td>
                    </tr>
                </table>
            </div>
    """ % link

    html = html + render_to_string('sam_mapping_demo.html', {'SCENARIO' : scenario})
    html = html + render_to_string('sam_charts_demo.html', {'SCENARIO' : scenario})

    return html