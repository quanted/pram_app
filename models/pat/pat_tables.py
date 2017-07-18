"""
.. module:: pat_tables
   :synopsis: A useful module indeed.
"""

import datetime
import logging
import os

import numpy
from django.template import Context, Template
from django.utils.safestring import mark_safe

logger = logging.getLogger("patTables")

def timestamp(pat_obj="", batch_jid=""):
    if pat_obj:
        st = datetime.datetime.strptime(pat_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')

    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>Pat Fugacity Modeling<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def getheaderpvu():
    headings = ["Parameter", "Value", "Units"]
    return headings    

def getheadersum():
    headings = ["Parameter", "Mean", "Std", "Min", "Max", "Units"]
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

def patoutput(pat_obj):
    data = { 
        "Parameter": ['Chemical concentration in pat tissue',],
        "Value": ['{0:.5e}'.format(pat_obj.out_pat_fugacity),],
        
        "Units": ['g/kg',],
    }
    return data


def gettsumdata(Kow, L, Cs, Kd, Ps):
    data = { 
        "Parameter": [mark_safe('Octanol to water partition coefficient K<sub>OW</sub>'), 'Lipid fraction of pat L', mark_safe('Chemical concentration in soil C<sub>S</sub>'), mark_safe('Soil partitioning coefficient K<sub>d</sub>'),
                    mark_safe('Bulk density of soil &#961;<sub>s</sub>'),mark_safe('Chemical concentration in pore water of soil C<sub>W</sub>'),
                    mark_safe('Molecular weight of chemical MW'),mark_safe('Density of pat &#961;<sub>E</sub>')],
        "Mean": ['{0:.2e}'.format(numpy.mean(Kow)),'{0:.2e}'.format(numpy.mean(L)),'{0:.2e}'.format(numpy.mean(Cs)), '{0:.2e}'.format(numpy.mean(Kd)), 
                 '{0:.2e}'.format(numpy.mean(Ps)),], # '%.2e' % numpy.mean(Cw), '%.2e' % numpy.mean(MW), '%.2e' % numpy.mean(Pe),],
        "Std":  ['{0:.2e}'.format(numpy.std(Kow)),'{0:.2e}'.format(numpy.std(L)),'{0:.2e}'.format(numpy.std(Cs)), '{0:.2e}'.format(numpy.std(Kd)), 
                '{0:.2e}'.format(numpy.std(Ps)),], # '%.2e' % numpy.std(Cw), '%.2e' % numpy.std(MW), '%.2e' % numpy.std(Pe),],
        "Min":  ['{0:.2e}'.format(numpy.min(Kow)),'{0:.2e}'.format(numpy.min(L)),'{0:.2e}'.format(numpy.min(Cs)), '{0:.2e}'.format(numpy.min(Kd)), 
                '{0:.2e}'.format(numpy.min(Ps)),], # '%.2e' % numpy.min(Cw), '%.2e' % numpy.min(MW), '%.2e' % numpy.min(Pe),],
        "Max":  ['{0:.2e}'.format(numpy.max(Kow)),'{0:.2e}'.format(numpy.max(L)),'{0:.2e}'.format(numpy.max(Cs)), '{0:.2e}'.format(numpy.max(Kd)), 
                '{0:.2e}'.format(numpy.max(Ps)),], # '%.2e' % numpy.max(Cw), '%.2e' % numpy.max(MW), '%.2e' % numpy.max(Pe),],
        "Units": ['none', 'none', mark_safe('mol/m<sup>3</sup>'),mark_safe('cm<sup>3</sup>/g'),mark_safe('g/cm<sup>3</sup>'),mark_safe('mol/m<sup>3</sup>'),'g/mol',mark_safe('kg/m<sup>3</sup>'),],
    }
    return data


def gettsumdata_out(Ce_out):
    data = { 
        "Parameter": ['Chemical concentration in pat tissue',],
        "Mean":['{0:.2e}'.format(numpy.mean(Ce_out)),],
        "Std":['{0:.2e}'.format(numpy.std(Ce_out)),],
        "Min":['{0:.2e}'.format(numpy.min(Ce_out)),],
        "Max":['{0:.2e}'.format(numpy.max(Ce_out)),],
        "Units": ['g/kg',],
    }
    return data


pvuheadings = getheaderpvu()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(pat_obj):
    table1_out = table_1batch(pvuheadings, tmpl, pat_obj)
    table2_out = table_2(pat_obj)
    templatepath = os.path.dirname(__file__) + '/../templates/'
    html_all = table1_out + table2_out 
    return html_all

def table_2(pat_obj):
        html = """
            <H4 class="out_4 collapsible" id="section2"><span></span>Pat Fugacity Modeling Output</H4>
                <div class="out_ container_output">
        """
        t2data = patoutput(pat_obj)
        t2rows = gethtmlrowsfromcols(t2data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_1batch(pvuheadings, tmpl, pat_obj):
        #pre-table 1
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Input</H4>
                <div class="out_ container_output">
        """
        #table 1
        t1data = getdata_batch(pat_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
        html = html + """
                </div>
        """
        return html

def getdata_batch(pat_obj):
    data = { 
        "Parameter": [mark_safe('Octanol to water partition coefficient K<sub>OW</sub>'), 'Lipid fraction of pat L', mark_safe('Chemical concentration in soil C<sub>S</sub>'), mark_safe('Soil partitioning coefficient K<sub>d</sub>'),
                    mark_safe('Bulk density of soil &#961;<sub>s</sub>')],
               # ,mark_safe('Chemical concentration in pore water of soil C<sub>W</sub>'),
               #     mark_safe('Molecular weight of chemical MW'),mark_safe('Density of pat &#961;<sub>E</sub>')],
        "Value": [pat_obj.k_ow, pat_obj.l_f_e, pat_obj.c_s, pat_obj.k_d, pat_obj.p_s], # pat_obj.c_w, pat_obj.m_w, pat_obj.p_e],
        "Units": ['none', 'none', mark_safe('mol/m<sup>3</sup>'),mark_safe('cm<sup>3</sup>/g'),mark_safe('g/cm<sup>3</sup>'),], # mark_safe('mol/m<sup>3</sup>'),'g/mol',mark_safe('kg/m<sup>3</sup>'),],
    }
    return data

def table_all_batch(pvuheadings, sumheadings, tmpl,pat_obj):
    html_all = table_1batch(pvuheadings, tmpl, pat_obj)
    html_all = html_all + table_2(pat_obj)
    return html_all

def table_all_sum(sumheadings, tmpl, Kow, L, Cs, Kd, Ps, Ce_out):
    html_all_sum = table_sum_input(sumheadings, tmpl, Kow, L, Cs, Kd, Ps) # Cw, MW, Pe)
    html_all_sum += table_sum_output(sumheadings, tmpl, Ce_out)
    return html_all_sum

def table_sum_input(sumheadings, tmpl, Kow, L, Cs, Kd, Ps): # Cw, MW, Pe):
        #pre-table sum_input
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Batch Inputs</H4>
                <div class="out_ container_output">
        """
        #table sum_input
        tsuminputdata = gettsumdata(Kow, L, Cs, Kd, Ps) # Cw, MW, Pe)
        tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
        html = html + """</div>"""
        return html

def table_sum_output(sumheadings, tmpl, Ce_out):
        #pre-table sum_input
        html = """
        <br>
            <H4 class="out_1 collapsible" id="section3"><span></span>Pat Fagacity Model Batch Outputs</H4>
                <div class="out_ container_output">
        """
        #table sum_input
        tsumoutputdata = gettsumdata_out(Ce_out)
        tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings)))
        html = html + """
                </div>
                </div>
                <br>
                """
        return html

