"""
.. module:: varroapop_tables
   :synopsis: A useful module indeed.
"""

import datetime
import logging

from django.template import Context, Template
from django.utils.safestring import mark_safe
from .varroapop_plots import VarroapopPlots


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
    html_all = summary_tab(varroapop_obj)
    html_all += plots_tab(varroapop_obj)
    html_all += table_test(varroapop_obj)
    return html_all


def summary_tab(varroapop_obj):
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>VarroaPop summary tables</H3>
        <div class="out_">
        """
    html += col_success_sum_tab(varroapop_obj)
    html += "<br>"
    html += """
        </div>
        """
    return html

def plots_tab(varroapop_obj):
    plots_obj = VarroapopPlots(varroapop_obj)
    html =  """
    <H3 class="out_2 collapsible" id="section1"><span></span>VarroaPop interactive plots</H3>
    <div class="out_">
    """
    html += bee_pop_plot_tab(plots_obj)
    html += "<br>"
    html += pol_nec_tab(plots_obj)
    html += "<br>"
    html += mites_tab(plots_obj)
    html += "<br>"
    html += mortality_tab(plots_obj)
    html += "<br>"
    html += """
    </div>
    """
    return html

def bee_pop_plot_tab(plots_obj):
    html = """
        <H4 class="out_1 collapsible" id="section2"><span></span>Colony population</H4>
            <div class="out_ container_output">
        """
    html += plots_obj.bee_pop_plot()
    html += """
            </div>
            """
    return html


def pol_nec_tab(plots_obj):
    html = """
            <H4 class="out_2 collapsible" id="section2"><span></span>Resources and chemical contamination</H4>
                <div class="out_ container_output">
            """
    html += plots_obj.pol_nec_plot()
    html += """
                </div>
                """
    return html


def mites_tab(plots_obj):
    html = """
            <H4 class="out_3 collapsible" id="section2"><span></span>Mite population</H4>
                <div class="out_ container_output">
            """
    html += plots_obj.mites_plot()
    html += """
                </div>
                """
    return html

def mortality_tab(plots_obj):
    html = """
                <H4 class="out_4 collapsible" id="section2"><span></span>Bee mortality due to chemical exposure</H4>
                    <div class="out_ container_output">
                """
    html += plots_obj.mortality_plot()
    html += """
                    </div>
                    """
    return html


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

def col_success_sum_tab(varroapop_obj):
    html = """

            <H4 class="out_6 collapsible" id="section2"><span></span>Colony success summary</H4>
                <div class="out_ container_output">
        """
    successheadings = getheaderinp()
    t1data = getdata_success(varroapop_obj)
    t1rows = gethtmlrowsfromcols(t1data, successheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=successheadings)))
    html = html + """
                </div>
        """
    return html


def getdata_success(varroapop_obj):
    data = {
        "Description": ["Mean colony size", "Min colony size", "Max colony size", "Total bee mortality due to A.I.",
                        "A.I. max concentration in colony pollen (ppm)", "A.I. max concentration in colony nectar (ppm)"],
        "Value": ["{0:.0f}".format(varroapop_obj.out_mean_colony_size), "{0:.0f}".format(varroapop_obj.out_min_colony_size),
                  "{0:.0f}".format(varroapop_obj.out_max_colony_size), "{0:.0f}".format(varroapop_obj.out_total_bee_mortality),
                  "{0:.4f}".format(varroapop_obj.out_max_chemical_conc_pollen), "{0:.4f}".format(varroapop_obj.out_max_chemical_conc_nectar)]
    }
    return data


def getheader_success():
    headings = ['Mean colony size', 'Min colony size', 'Max colony size', 'Total bee mortality due to A.I.',
                'A.I. max concentration in colony pollen (ug/g)', 'A.I. max concentration in colony nectar (ug/g)']
    return headings

def table_test(varroapop_obj):
    html = """
    <H3 class="out_3 collapsible" id="section1"><span></span>Summary tables</H3>
    <div class="out_">
        <H4 class="out_1 collapsible" id="section2"><span></span>Summary table 1</H4>
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

