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


# def getheadersum():
#     headings = ["Exposure", "Adults", "Larvae"]
#     return headings
#

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
        "Description": ['Application rate (lb a.i./A)', 'Application method',mark_safe('Log K<sub>oW</sub>'), mark_safe('K<sub>oC</sub>)'), 'Mass of tree vegetation (kg-wet weight)'],
        "Value": [beerex_obj.apprate, beerex_obj.solubility,beerex_obj.ld50_mammal_water,beerex_obj.bodyweight_tested_mammal,beerex_obj.noael_mammal_water,beerex_obj.noael_bodyweight_tested_mammal,beerex_obj.ld50_avian_water,beerex_obj.bodyweight_tested_bird,beerex_obj.mineau_scaling_factor,beerex_obj.noaec_duck,beerex_obj.noaec_quail,beerex_obj.noaec_bird_other_1,beerex_obj.bodyweight_bird_other_1,beerex_obj.noaec_bird_other_2,beerex_obj.bodyweight_bird_other_2],
    }
    return data


def gett2data(beerex_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % beerex_obj.out_dose_mamm, '%g' % beerex_obj.out_at_mamm, '%g' % beerex_obj.out_acute_mamm, '%s' % beerex_obj.out_acuconm,],
        "Chronic": ['%g' % beerex_obj.out_dose_mamm, '%g' % beerex_obj.out_act, '%g' % beerex_obj.out_chron_mamm, '%s' % beerex_obj.out_chronconm,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett2dataqaqc(beerex_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % beerex_obj.out_dose_mamm, '%g' % beerex_obj.out_at_mamm, '%g' % beerex_obj.out_acute_mamm, '%s' % beerex_obj.out_acuconm,],
        "Acute-Expected": ['%g' % beerex_obj.dose_mamm_exp,'%g' % beerex_obj.at_mamm_exp,'%g' % beerex_obj.acute_mamm_exp,'%s' % beerex_obj.acuconm_exp,],
        "Chronic": ['%g' % beerex_obj.out_dose_mamm, '%g' % beerex_obj.out_act, '%g' % beerex_obj.out_chron_mamm, '%s' % beerex_obj.out_chronconm,],
        "Chronic-Expected": ['%g' % beerex_obj.dose_mamm_exp,'%g' % beerex_obj.act_exp,'%g' % beerex_obj.chron_mamm_exp,'%s' % beerex_obj.chronconm_exp,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett3data(beerex_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % beerex_obj.out_dose_bird, '%g' % beerex_obj.out_at_bird,'%g' % beerex_obj.out_acute_bird, '%s' % beerex_obj.out_acuconb,],
        "Chronic": ['%g' % beerex_obj.out_dose_bird, '%g' % beerex_obj.out_det,'%g' % beerex_obj.out_chron_bird, '%s' % beerex_obj.out_chronconb,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett3dataqaqc(beerex_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % beerex_obj.out_dose_bird, '%g' % beerex_obj.out_at_bird,'%g' % beerex_obj.out_acute_bird, '%s' % beerex_obj.out_acuconb,],
        "Acute-Expected": ['%g' % beerex_obj.dose_bird_exp, '%g' % beerex_obj.at_bird_exp, '%g' % beerex_obj.acute_bird_exp, '%s' % beerex_obj.acuconb_exp,],
        "Chronic": ['%g' % beerex_obj.out_dose_bird, '%g' % beerex_obj.out_det,'%g' % beerex_obj.out_chron_bird, '%s' % beerex_obj.out_chronconb,],
        "Chronic-Expected": ['%g' % beerex_obj.dose_bird_exp,'%g' % beerex_obj.det_exp,'%g' % beerex_obj.chron_bird_exp,'%s' % beerex_obj.chronconb_exp,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gettsumdata(bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water):
    data = { 
        "Parameter": ['BW Quail', 'BW Duck', 'BW Bird Other', 'BW Rat', 'BW Mammal Other', 'Avian LD50', 'Mammalian LD50', 
                    'Solubility','AW Bird' , 'Mineau', 'NOAEC','NOAEL'],
        "Mean": ['%g' % numpy.mean(bodyweight_quail),'%g' % numpy.mean(bodyweight_duck),'%g' % numpy.mean(bodyweight_bird_other), '%g' % numpy.mean(bodyweight_rat), 
                 '%g' % numpy.mean(bodyweight_tested_mammal_other), '%g' % numpy.mean(solubility), '%g' % numpy.mean(avian_ld50), '%g' % numpy.mean(mammalian_ld50),
                 '%g' % numpy.mean(mineau_scaling_factor),
                 '%g' % numpy.mean(noael_avian_water), '%g' % numpy.mean(noael_mammal_water),],
        "Std": ['%g' % numpy.std(bodyweight_quail),'%g' % numpy.std(bodyweight_duck),'%g' % numpy.std(bodyweight_bird_other), '%g' % numpy.std(bodyweight_rat), 
                '%g' % numpy.std(bodyweight_tested_mammal_other), '%g' % numpy.std(solubility), '%g' % numpy.std(avian_ld50), '%g' % numpy.std(mammalian_ld50),
                 '%g' % numpy.std(mineau_scaling_factor),
                 '%g' % numpy.std(noael_avian_water),'%g' % numpy.std(noael_mammal_water),],
        "Min": ['%g' % numpy.min(bodyweight_quail),'%g' % numpy.min(bodyweight_duck),'%g' % numpy.min(bodyweight_bird_other), '%g' % numpy.min(bodyweight_rat), 
                '%g' % numpy.min(bodyweight_tested_mammal_other), '%g' % numpy.min(solubility), '%g' % numpy.min(avian_ld50), '%g' % numpy.min(mammalian_ld50),
                 '%g' % numpy.min(mineau_scaling_factor),
                 '%g' % numpy.min(noael_avian_water),'%g' % numpy.min(noael_mammal_water),],
         "Max": ['%g' % numpy.max(bodyweight_quail),'%g' % numpy.max(bodyweight_duck),'%g' % numpy.max(bodyweight_bird_other), '%g' % numpy.max(bodyweight_rat), 
                '%g' % numpy.max(bodyweight_tested_mammal_other), '%g' % numpy.max(solubility), '%g' % numpy.max(avian_ld50), '%g' % numpy.max(mammalian_ld50),
                 '%g' % numpy.max(mineau_scaling_factor),
                 '%g' % numpy.max(noael_avian_water),'%g' % numpy.max(noael_mammal_water),],
        "Unit": ['g', 'g', 'g', 'g', 'g','mg/kg-bw', 'mg/kg-bw', 'mg/L','g', '', 'g','mg/kg-diet', 'mg/kg-bw',],
    }
    return data

def gettsumdata_out(out_dose_bird, out_dose_mamm, out_at_bird, 
                    out_at_mamm, out_det, out_act, out_acute_bird, out_acute_mamm, 
                    out_chron_bird, out_chron_mamm):
    data = {
        "Parameter": ['Upper Bound Exposure - Avian', 'Upper Bound Exposure - Mammalian',
                    'Adjusted Toxicity Value (Acute) - Avian',
                    'Adjusted Toxicity Value (Acute) - Mammalian',
                    'Adjusted Toxicity Value (Chronic) - Avian',
                    'Adjusted Toxicity Value (Chronic) - Mammalian',
                    'Ratio of Exposure to Toxicity (Acute) - Avian',
                    'Ratio of Exposure to Toxicity (Acute) - Mammalian',
                    'Ratio of Exposure to Toxicity (Chronic) - Avian',
                    'Ratio of Exposure to Toxicity (Chronic) - Mammalian',],

        "Mean": [
                 '%g' % numpy.mean(out_dose_bird), '%g' % numpy.mean(out_dose_mamm), '%g' % numpy.mean(out_at_bird),
                 '%g' % numpy.mean(out_at_mamm), '%g' % numpy.mean(out_act), '%g' % numpy.mean(out_det),
                 '%g' % numpy.mean(out_acute_bird), '%g' % numpy.mean(out_acute_mamm),
                 '%g' % numpy.mean(out_chron_bird), '%g' % numpy.mean(out_chron_mamm),],

        "Std": ['%g' % numpy.std(out_dose_bird), '%g' % numpy.std(out_dose_mamm), '%g' % numpy.std(out_at_bird),
                '%g' % numpy.std(out_at_mamm), '%g' % numpy.std(out_act), '%g' % numpy.std(out_det),
                '%g' % numpy.std(out_acute_bird), '%g' % numpy.std(out_acute_mamm),
                '%g' % numpy.std(out_chron_bird), '%g' % numpy.std(out_chron_mamm),],

        "Min": ['%g' % numpy.min(out_dose_bird), '%g' % numpy.min(out_dose_mamm), '%g' % numpy.min(out_at_bird),
                '%g' % numpy.min(out_at_mamm), '%g' % numpy.min(out_act), '%g' % numpy.min(out_det),
                '%g' % numpy.min(out_acute_bird), '%g' % numpy.min(out_acute_mamm),
                '%g' % numpy.min(out_chron_bird), '%g' % numpy.min(out_chron_mamm),],

         "Max": ['%g' % numpy.max(out_dose_bird), '%g' % numpy.min(out_dose_mamm), '%g' % numpy.min(out_at_bird),
                '%g' % numpy.max(out_at_mamm), '%g' % numpy.max(out_act), '%g' % numpy.min(out_det),
                '%g' % numpy.max(out_acute_bird), '%g' % numpy.min(out_acute_mamm),
                '%g' % numpy.max(out_chron_bird), '%g' % numpy.max(out_chron_mamm),],

        "Unit": ['mg/kg-bw', 'mg/kg-bw','mg/kg-bw', 'mg/kg-bw', 'mg/kg-bw', 'mg/kg-bw', '','', '', '',],
    }
    return data


inpheadings = getheaderinp()
toxheadings = getheadertox()
eecheadings = getheadereecs()
rqsheadings = getheaderrqs()
# sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(beerex_obj):
    html_all = table_1(beerex_obj)
    html_all = html_all + table_2(beerex_obj)
    html_all = html_all + table_3(beerex_obj)
    html_all = html_all + table_4(beerex_obj)
    # html_all = html_all + table_5(beerex_obj)
    return html_all

# def table_all_qaqc(beerex_obj):
#     html_all = table_1(beerex_obj)
#     html_all = html_all + table_2_qaqc(beerex_obj)
#     html_all = html_all + table_3_qaqc(beerex_obj)
#     return html_all


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
#         t5rows = gethtmlrowsfromcols(t5data, sumheadings)
#         html = html + tmpl.render(Context(dict(data=t5rows, headings=sumheadings)))
#         html = html + """
#                 </div>
#         </div>
#         """
#         return html


def table_all_sum(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water,
                    out_dose_bird, out_dose_mamm, out_at_bird, 
                    out_at_mamm, out_det, out_act, out_acute_bird, out_acute_mamm, 
                    out_chron_bird, out_chron_mamm):
    html_all_sum = table_sum_input(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water)
    html_all_sum += table_sum_output(sumheadings,tmpl,out_dose_bird,out_dose_mamm,out_at_bird, 
                    out_at_mamm,out_det,out_act,out_acute_bird,out_acute_mamm,out_chron_bird,out_chron_mamm)
    return html_all_sum

def table_sum_input(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Batch Inputs</H4>
                <div class="out_ container_output">
        """
        tsuminputdata = gettsumdata(bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water)
        tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
        html = html + """
                </div>
        """
        return html

def table_sum_output(sumheadings, tmpl, out_dose_bird, out_dose_mamm, out_at_bird, 
                    out_at_mamm, out_det, out_act, out_acute_bird, out_acute_mamm, 
                    out_chron_bird, out_chron_mamm):
        html = """
        <br>
            <H4 class="out_1 collapsible" id="section3"><span></span>beerex Outputs</H4>
                <div class="out_ container_output">
        """
        tsumoutputdata = gettsumdata_out(out_dose_bird, out_dose_mamm, out_at_bird, 
                    out_at_mamm, out_det, out_act, out_acute_bird, out_acute_mamm, 
                    out_chron_bird, out_chron_mamm)
        tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

