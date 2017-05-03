"""
.. module:: kabam_tables
   :synopsis: A useful module indeed.
"""

import datetime
import logging

import numpy as np
from django.template import Context, Template
from django.utils.safestring import mark_safe

logger = logging.getLogger("KabamTables")


def getheaderpvu():
    headings = ["Parameter", "Value", "Units"]
    return headings


def getheaderptldr():
    headings = ["Parameter", mark_safe("Total <br>(&#956;g/kg-ww)"),
                mark_safe("Lipid Normalized <br>(&#956;g/kg-lipid)"),
                mark_safe("Diet Contribution <br>(&#956;g/kg-ww)"),
                mark_safe("Respiration Contribution <br>(&#956;g/kg-ww)")]
    return headings


def getheaderttb():
    headings = ["Trophic Level", mark_safe("Total BCF <br>(&#956;g/kg-ww)/<br>(&#956;g/L)"),
                mark_safe("Total BAF <br>(&#956;g/kg-ww)/<br>(&#956;g/L)")]
    return headings


def getheadertbbbb():
    headings = ["Trophic Level", mark_safe("BCF <br>(&#956;g/kg-lipid)/<br>(&#956;g/L)"),
                mark_safe("BAF <br>(&#956;g/kg-lipid)/<br>(&#956;g/L)"),
                mark_safe("BMF <br>(&#956;g/kg-lipid)/<br>(&#956;g/kg-lipid)"),
                mark_safe("BSAF <br>(&#956;g/kg-lipid)/<br>(&#956;g/kg-lipid)")]
    return headings


def getheaderwbdwddd():
    headings = ["Wildlife Species", "Body Weight (kg)", "Dry Food Ingestion Rate (kg-dry food/kg-bw/day)",
                "Wet Food Ingestion Rate (kg-wet food/kg-bw/day)", "Drinking Water Intake (L/d)",
                "Dose Based (mg/kg-bw/d)", "Dietary Based (ppm)"]
    return headings


def getheaderwadadcdcd():
    headings = ["Wildlife Species", "Acute Dose Based (mg/kg-bw)", "Acute Dietary Based (mg/kg-diet)",
                "Chronic Dose Based (mg/kg-bw)", "Chronic Dietary Based (mg/kg-diet)"]
    return headings


def getheaderwadadcdcd_noUnits():
    headings = ["Wildlife Species", "Acute Dose Based", "Acute Dietary Based", "Chronic Dose Based",
                "Chronic Dietary Based"]
    return headings


def getheadersum():
    headings = ["Parameter", "Mean", "Std", "Min", "Max", "Unit"]
    return headings


def getheadersum_out():
    headings = ["Parameter", "Mean", "Std", "Min", "Max"]
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


def gett1data(kabam_obj):
    data = {
        "Parameter": ['Chemical Name', mark_safe('Log K<sub>OW</sub>'), mark_safe('K<sub>OC</sub>'), 'Pore Water EEC',
                      'Water Column EEC'],
        "Value": [kabam_obj.chemical_name, kabam_obj.log_kow, kabam_obj.k_oc, (1e6 * kabam_obj.pore_water_eec),
                  kabam_obj.water_column_eec],
        "Units": ['', '', 'L/kg OC', mark_safe('&#956;g/L'), mark_safe('&#956;g/L')],
    }
    return data


def gett1dataqaqc(kabam_obj):
    data = {
        "Parameter": ['Chemical Name', mark_safe('Log K<sub>OW</sub>'), mark_safe('K<sub>OC</sub>'), 'Pore Water EEC',
                      'Water Column EEC'],
        "Value": [kabam_obj.chemical_name_exp, kabam_obj.log_kow, kabam_obj.k_oc, (1e6 * kabam_obj.pore_water_eec),
                  kabam_obj.water_column_eec],
        "Units": ['', '', 'L/kg OC', mark_safe('&#956;g/L'), mark_safe('&#956;g/L')],
    }
    return data


def gett2data(kabam_obj):
    data = {
        "Parameter": ['Water Total', 'Water Freely Dissolved', 'Sediment Pore Water', 'Sediment in Solid',
                      'Phytoplankton', 'Zooplankton', 'Benthic Invertebrates', 'Filter Feeders', 'Small Fish',
                      'Medium Fish', 'Large Fish'],
        mark_safe("Total <br>(&#956;g/kg-ww)"): [mark_safe('{0:.0f} (&#956;g/L)'.format(kabam_obj.water_column_eec)),
                                                 mark_safe('{0:.0f} (&#956;g/L)'.format(kabam_obj.out_free_pest_conc_watercol)),
                                                 mark_safe('{0:.0f} (&#956;g/L)'.format((1e6 * kabam_obj.pore_water_eec))),
                                                 mark_safe('{0:.0f} (&#956;g/kg-dw)'.format((1e6 * kabam_obj.conc_ss))),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_phytoplankton)),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_zoo)),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_beninv)), '{0:.0f}'.format((1e6 * kabam_obj.out_cb_filterfeeders)),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_sfish)), '{0:.0f}'.format((1e6 * kabam_obj.out_cb_mfish)),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_lfish))],
        mark_safe("Lipid Normalized <br>(&#956;g/kg-lipid)"): ['N/A', 'N/A', 'N/A', 'N/A',
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_phytoplankton),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_zoo),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_beninv), '{0:.0f}'.format(kabam_obj.out_cbl_filterfeeders),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_sfish), '{0:.0f}'.format(kabam_obj.out_cbl_mfish),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_lfish)],
        mark_safe("Diet Contribution <br>(&#956;g/kg-ww)"): ['N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_zoo)),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_beninv)),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_filterfeeders)),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_sfish)),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_mfish)),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_lfish))],
        mark_safe("Respiration Contribution <br>(&#956;g/kg-ww)"): ['N/A', 'N/A', 'N/A', 'N/A',
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_phytoplankton)),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_zoo)),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_beninv)),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_filterfeeders)),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_sfish)),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_mfish)),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_lfish))],

    }

    return data


def gett2dataqaqc(kabam_obj):
    data = {
        "Parameter": ['Water Total', 'Water Freely Dissolved', 'Sediment Pore Water', 'Sediment in Solid',
                      'Phytoplankton', 'Expected Phytoplankton', 'Zooplankton', 'Expected Zooplankton',
                      'Benthic Invertebrates', 'Expected Benthic Invertebrates', 'Filter Feeders',
                      'Expected Filter Feeders', 'Small Fish', 'Expected Small Fish', 'Medium Fish',
                      'Expected Medium Fish', 'Large Fish', 'Expected Large Fish'],
        mark_safe("Total <br>(&#956;g/kg-ww)"): [mark_safe('{0:.0f} (&#956;g/L)'.format(kabam_obj.water_column_eec)),
                                                 mark_safe('{0:.0f} (&#956;g/L)'.format(kabam_obj.out_water_dissolved)),
                                                 mark_safe('{0:.0f} (&#956;g/L)'.format((1e6 * kabam_obj.pore_water_eec))),
                                                 mark_safe('{0:.0f} (&#956;g/kg-dw)'.format((1e6 * kabam_obj.conc_ss))),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_phytoplankton)),
                                                 '{0:.0f}'.format(kabam_obj.out_cb_phytoplankton_exp),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_zoo)), '{0:.0f}'.format(kabam_obj.out_cb_zoo_exp),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_beninv)), '{0:.0f}'.format(kabam_obj.out_cb_beninv_exp),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_filterfeeders)), '{0:.0f}'.format(kabam_obj.out_cb_filterfeeders_exp),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_sfish)), '{0:.0f}'.format(kabam_obj.out_cb_sfish_exp),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_mfish)), '{0:.0f}'.format(kabam_obj.out_cb_mfish_exp),
                                                 '{0:.0f}'.format((1e6 * kabam_obj.out_cb_lfish)), '{0:.0f}'.format(kabam_obj.out_cb_lfish_exp)],
        mark_safe("Lipid Normalized <br>(&#956;g/kg-lipid)"): ['N/A', 'N/A', 'N/A', 'N/A',
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_phytoplankton),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_phytoplankton_exp),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_zoo),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_zoo_exp),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_beninv),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_beninv_exp),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_filterfeeders), '{0:.0f}'.format(kabam_obj.out_cbl_filterfeeders_exp),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_sfish), '{0:.0f}'.format(kabam_obj.out_cbl_sfish_exp),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_mfish), '{0:.0f}'.format(kabam_obj.out_cbl_mfish_exp),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_lfish),
                                                               '{0:.0f}'.format(kabam_obj.out_cbl_lfish_exp)],
        mark_safe("Diet Contribution <br>(&#956;g/kg-ww)"): ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_zoo)),
                                                             '{0:.2f}'.format(kabam_obj.out_cbd_zoo_exp),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_beninv)),
                                                             '{0:.2f}'.format(kabam_obj.out_cbd_beninv_exp),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_filterfeeders)),
                                                             '{0:.2f}'.format(kabam_obj.out_cbd_filterfeeders_exp),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_sfish)),
                                                             '{0:.2f}'.format(kabam_obj.out_cbd_sfish_exp),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_mfish)),
                                                             '{0:.2f}'.format(kabam_obj.out_cbd_mfish_exp),
                                                             '{0:.2f}'.format((1e6 * kabam_obj.out_cbd_lfish)),
                                                             '{0:.2f}'.format(kabam_obj.out_cbd_lfish_exp)],
        mark_safe("Respiration Contribution <br>(&#956;g/kg-ww)"): ['N/A', 'N/A', 'N/A', 'N/A',
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_phytoplankton)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_phytoplankton_exp),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_zoo)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_zoo_exp),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_beninv)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_beninv_exp),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_filterfeeders)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_filterfeeders_exp),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_sfish)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_sfish_exp),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_mfish)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_mfish_exp),
                                                                    '{0:.2f}'.format((1e6 * kabam_obj.out_cbr_lfish)),
                                                                    '{0:.2f}'.format(kabam_obj.out_cbr_lfish_exp)],
    }
    return data


def gett3data(kabam_obj):
    data = {
        "Trophic Level": ['Phytoplankton', 'Zooplankton', 'Benthic Invertebrates', 'Filter Feeders', 'Small Fish',
                          'Medium Fish', 'Large Fish'],
        mark_safe("Total BCF <br>(&#956;g/kg-ww)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbf_phytoplankton),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_zoo),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_beninv),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_filterfeeders),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_sfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_mfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_lfish)],
        mark_safe("Total BAF <br>(&#956;g/kg-ww)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbaf_phytoplankton),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_zoo),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_beninv),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_filterfeeders),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_sfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_mfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_lfish)],
    }
    return data


def gett3dataqaqc(kabam_obj):
    data = {
        "Trophic Level": ['Phytoplankton', 'Expected Phytoplankton', 'Zooplankton', 'Expected Zooplankton',
                          'Benthic Invertebrates', 'Expected Benthic Invertebrates', 'Filter Feeders',
                          'Expected Filter Feeders', 'Small Fish', 'Expected Small Fish', 'Medium Fish',
                          'Expected Medium Fish', 'Large Fish', 'Expected Large Fish'],
        mark_safe("Total BCF <br>(&#956;g/kg-ww)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbf_phytoplankton),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_phytoplankton_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_zoo),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_zoo_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_beninv),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_beninv_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_filterfeeders),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_filterfeeders_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_sfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_sfish_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_mfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_mfish_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_lfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbf_lfish_exp)],
        mark_safe("Total BAF <br>(&#956;g/kg-ww)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbaf_phytoplankton),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_phytoplankton_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_zoo),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_zoo_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_beninv),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_beninv_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_filterfeeders),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_filterfeeders_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_sfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_sfish_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_mfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_mfish_exp),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_lfish),
                                                                     '{0:.0f}'.format(kabam_obj.out_cbaf_lfish_exp)],
    }
    return data


def gett4data(kabam_obj):
    data = {
        "Trophic Level": ['Phytoplankton', 'Zooplankton', 'Benthic Invertebrates', 'Filter Feeders', 'Small Fish',
                          'Medium Fish', 'Large Fish'],
        mark_safe("BCF <br>(&#956;g/kg-lipid)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbfl_phytoplankton),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_zoo),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_beninv),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_filterfeeders),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_sfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_mfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_lfish)],
        mark_safe("BAF <br>(&#956;g/kg-lipid)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbafl_phytoplankton),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_zoo),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_beninv),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_filterfeeders),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_sfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_mfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_lfish)],
        mark_safe("BMF <br>(&#956;g/kg-lipid)/<br>(&#956;g/kg-lipid)"): ['N/A', '{0:.2f}'.format(kabam_obj.out_bmf_zoo),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_beninv),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_filterfeeders),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_sfish),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_mfish),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_lfish)],
        mark_safe("BSAF <br>(&#956;g/kg-lipid)/<br>(&#956;g/kg-lipid)"): ['{0:.0f}'.format(kabam_obj.out_cbsafl_phytoplankton),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_zoo),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_beninv),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_filterfeeders),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_sfish),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_mfish),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_lfish)],
    }
    return data


def gett4dataqaqc(kabam_obj):
    data = {
        "Trophic Level": ['Phytoplankton', 'Expected Phytoplankton', 'Zooplankton', 'Expected Zooplankton',
                          'Benthic Invertebrates', 'Expected Benthic Invertebrates', 'Filter Feeders',
                          'Expected Filter Feeders', 'Small Fish', 'Expected Small Fish', 'Medium Fish',
                          'Expected Medium Fish', 'Large Fish', 'Expected Large Fish'],
        mark_safe("BCF <br>(&#956;g/kg-lipid)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbfl_phytoplankton),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_phytoplankton_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_zoo),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_zoo_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_beninv),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_beninv_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_filterfeeders),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_filterfeeders_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_sfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_sfish_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_mfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_mfish_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_lfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbfl_lfish_exp)],
        mark_safe("BAF <br>(&#956;g/kg-lipid)/<br>(&#956;g/L)"): ['{0:.0f}'.format(kabam_obj.out_cbafl_phytoplankton),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_phytoplankton_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_zoo),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_zoo_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_beninv),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_beninv_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_filterfeeders),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_filterfeeders_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_sfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_sfish_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_mfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_mfish_exp),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_lfish),
                                                                  '{0:.0f}'.format(kabam_obj.out_cbafl_lfish_exp)],
        mark_safe("BMF <br>(&#956;g/kg-lipid)/<br>(&#956;g/kg-lipid)"): ['N/A', '{0:.2f}'.format(kabam_obj.out_bmf_zoo),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_zoo_exp),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_beninv),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_beninv_exp),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_filterfeeders),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_filterfeeders_exp),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_sfish),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_sfish_exp),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_mfish),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_mfish_exp),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_lfish),
                                                                         '{0:.2f}'.format(kabam_obj.out_bmf_lfish_exp)],
        mark_safe("BSAF <br>(&#956;g/kg-lipid)/<br>(&#956;g/kg-lipid)"): ['{0:.0f}'.format(kabam_obj.out_cbsafl_phytoplankton),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_phytoplankton_exp),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_zoo),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_zoo_exp),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_beninv),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_beninv_exp),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_filterfeeders),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_filterfeeders_exp),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_sfish),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_sfish_exp),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_mfish),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_mfish_exp),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_lfish),
                                                                          '{0:.0f}'.format(kabam_obj.out_cbsafl_lfish_exp)],
    }
    return data


def gett5data(kabam_obj):
    data = {
        "Wildlife Species": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink',
                             'small river otter', 'large river otter', 'sandpipers', 'cranes', 'rails', 'herons',
                             'small osprey', 'white pelican'],
        "Body Weight (kg)": ['{0:.2f}'.format(kabam_obj.out_mweight0), '{0:.2f}'.format(kabam_obj.out_mweight1),
                             '{0:.2f}'.format(kabam_obj.out_mweight2), '{0:.2f}'.format(kabam_obj.out_mweight3),
                             '{0:.2f}'.format(kabam_obj.out_mweight4), '{0:.2f}'.format(kabam_obj.out_mweight5),
                             '{0:.2f}'.format(kabam_obj.out_aweight0), '{0:.2f}'.format(kabam_obj.out_aweight1),
                             '{0:.2f}'.format(kabam_obj.out_aweight2), '{0:.2f}'.format(kabam_obj.out_aweight3),
                             '{0:.2f}'.format(kabam_obj.out_aweight4), '{0:.2f}'.format(kabam_obj.out_aweight5)],
        "Dry Food Ingestion Rate (kg-dry food/kg-bw/day)": ['{0:.3f}'.format(kabam_obj.out_dfir0),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir1),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir2),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir3),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir4),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir5),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira0),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira1),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira2),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira3),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira4),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira5)],
        "Wet Food Ingestion Rate (kg-wet food/kg-bw/day)": ['{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m0),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m1),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m2),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m3),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m4),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m5),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a0),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a1),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a2),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a3),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a4),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a5)],
        "Drinking Water Intake (L/d)": ['{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m0),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m1),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m2),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m3),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m4),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m5),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a0),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a1),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a2),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a3),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a4),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a5)],
        "Dose Based (mg/kg-bw/d)": ['{0:.3f}'.format(kabam_obj.out_db40), '{0:.3f}'.format(kabam_obj.out_db41),
                                    '{0:.3f}'.format(kabam_obj.out_db42), '{0:.3f}'.format(kabam_obj.out_db43),
                                    '{0:.3f}'.format(kabam_obj.out_db44), '{0:.3f}'.format(kabam_obj.out_db45),
                                    '{0:.4f}'.format(kabam_obj.out_db4a0), '{0:.4f}'.format(kabam_obj.out_db4a1),
                                    '{0:.4f}'.format(kabam_obj.out_db4a2), '{0:.4f}'.format(kabam_obj.out_db4a3),
                                    '{0:.4f}'.format(kabam_obj.out_db4a4), '{0:.4f}'.format(kabam_obj.out_db4a5)],
        "Dietary Based (ppm)": ['{0:.2f}'.format(kabam_obj.out_db50), '{0:.2f}'.format(kabam_obj.out_db51), '{0:.2f}'.format(kabam_obj.out_db52),
                                '{0:.2f}'.format(kabam_obj.out_db53), '{0:.2f}'.format(kabam_obj.out_db54), '{0:.2f}'.format(kabam_obj.out_db55),
                                '{0:.2f}'.format(kabam_obj.out_db5a0), '{0:.2f}'.format(kabam_obj.out_db5a1), '{0:.2f}'.format(kabam_obj.out_db5a2),
                                '{0:.2f}'.format(kabam_obj.out_db5a3), '{0:.2f}'.format(kabam_obj.out_db5a4), '{0:.2f}'.format(kabam_obj.out_db5a5)],
    }
    return data


def gett5dataqaqc(kabam_obj):
    data = {
        "Wildlife Species": ['fog/water shrew', 'Expected fog/water shrew', 'rice rate/star nosed mole',
                             'Expected rice rate/star nosed mole', 'small mink', 'Expected small mink', 'large mink',
                             'Expected large mink', 'small river otter', 'Expected small river otter',
                             'large river otter', 'Expected large river otter', 'sandpipers', 'Expected sandpipers',
                             'cranes', 'Expected cranes', 'rails', 'Expected rails', 'herons', 'Expected herons',
                             'small osprey', 'Expected small osprey', 'white pelican', 'Expected white pelican'],
        "Body Weight (kg)": ['{0:.2f}'.format(kabam_obj.out_mweight0), '{0:.2f}'.format(kabam_obj.out_mweight0_exp),
                             '{0:.2f}'.format(kabam_obj.out_mweight1), '{0:.2f}'.format(kabam_obj.out_mweight1_exp),
                             '{0:.2f}'.format(kabam_obj.out_mweight2), '{0:.2f}'.format(kabam_obj.out_mweight2_exp),
                             '{0:.2f}'.format(kabam_obj.out_mweight3), '{0:.2f}'.format(kabam_obj.out_mweight3_exp),
                             '{0:.2f}'.format(kabam_obj.out_mweight4), '{0:.2f}'.format(kabam_obj.out_mweight4_exp),
                             '{0:.2f}'.format(kabam_obj.out_mweight5), '{0:.2f}'.format(kabam_obj.out_mweight5_exp),
                             '{0:.2f}'.format(kabam_obj.out_aweight0), '{0:.2f}'.format(kabam_obj.out_aweight0_exp),
                             '{0:.2f}'.format(kabam_obj.out_aweight1), '{0:.2f}'.format(kabam_obj.out_aweight1_exp),
                             '{0:.2f}'.format(kabam_obj.out_aweight2), '{0:.2f}'.format(kabam_obj.out_aweight2_exp),
                             '{0:.2f}'.format(kabam_obj.out_aweight3), '{0:.2f}'.format(kabam_obj.out_aweight3_exp),
                             '{0:.2f}'.format(kabam_obj.out_aweight4), '{0:.2f}'.format(kabam_obj.out_aweight4_exp),
                             '{0:.2f}'.format(kabam_obj.out_aweight5), '{0:.2f}'.format(kabam_obj.out_aweight5_exp)],
        "Dry Food Ingestion Rate (kg-dry food/kg-bw/day)": ['{0:.3f}'.format(kabam_obj.out_dfir0), '{0:.3f}'.format(kabam_obj.out_dfir0_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir1), '{0:.3f}'.format(kabam_obj.out_dfir1_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir2), '{0:.3f}'.format(kabam_obj.out_dfir2_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir3), '{0:.3f}'.format(kabam_obj.out_dfir3_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir4), '{0:.3f}'.format(kabam_obj.out_dfir4_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfir5), '{0:.3f}'.format(kabam_obj.out_dfir5_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira0),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira0_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira1),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira1_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira2),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira2_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira3),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira3_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira4),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira4_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira5),
                                                            '{0:.3f}'.format(kabam_obj.out_dfira5_exp)],
        "Wet Food Ingestion Rate (kg-wet food/kg-bw/day)": ['{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m0),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m0_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m1),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m1_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m2),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m2_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m3),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m3_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m4),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m4_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m5),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_m5_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a0),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a0_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a1),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a1_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a2),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a2_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a3),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a3_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a4),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a4_exp),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a5),
                                                            '{0:.3f}'.format(kabam_obj.out_wet_food_ingestion_a5_exp)],
        "Drinking Water Intake (L/d)": ['{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m0),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m0_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m1),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m1_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m2),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m2_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m3),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m3_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m4),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m4_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m5),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_m5_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a0),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a0_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a1),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a1_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a2),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a2_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a3),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a3_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a4),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a4_exp),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a5),
                                        '{0:.3f}'.format(kabam_obj.out_drinking_water_intake_a5_exp)],
        "Dose Based (mg/kg-bw/d)": ['{0:.3f}'.format(kabam_obj.out_db40), '{0:.3f}'.format(kabam_obj.out_db40_exp),
                                    '{0:.3f}'.format(kabam_obj.out_db41), '{0:.3f}'.format(kabam_obj.out_db41_exp),
                                    '{0:.3f}'.format(kabam_obj.out_db42), '{0:.3f}'.format(kabam_obj.out_db42_exp),
                                    '{0:.3f}'.format(kabam_obj.out_db43), '{0:.3f}'.format(kabam_obj.out_db43_exp),
                                    '{0:.3f}'.format(kabam_obj.out_db44), '{0:.3f}'.format(kabam_obj.out_db44_exp),
                                    '{0:.3f}'.format(kabam_obj.out_db45), '{0:.3f}'.format(kabam_obj.out_db45_exp),
                                    '{0:.4f}'.format(kabam_obj.out_db4a0), '{0:.4f}'.format(kabam_obj.out_db4a0_exp),
                                    '{0:.4f}'.format(kabam_obj.out_db4a1), '{0:.4f}'.format(kabam_obj.out_db4a1_exp),
                                    '{0:.4f}'.format(kabam_obj.out_db4a2), '{0:.4f}'.format(kabam_obj.out_db4a2_exp),
                                    '{0:.4f}'.format(kabam_obj.out_db4a3), '{0:.4f}'.format(kabam_obj.out_db4a3_exp),
                                    '{0:.4f}'.format(kabam_obj.out_db4a4), '{0:.4f}'.format(kabam_obj.out_db4a4_exp),
                                    '{0:.4f}'.format(kabam_obj.out_db4a5), '{0:.4f}'.format(kabam_obj.out_db4a5_exp)],
        "Dietary Based (ppm)": ['{0:.2f}'.format(kabam_obj.out_db50), '{0:.2f}'.format(kabam_obj.out_db50_exp), '{0:.2f}'.format(kabam_obj.out_db51),
                                '{0:.2f}'.format(kabam_obj.out_db51_exp), '{0:.2f}'.format(kabam_obj.out_db52), '{0:.2f}'.format(kabam_obj.out_db52_exp),
                                '{0:.2f}'.format(kabam_obj.out_db53), '{0:.2f}'.format(kabam_obj.out_db53_exp), '{0:.2f}'.format(kabam_obj.out_db54),
                                '{0:.2f}'.format(kabam_obj.out_db54_exp), '{0:.2f}'.format(kabam_obj.out_db55), '{0:.2f}'.format(kabam_obj.out_db55_exp),
                                '{0:.2f}'.format(kabam_obj.out_db5a0), '{0:.2f}'.format(kabam_obj.out_db5a0_exp), '{0:.2f}'.format(kabam_obj.out_db5a1),
                                '{0:.2f}'.format(kabam_obj.out_db5a1_exp), '{0:.2f}'.format(kabam_obj.out_db5a2), '{0:.2f}'.format(kabam_obj.out_db5a2_exp),
                                '{0:.2f}'.format(kabam_obj.out_db5a3), '{0:.2f}'.format(kabam_obj.out_db5a3_exp), '{0:.2f}'.format(kabam_obj.out_db5a4),
                                '{0:.2f}'.format(kabam_obj.out_db5a4_exp), '{0:.2f}'.format(kabam_obj.out_db5a5), '{0:.2f}'.format(kabam_obj.out_db5a5_exp)],
    }
    return data


def gett6data(kabam_obj):
    data = {
        "Wildlife Species": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink',
                             'small river otter', 'large river otter', 'sandpipers', 'cranes', 'rails', 'herons',
                             'small osprey', 'white pelican'],
        "Acute Dose Based (mg/kg-bw)": ['{0:.2f}'.format(kabam_obj.out_acute_dose_based_m0),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m1),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m2),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m3),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m4),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m5),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a0),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a1),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a2),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a3),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a4),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a5)],
        "Acute Dietary Based (mg/kg-diet)": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50)],
        "Chronic Dose Based (mg/kg-bw)": ['{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m0),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m1),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m2),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m3),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m4),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m5), 'N/A', 'N/A', 'N/A', 'N/A',
                                          'N/A', 'N/A'],
        "Chronic Dietary Based (mg/kg-diet)": ['{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec)],
    }
    return data


def gett6dataqaqc(kabam_obj):
    data = {
        "Wildlife Species": ['fog/water shrew', 'Expected fog/water shrew', 'rice rate/star nosed mole',
                             'Expected rice rate/star nosed mole', 'small mink', 'Expected small mink', 'large mink',
                             'Expected large mink', 'small river otter', 'Expected small river otter',
                             'large river otter', 'Expected large river otter', 'sandpipers', 'Expected sandpipers',
                             'cranes', 'Expected cranes', 'rails', 'Expected rails', 'herons', 'Expected herons',
                             'small osprey', 'Expected small osprey', 'white pelican', 'Expected white pelican'],
        "Acute Dose Based (mg/kg-bw)": ['{0:.2f}'.format(kabam_obj.out_acute_dose_based_m0),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m0_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m1),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m1_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m2),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m2_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m3),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m3_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m4),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m4_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m5),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_m5_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a0),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a0_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a1),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a1_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a2),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a2_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a3),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a3_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a4),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a4_exp),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a5),
                                        '{0:.2f}'.format(kabam_obj.out_acute_dose_based_a5_exp)],
        "Acute Dietary Based (mg/kg-diet)": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                                             'N/A', 'N/A', '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50_exp), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50_exp), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50_exp), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50_exp), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50_exp), '{0:.2f}'.format(kabam_obj.avian_lc50),
                                             '{0:.2f}'.format(kabam_obj.avian_lc50_exp)],
        "Chronic Dose Based (mg/kg-bw)": ['{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m0),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m0_exp),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m1),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m1_exp),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m2),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m2_exp),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m3),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m3_exp),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m4),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m4_exp),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m5),
                                          '{0:.2f}'.format(kabam_obj.out_chronic_dose_based_m5_exp), 'N/A', 'N/A', 'N/A', 'N/A',
                                          'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        "Chronic Dietary Based (mg/kg-diet)": ['{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint_exp),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint_exp),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint_exp),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint_exp),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint_exp),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint),
                                               '{0:.0f}'.format(kabam_obj.mammalian_chronic_endpoint_exp),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec_exp),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec_exp),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec_exp),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec_exp),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec_exp),
                                               '{0:.0f}'.format(kabam_obj.avian_noaec), '{0:.0f}'.format(kabam_obj.avian_noaec_exp)],
    }
    return data


def gett7data(kabam_obj):
    data = {
        "Wildlife Species": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink',
                             'small river otter', 'large river otter', 'sandpipers', 'cranes', 'rails', 'herons',
                             'small osprey', 'white pelican'],
        "Acute Dose Based": ['{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m0), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m1),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m2), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m3),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m4), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m5),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a0), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a1),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a2), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a3),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a4), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a5)],
        "Acute Dietary Based": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a0),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a1), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a2),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a3), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a4),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a5)],
        "Chronic Dose Based": ['{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m0), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m1),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m2), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m3),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m4), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m5),
                               'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        "Chronic Dietary Based": ['{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m0), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m1),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m2), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m3),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m4), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m5),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a0), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a1),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a2), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a3),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a4), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a5)],
    }
    return data


def gett7dataqaqc(kabam_obj):
    data = {
        "Wildlife Species": ['fog/water shrew', 'Expected fog/water shrew', 'rice rate/star nosed mole',
                             'Expected rice rate/star nosed mole', 'small mink', 'Expected small mink', 'large mink',
                             'Expected large mink', 'small river otter', 'Expected small river otter',
                             'large river otter', 'Expected large river otter', 'sandpipers', 'Expected sandpipers',
                             'cranes', 'Expected cranes', 'rails', 'Expected rails', 'herons', 'Expected herons',
                             'small osprey', 'Expected small osprey', 'white pelican', 'Expected white pelican'],
        "Acute Dose Based": ['{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m0), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m0_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m1), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m1_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m2), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m2_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m3), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m3_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m4), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m4_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m5), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_m5_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a0), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a0_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a1), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a1_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a2), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a2_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a3), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a3_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a4), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a4_exp),
                             '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a5), '{0:.3f}'.format(kabam_obj.out_acute_rq_dose_a5_exp)],
        "Acute Dietary Based": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a0), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a0_exp),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a1), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a1_exp),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a2), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a2_exp),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a3), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a3_exp),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a4), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a4_exp),
                                '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a5), '{0:.3f}'.format(kabam_obj.out_acute_rq_diet_a5_exp)],
        "Chronic Dose Based": ['{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m0), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m0_exp),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m1), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m1_exp),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m2), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m2_exp),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m3), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m3_exp),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m4), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m4_exp),
                               '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m5), '{0:.3f}'.format(kabam_obj.out_chronic_rq_dose_m5_exp),
                               'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        "Chronic Dietary Based": ['{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m0), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m0_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m1), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m1_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m2), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m2_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m3), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m3_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m4), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m4_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m5), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_m5_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a0), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a0_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a1), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a1_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a2), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a2_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a3), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a3_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a4), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a4_exp),
                                  '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a5), '{0:.3f}'.format(kabam_obj.out_chronic_rq_diet_a5_exp)],
    }
    return data


def gettsumdata(l_kow, k_oc, c_wdp, water_column_EEC, mineau, x_poc, x_doc, c_ox, w_t, c_ss, oc, k_ow,
                bw_quail, bw_duck, bwb_other, avian_ld50, avian_lc50, avian_noaec, bw_rat, bwm_other, mammalian_ld50,
                mammalian_lc50, mammalian_chronic_endpoint):
    data = {
        "Parameter": [mark_safe('Log K<sub>OW</sub>'), mark_safe('K<sub>OC</sub>'), 'Pore water (benthic) EEC',
                      'Water column 1 in 10yr EEC', 'Mineau scaling factor', mark_safe('X<sub>POC</sub>'),
                      mark_safe('X<sub>DOC</sub>'), mark_safe('C<sub>OX</sub>'), mark_safe('Water Temperature'),
                      mark_safe('C<sub>SS</sub>'), 'OC', mark_safe('K<sub>OW</sub>'),
                      'BW Quail', 'BW Duck', 'BW Bird Other', mark_safe('Avian LD<sub>50</sub>'),
                      mark_safe('Avian LC<sub>50</sub>'), 'Avian NOAEC', 'BW Rat', 'BW Mammal Other',
                      mark_safe('Mammalian LD<sub>50</sub>'), mark_safe('Mammalian LC<sub>50</sub>'),
                      'Mammalian Chronic Endpoint'],

        "Mean": ['{0:.1f}'.format(np.mean(l_kow)), '{0:.1f}'.format(np.mean(k_oc)), '{0:.1f}'.format(np.mean(c_wdp)),
                 '{0:.1f}'.format(np.mean(water_column_EEC)), '{0:.1f}'.format(np.mean(mineau)), '{0:.1f}'.format(np.mean(x_poc)),
                 '{0:.1f}'.format(np.mean(x_doc)), '{0:.1f}'.format(np.mean(c_ox)), '{0:.1f}'.format(np.mean(w_t)), '{0:.1f}'.format(np.mean(c_ss)),
                 '{0:.1f}'.format(np.mean(oc)), '{0:.1f}'.format(np.mean(k_ow)),
                 '{0:.1f}'.format(np.mean(bw_quail)), '{0:.1f}'.format(np.mean(bw_duck)), '{0:.1f}'.format(np.mean(bwb_other)),
                 '{0:.1f}'.format(np.mean(avian_ld50)), '{0:.1f}'.format(np.mean(avian_lc50)), '{0:.1f}'.format(np.mean(avian_noaec)),
                 '{0:.1f}'.format(np.mean(bw_rat)), '{0:.1f}'.format(np.mean(bwm_other)), '{0:.1f}'.format(np.mean(mammalian_ld50)),
                 '{0:.1f}'.format(np.mean(mammalian_lc50)), '{0:.1f}'.format(np.mean(mammalian_chronic_endpoint))],

        "Std": ['{0:.1f}'.format(np.std(l_kow)), '{0:.1f}'.format(np.std(k_oc)), '{0:.1f}'.format(np.std(c_wdp)),
                '{0:.1f}'.format(np.std(water_column_EEC)), '{0:.1f}'.format(np.std(mineau)), '{0:.1f}'.format(np.std(x_poc)),
                '{0:.1f}'.format(np.std(x_doc)), '{0:.1f}'.format(np.std(c_ox)), '{0:.1f}'.format(np.std(w_t)), '{0:.1f}'.format(np.std(c_ss)),
                '{0:.1f}'.format(np.std(oc)), '{0:.1f}'.format(np.std(k_ow)),
                '{0:.1f}'.format(np.std(bw_quail)), '{0:.1f}'.format(np.std(bw_duck)), '{0:.1f}'.format(np.std(bwb_other)),
                '{0:.1f}'.format(np.std(avian_ld50)), '{0:.1f}'.format(np.std(avian_lc50)), '{0:.1f}'.format(np.std(avian_noaec)),
                '{0:.1f}'.format(np.std(bw_rat)), '{0:.1f}'.format(np.std(bwm_other)), '{0:.1f}'.format(np.std(mammalian_ld50)),
                '{0:.1f}'.format(np.std(mammalian_lc50)), '{0:.1f}'.format(np.std(mammalian_chronic_endpoint))],

        "Min": ['{0:.1f}'.format(np.min(l_kow)), '{0:.1f}'.format(np.min(k_oc)), '{0:.1f}'.format(np.min(c_wdp)),
                '{0:.1f}'.format(np.min(water_column_EEC)), '{0:.1f}'.format(np.min(mineau)), '{0:.1f}'.format(np.min(x_poc)),
                '{0:.1f}'.format(np.min(x_doc)), '{0:.1f}'.format(np.min(c_ox)), '{0:.1f}'.format(np.min(w_t)), '{0:.1f}'.format(np.min(c_ss)),
                '{0:.1f}'.format(np.min(oc)), '{0:.1f}'.format(np.min(k_ow)),
                '{0:.1f}'.format(np.min(bw_quail)), '{0:.1f}'.format(np.min(bw_duck)), '{0:.1f}'.format(np.min(bwb_other)),
                '{0:.1f}'.format(np.min(avian_ld50)), '{0:.1f}'.format(np.min(avian_lc50)), '{0:.1f}'.format(np.min(avian_noaec)),
                '{0:.1f}'.format(np.min(bw_rat)), '{0:.1f}'.format(np.min(bwm_other)), '{0:.1f}'.format(np.min(mammalian_ld50)),
                '{0:.1f}'.format(np.min(mammalian_lc50)), '{0:.1f}'.format(np.min(mammalian_chronic_endpoint))],

        "Max": ['{0:.1f}'.format(np.max(l_kow)), '{0:.1f}'.format(np.max(k_oc)), '{0:.1f}'.format(np.max(c_wdp)),
                '{0:.1f}'.format(np.max(water_column_EEC)), '{0:.1f}'.format(np.max(mineau)), '{0:.1f}'.format(np.max(x_poc)),
                '{0:.1f}'.format(np.max(x_doc)), '{0:.1f}'.format(np.max(c_ox)), '{0:.1f}'.format(np.max(w_t)), '{0:.1f}'.format(np.max(c_ss)),
                '{0:.1f}'.format(np.max(oc)), '{0:.1f}'.format(np.max(k_ow)),
                '{0:.1f}'.format(np.max(bw_quail)), '{0:.1f}'.format(np.max(bw_duck)), '{0:.1f}'.format(np.max(bwb_other)),
                '{0:.1f}'.format(np.max(avian_ld50)), '{0:.1f}'.format(np.max(avian_lc50)), '{0:.1f}'.format(np.max(avian_noaec)),
                '{0:.1f}'.format(np.max(bw_rat)), '{0:.1f}'.format(np.max(bwm_other)), '{0:.1f}'.format(np.max(mammalian_ld50)),
                '{0:.1f}'.format(np.max(mammalian_lc50)), '{0:.1f}'.format(np.max(mammalian_chronic_endpoint))],

        "Unit": ['', '', mark_safe('&#956;g/L'), mark_safe('&#956;g/L'), '', 'kg OC/L', 'kg OC/L',
                 mark_safe('mg O<sup>2</sup>/L'), mark_safe('&#176;C'), 'kg/L', '%', '', 'g', 'g', 'g', 'mg/kg-bw',
                 'mg/kg-diet', 'mg/kg-diet', 'g', 'g', 'mg/kg-bw', 'mg/kg-diet', 'ppm']
    }
    return data


def gettsumdata_out1(acute_dose_based_m_array, acute_dose_based_a_array):
    acute_dose_based_m_avg = np.mean(acute_dose_based_m_array, axis=0)
    acute_dose_based_m_std = np.std(acute_dose_based_m_array, axis=0)
    acute_dose_based_m_min = np.min(acute_dose_based_m_array, axis=0)
    acute_dose_based_m_max = np.max(acute_dose_based_m_array, axis=0)
    acute_dose_based_a_avg = np.mean(acute_dose_based_a_array, axis=0)
    acute_dose_based_a_std = np.std(acute_dose_based_a_array, axis=0)
    acute_dose_based_a_min = np.min(acute_dose_based_a_array, axis=0)
    acute_dose_based_a_max = np.max(acute_dose_based_a_array, axis=0)
    data = {
        "Parameter": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink', 'small river otter',
                      'large river otter', 'sandpipers', 'cranes', 'rails', 'herons', 'small osprey', 'white pelican'],

        "Mean": ['{0:.3f}'.format(acute_dose_based_m_avg[0]), '{0:.3f}'.format(acute_dose_based_m_avg[1]),
                 '{0:.3f}'.format(acute_dose_based_m_avg[2]), '{0:.3f}'.format(acute_dose_based_m_avg[3]),
                 '{0:.3f}'.format(acute_dose_based_m_avg[4]), '{0:.3f}'.format(acute_dose_based_m_avg[5]),
                 '{0:.3f}'.format(acute_dose_based_a_avg[0]), '{0:.3f}'.format(acute_dose_based_a_avg[1]),
                 '{0:.3f}'.format(acute_dose_based_a_avg[2]), '{0:.3f}'.format(acute_dose_based_a_avg[3]),
                 '{0:.3f}'.format(acute_dose_based_a_avg[4]), '{0:.3f}'.format(acute_dose_based_a_avg[5]),
                 ],

        "Std": ['{0:.3f}'.format(acute_dose_based_m_std[0]), '{0:.3f}'.format(acute_dose_based_m_std[1]),
                '{0:.3f}'.format(acute_dose_based_m_std[2]), '{0:.3f}'.format(acute_dose_based_m_std[3]),
                '{0:.3f}'.format(acute_dose_based_m_std[4]), '{0:.3f}'.format(acute_dose_based_m_std[5]),
                '{0:.3f}'.format(acute_dose_based_a_std[0]), '{0:.3f}'.format(acute_dose_based_a_std[1]),
                '{0:.3f}'.format(acute_dose_based_a_std[2]), '{0:.3f}'.format(acute_dose_based_a_std[3]),
                '{0:.3f}'.format(acute_dose_based_a_std[4]), '{0:.3f}'.format(acute_dose_based_a_std[5]),
                ],

        "Min": ['{0:.3f}'.format(acute_dose_based_m_min[0]), '{0:.3f}'.format(acute_dose_based_m_min[1]),
                '{0:.3f}'.format(acute_dose_based_m_min[2]), '{0:.3f}'.format(acute_dose_based_m_min[3]),
                '{0:.3f}'.format(acute_dose_based_m_min[4]), '{0:.3f}'.format(acute_dose_based_m_min[5]),
                '{0:.3f}'.format(acute_dose_based_a_min[0]), '{0:.3f}'.format(acute_dose_based_a_min[1]),
                '{0:.3f}'.format(acute_dose_based_a_min[2]), '{0:.3f}'.format(acute_dose_based_a_min[3]),
                '{0:.3f}'.format(acute_dose_based_a_min[4]), '{0:.3f}'.format(acute_dose_based_a_min[5]),
                ],

        "Max": ['{0:.3f}'.format(acute_dose_based_m_max[0]), '{0:.3f}'.format(acute_dose_based_m_max[1]),
                '{0:.3f}'.format(acute_dose_based_m_max[2]), '{0:.3f}'.format(acute_dose_based_m_max[3]),
                '{0:.3f}'.format(acute_dose_based_m_max[4]), '{0:.3f}'.format(acute_dose_based_m_max[5]),
                '{0:.3f}'.format(acute_dose_based_a_max[0]), '{0:.3f}'.format(acute_dose_based_a_max[1]),
                '{0:.3f}'.format(acute_dose_based_a_max[2]), '{0:.3f}'.format(acute_dose_based_a_max[3]),
                '{0:.3f}'.format(acute_dose_based_a_max[4]), '{0:.3f}'.format(acute_dose_based_a_max[5]),
                ]
    }
    return data


def gettsumdata_out2(chronic_dose_based_m_array):
    chronic_dose_based_m_avg = np.mean(chronic_dose_based_m_array, axis=0)
    chronic_dose_based_m_std = np.std(chronic_dose_based_m_array, axis=0)
    chronic_dose_based_m_min = np.min(chronic_dose_based_m_array, axis=0)
    chronic_dose_based_m_max = np.max(chronic_dose_based_m_array, axis=0)
    data = {
        "Parameter": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink', 'small river otter',
                      'large river otter', 'sandpipers', 'cranes', 'rails', 'herons', 'small osprey', 'white pelican'],

        "Mean": ['{0:.3f}'.format(chronic_dose_based_m_avg[0]), '{0:.3f}'.format(chronic_dose_based_m_avg[1]),
                 '{0:.3f}'.format(chronic_dose_based_m_avg[2]), '{0:.3f}'.format(chronic_dose_based_m_avg[3]),
                 '{0:.3f}'.format(chronic_dose_based_m_avg[4]), '{0:.3f}'.format(chronic_dose_based_m_avg[5]),
                 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                 ],

        "Std": ['{0:.3f}'.format(chronic_dose_based_m_std[0]), '{0:.3f}'.format(chronic_dose_based_m_std[1]),
                '{0:.3f}'.format(chronic_dose_based_m_std[2]), '{0:.3f}'.format(chronic_dose_based_m_std[3]),
                '{0:.3f}'.format(chronic_dose_based_m_std[4]), '{0:.3f}'.format(chronic_dose_based_m_std[5]),
                'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                ],

        "Min": ['{0:.3f}'.format(chronic_dose_based_m_min[0]), '{0:.3f}'.format(chronic_dose_based_m_min[1]),
                '{0:.3f}'.format(chronic_dose_based_m_min[2]), '{0:.3f}'.format(chronic_dose_based_m_min[3]),
                '{0:.3f}'.format(chronic_dose_based_m_min[4]), '{0:.3f}'.format(chronic_dose_based_m_min[5]),
                'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                ],

        "Max": ['{0:.3f}'.format(chronic_dose_based_m_max[0]), '{0:.3f}'.format(chronic_dose_based_m_max[1]),
                '{0:.3f}'.format(chronic_dose_based_m_max[2]), '{0:.3f}'.format(chronic_dose_based_m_max[3]),
                '{0:.3f}'.format(chronic_dose_based_m_max[4]), '{0:.3f}'.format(chronic_dose_based_m_max[5]),
                'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                ]
    }
    return data


def gettsumdata_out3(acute_rq_dose_m_array, acute_rq_dose_a_array):
    acute_rq_dose_m_avg = np.mean(acute_rq_dose_m_array, axis=0)
    acute_rq_dose_m_std = np.std(acute_rq_dose_m_array, axis=0)
    acute_rq_dose_m_min = np.min(acute_rq_dose_m_array, axis=0)
    acute_rq_dose_m_max = np.max(acute_rq_dose_m_array, axis=0)
    acute_rq_dose_a_avg = np.mean(acute_rq_dose_a_array, axis=0)
    acute_rq_dose_a_std = np.std(acute_rq_dose_a_array, axis=0)
    acute_rq_dose_a_min = np.min(acute_rq_dose_a_array, axis=0)
    acute_rq_dose_a_max = np.max(acute_rq_dose_a_array, axis=0)
    data = {
        "Parameter": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink', 'small river otter',
                      'large river otter', 'sandpipers', 'cranes', 'rails', 'herons', 'small osprey', 'white pelican'],

        "Mean": ['{0:.3f}'.format(acute_rq_dose_m_avg[0]), '{0:.3f}'.format(acute_rq_dose_m_avg[1]), '{0:.3f}'.format(acute_rq_dose_m_avg[2]),
                 '{0:.3f}'.format(acute_rq_dose_m_avg[3]), '{0:.3f}'.format(acute_rq_dose_m_avg[4]), '{0:.3f}'.format(acute_rq_dose_m_avg[5]),
                 '{0:.3f}'.format(acute_rq_dose_a_avg[0]), '{0:.3f}'.format(acute_rq_dose_a_avg[1]), '{0:.3f}'.format(acute_rq_dose_a_avg[2]),
                 '{0:.3f}'.format(acute_rq_dose_a_avg[3]), '{0:.3f}'.format(acute_rq_dose_a_avg[4]), '{0:.3f}'.format(acute_rq_dose_a_avg[5]),
                 ],

        "Std": ['{0:.3f}'.format(acute_rq_dose_m_std[0]), '{0:.3f}'.format(acute_rq_dose_m_std[1]), '{0:.3f}'.format(acute_rq_dose_m_std[2]),
                '{0:.3f}'.format(acute_rq_dose_m_std[3]), '{0:.3f}'.format(acute_rq_dose_m_std[4]), '{0:.3f}'.format(acute_rq_dose_m_std[5]),
                '{0:.3f}'.format(acute_rq_dose_a_std[0]), '{0:.3f}'.format(acute_rq_dose_a_std[1]), '{0:.3f}'.format(acute_rq_dose_a_std[2]),
                '{0:.3f}'.format(acute_rq_dose_a_std[3]), '{0:.3f}'.format(acute_rq_dose_a_std[4]), '{0:.3f}'.format(acute_rq_dose_a_std[5]),
                ],

        "Min": ['{0:.3f}'.format(acute_rq_dose_m_min[0]), '{0:.3f}'.format(acute_rq_dose_m_min[1]), '{0:.3f}'.format(acute_rq_dose_m_min[2]),
                '{0:.3f}'.format(acute_rq_dose_m_min[3]), '{0:.3f}'.format(acute_rq_dose_m_min[4]), '{0:.3f}'.format(acute_rq_dose_m_min[5]),
                '{0:.3f}'.format(acute_rq_dose_a_min[0]), '{0:.3f}'.format(acute_rq_dose_a_min[1]), '{0:.3f}'.format(acute_rq_dose_a_min[2]),
                '{0:.3f}'.format(acute_rq_dose_a_min[3]), '{0:.3f}'.format(acute_rq_dose_a_min[4]), '{0:.3f}'.format(acute_rq_dose_a_min[5]),
                ],

        "Max": ['{0:.3f}'.format(acute_rq_dose_m_max[0]), '{0:.3f}'.format(acute_rq_dose_m_max[1]), '{0:.3f}'.format(acute_rq_dose_m_max[2]),
                '{0:.3f}'.format(acute_rq_dose_m_max[3]), '{0:.3f}'.format(acute_rq_dose_m_max[4]), '{0:.3f}'.format(acute_rq_dose_m_max[5]),
                '{0:.3f}'.format(acute_rq_dose_a_max[0]), '{0:.3f}'.format(acute_rq_dose_a_max[1]), '{0:.3f}'.format(acute_rq_dose_a_max[2]),
                '{0:.3f}'.format(acute_rq_dose_a_max[3]), '{0:.3f}'.format(acute_rq_dose_a_max[4]), '{0:.3f}'.format(acute_rq_dose_a_max[5]),
                ]
    }
    return data


def gettsumdata_out4(acute_rq_diet_a_array):
    acute_rq_diet_a_avg = np.mean(acute_rq_diet_a_array, axis=0)
    acute_rq_diet_a_std = np.std(acute_rq_diet_a_array, axis=0)
    acute_rq_diet_a_min = np.min(acute_rq_diet_a_array, axis=0)
    acute_rq_diet_a_max = np.max(acute_rq_diet_a_array, axis=0)
    data = {
        "Parameter": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink', 'small river otter',
                      'large river otter', 'sandpipers', 'cranes', 'rails', 'herons', 'small osprey', 'white pelican'],

        "Mean": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                 '{0:.3f}'.format(acute_rq_diet_a_avg[0]), '{0:.3f}'.format(acute_rq_diet_a_avg[1]), '{0:.3f}'.format(acute_rq_diet_a_avg[2]),
                 '{0:.3f}'.format(acute_rq_diet_a_avg[3]), '{0:.3f}'.format(acute_rq_diet_a_avg[4]), '{0:.3f}'.format(acute_rq_diet_a_avg[5]),
                 ],

        "Std": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                '{0:.3f}'.format(acute_rq_diet_a_std[0]), '{0:.3f}'.format(acute_rq_diet_a_std[1]), '{0:.3f}'.format(acute_rq_diet_a_std[2]),
                '{0:.3f}'.format(acute_rq_diet_a_std[3]), '{0:.3f}'.format(acute_rq_diet_a_std[4]), '{0:.3f}'.format(acute_rq_diet_a_std[5]),
                ],

        "Min": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                '{0:.3f}'.format(acute_rq_diet_a_min[0]), '{0:.3f}'.format(acute_rq_diet_a_min[1]), '{0:.3f}'.format(acute_rq_diet_a_min[2]),
                '{0:.3f}'.format(acute_rq_diet_a_min[3]), '{0:.3f}'.format(acute_rq_diet_a_min[4]), '{0:.3f}'.format(acute_rq_diet_a_min[5]),
                ],

        "Max": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
                '{0:.3f}'.format(acute_rq_diet_a_max[0]), '{0:.3f}'.format(acute_rq_diet_a_max[1]), '{0:.3f}'.format(acute_rq_diet_a_max[2]),
                '{0:.3f}'.format(acute_rq_diet_a_max[3]), '{0:.3f}'.format(acute_rq_diet_a_max[4]), '{0:.3f}'.format(acute_rq_diet_a_max[5]),
                ]
    }
    return data


def gettsumdata_out5(chronic_rq_dose_m_array):
    chronic_rq_dose_m_avg = np.mean(chronic_rq_dose_m_array, axis=0)
    chronic_rq_dose_m_std = np.std(chronic_rq_dose_m_array, axis=0)
    chronic_rq_dose_m_min = np.min(chronic_rq_dose_m_array, axis=0)
    chronic_rq_dose_m_max = np.max(chronic_rq_dose_m_array, axis=0)
    data = {
        "Parameter": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink', 'small river otter',
                      'large river otter', 'sandpipers', 'cranes', 'rails', 'herons', 'small osprey', 'white pelican'],

        "Mean": ['{0:.3f}'.format(chronic_rq_dose_m_avg[0]), '{0:.3f}'.format(chronic_rq_dose_m_avg[1]),
                 '{0:.3f}'.format(chronic_rq_dose_m_avg[2]), '{0:.3f}'.format(chronic_rq_dose_m_avg[3]),
                 '{0:.3f}'.format(chronic_rq_dose_m_avg[4]), '{0:.3f}'.format(chronic_rq_dose_m_avg[5]),
                 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                 ],

        "Std": ['{0:.3f}'.format(chronic_rq_dose_m_std[0]), '{0:.3f}'.format(chronic_rq_dose_m_std[1]), '{0:.3f}'.format(chronic_rq_dose_m_std[2]),
                '{0:.3f}'.format(chronic_rq_dose_m_std[3]), '{0:.3f}'.format(chronic_rq_dose_m_std[4]), '{0:.3f}'.format(chronic_rq_dose_m_std[5]),
                'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                ],

        "Min": ['{0:.3f}'.format(chronic_rq_dose_m_min[0]), '{0:.3f}'.format(chronic_rq_dose_m_min[1]), '{0:.3f}'.format(chronic_rq_dose_m_min[2]),
                '{0:.3f}'.format(chronic_rq_dose_m_min[3]), '{0:.3f}'.format(chronic_rq_dose_m_min[4]), '{0:.3f}'.format(chronic_rq_dose_m_min[5]),
                'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                ],

        "Max": ['{0:.3f}'.format(chronic_rq_dose_m_max[0]), '{0:.3f}'.format(chronic_rq_dose_m_max[1]), '{0:.3f}'.format(chronic_rq_dose_m_max[2]),
                '{0:.3f}'.format(chronic_rq_dose_m_max[3]), '{0:.3f}'.format(chronic_rq_dose_m_max[4]), '{0:.3f}'.format(chronic_rq_dose_m_max[5]),
                'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                ]
    }
    return data


def gettsumdata_out6(chronic_rq_diet_m_array, chronic_rq_diet_a_array):
    chronic_rq_diet_m_avg = np.mean(chronic_rq_diet_m_array, axis=0)
    chronic_rq_diet_m_std = np.std(chronic_rq_diet_m_array, axis=0)
    chronic_rq_diet_m_min = np.min(chronic_rq_diet_m_array, axis=0)
    chronic_rq_diet_m_max = np.max(chronic_rq_diet_m_array, axis=0)
    chronic_rq_diet_a_avg = np.mean(chronic_rq_diet_a_array, axis=0)
    chronic_rq_diet_a_std = np.std(chronic_rq_diet_a_array, axis=0)
    chronic_rq_diet_a_min = np.min(chronic_rq_diet_a_array, axis=0)
    chronic_rq_diet_a_max = np.max(chronic_rq_diet_a_array, axis=0)
    data = {
        "Parameter": ['fog/water shrew', 'rice rate/star nosed mole', 'small mink', 'large mink', 'small river otter',
                      'large river otter', 'sandpipers', 'cranes', 'rails', 'herons', 'small osprey', 'white pelican'],

        "Mean": ['{0:.3f}'.format(chronic_rq_diet_m_avg[0]), '{0:.3f}'.format(chronic_rq_diet_m_avg[1]),
                 '{0:.3f}'.format(chronic_rq_diet_m_avg[2]), '{0:.3f}'.format(chronic_rq_diet_m_avg[3]),
                 '{0:.3f}'.format(chronic_rq_diet_m_avg[4]), '{0:.3f}'.format(chronic_rq_diet_m_avg[5]),
                 '{0:.3f}'.format(chronic_rq_diet_a_avg[0]), '{0:.3f}'.format(chronic_rq_diet_a_avg[1]),
                 '{0:.3f}'.format(chronic_rq_diet_a_avg[2]), '{0:.3f}'.format(chronic_rq_diet_a_avg[3]),
                 '{0:.3f}'.format(chronic_rq_diet_a_avg[4]), '{0:.3f}'.format(chronic_rq_diet_a_avg[5]),
                 ],

        "Std": ['{0:.3f}'.format(chronic_rq_diet_m_std[0]), '{0:.3f}'.format(chronic_rq_diet_m_std[1]), '{0:.3f}'.format(chronic_rq_diet_m_std[2]),
                '{0:.3f}'.format(chronic_rq_diet_m_std[3]), '{0:.3f}'.format(chronic_rq_diet_m_std[4]), '{0:.3f}'.format(chronic_rq_diet_m_std[5]),
                '{0:.3f}'.format(chronic_rq_diet_a_std[0]), '{0:.3f}'.format(chronic_rq_diet_a_std[1]), '{0:.3f}'.format(chronic_rq_diet_a_std[2]),
                '{0:.3f}'.format(chronic_rq_diet_a_std[3]), '{0:.3f}'.format(chronic_rq_diet_a_std[4]), '{0:.3f}'.format(chronic_rq_diet_a_std[5]),
                ],

        "Min": ['{0:.3f}'.format(chronic_rq_diet_m_min[0]), '{0:.3f}'.format(chronic_rq_diet_m_min[1]), '{0:.3f}'.format(chronic_rq_diet_m_min[2]),
                '{0:.3f}'.format(chronic_rq_diet_m_min[3]), '{0:.3f}'.format(chronic_rq_diet_m_min[4]), '{0:.3f}'.format(chronic_rq_diet_m_min[5]),
                '{0:.3f}'.format(chronic_rq_diet_a_min[0]), '{0:.3f}'.format(chronic_rq_diet_a_min[1]), '{0:.3f}'.format(chronic_rq_diet_a_min[2]),
                '{0:.3f}'.format(chronic_rq_diet_a_min[3]), '{0:.3f}'.format(chronic_rq_diet_a_min[4]), '{0:.3f}'.format(chronic_rq_diet_a_min[5]),
                ],

        "Max": ['{0:.3f}'.format(chronic_rq_diet_m_max[0]), '{0:.3f}'.format(chronic_rq_diet_m_max[1]), '{0:.3f}'.format(chronic_rq_diet_m_max[2]),
                '{0:.3f}'.format(chronic_rq_diet_m_max[3]), '{0:.3f}'.format(chronic_rq_diet_m_max[4]), '{0:.3f}'.format(chronic_rq_diet_m_max[5]),
                '{0:.3f}'.format(chronic_rq_diet_a_max[0]), '{0:.3f}'.format(chronic_rq_diet_a_max[1]), '{0:.3f}'.format(chronic_rq_diet_a_max[2]),
                '{0:.3f}'.format(chronic_rq_diet_a_max[3]), '{0:.3f}'.format(chronic_rq_diet_a_max[4]), '{0:.3f}'.format(chronic_rq_diet_a_max[5]),
                ]
    }
    return data


pvuheadings = getheaderpvu()
headerptldr = getheaderptldr()
headerttb = getheaderttb()
headertbbbb = getheadertbbbb()
headerwbdwddd = getheaderwbdwddd()
headerwadadcdcd = getheaderwadadcdcd()
headerwadadcdcd_noUnits = getheaderwadadcdcd_noUnits()
sumheadings = getheadersum()
sumheadings_out = getheadersum_out()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(kabam_obj):
    html_all = table_1(kabam_obj)
    html_all = html_all + table_2(kabam_obj)
    html_all = html_all + table_3(kabam_obj)
    html_all = html_all + table_4(kabam_obj)
    html_all = html_all + table_5(kabam_obj)
    html_all = html_all + table_6(kabam_obj)
    html_all = html_all + table_7(kabam_obj)
    return html_all


def table_all_qaqc(kabam_obj):
    html_all = table_1_qaqc(kabam_obj)
    html_all = html_all + table_2_qaqc(kabam_obj)
    html_all = html_all + table_3_qaqc(kabam_obj)
    html_all = html_all + table_4_qaqc(kabam_obj)
    html_all = html_all + table_5_qaqc(kabam_obj)
    html_all = html_all + table_6_qaqc(kabam_obj)
    html_all = html_all + table_7_qaqc(kabam_obj)
    return html_all


def timestamp(kabam_obj="", batch_jid=""):
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%A, %Y-%B-%d %H:%M:%S')
    if kabam_obj:
        st = datetime.datetime.strptime(kabam_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html = """
    <div class="out_">
        <b>Kabam Version 1.0 (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def table_1(kabam_obj):
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Chemical Information</H4>
                <div class="out_ container_output">
        """
    t1data = gett1data(kabam_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_1_qaqc(kabam_obj):
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Chemical Information</H4>
                <div class="out_ container_output">
        """
    t1data = gett1dataqaqc(kabam_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_2(kabam_obj):
    html = """
        <br>
        <H3 class="out_1 collapsible" id="section1"><span></span>Kabam Output</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Estimated concentrations of {0!s} in ecosystem components</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name))
    t2data = gett2data(kabam_obj)
    t2rows = gethtmlrowsfromcols(t2data, headerptldr)
    html = html + tmpl.render(Context(dict(data=t2rows, headings=headerptldr)))
    html = html + """
                </div>
        """
    return html


def table_2_qaqc(kabam_obj):
    html = """
        <br>
        <H3 class="out_1 collapsible" id="section1"><span></span>Kabam Output</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Estimated concentrations of {0!s} in ecosystem components</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name_exp))
    t2data = gett2dataqaqc(kabam_obj)
    t2rows = gethtmlrowsfromcols(t2data, headerptldr)
    html = html + tmpl.render(Context(dict(data=t2rows, headings=headerptldr)))
    html = html + """
                </div>
        """
    return html


def table_3(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Total BCF and BAF values of {0!s} in Aquatic Trophic Levels</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name))
    t3data = gett3data(kabam_obj)
    t3rows = gethtmlrowsfromcols(t3data, headerttb)
    html = html + tmpl.render(Context(dict(data=t3rows, headings=headerttb)))
    html = html + """
                </div>
        """
    return html


def table_3_qaqc(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Total BCF and BAF values of {0!s} in Aquatic Trophic Levels</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name_exp))
    t3data = gett3dataqaqc(kabam_obj)
    t3rows = gethtmlrowsfromcols(t3data, headerttb)
    html = html + tmpl.render(Context(dict(data=t3rows, headings=headerttb)))
    html = html + """
                </div>
        """
    return html


def table_4(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Lipid-normalized BCF, BAF, BMF, and BSAF values of {0!s} in Aquatic Trophic Levels</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name))
    t4data = gett4data(kabam_obj)
    t4rows = gethtmlrowsfromcols(t4data, headertbbbb)
    html = html + tmpl.render(Context(dict(data=t4rows, headings=headertbbbb)))
    html = html + """
                </div>
        """
    return html


def table_4_qaqc(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Lipid-normalized BCF, BAF, BMF, and BSAF values of {0!s} in Aquatic Trophic Levels</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name_exp))
    t4data = gett4dataqaqc(kabam_obj)
    t4rows = gethtmlrowsfromcols(t4data, headertbbbb)
    html = html + tmpl.render(Context(dict(data=t4rows, headings=headertbbbb)))
    html = html + """
                </div>
        """
    return html


def table_5(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Calculation of EECs for mammals and birds consuming fish contaminated by {0!s}</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name))
    t5data = gett5data(kabam_obj)
    t5rows = gethtmlrowsfromcols(t5data, headerwbdwddd)
    html = html + tmpl.render(Context(dict(data=t5rows, headings=headerwbdwddd)))
    html = html + """
                </div>
        """
    return html


def table_5_qaqc(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Calculation of EECs for mammals and birds consuming fish contaminated by {0!s}</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name_exp))
    t5data = gett5dataqaqc(kabam_obj)
    t5rows = gethtmlrowsfromcols(t5data, headerwbdwddd)
    html = html + tmpl.render(Context(dict(data=t5rows, headings=headerwbdwddd)))
    html = html + """
                </div>
        """
    return html


def table_6(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Calculation of toxicity values for mammals and birds consuming fish contaminated by {0!s}</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name))
    t6data = gett6data(kabam_obj)
    t6rows = gethtmlrowsfromcols(t6data, headerwadadcdcd)
    html = html + tmpl.render(Context(dict(data=t6rows, headings=headerwadadcdcd)))
    html = html + """
                </div>
        """
    return html


def table_6_qaqc(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Calculation of toxicity values for mammals and birds consuming fish contaminated by {0!s}</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name_exp))
    t6data = gett6dataqaqc(kabam_obj)
    t6rows = gethtmlrowsfromcols(t6data, headerwadadcdcd)
    html = html + tmpl.render(Context(dict(data=t6rows, headings=headerwadadcdcd)))
    html = html + """
                </div>
        """
    return html


def table_7(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Calculation of RQ values for mammals and birds consuming fish contaminated by {0!s}</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name))
    t7data = gett7data(kabam_obj)
    t7rows = gethtmlrowsfromcols(t7data, headerwadadcdcd_noUnits)
    html = html + tmpl.render(Context(dict(data=t7rows, headings=headerwadadcdcd_noUnits)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_7_qaqc(kabam_obj):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Calculation of RQ values for mammals and birds consuming fish contaminated by {0!s}</H4>
                <div class="out_ container_output">
        """.format((kabam_obj.chemical_name_exp))
    t7data = gett7dataqaqc(kabam_obj)
    t7rows = gethtmlrowsfromcols(t7data, headerwadadcdcd_noUnits)
    html = html + tmpl.render(Context(dict(data=t7rows, headings=headerwadadcdcd_noUnits)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_all_sum(sumheadings, tmpl, l_kow, k_oc, c_wdp, water_column_EEC, mineau, x_poc, x_doc, c_ox, w_t, c_ss, oc,
                  k_ow,
                  bw_quail, bw_duck, bwb_other, avian_ld50, avian_lc50, avian_noaec, bw_rat, bwm_other, mammalian_ld50,
                  mammalian_lc50, mammalian_chronic_endpoint,
                  sumheadings_out, acute_dose_based_m_array, acute_dose_based_a_array, chronic_dose_based_m_array,
                  acute_rq_dose_m_array, acute_rq_dose_a_array, acute_rq_diet_a_array, chronic_rq_dose_m_array,
                  chronic_rq_diet_m_array, chronic_rq_diet_a_array):
    html_all_sum = table_sum_input(sumheadings, tmpl, l_kow, k_oc, c_wdp, water_column_EEC, mineau, x_poc, x_doc, c_ox,
                                   w_t, c_ss, oc, k_ow,
                                   bw_quail, bw_duck, bwb_other, avian_ld50, avian_lc50, avian_noaec, bw_rat, bwm_other,
                                   mammalian_ld50, mammalian_lc50, mammalian_chronic_endpoint)
    html_all_sum += table_sum_output1(sumheadings_out, tmpl, acute_dose_based_m_array, acute_dose_based_a_array)
    html_all_sum += table_sum_output2(sumheadings_out, tmpl, chronic_dose_based_m_array)
    html_all_sum += table_sum_output3(sumheadings_out, tmpl, acute_rq_dose_m_array, acute_rq_dose_a_array)
    html_all_sum += table_sum_output4(sumheadings_out, tmpl, acute_rq_diet_a_array)
    html_all_sum += table_sum_output5(sumheadings_out, tmpl, chronic_rq_dose_m_array)
    html_all_sum += table_sum_output6(sumheadings_out, tmpl, chronic_rq_diet_m_array, chronic_rq_diet_a_array)
    return html_all_sum


def table_sum_input(sumheadings, tmpl, l_kow, k_oc, c_wdp, water_column_EEC, mineau, x_poc, x_doc, c_ox, w_t, c_ss, oc,
                    k_ow,
                    bw_quail, bw_duck, bwb_other, avian_ld50, avian_lc50, avian_noaec, bw_rat, bwm_other,
                    mammalian_ld50, mammalian_lc50, mammalian_chronic_endpoint):
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Inputs</H4>
                <div class="out_ container_output">
        """
    tsuminputdata = gettsumdata(l_kow, k_oc, c_wdp, water_column_EEC, mineau, x_poc, x_doc, c_ox, w_t, c_ss, oc, k_ow,
                                bw_quail, bw_duck, bwb_other, avian_ld50, avian_lc50, avian_noaec, bw_rat, bwm_other,
                                mammalian_ld50, mammalian_lc50, mammalian_chronic_endpoint)
    tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
    html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
    html = html + """
                </div>
        """
    return html


def table_sum_output1(sumheadings_out, tmpl, acute_dose_based_m_array, acute_dose_based_a_array):
    html = """
        <br>
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Outputs: Acute Dose Based Toxicity (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    tsumoutputdata = gettsumdata_out1(acute_dose_based_m_array, acute_dose_based_a_array)
    tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings_out)
    html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings_out)))
    html = html + """
                </div>
        """
    return html


def table_sum_output2(sumheadings_out, tmpl, chronic_dose_based_m_array):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Outputs: Chronic Dose Based Toxicity (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    tsumoutputdata = gettsumdata_out2(chronic_dose_based_m_array)
    tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings_out)
    html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings_out)))
    html = html + """
                </div>
        """
    return html


def table_sum_output3(sumheadings_out, tmpl, acute_rq_dose_m_array, acute_rq_dose_a_array):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Outputs: Acute Dose Based RQs</H4>
                <div class="out_ container_output">
        """
    tsumoutputdata = gettsumdata_out3(acute_rq_dose_m_array, acute_rq_dose_a_array)
    tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings_out)
    html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings_out)))
    html = html + """
                </div>
        """
    return html


def table_sum_output4(sumheadings_out, tmpl, acute_rq_diet_a_array):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Outputs: Acute Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    tsumoutputdata = gettsumdata_out4(acute_rq_diet_a_array)
    tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings_out)
    html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings_out)))
    html = html + """
                </div>
        """
    return html


def table_sum_output5(sumheadings_out, tmpl, chronic_rq_dose_m_array):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Outputs: Chronic Based RQs</H4>
                <div class="out_ container_output">
        """
    tsumoutputdata = gettsumdata_out5(chronic_rq_dose_m_array)
    tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings_out)
    html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings_out)))
    html = html + """
                </div>
        """
    return html


def table_sum_output6(sumheadings_out, tmpl, chronic_rq_diet_m_array, chronic_rq_diet_a_array):
    html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Kabam Batch Outputs: Chronic Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    tsumoutputdata = gettsumdata_out6(chronic_rq_diet_m_array, chronic_rq_diet_a_array)
    tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings_out)
    html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings_out)))
    html = html + """
                </div>
        </div>
        """
    return html


def bar_f(kabam_obj):
    resp_conc = [kabam_obj.out_cbr_zoo, kabam_obj.out_cbr_beninv, kabam_obj.out_cbr_filterfeeders, kabam_obj.out_cbr_sfish, kabam_obj.out_cbr_mfish,
                 kabam_obj.out_cbr_lfish]
    diet_conc = [kabam_obj.out_cbd_zoo, kabam_obj.out_cbd_beninv, kabam_obj.out_cbd_filterfeeders, kabam_obj.out_cbd_sfish, kabam_obj.out_cbd_mfish,
                 kabam_obj.out_cbd_lfish]
    html = """<table width="500" border="1">
                          <tr style="display: none">
                            <td id="conc_diet">concanddiet</td>
                            <td id="conc_diet_val">{0!s}</td>
                            </tr> 
                          <tr style="display: none">
                            <td id="conc_resp">concandresp</td>
                            <td id="conc_resp_val">{1!s}</td>
                           
                          </tr>                   
                            </table>""".format(resp_conc, diet_conc)
    return html
