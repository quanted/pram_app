"""
.. module:: beerex_tables
   :synopsis: A useful module indeed.
"""

import numpy
from django.template import Context, Template
from django.utils.safestring import mark_safe
import logging
import datetime

logger = logging.getLogger("beerexTables")


def getheaderinp():
    headings = ["Description", "Value"]
    return headings


def getheadertox():
    headings = ["Description", "Value (ug a.i./bee)"]
    return headings


def getheadereecs():
    headings = ["Application Method", "EECs (ug a.i./mg)"]
    return headings


def getheaderrqs():
    headings = ["Life Stage & Caste", "Age (days)", "Jelly (mg/day)", "Nectar (mg/day)", "Pollen (mg/day)", "Total Dose (ug a.i./bee)", "Acute RQ", "Chronic RQ"]
    return headings


# def getheadermaxrq():
#     headings = ["Exposure", "Adults", "Larvae"]
#     return headings


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


def gett1data(beerex_obj):
    data = { 
        "Description": ['Application rate (lb a.i./A)', 'Application method', mark_safe('Log Kow'), mark_safe('Koc)'), 'Mass of tree vegetation (kg-wet weight)'],
        "Value": [beerex_obj.application_rate, beerex_obj.application_method, beerex_obj.log_kow, beerex_obj.koc, beerex_obj.mass_tree_vegetation,]
    }
    return data


def gett2data(beerex_obj):
    data = { 
        "Description": ['Adult Contact LD50', 'Adult Oral LD50', 'Adult Oral NOAEL', 'Larval LD50', 'Larval NOAEL'],
        "Value (ug a.i./bee)": ['%g' % beerex_obj.adult_contact_ld50, '%g' % beerex_obj.adult_oral_ld50, '%g' % beerex_obj.adult_oral_noael, '%g' % beerex_obj.larval_ld50, '%s' % beerex_obj.larval_noael,]
    }
    return data


def gett3data(beerex_obj):
    data = { 
        "Application Method": ['Foliar Spray', 'Soil Application', 'Seed Treatment', 'Tree Trunk'],
        "EECs (ug a.i./mg)": ['%g' % beerex_obj.out_eec_spray, '%g' % beerex_obj.out_eec_soil,'%g' % beerex_obj.out_eec_seed, '%s' % beerex_obj.out_eec_tree,],
    }
    return data


def gett4data(beerex_obj):
    data = { 
        "Life Stage & Caste": ['Larval Worker', 'Larval Worker', 'Larval Worker', 'Larval Worker', 'Larval Worker',
                               'Larval Drone', 'Larval Queen', 'Larval Queen', 'Larval Queen', 'Larval Queen',
                               'Adult Worker (cell cleaning and capping)', 'Adult Worker (brood and queen tending, nurse bees)',
                               'Adult Worker (comb building, cleaning and food handling)', 'Adult Worker (foraging for pollen)',
                               'Adult Worker (foraging for nectar)', 'Adult Worker (maintenance of hive in winter)', 'Adult Drone',
                               'Adult Queen (laying 1500 eggs/day)'],
        "Average Age (days)": ['1', '2', '3', '4', '5', '6+', '1', '2', '3', '4+', '0-10', '6-17', '11-18', '>18', '>18', '0-90', '>10', 'entire lifestage'],
        "Jelly (mg/day)": ['%g' % beerex_obj.lw1_jelly, '%g' % beerex_obj.lw2_jelly, '%g' % beerex_obj.lw3_jelly, '%g', '%g', '%g', '%g' % beerex_obj.lq1_jelly,
                           '%g' % beerex_obj.lq2_jelly, '%g' % beerex_obj.lq3_jelly, '%g' % beerex_obj.lq4_jelly, '%g', '%g', '%g', '%g', '%g', '%g', '%g', '%s' % beerex_obj.aq_jelly],
        "Nectar (mg/day)": ['%g', '%g', '%g', '%g' % beerex_obj.lw4_nectar, '%g' % beerex_obj.lw5_nectar, '%g' % beerex_obj.ld6_nectar, '%g', '%g', '%g', '%g',
                            '%g' % beerex_obj.aw_cell_nectar, '%g' % beerex_obj.aw_brood_nectar, '%g' % beerex_obj.aw_comb_nectar, '%g' % beerex_obj.aw_fpollen_nectar,
                            '%g' % beerex_obj.aw_fnectar_nectar, '%g' % beerex_obj.aw_winter_nectar, '%g' % beerex_obj.ad_nectar, '%s'],
        "Pollen (mg/day)": ['%g', '%g', '%g', '%g' % beerex_obj.lw4_pollen, '%g' % beerex_obj.lw5_pollen, '%g' % beerex_obj.ld6_pollen, '%g', '%g', '%g', '%g',
                            '%g' % beerex_obj.aw_cell_pollen, '%g' % beerex_obj.aw_brood_pollen, '%g' % beerex_obj.aw_comb_pollen, '%g' % beerex_obj.aw_fpollen_pollen,
                            '%g' % beerex_obj.aw_fnectar_pollen, '%g' % beerex_obj.aw_winter_pollen, '%g' % beerex_obj.ad_pollen, '%s'],
        "Total Dose (ug a.i./bee)": ['%g' % beerex_obj.out_lw1_total_dose, '%g' % beerex_obj.out_lw2_total_dose, '%g' % beerex_obj.out_lw3_total_dose,
                                     '%g' % beerex_obj.out_lw4_total_dose, '%g' % beerex_obj.out_lw5_total_dose, '%g' % beerex_obj.out_ld6_total_dose,
                                     '%g' % beerex_obj.out_lq1_total_dose, '%g' % beerex_obj.out_lq2_total_dose, '%g' % beerex_obj.out_lq3_total_dose,
                                     '%g' % beerex_obj.out_lq4_total_dose, '%g' % beerex_obj.out_aw_cell_total_dose, '%g' % beerex_obj.out_aw_brood_total_dose,
                                     '%g' % beerex_obj.out_aw_comb_total_dose, '%g' % beerex_obj.out_aw_fpollen_total_dose, '%g' % beerex_obj.out_aw_fnectar_total_dose,
                                     '%g' % beerex_obj.out_aw_winter_total_dose, '%g' % beerex_obj.out_ad_total_dose, '%s' % beerex_obj.out_aq_total_dose],
        "Acute RQ": ['%g' % beerex_obj.out_lw1_acute_rq, '%g' % beerex_obj.out_lw2_acute_rq, '%g' % beerex_obj.out_lw3_acute_rq, '%g' % beerex_obj.out_lw4_acute_rq,
                     '%g' % beerex_obj.out_lw5_acute_rq, '%g' % beerex_obj.out_ld6_acute_rq, '%g' % beerex_obj.out_lq1_acute_rq, '%g' % beerex_obj.out_lq2_acute_rq,
                     '%g' % beerex_obj.out_lq3_acute_rq, '%g' % beerex_obj.out_lq4_acute_rq, '%g' % beerex_obj.out_aw_cell_acute_rq, '%g' % beerex_obj.out_aw_brood_acute_rq,
                     '%g' % beerex_obj.out_aw_comb_acute_rq, '%g' % beerex_obj.out_aw_pollen_acute_rq, '%s' % beerex_obj.out_aw_nectar_acute_rq,
                     '%g' % beerex_obj.out_aw_winter_acute_rq, '%g' % beerex_obj.out_ad_chronic_rq, '%g' % beerex_obj.out_aq_chronic_rq],
        "Chronic RQ": ['%g' % beerex_obj.out_lw1_chronic_rq, '%g' % beerex_obj.out_lw2_chronic_rq, '%g' % beerex_obj.out_lw3_chronic_rq, '%g' % beerex_obj.out_lw4_chronic_rq,
                       '%g' % beerex_obj.out_lw5_chronic_rq, '%g' % beerex_obj.out_ld6_chronic_rq, '%g' % beerex_obj.out_lq1_chronic_rq, '%g' % beerex_obj.out_lq2_chronic_rq,
                       '%g' % beerex_obj.out_lq3_chronic_rq, '%g' % beerex_obj.out_lq4_chronic_rq, '%g' % beerex_obj.out_aw_cell_chronic_rq, '%g' % beerex_obj.out_aw_brood_chronic_rq,
                       '%g' % beerex_obj.out_aw_comb_chronic_rq, '%g' % beerex_obj.out_aw_pollen_chronic_rq, '%g' % beerex_obj.out_aw_nectar_chronic_rq,
                       '%g' % beerex_obj.out_aw_winter_chronic_rq, '%g' % beerex_obj.out_ad_chronic_rq, '%s' % beerex_obj.out_aq_chronic_rq]
    }
    return data


# def gett5data(beerex_obj):
#     data = {
#         "Exposure": ['Acute Contact', 'Acute Dietary', 'Chronic Dietary'],
#         "Adults": ['%g' % numpy.max(beerex_obj.out_adult_acute_rq), '%g' % numpy.max(out_dose_mamm), '%g' % numpy.max(out_at_bird)],
#         "Larvae": ['%g', '%g' % numpy.max(out_dose_mamm), '%g' % numpy.max(out_at_bird)]
#     }
#     return data


inpheadings = getheaderinp()
toxheadings = getheadertox()
eecheadings = getheadereecs()
rqsheadings = getheaderrqs()
# maxrqheadings = getheadermaxrq()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(beerex_obj):
    html_all = table_1(beerex_obj)
    html_all = html_all + table_2(beerex_obj)
    html_all = html_all + table_3(beerex_obj)
    html_all = html_all + table_4(beerex_obj)
    # html_all = html_all + table_5(beerex_obj)
    return html_all


def timestamp(beerex_obj="", batch_jid=""):
    if beerex_obj:
        st = datetime.datetime.strptime(beerex_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>beerex <a href="http://www.epa.gov/oppefed1/models/terrestrial/beerex/beerex_user_guide.html">Version 1.0</a> (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def table_1(beerex_obj):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Application Information</H4>
                <div class="out_ container_output">
        """
        t1data = gett1data(beerex_obj)
        t1rows = gethtmlrowsfromcols(t1data, inpheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=inpheadings)))
        html = html + """
                </div>
        </div>
        """
        return html


def table_2(beerex_obj):
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>User Inputs</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Toxicity data</H4>
                <div class="out_ container_output">
        """
        t2data = gett2data(beerex_obj)
        t2rows = gethtmlrowsfromcols(t2data, toxheadings)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=toxheadings)))
        html = html + """
                </div>
        """
        return html  


def table_3(beerex_obj):
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>Bee-Rex Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Estimated concentrations in pollen and nectar</H4>
                <div class="out_ container_output">
        """
        t3data = gett3data(beerex_obj)
        t3rows = gethtmlrowsfromcols(t3data,eecheadings)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=eecheadings)))
        html = html + """
                </div>
        """
        return html  


def table_4(beerex_obj):
        html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Dietary risk quotients (RQs) for all bees</H4>
                <div class="out_ container_output">
        """
        t4data = gett4data(beerex_obj)
        t4rows = gethtmlrowsfromcols(t4data, rqsheadings)
        html = html + tmpl.render(Context(dict(data=t4rows, headings=rqsheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

# def table_5(beerex_obj):
#         html = """
#             <H4 class="out_1 collapsible" id="section4"><span></span>Highest RQs</H4>
#                 <div class="out_ container_output">
#         """
#         t5data = gett5data(beerex_obj)
#         t5rows = gethtmlrowsfromcols(t5data, maxrqheadings)
#         html = html + tmpl.render(Context(dict(data=t5rows, headings=maxrqheadings)))
#         html = html + """
#                 </div>
#         </div>
#         """
#         return html