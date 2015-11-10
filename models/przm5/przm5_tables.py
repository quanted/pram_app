"""
.. module:: przm5_tables
   :synopsis: A useful module indeed.
"""

from django.template import Context, Template
from django.utils.safestring import mark_safe
import przm5_model
import time
import datetime
import os
from django.template.loader import render_to_string
import logging

def getheaderpvu():
    headings = ["Parameter", "Value", "Units"]
    return headings

def getheaderpvu2():
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
            <th colspan={{ th_span|default:'1' }}>{{ heading|safe }}</th>
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
 
def gett1data(przm5_obj):
    data = { 
        "Parameter": ['Sorption Coefficient Type', 'Sorption Coefficient', 'Soil Halflife', 'Soil Reference Temp',
                      'Foliar Halflife', 'Number of Degradates'],
        "Value": ['%s' % przm5_obj.koc_check_text, '%s' % przm5_obj.Koc[0], '%s' % przm5_obj.soilHalfLifeBox[0], '%s' % przm5_obj.soilTempBox1,
                  '%s' % przm5_obj.foliarHalfLifeBox[0], '%s' % przm5_obj.deg_check],
        "Units": ['', 'mL/g', 'day', '<sup>o</sup>C', 'day', ''],
    }
    return data

def gett1data_b(przm5_obj):
    data = { 
        "Parameter": ['Sorption Coefficient', 'Soil Halflife', 'Soil Reference Temp', 'Foliar Halflife',
                      'Molar Conversion Factors (Soil)', 'Molar Conversion Factors (Foliar)',],
        "Value": ['%s' % przm5_obj.Koc[1], '%s' % przm5_obj.soilHalfLifeBox[1], 25, '%s' % przm5_obj.foliarHalfLifeBox[1],
                  '%s' % przm5_obj.convertSoil1, '%s' % przm5_obj.convert_Foliar1,],
        "Units": ['mL/g', 'day', '<sup>o</sup>C', 'day', '', ''],
    }
    return data

def gett1data_c(przm5_obj):
    data = { 
        "Parameter": ['Sorption Coefficient', 'Soil Halflife', 'Soil Reference Temp', 'Foliar Halflife',
                      'Source of Degradate 2', 'Molar Conversion Factors (Soil)', 'Molar Conversion Factors (Foliar)',],
        "Value": ['%s' % przm5_obj.Koc[2], '%s' % przm5_obj.soilHalfLifeBox[2], 25, '%s' % przm5_obj.foliarHalfLifeBox[2],
                  '%s' % przm5_obj.deg2_source_text, '%s' % przm5_obj.convertSoil2, '%s' % przm5_obj.convert_Foliar2,],
        "Units": ['mL/g', 'day', '<sup>o</sup>C', 'day', '', '', ''],
    }
    return data


def gett2data(przm5_obj):
    data = { 
        "Parameter": ['Choose Way of Entering Application Dates', 'Number of Applications', 'Specify Years?', 'Enter Eff. & Drift/T for',],
        "Value": ['%s' % przm5_obj.app_date_type_text, '%s' % przm5_obj.noa, '%s' % 'No', '%s' % 'Pond',],
    }
    return data

def gett3data(przm5_obj):
    if przm5_obj.tempflag == 0:
        data = { 
            "Parameter": ['Scenario ID', 'Weather File', 'Emerge (DD/MM)', 'Mature (DD/MM)', 'Harvest (DD/MM)',
                          'Pan Factor', 'Snowmelt Factor', 'Evaportation Depth', 'Root Depth', 'Canopy Cover',
                          'Canopy Height', 'Canopy Holdup', 'Irrigation', 'Extra Water Fraction', 'Allowed Depletion', 
                          'Max Rate', 'Post-Harvest Foliage', 'No. of Horizons', 'Simulate Temperature'],
            "Value": ['%s' % przm5_obj.scenID, '%s' % przm5_obj.dvf_file, '%s' % przm5_obj.Emerge_text, '%s' % przm5_obj.Mature_text, '%s' % przm5_obj.Harvest_text,
                      '%s' % przm5_obj.pfac, '%s' % przm5_obj.snowmelt, '%s' % przm5_obj.evapDepth, '%s' % przm5_obj.rootDepth, '%s' % przm5_obj.canopyCover,
                      '%s' % przm5_obj.canopyHeight, '%s' % przm5_obj.canopyHoldup, '%s' % przm5_obj.irflag_text, '%s' % przm5_obj.fleach, '%s' % przm5_obj.depletion, 
                      '%s' % przm5_obj.rateIrrig, '%s' % przm5_obj.PestDispHarvest_text, '%s' % przm5_obj.noh, '%s' % 'No',],
            "Units": ['', '', '', '', '',
                      '', '', '', 'cm', '%',
                      'cm', 'cm', '', '', '',
                      '', '', '', ''],
        }
    else:
        data = { 
            "Parameter": ['Scenario ID', 'Weather File', 'Emerge (DD/MM)', 'Mature (DD/MM)', 'Harvest (DD/MM)',
                          'Pan Factor', 'Snowmelt Factor', 'Evaportation Depth', 'Root Depth', 'Canopy Cover',
                          'Canopy Height', 'Canopy Holdup', 'Irrigation', 'Extra Water Fraction', 'Allowed Depletion', 
                          'Max Rate', 'Post-Harvest Foliage', 'No. of Horizons', 'Simulate Temperature', 'Lower BC Temperature', 'Albedo'],
            "Value": ['%s' % przm5_obj.scenID, '%s' % przm5_obj.dvf_file, '%s' % przm5_obj.Emerge_text, '%s' % przm5_obj.Mature_text, '%s' % przm5_obj.Harvest_text,
                      '%s' % przm5_obj.pfac, '%s' % przm5_obj.snowmelt, '%s' % przm5_obj.evapDepth, '%s' % przm5_obj.rootDepth, '%s' % przm5_obj.canopyCover,
                      '%s' % przm5_obj.canopyHeight, '%s' % przm5_obj.canopyHoldup, '%s' % przm5_obj.irflag_text, '%s' % przm5_obj.fleach, '%s' % przm5_obj.depletion, 
                      '%s' % przm5_obj.rateIrrig, '%s' % przm5_obj.PestDispHarvest_text, '%s' % przm5_obj.noh, '%s' % 'Yes', '%s' % przm5_obj.bcTemp, '%s' % przm5_obj.albedo,],
            "Units": ['', '', '', '', '',
                      '', '', '', 'cm', '%',
                      'cm', 'cm', '', '', '',
                      '', '', '', '', '<sup>o</sup>C', ''],
        }

    return data

def gett4data(przm5_obj):
    data = { 
        "Parameter": ['USLE K', 'USLE LS', 'USLE P', 'IREG', 'Slope',
                      'R-Depth', 'R-Decline', 'Efficiency', 'E-Depth', 'E-Decline',],
        "Value": ['%s' % przm5_obj.uslek, '%s' % przm5_obj.uslels, '%s' % przm5_obj.uslep, '%s' % przm5_obj.ireg, '%s' % przm5_obj.slope,
                  '%s' % przm5_obj.rDepthBox, '%s' % przm5_obj.rDeclineBox, '%s' % przm5_obj.rBypassBox, '%s' % przm5_obj.eDepthBox, '%s' % przm5_obj.eDeclineBox,],
        "Units": ['', '', '', '', '%',
                  'cm', '1/cm', '', 'cm', '1/cm',],
    }
    return data

def gett5data(przm5_obj):
    data = { 
        "Parameter": ['Area of Field', 'Hydraulic Length',],
        "Value": ['%s' % przm5_obj.fieldSize, '%s' % przm5_obj.hydlength,],
        "Units": ['ha.', 'm',],
    }
    return data

pvuheadings = getheaderpvu()
pvuheadings2 = getheaderpvu2()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def timestamp(przm5_obj):
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%A, %Y-%B-%d %H:%M:%S')
    st = datetime.datetime.strptime(przm5_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A %Y-%m-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>PRZM 5<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def table_all(przm5_obj):
    logging.info(przm5_obj.deg2_source)

    table1_out = table_1(przm5_obj)
    table1_out_b = table_1_b(przm5_obj)
    table1_out_c = table_1_c(przm5_obj)
    if przm5_obj.deg_check == '0':
        table1_out_all = table1_out
    elif przm5_obj.deg_check == '1':
        table1_out_all = table1_out + table1_out_b
    elif przm5_obj.deg_check == '2':
        table1_out_all = table1_out + table1_out_b + table1_out_c
    table2_out = table_2(przm5_obj) + table_2_b(przm5_obj)
    table3_out = table_3(przm5_obj) + table_3_b(przm5_obj)
    table4_out = table_4(przm5_obj) + table_4_b(przm5_obj)
    table5_out = table_5(przm5_obj)
    table6_out = table_6(przm5_obj)
    table7_out = table_7(przm5_obj)
    table8_out = table_8(przm5_obj)

    html_plot = render_to_string('przm5-output-jqplot.html', {})
    # html_all = timestamp(przm5_obj) + table1_out + table2_out + table3_out + table4_out + html_plot
    html_all = table1_out_all + table2_out + table3_out + table4_out + table5_out + table6_out + table7_out + table8_out + html_plot
    return html_all


def table_1(przm5_obj):
    html = """<H3 class="out_1 collapsible" id="section1"><span></span>User Inputs:</H3>
                <div class="out_input_table out_">
                    <H4 class="out_1 collapsible" id="section2"><span></span>Chemical</H4>
                        <div class="out_ container_output">
               """
    if przm5_obj.koc_check == '1':
        przm5_obj.koc_check_text='Koc'
    else:
        przm5_obj.koc_check_text='Kd'
    if przm5_obj.deg2_source == '1':
        przm5_obj.deg2_source_text = 'Degradate 1'
    else:
        przm5_obj.deg2_source_text = 'Parent'
    t1data = gett1data(przm5_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
            </div>
    """
    return html

def table_1_b(przm5_obj):
    html = """<H4 class="out_1 collapsible" id="section2"><span></span>Chemical Degradate 1</H4>
                        <div class="out_ container_output">
               """
    t1data_b = gett1data_b(przm5_obj)
    t1rows_b = gethtmlrowsfromcols(t1data_b, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows_b, headings=pvuheadings)))
    html = html + """
            </div>
    """
    return html

def table_1_c(przm5_obj):
    html = """<H4 class="out_1 collapsible" id="section2"><span></span>Chemical Degradate 2</H4>
                        <div class="out_ container_output">
               """
    t1data_c = gett1data_c(przm5_obj)
    t1rows_c = gethtmlrowsfromcols(t1data_c, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows_c, headings=pvuheadings)))
    html = html + """
            </div>
    """
    return html

def table_2(przm5_obj):
    html = """<H4 class="out_3 collapsible" id="section2"><span></span>Application (n=%s)</H4>
                <div class="out_input_table out_">
               """%(przm5_obj.noa)
    if przm5_obj.app_date_type == '0':
        przm5_obj.app_date_type_text = 'Absolute Dates'
    else:
        przm5_obj.app_date_type_text = 'Relative Dates'
    t2data = gett2data(przm5_obj)
    t2rows = gethtmlrowsfromcols(t2data, pvuheadings2)
    html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings2)))
    html = html + """
            </div>
    """
    return html

def getheader_table_2b():
    headings = ["Day", "Month", "Year", "Amount", "Application", "Depth", "Eff", "Drift"]
    headings_show = ["Day", "Month", "Year", "Amount (kg/hA)", "Application Method", "Depth (cm)", "Eff.", "Drift/T"]
    return headings, headings_show

table_2b_headings = getheader_table_2b()

def gett2data_b(Day, Month, Amount, Method, Depth, Eff, Drift):
    data = { 
        "Day": ['%s' %Day,],
        "Month": ['%s' %Month, ],
        "Year": ['NA'],
        "Amount": ['%s' %Amount,],
        "Application": ['%s' %Method,],
        "Depth": ['%s' %Depth,],
        "Eff": ['%s' %Eff,],
        "Drift": ['%s' %Drift,],
    }
    return data

def table_2_b(przm5_obj):
        # #pre-table 2
        html = """
                <div class="out_ container_output">
        """ 
        #table 2_b
        t2_b_data_all=[]
        for i in range(int(przm5_obj.noa)):
            Day_temp = przm5_obj.PestAppyDay[i]
            Month_temp = przm5_obj.PestAppyMon[i]
            Amount_temp = przm5_obj.PestAppyRate[i]
            Method_temp = przm5_obj.ApplicationTypes[i]
            Depth_temp = przm5_obj.DepthIncorp[i]
            Eff_temp = przm5_obj.localEff[i]
            Drift_temp = przm5_obj.localSpray[i]

            t2_d_data_temp=gett2data_b(Day_temp, Month_temp, Amount_temp, Method_temp, Depth_temp, Eff_temp, Drift_temp)
            t2_b_data_all.append(t2_d_data_temp)

        t2_b_data = dict([(k,[t2data_ind[k][0] for t2data_ind in t2_b_data_all]) for k in t2_d_data_temp])
        t2_b_rows = gethtmlrowsfromcols(t2_b_data, table_2b_headings[0])
        html = html + tmpl.render(Context(dict(data=t2_b_rows, headings=table_2b_headings[1])))
        html = html + """
                </div>
        """
        return html

def table_3(przm5_obj):
    html = """<H4 class="out_3 collapsible" id="section2"><span></span>Crop/Land</H3>
                <div class="out_input_table out_">
               """
    if przm5_obj.irflag == '0':
        przm5_obj.irflag_text = 'None'
    elif przm5_obj.irflag == '1':
        przm5_obj.irflag_text = 'Over Canopy'
    else:
        przm5_obj.irflag_text = 'Under Canopy'
    if przm5_obj.PestDispHarvest == '1':
        przm5_obj.PestDispHarvest_text = 'Surface Applied'
    elif przm5_obj.PestDispHarvest == '2':
        przm5_obj.PestDispHarvest_text = 'Removed'
    else:
        przm5_obj.PestDispHarvest_text = 'Left as Foliage'
    t3data = gett3data(przm5_obj)
    t3rows = gethtmlrowsfromcols(t3data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t3rows, headings=pvuheadings)))
    html = html + """
            </div>
    """
    return html

def getheader_table_3b():
    headings = ["thick", "rho", "max_cap", "min_cap", "oc", "n"]
    headings_show = ["Thick", "&#961;", "Max. Cap.", "Min. Cap.", "O.C.", "N"]
    return headings, headings_show

table_3b_headings = getheader_table_3b()


def gett3data_b(thick, rho, max_cap, min_cap, oc, n):
    data = { 
        "thick": ['%s' %thick,],
        "rho": ['%s' %rho, ],
        "max_cap": ['%s' %max_cap,],
        "min_cap": ['%s' %min_cap,],
        "oc": ['%s' %oc,],
        "n": ['%s' %n,],
    }
    return data

def table_3_b(przm5_obj):
        # #pre-table 3
        html = """
                <div class="out_ container_output">
        """ 
        #table 3_b
        t3_b_data_all=[]
        for i in range(int(przm5_obj.noh)):
            thick_temp = przm5_obj.SoilProperty_thick[i]
            rho_temp = przm5_obj.SoilProperty_bulkden[i]
            max_cap_temp = przm5_obj.SoilProperty_maxcap[i]
            min_cap_temp = przm5_obj.SoilProperty_mincap[i]
            oc_temp = przm5_obj.SoilProperty_oc[i]
            n_temp = przm5_obj.SoilProperty_compartment[i]

            t3_b_data_temp=gett3data_b(thick_temp, rho_temp, max_cap_temp, min_cap_temp, oc_temp, n_temp)
            t3_b_data_all.append(t3_b_data_temp)

        t3_b_data = dict([(k,[t3data_ind[k][0] for t3data_ind in t3_b_data_all]) for k in t3_b_data_temp])
        t3_b_rows = gethtmlrowsfromcols(t3_b_data, table_3b_headings[0])
        html = html + tmpl.render(Context(dict(data=t3_b_rows, headings=table_3b_headings[1])))
        html = html + """
                </div>
        """
        return html


def table_4(przm5_obj):
    html = """<H4 class="out_3 collapsible" id="section2"><span></span>Runoff</H3>
                <div class="out_input_table out_">
               """
    t4data = gett4data(przm5_obj)
    t4rows = gethtmlrowsfromcols(t4data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t4rows, headings=pvuheadings)))
    html = html + """
            </div>
    """
    return html


def getheader_table_4b():
    headings = ["No", "Day", "Month", "Year", "CN", "C", "N"]
    headings_show = ["No.", "Day", "Month", "Year", "CN", "C", "N"]
    return headings, headings_show

table_4b_headings = getheader_table_4b()


def gett4data_b(No, Day, Month, Year, CN, C, N):
    data = { 
        "No": ['%s' %No,],
        "Day": ['%s' %Day, ],
        "Month": ['%s' %Month,],
        "Year": ['%s' %Year,],
        "CN": ['%s' %CN,],
        "C": ['%s' %C,],
        "N": ['%s' %N,],
    }
    return data

def table_4_b(przm5_obj):
        # #pre-table 4
        html = """
                <div class="out_ container_output">
        """ 
        #table 4_b
        t4_b_data_all=[]
        for i in range(int(przm5_obj.nott)):
            No_temp = i+1
            Day_temp = przm5_obj.USLE_day[i]
            Month_temp = przm5_obj.USLE_mon[i]
            CN_temp = przm5_obj.USLE_cn[i]
            C_temp = przm5_obj.USLE_c[i]
            N_temp = przm5_obj.USLE_n[i]
            try:
                Year_temp = przm5_obj.USLE_year[i]
            except:
                Year_temp = '1972'

            t4_b_data_temp=gett4data_b(No_temp, Day_temp, Month_temp, Year_temp, CN_temp, C_temp, N_temp)
            t4_b_data_all.append(t4_b_data_temp)

        t4_b_data = dict([(k,[t4data_ind[k][0] for t4data_ind in t4_b_data_all]) for k in t4_b_data_temp])
        t4_b_rows = gethtmlrowsfromcols(t4_b_data, table_4b_headings[0])
        html = html + tmpl.render(Context(dict(data=t4_b_rows, headings=table_4b_headings[1])))
        html = html + """
                </div>
        """
        return html




def table_5(przm5_obj):
    html = """<H4 class="out_3 collapsible" id="section2"><span></span>Water Body</H3>
                <div class="out_input_table out_">
               """
    t5data = gett5data(przm5_obj)
    t5rows = gethtmlrowsfromcols(t5data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t5rows, headings=pvuheadings)))
    html = html + """
            </div>
        </div>
    """
    return html


def table_6(przm5_obj):
    html = """  <H3 class="out_3 collapsible" id="section1"><span></span>User Outputs</H3>
                <div class="out_3">
                    <H4 class="out_1 collapsible" id="section1"><span></span>Download</H4>
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
                </div>"""%(przm5_obj.link)
    return html

def table_7(przm5_obj):
    html = """  <H4 class="out_4 collapsible" id="section1" style="display: none"><span></span>Plot</H4>
                <div class="out_4 container_output">
                    <table class="out_" style="display: none">
                        <tr>
                            <td id="x_pre_irr">pre+irr</td>
                            <td id="x_pre_irr_val_%s">%s</td>
                        </tr>
                        <tr>
                            <td id="x_et">et</td>
                            <td id="x_et_val_%s">%s</td>
                        </tr>
                        <tr>
                            <td id="x_runoff">runoff</td>
                            <td id="x_runoff_val_%s">%s</td>
                        </tr>                          
                    </table>
                </div>"""%(1, przm5_obj.PRCP_IRRG_sum, 1, przm5_obj.CEVP_TETD_sum, 1, przm5_obj.RUNF_sum)
    return html

def table_8(przm5_obj):
    html = """
            <H3 class="out_3 collapsible" id="section1"><span></span>Plots</H3>
            <div class="out_3">
                <H4 class="out_4 collapsible" id="section1"><span></span></H4>
                    <div id="chart1" style="margin-top:20px; margin-left:20px; width:600px; height:400px;"></div>
                <H4 class="out_4 collapsible" id="section1"><span></span></H4>
                    <div id="chart2" style="margin-top:20px; margin-left:20px; width:600px; height:400px;"></div>
            </div>
           """
    return html

