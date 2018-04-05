"""
.. module:: varroapop_tables
   :synopsis: A useful module indeed.
"""

import datetime
import logging

from django.template import Context, Template
from django.utils.safestring import mark_safe

logger = logging.getLogger("varroapopTables")


def getheaderinp():
    headings = ["Description", "Value"]
    return headings

def getheaderbigtable():
    headings = ['Date', 'Colony size', 'Adult drones', 'Adult workers', 'Foragers', 'Capped drone brood',
                'Capped worker Brood', 'Drone larvae', 'Worker larvae', 'Drone eggs', 'Worker eggs', 'Free mites',
                'Drone brood mites', 'Worker brood mites', 'Drone mites/cell', 'Worker mites/cell', 'Mites dying',
                'Proportion mites dying', 'Colony pollen (g)', 'Conc. of chemical in pollen (ug/g)',
                'Colony nectar (g)','Conc. of chemical in nectar (ug/g)', 'Dead drone larvae', 'Dead worker larvae',
                'Dead drone adults', 'Dead worker adults', 'Dead foragers', 'Queen Strength', 'Average temperature (C)',
                'Precip. (in)']
    return headings

def getheadertest():
    headings = ['Date', 'Colony size', 'Colony pollen (g)', 'Colony nectar (g)']
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

def getdatatest(varroapop_obj):
    data = {
        "Date": varroapop_obj.pd_obj_out['out_date'].tolist(),
        "Colony size": ["{0!s}".format(output) for output in varroapop_obj.pd_obj_out['out_colony_size'].tolist()],
        "Colony pollen (g)": ["{0!s}".format(output) for output in varroapop_obj.pd_obj_out['out_colony_pollen'].tolist()],
        "Colony nectar (g)": ["{0!s}".format(output) for output in varroapop_obj.pd_obj_out['out_colony_nectar'].tolist()]
    }
    return data

def getdatabig(varroapop_obj):
    data = { 
        "Description": ['Application rate (lb a.i./A)', 'Application method', mark_safe('Log Kow'), mark_safe('Koc)'), 'Mass of tree vegetation (kg-wet weight)'],
        "Value": [beerex_obj.application_rate, beerex_obj.application_method, beerex_obj.log_kow, beerex_obj.koc, beerex_obj.mass_tree_vegetation,]
    }
    return data



testheadings = getheadertest()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(varroapop_obj):
    html_all = table_test(varroapop_obj)
    return html_all


def timestamp(varroapop_obj="", batch_jid=""):
    if varroapop_obj:
        st = datetime.datetime.strptime(varroapop_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
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


def table_test(varroapop_obj):
    html = """
    <H3 class="out_1 collapsible" id="section1"><span></span>VarroaPop output</H3>
    <div class="out_">
        <H4 class="out_1 collapsible" id="section2"><span></span>Raw colony data</H4>
            <div class="out_ container_output">
    """
    t1data = getdatatest(varroapop_obj)
    t1rows = gethtmlrowsfromcols(t1data, testheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=testheadings)))
    html = html + """
            </div>
    </div>
    """
    return html

