"""
.. module:: sam_tables
   :synopsis: A useful module indeed.
"""
from django.template import Context, Template
from django.utils.safestring import mark_safe
import time
import datetime
from django.template.loader import render_to_string


def getheaderpvu():
    headings = ["Parameter", "Value"]
    return headings

def getheaderpvu2():
    headings = ["Parameter", "Value", "Units"]
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
 
def gett1data(przm_obj):
    data = { 
        "Parameter": ['Chemical Name', 'Standard OPP/EFED Scenarios', 'Weather station', 'Met filename',
                      'INP filename', 'RUN filename', 'Number of applications',],
        "Value": ['%s' % przm_obj.chemical_name, przm_obj.Scenarios, '%s' % przm_obj.station, '%s' % przm_obj.met_o,
                  '%s' % przm_obj.inp_o, '%s' % przm_obj.run_o, '%s' % przm_obj.NOA,],
    }
    return data

def timestamp(sam_obj="", batch_jid=""):
    if sam_obj:
        st = datetime.datetime.strptime(sam_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
    <b>Surface Aquatic Model (SAM) Beta<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """-
    </div>"""
    return html

def table_all(sam_obj):
    html = """
    <H3 class="out_3 collapsible" id="section1"><span></span>Model Outputs</H3>
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
    </div>""" %sam_obj.link
    return html