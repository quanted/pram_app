"""
.. module:: terrplant_tables
   :synopsis: A useful module indeed.
"""

import numpy
from django.template import Context, Template
from django.utils.safestring import mark_safe
import logging
import time
import datetime

logger = logging.getLogger('TerrplantTables')

def getheaderpv():
    headings = ["Parameter", "Value"]
    return headings

def getheaderpvu():
    headings = ["Parameter", "Value", "Units"]
    return headings

def getheaderde():
    headings = ["Description", "EEC"]
    return headings

def getheaderplantec25noaec():
    headings = ["Plant Type", "ec25", "noaec", "ec25", "noaec"]
    return headings

def getheaderplantecdrysemispray():
    headings = ["Plant Type", "Listed Status", "Dry", "Semi-Aquatic", "Spray Drift"]
    return headings

def getheaderdeqaqc():
    headings = ["Description", "EEC", "Expected"]
    return headings

def getheaderplantecdrysemisprayqaqc():
    headings = ["Plant Type", "Listed Status", "Dry", "Dry-Expected", "Semi-Aquatic", "Semi-Aquatic-Expected", "Spray Drift", "Spray Drift-Expected"]
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

def gett1data(terrplant_obj):
    data = { 
        "Parameter": ['Chemical Name', 'PC Code', 'Use', 'Application Method','Application Form',],
        "Value": [terrplant_obj.chemical_name, terrplant_obj.pc_code, terrplant_obj.use, terrplant_obj.application_method,terrplant_obj.application_form,],
    }
    return data

def gett1dataqaqc(terrplant_obj):
    data = { 
        "Parameter": ['Chemical Name', 'PC Code', 'Use', 'Application Method','Application Form',],
        "Value": [terrplant_obj.chemical_name, terrplant_obj.pc_code, terrplant_obj.use, terrplant_obj.application_method,terrplant_obj.application_form,],
    }
    return data

def gett2data(terrplant_obj):
    data = { 
        "Parameter": ['Incorporation', 'Application Rate', 'Drift Fraction', 'Runoff Fraction',],
        "Value": [terrplant_obj.incorporation_depth, terrplant_obj.application_rate, terrplant_obj.drift_fraction, terrplant_obj.runoff_fraction,],
        "Units": ['in', 'lbs ai/A', '','', ],
    }
    return data

def gett3data(terrplant_obj):
    data = { 
        "Description": ['Runoff to Dry Areas', 'Runoff to Semi-Aquatic Areas', 'Spray Drift','Total to Dry Areas', 'Total to Semi-Aquatic Areas',],
        "EEC": ['%g' % terrplant_obj.out_run_dry,'%g' % terrplant_obj.out_run_semi,'%g' % terrplant_obj.out_spray,
                '%g' % terrplant_obj.out_total_dry,'%g' % terrplant_obj.out_total_semi, ],
    }
    return data

def gett3dataqaqc(terrplant_obj):
    data = { 
        "Description": ['Runoff to Dry Areas', 'Runoff to Semi-Aquatic Areas', 'Spray Drift','Total to Dry Areas', 'Total to Semi-Aquatic Areas',],
        "EEC": ['%g' % terrplant_obj.exp_run_dry,'%g' % terrplant_obj.exp_run_semi,'%g' % terrplant_obj.exp_spray,
                '%g' % terrplant_obj.exp_total_dry,'%g' % terrplant_obj.exp_total_semi, ],
    }
    return data

def gett4data(terrplant_obj):
    data = { 
        "Plant Type": ['Monocot', 'Dicot',],
        "ec25": [terrplant_obj.ec25_nonlisted_seedling_emergence_monocot,terrplant_obj.noaec_listed_seedling_emergence_monocot,],
        "noaec": [terrplant_obj.ec25_nonlisted_seedling_emergence_dicot,terrplant_obj.noaec_listed_seedling_emergence_dicot,],
        "ec25": [terrplant_obj.ec25_nonlisted_vegetative_vigor_monocot,terrplant_obj.noaec_listed_vegetative_vigor_monocot,],
        "noaec":[terrplant_obj.ec25_nonlisted_vegetative_vigor_dicot,terrplant_obj.noaec_listed_vegetative_vigor_dicot,],
    }
    return data

def gett4dataqaqc(terrplant_obj):
    data = { 
        "Plant Type": ['Monocot', 'Dicot',],
        "ec25": [terrplant_obj.ec25_nonlisted_seedling_emergence_monocot,terrplant_obj.noaec_listed_seedling_emergence_monocot,],
        "noaec": [terrplant_obj.ec25_nonlisted_seedling_emergence_dicot,terrplant_obj.noaec_listed_seedling_emergence_dicot,],
        "ec25": [terrplant_obj.ec25_nonlisted_vegetative_vigor_monocot,terrplant_obj.noaec_listed_vegetative_vigor_monocot,],
        "noaec":[terrplant_obj.ec25_nonlisted_vegetative_vigor_dicot,terrplant_obj.noaec_listed_vegetative_vigor_dicot,],
    }
    return data

def gett5data(terrplant_obj):
    data = { 
        "Plant Type": ['Monocot', 'Monocot', 'Dicot', 'Dicot',],
        "Listed Status": ['non-listed','listed','non-listed','listed',],
        "Dry": ['%g' % terrplant_obj.out_nms_rq_dry,'%g' % terrplant_obj.out_lms_rq_dry,'%g' % terrplant_obj.out_nds_rq_dry,'%g' % terrplant_obj.out_lds_rq_dry,],
        "Semi-Aquatic": ['%g' % terrplant_obj.out_nms_rq_semi,'%g' % terrplant_obj.out_lms_rq_semi,'%g' % terrplant_obj.out_nds_rq_semi,'%g' % terrplant_obj.out_lds_rq_semi,],
        "Spray Drift":['%g' % terrplant_obj.out_nms_rq_spray,'%g' % terrplant_obj.out_lms_rq_spray,'%g' % terrplant_obj.out_nds_rq_spray,'%g' % terrplant_obj.out_lds_rq_spray,],
    }
    return data


def gett5dataqaqc(terrplant_obj):
    data = { 
        "Plant Type": ['Monocot', 'Monocot', 'Dicot', 'Dicot',],
        "Listed Status": ['non-listed','listed','non-listed','listed',],
        "Dry": ['%g' % terrplant_obj.out_nms_rq_dry,'%g' % terrplant_obj.out_lms_rq_dry,'%g' % terrplant_obj.out_nds_rq_dry,'%g' % terrplant_obj.out_lds_rq_dry,],
        "Dry-Expected": ['%g' % terrplant_obj.exp_nms_rq_dry,'%g' % terrplant_obj.exp_lms_rq_dry,'%g' % terrplant_obj.exp_nds_rq_dry,'%g' % terrplant_obj.exp_lds_rq_dry,],
        "Semi-Aquatic": ['%g' % terrplant_obj.out_nms_rq_semi,'%g' % terrplant_obj.out_lms_rq_semi,'%g' % terrplant_obj.out_nds_rq_semi,'%g' % terrplant_obj.out_lds_rq_semi,],
        "Semi-Aquatic-Expected": ['%g' % terrplant_obj.exp_nms_rq_semi,'%g' % terrplant_obj.exp_lms_rq_semi,'%g' % terrplant_obj.exp_nds_rq_semi,'%g' % terrplant_obj.exp_lds_rq_semi,],
        "Spray Drift":['%g' % terrplant_obj.out_nms_rq_spray,'%g' % terrplant_obj.out_lms_rq_spray,'%g' % terrplant_obj.out_nds_rq_spray,'%g' % terrplant_obj.out_lds_rq_spray,],
        "Spray Drift-Expected":['%g' % terrplant_obj.exp_nms_rq_spray,'%g' % terrplant_obj.exp_lms_rq_spray,'%g' % terrplant_obj.exp_nds_rq_spray,'%g' % terrplant_obj.exp_lds_rq_spray,],
    }
    return data

def gettsumdata(application_rate, incorporation_depth, runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot):
    data = { 
        "Parameter": ['Incorporation', 'Application Rate', 'Drift Fraction', 'Runoff Fraction', 
                    'Noaec for listed seedling emergence monocot','Ec25 for nonlisted seedling emergence monocot',
                    'Noaec for listed seedling emergence dicot','Noaec for listed seedling emergence dicot'],
        "Mean": ['%.2e' % numpy.mean(application_rate),'%.2e' % numpy.mean(incorporation_depth),'%.2e' % numpy.mean(runoff_fraction), '%.2e' % numpy.mean(drift_fraction), 
                 '%.2e' % numpy.mean(ec25_nonlisted_seedling_emergence_monocot), '%.2e' % numpy.mean(ec25_nonlisted_seedling_emergence_dicot), '%.2e' % numpy.mean(noaec_listed_seedling_emergence_monocot), '%.2e' % numpy.mean(noaec_listed_seedling_emergence_dicot),],
        "Std": ['%.2e' % numpy.std(application_rate),'%.2e' % numpy.std(incorporation_depth),'%.2e' % numpy.std(runoff_fraction), '%.2e' % numpy.std(drift_fraction), 
                '%.2e' % numpy.std(ec25_nonlisted_seedling_emergence_monocot), '%.2e' % numpy.std(ec25_nonlisted_seedling_emergence_dicot), '%.2e' % numpy.std(noaec_listed_seedling_emergence_monocot), '%.2e' % numpy.std(noaec_listed_seedling_emergence_dicot),],
        "Min": ['%.2e' % numpy.min(application_rate),'%.2e' % numpy.min(incorporation_depth),'%.2e' % numpy.min(runoff_fraction), '%.2e' % numpy.min(drift_fraction), 
                '%.2e' % numpy.min(ec25_nonlisted_seedling_emergence_monocot), '%.2e' % numpy.min(ec25_nonlisted_seedling_emergence_dicot), '%.2e' % numpy.min(noaec_listed_seedling_emergence_monocot), '%.2e' % numpy.min(noaec_listed_seedling_emergence_dicot),],
         "Max": ['%.2e' % numpy.max(application_rate),'%.2e' % numpy.max(incorporation_depth),'%.2e' % numpy.max(runoff_fraction), '%.2e' % numpy.max(drift_fraction), 
                '%.2e' % numpy.max(ec25_nonlisted_seedling_emergence_monocot), '%.2e' % numpy.max(ec25_nonlisted_seedling_emergence_dicot), '%.2e' % numpy.max(noaec_listed_seedling_emergence_monocot), '%.2e' % numpy.max(noaec_listed_seedling_emergence_dicot),],
        "Unit": ['', '', '', '', '','', '', '',],
    }
    return data

def gettsumdata_out(run_dry_out, run_semi_out, spray_out, total_dry_out, total_semi_out,
                    nms_rq_dry_out, nms_rq_semi_out, nms_rq_spray_out, 
                    lms_rq_dry_out, lms_rq_semi_out, lms_rq_spray_out, 
                    nds_rq_dry_out, nds_rq_semi_out, nds_rq_spray_out, 
                    lds_rq_dry_out, lds_rq_semi_out, lds_rq_spray_out):
    data = { 
        "Parameter": ['Runoff to Dry Areas', 'Runoff to Semi-Aquatic Areas', 'Spray Drift',
                    'Total to Dry Areas', 'Total to Semi-Aquatic Areas',
                    'Risk Quotient for non-listed monocot seedlings exposed to pesticide X in a dry area',
                    'Risk Quotient for non-listed monocot seedlings exposed to Pesticide X in a semi-aquatic area',
                    'Risk Quotient for non-listed monocot seedlings exposed to Pesticide X via spray drift',
                    'Risk Quotient for listed monocot seedlings exposed to Pesticide X in a dry areas',
                    'Risk Quotient for listed monocot seedlings exposed to Pesticide X in a semi-aquatic area',
                    'Risk Quotient for listed monocot seedlings exposed to Pesticide X via spray drift',
                    'Risk Quotient for non-listed dicot seedlings exposed to Pesticide X in dry areas',
                    'Risk Quotient for non-listed dicot seedlings exposed to Pesticide X in semi-aquatic areas',
                    'Risk Quotient for non-listed dicot seedlings exposed to Pesticide X in dry areas',
                    'Risk Quotient for listed dicot seedlings exposed to Pesticide X in dry areas',
                    'Risk Quotient for listed dicot seedlings exposed to Pesticide X in semi-aquatic areas',
                    'Risk Quotient for listed dicot seedlings exposed to Pesticide X via spray drift',],

        "Mean": [
                 '%.2e' % numpy.mean(run_dry_out), '%.2e' % numpy.mean(run_semi_out), '%.2e' % numpy.mean(spray_out), '%.2e' % numpy.mean(total_dry_out), '%.2e' % numpy.mean(total_dry_out),
                 '%.2e' % numpy.mean(nms_rq_dry_out), '%.2e' % numpy.mean(nms_rq_semi_out), '%.2e' % numpy.mean(nms_rq_spray_out),
                 '%.2e' % numpy.mean(lms_rq_dry_out), '%.2e' % numpy.mean(lms_rq_semi_out), '%.2e' % numpy.mean(lms_rq_spray_out),
                 '%.2e' % numpy.mean(nds_rq_dry_out), '%.2e' % numpy.mean(nds_rq_semi_out), '%.2e' % numpy.mean(nds_rq_spray_out),
                 '%.2e' % numpy.mean(lds_rq_dry_out), '%.2e' % numpy.mean(lds_rq_semi_out), '%.2e' % numpy.mean(lds_rq_spray_out),],

        "Std": ['%.2e' % numpy.std(run_dry_out), '%.2e' % numpy.std(run_semi_out), '%.2e' % numpy.std(spray_out), '%.2e' % numpy.std(total_dry_out), '%.2e' % numpy.std(total_dry_out),
                '%.2e' % numpy.std(nms_rq_dry_out), '%.2e' % numpy.std(nms_rq_semi_out), '%.2e' % numpy.std(nms_rq_spray_out),
                '%.2e' % numpy.std(lms_rq_dry_out), '%.2e' % numpy.std(lms_rq_semi_out), '%.2e' % numpy.std(lms_rq_spray_out),
                '%.2e' % numpy.std(nds_rq_dry_out), '%.2e' % numpy.std(nds_rq_semi_out), '%.2e' % numpy.std(nds_rq_spray_out),
                '%.2e' % numpy.std(lds_rq_dry_out), '%.2e' % numpy.std(lds_rq_semi_out), '%.2e' % numpy.std(lds_rq_spray_out),],

        "Min": ['%.2e' % numpy.min(run_dry_out), '%.2e' % numpy.min(run_semi_out), '%.2e' % numpy.min(spray_out), '%.2e' % numpy.min(total_dry_out), '%.2e' % numpy.min(total_dry_out),
                '%.2e' % numpy.min(nms_rq_dry_out), '%.2e' % numpy.min(nms_rq_semi_out), '%.2e' % numpy.min(nms_rq_spray_out),
                '%.2e' % numpy.min(lms_rq_dry_out), '%.2e' % numpy.min(lms_rq_semi_out), '%.2e' % numpy.min(lms_rq_spray_out),
                '%.2e' % numpy.min(nds_rq_dry_out), '%.2e' % numpy.min(nds_rq_semi_out), '%.2e' % numpy.min(nds_rq_spray_out),
                '%.2e' % numpy.min(lds_rq_dry_out), '%.2e' % numpy.min(lds_rq_semi_out), '%.2e' % numpy.min(lds_rq_spray_out),],

         "Max": ['%.2e' % numpy.max(run_dry_out), '%.2e' % numpy.max(run_semi_out), '%.2e' % numpy.max(spray_out), '%.2e' % numpy.min(total_dry_out), '%.2e' % numpy.min(total_dry_out),
                '%.2e' % numpy.max(nms_rq_dry_out), '%.2e' % numpy.max(nms_rq_semi_out), '%.2e' % numpy.min(nms_rq_spray_out),
                '%.2e' % numpy.max(lms_rq_dry_out), '%.2e' % numpy.max(lms_rq_semi_out), '%.2e' % numpy.min(lms_rq_spray_out),
                '%.2e' % numpy.max(nds_rq_dry_out), '%.2e' % numpy.max(nds_rq_semi_out), '%.2e' % numpy.min(nds_rq_spray_out),
                '%.2e' % numpy.max(lds_rq_dry_out), '%.2e' % numpy.max(lds_rq_semi_out), '%.2e' % numpy.min(lds_rq_spray_out),],

        "Unit": ['', '','', '', '', '', '','', '', '', '', '','', '', '', '', '',],
    }
    return data

pvheadings = getheaderpv()
pvuheadings = getheaderpvu()
deheadings = getheaderde()
deheadingsqaqc = getheaderdeqaqc()
plantec25noaecheadings = getheaderplantec25noaec()
plantecdrysemisprayheadings = getheaderplantecdrysemispray()
plantecdrysemisprayheadingsqaqc = getheaderplantecdrysemisprayqaqc()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_all(terrplant_obj):
    html_all = table_1(terrplant_obj)
    html_all = html_all + table_2(terrplant_obj)
    html_all = html_all + table_3(terrplant_obj)
    html_all = html_all + table_4(terrplant_obj)
    html_all = html_all + table_5(terrplant_obj)
    return html_all

def table_all_qaqc(terrplant_obj):
    html_all = table_1_qaqc(terrplant_obj)
    html_all = html_all + table_2(terrplant_obj)
    html_all = html_all + table_3_qaqc(terrplant_obj)
    html_all = html_all + table_4_qaqc(terrplant_obj)
    html_all = html_all + table_5_qaqc(terrplant_obj)
    return html_all

def table_all_sum(sumheadings, tmpl, application_rate, incorporation_depth, runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot, 
                    run_dry_out, run_semi_out, spray_out, total_dry_out, total_semi_out,
                    nms_rq_dry_out, nms_rq_semi_out, nms_rq_spray_out, 
                    lms_rq_dry_out, lms_rq_semi_out, lms_rq_spray_out, 
                    nds_rq_dry_out, nds_rq_semi_out, nds_rq_spray_out, 
                    lds_rq_dry_out, lds_rq_semi_out, lds_rq_spray_out):
    html_all_sum = table_sum_input(sumheadings, tmpl, application_rate, incorporation_depth, runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot)
    html_all_sum += table_sum_output(sumheadings, tmpl, run_dry_out, run_semi_out, spray_out, total_dry_out, total_semi_out,
                    nms_rq_dry_out, nms_rq_semi_out, nms_rq_spray_out, 
                    lms_rq_dry_out, lms_rq_semi_out, lms_rq_spray_out, 
                    nds_rq_dry_out, nds_rq_semi_out, nds_rq_spray_out, 
                    lds_rq_dry_out, lds_rq_semi_out, lds_rq_spray_out)
    return html_all_sum

def table_sum_input(sumheadings, tmpl, application_rate, incorporation_depth, runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot):
        #pre-table sum_input
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Batch Inputs</H4>
                <div class="out_ container_output">
        """
        #table sum_input
        tsuminputdata = gettsumdata(application_rate, incorporation_depth, runoff_fraction, drift_fraction, ec25_nonlisted_seedling_emergence_monocot, ec25_nonlisted_seedling_emergence_dicot, noaec_listed_seedling_emergence_monocot, noaec_listed_seedling_emergence_dicot)
        tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
        html = html + """
                </div>
        """
        return html

def table_sum_output(sumheadings, tmpl, run_dry_out, run_semi_out, spray_out, total_dry_out, total_semi_out,
                    nms_rq_dry_out, nms_rq_semi_out, nms_rq_spray_out, 
                    lms_rq_dry_out, lms_rq_semi_out, lms_rq_spray_out, 
                    nds_rq_dry_out, nds_rq_semi_out, nds_rq_spray_out, 
                    lds_rq_dry_out, lds_rq_semi_out, lds_rq_spray_out):

        #pre-table sum_input
        html = """
        <br>
            <H4 class="out_1 collapsible" id="section3"><span></span>Rice Model Outputs</H4>
                <div class="out_ container_output">
        """
        #table sum_input
        tsumoutputdata = gettsumdata_out(run_dry_out, run_semi_out, spray_out, total_dry_out, total_semi_out,
                    nms_rq_dry_out, nms_rq_semi_out, nms_rq_spray_out, 
                    lms_rq_dry_out, lms_rq_semi_out, lms_rq_spray_out, 
                    nds_rq_dry_out, nds_rq_semi_out, nds_rq_spray_out, 
                    lds_rq_dry_out, lds_rq_semi_out, lds_rq_spray_out)
        tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings)))
        html = html + """
                </div>
        </div>
        <br>
        """
        return html

def timestamp(terrplant_obj="", batch_jid=""):
    if terrplant_obj:
        st = datetime.datetime.strptime(terrplant_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
    <b>TerrPlant <a href="http://www.epa.gov/oppefed1/models/terrestrial/terrplant/terrplant_user_guide.html">Version 1.2.2</a> (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def table_1(terrplant_obj):
        #pre-table 1
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Chemical Identity</H4>
                <div class="out_ container_output">
        """
        #table 1
        t1data = gett1data(terrplant_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvheadings)))
        html = html + """
                </div>
        """
        return html

def table_1_qaqc(terrplant_obj):
        #pre-table 1
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Chemical Identity</H4>
                <div class="out_ container_output">
        """
        #table 1
        t1data = gett1dataqaqc(terrplant_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvheadings)))
        html = html + """
                </div>
        """
        return html

def table_2(terrplant_obj):
        # #pre-table 2
        html = """
            <H4 class="out_2 collapsible" id="section3"><span></span>Input parameters used to derive EECs</H4>
                <div class="out_ container_output">
        """
        #table 2
        t2data = gett2data(terrplant_obj)
        t2rows = gethtmlrowsfromcols(t2data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_3(terrplant_obj):
        #pre-table 3
        html = """
        <br>
        <H3 class="out_3 collapsible" id="section4"><span></span>Exposure Estimates</H3>
        <div class="out_">
            <H4 class="out_3 collapsible" id="section5"><span></span>EECs for %s</H4>
                <div class="out_ container_output">
        """%(terrplant_obj.chemical_name)
        #table 3
        t3data = gett3data(terrplant_obj)
        t3rows = gethtmlrowsfromcols(t3data,deheadings)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=deheadings)))
        html = html + """
                </div>
        """
        return html


def table_3_qaqc(terrplant_obj):
        #pre-table 3
        html = """
        <br>
        <H3 class="out_3 collapsible" id="section4"><span></span>Exposure Estimates</H3>
        <div class="out_">
            <H4 class="out_3 collapsible" id="section5"><span></span>EECs for %s</H4>
                <div class="out_ container_output">
        """%(terrplant_obj.chemical_name)
        #table 3
        t3data = gett3dataqaqc(terrplant_obj)
        t3rows = gethtmlrowsfromcols(t3data,deheadings)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=deheadings)))
        html = html + """
                </div>
        """
        return html

def table_4(terrplant_obj):
        #pre-table 4
        html = """     
            <H4 class="out_4 collapsible" id="section6"><span></span>Plant survival and growth data used for _rq_ derivation</H4>
                <div class="out_ container_output">
        """
        #table 4
        t4data = gett4data(terrplant_obj)
        t4rows = gethtmlrowsfromcols(t4data,plantec25noaecheadings)
        html = html + tmpl.render(Context(dict(data=t4rows, headings=plantec25noaecheadings)))
        html = html + """
                </div>
        """
        return html

def table_4_qaqc(terrplant_obj):
        #pre-table 4
        html = """     
            <H4 class="out_4 collapsible" id="section6"><span></span>Plant survival and growth data used for _rq_ derivation</H4>
                <div class="out_ container_output">
        """
        #table 4
        t4data = gett4dataqaqc(terrplant_obj)
        t4rows = gethtmlrowsfromcols(t4data,plantec25noaecheadings)
        html = html + tmpl.render(Context(dict(data=t4rows, headings=plantec25noaecheadings)))
        html = html + """
                </div>
        """
        return html

def table_5(terrplant_obj):
        #pre-table 5
        html = """         
            <H4 class="out_5 collapsible" id="section7"><span></span>_rq_ values for plants in dry and semi-aquatic areas exposed to %s through runoff and/or spray drift*</H4>
                <div class="out_ container_output">
        """%(terrplant_obj.chemical_name)
        #table 5
        t5data = gett5data(terrplant_obj)
        t5rows = gethtmlrowsfromcols(t5data,plantecdrysemisprayheadings)
        html = html + tmpl.render(Context(dict(data=t5rows, headings=plantecdrysemisprayheadings)))
        html = html + """
                <H4>*If _rq_ > 1.0, the LOC is exceeded, resulting in potential for risk to that plant group</H4>
                </div>
        </div>
        """
        return html

def table_5_qaqc(terrplant_obj):
        #pre-table 5
        html = """         
            <H4 class="out_5 collapsible" id="section7"><span></span>_rq_ values for plants in dry and semi-aquatic areas exposed to %s through runoff and/or spray drift*</H4>
                <div class="out_ container_output">
        """%(terrplant_obj.chemical_name)
        #table 5
        t5data = gett5dataqaqc(terrplant_obj)
        t5rows = gethtmlrowsfromcols(t5data,plantecdrysemisprayheadingsqaqc)
        html = html + tmpl.render(Context(dict(data=t5rows, headings=plantecdrysemisprayheadingsqaqc)))
        html = html + """
                <H4>*If _rq_ > 1.0, the LOC is exceeded, resulting in potential for risk to that plant group</H4>
                </div>
        </div>
        """
        return html
