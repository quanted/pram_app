"""
.. module:: rice_tables
   :synopsis: A useful module indeed.
"""

import numpy
from django.template import Context, Template
from django.utils.safestring import mark_safe
import rice_model,rice_parameters
import logging
import time
import datetime

logger = logging.getLogger("RiceTables")

def getheaderpvu():
	headings = ["Parameter", "Value", "Units"]
	return headings

def getheaderpvu_calculated():
    headings = ["Parameter", "Calculated-Value", "Units"]
    return headings

def getheaderpvuqaqc():
    headings = ["Parameter", "Calculated-Value", "Expected-Value", "Units"]
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

def gett1data(rice_obj):
    data = { 
        "Parameter": ['Chemical Name','Mass applied to patty','Area of patty','Sediment Depth',
            mark_safe('Sediment bulk density, &#961;<sub>b</sub>'),'Water column depth',
            mark_safe('Sediment porosity, K<sub>d</sub>'), 
            mark_safe('Water-Sediment partitioning coefficient, K<sub>d</sub>')],
        "Value": ['{0!s}'.format(rice_obj.chemical_name), '{0:.4f}'.format(rice_obj.mai), '{0:.2f}'.format(rice_obj.area), 
            '{0:.2f}'.format(rice_obj.dsed), '{0:.2f}'.format(rice_obj.pb), '{0:.2f}'.format(rice_obj.dw), 
            '{0:.4f}'.format(rice_obj.osed), '{0:.2f}'.format(rice_obj.kd)],
        "Units": ['','kg',mark_safe('m<sup>2</sup>'),'m',mark_safe('kg/m<sup>3</sup>'),'m','','L/kg'],
    }
    return data

def gett1dataqaqc(rice_obj):
    data = { 
        "Parameter": ['Chemical Name','Mass applied to patty','Area of patty','Sediment Depth',mark_safe('Sediment bulk density, &#961;<sub>b</sub>'),'Water column depth',mark_safe('Sediment porosity, K<sub>d</sub>'), mark_safe('Water-Sediment partitioning coefficient, K<sub>d</sub>')],
        "Calculated-Value": [rice_obj.chemical_name,rice_obj.mai,rice_obj.area,rice_obj.dsed,rice_obj.pb,rice_obj.dw,rice_obj.osed,rice_obj.kd],
        "Expected-Value": [rice_obj.chemical_name,rice_obj.mai,rice_obj.area,rice_obj.dsed,rice_obj.pb,rice_obj.dw,rice_obj.osed,rice_obj.kd],
        "Units": ['','kg',mark_safe('m<sup>2</sup>'),'m',mark_safe('kg/m<sup>3</sup>'),'m','','L/kg'],
    }
    return data

def gett2data(rice_obj):
    data = { 
        "Parameter": ['Sediment Mass', 'Water Column Volume', 'Mass per unit area', 'Water Concentration',],
        "Calculated-Value": ['{0:.2f}'.format(rice_obj.out_msed), '{0:.2f}'.format(rice_obj.out_vw), '{0:.4f}'.format(rice_obj.out_mass_area), '{0:.4f}'.format(rice_obj.out_cw),],
        "Units": ['kg', mark_safe('m<sup>3</sup>'), 'kg/ha', mark_safe('&#956;g/L'),],
    }
    return data

def gett2dataqaqc(rice_obj):
    data = { 
        "Parameter": ['Sediment Mass', 'Water Column Volume', 'Mass per unit area', 'Water Concentration',],
        "Calculated-Value": ['{0:.2f}'.format(rice_obj.out_msed), '{0:.2f}'.format(rice_obj.out_vw), '{0:.4f}'.format(rice_obj.out_mass_area), '{0:.4f}'.format(rice_obj.out_cw),],
        "Expected-Value": ['{0:.2f}'.format(rice_obj.exp_msed), '{0:.2f}'.format(rice_obj.exp_vw), '{0:.4f}'.format(rice_obj.exp_mass_area), '{0:.4f}'.format(rice_obj.exp_cw),],
        "Units": ['kg', mark_safe('m<sup>3</sup>'), 'kg/ha', mark_safe('&#956;g/L'),],
    }
    return data

def gettsumdata(mai, dsed, a, pb, dw, osed, kd):
    data = {
        "Parameter": ['Mass applied to patty','Area of patty','Sediment Depth',mark_safe('Sediment bulk density, &#961;<sub>b</sub>'),'Water column depth',mark_safe('Sediment porosity, K<sub>d</sub>'), mark_safe('Water-Sediment partitioning coefficient, K<sub>d</sub>')],
        "Mean": ['{0:.2e}'.format(numpy.mean(mai)),'{0:.2e}'.format(numpy.mean(dsed)),'{0:.2e}'.format(numpy.mean(a)), '{0:.2e}'.format(numpy.mean(pb)), 
                 '{0:.2e}'.format(numpy.mean(dw)), '{0:.2e}'.format(numpy.mean(osed)), '{0:.2e}'.format(numpy.mean(kd))],
        "Std": ['{0:.2e}'.format(numpy.std(mai)),'{0:.2e}'.format(numpy.std(dsed)),'{0:.2e}'.format(numpy.std(a)), '{0:.2e}'.format(numpy.std(pb)), 
                '{0:.2e}'.format(numpy.std(dw)), '{0:.2e}'.format(numpy.std(osed)), '{0:.2e}'.format(numpy.std(kd))],
        "Min": ['{0:.2e}'.format(numpy.min(mai)),'{0:.2e}'.format(numpy.min(dsed)),'{0:.2e}'.format(numpy.min(a)), '{0:.2e}'.format(numpy.min(pb)), 
                '{0:.2e}'.format(numpy.min(dw)), '{0:.2e}'.format(numpy.min(osed)), '{0:.2e}'.format(numpy.min(kd))],
         "Max": ['{0:.2e}'.format(numpy.max(mai)),'{0:.2e}'.format(numpy.max(dsed)),'{0:.2e}'.format(numpy.max(a)), '{0:.2e}'.format(numpy.max(pb)), 
                '{0:.2e}'.format(numpy.max(dw)), '{0:.2e}'.format(numpy.max(osed)), '{0:.2e}'.format(numpy.max(kd))],
        "Unit": ['kg',mark_safe('m<sup>2</sup>'),'m',mark_safe('kg/m<sup>3</sup>'),'m','','L/kg'],
    }
    return data

def gettsumdata_out(msed, vw, mass_area, cw):
    data = {
        "Parameter": ['Sediment Mass', 'Water Column Volume', 'Mass per unit area', 'Water Concentration',],
        "Mean": ['{0:.2e}'.format(numpy.mean(msed)),'{0:.2e}'.format(numpy.mean(vw)),'{0:.2e}'.format(numpy.mean(mass_area)), '{0:.2e}'.format(numpy.mean(cw))],
        "Std": ['{0:.2e}'.format(numpy.std(msed)),'{0:.2e}'.format(numpy.std(vw)),'{0:.2e}'.format(numpy.std(mass_area)), '{0:.2e}'.format(numpy.std(cw))],
        "Min": ['{0:.2e}'.format(numpy.min(msed)),'{0:.2e}'.format(numpy.min(vw)),'{0:.2e}'.format(numpy.min(mass_area)), '{0:.2e}'.format(numpy.min(cw))],
         "Max": ['{0:.2e}'.format(numpy.max(msed)),'{0:.2e}'.format(numpy.max(vw)),'{0:.2e}'.format(numpy.max(mass_area)), '{0:.2e}'.format(numpy.max(cw))],
        "Unit": ['kg', mark_safe('m<sup>3</sup>'), 'kg/ha', mark_safe('&#956;g/L'),],
    }
    return data

pvuheadings = getheaderpvu()
pvuheadings_calculated = getheaderpvu_calculated()
pvuheadingsqaqc = getheaderpvuqaqc()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_all(rice_obj):
   
    html_all = table_1(rice_obj)      
    html_all = html_all + table_2(rice_obj)

    return html_all

def table_all_qaqc(rice_obj):
   
    html_all = table_1_qaqc(rice_obj)
    html_all = html_all + table_2_qaqc(rice_obj)

    return html_all

def timestamp(rice_obj="", batch_jid=""):
    if rice_obj:
        st = datetime.datetime.strptime(rice_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>Tier 1 Rice Model (Version 1.0)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def table_1(rice_obj):
        #pre-table 1
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Model Inputs</H4>
                <div class="out_ container_output">
        """
        #table 1
        t1data = gett1data(rice_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_1_qaqc(rice_obj):
        #pre-table 1
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Model Inputs</H4>
                <div class="out_ container_output">
        """
        #table 1
        t1data = gett1dataqaqc(rice_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvuheadingsqaqc)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadingsqaqc)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_2(rice_obj):
        #pre-table 1
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>Rice Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Model Output</H4>
                <div class="out_ container_output">
        """
        #table 1
        t2data = gett2data(rice_obj)
        t2rows = gethtmlrowsfromcols(t2data, pvuheadings_calculated)
        html = html + tmpl.render(Context(dict(data = t2rows, headings = pvuheadings_calculated)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_2_qaqc(rice_obj):
        #pre-table 1
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>Rice Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Model Output</H4>
                <div class="out_ container_output">
        """
        #table 1
        t2data = gett2dataqaqc(rice_obj)
        t2rows = gethtmlrowsfromcols(t2data, pvuheadingsqaqc)
        html = html + tmpl.render(Context(dict(data = t2rows, headings = pvuheadingsqaqc)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_sum_all(sumheadings, tmpl, mai, dsed, a, pb, dw, osed, kd, msed, vw, mass_area, cw):
    html_all_sum = table_sum_input(sumheadings, tmpl, mai, dsed, a, pb, dw, osed, kd)
    html_all_sum += table_sum_output(sumheadings, tmpl, msed, vw, mass_area, cw)
    return html_all_sum

def table_sum_input(sumheadings, tmpl, mai, dsed, a, pb, dw, osed, kd):
    #pre-table sum_input
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Batch Inputs</H4>
                <div class="out_ container_output">
        """
        #table sum_input
        tsuminputdata = gettsumdata(mai, dsed, a, pb, dw, osed, kd)
        tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
        html = html + """
        </div>
        """
        return html

def table_sum_output(sumheadings, tmpl, msed, vw, mass_area, cw):
    #pre-table sum_input
        html = """
        <br>
            <H4 class="out_1 collapsible" id="section3"><span></span>Rice Model Outputs</H4>
                <div class="out_ container_output">
        """
        #table sum_input
        tsumoutputdata = gettsumdata_out(msed, vw, mass_area, cw)
        tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings)))
        html = html + """
                </div>
        </div>
        <br>
        """
        return html

