"""
.. module:: sip_tables
   :synopsis: A useful module indeed.
"""

import numpy
from django.template import Context, Template
from django.utils.safestring import mark_safe
import logging
import time
import datetime

logger = logging.getLogger("SipTables")

def getheaderpvu():
	headings = ["Parameter", "Value", "Units"]
	return headings

def getheaderpvr():
	headings = ["Parameter", "Acute", "Chronic","Units"]
	return headings

def getheaderpvrqaqc():
    headings = ["Parameter", "Acute", "Acute-Expected", "Chronic", "Chronic-Expected","Units"]
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

def gett1data(sip_obj):
    data = { 
        "Parameter": ['Chemical Name',mark_safe('Solubility (in water @25&deg;C)'),mark_safe('Mammalian LD<sub>50</sub>'),'Body Weight of Tested Mammal','Body Weight of Assessed Mammal','Mammalian NOAEL',mark_safe('Avian LD<sub>50</sub>'),'Body Weight of Tested Bird','Body Weight of Assessed Bird','Mineau Scaling Factor','Avian NOAEC',],
        "Value": [sip_obj.chemical_name,sip_obj.solubility,sip_obj.ld50_mammal_water,sip_obj.bodyweight_tested_mammal,sip_obj.bodyweight_assessed_mammal,sip_obj.noael_mammal_water,sip_obj.ld50_avian_water,sip_obj.bodyweight_tested_bird,sip_obj.bodyweight_assessed_bird,sip_obj.mineau_scaling_factor,sip_obj.noael_avian_water,],
        "Units": ['','mg/L','mg/kg-bw','g','g','mg/kg-bw','mg/kg-bw','g','g','','mg/kg-diet'],
    }
    return data

def gett1dataqaqc(sip_obj):
    data = { 
        "Parameter": ['Chemical Name',mark_safe('Solubility (in water @25&deg;C)'),mark_safe('Mammalian LD<sub>50</sub>'),'Body Weight of Tested Mammal','Body Weight of Assessed Mammal','Mammalian NOAEL',mark_safe('Avian LD<sub>50</sub>'),'Body Weight of Tested Bird','Body Weight of Assessed Bird','Mineau Scaling Factor','Avian NOAEC',],
        "Value": [sip_obj.chemical_name_expected,sip_obj.solubility,sip_obj.ld50_mammal_water,sip_obj.bodyweight_tested_mammal,sip_obj.bodyweight_assessed_mammal,sip_obj.noael_mammal_water,sip_obj.ld50_avian_water,sip_obj.bodyweight_tested_bird,sip_obj.bodyweight_assessed_bird,sip_obj.mineau_scaling_factor,sip_obj.noael_avian_water,],
        "Units": ['','mg/L','mg/kg-bw','g','g','mg/kg-bw','mg/kg-bw','g','g','','mg/kg-diet'],
    }
    return data

def gett2data(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%.3e' % sip_obj.dose_mamm_out, '%.4f' % sip_obj.at_mamm_out, '%.4f' % sip_obj.acute_mamm_out, '%s' % sip_obj.acuconm_out,],
        "Chronic": ['%.3e' % sip_obj.dose_mamm_out, '%.4f' % sip_obj.act_out, '%.4f' % sip_obj.chron_mamm_out, '%s' % sip_obj.chronconm_out,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett2dataqaqc(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%.3e' % sip_obj.dose_mamm_out, '%.4f' % sip_obj.at_mamm_out, '%.4f' % sip_obj.acute_mamm_out, '%s' % sip_obj.acuconm_out,],
        "Acute-Expected": ['%.3e' % sip_obj.dose_mamm_out_expected,'%.4f' % sip_obj.at_mamm_out_expected,'%.4f' % sip_obj.acute_mamm_out_expected,'%s' % sip_obj.acuconm_out_expected,],
        "Chronic": ['%.3e' % sip_obj.dose_mamm_out, '%.4f' % sip_obj.act_out, '%.4f' % sip_obj.chron_mamm_out, '%s' % sip_obj.chronconm_out,],
        "Chronic-Expected": ['%.3e' % sip_obj.dose_mamm_out_expected,'%.4f' % sip_obj.act_out_expected,'%.4f' % sip_obj.chron_mamm_out_expected,'%s' % sip_obj.chronconm_out_expected,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett3data(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%.5e' % sip_obj.dose_bird_out, '%.4f' % sip_obj.at_bird_out,'%.4f' % sip_obj.acute_bird_out, '%s' % sip_obj.acuconb_out,],
        "Chronic": ['%.5e' % sip_obj.dose_bird_out, '%.4f' % sip_obj.det_out,'%.4f' % sip_obj.chron_bird_out, '%s' % sip_obj.chronconb_out,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett3dataqaqc(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%.5e' % sip_obj.dose_bird_out, '%.4f' % sip_obj.at_bird_out,'%.4f' % sip_obj.acute_bird_out, '%s' % sip_obj.acuconb_out,],
        "Acute-Expected": ['%.5e' % sip_obj.dose_bird_out_expected, '%.4f' % sip_obj.at_bird_out_expected, '%.4f' % sip_obj.acute_bird_out_expected, '%s' % sip_obj.acuconb_out_expected,],
        "Chronic": ['%.5e' % sip_obj.dose_bird_out, '%.4f' % sip_obj.det_out,'%.4f' % sip_obj.chron_bird_out, '%s' % sip_obj.chronconb_out,],
        "Chronic-Expected": ['%.5e' % sip_obj.dose_bird_out_expected,'%.4f' % sip_obj.det_out_expected,'%.4f' % sip_obj.chron_bird_out_expected,'%s' % sip_obj.chronconb_out_expected,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gettsumdata(bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,bodyweight_assessed_bird,mineau_scaling_factor,bodyweight_assessed_mammal,noael_avian_water,noael_mammal_water):
    data = { 
        "Parameter": ['BW Quail', 'BW Duck', 'BW Bird Other', 'BW Rat', 'BW Mammal Other', 'Avian LD50', 'Mammalian LD50', 
                    'Solubility','AW Bird' , 'Mineau', 'AW Mammalian', 'NOAEC','NOAEL'],
        "Mean": ['%.2e' % numpy.mean(bodyweight_quail),'%.2e' % numpy.mean(bodyweight_duck),'%.2e' % numpy.mean(bodyweight_bird_other), '%.2e' % numpy.mean(bodyweight_rat), 
                 '%.2e' % numpy.mean(bodyweight_tested_mammal_other), '%.2e' % numpy.mean(solubility), '%.2e' % numpy.mean(avian_ld50), '%.2e' % numpy.mean(mammalian_ld50),
                 '%.2e' % numpy.mean(bodyweight_assessed_bird), '%.2e' % numpy.mean(mineau_scaling_factor), '%.2e' % numpy.mean(bodyweight_assessed_mammal),
                 '%.2e' % numpy.mean(noael_avian_water), '%.2e' % numpy.mean(noael_mammal_water),],
        "Std": ['%.2e' % numpy.std(bodyweight_quail),'%.2e' % numpy.std(bodyweight_duck),'%.2e' % numpy.std(bodyweight_bird_other), '%.2e' % numpy.std(bodyweight_rat), 
                '%.2e' % numpy.std(bodyweight_tested_mammal_other), '%.2e' % numpy.std(solubility), '%.2e' % numpy.std(avian_ld50), '%.2e' % numpy.std(mammalian_ld50),
                 '%.2e' % numpy.std(bodyweight_assessed_bird), '%.2e' % numpy.std(mineau_scaling_factor), '%.2e' % numpy.std(bodyweight_assessed_mammal),
                 '%.2e' % numpy.std(noael_avian_water),'%.2e' % numpy.std(noael_mammal_water),],
        "Min": ['%.2e' % numpy.min(bodyweight_quail),'%.2e' % numpy.min(bodyweight_duck),'%.2e' % numpy.min(bodyweight_bird_other), '%.2e' % numpy.min(bodyweight_rat), 
                '%.2e' % numpy.min(bodyweight_tested_mammal_other), '%.2e' % numpy.min(solubility), '%.2e' % numpy.min(avian_ld50), '%.2e' % numpy.min(mammalian_ld50),
                 '%.2e' % numpy.min(bodyweight_assessed_bird), '%.2e' % numpy.min(mineau_scaling_factor), '%.2e' % numpy.min(bodyweight_assessed_mammal),
                 '%.2e' % numpy.min(noael_avian_water),'%.2e' % numpy.min(noael_mammal_water),],
         "Max": ['%.2e' % numpy.max(bodyweight_quail),'%.2e' % numpy.max(bodyweight_duck),'%.2e' % numpy.max(bodyweight_bird_other), '%.2e' % numpy.max(bodyweight_rat), 
                '%.2e' % numpy.max(bodyweight_tested_mammal_other), '%.2e' % numpy.max(solubility), '%.2e' % numpy.max(avian_ld50), '%.2e' % numpy.max(mammalian_ld50),
                 '%.2e' % numpy.max(bodyweight_assessed_bird), '%.2e' % numpy.max(mineau_scaling_factor), '%.2e' % numpy.max(bodyweight_assessed_mammal),
                 '%.2e' % numpy.max(noael_avian_water),'%.2e' % numpy.max(noael_mammal_water),],
        "Unit": ['g', 'g', 'g', 'g', 'g','mg/kg-bw', 'mg/kg-bw', 'mg/L','g', '', 'g','mg/kg-diet', 'mg/kg-bw',],
    }
    return data

def gettsumdata_out(dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out):
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
                 '%.2e' % numpy.mean(dose_bird_out), '%.2e' % numpy.mean(dose_mamm_out), '%.2e' % numpy.mean(at_bird_out),
                 '%.2e' % numpy.mean(at_mamm_out), '%.2e' % numpy.mean(act_out), '%.2e' % numpy.mean(det_out),
                 '%.2e' % numpy.mean(acute_bird_out), '%.2e' % numpy.mean(acute_mamm_out),
                 '%.2e' % numpy.mean(chron_bird_out), '%.2e' % numpy.mean(chron_mamm_out),],

        "Std": ['%.2e' % numpy.std(dose_bird_out), '%.2e' % numpy.std(dose_mamm_out), '%.2e' % numpy.std(at_bird_out),
                '%.2e' % numpy.std(at_mamm_out), '%.2e' % numpy.std(act_out), '%.2e' % numpy.std(det_out),
                '%.2e' % numpy.std(acute_bird_out), '%.2e' % numpy.std(acute_mamm_out),
                '%.2e' % numpy.std(chron_bird_out), '%.2e' % numpy.std(chron_mamm_out),],

        "Min": ['%.2e' % numpy.min(dose_bird_out), '%.2e' % numpy.min(dose_mamm_out), '%.2e' % numpy.min(at_bird_out),
                '%.2e' % numpy.min(at_mamm_out), '%.2e' % numpy.min(act_out), '%.2e' % numpy.min(det_out),
                '%.2e' % numpy.min(acute_bird_out), '%.2e' % numpy.min(acute_mamm_out),
                '%.2e' % numpy.min(chron_bird_out), '%.2e' % numpy.min(chron_mamm_out),],

         "Max": ['%.2e' % numpy.max(dose_bird_out), '%.2e' % numpy.min(dose_mamm_out), '%.2e' % numpy.min(at_bird_out),
                '%.2e' % numpy.max(at_mamm_out), '%.2e' % numpy.max(act_out), '%.2e' % numpy.min(det_out),
                '%.2e' % numpy.max(acute_bird_out), '%.2e' % numpy.min(acute_mamm_out),
                '%.2e' % numpy.max(chron_bird_out), '%.2e' % numpy.max(chron_mamm_out),],

        "Unit": ['mg/kg-bw', 'mg/kg-bw','mg/kg-bw', 'mg/kg-bw', 'mg/kg-bw', 'mg/kg-bw', '','', '', '',],
    }
    return data


pvuheadings = getheaderpvu()
pvrheadings = getheaderpvr()
pvrheadingsqaqc = getheaderpvrqaqc()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_all(sip_obj):
    html_all = table_1(sip_obj)      
    html_all = html_all + table_2(sip_obj)
    html_all = html_all + table_3(sip_obj)
    return html_all

def table_all_qaqc(sip_obj):
    html_all = table_1_qaqc(sip_obj)
    html_all = html_all + table_2_qaqc(sip_obj)
    html_all = html_all + table_3_qaqc(sip_obj)
    return html_all

def timestamp(sip_obj="", batch_jid=""):
    if sip_obj:
        st = datetime.datetime.strptime(sip_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>SIP <a href="http://www.epa.gov/oppefed1/models/terrestrial/sip/sip_user_guide.html">Version 1.0</a> (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def table_1(sip_obj):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Application and Chemical Information</H4>
                <div class="out_ container_output">
        """
        t1data = gett1data(sip_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_1_qaqc(sip_obj):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Application and Chemical Information</H4>
                <div class="out_ container_output">
        """
        t1data = gett1dataqaqc(sip_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_2(sip_obj):
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>SIP Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Mammalian Results (%s g)</H4>
                <div class="out_ container_output">
        """%(sip_obj.bodyweight_assessed_mammal)
        t2data = gett2data(sip_obj)
        t2rows = gethtmlrowsfromcols(t2data,pvrheadings)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvrheadings)))
        html = html + """
                </div>
        """
        return html  

def table_2_qaqc(sip_obj):
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>SIP Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Mammalian Results (%s g)</H4>
                <div class="out_ container_output">
        """%(sip_obj.bodyweight_assessed_mammal)
        t2data = gett2dataqaqc(sip_obj)
        t2rows = gethtmlrowsfromcols(t2data,pvrheadingsqaqc)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvrheadingsqaqc)))
        html = html + """
                </div>
        """
        return html  

def table_3(sip_obj):
        html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Avian Results (%s g)</H4>
                <div class="out_ container_output">
        """%(sip_obj.bodyweight_assessed_bird)
        t3data = gett3data(sip_obj)
        t3rows = gethtmlrowsfromcols(t3data,pvrheadings)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=pvrheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_3_qaqc(sip_obj):
        html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Avian Results (%s g)</H4>
                <div class="out_ container_output">
        """%(sip_obj.bodyweight_assessed_bird)
        t3data = gett3dataqaqc(sip_obj)
        t3rows = gethtmlrowsfromcols(t3data,pvrheadingsqaqc)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=pvrheadingsqaqc)))
        html = html + """
                </div>
        </div>
        """
        return html


def table_all_sum(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,bodyweight_assessed_bird,mineau_scaling_factor,bodyweight_assessed_mammal,noael_avian_water,noael_mammal_water,
                    dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out):
    html_all_sum = table_sum_input(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,bodyweight_assessed_bird,mineau_scaling_factor,bodyweight_assessed_mammal,noael_avian_water,noael_mammal_water)
    html_all_sum += table_sum_output(sumheadings,tmpl,dose_bird_out,dose_mamm_out,at_bird_out, 
                    at_mamm_out,det_out,act_out,acute_bird_out,acute_mamm_out,chron_bird_out,chron_mamm_out)
    return html_all_sum

def table_sum_input(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,bodyweight_assessed_bird,mineau_scaling_factor,bodyweight_assessed_mammal,noael_avian_water,noael_mammal_water):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Batch Inputs</H4>
                <div class="out_ container_output">
        """
        tsuminputdata = gettsumdata(bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,avian_ld50,mammalian_ld50,bodyweight_assessed_bird,mineau_scaling_factor,bodyweight_assessed_mammal,noael_avian_water,noael_mammal_water)
        tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
        html = html + """
                </div>
        """
        return html

def table_sum_output(sumheadings, tmpl, dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out):
        html = """
        <br>
            <H4 class="out_1 collapsible" id="section3"><span></span>SIP Outputs</H4>
                <div class="out_ container_output">
        """
        tsumoutputdata = gettsumdata_out(dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out)
        tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

