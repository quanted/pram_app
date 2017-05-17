"""
.. module:: agdrift_tables
   :synopsis: A useful module indeed.
"""

# import django
import datetime
import logging

from django.template import Context, Template

logger = logging.getLogger("AgdriftTables")


def getheaderpvu():
    headings = ["Parameter", "Value"]
    return headings


def getheaderpvr():
    headings = ["Parameter", "Value"]
    return headings


def getheadersum():
    headings = ["Parameter", "Mean", "Std", "Min", "Max", "Unit"]
    return headings


def gethtmlrowsfromcols(data, headings):
    columns = [data[heading] for heading in headings]

    # get the length of the longest column
    max_len = len(max(columns, key=len))

    for col in columns:
        # padding the short columns with None
        col += [None, ] * (max_len - len(col))

    # Then rotate the structure...
    rows = [[col[i] for col in columns] for i in range(max_len)]
    return rows


def getdjtemplate():
    dj_template = """
    <table class="out_">
    {# headings #}
        <tr>
        {% for heading in headings %}
            <th>{{ heading }}</th>
        {% endfor %}
        </tr>
    {# data #}
    {% for row in data %}
    <tr>
        {% for val in row %}
        <td>{{ val|default:'' }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    </table>
    """
    return dj_template


def gett1data(agdrift_obj):
    # general inputs describing scenario to be executed

    #localize variables for table construction
    assess_type = agdrift_obj.ecosystem_type
    app_rate = agdrift_obj.application_rate
    calc_input = agdrift_obj.calculation_input
    chem_name = agdrift_obj.chemical_name
    app_method = agdrift_obj.application_method

    if(app_method == 'tier_1_aerial'):
        drop_size = agdrift_obj.drop_size_aerial

        data = {
            "Parameter": ['Chemical Name', 'Application method', 'Drop size', 'Assessment type', 'Application rate',
                          'Calculation Input', ],
            "Value": [chem_name, app_method, drop_size, assess_type, app_rate, calc_input,],
        }
    elif(app_method == 'tier_1_ground'):
        drop_size = agdrift_obj.drop_size_ground
        boom_hgt = agdrift_obj.boom_height

        data = {
            "Parameter": ['Chemical Name', 'Application method', 'Drop size', 'Boom Height', 'Assessment type',
                          'Application rate', 'Calculation Input', ],
            "Value": [chem_name, app_method, drop_size, boom_hgt, assess_type, app_rate, calc_input,],
        }
    else:  #this is the airblast application
        blast_type = agdrift_obj.airblast_type

        data = {
            "Parameter": ['Chemical Name', 'Application method', 'Airblast Type', 'Assessment type',
                          'Application rate', 'Calculation Input', ],
            "Value": [chem_name, app_method, blast_type, assess_type, app_rate, calc_input,],
        }

    return data


def gett2data(agdrift_obj):
    #dimentions of the exposure area (i.e., pond, wetland, or terrestrial field)

    #localize variables for table construction
    assess_type = agdrift_obj.ecosystem_type

    if(assess_type == 'aquatic_assessment'):
        waterbody_type = agdrift_obj.aquatic_body_type
        
        width = agdrift_obj.out_area_width
        length = agdrift_obj.out_area_length
        depth = agdrift_obj.out_area_depth

        # if(waterbody_type == 'EPA Defined Pond'):
        #     #width = agdrift_obj.default_width
        #     #length = agdrift_obj.default_length
        #     #depth = agdrift_obj.default_pond_depth
        #     width = 208.7
        #     length = 515.8
        #     depth = 6.56
        # elif(waterbody_type == 'User Defined Pond'):
        #     width = agdrift_obj.user_pond_width
        #     length = agdrift_obj.sqft_per_hectare / width
        #     depth = agdrift_obj.user_pond_depth
        # elif(waterbody_type == 'EPA Defined Wetland'):
        #     #width = agdrift_obj.default_width
        #     #length = agdrift_obj.default_length
        #     #depth = agdrift_obj.out_default_wetland_depth
        #     width = 208.7
        #     length = 515.8
        #     depth = 6.56
        # elif(waterbody_type == 'User Defined Wetland'):
        #     width = agdrift_obj.user_wetland_width
        #     length = agdrift_obj.sqft_per_hectare / width
        #     depth = agdrift_obj.user_wetland_depth

        data = {
            "Parameter": ['Waterbody_type', 'Width (feet)', 'Length (feet)', 'Depth (feet)', ],
            "Value": [waterbody_type, width, length, depth, ],
        }

    else:  #this is a terrestrial assessment
        terrestrial_type = agdrift_obj.terrestrial_field_type

        if(terrestrial_type == 'epa_defined_terrestrial'):  #this is a point deposition
            width = 'NA'
            depth = 'NA'
            length = 'NA'
            data = {
                "Parameter": ['Terrestrial Type', 'Width (feet)', 'Length (feet)', 'Depth (feet)', ],
                "Value": [terrestrial_type, width, length, depth, ],
            }
        else: #this is an average deposition over a field
            width = agdrift_obj.user_terrestrial_width
            length = 'NA'  #length of terrestrial field is not relevant to output calculations 
            depth = 'NA'

            data = {
                "Parameter": ['Terrestrial Type', 'Width (feet)', 'Length (feet)', 'Depth (feet)', ],
                "Value": [terrestrial_type, width, length, depth, ],
            }
    return data


def gett3data(agdrift_obj):
    data = {
        "Parameter": ['Assessment type', 'Application method', 'Aquatic Body Type', 'Drop size', 'Scenario', ],
        "Value": [agdrift_obj.ecosystem_type, agdrift_obj.application_method, agdrift_obj.aquatic_body_type,
                  agdrift_obj.drop_size, agdrift_obj.out_sim_scenario_chk, ],
    }
    return data


def gett4data(agdrift_obj):
    data = {
        "Parameter": ['Assessment type', 'Application method', 'Aquatic Body Type', 'Drop size', 'Scenario', ],
        "Value": [agdrift_obj.ecosystem_type, agdrift_obj.application_method, agdrift_obj.aquatic_body_type,
                  agdrift_obj.drop_size, agdrift_obj.out_sim_scenario_chk, ],
    }
    return data


# def gett2data(agdrift_obj):
#    data = { 
#        "Parameter": ['Distance', 'Spray drift fraction',],
#        "Value": [agdrift_obj.results[0], agdrift_obj.results[1],],
#    }
#    return data


def gett5data(agdrift_obj):
    #model outputs (note: user specifies any one of these and the rest are calculated

    #localize variables for table construction



    range_chk_out = agdrift_obj.out_range_chk
    range_chk_in =  agdrift_obj.out_sim_scenario_chk
    foa = agdrift_obj.out_avg_dep_foa
    gha = agdrift_obj.out_avg_dep_gha
    lbac = agdrift_obj.out_avg_dep_lbac
    ngl = agdrift_obj.out_avg_waterconc_ngl
    mgcm2 = agdrift_obj.out_avg_field_dep_mgcm2
    dist = agdrift_obj.out_distance_downwind

    if(agdrift_obj.ecosystem_type == 'aquatic_assessment'):
        if (range_chk_out == 'out of range' or 'Invalid' in range_chk_in ):
            data = {
                "Parameter": ['Range Check', 'Distance to Waterbody (ft)', 'Spray drift fraction of applied',
                              'Initial Average Deposition (g/ha)', 'Initial Average Deposition (lb/ac)',
                              'Initial Average Concentration (ng/L)', ],
                # "Value": ['%.3f' % agdrift_obj.out_init_avg_dep_foa,'%.3f' % agdrift_obj.out_avg_dep_gha,'%.3f' % agdrift_obj.out_avg_dep_lbac, '%.3f' % agdrift_obj.out_deposition_ngl, '%.3f' % agdrift_obj.out_avg_field_dep_mgcm,],
                "Value": ['width and/or distance is out of range', '{0:.2f}'.format(dist), '{0:.4e}'.format(foa), '{0:.4e}'.format(gha),
                          '{0:.4e}'.format(lbac), '{0:.4e}'.format(ngl), ],
            }
        else:
            data = {
                "Parameter": ['Distance to Waterbody (ft)', 'Spray drift fraction of applied',
                              'Initial Average Deposition (g/ha)', 'Initial Average Deposition (lb/ac)',
                              'Initial Average Concentration (ng/L)', ],
                # "Value": ['%.3f' % agdrift_obj.out_init_avg_dep_foa,'%.3f' % agdrift_obj.out_avg_dep_gha,'%.3f' % agdrift_obj.out_avg_dep_lbac, '%.3f' % agdrift_obj.out_deposition_ngl, '%.3f' % agdrift_obj.out_avg_field_dep_mgcm,],
                "Value": ['{0:.2f}'.format(dist), '{0:.4e}'.format(foa), '{0:.4e}'.format(gha),
                          '{0:.4e}'.format(lbac), '{0:.4e}'.format(ngl), ],
            }
    elif(agdrift_obj.ecosystem_type == 'terrestrial_assessment'
         and agdrift_obj.terrestrial_field_type == 'epa_defined_terrestrial'):
        if (range_chk_out == 'out of range'):
            data = {
                "Parameter": ['Range Check', 'Distance to Point (ft)', 'Spray drift fraction of applied',
                              'Initial Point Deposition (g/ha)', 'Initial Point Deposition (lb/ac)',
                              'Initial Point Deposition (mg/cm2)', ],
                 "Value": ['calculated distance is out of range', '{0:.2f}'.format(dist), '{0:.4e}'.format(foa), '{0:.4e}'.format(gha),
                          '{0:.4e}'.format(lbac), '{0:.4e}'.format(mgcm2), ],
            }
        else:
            data = {
                "Parameter": ['Distance to Point (ft)', 'Spray drift fraction of applied',
                              'Initial Point Deposition (g/ha)', 'Initial Point Deposition (lb/ac)',
                              'Initial Point Deposition (mg/cm2)', ],
                "Value": ['{0:.2f}'.format(dist), '{0:.4e}'.format(foa), '{0:.4e}'.format(gha),
                          '{0:.4e}'.format(lbac), '{0:.4e}'.format(mgcm2), ],
            }
    elif(agdrift_obj.ecosystem_type == 'terrestrial_assessment'
         and agdrift_obj.terrestrial_field_type == 'user_defined_terrestrial'):
        if (range_chk_out == 'out of range'):
            data = {
                "Parameter": ['Range Check', 'Distance to Terrestrial Field (ft)', 'Spray drift fraction of applied',
                              'Initial Average Deposition (g/ha)', 'Initial Average Deposition (lb/ac)',
                              'Initial Average Deposition (mg/cm2)', ],
                 "Value": ['calculated distance is out of range', '{0:.2f}'.format(dist), '{0:.4e}'.format(foa), '{0:.4e}'.format(gha),
                          '{0:.4e}'.format(lbac), '{0:.4e}'.format(mgcm2), ],
            }
        else:
            data = {
                "Parameter": ['Distance to Terrestrial Field (ft)', 'Spray drift fraction of applied',
                              'Initial Average Deposition (g/ha)', 'Initial Average Deposition (lb/ac)',
                              'Initial Average Deposition (mg/cm2)', ],
                "Value": ['{0:.2f}'.format(dist), '{0:.4e}'.format(foa), '{0:.4e}'.format(gha),
                          '{0:.4e}'.format(lbac), '{0:.4e}'.format(mgcm2), ],
            }

    return data


pvuheadings = getheaderpvu()
pvrheadings = getheaderpvr()
# pvrheadingsqaqc = getheaderpvrqaqc()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(agdrift_obj):
    html_all = table_1(agdrift_obj)
    html_all = html_all + table_2(agdrift_obj)
    #html_all = html_all + table_3(agdrift_obj)
    #html_all = html_all + table_4(agdrift_obj)
    html_all = html_all + table_5(agdrift_obj)
    # html_all = html_all + table_3(agdrift_obj)
    # html_all = html_all + render_to_string('agdrift-output-jqplot.html', {'chart_num':1}) #agdrift_obj.loop_indx
    return html_all


def timestamp(agdrift_obj="", batch_jid=""):
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%A, %Y-%B-%d %H:%M:%S')
    if agdrift_obj:
        st = datetime.datetime.strptime(agdrift_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html = """
    <div class="out_">
    <b>Agdrift Version 0.1 (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def table_1(agdrift_obj):
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section1"><span></span>Application and Chemical Information</H4>
                <div class="out_ container_output">
        """
    t1data = gett1data(agdrift_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_2(agdrift_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Aquatic Body Information</H4>
            <div class="out_ container_output">
        """
    t2data = gett2data(agdrift_obj)
    t2rows = gethtmlrowsfromcols(t2data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings)))
    html = html + """
            </div>
        """
    return html


def table_3(agdrift_obj):
    html = """
        <H4 class="out_3 collapsible" id="section2"><span></span>Model Output</H4>
            <div class="out_ container_output">
        """
    t3data = gett3data(agdrift_obj)
    t3rows = gethtmlrowsfromcols(t3data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t3rows, headings=pvuheadings)))
    html = html + """
            </div>
        """
    return html


def table_4(agdrift_obj):
    html = """
    <H4 class="out_4 collapsible" id="section2"><span></span>Model Output</H4>
        <div class="out_ container_output">
    """
    t4data = gett4data(agdrift_obj)
    t4rows = gethtmlrowsfromcols(t4data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t4rows, headings=pvuheadings)))
    html = html + """
        </div>
    """
    return html


def table_5(agdrift_obj):
    html = """
    <H4 class="out_5 collapsible" id="section2"><span></span>Model Output</H4>
        <div class="out_ container_output">
    """
    t5data = gett5data(agdrift_obj)
    t5rows = gethtmlrowsfromcols(t5data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t5rows, headings=pvuheadings)))
    html = html + """
        </div>
    """
    return html


def table_6(agdrift_obj):
    html = """
        <table style="display:none;">
            <tr>
                <td>distance</td>
                <td id="distance{0!s}">{1!s}</td>
            </tr>
            <tr>
                <td>deposition</td>
                <td id="deposition{2!s}">{3!s}</td>
            </tr>
        </table>
        <br>
        <h3 class="out_6 collapsible" id="section2"><span></span>Results</h3>
            <H4 class="out_6 collapsible" id="section3"><span></span>Plot of spray drift</H4>
                <div class="out_"></div>
        """.format(1, agdrift_obj.out_x, 1, agdrift_obj.out_express_y)  # agdrift_obj.loop_indx

    # t2data = gett2data(agdrift_obj)
    # t2rows = gethtmlrowsfromcols(t2data,pvrheadings)
    # html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings)))
    # html = html + """
    #         </div>
    # """
    return html
