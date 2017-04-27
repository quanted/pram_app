"""
.. module:: trex_tables
   :synopsis: A useful module indeed.
"""

import datetime

import numpy as np
from django.template import Context, Template


def getheaderpvu():
    headings = ["Parameter", "Value", "Units"]
    return headings


def getheaderpva():
    headings = ["App", "Rate", "Day of Application"]
    headings_show = ["App", "Rate (lb ai/acre)", "Day of Application"]
    headings_show_seed = ["App", "Rate (fl oz/cwt)", "Day of Application"]
    return headings, headings_show, headings_show_seed


def getheaderpv5():
    headings_1 = ["Avian (20g)", "Mammalian (15g)"]
    headings_2 = ["Size", "AAcute #1", "AAcute #2", "AChronic", "MAcute #1", "MAcute #2", "MChronic"]
    headings_2_show = ["", "Acute #1", "Acute #2", "Chronic", "Acute #1", "Acute #2", "Chronic"]
    headings_3_show = ["Size", "(mg ai /kg-bw/day)/LD50", "mg ai ft<sup>-2</sup>/(LD50*bw)",
                       "mg kg<sup>-1</sup>seed/NOAEL", "(mg ai /kg-bw/day)/LD50", "mg ai ft<sup>-2</sup>/(LD50*bw)",
                       "mg a.i./kg-bw/day/adjusted NOAEL"]

    return headings_1, headings_2, headings_2_show, headings_3_show


def getheaderpv6():
    headings = ["Application Target", "Value"]
    return headings


def getheaderpv7():
    headings = ["Application Target", "Small", "Medium", "Large"]
    return headings


def getheaderpv8():
    headings = ["Application Target", "Acute", "Chronic"]
    return headings


def getheaderpv10():
    headings = ["Application Target", "Acute_sm", "Chronic_sm", "Acute_md", "Chronic_md", "Acute_lg", "Chronic_lg"]
    return headings


def getheaderpv12():
    headings = ["Animal Size", "Avian", "Mammal"]
    return headings


def getheaderpvr():
    headings = ["Parameter", "Value", "Results"]
    return headings


def getheadersum():
    headings = ["Parameter", "Mean", "Std", "Min", "Max", "Unit"]
    return headings


def getheadersum5():
    headings_1 = ["Avian (20g)", "Mammalian (15g)"]
    headings_2 = ["Size", "Metric", "AAcute #1", "AAcute #2", "AChronic", "MAcute #1", "MAcute #2", "MChronic"]
    headings_2_show = ["Size", "Metric", "Acute #1", "Acute #2", "Chronic", "Acute #1", "Acute #2", "Chronic"]
    return headings_1, headings_2, headings_2_show


def getheadersum6():
    headings_1 = ["Metric", "Application Target"]
    headings_1_c_span = [1, 5]
    headings_1_max_seed_ratepan = [2, 1]
    headings_1_zip = zip(headings_1, headings_1_c_span, headings_1_max_seed_ratepan)
    headings_2 = ["Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods/Seeds", "Arthropods"]
    headings_2_show = ["Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods/Seeds", "Arthropods"]
    return headings_1_zip, headings_2, headings_2_show


def getheadersum7():
    headings_1 = ["Animal Size", "Metric", "Application Target"]
    headings_1_c_span = [1, 1, 6]
    headings_1_max_seed_ratepan = [2, 2, 1]
    headings_1_zip = zip(headings_1, headings_1_c_span, headings_1_max_seed_ratepan)
    headings_2 = ["Animal Size", "Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods",
                  "Seeds"]
    # headings_2 = ["Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods", "Seeds"]
    headings_2_show = ["Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods", "Seeds"]
    return headings_1_zip, headings_2, headings_2_show


def getheadersum8():
    headings_1 = ["Type", "Metric", "Application Target"]
    headings_1_c_span = [1, 1, 5]
    headings_1_max_seed_ratepan = [2, 2, 1]
    headings_1_zip = zip(headings_1, headings_1_c_span, headings_1_max_seed_ratepan)
    headings_2 = ["Type", "Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods"]
    headings_2_show = ["Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods"]
    return headings_1_zip, headings_2, headings_2_show


def getheadersum9():
    headings_1 = ["Animal Size", "Metric", "Application Target"]
    headings_1_c_span = [1, 1, 6]
    headings_1_max_seed_ratepan = [2, 2, 1]
    headings_1_zip = zip(headings_1, headings_1_c_span, headings_1_max_seed_ratepan)
    headings_2 = ["Animal Size", "Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods",
                  "Seeds"]
    headings_2_show = ["Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods", "Seeds"]
    return headings_1_zip, headings_2, headings_2_show


def getheadersum10():
    headings_1 = ["Animal Size", "Type", "Metric", "Application Target"]
    headings_1_c_span = [1, 1, 1, 6]
    headings_1_max_seed_ratepan = [2, 2, 2, 1]
    headings_1_zip = zip(headings_1, headings_1_c_span, headings_1_max_seed_ratepan)
    headings_2 = ["Animal Size", "Type", "Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods",
                  "Arthropods", "Seeds"]
    headings_2_show = ["Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods", "Arthropods", "Seeds"]
    return headings_1_zip, headings_2, headings_2_show


def getheadersum11():
    headings_1 = ["Type", "Metric", "Application Target"]
    headings_1_c_span = [1, 1, 5]
    headings_1_max_seed_ratepan = [2, 2, 1]
    headings_1_zip = zip(headings_1, headings_1_c_span, headings_1_max_seed_ratepan)
    headings_2 = ["Type", "Metric", "Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods/Seeds", "Arthropods"]
    headings_2_show = ["Short Grass", "Tall Grass", "Broadleaf Plants", "Fruits/Pods/Seeds", "Arthropods"]
    return headings_1_zip, headings_2, headings_2_show


def getheadersum12():
    headings = ["Animal Size", "Metric", "Avian", "Mammal"]
    return headings


def getheaderpv5_qaqc():
    headings_1 = ["Avian (20g)", "Mammalian (15g)"]
    headings_2 = ["Type", "Size", "AAcute #1", "AAcute #2", "AChronic", "MAcute #1", "MAcute #2", "MChronic"]
    headings_2_show = ["", "", "Acute #1", "Acute #2", "Chronic", "Acute #1", "Acute #2", "Chronic"]
    headings_3_show = ["Type", "Size", "(mg ai /kg-bw/day)/LD50", "mg ai ft<sup>-2</sup>/(LD50*bw)",
                       "mg kg<sup>-1</sup>seed/NOAEL", "(mg ai /kg-bw/day)/LD50", "mg ai ft<sup>-2</sup>/(LD50*bw)",
                       "mg a.i./kg-bw/day/adjusted NOAEL"]
    return headings_1, headings_2, headings_2_show, headings_3_show


def getheaderpv6_qaqc():
    headings = ["Type", "Application Target", "Value"]
    return headings


def getheaderpv7_qaqc():
    headings = ["Type", "Application Target", "Small", "Medium", "Large"]
    return headings


def getheaderpv8_qaqc():
    headings = ["Type", "Application Target", "Acute", "Chronic"]
    return headings


def getheaderpv10_qaqc():
    headings = ["Type", "Application Target", "Acute_sm", "Chronic_sm", "Acute_md", "Chronic_md", "Acute_lg",
                "Chronic_lg"]
    return headings


def getheaderpv12_qaqc():
    headings = ["Type", "Animal Size", "Avian", "Mammal"]
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
                <th colspan={{ th_span|default:'1' }}>{{ heading }}</th>
        {% endfor %}
        </tr>
    {% if sub_headings %}
        <tr>
        {% for sub_heading in sub_headings %}
            <th>{{ sub_heading }}</th>
        {% endfor %}
        </tr>
        {% if sub_headings_1 %}
            <tr>
            {% for sub_heading_1 in sub_headings_1 %}
                <th>{{ sub_heading_1|safe }}</th>
            {% endfor %}
            </tr>
        {% endif %}
    {% endif %}
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


def getdjtemplate_sum():
    dj_template = """
    <table class="out_">
    {# headings #}
        <tr>
            {% for heading, th_c_span, th_max_seed_ratepan in headings %}
                <th colspan={{ th_c_span|default:'1' }} rowspan={{ th_max_seed_ratepan|default:'1' }}>{{ heading }}</th>
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
    {% if data %}
        {% for row in data %}
                <tr>
                    {% for val in row %}
                        <td>{{ val|default:'' }}</td>
                    {% endfor %}
                </tr>
        {% endfor %}
    {% endif %}

    {% if data_cols %}
        {% for data_col in data_cols %}
            <tr>
                <td rowspan='4'>{{ data_col|default:''}}</td>
                    {% for row in data_new %}
                        {% for val in row %}
                            <td>{{ val|default:'' }}</td>
                        {% endfor %}
                    {% endfor %}
            </tr>
        {% endfor %}
    {% endif %}


    </table>
    """
    return dj_template


def getdjtemplate_10():
    dj_template = """
    <table class="out_">
    {# headings #}
      <tr>
        <th rowspan="2">Application Target</div></th>
        <th colspan="2">Small</th>
        <th colspan="2">Medium</th>
        <th colspan="2">Large</th>
        </tr>
        <tr>
        <th scope="col">Acute</div></th>
        <th scope="col">Chronic</div></th>
        <th scope="col">Acute</div></th>
        <th scope="col">Chronic</div></th>
        <th scope="col">Acute</div></th>
        <th scope="col">Chronic</div></th>
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


def getdjtemplate_10_qaqc():
    dj_template = """
    <table class="out_">
    {# headings #}
      <tr>
        <th rowspan="2">Type</div></th>
        <th rowspan="2">Application Target</div></th>
        <th colspan="2">Small</th>
        <th colspan="2">Medium</th>
        <th colspan="2">Large</th>
        </tr>
        <tr>
        <th scope="col">Acute</div></th>
        <th scope="col">Chronic</div></th>
        <th scope="col">Acute</div></th>
        <th scope="col">Chronic</div></th>
        <th scope="col">Acute</div></th>
        <th scope="col">Chronic</div></th>
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


pvuheadings = getheaderpvu()
pvaheadings = getheaderpva()
pvrheadings = getheaderpvr()
pv5headings = getheaderpv5()
pv6headings = getheaderpv6()
pv7headings = getheaderpv7()
pv8headings = getheaderpv8()
pv10headings = getheaderpv10()
pv12headings = getheaderpv12()

sumheadings = getheadersum()
sumheadings_5 = getheadersum5()
sumheadings_6 = getheadersum6()
sumheadings_7 = getheadersum7()
sumheadings_8 = getheadersum8()
sumheadings_9 = getheadersum9()
sumheadings_10 = getheadersum10()
sumheadings_11 = getheadersum11()
sumheadings_12 = getheadersum12()

pv5headings_qaqc = getheaderpv5_qaqc()
pv6headings_qaqc = getheaderpv6_qaqc()
pv7headings_qaqc = getheaderpv7_qaqc()
pv8headings_qaqc = getheaderpv8_qaqc()
pv10headings_qaqc = getheaderpv10_qaqc()
pv12headings_qaqc = getheaderpv12_qaqc()

djtemplate = getdjtemplate()
djtemplate_sum = getdjtemplate_sum()
djtemplate_10 = getdjtemplate_10()
djtemplate_10_qaqc = getdjtemplate_10_qaqc()

tmpl = Template(djtemplate)
tmpl_sum = Template(djtemplate_sum)
tmpl_10 = Template(djtemplate_10)
tmpl_10_qaqc = Template(djtemplate_10_qaqc)


def gett1data_broad(trex_obj):
    data = {
        "Parameter": ['Chemical Name', 'Use', 'Formulated product name', 'Percentage active ingredient',
                      'Application type', 'Percentage incorporated', 'Foliar dissipation half-life', ],
        "Value": ['{0!s}'.format(trex_obj.chemical_name), '{0!s}'.format(trex_obj.use), '{0!s}'.format(trex_obj.formu_name),
                  '{0!s}'.format(trex_obj.percent_act_ing), '{0!s}'.format(trex_obj.application_type),
                  '{0!s}'.format(trex_obj.percent_incorp), '{0!s}'.format(trex_obj.foliar_diss_hlife), ],
        "Units": ['', '', '', '%', '', '%', 'days', ],
    }
    return data


def gett1data_band(trex_obj):
    data = {
        "Parameter": ['Chemical Name', 'Use', 'Formulated product name', 'Percentage active ingredient',
                      'Application type', 'Row spacing', 'Bandwidth', 'Percentage incorporated',
                      'Foliar dissipation half-life', ],
        "Value": ['{0!s}'.format(trex_obj.chemical_name), '{0!s}'.format(trex_obj.use), '{0!s}'.format(trex_obj.formu_name),
                  '{0!s}'.format(trex_obj.percent_act_ing), '{0!s}'.format(trex_obj.application_type),
                  '{0:.4!s}'.format(trex_obj.row_spacing), '{0:.4!s}'.format(trex_obj.bandwidth), '{0!s}'.format(trex_obj.percent_incorp), '{0!s}'.format(trex_obj.foliar_diss_hlife), ],
        "Units": ['', '', '', '%', '', 'inch', 'inch', '%', 'days', ],
    }
    return data


def gett1data_seed(trex_obj):
    data = {
        "Parameter": ['Chemical Name', 'Use', 'Formulated product name', 'Percentage active ingredient',
                      'Application type', 'Seed treatment formulation name', 'Crop use', 'Density of product',
                      'Seeding rare'],
        "Value": ['{0!s}'.format(trex_obj.chemical_name), '{0!s}'.format(trex_obj.use), '{0!s}'.format(trex_obj.formu_name),
                  '{0!s}'.format(trex_obj.percent_act_ing), '{0!s}'.format(trex_obj.application_type),
                  '{0!s}'.format(trex_obj.seed_treatment_formulation_name), '{0!s}'.format(trex_obj.seed_crop), '{0!s}'.format(trex_obj.density),
                  '{0!s}'.format(trex_obj.max_seed_rate), ],
        "Units": ['', '', '', '%', '', '', '', 'lbs/gal', 'lbs/acre', ],
    }
    return data


def gett2data(index, rate, day):
    data = {
        "App": ['{0!s}'.format(index), ],
        "Rate": [rate, ],
        "Day of Application": ['{0!s}'.format(day), ],
    }
    return data


def gett3data(trex_obj):
    data = {
        "Parameter": ['Avian LD50', 'Test species (for Avian LD50)', 'Weight',
                      'Avian LC50', 'Test species (for Avian LC50)', 'Weight',
                      'Avian NOAEC', 'Test species (for Avian NOAEC)', 'Weight',
                      'Avian NOAEL', 'Test species (for Avian NOAEL)', 'Weight',
                      'Body weight of assessed bird small', 'Body weight of assessed bird medium',
                      'Body weight of assessed bird large', 'Mineau scaling factor', ],
        "Value": ['{0!s}'.format(trex_obj.ld50_bird), '{0!s}'.format(trex_obj.species_of_the_tested_bird_avian_ld50),
                  '{0!s}'.format(trex_obj.tw_bird_ld50),
                  '{0!s}'.format(trex_obj.lc50_bird), '{0!s}'.format(trex_obj.species_of_the_tested_bird_avian_lc50),
                  '{0!s}'.format(trex_obj.tw_bird_lc50),
                  '{0!s}'.format(trex_obj.noaec_bird), '{0!s}'.format(trex_obj.species_of_the_tested_bird_avian_noaec),
                  '{0!s}'.format(trex_obj.tw_bird_noaec),
                  '{0!s}'.format(trex_obj.noael_bird), '{0!s}'.format(trex_obj.species_of_the_tested_bird_avian_noael),
                  '{0!s}'.format(trex_obj.tw_bird_noael),
                  '{0!s}'.format(trex_obj.aw_bird_sm), '{0!s}'.format(trex_obj.aw_bird_md), '{0!s}'.format(trex_obj.aw_bird_lg),
                  '{0!s}'.format(trex_obj.mineau_sca_fact), ],
        "Units": ['mg/kg-bw', '', 'g', 'mg/kg-diet', '', 'g', 'mg/kg-diet', '', 'g', 'mg/kg-bw', '', 'g', 'g', 'g', 'g',
                  ''],
    }
    return data


def gett4data(trex_obj):
    data = {
        "Parameter": ['Mammalian LD50', 'Mammalian LC50', 'Mammalian NOAEC', 'Mammalian NOAEL',
                      'Body weight of assessed mammal small',
                      'Body weight of assessed mammal medium', 'Body weight of assessed mammal large',
                      'Body weight of tested mammal', ],
        "Value": ['{0!s}'.format(trex_obj.ld50_mamm), '{0!s}'.format(trex_obj.lc50_mamm), '{0!s}'.format(trex_obj.noaec_mamm),
                  '{0!s}'.format(trex_obj.noael_mamm),
                  '{0!s}'.format(trex_obj.aw_mamm_sm), '{0!s}'.format(trex_obj.aw_mamm_md), '{0!s}'.format(trex_obj.aw_mamm_lg),
                  '{0!s}'.format(trex_obj.tw_mamm), ],
        "Units": ['mg/kg-bw', 'mg/kg-diet', 'mg/kg-diet', 'mg/kg-bw', 'g', 'g', 'g', 'g', ],
    }
    return data


def gett5data(out_sa_bird_1_s, out_sa_bird_2_s, out_sc_bird_s, out_sa_mamm_1_s, out_sa_mamm_2_s, out_sc_mamm_s,
              out_sa_bird_1_m, out_sa_bird_2_m, out_sc_bird_m, out_sa_mamm_1_m, out_sa_mamm_2_m, out_sc_mamm_m,
              out_sa_bird_1_l, out_sa_bird_2_l, out_sc_bird_l, out_sa_mamm_1_l, out_sa_mamm_2_l, out_sc_mamm_l):
    data = {
        "Size": ['Small', 'Medium', 'Large', ],
        "AAcute #1": ['{0:.2e}'.format(out_sa_bird_1_s), '{0:.2e}'.format(out_sa_bird_1_m), '{0:.2e}'.format(out_sa_bird_1_l), ],
        "AAcute #2": ['{0:.2e}'.format(out_sa_bird_2_s), '{0:.2e}'.format(out_sa_bird_2_m), '{0:.2e}'.format(out_sa_bird_2_l), ],
        "AChronic": ['{0:.2e}'.format(out_sc_bird_s), '{0:.2e}'.format(out_sc_bird_m), '{0:.2e}'.format(out_sc_bird_l), ],
        "MAcute #1": ['{0:.2e}'.format(out_sa_mamm_1_s), '{0:.2e}'.format(out_sa_mamm_1_m), '{0:.2e}'.format(out_sa_mamm_1_l), ],
        "MAcute #2": ['{0:.2e}'.format(out_sa_mamm_2_s), '{0:.2e}'.format(out_sa_mamm_2_m), '{0:.2e}'.format(out_sa_mamm_2_l), ],
        "MChronic": ['{0:.2e}'.format(out_sc_mamm_s), '{0:.2e}'.format(out_sc_mamm_m), '{0:.2e}'.format(out_sc_mamm_l), ],
    }
    return data


def gett6data(out_eec_diet_sg, out_eec_diet_tg, out_eec_diet_bp, out_eec_diet_fr, out_eec_diet_ar):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods/Seeds', 'Arthropods', ],
        "Value": ['{0:.2e}'.format(out_eec_diet_sg), '{0:.2e}'.format(out_eec_diet_tg), '{0:.2e}'.format(out_eec_diet_bp), '{0:.2e}'.format(out_eec_diet_fr),
                  '{0:.2e}'.format(out_eec_diet_ar)],
    }
    return data


def gett7data(out_eec_dose_bird_sg_sm, out_eec_dose_bird_sg_md, out_eec_dose_bird_sg_lg, out_eec_dose_bird_tg_sm, out_eec_dose_bird_tg_md,
              out_eec_dose_bird_tg_lg, out_eec_dose_bird_bp_sm, out_eec_dose_bird_bp_md, out_eec_dose_bird_bp_lg, out_eec_dose_bird_fp_sm,
              out_eec_dose_bird_fp_md, out_eec_dose_bird_fp_lg, out_eec_dose_bird_ar_sm, out_eec_dose_bird_ar_md, out_eec_dose_bird_ar_lg,
              out_eec_dose_bird_se_sm, out_eec_dose_bird_se_md, out_eec_dose_bird_se_lg):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods', 'Arthropods', 'Seeds', ],
        "Small": ['{0:.2e}'.format(out_eec_dose_bird_sg_sm), '{0:.2e}'.format(out_eec_dose_bird_tg_sm), '{0:.2e}'.format(out_eec_dose_bird_bp_sm),
                  '{0:.2e}'.format(out_eec_dose_bird_fp_sm), '{0:.2e}'.format(out_eec_dose_bird_ar_sm), '{0:.2e}'.format(out_eec_dose_bird_se_sm)],
        "Medium": ['{0:.2e}'.format(out_eec_dose_bird_sg_md), '{0:.2e}'.format(out_eec_dose_bird_tg_md), '{0:.2e}'.format(out_eec_dose_bird_bp_md),
                   '{0:.2e}'.format(out_eec_dose_bird_fp_md), '{0:.2e}'.format(out_eec_dose_bird_ar_md), '{0:.2e}'.format(out_eec_dose_bird_se_md)],
        "Large": ['{0:.2e}'.format(out_eec_dose_bird_sg_lg), '{0:.2e}'.format(out_eec_dose_bird_tg_lg), '{0:.2e}'.format(out_eec_dose_bird_bp_lg),
                  '{0:.2e}'.format(out_eec_dose_bird_fp_lg), '{0:.2e}'.format(out_eec_dose_bird_ar_lg), '{0:.2e}'.format(out_eec_dose_bird_se_lg)],
    }
    return data


def gett7_add_data(out_arq_bird_sg_sm, out_arq_bird_sg_md, out_arq_bird_sg_lg, out_arq_bird_tg_sm, out_arq_bird_tg_md, out_arq_bird_tg_lg,
                   out_arq_bird_bp_sm, out_arq_bird_bp_md, out_arq_bird_bp_lg, out_arq_bird_fp_sm, out_arq_bird_fp_md, out_arq_bird_fp_lg,
                   out_arq_bird_ar_sm, out_arq_bird_ar_md, out_arq_bird_ar_lg, out_arq_bird_se_sm, out_arq_bird_se_md, out_arq_bird_se_lg):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods', 'Arthropods', 'Seeds', ],
        "Small": ['{0:.2e}'.format(out_arq_bird_sg_sm), '{0:.2e}'.format(out_arq_bird_tg_sm), '{0:.2e}'.format(out_arq_bird_bp_sm),
                  '{0:.2e}'.format(out_arq_bird_fp_sm), '{0:.2e}'.format(out_arq_bird_ar_sm), '{0:.2e}'.format(out_arq_bird_se_sm)],
        "Medium": ['{0:.2e}'.format(out_arq_bird_sg_md), '{0:.2e}'.format(out_arq_bird_tg_md), '{0:.2e}'.format(out_arq_bird_bp_md),
                   '{0:.2e}'.format(out_arq_bird_fp_md), '{0:.2e}'.format(out_arq_bird_ar_md), '{0:.2e}'.format(out_arq_bird_se_md)],
        "Large": ['{0:.2e}'.format(out_arq_bird_sg_lg), '{0:.2e}'.format(out_arq_bird_tg_lg), '{0:.2e}'.format(out_arq_bird_bp_lg),
                  '{0:.2e}'.format(out_arq_bird_fp_lg), '{0:.2e}'.format(out_arq_bird_ar_lg), '{0:.2e}'.format(out_arq_bird_se_lg)],
    }
    return data


def gett8data(out_arq_diet_bird_sg_a, out_arq_diet_bird_sg_c, out_arq_diet_bird_tg_a, out_arq_diet_bird_tg_c, out_arq_diet_bird_bp_a,
              out_arq_diet_bird_bp_c, out_arq_diet_bird_fp_a, out_arq_diet_bird_fp_c, out_arq_diet_bird_ar_a, out_arq_diet_bird_ar_c):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods', 'Arthropods', ],
        "Acute": ['{0:.2e}'.format(out_arq_diet_bird_sg_a), '{0:.2e}'.format(out_arq_diet_bird_tg_a), '{0:.2e}'.format(out_arq_diet_bird_bp_a),
                  '{0:.2e}'.format(out_arq_diet_bird_fp_a), '{0:.2e}'.format(out_arq_diet_bird_ar_a), ],
        "Chronic": ['{0:.2e}'.format(out_arq_diet_bird_sg_c), '{0:.2e}'.format(out_arq_diet_bird_tg_c), '{0:.2e}'.format(out_arq_diet_bird_bp_c),
                    '{0:.2e}'.format(out_arq_diet_bird_fp_c), '{0:.2e}'.format(out_arq_diet_bird_ar_c), ],
    }
    return data


def gett9data(out_eec_dose_mamm_sg_sm, out_eec_dose_mamm_sg_md, out_eec_dose_mamm_sg_lg, out_eec_dose_mamm_tg_sm, out_eec_dose_mamm_tg_md,
              out_eec_dose_mamm_tg_lg, out_eec_dose_mamm_bp_sm, out_eec_dose_mamm_bp_md, out_eec_dose_mamm_bp_lg, out_eec_dose_mamm_fp_sm,
              out_eec_dose_mamm_fp_md, out_eec_dose_mamm_fp_lg, out_eec_dose_mamm_ar_sm, out_eec_dose_mamm_ar_md, out_eec_dose_mamm_ar_lg,
              out_eec_dose_mamm_se_sm, out_eec_dose_mamm_se_md, out_eec_dose_mamm_se_lg):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods', 'Arthropods', 'Seeds', ],
        "Small": ['{0:.2e}'.format(out_eec_dose_mamm_sg_sm), '{0:.2e}'.format(out_eec_dose_mamm_tg_sm), '{0:.2e}'.format(out_eec_dose_mamm_bp_sm),
                  '{0:.2e}'.format(out_eec_dose_mamm_fp_sm), '{0:.2e}'.format(out_eec_dose_mamm_ar_sm), '{0:.2e}'.format(out_eec_dose_mamm_se_sm)],
        "Medium": ['{0:.2e}'.format(out_eec_dose_mamm_sg_md), '{0:.2e}'.format(out_eec_dose_mamm_tg_md), '{0:.2e}'.format(out_eec_dose_mamm_bp_md),
                   '{0:.2e}'.format(out_eec_dose_mamm_fp_md), '{0:.2e}'.format(out_eec_dose_mamm_ar_md), '{0:.2e}'.format(out_eec_dose_mamm_se_md)],
        "Large": ['{0:.2e}'.format(out_eec_dose_mamm_sg_lg), '{0:.2e}'.format(out_eec_dose_mamm_tg_lg), '{0:.2e}'.format(out_eec_dose_mamm_bp_lg),
                  '{0:.2e}'.format(out_eec_dose_mamm_fp_lg), '{0:.2e}'.format(out_eec_dose_mamm_ar_lg), '{0:.2e}'.format(out_eec_dose_mamm_se_lg)],
    }
    return data


def gett10data(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md, out_crq_dose_mamm_sg_md, out_arq_dose_mamm_sg_lg,
               out_crq_dose_mamm_sg_lg, out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm, out_arq_dose_mamm_tg_md, out_crq_dose_mamm_tg_md,
               out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg, out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md,
               out_crq_dose_mamm_bp_md, out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg, out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm,
               out_arq_dose_mamm_fp_md, out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg, out_arq_dose_mamm_ar_sm,
               out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md, out_crq_dose_mamm_ar_md, out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg,
               out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm, out_arq_dose_mamm_se_md, out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg,
               out_crq_dose_mamm_se_lg):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods', 'Arthropods', 'Seeds', ],
        "Acute_sm": ['{0:.2e}'.format(out_arq_dose_mamm_sg_sm), '{0:.2e}'.format(out_arq_dose_mamm_tg_sm), '{0:.2e}'.format(out_arq_dose_mamm_bp_sm),
                     '{0:.2e}'.format(out_arq_dose_mamm_fp_sm), '{0:.2e}'.format(out_arq_dose_mamm_ar_sm), '{0:.2e}'.format(out_arq_dose_mamm_se_sm)],
        "Chronic_sm": ['{0:.2e}'.format(out_crq_dose_mamm_sg_sm), '{0:.2e}'.format(out_crq_dose_mamm_tg_sm),
                       '{0:.2e}'.format(out_crq_dose_mamm_bp_sm), '{0:.2e}'.format(out_crq_dose_mamm_fp_sm),
                       '{0:.2e}'.format(out_crq_dose_mamm_ar_sm), '{0:.2e}'.format(out_crq_dose_mamm_se_sm)],
        "Acute_md": ['{0:.2e}'.format(out_arq_dose_mamm_sg_md), '{0:.2e}'.format(out_arq_dose_mamm_tg_md), '{0:.2e}'.format(out_arq_dose_mamm_bp_md),
                     '{0:.2e}'.format(out_arq_dose_mamm_fp_md), '{0:.2e}'.format(out_arq_dose_mamm_ar_md), '{0:.2e}'.format(out_arq_dose_mamm_se_md)],
        "Chronic_md": ['{0:.2e}'.format(out_crq_dose_mamm_sg_md), '{0:.2e}'.format(out_crq_dose_mamm_tg_md),
                       '{0:.2e}'.format(out_crq_dose_mamm_bp_md), '{0:.2e}'.format(out_crq_dose_mamm_fp_md),
                       '{0:.2e}'.format(out_crq_dose_mamm_ar_md), '{0:.2e}'.format(out_crq_dose_mamm_se_md)],
        "Acute_lg": ['{0:.2e}'.format(out_arq_dose_mamm_sg_lg), '{0:.2e}'.format(out_arq_dose_mamm_tg_lg), '{0:.2e}'.format(out_arq_dose_mamm_bp_lg),
                     '{0:.2e}'.format(out_arq_dose_mamm_fp_lg), '{0:.2e}'.format(out_arq_dose_mamm_ar_lg), '{0:.2e}'.format(out_arq_dose_mamm_se_lg)],
        "Chronic_lg": ['{0:.2e}'.format(out_crq_dose_mamm_sg_lg), '{0:.2e}'.format(out_crq_dose_mamm_tg_lg),
                       '{0:.2e}'.format(out_crq_dose_mamm_bp_lg), '{0:.2e}'.format(out_crq_dose_mamm_fp_lg),
                       '{0:.2e}'.format(out_crq_dose_mamm_ar_lg), '{0:.2e}'.format(out_crq_dose_mamm_se_lg)],
    }
    return data


def gett11data(out_arq_diet_mamm_sg, out_crq_diet_bird_sg, out_arq_diet_mamm_tg, out_crq_diet_bird_tg, out_arq_diet_mamm_bp,
               out_crq_diet_bird_bp, out_arq_diet_mamm_fp, out_crq_diet_bird_fp, out_arq_diet_mamm_ar, out_crq_diet_bird_ar):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods/Seeds', 'Arthropods', ],
        "Acute": ['{0:.2e}'.format(out_arq_diet_mamm_sg), '{0:.2e}'.format(out_arq_diet_mamm_tg), '{0:.2e}'.format(out_arq_diet_mamm_bp),
                  '{0:.2e}'.format(out_arq_diet_mamm_fp), '{0:.2e}'.format(out_arq_diet_mamm_ar)],
        "Chronic": ['{0:.2e}'.format(out_crq_diet_bird_sg), '{0:.2e}'.format(out_crq_diet_bird_tg), '{0:.2e}'.format(out_crq_diet_bird_bp),
                    '{0:.2e}'.format(out_crq_diet_bird_fp), '{0:.2e}'.format(out_crq_diet_bird_ar)],
    }
    return data


def gett11data_na(out_arq_diet_mamm_sg, out_crq_diet_bird_sg, out_arq_diet_mamm_tg, out_crq_diet_bird_tg, out_arq_diet_mamm_bp,
                  out_crq_diet_bird_bp, out_arq_diet_mamm_fp, out_crq_diet_bird_fp, out_arq_diet_mamm_ar, out_crq_diet_bird_ar):
    data = {
        "Application Target": ['Short Grass', 'Tall Grass', 'Broadleaf Plants', 'Fruits/Pods/Seeds', 'Arthropods', ],
        "Acute": ['{0!s}'.format(out_arq_diet_mamm_sg), '{0!s}'.format(out_arq_diet_mamm_tg), '{0!s}'.format(out_arq_diet_mamm_bp),
                  '{0!s}'.format(out_arq_diet_mamm_fp), '{0!s}'.format(out_arq_diet_mamm_ar)],
        "Chronic": ['{0:.2e}'.format(out_crq_diet_bird_sg), '{0:.2e}'.format(out_crq_diet_bird_tg), '{0:.2e}'.format(out_crq_diet_bird_bp),
                    '{0:.2e}'.format(out_crq_diet_bird_fp), '{0:.2e}'.format(out_crq_diet_bird_ar)],
    }
    return data


def gett12data(out_ld50_rg_bird_sm, out_ld50_rg_mamm_sm, out_ld50_rg_bird_md, out_ld50_rg_mamm_md, out_ld50_rg_bird_lg, out_ld50_rg_mamm_lg):
    data = {
        "Animal Size": ['Small', 'Medium', 'Large', ],
        "Avian": ['{0:.2e}'.format(out_ld50_rg_bird_sm), '{0:.2e}'.format(out_ld50_rg_bird_md), '{0:.2e}'.format(out_ld50_rg_bird_lg), ],
        "Mammal": ['{0:.2e}'.format(out_ld50_rg_mamm_sm), '{0:.2e}'.format(out_ld50_rg_mamm_md), '{0:.2e}'.format(out_ld50_rg_mamm_lg), ],
    }
    return data


def gett5data_qaqc(out_sa_bird_1_s, out_sa_bird_2_s, out_sc_bird_s, out_sa_mamm_1_s, out_sa_mamm_2_s, out_sc_mamm_s,
                   out_sa_bird_1_m, out_sa_bird_2_m, out_sc_bird_m, out_sa_mamm_1_m, out_sa_mamm_2_m, out_sc_mamm_m,
                   out_sa_bird_1_l, out_sa_bird_2_l, out_sc_bird_l, out_sa_mamm_1_l, out_sa_mamm_2_l, out_sc_mamm_l,
                   out_sa_bird_1_s_exp, out_sa_bird_2_s_exp, out_sc_bird_s_exp, out_sa_mamm_1_s_exp, out_sa_mamm_2_s_exp, out_sc_mamm_s_exp,
                   out_sa_bird_1_m_exp, out_sa_bird_2_m_exp, out_sc_bird_m_exp, out_sa_mamm_1_m_exp, out_sa_mamm_2_m_exp, out_sc_mamm_m_exp,
                   out_sa_bird_1_l_exp, out_sa_bird_2_l_exp, out_sc_bird_l_exp, out_sa_mamm_1_l_exp, out_sa_mamm_2_l_exp, out_sc_mamm_l_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', ],
        "Size": ['Small', 'Small', 'Medium', 'Medium', 'Large', 'Large', ],
        "AAcute #1": ['{0:.2e}'.format(out_sa_bird_1_s), '{0:.2e}'.format(out_sa_bird_1_s_exp), '{0:.2e}'.format(out_sa_bird_1_m), '{0:.2e}'.format(out_sa_bird_1_m_exp),
                      '{0:.2e}'.format(out_sa_bird_1_l), '{0:.2e}'.format(out_sa_bird_1_l_exp), ],
        "AAcute #2": ['{0:.2e}'.format(out_sa_bird_2_s), '{0:.2e}'.format(out_sa_bird_2_s_exp), '{0:.2e}'.format(out_sa_bird_2_m), '{0:.2e}'.format(out_sa_bird_2_m_exp),
                      '{0:.2e}'.format(out_sa_bird_2_l), '{0:.2e}'.format(out_sa_bird_2_l_exp), ],
        "AChronic": ['{0:.2e}'.format(out_sc_bird_s), '{0:.2e}'.format(out_sc_bird_s_exp), '{0:.2e}'.format(out_sc_bird_m), '{0:.2e}'.format(out_sc_bird_m_exp),
                     '{0:.2e}'.format(out_sc_bird_l), '{0:.2e}'.format(out_sc_bird_l_exp), ],
        "MAcute #1": ['{0:.2e}'.format(out_sa_mamm_1_s), '{0:.2e}'.format(out_sa_mamm_1_s_exp), '{0:.2e}'.format(out_sa_mamm_1_m), '{0:.2e}'.format(out_sa_mamm_1_m_exp),
                      '{0:.2e}'.format(out_sa_mamm_1_l), '{0:.2e}'.format(out_sa_mamm_1_l_exp), ],
        "MAcute #2": ['{0:.2e}'.format(out_sa_mamm_2_s), '{0:.2e}'.format(out_sa_mamm_2_s_exp), '{0:.2e}'.format(out_sa_mamm_2_m), '{0:.2e}'.format(out_sa_mamm_2_m_exp),
                      '{0:.2e}'.format(out_sa_mamm_2_l), '{0:.2e}'.format(out_sa_mamm_2_l_exp), ],
        "MChronic": ['{0:.2e}'.format(out_sc_mamm_s), '{0:.2e}'.format(out_sc_mamm_s_exp), '{0:.2e}'.format(out_sc_mamm_m), '{0:.2e}'.format(out_sc_mamm_m_exp),
                     '{0:.2e}'.format(out_sc_mamm_l), '{0:.2e}'.format(out_sc_mamm_l_exp), ],
    }
    return data


def gett6data_qaqc(out_eec_diet_sg, out_eec_diet_tg, out_eec_diet_bp, out_eec_diet_fr, out_eec_diet_ar, out_eec_diet_sg_exp, out_eec_diet_tg_exp,
                   out_eec_diet_bp_exp, out_eec_diet_fr_exp, out_eec_diet_ar_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods/Seeds', 'Fruits/Pods/Seeds', 'Arthropods',
                               'Arthropods', ],
        "Value": ['{0:.2e}'.format(out_eec_diet_sg), '{0:.2e}'.format(out_eec_diet_sg_exp), '{0:.2e}'.format(out_eec_diet_tg), '{0:.2e}'.format(out_eec_diet_tg_exp),
                  '{0:.2e}'.format(out_eec_diet_bp), '{0:.2e}'.format(out_eec_diet_bp_exp), '{0:.2e}'.format(out_eec_diet_fr), '{0:.2e}'.format(out_eec_diet_fr_exp),
                  '{0:.2e}'.format(out_eec_diet_ar), '{0:.2e}'.format(out_eec_diet_ar_exp)],
    }
    return data


def gett7data_qaqc(out_eec_dose_bird_sg_sm, out_eec_dose_bird_sg_md, out_eec_dose_bird_sg_lg, out_eec_dose_bird_tg_sm,
                   out_eec_dose_bird_tg_md, out_eec_dose_bird_tg_lg, out_eec_dose_bird_bp_sm, out_eec_dose_bird_bp_md,
                   out_eec_dose_bird_bp_lg, out_eec_dose_bird_fp_sm, out_eec_dose_bird_fp_md, out_eec_dose_bird_fp_lg,
                   out_eec_dose_bird_ar_sm, out_eec_dose_bird_ar_md, out_eec_dose_bird_ar_lg, out_eec_dose_bird_se_sm,
                   out_eec_dose_bird_se_md, out_eec_dose_bird_se_lg,
                   out_eec_dose_bird_sg_sm_exp, out_eec_dose_bird_sg_md_exp, out_eec_dose_bird_sg_lg_exp, out_eec_dose_bird_tg_sm_exp,
                   out_eec_dose_bird_tg_md_exp, out_eec_dose_bird_tg_lg_exp, out_eec_dose_bird_bp_sm_exp, out_eec_dose_bird_bp_md_exp,
                   out_eec_dose_bird_bp_lg_exp, out_eec_dose_bird_fp_sm_exp, out_eec_dose_bird_fp_md_exp, out_eec_dose_bird_fp_lg_exp,
                   out_eec_dose_bird_ar_sm_exp, out_eec_dose_bird_ar_md_exp, out_eec_dose_bird_ar_lg_exp, out_eec_dose_bird_se_sm_exp,
                   out_eec_dose_bird_se_md_exp, out_eec_dose_bird_se_lg_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value',
                 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods', 'Fruits/Pods', 'Arthropods', 'Arthropods', 'Seeds',
                               'Seeds', ],
        "Small": ['{0:.2e}'.format(out_eec_dose_bird_sg_sm[0]), '{0:.2e}'.format(out_eec_dose_bird_sg_sm_exp), '{0:.2e}'.format(out_eec_dose_bird_tg_sm[0]),
                  '{0:.2e}'.format(out_eec_dose_bird_tg_sm_exp), '{0:.2e}'.format(out_eec_dose_bird_bp_sm[0]), '{0:.2e}'.format(out_eec_dose_bird_bp_sm_exp),
                  '{0:.2e}'.format(out_eec_dose_bird_fp_sm[0]), '{0:.2e}'.format(out_eec_dose_bird_fp_sm_exp), '{0:.2e}'.format(out_eec_dose_bird_ar_sm[0]),
                  '{0:.2e}'.format(out_eec_dose_bird_ar_sm_exp), '{0:.2e}'.format(out_eec_dose_bird_se_sm[0]), '{0:.2e}'.format(out_eec_dose_bird_se_sm_exp)],
        "Medium": ['{0:.2e}'.format(out_eec_dose_bird_sg_md[0]), '{0:.2e}'.format(out_eec_dose_bird_sg_md_exp), '{0:.2e}'.format(out_eec_dose_bird_tg_md[0]),
                   '{0:.2e}'.format(out_eec_dose_bird_tg_md_exp), '{0:.2e}'.format(out_eec_dose_bird_bp_md[0]), '{0:.2e}'.format(out_eec_dose_bird_bp_md_exp),
                   '{0:.2e}'.format(out_eec_dose_bird_fp_md[0]), '{0:.2e}'.format(out_eec_dose_bird_fp_md_exp), '{0:.2e}'.format(out_eec_dose_bird_ar_md[0]),
                   '{0:.2e}'.format(out_eec_dose_bird_ar_md_exp), '{0:.2e}'.format(out_eec_dose_bird_se_md[0]), '{0:.2e}'.format(out_eec_dose_bird_se_md_exp)],
        "Large": ['{0:.2e}'.format(out_eec_dose_bird_sg_lg[0]), '{0:.2e}'.format(out_eec_dose_bird_sg_lg_exp), '{0:.2e}'.format(out_eec_dose_bird_tg_lg[0]),
                  '{0:.2e}'.format(out_eec_dose_bird_tg_lg_exp), '{0:.2e}'.format(out_eec_dose_bird_bp_lg[0]), '{0:.2e}'.format(out_eec_dose_bird_bp_lg_exp),
                  '{0:.2e}'.format(out_eec_dose_bird_fp_lg[0]), '{0:.2e}'.format(out_eec_dose_bird_fp_lg_exp), '{0:.2e}'.format(out_eec_dose_bird_ar_lg[0]),
                  '{0:.2e}'.format(out_eec_dose_bird_ar_lg_exp), '{0:.2e}'.format(out_eec_dose_bird_se_lg[0]), '{0:.2e}'.format(out_eec_dose_bird_se_lg_exp)],
    }
    return data


def gett7_add_data_qaqc(out_arq_bird_sg_sm, out_arq_bird_sg_md, out_arq_bird_sg_lg, out_arq_bird_tg_sm, out_arq_bird_tg_md, out_arq_bird_tg_lg,
                        out_arq_bird_bp_sm, out_arq_bird_bp_md, out_arq_bird_bp_lg, out_arq_bird_fp_sm, out_arq_bird_fp_md, out_arq_bird_fp_lg,
                        out_arq_bird_ar_sm, out_arq_bird_ar_md, out_arq_bird_ar_lg, out_arq_bird_se_sm, out_arq_bird_se_md, out_arq_bird_se_lg,
                        out_arq_bird_sg_sm_exp, out_arq_bird_sg_md_exp, out_arq_bird_sg_lg_exp, out_arq_bird_tg_sm_exp,
                        out_arq_bird_tg_md_exp, out_arq_bird_tg_lg_exp, out_arq_bird_bp_sm_exp, out_arq_bird_bp_md_exp,
                        out_arq_bird_bp_lg_exp, out_arq_bird_fp_sm_exp, out_arq_bird_fp_md_exp, out_arq_bird_fp_lg_exp,
                        out_arq_bird_ar_sm_exp, out_arq_bird_ar_md_exp, out_arq_bird_ar_lg_exp, out_arq_bird_se_sm_exp,
                        out_arq_bird_se_md_exp, out_arq_bird_se_lg_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value',
                 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods', 'Fruits/Pods', 'Arthropods', 'Arthropods', 'Seeds',
                               'Seeds', ],
        "Small": ['{0:.2e}'.format(out_arq_bird_sg_sm), '{0:.2e}'.format(out_arq_bird_sg_sm_exp), '{0:.2e}'.format(out_arq_bird_tg_sm),
                  '{0:.2e}'.format(out_arq_bird_tg_sm_exp), '{0:.2e}'.format(out_arq_bird_bp_sm), '{0:.2e}'.format(out_arq_bird_bp_sm_exp),
                  '{0:.2e}'.format(out_arq_bird_fp_sm), '{0:.2e}'.format(out_arq_bird_fp_sm_exp), '{0:.2e}'.format(out_arq_bird_ar_sm),
                  '{0:.2e}'.format(out_arq_bird_ar_sm_exp), '{0:.2e}'.format(out_arq_bird_se_sm), '{0:.2e}'.format(out_arq_bird_se_sm_exp)],
        "Medium": ['{0:.2e}'.format(out_arq_bird_sg_md), '{0:.2e}'.format(out_arq_bird_sg_md_exp), '{0:.2e}'.format(out_arq_bird_tg_md),
                   '{0:.2e}'.format(out_arq_bird_tg_md_exp), '{0:.2e}'.format(out_arq_bird_bp_md), '{0:.2e}'.format(out_arq_bird_bp_md_exp),
                   '{0:.2e}'.format(out_arq_bird_fp_md), '{0:.2e}'.format(out_arq_bird_fp_md_exp), '{0:.2e}'.format(out_arq_bird_ar_md),
                   '{0:.2e}'.format(out_arq_bird_ar_md_exp), '{0:.2e}'.format(out_arq_bird_se_md), '{0:.2e}'.format(out_arq_bird_se_md_exp)],
        "Large": ['{0:.2e}'.format(out_arq_bird_sg_lg), '{0:.2e}'.format(out_arq_bird_sg_lg_exp), '{0:.2e}'.format(out_arq_bird_tg_lg),
                  '{0:.2e}'.format(out_arq_bird_tg_lg_exp), '{0:.2e}'.format(out_arq_bird_bp_lg), '{0:.2e}'.format(out_arq_bird_bp_lg_exp),
                  '{0:.2e}'.format(out_arq_bird_fp_lg), '{0:.2e}'.format(out_arq_bird_fp_lg_exp), '{0:.2e}'.format(out_arq_bird_ar_lg),
                  '{0:.2e}'.format(out_arq_bird_ar_lg_exp), '{0:.2e}'.format(out_arq_bird_se_lg), '{0:.2e}'.format(out_arq_bird_se_lg_exp)],
    }
    return data


def gett8data_qaqc(out_arq_diet_bird_sg_a, out_arq_diet_bird_sg_c, out_arq_diet_bird_tg_a, out_arq_diet_bird_tg_c, out_arq_diet_bird_bp_a,
                   out_arq_diet_bird_bp_c, out_arq_diet_bird_fp_a, out_arq_diet_bird_fp_c, out_arq_diet_bird_ar_a, out_arq_diet_bird_ar_c,
                   out_arq_diet_bird_sg_a_exp, out_arq_diet_bird_sg_c_exp, out_arq_diet_bird_tg_a_exp, out_arq_diet_bird_tg_c_exp,
                   out_arq_diet_bird_bp_a_exp, out_arq_diet_bird_bp_c_exp, out_arq_diet_bird_fp_a_exp, out_arq_diet_bird_fp_c_exp,
                   out_arq_diet_bird_ar_a_exp, out_arq_diet_bird_ar_c_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods', 'Fruits/Pods', 'Arthropods', 'Arthropods', ],
        "Acute": ['{0:.2e}'.format(out_arq_diet_bird_sg_a), '{0:.2e}'.format(out_arq_diet_bird_sg_a_exp), '{0:.2e}'.format(out_arq_diet_bird_tg_a),
                  '{0:.2e}'.format(out_arq_diet_bird_tg_a_exp), '{0:.2e}'.format(out_arq_diet_bird_bp_a), '{0:.2e}'.format(out_arq_diet_bird_bp_a_exp),
                  '{0:.2e}'.format(out_arq_diet_bird_fp_a), '{0:.2e}'.format(out_arq_diet_bird_fp_a_exp), '{0:.2e}'.format(out_arq_diet_bird_ar_a),
                  '{0:.2e}'.format(out_arq_diet_bird_ar_a_exp), ],
        "Chronic": ['{0:.2e}'.format(out_arq_diet_bird_sg_c), '{0:.2e}'.format(out_arq_diet_bird_sg_c_exp), '{0:.2e}'.format(out_arq_diet_bird_tg_c),
                    '{0:.2e}'.format(out_arq_diet_bird_tg_c_exp), '{0:.2e}'.format(out_arq_diet_bird_bp_c), '{0:.2e}'.format(out_arq_diet_bird_bp_c_exp),
                    '{0:.2e}'.format(out_arq_diet_bird_fp_c), '{0:.2e}'.format(out_arq_diet_bird_fp_c_exp), '{0:.2e}'.format(out_arq_diet_bird_ar_c),
                    '{0:.2e}'.format(out_arq_diet_bird_ar_c_exp), ],
    }
    return data


def gett9data_qaqc(out_eec_dose_mamm_sg_sm, out_eec_dose_mamm_sg_md, out_eec_dose_mamm_sg_lg, out_eec_dose_mamm_tg_sm,
                   out_eec_dose_mamm_tg_md, out_eec_dose_mamm_tg_lg, out_eec_dose_mamm_bp_sm, out_eec_dose_mamm_bp_md,
                   out_eec_dose_mamm_bp_lg, out_eec_dose_mamm_fp_sm, out_eec_dose_mamm_fp_md, out_eec_dose_mamm_fp_lg,
                   out_eec_dose_mamm_ar_sm, out_eec_dose_mamm_ar_md, out_eec_dose_mamm_ar_lg, out_eec_dose_mamm_se_sm,
                   out_eec_dose_mamm_se_md, out_eec_dose_mamm_se_lg,
                   out_eec_dose_mamm_sg_sm_exp, out_eec_dose_mamm_sg_md_exp, out_eec_dose_mamm_sg_lg_exp, out_eec_dose_mamm_tg_sm_exp,
                   out_eec_dose_mamm_tg_md_exp, out_eec_dose_mamm_tg_lg_exp, out_eec_dose_mamm_bp_sm_exp, out_eec_dose_mamm_bp_md_exp,
                   out_eec_dose_mamm_bp_lg_exp, out_eec_dose_mamm_fp_sm_exp, out_eec_dose_mamm_fp_md_exp, out_eec_dose_mamm_fp_lg_exp,
                   out_eec_dose_mamm_ar_sm_exp, out_eec_dose_mamm_ar_md_exp, out_eec_dose_mamm_ar_lg_exp, out_eec_dose_mamm_se_sm_exp,
                   out_eec_dose_mamm_se_md_exp, out_eec_dose_mamm_se_lg_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value',
                 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods', 'Fruits/Pods', 'Arthropods', 'Arthropods', 'Seeds',
                               'Seeds', ],
        "Small": ['{0:.2e}'.format(out_eec_dose_mamm_sg_sm), '{0:.2e}'.format(out_eec_dose_mamm_sg_sm_exp), '{0:.2e}'.format(out_eec_dose_mamm_tg_sm),
                  '{0:.2e}'.format(out_eec_dose_mamm_tg_sm_exp), '{0:.2e}'.format(out_eec_dose_mamm_bp_sm), '{0:.2e}'.format(out_eec_dose_mamm_bp_sm_exp),
                  '{0:.2e}'.format(out_eec_dose_mamm_fp_sm), '{0:.2e}'.format(out_eec_dose_mamm_fp_sm_exp), '{0:.2e}'.format(out_eec_dose_mamm_ar_sm),
                  '{0:.2e}'.format(out_eec_dose_mamm_ar_sm_exp), '{0:.2e}'.format(out_eec_dose_mamm_se_sm), '{0:.2e}'.format(out_eec_dose_mamm_se_sm_exp)],
        "Medium": ['{0:.2e}'.format(out_eec_dose_mamm_sg_md), '{0:.2e}'.format(out_eec_dose_mamm_sg_md_exp), '{0:.2e}'.format(out_eec_dose_mamm_tg_md),
                   '{0:.2e}'.format(out_eec_dose_mamm_tg_md_exp), '{0:.2e}'.format(out_eec_dose_mamm_bp_md), '{0:.2e}'.format(out_eec_dose_mamm_bp_md_exp),
                   '{0:.2e}'.format(out_eec_dose_mamm_fp_md), '{0:.2e}'.format(out_eec_dose_mamm_fp_md_exp), '{0:.2e}'.format(out_eec_dose_mamm_ar_md),
                   '{0:.2e}'.format(out_eec_dose_mamm_ar_md_exp), '{0:.2e}'.format(out_eec_dose_mamm_se_md), '{0:.2e}'.format(out_eec_dose_mamm_se_md_exp)],
        "Large": ['{0:.2e}'.format(out_eec_dose_mamm_sg_lg), '{0:.2e}'.format(out_eec_dose_mamm_sg_lg_exp), '{0:.2e}'.format(out_eec_dose_mamm_tg_lg),
                  '{0:.2e}'.format(out_eec_dose_mamm_tg_lg_exp), '{0:.2e}'.format(out_eec_dose_mamm_bp_lg), '{0:.2e}'.format(out_eec_dose_mamm_bp_lg_exp),
                  '{0:.2e}'.format(out_eec_dose_mamm_fp_lg), '{0:.2e}'.format(out_eec_dose_mamm_fp_lg_exp), '{0:.2e}'.format(out_eec_dose_mamm_ar_lg),
                  '{0:.2e}'.format(out_eec_dose_mamm_ar_lg_exp), '{0:.2e}'.format(out_eec_dose_mamm_se_lg), '{0:.2e}'.format(out_eec_dose_mamm_se_lg_exp)],
    }
    return data


def gett10data_qaqc(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md, out_crq_dose_mamm_sg_md,
                    out_arq_dose_mamm_sg_lg, out_crq_dose_mamm_sg_lg, out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm,
                    out_arq_dose_mamm_tg_md, out_crq_dose_mamm_tg_md, out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg,
                    out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md, out_crq_dose_mamm_bp_md,
                    out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg, out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm,
                    out_arq_dose_mamm_fp_md, out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg,
                    out_arq_dose_mamm_ar_sm, out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md, out_crq_dose_mamm_ar_md,
                    out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg, out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm,
                    out_arq_dose_mamm_se_md, out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg, out_crq_dose_mamm_se_lg,
                    out_arq_dose_mamm_sg_sm_exp, out_crq_dose_mamm_sg_sm_exp, out_arq_dose_mamm_sg_md_exp, out_crq_dose_mamm_sg_md_exp,
                    out_arq_dose_mamm_sg_lg_exp, out_crq_dose_mamm_sg_lg_exp, out_arq_dose_mamm_tg_sm_exp, out_crq_dose_mamm_tg_sm_exp,
                    out_arq_dose_mamm_tg_md_exp, out_crq_dose_mamm_tg_md_exp, out_arq_dose_mamm_tg_lg_exp, out_crq_dose_mamm_tg_lg_exp,
                    out_arq_dose_mamm_bp_sm_exp, out_crq_dose_mamm_bp_sm_exp, out_arq_dose_mamm_bp_md_exp, out_crq_dose_mamm_bp_md_exp,
                    out_arq_dose_mamm_bp_lg_exp, out_crq_dose_mamm_bp_lg_exp, out_arq_dose_mamm_fp_sm_exp, out_crq_dose_mamm_fp_sm_exp,
                    out_arq_dose_mamm_fp_md_exp, out_crq_dose_mamm_fp_md_exp, out_arq_dose_mamm_fp_lg_exp, out_crq_dose_mamm_fp_lg_exp,
                    out_arq_dose_mamm_ar_sm_exp, out_crq_dose_mamm_ar_sm_exp, out_arq_dose_mamm_ar_md_exp, out_crq_dose_mamm_ar_md_exp,
                    out_arq_dose_mamm_ar_lg_exp, out_crq_dose_mamm_ar_lg_exp, out_arq_dose_mamm_se_sm_exp, out_crq_dose_mamm_se_sm_exp,
                    out_arq_dose_mamm_se_md_exp, out_crq_dose_mamm_se_md_exp, out_arq_dose_mamm_se_lg_exp, out_crq_dose_mamm_se_lg_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value',
                 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods', 'Fruits/Pods', 'Arthropods', 'Arthropods', 'Seeds',
                               'Seeds', ],
        "Acute_sm": ['{0:.2e}'.format(out_arq_dose_mamm_sg_sm), '{0:.2e}'.format(out_arq_dose_mamm_sg_sm_exp), '{0:.2e}'.format(out_arq_dose_mamm_tg_sm),
                     '{0:.2e}'.format(out_arq_dose_mamm_tg_sm_exp), '{0:.2e}'.format(out_arq_dose_mamm_bp_sm),
                     '{0:.2e}'.format(out_arq_dose_mamm_bp_sm_exp), '{0:.2e}'.format(out_arq_dose_mamm_fp_sm),
                     '{0:.2e}'.format(out_arq_dose_mamm_fp_sm_exp), '{0:.2e}'.format(out_arq_dose_mamm_ar_sm),
                     '{0:.2e}'.format(out_arq_dose_mamm_ar_sm_exp), '{0:.2e}'.format(out_arq_dose_mamm_se_sm),
                     '{0:.2e}'.format(out_arq_dose_mamm_se_sm_exp)],
        "Chronic_sm": ['{0:.2e}'.format(out_crq_dose_mamm_sg_sm), '{0:.2e}'.format(out_crq_dose_mamm_sg_sm_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_tg_sm), '{0:.2e}'.format(out_crq_dose_mamm_tg_sm_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_bp_sm), '{0:.2e}'.format(out_crq_dose_mamm_bp_sm_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_fp_sm), '{0:.2e}'.format(out_crq_dose_mamm_fp_sm_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_ar_sm), '{0:.2e}'.format(out_crq_dose_mamm_ar_sm_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_se_sm), '{0:.2e}'.format(out_crq_dose_mamm_se_sm_exp)],
        "Acute_md": ['{0:.2e}'.format(out_arq_dose_mamm_sg_md), '{0:.2e}'.format(out_arq_dose_mamm_sg_md_exp), '{0:.2e}'.format(out_arq_dose_mamm_tg_md),
                     '{0:.2e}'.format(out_arq_dose_mamm_tg_md_exp), '{0:.2e}'.format(out_arq_dose_mamm_bp_md),
                     '{0:.2e}'.format(out_arq_dose_mamm_bp_md_exp), '{0:.2e}'.format(out_arq_dose_mamm_fp_md),
                     '{0:.2e}'.format(out_arq_dose_mamm_fp_md_exp), '{0:.2e}'.format(out_arq_dose_mamm_ar_md),
                     '{0:.2e}'.format(out_arq_dose_mamm_ar_md_exp), '{0:.2e}'.format(out_arq_dose_mamm_se_md),
                     '{0:.2e}'.format(out_arq_dose_mamm_se_md_exp)],
        "Chronic_md": ['{0:.2e}'.format(out_crq_dose_mamm_sg_md), '{0:.2e}'.format(out_crq_dose_mamm_sg_md_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_tg_md), '{0:.2e}'.format(out_crq_dose_mamm_tg_md_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_bp_md), '{0:.2e}'.format(out_crq_dose_mamm_bp_md_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_fp_md), '{0:.2e}'.format(out_crq_dose_mamm_fp_md_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_ar_md), '{0:.2e}'.format(out_crq_dose_mamm_ar_md_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_se_md), '{0:.2e}'.format(out_crq_dose_mamm_se_md_exp)],
        "Acute_lg": ['{0:.2e}'.format(out_arq_dose_mamm_sg_lg), '{0:.2e}'.format(out_arq_dose_mamm_sg_lg_exp), '{0:.2e}'.format(out_arq_dose_mamm_tg_lg),
                     '{0:.2e}'.format(out_arq_dose_mamm_tg_lg_exp), '{0:.2e}'.format(out_arq_dose_mamm_bp_lg),
                     '{0:.2e}'.format(out_arq_dose_mamm_bp_lg_exp), '{0:.2e}'.format(out_arq_dose_mamm_fp_lg),
                     '{0:.2e}'.format(out_arq_dose_mamm_fp_lg_exp), '{0:.2e}'.format(out_arq_dose_mamm_ar_lg),
                     '{0:.2e}'.format(out_arq_dose_mamm_ar_lg_exp), '{0:.2e}'.format(out_arq_dose_mamm_se_lg),
                     '{0:.2e}'.format(out_arq_dose_mamm_se_lg_exp)],
        "Chronic_lg": ['{0:.2e}'.format(out_crq_dose_mamm_sg_lg), '{0:.2e}'.format(out_crq_dose_mamm_sg_lg_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_tg_lg), '{0:.2e}'.format(out_crq_dose_mamm_tg_lg_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_bp_lg), '{0:.2e}'.format(out_crq_dose_mamm_bp_lg_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_fp_lg), '{0:.2e}'.format(out_crq_dose_mamm_fp_lg_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_ar_lg), '{0:.2e}'.format(out_crq_dose_mamm_ar_lg_exp),
                       '{0:.2e}'.format(out_crq_dose_mamm_se_lg), '{0:.2e}'.format(out_crq_dose_mamm_se_lg_exp)],
    }
    return data


def gett11data_na_qaqc(out_arq_diet_mamm_sg, out_crq_diet_bird_sg, out_arq_diet_mamm_tg, out_crq_diet_bird_tg, out_arq_diet_mamm_bp,
                       out_crq_diet_bird_bp, out_arq_diet_mamm_fp, out_crq_diet_bird_fp, out_arq_diet_mamm_ar, out_crq_diet_bird_ar,
                       out_arq_diet_mamm_sg_exp, out_crq_diet_bird_sg_exp, out_arq_diet_mamm_tg_exp, out_crq_diet_bird_tg_exp,
                       out_arq_diet_mamm_bp_exp, out_crq_diet_bird_bp_exp, out_arq_diet_mamm_fp_exp, out_crq_diet_bird_fp_exp,
                       out_arq_diet_mamm_ar_exp, out_crq_diet_bird_ar_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', ],
        "Application Target": ['Short Grass', 'Short Grass', 'Tall Grass', 'Tall Grass', 'Broadleaf Plants',
                               'Broadleaf Plants', 'Fruits/Pods/Seeds', 'Fruits/Pods/Seeds', 'Arthropods',
                               'Arthropods'],
        "Acute": ['{0!s}'.format(out_arq_diet_mamm_sg), '{0!s}'.format(out_arq_diet_mamm_sg_exp), '{0!s}'.format(out_arq_diet_mamm_tg),
                  '{0!s}'.format(out_arq_diet_mamm_tg_exp), '{0!s}'.format(out_arq_diet_mamm_bp), '{0!s}'.format(out_arq_diet_mamm_bp_exp),
                  '{0!s}'.format(out_arq_diet_mamm_fp), '{0!s}'.format(out_arq_diet_mamm_fp_exp), '{0!s}'.format(out_arq_diet_mamm_ar),
                  '{0!s}'.format(out_arq_diet_mamm_ar_exp)],
        "Chronic": ['{0:.2e}'.format(out_crq_diet_bird_sg), '{0:.2e}'.format(out_crq_diet_bird_sg_exp), '{0:.2e}'.format(out_crq_diet_bird_tg),
                    '{0:.2e}'.format(out_crq_diet_bird_tg_exp), '{0:.2e}'.format(out_crq_diet_bird_bp), '{0:.2e}'.format(out_crq_diet_bird_bp_exp),
                    '{0:.2e}'.format(out_crq_diet_bird_fp), '{0:.2e}'.format(out_crq_diet_bird_fp_exp), '{0:.2e}'.format(out_crq_diet_bird_ar),
                    '{0:.2e}'.format(out_crq_diet_bird_ar_exp)],
    }
    return data


def gett12data_qaqc(out_ld50_rg_bird_sm, out_ld50_rg_mamm_sm, out_ld50_rg_bird_md, out_ld50_rg_mamm_md, out_ld50_rg_bird_lg,
                    out_ld50_rg_mamm_lg,
                    out_ld50_rg_bird_sm_exp, out_ld50_rg_mamm_sm_exp, out_ld50_rg_bird_md_exp, out_ld50_rg_mamm_md_exp,
                    out_ld50_rg_bird_lg_exp, out_ld50_rg_mamm_lg_exp):
    data = {
        "Type": ['Calculated Value', 'Expected Value', 'Calculated Value', 'Expected Value', 'Calculated Value',
                 'Expected Value', ], "Animal Size": ['Small', 'Small', 'Medium', 'Medium', 'Large', 'Large', ],
        "Avian": ['{0:.2e}'.format(out_ld50_rg_bird_sm), '{0:.2e}'.format(out_ld50_rg_bird_sm_exp), '{0:.2e}'.format(out_ld50_rg_bird_md),
                  '{0:.2e}'.format(out_ld50_rg_bird_md_exp), '{0:.2e}'.format(out_ld50_rg_bird_lg), '{0:.2e}'.format(out_ld50_rg_bird_lg_exp), ],
        "Mammal": ['{0:.2e}'.format(out_ld50_rg_mamm_sm), '{0:.2e}'.format(out_ld50_rg_mamm_sm_exp), '{0:.2e}'.format(out_ld50_rg_mamm_md),
                   '{0:.2e}'.format(out_ld50_rg_mamm_md_exp), '{0:.2e}'.format(out_ld50_rg_mamm_lg), '{0:.2e}'.format(out_ld50_rg_mamm_lg_exp), ],
    }
    return data


def gettsumdata_1(a_i, max_seed_rate, b_w, percent_incorp, den, Foliar_dissipation_half_life, num_apps, rate_out_t):
    if 'N/A' in percent_incorp:
        percent_incorp_mean = 'N/A'
        percent_incorp_std = 'N/A'
        percent_incorp_min = 'N/A'
        percent_incorp_max = 'N/A'
    else:
        percent_incorp_mean = '{0:.2e}'.format(np.mean(percent_incorp))
        percent_incorp_std = '{0:.2e}'.format(np.std(percent_incorp))
        percent_incorp_min = '{0:.2e}'.format(np.min(percent_incorp))
        percent_incorp_max = '{0:.2e}'.format(np.max(percent_incorp))
    data = {
        "Parameter": ['Percentage active ingredient', 'Row spacing', 'Bandwidth', 'Percentage incorporated',
                      'Density of product', 'Foliar dissipation half-life', 'Number of application',
                      'Application rate', ],
        "Mean": ['{0:.2e}'.format(np.mean(a_i)), '{0:.2e}'.format(np.mean(max_seed_rate)), '{0:.2e}'.format(np.mean(b_w)), percent_incorp_mean, '{0:.2e}'.format(np.mean(den)),
                 '{0:.2e}'.format(np.mean(Foliar_dissipation_half_life)), '{0:.2e}'.format(np.mean(num_apps)), '{0:.2e}'.format(np.mean(rate_out_t)), ],
        "Std": ['{0:.2e}'.format(np.std(a_i)), '{0:.2e}'.format(np.mean(max_seed_rate)), '{0:.2e}'.format(np.mean(b_w)), percent_incorp_std, '{0:.2e}'.format(np.mean(den)),
                '{0:.2e}'.format(np.std(Foliar_dissipation_half_life)), '{0:.2e}'.format(np.std(num_apps)), '{0:.2e}'.format(np.std(rate_out_t)), ],
        "Min": ['{0:.2e}'.format(np.min(a_i)), '{0:.2e}'.format(np.mean(max_seed_rate)), '{0:.2e}'.format(np.mean(b_w)), percent_incorp_min, '{0:.2e}'.format(np.mean(den)),
                '{0:.2e}'.format(np.min(Foliar_dissipation_half_life)), '{0:.2e}'.format(np.min(num_apps)), '{0:.2e}'.format(np.min(rate_out_t)), ],
        "Max": ['{0:.2e}'.format(np.max(a_i)), '{0:.2e}'.format(np.mean(max_seed_rate)), '{0:.2e}'.format(np.mean(b_w)), percent_incorp_max, '{0:.2e}'.format(np.mean(den)),
                '{0:.2e}'.format(np.max(Foliar_dissipation_half_life)), '{0:.2e}'.format(np.max(num_apps)), '{0:.2e}'.format(np.max(rate_out_t)), ],
        "Unit": ['%', 'inch', 'inch', '%', 'lbs/gal', 'days', '', ],
    }
    return data


def gettsumdata_2(avian_ld50, avian_lc50, avian_NOAEC, avian_NOAEL, bw_assessed_bird_s, bw_assessed_bird_m,
                  bw_assessed_bird_l, tw_bird_ld50, tw_bird_lc50, tw_bird_noaec, tw_bird_noael, mineau_scaling_factor):
    if 'N/A' in avian_NOAEL:
        avian_lc50_mean = 'N/A'
        avian_lc50_std = 'N/A'
        avian_lc50_min = 'N/A'
        avian_lc50_max = 'N/A'
    else:
        avian_lc50_mean = '{0:.2e}'.format(np.mean(avian_lc50))
        avian_lc50_std = '{0:.2e}'.format(np.std(avian_lc50))
        avian_lc50_min = '{0:.2e}'.format(np.min(avian_lc50))
        avian_lc50_max = '{0:.2e}'.format(np.max(avian_lc50))

    data = {
        "Parameter": ['Avian LD50', 'Weight (LD50)', 'Avian LC50', 'Weight (LC50)',
                      'Avian NOAEC', 'Weight (NOAEC)', 'Avian NOAEL', 'Weight (NOAEL)',
                      'Body weight of assessed bird small', 'Body weight of assessed bird medium',
                      'Body weight of assessed bird large',
                      'Mineau scaling factor', ],
        "Mean": ['{0:.2e}'.format(np.mean(avian_ld50)), '{0:.2e}'.format(np.mean(tw_bird_ld50)), avian_lc50_mean,
                 '{0:.2e}'.format(np.mean(tw_bird_lc50)), '{0:.2e}'.format(np.mean(avian_NOAEC)), '{0:.2e}'.format(np.mean(tw_bird_noaec)),
                 '{0:.2e}'.format(np.mean(avian_NOAEL)), '{0:.2e}'.format(np.mean(tw_bird_noael)), '{0:.2e}'.format(np.mean(bw_assessed_bird_s)),
                 '{0:.2e}'.format(np.mean(bw_assessed_bird_m)), '{0:.2e}'.format(np.mean(bw_assessed_bird_l)),
                 '{0:.2e}'.format(np.mean(mineau_scaling_factor)), ],
        "Std": ['{0:.2e}'.format(np.std(avian_ld50)), '{0:.2e}'.format(np.std(tw_bird_ld50)), avian_lc50_std,
                '{0:.2e}'.format(np.std(tw_bird_lc50)), '{0:.2e}'.format(np.std(avian_NOAEC)), '{0:.2e}'.format(np.std(tw_bird_noaec)),
                '{0:.2e}'.format(np.std(avian_NOAEL)), '{0:.2e}'.format(np.std(tw_bird_noael)), '{0:.2e}'.format(np.std(bw_assessed_bird_s)),
                '{0:.2e}'.format(np.std(bw_assessed_bird_m)), '{0:.2e}'.format(np.std(bw_assessed_bird_l)),
                '{0:.2e}'.format(np.std(mineau_scaling_factor)), ],
        "Min": ['{0:.2e}'.format(np.min(avian_ld50)), '{0:.2e}'.format(np.min(tw_bird_ld50)), avian_lc50_min,
                '{0:.2e}'.format(np.min(tw_bird_lc50)), '{0:.2e}'.format(np.min(avian_NOAEC)), '{0:.2e}'.format(np.min(tw_bird_noaec)),
                '{0:.2e}'.format(np.min(avian_NOAEL)), '{0:.2e}'.format(np.min(tw_bird_noael)), '{0:.2e}'.format(np.min(bw_assessed_bird_s)),
                '{0:.2e}'.format(np.min(bw_assessed_bird_m)), '{0:.2e}'.format(np.min(bw_assessed_bird_l)),
                '{0:.2e}'.format(np.min(mineau_scaling_factor)), ],
        "Max": ['{0:.2e}'.format(np.max(avian_ld50)), '{0:.2e}'.format(np.max(tw_bird_ld50)), avian_lc50_max,
                '{0:.2e}'.format(np.max(tw_bird_lc50)), '{0:.2e}'.format(np.max(avian_NOAEC)), '{0:.2e}'.format(np.max(tw_bird_noaec)),
                '{0:.2e}'.format(np.max(avian_NOAEL)), '{0:.2e}'.format(np.max(tw_bird_noael)), '{0:.2e}'.format(np.max(bw_assessed_bird_s)),
                '{0:.2e}'.format(np.max(bw_assessed_bird_m)), '{0:.2e}'.format(np.max(bw_assessed_bird_l)),
                '{0:.2e}'.format(np.max(mineau_scaling_factor)), ],
        "Unit": ['mg/kg-bw', 'g', 'mg/kg-diet', 'g', 'mg/kg-diet', 'g', 'mg/kg-bw', 'g', 'g', 'g', 'g', '', ],
    }
    return data


def gettsumdata_3(mammalian_ld50, mammalian_lc50, mammalian_NOAEC, mammalian_NOAEL, bw_assessed_mamm_s,
                  bw_assessed_mamm_m,
                  bw_assessed_mamm_l, bw_tested_mamm):
    if 'N/A' in mammalian_lc50:
        mammalian_lc50_mean = 'N/A'
        mammalian_lc50_std = 'N/A'
        mammalian_lc50_min = 'N/A'
        mammalian_lc50_max = 'N/A'
    else:
        mammalian_lc50_mean = '{0:.2e}'.format(np.mean(mammalian_lc50))
        mammalian_lc50_std = '{0:.2e}'.format(np.std(mammalian_lc50))
        mammalian_lc50_min = '{0:.2e}'.format(np.min(mammalian_lc50))
        mammalian_lc50_max = '{0:.2e}'.format(np.max(mammalian_lc50))

    data = {
        "Parameter": ['Mammalian LD50', 'Mammalian LC50', 'Mammalian NOAEC', 'Mammalian NOAEL',
                      'Body weight of assessed mammal small',
                      'Body weight of assessed mammal medium', 'Body weight of assessed mammal large',
                      'Body weight of tested mammal', ],
        "Mean": ['{0:.2e}'.format(np.mean(mammalian_ld50)), mammalian_lc50_mean, '{0:.2e}'.format(np.mean(mammalian_NOAEC)),
                 '{0:.2e}'.format(np.mean(mammalian_NOAEL)), '{0:.2e}'.format(np.mean(bw_assessed_mamm_s)),
                 '{0:.2e}'.format(np.mean(bw_assessed_mamm_m)), '{0:.2e}'.format(np.mean(bw_assessed_mamm_l)),
                 '{0:.2e}'.format(np.mean(bw_tested_mamm)), ],
        "Std": ['{0:.2e}'.format(np.std(mammalian_ld50)), mammalian_lc50_std, '{0:.2e}'.format(np.std(mammalian_NOAEC)),
                '{0:.2e}'.format(np.std(mammalian_NOAEL)), '{0:.2e}'.format(np.std(bw_assessed_mamm_s)),
                '{0:.2e}'.format(np.std(bw_assessed_mamm_m)), '{0:.2e}'.format(np.std(bw_assessed_mamm_l)),
                '{0:.2e}'.format(np.std(bw_tested_mamm)), ],
        "Min": ['{0:.2e}'.format(np.min(mammalian_ld50)), mammalian_lc50_min, '{0:.2e}'.format(np.min(mammalian_NOAEC)),
                '{0:.2e}'.format(np.min(mammalian_NOAEL)), '{0:.2e}'.format(np.min(bw_assessed_mamm_s)),
                '{0:.2e}'.format(np.min(bw_assessed_mamm_m)), '{0:.2e}'.format(np.min(bw_assessed_mamm_l)),
                '{0:.2e}'.format(np.min(bw_tested_mamm)), ],
        "Max": ['{0:.2e}'.format(np.max(mammalian_ld50)), mammalian_lc50_max, '{0:.2e}'.format(np.max(mammalian_NOAEC)),
                '{0:.2e}'.format(np.max(mammalian_NOAEL)), '{0:.2e}'.format(np.max(bw_assessed_mamm_s)),
                '{0:.2e}'.format(np.max(bw_assessed_mamm_m)), '{0:.2e}'.format(np.max(bw_assessed_mamm_l)),
                '{0:.2e}'.format(np.max(bw_tested_mamm)), ],
        "Unit": ['mg/kg-bw', 'mg/kg-diet', 'mg/kg-diet', 'mg/kg-bw', 'g', 'g', 'g', 'g', ],
    }
    return data


def gettsumdata_5(out_sa_bird_1_s_out, out_sa_bird_2_s_out, out_sc_bird_s_out, out_sa_mamm_1_s_out, out_sa_mamm_2_s_out, out_sc_mamm_s_out,
                  out_sa_bird_1_m_out, out_sa_bird_2_m_out, out_sc_bird_m_out, out_sa_mamm_1_m_out, out_sa_mamm_2_m_out, out_sc_mamm_m_out,
                  out_sa_bird_1_l_out, out_sa_bird_2_l_out, out_sc_bird_l_out, out_sa_mamm_1_l_out, out_sa_mamm_2_l_out, out_sc_mamm_l_out):
    data = {
        "Size": ['Small', 'Small', 'Small', 'Small', 'Medium', 'Medium', 'Medium', 'Medium', 'Large', 'Large', 'Large',
                 'Large', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],
        "AAcute #1": ['{0:.2e}'.format(np.mean(out_sa_bird_1_s_out)), '{0:.2e}'.format(np.std(out_sa_bird_1_s_out)),
                      '{0:.2e}'.format(np.min(out_sa_bird_1_s_out)), '{0:.2e}'.format(np.max(out_sa_bird_1_s_out)),
                      '{0:.2e}'.format(np.mean(out_sa_bird_1_m_out)), '{0:.2e}'.format(np.std(out_sa_bird_1_m_out)),
                      '{0:.2e}'.format(np.min(out_sa_bird_1_m_out)), '{0:.2e}'.format(np.max(out_sa_bird_1_m_out)),
                      '{0:.2e}'.format(np.mean(out_sa_bird_1_l_out)), '{0:.2e}'.format(np.std(out_sa_bird_1_l_out)),
                      '{0:.2e}'.format(np.min(out_sa_bird_1_l_out)), '{0:.2e}'.format(np.max(out_sa_bird_1_l_out)), ],

        "AAcute #2": ['{0:.2e}'.format(np.mean(out_sa_bird_2_s_out)), '{0:.2e}'.format(np.std(out_sa_bird_2_s_out)),
                      '{0:.2e}'.format(np.min(out_sa_bird_2_s_out)), '{0:.2e}'.format(np.max(out_sa_bird_2_s_out)),
                      '{0:.2e}'.format(np.mean(out_sa_bird_2_m_out)), '{0:.2e}'.format(np.std(out_sa_bird_2_m_out)),
                      '{0:.2e}'.format(np.min(out_sa_bird_2_m_out)), '{0:.2e}'.format(np.max(out_sa_bird_2_m_out)),
                      '{0:.2e}'.format(np.mean(out_sa_bird_2_l_out)), '{0:.2e}'.format(np.std(out_sa_bird_2_l_out)),
                      '{0:.2e}'.format(np.min(out_sa_bird_2_l_out)), '{0:.2e}'.format(np.max(out_sa_bird_2_l_out)), ],

        "AChronic": ['{0:.2e}'.format(np.mean(out_sc_bird_s_out)), '{0:.2e}'.format(np.std(out_sc_bird_s_out)), '{0:.2e}'.format(np.min(out_sc_bird_s_out)),
                     '{0:.2e}'.format(np.max(out_sc_bird_s_out)),
                     '{0:.2e}'.format(np.mean(out_sc_bird_m_out)), '{0:.2e}'.format(np.std(out_sc_bird_m_out)), '{0:.2e}'.format(np.min(out_sc_bird_m_out)),
                     '{0:.2e}'.format(np.max(out_sc_bird_m_out)),
                     '{0:.2e}'.format(np.mean(out_sc_bird_l_out)), '{0:.2e}'.format(np.std(out_sc_bird_l_out)), '{0:.2e}'.format(np.min(out_sc_bird_l_out)),
                     '{0:.2e}'.format(np.max(out_sc_bird_l_out)), ],

        "MAcute #1": ['{0:.2e}'.format(np.mean(out_sa_mamm_1_s_out)), '{0:.2e}'.format(np.std(out_sa_mamm_1_s_out)),
                      '{0:.2e}'.format(np.min(out_sa_mamm_1_s_out)), '{0:.2e}'.format(np.max(out_sa_mamm_1_s_out)),
                      '{0:.2e}'.format(np.mean(out_sa_mamm_1_m_out)), '{0:.2e}'.format(np.std(out_sa_mamm_1_m_out)),
                      '{0:.2e}'.format(np.min(out_sa_mamm_1_m_out)), '{0:.2e}'.format(np.max(out_sa_mamm_1_m_out)),
                      '{0:.2e}'.format(np.mean(out_sa_mamm_1_l_out)), '{0:.2e}'.format(np.std(out_sa_mamm_1_l_out)),
                      '{0:.2e}'.format(np.min(out_sa_mamm_1_l_out)), '{0:.2e}'.format(np.max(out_sa_mamm_1_l_out)), ],

        "MAcute #2": ['{0:.2e}'.format(np.mean(out_sa_mamm_2_s_out)), '{0:.2e}'.format(np.std(out_sa_mamm_2_s_out)),
                      '{0:.2e}'.format(np.min(out_sa_mamm_2_s_out)), '{0:.2e}'.format(np.max(out_sa_mamm_2_s_out)),
                      '{0:.2e}'.format(np.mean(out_sa_mamm_2_m_out)), '{0:.2e}'.format(np.std(out_sa_mamm_2_m_out)),
                      '{0:.2e}'.format(np.min(out_sa_mamm_2_m_out)), '{0:.2e}'.format(np.max(out_sa_mamm_2_m_out)),
                      '{0:.2e}'.format(np.mean(out_sa_mamm_2_l_out)), '{0:.2e}'.format(np.std(out_sa_mamm_2_l_out)),
                      '{0:.2e}'.format(np.min(out_sa_mamm_2_l_out)), '{0:.2e}'.format(np.max(out_sa_mamm_2_l_out)), ],

        "MChronic": ['{0:.2e}'.format(np.mean(out_sc_mamm_s_out)), '{0:.2e}'.format(np.std(out_sc_mamm_s_out)), '{0:.2e}'.format(np.min(out_sc_mamm_s_out)),
                     '{0:.2e}'.format(np.max(out_sc_mamm_s_out)),
                     '{0:.2e}'.format(np.mean(out_sc_mamm_m_out)), '{0:.2e}'.format(np.std(out_sc_mamm_m_out)), '{0:.2e}'.format(np.min(out_sc_mamm_m_out)),
                     '{0:.2e}'.format(np.max(out_sc_mamm_m_out)),
                     '{0:.2e}'.format(np.mean(out_sc_mamm_l_out)), '{0:.2e}'.format(np.std(out_sc_mamm_l_out)), '{0:.2e}'.format(np.min(out_sc_mamm_l_out)),
                     '{0:.2e}'.format(np.max(out_sc_mamm_l_out)), ],
    }
    return data


def gettsumdata_6(out_eec_diet_sg_RBG_out, out_eec_diet_tg_RBG_out, out_eec_diet_bp_RBG_out, out_eec_diet_fr_RBG_out,
                  out_eec_diet_ar_RBG_out):
    data = {
        "Metric": ['Mean', 'Std', 'Min', 'Max', ],
        "Short Grass": ['{0:.2e}'.format(np.mean(out_eec_diet_sg_RBG_out)), '{0:.2e}'.format(np.std(out_eec_diet_sg_RBG_out)),
                        '{0:.2e}'.format(np.min(out_eec_diet_sg_RBG_out)), '{0:.2e}'.format(np.max(out_eec_diet_sg_RBG_out)), ],
        "Tall Grass": ['{0:.2e}'.format(np.mean(out_eec_diet_tg_RBG_out)), '{0:.2e}'.format(np.std(out_eec_diet_tg_RBG_out)),
                       '{0:.2e}'.format(np.min(out_eec_diet_tg_RBG_out)), '{0:.2e}'.format(np.max(out_eec_diet_tg_RBG_out)), ],
        "Broadleaf Plants": ['{0:.2e}'.format(np.mean(out_eec_diet_bp_RBG_out)), '{0:.2e}'.format(np.std(out_eec_diet_bp_RBG_out)),
                             '{0:.2e}'.format(np.min(out_eec_diet_bp_RBG_out)), '{0:.2e}'.format(np.max(out_eec_diet_bp_RBG_out)), ],
        "Fruits/Pods/Seeds": ['{0:.2e}'.format(np.mean(out_eec_diet_fr_RBG_out)), '{0:.2e}'.format(np.std(out_eec_diet_fr_RBG_out)),
                              '{0:.2e}'.format(np.min(out_eec_diet_fr_RBG_out)), '{0:.2e}'.format(np.max(out_eec_diet_fr_RBG_out)), ],
        "Arthropods": ['{0:.2e}'.format(np.mean(out_eec_diet_ar_RBG_out)), '{0:.2e}'.format(np.std(out_eec_diet_ar_RBG_out)),
                       '{0:.2e}'.format(np.min(out_eec_diet_ar_RBG_out)), '{0:.2e}'.format(np.max(out_eec_diet_ar_RBG_out)), ],
    }
    return data


def gettsumdata_7(out_eec_dose_bird_sg_sm_out, out_eec_dose_bird_sg_md_out, out_eec_dose_bird_sg_lg_out, out_eec_dose_bird_tg_sm_out,
                  out_eec_dose_bird_tg_md_out, out_eec_dose_bird_tg_lg_out, out_eec_dose_bird_bp_sm_out, out_eec_dose_bird_bp_md_out,
                  out_eec_dose_bird_bp_lg_out, out_eec_dose_bird_fp_sm_out, out_eec_dose_bird_fp_md_out, out_eec_dose_bird_fp_lg_out,
                  out_eec_dose_bird_ar_sm_out, out_eec_dose_bird_ar_md_out, out_eec_dose_bird_ar_lg_out, out_eec_dose_bird_se_sm_out,
                  out_eec_dose_bird_se_md_out, out_eec_dose_bird_se_lg_out):
    data = {
        "Animal Size": ['Small', 'Small', 'Small', 'Small', 'Medium', 'Medium', 'Medium', 'Medium', 'Large', 'Large',
                        'Large', 'Large', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],
        "Short Grass": ['{0:.2e}'.format(np.mean(out_eec_dose_bird_sg_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_sg_sm_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_bird_sg_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_sg_sm_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_bird_sg_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_sg_md_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_bird_sg_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_sg_md_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_bird_sg_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_sg_lg_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_bird_sg_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_sg_lg_out)), ],

        "Tall Grass": ['{0:.2e}'.format(np.mean(out_eec_dose_bird_tg_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_tg_sm_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_bird_tg_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_tg_sm_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_bird_tg_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_tg_md_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_bird_tg_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_tg_md_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_bird_tg_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_tg_lg_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_bird_tg_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_tg_lg_out)), ],

        "Broadleaf Plants": ['{0:.2e}'.format(np.mean(out_eec_dose_bird_bp_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_bp_sm_out)),
                             '{0:.2e}'.format(np.min(out_eec_dose_bird_bp_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_bp_sm_out)),
                             '{0:.2e}'.format(np.mean(out_eec_dose_bird_bp_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_bp_md_out)),
                             '{0:.2e}'.format(np.min(out_eec_dose_bird_bp_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_bp_md_out)),
                             '{0:.2e}'.format(np.mean(out_eec_dose_bird_bp_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_bp_lg_out)),
                             '{0:.2e}'.format(np.min(out_eec_dose_bird_bp_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_bp_lg_out)), ],

        "Fruits/Pods": ['{0:.2e}'.format(np.mean(out_eec_dose_bird_fp_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_fp_sm_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_bird_fp_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_fp_sm_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_bird_fp_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_fp_md_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_bird_fp_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_fp_md_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_bird_fp_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_fp_lg_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_bird_fp_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_fp_lg_out)), ],

        "Arthropods": ['{0:.2e}'.format(np.mean(out_eec_dose_bird_ar_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_ar_sm_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_bird_ar_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_ar_sm_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_bird_ar_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_ar_md_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_bird_ar_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_ar_md_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_bird_ar_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_ar_lg_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_bird_ar_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_ar_lg_out)), ],

        "Seeds": ['{0:.2e}'.format(np.mean(out_eec_dose_bird_se_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_se_sm_out)),
                  '{0:.2e}'.format(np.min(out_eec_dose_bird_se_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_se_sm_out)),
                  '{0:.2e}'.format(np.mean(out_eec_dose_bird_se_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_se_md_out)),
                  '{0:.2e}'.format(np.min(out_eec_dose_bird_se_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_se_md_out)),
                  '{0:.2e}'.format(np.mean(out_eec_dose_bird_se_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_bird_se_lg_out)),
                  '{0:.2e}'.format(np.min(out_eec_dose_bird_se_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_bird_se_lg_out)), ],
    }
    return data


def gettsumdata_8(out_arq_diet_bird_sg_a_out, out_arq_diet_bird_sg_c_out, out_arq_diet_bird_tg_a_out, out_arq_diet_bird_tg_c_out,
                  out_arq_diet_bird_bp_a_out, out_arq_diet_bird_bp_c_out, out_arq_diet_bird_fp_a_out, out_arq_diet_bird_fp_c_out,
                  out_arq_diet_bird_ar_a_out, out_arq_diet_bird_ar_c_out):
    data = {
        "Type": ['Acute', 'Acute', 'Acute', 'Acute', 'Chronic', 'Chronic', 'Chronic', 'Chronic', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],
        "Short Grass": ['{0:.2e}'.format(np.mean(out_arq_diet_bird_sg_a_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_sg_a_out)),
                        '{0:.2e}'.format(np.min(out_arq_diet_bird_sg_a_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_sg_a_out)),
                        '{0:.2e}'.format(np.mean(out_arq_diet_bird_sg_c_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_sg_c_out)),
                        '{0:.2e}'.format(np.min(out_arq_diet_bird_sg_c_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_sg_c_out)), ],

        "Tall Grass": ['{0:.2e}'.format(np.mean(out_arq_diet_bird_tg_a_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_tg_a_out)),
                       '{0:.2e}'.format(np.min(out_arq_diet_bird_tg_a_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_tg_a_out)),
                       '{0:.2e}'.format(np.mean(out_arq_diet_bird_tg_c_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_tg_c_out)),
                       '{0:.2e}'.format(np.min(out_arq_diet_bird_tg_c_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_tg_c_out)), ],

        "Broadleaf Plants": ['{0:.2e}'.format(np.mean(out_arq_diet_bird_bp_a_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_bp_a_out)),
                             '{0:.2e}'.format(np.min(out_arq_diet_bird_bp_a_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_bp_a_out)),
                             '{0:.2e}'.format(np.mean(out_arq_diet_bird_bp_c_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_bp_c_out)),
                             '{0:.2e}'.format(np.min(out_arq_diet_bird_bp_c_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_bp_c_out)), ],

        "Fruits/Pods": ['{0:.2e}'.format(np.mean(out_arq_diet_bird_fp_a_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_fp_a_out)),
                        '{0:.2e}'.format(np.min(out_arq_diet_bird_fp_a_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_fp_a_out)),
                        '{0:.2e}'.format(np.mean(out_arq_diet_bird_fp_c_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_fp_c_out)),
                        '{0:.2e}'.format(np.min(out_arq_diet_bird_fp_c_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_fp_c_out)), ],

        "Arthropods": ['{0:.2e}'.format(np.mean(out_arq_diet_bird_ar_a_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_ar_a_out)),
                       '{0:.2e}'.format(np.min(out_arq_diet_bird_ar_a_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_ar_a_out)),
                       '{0:.2e}'.format(np.mean(out_arq_diet_bird_ar_c_out)), '{0:.2e}'.format(np.std(out_arq_diet_bird_ar_c_out)),
                       '{0:.2e}'.format(np.min(out_arq_diet_bird_ar_c_out)), '{0:.2e}'.format(np.max(out_arq_diet_bird_ar_c_out)), ],
    }
    return data


def gettsumdata_9(out_eec_dose_mamm_sg_sm_out, out_eec_dose_mamm_sg_md_out, out_eec_dose_mamm_sg_lg_out, out_eec_dose_mamm_tg_sm_out,
                  out_eec_dose_mamm_tg_md_out, out_eec_dose_mamm_tg_lg_out, out_eec_dose_mamm_bp_sm_out, out_eec_dose_mamm_bp_md_out,
                  out_eec_dose_mamm_bp_lg_out, out_eec_dose_mamm_fp_sm_out, out_eec_dose_mamm_fp_md_out, out_eec_dose_mamm_fp_lg_out,
                  out_eec_dose_mamm_ar_sm_out, out_eec_dose_mamm_ar_md_out, out_eec_dose_mamm_ar_lg_out, out_eec_dose_mamm_se_sm_out,
                  out_eec_dose_mamm_se_md_out, out_eec_dose_mamm_se_lg_out):
    data = {
        "Animal Size": ['Small', 'Small', 'Small', 'Small', 'Medium', 'Medium', 'Medium', 'Medium', 'Large', 'Large',
                        'Large', 'Large', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],
        "Short Grass": ['{0:.2e}'.format(np.mean(out_eec_dose_mamm_sg_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_sg_sm_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_mamm_sg_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_sg_sm_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_mamm_sg_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_sg_md_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_mamm_sg_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_sg_md_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_mamm_sg_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_sg_lg_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_mamm_sg_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_sg_lg_out)), ],

        "Tall Grass": ['{0:.2e}'.format(np.mean(out_eec_dose_mamm_tg_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_tg_sm_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_mamm_tg_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_tg_sm_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_mamm_tg_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_tg_md_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_mamm_tg_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_tg_md_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_mamm_tg_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_tg_lg_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_mamm_tg_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_tg_lg_out)), ],

        "Broadleaf Plants": ['{0:.2e}'.format(np.mean(out_eec_dose_mamm_bp_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_bp_sm_out)),
                             '{0:.2e}'.format(np.min(out_eec_dose_mamm_bp_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_bp_sm_out)),
                             '{0:.2e}'.format(np.mean(out_eec_dose_mamm_bp_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_bp_md_out)),
                             '{0:.2e}'.format(np.min(out_eec_dose_mamm_bp_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_bp_md_out)),
                             '{0:.2e}'.format(np.mean(out_eec_dose_mamm_bp_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_bp_lg_out)),
                             '{0:.2e}'.format(np.min(out_eec_dose_mamm_bp_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_bp_lg_out)), ],

        "Fruits/Pods": ['{0:.2e}'.format(np.mean(out_eec_dose_mamm_fp_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_fp_sm_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_mamm_fp_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_fp_sm_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_mamm_fp_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_fp_md_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_mamm_fp_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_fp_md_out)),
                        '{0:.2e}'.format(np.mean(out_eec_dose_mamm_fp_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_fp_lg_out)),
                        '{0:.2e}'.format(np.min(out_eec_dose_mamm_fp_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_fp_lg_out)), ],

        "Arthropods": ['{0:.2e}'.format(np.mean(out_eec_dose_mamm_ar_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_ar_sm_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_mamm_ar_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_ar_sm_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_mamm_ar_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_ar_md_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_mamm_ar_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_ar_md_out)),
                       '{0:.2e}'.format(np.mean(out_eec_dose_mamm_ar_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_ar_lg_out)),
                       '{0:.2e}'.format(np.min(out_eec_dose_mamm_ar_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_ar_lg_out)), ],

        "Seeds": ['{0:.2e}'.format(np.mean(out_eec_dose_mamm_se_sm_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_se_sm_out)),
                  '{0:.2e}'.format(np.min(out_eec_dose_mamm_se_sm_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_se_sm_out)),
                  '{0:.2e}'.format(np.mean(out_eec_dose_mamm_se_md_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_se_md_out)),
                  '{0:.2e}'.format(np.min(out_eec_dose_mamm_se_md_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_se_md_out)),
                  '{0:.2e}'.format(np.mean(out_eec_dose_mamm_se_lg_out)), '{0:.2e}'.format(np.std(out_eec_dose_mamm_se_lg_out)),
                  '{0:.2e}'.format(np.min(out_eec_dose_mamm_se_lg_out)), '{0:.2e}'.format(np.max(out_eec_dose_mamm_se_lg_out)), ],
    }
    return data


def gettsumdata_10(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md, out_crq_dose_mamm_sg_md,
                   out_arq_dose_mamm_sg_lg, out_crq_dose_mamm_sg_lg, out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm,
                   out_arq_dose_mamm_tg_md, out_crq_dose_mamm_tg_md, out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg,
                   out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md, out_crq_dose_mamm_bp_md,
                   out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg, out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm,
                   out_arq_dose_mamm_fp_md, out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg,
                   out_arq_dose_mamm_ar_sm, out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md, out_crq_dose_mamm_ar_md,
                   out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg, out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm,
                   out_arq_dose_mamm_se_md, out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg, out_crq_dose_mamm_se_lg):
    data = {
        "Animal Size": ['Small', 'Small', 'Small', 'Small', 'Small', 'Small', 'Small', 'Small', 'Medium', 'Medium',
                        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Large', 'Large', 'Large', 'Large',
                        'Large', 'Large', 'Large', 'Large', ],
        "Type": ['Acute', 'Acute', 'Acute', 'Acute', 'Chronic', 'Chronic', 'Chronic', 'Chronic', 'Acute', 'Acute',
                 'Acute', 'Acute', 'Chronic', 'Chronic', 'Chronic', 'Chronic', 'Acute', 'Acute', 'Acute', 'Acute',
                 'Chronic', 'Chronic', 'Chronic', 'Chronic', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std',
                   'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],

        "Short Grass": ['{0:.2e}'.format(np.mean(out_arq_dose_mamm_sg_sm)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_sg_sm)),
                        '{0:.2e}'.format(np.min(out_arq_dose_mamm_sg_sm)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_sg_sm)),
                        '{0:.2e}'.format(np.mean(out_crq_dose_mamm_sg_sm)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_sg_sm)),
                        '{0:.2e}'.format(np.min(out_crq_dose_mamm_sg_sm)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_sg_sm)),
                        '{0:.2e}'.format(np.mean(out_arq_dose_mamm_sg_md)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_sg_md)),
                        '{0:.2e}'.format(np.min(out_arq_dose_mamm_sg_md)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_sg_md)),
                        '{0:.2e}'.format(np.mean(out_crq_dose_mamm_sg_md)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_sg_md)),
                        '{0:.2e}'.format(np.min(out_crq_dose_mamm_sg_md)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_sg_md)),
                        '{0:.2e}'.format(np.mean(out_arq_dose_mamm_sg_lg)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_sg_lg)),
                        '{0:.2e}'.format(np.min(out_arq_dose_mamm_sg_lg)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_sg_lg)),
                        '{0:.2e}'.format(np.mean(out_crq_dose_mamm_sg_lg)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_sg_lg)),
                        '{0:.2e}'.format(np.min(out_crq_dose_mamm_sg_lg)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_sg_lg)), ],

        "Tall Grass": ['{0:.2e}'.format(np.mean(out_arq_dose_mamm_tg_sm)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_tg_sm)),
                       '{0:.2e}'.format(np.min(out_arq_dose_mamm_tg_sm)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_tg_sm)),
                       '{0:.2e}'.format(np.mean(out_crq_dose_mamm_tg_sm)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_tg_sm)),
                       '{0:.2e}'.format(np.min(out_crq_dose_mamm_tg_sm)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_tg_sm)),
                       '{0:.2e}'.format(np.mean(out_arq_dose_mamm_tg_md)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_tg_md)),
                       '{0:.2e}'.format(np.min(out_arq_dose_mamm_tg_md)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_tg_md)),
                       '{0:.2e}'.format(np.mean(out_crq_dose_mamm_tg_md)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_tg_md)),
                       '{0:.2e}'.format(np.min(out_crq_dose_mamm_tg_md)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_tg_md)),
                       '{0:.2e}'.format(np.mean(out_arq_dose_mamm_tg_lg)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_tg_lg)),
                       '{0:.2e}'.format(np.min(out_arq_dose_mamm_tg_lg)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_tg_lg)),
                       '{0:.2e}'.format(np.mean(out_crq_dose_mamm_tg_lg)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_tg_lg)),
                       '{0:.2e}'.format(np.min(out_crq_dose_mamm_tg_lg)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_tg_lg)), ],

        "Broadleaf Plants": ['{0:.2e}'.format(np.mean(out_arq_dose_mamm_bp_sm)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_bp_sm)),
                             '{0:.2e}'.format(np.min(out_arq_dose_mamm_bp_sm)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_bp_sm)),
                             '{0:.2e}'.format(np.mean(out_crq_dose_mamm_bp_sm)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_bp_sm)),
                             '{0:.2e}'.format(np.min(out_crq_dose_mamm_bp_sm)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_bp_sm)),
                             '{0:.2e}'.format(np.mean(out_arq_dose_mamm_bp_md)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_bp_md)),
                             '{0:.2e}'.format(np.min(out_arq_dose_mamm_bp_md)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_bp_md)),
                             '{0:.2e}'.format(np.mean(out_crq_dose_mamm_bp_md)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_bp_md)),
                             '{0:.2e}'.format(np.min(out_crq_dose_mamm_bp_md)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_bp_md)),
                             '{0:.2e}'.format(np.mean(out_arq_dose_mamm_bp_lg)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_bp_lg)),
                             '{0:.2e}'.format(np.min(out_arq_dose_mamm_bp_lg)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_bp_lg)),
                             '{0:.2e}'.format(np.mean(out_crq_dose_mamm_bp_lg)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_bp_lg)),
                             '{0:.2e}'.format(np.min(out_crq_dose_mamm_bp_lg)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_bp_lg)), ],

        "Fruits/Pods": ['{0:.2e}'.format(np.mean(out_arq_dose_mamm_fp_sm)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_fp_sm)),
                        '{0:.2e}'.format(np.min(out_arq_dose_mamm_fp_sm)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_fp_sm)),
                        '{0:.2e}'.format(np.mean(out_crq_dose_mamm_fp_sm)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_fp_sm)),
                        '{0:.2e}'.format(np.min(out_crq_dose_mamm_fp_sm)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_fp_sm)),
                        '{0:.2e}'.format(np.mean(out_arq_dose_mamm_fp_md)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_fp_md)),
                        '{0:.2e}'.format(np.min(out_arq_dose_mamm_fp_md)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_fp_md)),
                        '{0:.2e}'.format(np.mean(out_crq_dose_mamm_fp_md)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_fp_md)),
                        '{0:.2e}'.format(np.min(out_crq_dose_mamm_fp_md)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_fp_md)),
                        '{0:.2e}'.format(np.mean(out_arq_dose_mamm_fp_lg)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_fp_lg)),
                        '{0:.2e}'.format(np.min(out_arq_dose_mamm_fp_lg)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_fp_lg)),
                        '{0:.2e}'.format(np.mean(out_crq_dose_mamm_fp_lg)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_fp_lg)),
                        '{0:.2e}'.format(np.min(out_crq_dose_mamm_fp_lg)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_fp_lg)), ],

        "Arthropods": ['{0:.2e}'.format(np.mean(out_arq_dose_mamm_ar_sm)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_ar_sm)),
                       '{0:.2e}'.format(np.min(out_arq_dose_mamm_ar_sm)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_ar_sm)),
                       '{0:.2e}'.format(np.mean(out_crq_dose_mamm_ar_sm)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_ar_sm)),
                       '{0:.2e}'.format(np.min(out_crq_dose_mamm_ar_sm)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_ar_sm)),
                       '{0:.2e}'.format(np.mean(out_arq_dose_mamm_ar_md)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_ar_md)),
                       '{0:.2e}'.format(np.min(out_arq_dose_mamm_ar_md)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_ar_md)),
                       '{0:.2e}'.format(np.mean(out_crq_dose_mamm_ar_md)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_ar_md)),
                       '{0:.2e}'.format(np.min(out_crq_dose_mamm_ar_md)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_ar_md)),
                       '{0:.2e}'.format(np.mean(out_arq_dose_mamm_ar_lg)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_ar_lg)),
                       '{0:.2e}'.format(np.min(out_arq_dose_mamm_ar_lg)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_ar_lg)),
                       '{0:.2e}'.format(np.mean(out_crq_dose_mamm_ar_lg)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_ar_lg)),
                       '{0:.2e}'.format(np.min(out_crq_dose_mamm_ar_lg)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_ar_lg)), ],

        "Seeds": ['{0:.2e}'.format(np.mean(out_arq_dose_mamm_ar_sm)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_se_sm)),
                  '{0:.2e}'.format(np.min(out_arq_dose_mamm_se_sm)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_se_sm)),
                  '{0:.2e}'.format(np.mean(out_crq_dose_mamm_se_sm)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_se_sm)),
                  '{0:.2e}'.format(np.min(out_crq_dose_mamm_se_sm)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_se_sm)),
                  '{0:.2e}'.format(np.mean(out_arq_dose_mamm_se_md)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_se_md)),
                  '{0:.2e}'.format(np.min(out_arq_dose_mamm_se_md)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_se_md)),
                  '{0:.2e}'.format(np.mean(out_crq_dose_mamm_se_md)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_se_md)),
                  '{0:.2e}'.format(np.min(out_crq_dose_mamm_se_md)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_se_md)),
                  '{0:.2e}'.format(np.mean(out_arq_dose_mamm_se_lg)), '{0:.2e}'.format(np.std(out_arq_dose_mamm_se_lg)),
                  '{0:.2e}'.format(np.min(out_arq_dose_mamm_se_lg)), '{0:.2e}'.format(np.max(out_arq_dose_mamm_se_lg)),
                  '{0:.2e}'.format(np.mean(out_crq_dose_mamm_se_lg)), '{0:.2e}'.format(np.std(out_crq_dose_mamm_se_lg)),
                  '{0:.2e}'.format(np.min(out_crq_dose_mamm_se_lg)), '{0:.2e}'.format(np.max(out_crq_dose_mamm_se_lg)), ],
    }
    return data


def gettsumdata_11(out_arq_diet_mamm_sg, out_crq_diet_mamm_sg, out_arq_diet_mamm_tg, out_crq_diet_mamm_tg, out_arq_diet_mamm_bp,
                   out_crq_diet_mamm_bp, out_arq_diet_mamm_fp, out_crq_diet_mamm_fp, out_arq_diet_mamm_ar, out_crq_diet_mamm_ar):
    if 'N/A' in out_arq_diet_mamm_sg:
        out_arq_diet_mamm_sg_mean = 'N/A'
        out_arq_diet_mamm_sg_std = 'N/A'
        out_arq_diet_mamm_sg_min = 'N/A'
        out_arq_diet_mamm_sg_max = 'N/A'
        out_arq_diet_mamm_tg_mean = 'N/A'
        out_arq_diet_mamm_tg_std = 'N/A'
        out_arq_diet_mamm_tg_min = 'N/A'
        out_arq_diet_mamm_tg_max = 'N/A'
        out_arq_diet_mamm_bp_mean = 'N/A'
        out_arq_diet_mamm_bp_std = 'N/A'
        out_arq_diet_mamm_bp_min = 'N/A'
        out_arq_diet_mamm_bp_max = 'N/A'
        out_arq_diet_mamm_fp_mean = 'N/A'
        out_arq_diet_mamm_fp_std = 'N/A'
        out_arq_diet_mamm_fp_min = 'N/A'
        out_arq_diet_mamm_fp_max = 'N/A'
        out_arq_diet_mamm_ar_mean = 'N/A'
        out_arq_diet_mamm_amax_seed_ratetd = 'N/A'
        out_arq_diet_mamm_ar_min = 'N/A'
        out_arq_diet_mamm_ar_max = 'N/A'
    else:
        out_arq_diet_mamm_sg_mean = '{0:.2e}'.format(np.mean(out_arq_diet_mamm_sg))
        out_arq_diet_mamm_sg_std = '{0:.2e}'.format(np.std(out_arq_diet_mamm_sg))
        out_arq_diet_mamm_sg_min = '{0:.2e}'.format(np.min(out_arq_diet_mamm_sg))
        out_arq_diet_mamm_sg_max = '{0:.2e}'.format(np.max(out_arq_diet_mamm_sg))
        out_arq_diet_mamm_tg_mean = '{0:.2e}'.format(np.mean(out_arq_diet_mamm_tg))
        out_arq_diet_mamm_tg_std = '{0:.2e}'.format(np.std(out_arq_diet_mamm_tg))
        out_arq_diet_mamm_tg_min = '{0:.2e}'.format(np.min(out_arq_diet_mamm_tg))
        out_arq_diet_mamm_tg_max = '{0:.2e}'.format(np.max(out_arq_diet_mamm_tg))
        out_arq_diet_mamm_bp_mean = '{0:.2e}'.format(np.mean(out_arq_diet_mamm_bp))
        out_arq_diet_mamm_bp_std = '{0:.2e}'.format(np.std(out_arq_diet_mamm_bp))
        out_arq_diet_mamm_bp_min = '{0:.2e}'.format(np.min(out_arq_diet_mamm_bp))
        out_arq_diet_mamm_bp_max = '{0:.2e}'.format(np.max(out_arq_diet_mamm_bp))
        out_arq_diet_mamm_fp_mean = '{0:.2e}'.format(np.mean(out_arq_diet_mamm_fp))
        out_arq_diet_mamm_fp_std = '{0:.2e}'.format(np.std(out_arq_diet_mamm_fp))
        out_arq_diet_mamm_fp_min = '{0:.2e}'.format(np.min(out_arq_diet_mamm_fp))
        out_arq_diet_mamm_fp_max = '{0:.2e}'.format(np.max(out_arq_diet_mamm_fp))
        out_arq_diet_mamm_ar_mean = '{0:.2e}'.format(np.mean(out_arq_diet_mamm_ar))
        out_arq_diet_mamm_amax_seed_ratetd = '{0:.2e}'.format(np.std(out_arq_diet_mamm_ar))
        out_arq_diet_mamm_ar_min = '{0:.2e}'.format(np.min(out_arq_diet_mamm_ar))
        out_arq_diet_mamm_ar_max = '{0:.2e}'.format(np.max(out_arq_diet_mamm_ar))
    data = {
        "Type": ['Acute', 'Acute', 'Acute', 'Acute', 'Chronic', 'Chronic', 'Chronic', 'Chronic', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],
        "Short Grass": [out_arq_diet_mamm_sg_mean, out_arq_diet_mamm_sg_std, out_arq_diet_mamm_sg_min, out_arq_diet_mamm_sg_max,
                        '{0:.2e}'.format(np.mean(out_crq_diet_mamm_sg)), '{0:.2e}'.format(np.std(out_crq_diet_mamm_sg)),
                        '{0:.2e}'.format(np.min(out_crq_diet_mamm_sg)), '{0:.2e}'.format(np.max(out_crq_diet_mamm_sg)), ],

        "Tall Grass": [out_arq_diet_mamm_tg_mean, out_arq_diet_mamm_tg_std, out_arq_diet_mamm_tg_min, out_arq_diet_mamm_tg_max,
                       '{0:.2e}'.format(np.mean(out_crq_diet_mamm_tg)), '{0:.2e}'.format(np.std(out_crq_diet_mamm_tg)),
                       '{0:.2e}'.format(np.min(out_crq_diet_mamm_tg)), '{0:.2e}'.format(np.max(out_crq_diet_mamm_tg)), ],

        "Broadleaf Plants": [out_arq_diet_mamm_bp_mean, out_arq_diet_mamm_bp_std, out_arq_diet_mamm_bp_min, out_arq_diet_mamm_bp_max,
                             '{0:.2e}'.format(np.mean(out_crq_diet_mamm_bp)), '{0:.2e}'.format(np.std(out_crq_diet_mamm_bp)),
                             '{0:.2e}'.format(np.min(out_crq_diet_mamm_bp)), '{0:.2e}'.format(np.max(out_crq_diet_mamm_bp)), ],

        "Fruits/Pods/Seeds": [out_arq_diet_mamm_fp_mean, out_arq_diet_mamm_fp_std, out_arq_diet_mamm_fp_min, out_arq_diet_mamm_fp_max,
                              '{0:.2e}'.format(np.mean(out_crq_diet_mamm_fp)), '{0:.2e}'.format(np.std(out_crq_diet_mamm_fp)),
                              '{0:.2e}'.format(np.min(out_crq_diet_mamm_fp)), '{0:.2e}'.format(np.max(out_crq_diet_mamm_fp)), ],

        "Arthropods": [out_arq_diet_mamm_ar_mean, out_arq_diet_mamm_amax_seed_ratetd, out_arq_diet_mamm_ar_min, out_arq_diet_mamm_ar_max,
                       '{0:.2e}'.format(np.mean(out_crq_diet_mamm_ar)), '{0:.2e}'.format(np.std(out_crq_diet_mamm_ar)),
                       '{0:.2e}'.format(np.min(out_crq_diet_mamm_ar)), '{0:.2e}'.format(np.max(out_crq_diet_mamm_ar)), ],
    }
    return data


def gettsumdata_12(out_ld50_rg_bird_sm_out, out_ld50_rg_mamm_sm_out, out_ld50_rg_bird_md_out, out_ld50_rg_mamm_md_out,
                   out_ld50_rg_bird_lg_out, out_ld50_rg_mamm_lg_out):
    data = {
        "Animal Size": ['Small', 'Small', 'Small', 'Small', 'Medium', 'Medium', 'Medium', 'Medium', 'Large', 'Large',
                        'Large', 'Large', ],
        "Metric": ['Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', 'Mean', 'Std', 'Min', 'Max', ],
        "Avian": ['{0:.2e}'.format(np.mean(out_ld50_rg_bird_sm_out)), '{0:.2e}'.format(np.std(out_ld50_rg_bird_sm_out)),
                  '{0:.2e}'.format(np.min(out_ld50_rg_bird_sm_out)), '{0:.2e}'.format(np.max(out_ld50_rg_bird_sm_out)),
                  '{0:.2e}'.format(np.mean(out_ld50_rg_bird_md_out)), '{0:.2e}'.format(np.std(out_ld50_rg_bird_md_out)),
                  '{0:.2e}'.format(np.min(out_ld50_rg_bird_md_out)), '{0:.2e}'.format(np.max(out_ld50_rg_bird_md_out)),
                  '{0:.2e}'.format(np.mean(out_ld50_rg_bird_lg_out)), '{0:.2e}'.format(np.std(out_ld50_rg_bird_lg_out)),
                  '{0:.2e}'.format(np.min(out_ld50_rg_bird_lg_out)), '{0:.2e}'.format(np.max(out_ld50_rg_bird_lg_out)), ],
        "Mammal": ['{0:.2e}'.format(np.mean(out_ld50_rg_mamm_sm_out)), '{0:.2e}'.format(np.std(out_ld50_rg_mamm_sm_out)),
                   '{0:.2e}'.format(np.min(out_ld50_rg_mamm_sm_out)), '{0:.2e}'.format(np.max(out_ld50_rg_mamm_sm_out)),
                   '{0:.2e}'.format(np.mean(out_ld50_rg_mamm_md_out)), '{0:.2e}'.format(np.std(out_ld50_rg_mamm_md_out)),
                   '{0:.2e}'.format(np.min(out_ld50_rg_mamm_md_out)), '{0:.2e}'.format(np.max(out_ld50_rg_mamm_md_out)),
                   '{0:.2e}'.format(np.mean(out_ld50_rg_mamm_lg_out)), '{0:.2e}'.format(np.std(out_ld50_rg_mamm_lg_out)),
                   '{0:.2e}'.format(np.min(out_ld50_rg_mamm_lg_out)), '{0:.2e}'.format(np.max(out_ld50_rg_mamm_lg_out)), ],
    }
    return data


def table_all(trex_obj):
    table1_out = table_1(trex_obj)
    table2_out = table_2(trex_obj)
    table3_out = table_3(trex_obj)
    table4_out = table_4(trex_obj)

    html = table1_out
    html = html + table2_out
    html = html + table3_out
    html = html + table4_out

    if trex_obj.application_type == 'Seed Treatment':
        table5_out = table_5(trex_obj)

        html = html + table5_out['html']
        return html, table5_out
    else:
        a_r_p = 0
        table6_out = table_6(trex_obj)
        table7_out = table_7(trex_obj)
        table7_add_out = table_7_add(trex_obj)
        table8_out = table_8(trex_obj)
        table9_out = table_9(trex_obj)
        table10_out = table_10(trex_obj)
        table11_out = table_11(trex_obj)

        html = html + table6_out['html']
        html = html + table7_out['html']
        html = html + table7_add_out['html']
        html = html + table8_out['html']
        html = html + table9_out['html']
        html = html + table10_out['html']
        html = html + table11_out['html']

        if trex_obj.application_type == 'Row/Band/In-furrow-Granular':
            table12_out = table_12(trex_obj)
            html = html + table12_out['html']
            return html, table6_out, table7_out, table7_add_out, table8_out, table9_out, table10_out, table11_out, table12_out

        elif trex_obj.application_type == 'Row/Band/In-furrow-Liquid':
            table13_out = table_13(trex_obj)
            html = html + table13_out['html']
            return html, table6_out, table7_out, table7_add_out, table8_out, table9_out, table10_out, table11_out, table13_out

        elif trex_obj.application_type == 'Broadcast-Granular':
            table14_out = table_14(trex_obj)
            html = html + table14_out['html']
            return html, table6_out, table7_out, table7_add_out, table8_out, table9_out, table10_out, table11_out, table14_out

        elif trex_obj.application_type == 'Broadcast-Liquid':
            table15_out = table_15(trex_obj)
            html = html + table15_out['html']
            return html, table6_out, table7_out, table7_add_out, table8_out, table9_out, table10_out, table11_out, table15_out


def timestamp(trex_obj="", batch_jid=""):
    if trex_obj:
        st = datetime.datetime.strptime(trex_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html = """
    <div class="out_">
        <b>T-Rex <a href="http://www.epa.gov/oppefed1/models/terrestrial/trex/t_rex_user_guide.htm">Version 1.5.2</a> (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def table_all_qaqc(trex_obj):
    table1_out = table_1(trex_obj)
    table2_out = table_2(trex_obj)
    table3_out = table_3(trex_obj)
    table4_out = table_4(trex_obj)
    a_r_p = 0

    if trex_obj.application_type != 'Seed Treatment':
        table6_out_qaqc = table_6_qaqc(trex_obj)
        table7_out_qaqc = table_7_qaqc(trex_obj)
        table_7_add_out_qaqc = table_7_add_qaqc(trex_obj)
        table8_out_qaqc = table_8_qaqc(trex_obj)
        table9_out_qaqc = table_9_qaqc(trex_obj)
        table10_out_qaqc = table_10_qaqc(trex_obj)
        table11_out_qaqc = table_11_qaqc(trex_obj)
        table15_out_qaqc = table_15_qaqc(trex_obj)

        html_all = table1_out + table2_out + table3_out + table4_out + table6_out_qaqc + \
                   table7_out_qaqc + table_7_add_out_qaqc + table8_out_qaqc + table9_out_qaqc + \
                   table10_out_qaqc + table11_out_qaqc + table15_out_qaqc
    else:
        table5_out_qaqc = table_5_qaqc(trex_obj)
        html_all = table1_out + table2_out + table3_out + table4_out + table5_out_qaqc

    return html_all


def table_sum_1(i, a_i, max_seed_rate, b_w, percent_incorp, den, Foliar_dissipation_half_life, num_apps, app_rates):
    # pre-table sum_input_1
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Batch Summary Statistics (Iterations={0!s})</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Chemical Properties</H4>
                <div class="out_ container_output">
        """.format((i - 1))

    rate_out_t = []
    for jj in app_rates.split(','):
        rate_out_t.append(np.mean(jj))

    # table sum_input_1
    tsuminputdata_1 = gettsumdata_1(a_i, max_seed_rate, b_w, percent_incorp, den, Foliar_dissipation_half_life, num_apps, rate_out_t)
    tsuminputrows_1 = gethtmlrowsfromcols(tsuminputdata_1, sumheadings)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_1, headings=sumheadings)))
    html = html + """
        </div>
        """
    return html


def table_sum_2(avian_ld50, avian_lc50, avian_NOAEC, avian_NOAEL, bw_assessed_bird_s, bw_assessed_bird_m,
                bw_assessed_bird_l, tw_bird_ld50, tw_bird_lc50, tw_bird_noaec, tw_bird_noael, mineau_scaling_factor):
    # pre-table sum_input_2
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Toxicity Properties (Avian)</H4>
                <div class="out_ container_output">
        """
    # table sum_input_2
    tsuminputdata_2 = gettsumdata_2(avian_ld50, avian_lc50, avian_NOAEC, avian_NOAEL, bw_assessed_bird_s,
                                    bw_assessed_bird_m, bw_assessed_bird_l, tw_bird_ld50, tw_bird_lc50, tw_bird_noaec,
                                    tw_bird_noael, mineau_scaling_factor)
    tsuminputrows_2 = gethtmlrowsfromcols(tsuminputdata_2, sumheadings)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_2, headings=sumheadings)))
    html = html + """
        </div>
        """
    return html


def table_sum_3(mammalian_ld50, mammalian_lc50, mammalian_NOAEC, mammalian_NOAEL, bw_assessed_mamm_s,
                bw_assessed_mamm_m, bw_assessed_mamm_l, bw_tested_mamm):
    # pre-table sum_input_3
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Toxicity Properties (Mammal)</H4>
                <div class="out_ container_output">
        """
    # table sum_input_3
    tsuminputdata_3 = gettsumdata_3(mammalian_ld50, mammalian_lc50, mammalian_NOAEC, mammalian_NOAEL,
                                    bw_assessed_mamm_s, bw_assessed_mamm_m,
                                    bw_assessed_mamm_l, bw_tested_mamm)
    tsuminputrows_3 = gethtmlrowsfromcols(tsuminputdata_3, sumheadings)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_3, headings=sumheadings)))
    html = html + """
                </div>
        </div>
        <br>
        """
    return html


def table_sum_5(application_type_ST, out_sa_bird_1_s_out, out_sa_bird_2_s_out, out_sc_bird_s_out, out_sa_mamm_1_s_out, out_sa_mamm_2_s_out,
                out_sc_mamm_s_out, out_sa_bird_1_m_out, out_sa_bird_2_m_out, out_sc_bird_m_out, out_sa_mamm_1_m_out, out_sa_mamm_2_m_out,
                out_sc_mamm_m_out, out_sa_bird_1_l_out, out_sa_bird_2_l_out, out_sc_bird_l_out, out_sa_mamm_1_l_out, out_sa_mamm_2_l_out,
                out_sc_mamm_l_out):
    # pre-table sum_5
    html = """
        <H3 class="out_3 collapsible" id="section4"><span></span>Batch Outputs: Application Type : Seed Treatment (N={0!s})</H3>
                <div class="out_ container_output">
        """.format((application_type_ST))

    # table sum_output_5
    tsuminputdata_5 = gettsumdata_5(out_sa_bird_1_s_out, out_sa_bird_2_s_out, out_sc_bird_s_out, out_sa_mamm_1_s_out, out_sa_mamm_2_s_out,
                                    out_sc_mamm_s_out, out_sa_bird_1_m_out, out_sa_bird_2_m_out, out_sc_bird_m_out, out_sa_mamm_1_m_out,
                                    out_sa_mamm_2_m_out, out_sc_mamm_m_out, out_sa_bird_1_l_out, out_sa_bird_2_l_out, out_sc_bird_l_out,
                                    out_sa_mamm_1_l_out, out_sa_mamm_2_l_out, out_sc_mamm_l_out)
    tsuminputrows_5 = gethtmlrowsfromcols(tsuminputdata_5, sumheadings_5[1])
    html = html + tmpl.render(
        Context(dict(data=tsuminputrows_5, headings=sumheadings_5[0], sub_headings=sumheadings_5[2], th_span='5')))
    html = html + """
                </div>
        """
    return html


def table_sum_6(application_type, application_type_str, out_eec_diet_sg_RBG_out, out_eec_diet_tg_RBG_out, out_eec_diet_bp_RBG_out,
                out_eec_diet_fr_RBG_out, out_eec_diet_ar_RBG_out):
    # pre-table sum_6
    html = """
        <br>
        <H3 class="out_3 collapsible" id="section4"><span></span>Batch Outputs: Application Type : {0!s} (N={1!s})</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section3"><span></span>Dietary based EECs (ppm)</H4>
                <div class="out_ container_output">
        """.format(application_type_str, application_type)

    # table sum_output_6
    tsuminputdata_6 = gettsumdata_6(out_eec_diet_sg_RBG_out, out_eec_diet_tg_RBG_out, out_eec_diet_bp_RBG_out, out_eec_diet_fr_RBG_out,
                                    out_eec_diet_ar_RBG_out)
    tsuminputrows_6 = gethtmlrowsfromcols(tsuminputdata_6, sumheadings_6[1])
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_6, headings=sumheadings_6[0], sub_headings=sumheadings_6[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_7(out_eec_dose_bird_sg_sm_out, out_eec_dose_bird_sg_md_out, out_eec_dose_bird_sg_lg_out, out_eec_dose_bird_tg_sm_out,
                out_eec_dose_bird_tg_md_out, out_eec_dose_bird_tg_lg_out, out_eec_dose_bird_bp_sm_out, out_eec_dose_bird_bp_md_out,
                out_eec_dose_bird_bp_lg_out, out_eec_dose_bird_fp_sm_out, out_eec_dose_bird_fp_md_out, out_eec_dose_bird_fp_lg_out,
                out_eec_dose_bird_ar_sm_out, out_eec_dose_bird_ar_md_out, out_eec_dose_bird_ar_lg_out, out_eec_dose_bird_se_sm_out,
                out_eec_dose_bird_se_md_out, out_eec_dose_bird_se_lg_out):
    # pre-table sum_7
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Avian Dosed Based EECs</H4>
                <div class="out_ container_output">
        """

    # table sum_output_7
    tsuminputdata_7 = gettsumdata_7(out_eec_dose_bird_sg_sm_out, out_eec_dose_bird_sg_md_out, out_eec_dose_bird_sg_lg_out,
                                    out_eec_dose_bird_tg_sm_out, out_eec_dose_bird_tg_md_out, out_eec_dose_bird_tg_lg_out,
                                    out_eec_dose_bird_bp_sm_out, out_eec_dose_bird_bp_md_out, out_eec_dose_bird_bp_lg_out,
                                    out_eec_dose_bird_fp_sm_out, out_eec_dose_bird_fp_md_out, out_eec_dose_bird_fp_lg_out,
                                    out_eec_dose_bird_ar_sm_out, out_eec_dose_bird_ar_md_out, out_eec_dose_bird_ar_lg_out,
                                    out_eec_dose_bird_se_sm_out, out_eec_dose_bird_se_md_out, out_eec_dose_bird_se_lg_out)
    tsuminputrows_7 = gethtmlrowsfromcols(tsuminputdata_7, sumheadings_7[1])
    # html = html + tmpl_sum.render(Context(dict(data_new=tsuminputrows_7, headings=sumheadings_7[0], sub_headings=sumheadings_7[2], data_cols=["Small", "Medium", "Large"])))
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_7, headings=sumheadings_7[0], sub_headings=sumheadings_7[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_7_add(out_arq_bird_sg_RBG_sm_out, out_arq_bird_sg_RBG_md_out, out_arq_bird_sg_RBG_lg_out, out_arq_bird_tg_RBG_sm_out,
                    out_arq_bird_tg_RBG_md_out, out_arq_bird_tg_RBG_lg_out, out_arq_bird_bp_RBG_sm_out, out_arq_bird_bp_RBG_md_out,
                    out_arq_bird_bp_RBG_lg_out, out_arq_bird_fp_RBG_sm_out, out_arq_bird_fp_RBG_md_out, out_arq_bird_fp_RBG_lg_out,
                    out_arq_bird_ar_RBG_sm_out, out_arq_bird_ar_RBG_md_out, out_arq_bird_ar_RBG_lg_out, out_arq_bird_se_RBG_sm_out,
                    out_arq_bird_se_RBG_md_out, out_arq_bird_se_RBG_lg_out):
    # pre-table sum_7_add
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Avian Dosed Based RQs</H4>
                <div class="out_ container_output">
        """

    # table sum_output_7
    tsuminputdata_7_add = gettsumdata_7(out_arq_bird_sg_RBG_sm_out, out_arq_bird_sg_RBG_md_out, out_arq_bird_sg_RBG_lg_out,
                                        out_arq_bird_tg_RBG_sm_out, out_arq_bird_tg_RBG_md_out, out_arq_bird_tg_RBG_lg_out,
                                        out_arq_bird_bp_RBG_sm_out, out_arq_bird_bp_RBG_md_out, out_arq_bird_bp_RBG_lg_out,
                                        out_arq_bird_fp_RBG_sm_out, out_arq_bird_fp_RBG_md_out, out_arq_bird_fp_RBG_lg_out,
                                        out_arq_bird_ar_RBG_sm_out, out_arq_bird_ar_RBG_md_out, out_arq_bird_ar_RBG_lg_out,
                                        out_arq_bird_se_RBG_sm_out, out_arq_bird_se_RBG_md_out, out_arq_bird_se_RBG_lg_out)
    tsuminputrows_7_add = gethtmlrowsfromcols(tsuminputdata_7_add, sumheadings_7[1])
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_7_add, headings=sumheadings_7[0], sub_headings=sumheadings_7[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_8(out_arq_diet_bird_sg_a_out, out_arq_diet_bird_sg_c_out, out_arq_diet_bird_tg_a_out, out_arq_diet_bird_tg_c_out,
                out_arq_diet_bird_bp_a_out, out_arq_diet_bird_bp_c_out, out_arq_diet_bird_fp_a_out, out_arq_diet_bird_fp_c_out,
                out_arq_diet_bird_ar_a_out, out_arq_diet_bird_ar_c_out):
    # pre-table sum_8
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Avian Diet Based RQs</H4>
                <div class="out_ container_output">
        """

    # table sum_output_8
    tsuminputdata_8 = gettsumdata_8(out_arq_diet_bird_sg_a_out, out_arq_diet_bird_sg_c_out, out_arq_diet_bird_tg_a_out,
                                    out_arq_diet_bird_tg_c_out, out_arq_diet_bird_bp_a_out, out_arq_diet_bird_bp_c_out,
                                    out_arq_diet_bird_fp_a_out, out_arq_diet_bird_fp_c_out, out_arq_diet_bird_ar_a_out,
                                    out_arq_diet_bird_ar_c_out)
    tsuminputrows_8 = gethtmlrowsfromcols(tsuminputdata_8, sumheadings_8[1])
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_8, headings=sumheadings_8[0], sub_headings=sumheadings_8[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_9(out_eec_dose_mamm_sg_sm_out, out_eec_dose_mamm_sg_md_out, out_eec_dose_mamm_sg_lg_out, out_eec_dose_mamm_tg_sm_out,
                out_eec_dose_mamm_tg_md_out, out_eec_dose_mamm_tg_lg_out, out_eec_dose_mamm_bp_sm_out, out_eec_dose_mamm_bp_md_out,
                out_eec_dose_mamm_bp_lg_out, out_eec_dose_mamm_fp_sm_out, out_eec_dose_mamm_fp_md_out, out_eec_dose_mamm_fp_lg_out,
                out_eec_dose_mamm_ar_sm_out, out_eec_dose_mamm_ar_md_out, out_eec_dose_mamm_ar_lg_out, out_eec_dose_mamm_se_sm_out,
                out_eec_dose_mamm_se_md_out, out_eec_dose_mamm_se_lg_out):
    # pre-table sum_9
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Mammalian Dose Based EECs (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """

    # table sum_output_9
    tsuminputdata_9 = gettsumdata_9(out_eec_dose_mamm_sg_sm_out, out_eec_dose_mamm_sg_md_out, out_eec_dose_mamm_sg_lg_out,
                                    out_eec_dose_mamm_tg_sm_out, out_eec_dose_mamm_tg_md_out, out_eec_dose_mamm_tg_lg_out,
                                    out_eec_dose_mamm_bp_sm_out, out_eec_dose_mamm_bp_md_out, out_eec_dose_mamm_bp_lg_out,
                                    out_eec_dose_mamm_fp_sm_out, out_eec_dose_mamm_fp_md_out, out_eec_dose_mamm_fp_lg_out,
                                    out_eec_dose_mamm_ar_sm_out, out_eec_dose_mamm_ar_md_out, out_eec_dose_mamm_ar_lg_out,
                                    out_eec_dose_mamm_se_sm_out, out_eec_dose_mamm_se_md_out, out_eec_dose_mamm_se_lg_out)
    tsuminputrows_9 = gethtmlrowsfromcols(tsuminputdata_9, sumheadings_9[1])
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_9, headings=sumheadings_9[0], sub_headings=sumheadings_9[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_10(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md, out_crq_dose_mamm_sg_md,
                 out_arq_dose_mamm_sg_lg, out_crq_dose_mamm_sg_lg, out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm,
                 out_arq_dose_mamm_tg_md, out_crq_dose_mamm_tg_md, out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg,
                 out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md, out_crq_dose_mamm_bp_md,
                 out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg, out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm,
                 out_arq_dose_mamm_fp_md, out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg,
                 out_arq_dose_mamm_ar_sm, out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md, out_crq_dose_mamm_ar_md,
                 out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg, out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm,
                 out_arq_dose_mamm_se_md, out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg, out_crq_dose_mamm_se_lg):
    # pre-table sum_10
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Mammalian Dose Based RQs</H4>
                <div class="out_ container_output">
        """

    # table sum_output_10
    tsuminputdata_10 = gettsumdata_10(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md,
                                      out_crq_dose_mamm_sg_md, out_arq_dose_mamm_sg_lg, out_crq_dose_mamm_sg_lg,
                                      out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm, out_arq_dose_mamm_tg_md,
                                      out_crq_dose_mamm_tg_md, out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg,
                                      out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md,
                                      out_crq_dose_mamm_bp_md, out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg,
                                      out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm, out_arq_dose_mamm_fp_md,
                                      out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg,
                                      out_arq_dose_mamm_ar_sm, out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md,
                                      out_crq_dose_mamm_ar_md, out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg,
                                      out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm, out_arq_dose_mamm_se_md,
                                      out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg, out_crq_dose_mamm_se_lg)
    tsuminputrows_10 = gethtmlrowsfromcols(tsuminputdata_10, sumheadings_10[1])
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_10, headings=sumheadings_10[0], sub_headings=sumheadings_10[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_11(out_arq_diet_mamm_sg, out_crq_diet_mamm_sg, out_arq_diet_mamm_tg, out_crq_diet_mamm_tg, out_arq_diet_mamm_bp,
                 out_crq_diet_mamm_bp, out_arq_diet_mamm_fp, out_crq_diet_mamm_fp, out_arq_diet_mamm_ar, out_crq_diet_mamm_ar):
    # pre-table sum_11
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>Mammalian Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    # table sum_output_11
    tsuminputdata_11 = gettsumdata_11(out_arq_diet_mamm_sg, out_crq_diet_mamm_sg, out_arq_diet_mamm_tg, out_crq_diet_mamm_tg,
                                      out_arq_diet_mamm_bp, out_crq_diet_mamm_bp, out_arq_diet_mamm_fp, out_crq_diet_mamm_fp,
                                      out_arq_diet_mamm_ar, out_crq_diet_mamm_ar)
    tsuminputrows_11 = gethtmlrowsfromcols(tsuminputdata_11, sumheadings_11[1])
    html = html + tmpl_sum.render(
        Context(dict(data=tsuminputrows_11, headings=sumheadings_11[0], sub_headings=sumheadings_11[2])))
    html = html + """
                </div>
        """
    return html


def table_sum_12(out_ld50_rg_bird_sm_out, out_ld50_rg_mamm_sm_out, out_ld50_rg_bird_md_out, out_ld50_rg_mamm_md_out,
                 out_ld50_rg_bird_lg_out, out_ld50_rg_mamm_lg_out):
    # pre-table sum_12
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>LD50ft-2(mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    # table sum_output_12
    tsuminputdata_12 = gettsumdata_12(out_ld50_rg_bird_sm_out, out_ld50_rg_mamm_sm_out, out_ld50_rg_bird_md_out,
                                      out_ld50_rg_mamm_md_out, out_ld50_rg_bird_lg_out, out_ld50_rg_mamm_lg_out)
    tsuminputrows_12 = gethtmlrowsfromcols(tsuminputdata_12, sumheadings_12)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_12, headings=sumheadings_12)))
    return html


def table_sum_13(out_ld50_rl_bird_sm_out, out_ld50_rl_mamm_sm_out, out_ld50_rl_bird_md_out, out_ld50_rl_mamm_md_out,
                 out_ld50_rl_bird_lg_out, out_ld50_rl_mamm_lg_out):
    # pre-table sum_13
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>LD50ft-2(mg/kg-bw)</H4>
                <div class="out_ container_output">
        """

    # table sum_output_13
    tsuminputdata_13 = gettsumdata_12(out_ld50_rl_bird_sm_out, out_ld50_rl_mamm_sm_out, out_ld50_rl_bird_md_out,
                                      out_ld50_rl_mamm_md_out, out_ld50_rl_bird_lg_out, out_ld50_rl_mamm_lg_out)
    tsuminputrows_13 = gethtmlrowsfromcols(tsuminputdata_13, sumheadings_12)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_13, headings=sumheadings_12)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_sum_14(out_ld50_bg_bird_sm_out, out_ld50_bg_mamm_sm_out, out_ld50_bg_bird_md_out, out_ld50_bg_mamm_md_out,
                 out_ld50_bg_bird_lg_out, out_ld50_bg_mamm_lg_out):
    # pre-table sum_14
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>LD50ft-2(mg/kg-bw)</H4>
                <div class="out_ container_output">
        """

    # table sum_output_14
    tsuminputdata_14 = gettsumdata_12(out_ld50_bg_bird_sm_out, out_ld50_bg_mamm_sm_out, out_ld50_bg_bird_md_out,
                                      out_ld50_bg_mamm_md_out, out_ld50_bg_bird_lg_out, out_ld50_bg_mamm_lg_out)
    tsuminputrows_14 = gethtmlrowsfromcols(tsuminputdata_14, sumheadings_12)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_14, headings=sumheadings_12)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_sum_15(out_ld50_bl_bird_sm_out, out_ld50_bl_mamm_sm_out, out_ld50_bl_bird_md_out, out_ld50_bl_mamm_md_out,
                 out_ld50_bl_bird_lg_out, out_ld50_bl_mamm_lg_out):
    # pre-table sum_15
    html = """
            <H4 class="out_1 collapsible" id="section3"><span></span>LD50ft-2(mg/kg-bw)</H4>
                <div class="out_ container_output">
        """

    # table sum_output_15
    tsuminputdata_15 = gettsumdata_12(out_ld50_bl_bird_sm_out, out_ld50_bl_mamm_sm_out, out_ld50_bl_bird_md_out,
                                      out_ld50_bl_mamm_md_out, out_ld50_bl_bird_lg_out, out_ld50_bl_mamm_lg_out)
    tsuminputrows_15 = gethtmlrowsfromcols(tsuminputdata_15, sumheadings_12)
    html = html + tmpl.render(Context(dict(data=tsuminputrows_15, headings=sumheadings_12)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_1(trex_obj):
    # pre-table 1
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs:</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Chemical Properties</H4>
                <div class="out_ container_output">
        """
    # table 1
    if trex_obj.application_type == "Broadcast-Liquid" or trex_obj.application_type == "Broadcast-Granular":
        t1data = gett1data_broad(trex_obj)
    elif trex_obj.application_type == "Row/Band/In-furrow-Granular" or trex_obj.application_type == "Row/Band/In-furrow-Liquid":
        t1data = gett1data_band(trex_obj)
    else:
        t1data = gett1data_seed(trex_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
                </div>
        """
    return html


def table_2(trex_obj):
    # #pre-table 2
    html = """
            <H4 class="out_2 collapsible" id="section3"><span></span>Chemical Application (n={0!s})</H4>
                <div class="out_ container_output">
        """.format((trex_obj.num_apps))
    # table 2
    t2data_all = []
    for i in range(int(trex_obj.num_apps)):
        app_rates_list = trex_obj.app_rates.split(',')
        day_out_list = trex_obj.day_out.split(',')
        rate_temp = app_rates_list[i]
        day_temp = day_out_list[i]
        t2data_temp = gett2data(i + 1, rate_temp, day_temp)
        t2data_all.append(t2data_temp)
    t2data = dict([(k, [t2data_ind[k][0] for t2data_ind in t2data_all]) for k in t2data_temp])
    t2rows = gethtmlrowsfromcols(t2data, pvaheadings[0])
    if trex_obj.application_type == "Seed Treatment":
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvaheadings[1])))
    else:
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvaheadings[2])))
    html = html + """
                </div>
        """
    return html


def table_3(trex_obj):
    # pre-table 3
    html = """
            <H4 class="out_3 collapsible" id="section4"><span></span>Toxicity Properties (Avian)</H4>
                <div class="out_ container_output">
        """
    # table 3
    t3data = gett3data(trex_obj)
    t3rows = gethtmlrowsfromcols(t3data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t3rows, headings=pvuheadings)))
    html = html + """
                </div>
        """
    return html


def table_4(trex_obj):
    # pre-table 4
    html = """
            <H4 class="out_4 collapsible" id="section5"><span></span>Toxicity Properties (Mammal)</H4>
                <div class="out_ container_output">
        """
    # table 4
    t4data = gett4data(trex_obj)
    t4rows = gethtmlrowsfromcols(t4data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t4rows, headings=pvuheadings)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_5(trex_obj):
    # pre-table 5
    html = """
        <br>
        <H3 class="out_1 collapsible" id="section6"><span></span>Results (Upper Bound Kenaga): Application Type : {0!s}</H3>
            <div class="out_ container_output">
        """.format((trex_obj.application_type))
    # table 5
    out_sa_bird_1_s = trex_obj.out_sa_bird_1_s
    out_sa_bird_2_s = trex_obj.out_sa_bird_2_s
    out_sc_bird_s = trex_obj.out_sc_bird_s
    out_sa_mamm_1_s = trex_obj.out_sa_mamm_1_s
    out_sa_mamm_2_s = trex_obj.out_sa_mamm_2_s
    out_sc_mamm_s = trex_obj.out_sc_mamm_s

    out_sa_bird_1_m = trex_obj.out_sa_bird_1_m
    out_sa_bird_2_m = trex_obj.out_sa_bird_2_m
    out_sc_bird_m = trex_obj.out_sc_bird_m
    out_sa_mamm_1_m = trex_obj.out_sa_mamm_1_m
    out_sa_mamm_2_m = trex_obj.out_sa_mamm_2_m
    out_sc_mamm_m = trex_obj.out_sc_mamm_m

    out_sa_bird_1_l = trex_obj.out_sa_bird_1_l
    out_sa_bird_2_l = trex_obj.out_sa_bird_2_l
    out_sc_bird_l = trex_obj.out_sc_bird_l
    out_sa_mamm_1_l = trex_obj.out_sa_mamm_1_l
    out_sa_mamm_2_l = trex_obj.out_sa_mamm_2_l
    out_sc_mamm_l = trex_obj.out_sc_mamm_l

    t5data = gett5data(out_sa_bird_1_s, out_sa_bird_2_s, out_sc_bird_s, out_sa_mamm_1_s, out_sa_mamm_2_s, out_sc_mamm_s,
                       out_sa_bird_1_m, out_sa_bird_2_m, out_sc_bird_m, out_sa_mamm_1_m, out_sa_mamm_2_m, out_sc_mamm_m,
                       out_sa_bird_1_l, out_sa_bird_2_l, out_sc_bird_l, out_sa_mamm_1_l, out_sa_mamm_2_l, out_sc_mamm_l)
    t5rows = gethtmlrowsfromcols(t5data, pv5headings[1])
    html = html + tmpl.render(Context(
        dict(data=t5rows, headings=pv5headings[0], sub_headings=pv5headings[2], sub_headings_1=pv5headings[3],
             th_span='4')))
    html = html + """
                </div>
        """
    return {'html': html, 'out_sa_bird_1_s': out_sa_bird_1_s, 'out_sa_bird_2_s': out_sa_bird_2_s, 'out_sc_bird_s': out_sc_bird_s,
            'out_sa_mamm_1_s': out_sa_mamm_1_s, 'out_sa_mamm_2_s': out_sa_mamm_2_s, 'out_sc_mamm_s': out_sc_mamm_s,
            'out_sa_bird_1_m': out_sa_bird_1_m, 'out_sa_bird_2_m': out_sa_bird_2_m, 'out_sc_bird_m': out_sc_bird_m, 'out_sa_mamm_1_m': out_sa_mamm_1_m,
            'out_sa_mamm_2_m': out_sa_mamm_2_m, 'out_sc_mamm_m': out_sc_mamm_m,
            'out_sa_bird_1_l': out_sa_bird_1_l, 'out_sa_bird_2_l': out_sa_bird_2_l, 'out_sc_bird_l': out_sc_bird_l, 'out_sa_mamm_1_l': out_sa_mamm_1_l,
            'out_sa_mamm_2_l': out_sa_mamm_2_l, 'out_sc_mamm_l': out_sc_mamm_l}


def table_6(trex_obj):
    # pre-table 6
    html = """
        <br>
        <H3 class="out_1 collapsible" id="section6"><span></span>Results: Application Type : {0!s}</H3>
        <div class="out_">
            <H4 class="out_ collapsible" id="section7"><span></span>Dietary Based EECs (mg/kg-dietary item)</H4>
                <div class="out_ container_output">
        """.format((trex_obj.application_type))
    # table 6
    out_eec_diet_sg = trex_obj.out_eec_diet_sg
    out_eec_diet_tg = trex_obj.out_eec_diet_tg
    out_eec_diet_bp = trex_obj.out_eec_diet_bp
    out_eec_diet_fr = trex_obj.out_eec_diet_fr
    out_eec_diet_ar = trex_obj.out_eec_diet_ar

    t6data = gett6data(out_eec_diet_sg, out_eec_diet_tg, out_eec_diet_bp, out_eec_diet_fr, out_eec_diet_ar)
    t6rows = gethtmlrowsfromcols(t6data, pv6headings)
    html = html + tmpl.render(Context(dict(data=t6rows, headings=pv6headings)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_eec_diet_sg': out_eec_diet_sg, 'out_eec_diet_tg': out_eec_diet_tg, 'out_eec_diet_bp': out_eec_diet_bp,
            'out_eec_diet_fr': out_eec_diet_fr, 'out_eec_diet_ar': out_eec_diet_ar}


def table_7(trex_obj):
    # pre-table 7
    html = """
            <H4 class="out_ collapsible" id="section8"><span></span>Avian Dose Based EECs (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    # table 7
    out_eec_dose_bird_sg_sm = trex_obj.out_eec_dose_bird_sg_sm
    out_eec_dose_bird_sg_md = trex_obj.out_eec_dose_bird_sg_md
    out_eec_dose_bird_sg_lg = trex_obj.out_eec_dose_bird_sg_lg
    out_eec_dose_bird_tg_sm = trex_obj.out_eec_dose_bird_tg_sm
    out_eec_dose_bird_tg_md = trex_obj.out_eec_dose_bird_tg_md
    out_eec_dose_bird_tg_lg = trex_obj.out_eec_dose_bird_tg_lg
    out_eec_dose_bird_bp_sm = trex_obj.out_eec_dose_bird_bp_sm
    out_eec_dose_bird_bp_md = trex_obj.out_eec_dose_bird_bp_md
    out_eec_dose_bird_bp_lg = trex_obj.out_eec_dose_bird_bp_lg
    out_eec_dose_bird_fp_sm = trex_obj.out_eec_dose_bird_fp_sm
    out_eec_dose_bird_fp_md = trex_obj.out_eec_dose_bird_fp_md
    out_eec_dose_bird_fp_lg = trex_obj.out_eec_dose_bird_fp_lg
    out_eec_dose_bird_ar_sm = trex_obj.out_eec_dose_bird_ar_sm
    out_eec_dose_bird_ar_md = trex_obj.out_eec_dose_bird_ar_md
    out_eec_dose_bird_ar_lg = trex_obj.out_eec_dose_bird_ar_lg
    out_eec_dose_bird_se_sm = trex_obj.out_eec_dose_bird_se_sm
    out_eec_dose_bird_se_md = trex_obj.out_eec_dose_bird_se_md
    out_eec_dose_bird_se_lg = trex_obj.out_eec_dose_bird_se_lg

    t7data = gett7data(out_eec_dose_bird_sg_sm, out_eec_dose_bird_sg_md, out_eec_dose_bird_sg_lg, out_eec_dose_bird_tg_sm,
                       out_eec_dose_bird_tg_md, out_eec_dose_bird_tg_lg, out_eec_dose_bird_bp_sm, out_eec_dose_bird_bp_md,
                       out_eec_dose_bird_bp_lg, out_eec_dose_bird_fp_sm, out_eec_dose_bird_fp_md, out_eec_dose_bird_fp_lg,
                       out_eec_dose_bird_ar_sm, out_eec_dose_bird_ar_md, out_eec_dose_bird_ar_lg, out_eec_dose_bird_se_sm,
                       out_eec_dose_bird_se_md, out_eec_dose_bird_se_lg)
    t7rows = gethtmlrowsfromcols(t7data, pv7headings)
    html = html + tmpl.render(Context(dict(data=t7rows, headings=pv7headings)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_eec_dose_bird_sg_sm': out_eec_dose_bird_sg_sm, 'out_eec_dose_bird_sg_md': out_eec_dose_bird_sg_md,
            'out_eec_dose_bird_sg_lg': out_eec_dose_bird_sg_lg, 'out_eec_dose_bird_tg_sm': out_eec_dose_bird_tg_sm,
            'out_eec_dose_bird_tg_md': out_eec_dose_bird_tg_md, 'out_eec_dose_bird_tg_lg': out_eec_dose_bird_tg_lg,
            'out_eec_dose_bird_bp_sm': out_eec_dose_bird_bp_sm, 'out_eec_dose_bird_bp_md': out_eec_dose_bird_bp_md,
            'out_eec_dose_bird_bp_lg': out_eec_dose_bird_bp_lg, 'out_eec_dose_bird_fp_sm': out_eec_dose_bird_fp_sm,
            'out_eec_dose_bird_fp_md': out_eec_dose_bird_fp_md, 'out_eec_dose_bird_fp_lg': out_eec_dose_bird_fp_lg,
            'out_eec_dose_bird_ar_sm': out_eec_dose_bird_ar_sm, 'out_eec_dose_bird_ar_md': out_eec_dose_bird_ar_md,
            'out_eec_dose_bird_ar_lg': out_eec_dose_bird_ar_lg, 'out_eec_dose_bird_se_sm': out_eec_dose_bird_se_sm,
            'out_eec_dose_bird_se_md': out_eec_dose_bird_se_md, 'out_eec_dose_bird_se_lg': out_eec_dose_bird_se_lg}


def table_7_add(trex_obj):
    # pre-table 7
    html = """
            <H4 class="out_ collapsible" id="section8_add"><span></span>Avian Dose Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 7_add
    out_arq_bird_sg_sm = trex_obj.out_arq_bird_sg_sm
    out_arq_bird_sg_md = trex_obj.out_arq_bird_sg_md
    out_arq_bird_sg_lg = trex_obj.out_arq_bird_sg_lg
    out_arq_bird_tg_sm = trex_obj.out_arq_bird_tg_sm
    out_arq_bird_tg_md = trex_obj.out_arq_bird_tg_md
    out_arq_bird_tg_lg = trex_obj.out_arq_bird_tg_lg
    out_arq_bird_bp_sm = trex_obj.out_arq_bird_bp_sm
    out_arq_bird_bp_md = trex_obj.out_arq_bird_bp_md
    out_arq_bird_bp_lg = trex_obj.out_arq_bird_bp_lg
    out_arq_bird_fp_sm = trex_obj.out_arq_bird_fp_sm
    out_arq_bird_fp_md = trex_obj.out_arq_bird_fp_md
    out_arq_bird_fp_lg = trex_obj.out_arq_bird_fp_lg
    out_arq_bird_ar_sm = trex_obj.out_arq_bird_ar_sm
    out_arq_bird_ar_md = trex_obj.out_arq_bird_ar_md
    out_arq_bird_ar_lg = trex_obj.out_arq_bird_ar_lg
    out_arq_bird_se_sm = trex_obj.out_arq_bird_se_sm
    out_arq_bird_se_md = trex_obj.out_arq_bird_se_md
    out_arq_bird_se_lg = trex_obj.out_arq_bird_se_lg

    t7_add_data = gett7_add_data(out_arq_bird_sg_sm, out_arq_bird_sg_md, out_arq_bird_sg_lg, out_arq_bird_tg_sm, out_arq_bird_tg_md,
                                 out_arq_bird_tg_lg, out_arq_bird_bp_sm, out_arq_bird_bp_md, out_arq_bird_bp_lg, out_arq_bird_fp_sm,
                                 out_arq_bird_fp_md, out_arq_bird_fp_lg, out_arq_bird_ar_sm, out_arq_bird_ar_md, out_arq_bird_ar_lg,
                                 out_arq_bird_se_sm, out_arq_bird_se_md, out_arq_bird_se_lg)
    t7_add_rows = gethtmlrowsfromcols(t7_add_data, pv7headings)
    html = html + tmpl.render(Context(dict(data=t7_add_rows, headings=pv7headings)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_arq_bird_sg_sm': out_arq_bird_sg_sm, 'out_arq_bird_sg_md': out_arq_bird_sg_md,
            'out_arq_bird_sg_lg': out_arq_bird_sg_lg, 'out_arq_bird_tg_sm': out_arq_bird_tg_sm, 'out_arq_bird_tg_md': out_arq_bird_tg_md,
            'out_arq_bird_tg_lg': out_arq_bird_tg_lg,
            'out_arq_bird_bp_sm': out_arq_bird_bp_sm, 'out_arq_bird_bp_md': out_arq_bird_bp_md, 'out_arq_bird_bp_lg': out_arq_bird_bp_lg,
            'out_arq_bird_fp_sm': out_arq_bird_fp_sm, 'out_arq_bird_fp_md': out_arq_bird_fp_md, 'out_arq_bird_fp_lg': out_arq_bird_fp_lg,
            'out_arq_bird_ar_sm': out_arq_bird_ar_sm, 'out_arq_bird_ar_md': out_arq_bird_ar_md, 'out_arq_bird_ar_lg': out_arq_bird_ar_lg,
            'out_arq_bird_se_sm': out_arq_bird_se_sm, 'out_arq_bird_se_md': out_arq_bird_se_md, 'out_arq_bird_se_lg': out_arq_bird_se_lg}


def table_8(trex_obj):
    # pre-table 8
    html = """
            <H4 class="out_ collapsible" id="section9"><span></span>Avian Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 8
    out_arq_diet_bird_sg_a = trex_obj.out_arq_diet_bird_sg_a
    out_arq_diet_bird_sg_c = trex_obj.out_arq_diet_bird_sg_c
    out_arq_diet_bird_tg_a = trex_obj.out_arq_diet_bird_tg_a
    out_arq_diet_bird_tg_c = trex_obj.out_arq_diet_bird_tg_c
    out_arq_diet_bird_bp_a = trex_obj.out_arq_diet_bird_bp_a
    out_arq_diet_bird_bp_c = trex_obj.out_arq_diet_bird_bp_c
    out_arq_diet_bird_fp_a = trex_obj.out_arq_diet_bird_fp_a
    out_arq_diet_bird_fp_c = trex_obj.out_arq_diet_bird_fp_c
    out_arq_diet_bird_ar_a = trex_obj.out_arq_diet_bird_ar_a
    out_arq_diet_bird_ar_c = trex_obj.out_arq_diet_bird_ar_c

    t8data = gett8data(out_arq_diet_bird_sg_a, out_arq_diet_bird_sg_c, out_arq_diet_bird_tg_a, out_arq_diet_bird_tg_c,
                       out_arq_diet_bird_bp_a, out_arq_diet_bird_bp_c, out_arq_diet_bird_fp_a, out_arq_diet_bird_fp_c,
                       out_arq_diet_bird_ar_a, out_arq_diet_bird_ar_c)
    t8rows = gethtmlrowsfromcols(t8data, pv8headings)
    html = html + tmpl.render(Context(dict(data=t8rows, headings=pv8headings)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_arq_diet_bird_sg_a': out_arq_diet_bird_sg_a, 'out_arq_diet_bird_sg_c': out_arq_diet_bird_sg_c,
            'out_arq_diet_bird_tg_a': out_arq_diet_bird_tg_a, 'out_arq_diet_bird_tg_c': out_arq_diet_bird_tg_c,
            'out_arq_diet_bird_bp_a': out_arq_diet_bird_bp_a, 'out_arq_diet_bird_bp_c': out_arq_diet_bird_bp_c,
            'out_arq_diet_bird_fp_a': out_arq_diet_bird_fp_a, 'out_arq_diet_bird_fp_c': out_arq_diet_bird_fp_c,
            'out_arq_diet_bird_ar_a': out_arq_diet_bird_ar_a, 'out_arq_diet_bird_ar_c': out_arq_diet_bird_ar_c}


def table_9(trex_obj):
    # pre-table 9
    html = """
            <H4 class="out_ collapsible" id="section10"><span></span>Mammalian Dose Based EECs (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    # table 9
    out_eec_dose_mamm_sg_sm = trex_obj.out_eec_dose_mamm_sg_sm
    out_eec_dose_mamm_sg_md = trex_obj.out_eec_dose_mamm_sg_md
    out_eec_dose_mamm_sg_lg = trex_obj.out_eec_dose_mamm_sg_lg
    out_eec_dose_mamm_tg_sm = trex_obj.out_eec_dose_mamm_tg_sm
    out_eec_dose_mamm_tg_md = trex_obj.out_eec_dose_mamm_tg_md
    out_eec_dose_mamm_tg_lg = trex_obj.out_eec_dose_mamm_tg_lg
    out_eec_dose_mamm_bp_sm = trex_obj.out_eec_dose_mamm_bp_sm
    out_eec_dose_mamm_bp_md = trex_obj.out_eec_dose_mamm_bp_md
    out_eec_dose_mamm_bp_lg = trex_obj.out_eec_dose_mamm_bp_lg
    out_eec_dose_mamm_fp_sm = trex_obj.out_eec_dose_mamm_fp_sm
    out_eec_dose_mamm_fp_md = trex_obj.out_eec_dose_mamm_fp_md
    out_eec_dose_mamm_fp_lg = trex_obj.out_eec_dose_mamm_fp_lg
    out_eec_dose_mamm_ar_sm = trex_obj.out_eec_dose_mamm_ar_sm
    out_eec_dose_mamm_ar_md = trex_obj.out_eec_dose_mamm_ar_md
    out_eec_dose_mamm_ar_lg = trex_obj.out_eec_dose_mamm_ar_lg
    out_eec_dose_mamm_se_sm = trex_obj.out_eec_dose_mamm_se_sm
    out_eec_dose_mamm_se_md = trex_obj.out_eec_dose_mamm_se_md
    out_eec_dose_mamm_se_lg = trex_obj.out_eec_dose_mamm_se_lg

    t9data = gett9data(out_eec_dose_mamm_sg_sm, out_eec_dose_mamm_sg_md, out_eec_dose_mamm_sg_lg, out_eec_dose_mamm_tg_sm,
                       out_eec_dose_mamm_tg_md, out_eec_dose_mamm_tg_lg, out_eec_dose_mamm_bp_sm, out_eec_dose_mamm_bp_md,
                       out_eec_dose_mamm_bp_lg, out_eec_dose_mamm_fp_sm, out_eec_dose_mamm_fp_md, out_eec_dose_mamm_fp_lg,
                       out_eec_dose_mamm_ar_sm, out_eec_dose_mamm_ar_md, out_eec_dose_mamm_ar_lg, out_eec_dose_mamm_se_sm,
                       out_eec_dose_mamm_se_md, out_eec_dose_mamm_se_lg)
    t9rows = gethtmlrowsfromcols(t9data, pv7headings)
    html = html + tmpl.render(Context(dict(data=t9rows, headings=pv7headings)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_eec_dose_mamm_sg_sm': out_eec_dose_mamm_sg_sm, 'out_eec_dose_mamm_sg_md': out_eec_dose_mamm_sg_md,
            'out_eec_dose_mamm_sg_lg': out_eec_dose_mamm_sg_lg, 'out_eec_dose_mamm_tg_sm': out_eec_dose_mamm_tg_sm,
            'out_eec_dose_mamm_tg_md': out_eec_dose_mamm_tg_md, 'out_eec_dose_mamm_tg_lg': out_eec_dose_mamm_tg_lg,
            'out_eec_dose_mamm_bp_sm': out_eec_dose_mamm_bp_sm, 'out_eec_dose_mamm_bp_md': out_eec_dose_mamm_bp_md,
            'out_eec_dose_mamm_bp_lg': out_eec_dose_mamm_bp_lg, 'out_eec_dose_mamm_fp_sm': out_eec_dose_mamm_fp_sm,
            'out_eec_dose_mamm_fp_md': out_eec_dose_mamm_fp_md, 'out_eec_dose_mamm_fp_lg': out_eec_dose_mamm_fp_lg,
            'out_eec_dose_mamm_ar_sm': out_eec_dose_mamm_ar_sm, 'out_eec_dose_mamm_ar_md': out_eec_dose_mamm_ar_md,
            'out_eec_dose_mamm_ar_lg': out_eec_dose_mamm_ar_lg, 'out_eec_dose_mamm_se_sm': out_eec_dose_mamm_se_sm,
            'out_eec_dose_mamm_se_md': out_eec_dose_mamm_se_md, 'out_eec_dose_mamm_se_lg': out_eec_dose_mamm_se_lg}


def table_10(trex_obj):
    # pre-table 10
    html = """
            <H4 class="out_ collapsible" id="section11"><span></span>Mammalian Dose Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 10
    out_arq_dose_mamm_sg_sm = trex_obj.out_arq_dose_mamm_sg_sm
    out_crq_dose_mamm_sg_sm = trex_obj.out_crq_dose_mamm_sg_sm
    out_arq_dose_mamm_sg_md = trex_obj.out_arq_dose_mamm_sg_md
    out_crq_dose_mamm_sg_md = trex_obj.out_crq_dose_mamm_sg_md
    out_arq_dose_mamm_sg_lg = trex_obj.out_arq_dose_mamm_sg_lg
    out_crq_dose_mamm_sg_lg = trex_obj.out_crq_dose_mamm_sg_lg

    out_arq_dose_mamm_tg_sm = trex_obj.out_arq_dose_mamm_tg_sm
    out_crq_dose_mamm_tg_sm = trex_obj.out_crq_dose_mamm_tg_sm
    out_arq_dose_mamm_tg_md = trex_obj.out_arq_dose_mamm_tg_md
    out_crq_dose_mamm_tg_md = trex_obj.out_crq_dose_mamm_tg_md
    out_arq_dose_mamm_tg_lg = trex_obj.out_arq_dose_mamm_tg_lg
    out_crq_dose_mamm_tg_lg = trex_obj.out_crq_dose_mamm_tg_lg

    out_arq_dose_mamm_bp_sm = trex_obj.out_arq_dose_mamm_bp_sm
    out_crq_dose_mamm_bp_sm = trex_obj.out_crq_dose_mamm_bp_sm
    out_arq_dose_mamm_bp_md = trex_obj.out_arq_dose_mamm_bp_md
    out_crq_dose_mamm_bp_md = trex_obj.out_crq_dose_mamm_bp_md
    out_arq_dose_mamm_bp_lg = trex_obj.out_arq_dose_mamm_bp_lg
    out_crq_dose_mamm_bp_lg = trex_obj.out_crq_dose_mamm_bp_lg

    out_arq_dose_mamm_fp_sm = trex_obj.out_arq_dose_mamm_fp_sm
    out_crq_dose_mamm_fp_sm = trex_obj.out_crq_dose_mamm_fp_sm
    out_arq_dose_mamm_fp_md = trex_obj.out_arq_dose_mamm_fp_md
    out_crq_dose_mamm_fp_md = trex_obj.out_crq_dose_mamm_fp_md
    out_arq_dose_mamm_fp_lg = trex_obj.out_arq_dose_mamm_fp_lg
    out_crq_dose_mamm_fp_lg = trex_obj.out_crq_dose_mamm_fp_lg

    out_arq_dose_mamm_ar_sm = trex_obj.out_arq_dose_mamm_ar_sm
    out_crq_dose_mamm_ar_sm = trex_obj.out_crq_dose_mamm_ar_sm
    out_arq_dose_mamm_ar_md = trex_obj.out_arq_dose_mamm_ar_md
    out_crq_dose_mamm_ar_md = trex_obj.out_crq_dose_mamm_ar_md
    out_arq_dose_mamm_ar_lg = trex_obj.out_arq_dose_mamm_ar_lg
    out_crq_dose_mamm_ar_lg = trex_obj.out_crq_dose_mamm_ar_lg

    out_arq_dose_mamm_se_sm = trex_obj.out_arq_dose_mamm_se_sm
    out_crq_dose_mamm_se_sm = trex_obj.out_crq_dose_mamm_se_sm
    out_arq_dose_mamm_se_md = trex_obj.out_arq_dose_mamm_se_md
    out_crq_dose_mamm_se_md = trex_obj.out_crq_dose_mamm_se_md
    out_arq_dose_mamm_se_lg = trex_obj.out_arq_dose_mamm_se_lg
    out_crq_dose_mamm_se_lg = trex_obj.out_crq_dose_mamm_se_lg

    t10data = gett10data(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md, out_crq_dose_mamm_sg_md,
                         out_arq_dose_mamm_sg_lg, out_crq_dose_mamm_sg_lg, out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm,
                         out_arq_dose_mamm_tg_md, out_crq_dose_mamm_tg_md, out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg,
                         out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md, out_crq_dose_mamm_bp_md,
                         out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg, out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm,
                         out_arq_dose_mamm_fp_md, out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg,
                         out_arq_dose_mamm_ar_sm, out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md, out_crq_dose_mamm_ar_md,
                         out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg, out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm,
                         out_arq_dose_mamm_se_md, out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg, out_crq_dose_mamm_se_lg)
    t10rows = gethtmlrowsfromcols(t10data, pv10headings)
    html = html + tmpl_10.render(Context(dict(data=t10rows)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_arq_dose_mamm_sg_sm': out_arq_dose_mamm_sg_sm, 'out_crq_dose_mamm_sg_sm': out_crq_dose_mamm_sg_sm,
            'out_arq_dose_mamm_sg_md': out_arq_dose_mamm_sg_md, 'out_crq_dose_mamm_sg_md': out_crq_dose_mamm_sg_md,
            'out_arq_dose_mamm_sg_lg': out_arq_dose_mamm_sg_lg, 'out_crq_dose_mamm_sg_lg': out_crq_dose_mamm_sg_lg,
            'out_arq_dose_mamm_tg_sm': out_arq_dose_mamm_tg_sm, 'out_crq_dose_mamm_tg_sm': out_crq_dose_mamm_tg_sm,
            'out_arq_dose_mamm_tg_md': out_arq_dose_mamm_tg_md, 'out_crq_dose_mamm_tg_md': out_crq_dose_mamm_tg_md,
            'out_arq_dose_mamm_tg_lg': out_arq_dose_mamm_tg_lg, 'out_crq_dose_mamm_tg_lg': out_crq_dose_mamm_tg_lg,
            'out_arq_dose_mamm_bp_sm': out_arq_dose_mamm_bp_sm, 'out_crq_dose_mamm_bp_sm': out_crq_dose_mamm_bp_sm,
            'out_arq_dose_mamm_bp_md': out_arq_dose_mamm_bp_md, 'out_crq_dose_mamm_bp_md': out_crq_dose_mamm_bp_md,
            'out_arq_dose_mamm_bp_lg': out_arq_dose_mamm_bp_lg, 'out_crq_dose_mamm_bp_lg': out_crq_dose_mamm_bp_lg,
            'out_arq_dose_mamm_fp_sm': out_arq_dose_mamm_fp_sm, 'out_crq_dose_mamm_fp_sm': out_crq_dose_mamm_fp_sm,
            'out_arq_dose_mamm_fp_md': out_arq_dose_mamm_fp_md, 'out_crq_dose_mamm_fp_md': out_crq_dose_mamm_fp_md,
            'out_arq_dose_mamm_fp_lg': out_arq_dose_mamm_fp_lg, 'out_crq_dose_mamm_fp_lg': out_crq_dose_mamm_fp_lg,
            'out_arq_dose_mamm_ar_sm': out_arq_dose_mamm_ar_sm, 'out_crq_dose_mamm_ar_sm': out_crq_dose_mamm_ar_sm,
            'out_arq_dose_mamm_ar_md': out_arq_dose_mamm_ar_md, 'out_crq_dose_mamm_ar_md': out_crq_dose_mamm_ar_md,
            'out_arq_dose_mamm_ar_lg': out_arq_dose_mamm_ar_lg, 'out_crq_dose_mamm_ar_lg': out_crq_dose_mamm_ar_lg,
            'out_arq_dose_mamm_se_sm': out_arq_dose_mamm_se_sm, 'out_crq_dose_mamm_se_sm': out_crq_dose_mamm_se_sm,
            'out_arq_dose_mamm_se_md': out_arq_dose_mamm_se_md, 'out_crq_dose_mamm_se_md': out_crq_dose_mamm_se_md,
            'out_arq_dose_mamm_se_lg': out_arq_dose_mamm_se_lg, 'out_crq_dose_mamm_se_lg': out_crq_dose_mamm_se_lg}


def table_11(trex_obj):
    # pre-table 11
    html = """
            <H4 class="out_ collapsible" id="section12"><span></span>Mammalian Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 11
    out_arq_diet_mamm_sg = trex_obj.out_arq_diet_mamm_sg
    out_crq_diet_mamm_sg = trex_obj.out_crq_diet_mamm_sg
    out_arq_diet_mamm_tg = trex_obj.out_arq_diet_mamm_tg
    out_crq_diet_mamm_tg = trex_obj.out_crq_diet_mamm_tg
    out_arq_diet_mamm_bp = trex_obj.out_arq_diet_mamm_bp
    out_crq_diet_mamm_bp = trex_obj.out_crq_diet_mamm_bp
    out_arq_diet_mamm_fp = trex_obj.out_arq_diet_mamm_fp
    out_crq_diet_mamm_fp = trex_obj.out_crq_diet_mamm_fp
    out_arq_diet_mamm_ar = trex_obj.out_arq_diet_mamm_ar
    out_crq_diet_mamm_ar = trex_obj.out_crq_diet_mamm_ar
    if out_arq_diet_mamm_sg == 'N/A':
        t11data = gett11data_na(out_arq_diet_mamm_sg, out_crq_diet_mamm_sg, out_arq_diet_mamm_tg, out_crq_diet_mamm_tg,
                                out_arq_diet_mamm_bp, out_crq_diet_mamm_bp, out_arq_diet_mamm_fp, out_crq_diet_mamm_fp,
                                out_arq_diet_mamm_ar, out_crq_diet_mamm_ar)
    else:
        t11data = gett11data(out_arq_diet_mamm_sg, out_crq_diet_mamm_sg, out_arq_diet_mamm_tg, out_crq_diet_mamm_tg, out_arq_diet_mamm_bp,
                             out_crq_diet_mamm_bp, out_arq_diet_mamm_fp, out_crq_diet_mamm_fp, out_arq_diet_mamm_ar, out_crq_diet_mamm_ar)
    t11rows = gethtmlrowsfromcols(t11data, pv8headings)
    html = html + tmpl.render(Context(dict(data=t11rows, headings=pv8headings)))
    html = html + """
                </div>
        """
    return {'html': html, 'out_arq_diet_mamm_sg': out_arq_diet_mamm_sg, 'out_crq_diet_mamm_sg': out_crq_diet_mamm_sg,
            'out_arq_diet_mamm_tg': out_arq_diet_mamm_tg, 'out_crq_diet_mamm_tg': out_crq_diet_mamm_tg,
            'out_arq_diet_mamm_bp': out_arq_diet_mamm_bp, 'out_crq_diet_mamm_bp': out_crq_diet_mamm_bp,
            'out_arq_diet_mamm_fp': out_arq_diet_mamm_fp, 'out_crq_diet_mamm_fp': out_crq_diet_mamm_fp,
            'out_arq_diet_mamm_ar': out_arq_diet_mamm_ar, 'out_crq_diet_mamm_ar': out_crq_diet_mamm_ar}


def table_12(trex_obj):
    # pre-table 12
    html = """
            <H4 class="out_ collapsible" id="section13"><span></span>LD<sub>50</sub> ft<sup>-2</sup></H4>
                <div class="out_ container_output">
        """
    # table 12
    out_ld50_rg_bird_sm = trex_obj.out_ld50_rg_bird_sm
    out_ld50_rg_mamm_sm = trex_obj.out_ld50_rg_mamm_sm
    out_ld50_rg_bird_md = trex_obj.out_ld50_rg_bird_md
    out_ld50_rg_mamm_md = trex_obj.out_ld50_rg_mamm_md
    out_ld50_rg_bird_lg = trex_obj.out_ld50_rg_bird_lg
    out_ld50_rg_mamm_lg = trex_obj.out_ld50_rg_mamm_lg

    t12data = gett12data(out_ld50_rg_bird_sm, out_ld50_rg_mamm_sm, out_ld50_rg_bird_md, out_ld50_rg_mamm_md, out_ld50_rg_bird_lg,
                         out_ld50_rg_mamm_lg)
    t12rows = gethtmlrowsfromcols(t12data, pv12headings)
    html = html + tmpl.render(Context(dict(data=t12rows, headings=pv12headings)))
    html = html + """
                </div>
        </div>
        """
    return {'html': html, 'out_ld50_rg_bird_sm': out_ld50_rg_bird_sm, 'out_ld50_rg_mamm_sm': out_ld50_rg_mamm_sm,
            'out_ld50_rg_bird_md': out_ld50_rg_bird_md, 'out_ld50_rg_mamm_md': out_ld50_rg_mamm_md,
            'out_ld50_rg_bird_lg': out_ld50_rg_bird_lg, 'out_ld50_rg_mamm_lg': out_ld50_rg_mamm_lg}


def table_13(trex_obj):
    # pre-table 13
    html = """
            <H4 class="out_ collapsible" id="section13"><span></span>LD<sub>50</sub> ft<sup>-2</sup></H4>
                <div class="out_ container_output">
        """
    # table 13
    out_ld50_rl_bird_sm = trex_obj.out_ld50_rl_bird_sm
    out_ld50_rl_mamm_sm = trex_obj.out_ld50_rl_mamm_sm
    out_ld50_rl_bird_md = trex_obj.out_ld50_rl_bird_md
    out_ld50_rl_mamm_md = trex_obj.out_ld50_rl_mamm_md
    out_ld50_rl_bird_lg = trex_obj.out_ld50_rl_bird_lg
    out_ld50_rl_mamm_lg = trex_obj.out_ld50_rl_mamm_lg

    t13data = gett12data(out_ld50_rl_bird_sm, out_ld50_rl_mamm_sm, out_ld50_rl_bird_md, out_ld50_rl_mamm_md, out_ld50_rl_bird_lg,
                         out_ld50_rl_mamm_lg)
    t13rows = gethtmlrowsfromcols(t13data, pv12headings)
    html = html + tmpl.render(Context(dict(data=t13rows, headings=pv12headings)))
    html = html + """
                </div>
        </div>
        """
    return {'html': html, 'out_ld50_rl_bird_sm': out_ld50_rl_bird_sm, 'out_ld50_rl_mamm_sm': out_ld50_rl_mamm_sm,
            'out_ld50_rl_bird_md': out_ld50_rl_bird_md, 'out_ld50_rl_mamm_md': out_ld50_rl_mamm_md,
            'out_ld50_rl_bird_lg': out_ld50_rl_bird_lg, 'out_ld50_rl_mamm_lg': out_ld50_rl_mamm_lg}


def table_14(trex_obj):
    # pre-table 14
    html = """
            <H4 class="out_ collapsible" id="section13"><span></span>LD<sub>50</sub> ft<sup>-2</sup></H4>
                <div class="out_ container_output">
        """
    # table 14
    out_ld50_bg_bird_sm = trex_obj.out_ld50_bg_bird_sm
    out_ld50_bg_mamm_sm = trex_obj.out_ld50_bg_mamm_sm
    out_ld50_bg_bird_md = trex_obj.out_ld50_bg_bird_md
    out_ld50_bg_mamm_md = trex_obj.out_ld50_bg_mamm_md
    out_ld50_bg_bird_lg = trex_obj.out_ld50_bg_bird_lg
    out_ld50_bg_mamm_lg = trex_obj.out_ld50_bg_mamm_lg

    t14data = gett12data(out_ld50_bg_bird_sm, out_ld50_bg_mamm_sm, out_ld50_bg_bird_md, out_ld50_bg_mamm_md, out_ld50_bg_bird_lg,
                         out_ld50_bg_mamm_lg)
    t14rows = gethtmlrowsfromcols(t14data, pv12headings)
    html = html + tmpl.render(Context(dict(data=t14rows, headings=pv12headings)))
    html = html + """
                </div>
        </div>
        """
    return {'html': html, 'out_ld50_bg_bird_sm': out_ld50_bg_bird_sm, 'out_ld50_bg_mamm_sm': out_ld50_bg_mamm_sm,
            'out_ld50_bg_bird_md': out_ld50_bg_bird_md, 'out_ld50_bg_mamm_md': out_ld50_bg_mamm_md,
            'out_ld50_bg_bird_lg': out_ld50_bg_bird_lg, 'out_ld50_bg_mamm_lg': out_ld50_bg_mamm_lg}


def table_15(trex_obj):
    # pre-table 15
    html = """
            <H4 class="out_ collapsible" id="section13"><span></span>LD<sub>50</sub> ft<sup>-2</sup></H4>
                <div class="out_ container_output">
        """
    # table 15
    out_ld50_bl_bird_sm = trex_obj.out_ld50_bl_bird_sm
    out_ld50_bl_mamm_sm = trex_obj.out_ld50_bl_mamm_sm
    out_ld50_bl_bird_md = trex_obj.out_ld50_bl_bird_md
    out_ld50_bl_mamm_md = trex_obj.out_ld50_bl_mamm_md
    out_ld50_bl_bird_lg = trex_obj.out_ld50_bl_bird_lg
    out_ld50_bl_mamm_lg = trex_obj.out_ld50_bl_mamm_lg

    t15data = gett12data(out_ld50_bl_bird_sm, out_ld50_bl_mamm_sm, out_ld50_bl_bird_md, out_ld50_bl_mamm_md, out_ld50_bl_bird_lg,
                         out_ld50_bl_mamm_lg)
    t15rows = gethtmlrowsfromcols(t15data, pv12headings)
    html = html + tmpl.render(Context(dict(data=t15rows, headings=pv12headings)))
    html = html + """
                </div>
        </div>
        """
    return {'html': html, 'out_ld50_bl_bird_sm': out_ld50_bl_bird_sm, 'out_ld50_bl_mamm_sm': out_ld50_bl_mamm_sm,
            'out_ld50_bl_bird_md': out_ld50_bl_bird_md, 'out_ld50_bl_mamm_md': out_ld50_bl_mamm_md,
            'out_ld50_bl_bird_lg': out_ld50_bl_bird_lg, 'out_ld50_bl_mamm_lg': out_ld50_bl_mamm_lg}


def table_5_qaqc(trex_obj):
    # pre-table 5_qaqc
    html = """
        <br>
        <H3 class="out_1 collapsible" id="section6"><span></span>Results (Upper Bound Kenaga): Application Type : Seed Treatment</H3>
            <div class="out_ container_output">
        """
    # table 5_qaqc
    out_sa_bird_1_s = trex_obj.out_sa_bird_1_s
    out_sa_bird_2_s = trex_obj.out_sa_bird_2_s
    out_sc_bird_s = trex_obj.out_sc_bird_s
    out_sa_mamm_1_s = trex_obj.out_sa_mamm_1_s
    out_sa_mamm_2_s = trex_obj.out_sa_mamm_2_s
    out_sc_mamm_s = trex_obj.out_sc_mamm_s

    out_sa_bird_1_m = trex_obj.out_sa_bird_1_m
    out_sa_bird_2_m = trex_obj.out_sa_bird_2_m
    out_sc_bird_m = trex_obj.out_sc_bird_m
    out_sa_mamm_1_m = trex_obj.out_sa_mamm_1_m
    out_sa_mamm_2_m = trex_obj.out_sa_mamm_2_m
    out_sc_mamm_m = trex_obj.out_sc_mamm_m

    out_sa_bird_1_l = trex_obj.out_sa_bird_1_l
    out_sa_bird_2_l = trex_obj.out_sa_bird_2_l
    out_sc_bird_l = trex_obj.out_sc_bird_l
    out_sa_mamm_1_l = trex_obj.out_sa_mamm_1_l
    out_sa_mamm_2_l = trex_obj.out_sa_mamm_2_l
    out_sc_mamm_l = trex_obj.out_sc_mamm_l

    out_sa_bird_1_s_exp = trex_obj.out_sa_bird_1_s_out_exp
    out_sa_bird_2_s_exp = trex_obj.out_sa_bird_2_s_out_exp
    out_sc_bird_s_exp = trex_obj.out_sc_bird_s_out_exp
    out_sa_mamm_1_s_exp = trex_obj.out_sa_mamm_1_s_out_exp
    out_sa_mamm_2_s_exp = trex_obj.out_sa_mamm_2_s_out_exp
    out_sc_mamm_s_exp = trex_obj.out_sc_mamm_s_out_exp

    out_sa_bird_1_m_exp = trex_obj.out_sa_bird_1_m_out_exp
    out_sa_bird_2_m_exp = trex_obj.out_sa_bird_2_m_out_exp
    out_sc_bird_m_exp = trex_obj.out_sc_bird_m_out_exp
    out_sa_mamm_1_m_exp = trex_obj.out_sa_mamm_1_m_out_exp
    out_sa_mamm_2_m_exp = trex_obj.out_sa_mamm_2_m_out_exp
    out_sc_mamm_m_exp = trex_obj.out_sc_mamm_m_out_exp

    out_sa_bird_1_l_exp = trex_obj.out_sa_bird_1_l_out_exp
    out_sa_bird_2_l_exp = trex_obj.out_sa_bird_2_l_out_exp
    out_sc_bird_l_exp = trex_obj.out_sc_bird_l_out_exp
    out_sa_mamm_1_l_exp = trex_obj.out_sa_mamm_1_l_out_exp
    out_sa_mamm_2_l_exp = trex_obj.out_sa_mamm_2_l_out_exp
    out_sc_mamm_l_exp = trex_obj.out_sc_mamm_l_out_exp

    t5data_qaqc = gett5data_qaqc(out_sa_bird_1_s, out_sa_bird_2_s, out_sc_bird_s, out_sa_mamm_1_s, out_sa_mamm_2_s, out_sc_mamm_s,
                                 out_sa_bird_1_m, out_sa_bird_2_m, out_sc_bird_m, out_sa_mamm_1_m, out_sa_mamm_2_m, out_sc_mamm_m,
                                 out_sa_bird_1_l, out_sa_bird_2_l, out_sc_bird_l, out_sa_mamm_1_l, out_sa_mamm_2_l, out_sc_mamm_l,
                                 out_sa_bird_1_s_exp, out_sa_bird_2_s_exp, out_sc_bird_s_exp, out_sa_mamm_1_s_exp, out_sa_mamm_2_s_exp,
                                 out_sc_mamm_s_exp,
                                 out_sa_bird_1_m_exp, out_sa_bird_2_m_exp, out_sc_bird_m_exp, out_sa_mamm_1_m_exp, out_sa_mamm_2_m_exp,
                                 out_sc_mamm_m_exp,
                                 out_sa_bird_1_l_exp, out_sa_bird_2_l_exp, out_sc_bird_l_exp, out_sa_mamm_1_l_exp, out_sa_mamm_2_l_exp,
                                 out_sc_mamm_l_exp)
    t5rows_qaqc = gethtmlrowsfromcols(t5data_qaqc, pv5headings_qaqc[1])
    html = html + tmpl.render(Context(
        dict(data=t5rows_qaqc, headings=pv5headings_qaqc[0], sub_headings=pv5headings_qaqc[2],
             sub_headings_1=pv5headings_qaqc[3], th_span='4')))
    html = html + """
                </div>
        """
    return html


def table_6_qaqc(trex_obj):
    # pre-table 6_qaqc
    html = """
        <br>
        <H3 class="out_1 collapsible" id="section6"><span></span>Results: Application Type : Broadcast-Liquid</H3>
        <div class="out_">
            <H4 class="out_ collapsible" id="section7"><span></span>Dietary Based EECs (mg/kg-dietary item)</H4>
                <div class="out_ container_output">
        """
    # table 6_qaqc
    out_eec_diet_sg = trex_obj.out_eec_diet_sg
    out_eec_diet_tg = trex_obj.out_eec_diet_tg
    out_eec_diet_bp = trex_obj.out_eec_diet_bp
    out_eec_diet_fr = trex_obj.out_eec_diet_fr
    out_eec_diet_ar = trex_obj.out_eec_diet_ar

    out_eec_diet_sg_exp = trex_obj.out_eec_diet_sg_BL_out_exp
    out_eec_diet_tg_exp = trex_obj.out_eec_diet_tg_BL_out_exp
    out_eec_diet_bp_exp = trex_obj.out_eec_diet_bp_BL_out_exp
    out_eec_diet_fr_exp = trex_obj.out_eec_diet_fr_BL_out_exp
    out_eec_diet_ar_exp = trex_obj.out_eec_diet_ar_BL_out_exp

    t6data_qaqc = gett6data_qaqc(out_eec_diet_sg, out_eec_diet_tg, out_eec_diet_bp, out_eec_diet_fr, out_eec_diet_ar, out_eec_diet_sg_exp,
                                 out_eec_diet_tg_exp, out_eec_diet_bp_exp, out_eec_diet_fr_exp, out_eec_diet_ar_exp)
    t6rows_qaqc = gethtmlrowsfromcols(t6data_qaqc, pv6headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t6rows_qaqc, headings=pv6headings_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_7_qaqc(trex_obj):
    # pre-table 7
    html = """
            <H4 class="out_ collapsible" id="section8"><span></span>Avian Dose Based EECs (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    # table 7
    out_eec_dose_bird_sg_sm = trex_obj.out_eec_dose_bird_sg_sm
    out_eec_dose_bird_sg_md = trex_obj.out_eec_dose_bird_sg_md
    out_eec_dose_bird_sg_lg = trex_obj.out_eec_dose_bird_sg_lg
    out_eec_dose_bird_tg_sm = trex_obj.out_eec_dose_bird_tg_sm
    out_eec_dose_bird_tg_md = trex_obj.out_eec_dose_bird_tg_md
    out_eec_dose_bird_tg_lg = trex_obj.out_eec_dose_bird_tg_lg
    out_eec_dose_bird_bp_sm = trex_obj.out_eec_dose_bird_bp_sm
    out_eec_dose_bird_bp_md = trex_obj.out_eec_dose_bird_bp_md
    out_eec_dose_bird_bp_lg = trex_obj.out_eec_dose_bird_bp_lg
    out_eec_dose_bird_fp_sm = trex_obj.out_eec_dose_bird_fp_sm
    out_eec_dose_bird_fp_md = trex_obj.out_eec_dose_bird_fp_md
    out_eec_dose_bird_fp_lg = trex_obj.out_eec_dose_bird_fp_lg
    out_eec_dose_bird_ar_sm = trex_obj.out_eec_dose_bird_ar_sm
    out_eec_dose_bird_ar_md = trex_obj.out_eec_dose_bird_ar_md
    out_eec_dose_bird_ar_lg = trex_obj.out_eec_dose_bird_ar_lg
    out_eec_dose_bird_se_sm = trex_obj.out_eec_dose_bird_se_sm
    out_eec_dose_bird_se_md = trex_obj.out_eec_dose_bird_se_md
    out_eec_dose_bird_se_lg = trex_obj.out_eec_dose_bird_se_lg

    out_eec_dose_bird_sg_sm_exp = trex_obj.out_eec_dose_bird_sg_BL_sm_out_exp
    out_eec_dose_bird_sg_md_exp = trex_obj.out_eec_dose_bird_sg_BL_md_out_exp
    out_eec_dose_bird_sg_lg_exp = trex_obj.out_eec_dose_bird_sg_BL_lg_out_exp
    out_eec_dose_bird_tg_sm_exp = trex_obj.out_eec_dose_bird_tg_BL_sm_out_exp
    out_eec_dose_bird_tg_md_exp = trex_obj.out_eec_dose_bird_tg_BL_md_out_exp
    out_eec_dose_bird_tg_lg_exp = trex_obj.out_eec_dose_bird_tg_BL_lg_out_exp
    out_eec_dose_bird_bp_sm_exp = trex_obj.out_eec_dose_bird_bp_BL_sm_out_exp
    out_eec_dose_bird_bp_md_exp = trex_obj.out_eec_dose_bird_bp_BL_md_out_exp
    out_eec_dose_bird_bp_lg_exp = trex_obj.out_eec_dose_bird_bp_BL_lg_out_exp
    out_eec_dose_bird_fp_sm_exp = trex_obj.out_eec_dose_bird_fp_BL_sm_out_exp
    out_eec_dose_bird_fp_md_exp = trex_obj.out_eec_dose_bird_fp_BL_md_out_exp
    out_eec_dose_bird_fp_lg_exp = trex_obj.out_eec_dose_bird_fp_BL_lg_out_exp
    out_eec_dose_bird_ar_sm_exp = trex_obj.out_eec_dose_bird_ar_BL_sm_out_exp
    out_eec_dose_bird_ar_md_exp = trex_obj.out_eec_dose_bird_ar_BL_md_out_exp
    out_eec_dose_bird_ar_lg_exp = trex_obj.out_eec_dose_bird_ar_BL_lg_out_exp
    out_eec_dose_bird_se_sm_exp = trex_obj.out_eec_dose_bird_se_BL_sm_out_exp
    out_eec_dose_bird_se_md_exp = trex_obj.out_eec_dose_bird_se_BL_md_out_exp
    out_eec_dose_bird_se_lg_exp = trex_obj.out_eec_dose_bird_se_BL_lg_out_exp

    t7data_qaqc = gett7data_qaqc(out_eec_dose_bird_sg_sm, out_eec_dose_bird_sg_md, out_eec_dose_bird_sg_lg, out_eec_dose_bird_tg_sm,
                                 out_eec_dose_bird_tg_md, out_eec_dose_bird_tg_lg, out_eec_dose_bird_bp_sm, out_eec_dose_bird_bp_md,
                                 out_eec_dose_bird_bp_lg, out_eec_dose_bird_fp_sm, out_eec_dose_bird_fp_md, out_eec_dose_bird_fp_lg,
                                 out_eec_dose_bird_ar_sm, out_eec_dose_bird_ar_md, out_eec_dose_bird_ar_lg, out_eec_dose_bird_se_sm,
                                 out_eec_dose_bird_se_md, out_eec_dose_bird_se_lg,
                                 out_eec_dose_bird_sg_sm_exp, out_eec_dose_bird_sg_md_exp, out_eec_dose_bird_sg_lg_exp,
                                 out_eec_dose_bird_tg_sm_exp, out_eec_dose_bird_tg_md_exp, out_eec_dose_bird_tg_lg_exp,
                                 out_eec_dose_bird_bp_sm_exp, out_eec_dose_bird_bp_md_exp, out_eec_dose_bird_bp_lg_exp,
                                 out_eec_dose_bird_fp_sm_exp, out_eec_dose_bird_fp_md_exp, out_eec_dose_bird_fp_lg_exp,
                                 out_eec_dose_bird_ar_sm_exp, out_eec_dose_bird_ar_md_exp, out_eec_dose_bird_ar_lg_exp,
                                 out_eec_dose_bird_se_sm_exp, out_eec_dose_bird_se_md_exp, out_eec_dose_bird_se_lg_exp)
    t7rows_qaqc = gethtmlrowsfromcols(t7data_qaqc, pv7headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t7rows_qaqc, headings=pv7headings_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_7_add_qaqc(trex_obj):
    # pre-table 7
    html = """
            <H4 class="out_ collapsible" id="section8_add"><span></span>Avianr Dose Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 7_add
    out_arq_bird_sg_sm = trex_obj.out_arq_bird_sg_sm
    out_arq_bird_sg_md = trex_obj.out_arq_bird_sg_md
    out_arq_bird_sg_lg = trex_obj.out_arq_bird_sg_lg
    out_arq_bird_tg_sm = trex_obj.out_arq_bird_tg_sm
    out_arq_bird_tg_md = trex_obj.out_arq_bird_tg_md
    out_arq_bird_tg_lg = trex_obj.out_arq_bird_tg_lg
    out_arq_bird_bp_sm = trex_obj.out_arq_bird_bp_sm
    out_arq_bird_bp_md = trex_obj.out_arq_bird_bp_md
    out_arq_bird_bp_lg = trex_obj.out_arq_bird_bp_lg
    out_arq_bird_fp_sm = trex_obj.out_arq_bird_fp_sm
    out_arq_bird_fp_md = trex_obj.out_arq_bird_fp_md
    out_arq_bird_fp_lg = trex_obj.out_arq_bird_fp_lg
    out_arq_bird_ar_sm = trex_obj.out_arq_bird_ar_sm
    out_arq_bird_ar_md = trex_obj.out_arq_bird_ar_md
    out_arq_bird_ar_lg = trex_obj.out_arq_bird_ar_lg
    out_arq_bird_se_sm = trex_obj.out_arq_bird_se_sm
    out_arq_bird_se_md = trex_obj.out_arq_bird_se_md
    out_arq_bird_se_lg = trex_obj.out_arq_bird_se_lg

    out_arq_bird_sg_sm_exp = trex_obj.out_arq_bird_sg_BL_sm_out_exp
    out_arq_bird_sg_md_exp = trex_obj.out_arq_bird_sg_BL_md_out_exp
    out_arq_bird_sg_lg_exp = trex_obj.out_arq_bird_sg_BL_lg_out_exp
    out_arq_bird_tg_sm_exp = trex_obj.out_arq_bird_tg_BL_sm_out_exp
    out_arq_bird_tg_md_exp = trex_obj.out_arq_bird_tg_BL_md_out_exp
    out_arq_bird_tg_lg_exp = trex_obj.out_arq_bird_tg_BL_lg_out_exp
    out_arq_bird_bp_sm_exp = trex_obj.out_arq_bird_bp_BL_sm_out_exp
    out_arq_bird_bp_md_exp = trex_obj.out_arq_bird_bp_BL_md_out_exp
    out_arq_bird_bp_lg_exp = trex_obj.out_arq_bird_bp_BL_lg_out_exp
    out_arq_bird_fp_sm_exp = trex_obj.out_arq_bird_fp_BL_sm_out_exp
    out_arq_bird_fp_md_exp = trex_obj.out_arq_bird_fp_BL_md_out_exp
    out_arq_bird_fp_lg_exp = trex_obj.out_arq_bird_fp_BL_lg_out_exp
    out_arq_bird_ar_sm_exp = trex_obj.out_arq_bird_ar_BL_sm_out_exp
    out_arq_bird_ar_md_exp = trex_obj.out_arq_bird_ar_BL_md_out_exp
    out_arq_bird_ar_lg_exp = trex_obj.out_arq_bird_ar_BL_lg_out_exp
    out_arq_bird_se_sm_exp = trex_obj.out_arq_bird_se_BL_sm_out_exp
    out_arq_bird_se_md_exp = trex_obj.out_arq_bird_se_BL_md_out_exp
    out_arq_bird_se_lg_exp = trex_obj.out_arq_bird_se_BL_lg_out_exp

    t7_add_data_qaqc = gett7_add_data_qaqc(out_arq_bird_sg_sm, out_arq_bird_sg_md, out_arq_bird_sg_lg, out_arq_bird_tg_sm,
                                           out_arq_bird_tg_md, out_arq_bird_tg_lg, out_arq_bird_bp_sm, out_arq_bird_bp_md,
                                           out_arq_bird_bp_lg, out_arq_bird_fp_sm, out_arq_bird_fp_md, out_arq_bird_fp_lg,
                                           out_arq_bird_ar_sm, out_arq_bird_ar_md, out_arq_bird_ar_lg, out_arq_bird_se_sm,
                                           out_arq_bird_se_md, out_arq_bird_se_lg,
                                           out_arq_bird_sg_sm_exp, out_arq_bird_sg_md_exp, out_arq_bird_sg_lg_exp,
                                           out_arq_bird_tg_sm_exp, out_arq_bird_tg_md_exp, out_arq_bird_tg_lg_exp,
                                           out_arq_bird_bp_sm_exp, out_arq_bird_bp_md_exp, out_arq_bird_bp_lg_exp,
                                           out_arq_bird_fp_sm_exp, out_arq_bird_fp_md_exp, out_arq_bird_fp_lg_exp,
                                           out_arq_bird_ar_sm_exp, out_arq_bird_ar_md_exp, out_arq_bird_ar_lg_exp,
                                           out_arq_bird_se_sm_exp, out_arq_bird_se_md_exp, out_arq_bird_se_lg_exp)
    t7_add_rows_qaqc = gethtmlrowsfromcols(t7_add_data_qaqc, pv7headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t7_add_rows_qaqc, headings=pv7headings_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_8_qaqc(trex_obj):
    # pre-table 8 qaqc
    html = """
            <H4 class="out_ collapsible" id="section9"><span></span>Avian Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 8
    out_arq_diet_bird_sg_a = trex_obj.out_arq_diet_bird_sg_a
    out_arq_diet_bird_sg_c = trex_obj.out_arq_diet_bird_sg_c
    out_arq_diet_bird_tg_a = trex_obj.out_arq_diet_bird_tg_a
    out_arq_diet_bird_tg_c = trex_obj.out_arq_diet_bird_tg_c
    out_arq_diet_bird_bp_a = trex_obj.out_arq_diet_bird_bp_a
    out_arq_diet_bird_bp_c = trex_obj.out_arq_diet_bird_bp_c
    out_arq_diet_bird_fp_a = trex_obj.out_arq_diet_bird_fp_a
    out_arq_diet_bird_fp_c = trex_obj.out_arq_diet_bird_fp_c
    out_arq_diet_bird_ar_a = trex_obj.out_arq_diet_bird_ar_a
    out_arq_diet_bird_ar_c = trex_obj.out_arq_diet_bird_ar_c

    out_arq_diet_bird_sg_a_exp = trex_obj.out_arq_diet_bird_sg_a_BL_out_exp
    out_arq_diet_bird_sg_c_exp = trex_obj.out_arq_diet_bird_sg_c_BL_out_exp
    out_arq_diet_bird_tg_a_exp = trex_obj.out_arq_diet_bird_tg_a_BL_out_exp
    out_arq_diet_bird_tg_c_exp = trex_obj.out_arq_diet_bird_tg_c_BL_out_exp
    out_arq_diet_bird_bp_a_exp = trex_obj.out_arq_diet_bird_bp_a_BL_out_exp
    out_arq_diet_bird_bp_c_exp = trex_obj.out_arq_diet_bird_bp_c_BL_out_exp
    out_arq_diet_bird_fp_a_exp = trex_obj.out_arq_diet_bird_fp_a_BL_out_exp
    out_arq_diet_bird_fp_c_exp = trex_obj.out_arq_diet_bird_fp_c_BL_out_exp
    out_arq_diet_bird_ar_a_exp = trex_obj.out_arq_diet_bird_ar_a_BL_out_exp
    out_arq_diet_bird_ar_c_exp = trex_obj.out_arq_diet_bird_ar_c_BL_out_exp

    t8data_qaqc = gett8data_qaqc(out_arq_diet_bird_sg_a, out_arq_diet_bird_sg_c, out_arq_diet_bird_tg_a, out_arq_diet_bird_tg_c,
                                 out_arq_diet_bird_bp_a, out_arq_diet_bird_bp_c, out_arq_diet_bird_fp_a, out_arq_diet_bird_fp_c,
                                 out_arq_diet_bird_ar_a, out_arq_diet_bird_ar_c,
                                 out_arq_diet_bird_sg_a_exp, out_arq_diet_bird_sg_c_exp, out_arq_diet_bird_tg_a_exp,
                                 out_arq_diet_bird_tg_c_exp, out_arq_diet_bird_bp_a_exp, out_arq_diet_bird_bp_c_exp,
                                 out_arq_diet_bird_fp_a_exp, out_arq_diet_bird_fp_c_exp, out_arq_diet_bird_ar_a_exp,
                                 out_arq_diet_bird_ar_c_exp)
    t8rows_qaqc = gethtmlrowsfromcols(t8data_qaqc, pv8headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t8rows_qaqc, headings=pv8headings_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_9_qaqc(trex_obj):
    # pre-table 9_qaqc
    html = """
            <H4 class="out_ collapsible" id="section10"><span></span>Mammalian Dose Based EECs (mg/kg-bw)</H4>
                <div class="out_ container_output">
        """
    # table 9_qaqc
    out_eec_dose_mamm_sg_sm = trex_obj.out_eec_dose_mamm_sg_sm
    out_eec_dose_mamm_sg_md = trex_obj.out_eec_dose_mamm_sg_md
    out_eec_dose_mamm_sg_lg = trex_obj.out_eec_dose_mamm_sg_lg
    out_eec_dose_mamm_tg_sm = trex_obj.out_eec_dose_mamm_tg_sm
    out_eec_dose_mamm_tg_md = trex_obj.out_eec_dose_mamm_tg_md
    out_eec_dose_mamm_tg_lg = trex_obj.out_eec_dose_mamm_tg_lg
    out_eec_dose_mamm_bp_sm = trex_obj.out_eec_dose_mamm_bp_sm
    out_eec_dose_mamm_bp_md = trex_obj.out_eec_dose_mamm_bp_md
    out_eec_dose_mamm_bp_lg = trex_obj.out_eec_dose_mamm_bp_lg
    out_eec_dose_mamm_fp_sm = trex_obj.out_eec_dose_mamm_fp_sm
    out_eec_dose_mamm_fp_md = trex_obj.out_eec_dose_mamm_fp_md
    out_eec_dose_mamm_fp_lg = trex_obj.out_eec_dose_mamm_fp_lg
    out_eec_dose_mamm_ar_sm = trex_obj.out_eec_dose_mamm_ar_sm
    out_eec_dose_mamm_ar_md = trex_obj.out_eec_dose_mamm_ar_md
    out_eec_dose_mamm_ar_lg = trex_obj.out_eec_dose_mamm_ar_lg
    out_eec_dose_mamm_se_sm = trex_obj.out_eec_dose_mamm_se_sm
    out_eec_dose_mamm_se_md = trex_obj.out_eec_dose_mamm_se_md
    out_eec_dose_mamm_se_lg = trex_obj.out_eec_dose_mamm_se_lg

    out_eec_dose_mamm_sg_sm_exp = trex_obj.out_eec_dose_mamm_sg_sm_BL_out_exp
    out_eec_dose_mamm_sg_md_exp = trex_obj.out_eec_dose_mamm_sg_md_BL_out_exp
    out_eec_dose_mamm_sg_lg_exp = trex_obj.out_eec_dose_mamm_sg_lg_BL_out_exp
    out_eec_dose_mamm_tg_sm_exp = trex_obj.out_eec_dose_mamm_tg_sm_BL_out_exp
    out_eec_dose_mamm_tg_md_exp = trex_obj.out_eec_dose_mamm_tg_md_BL_out_exp
    out_eec_dose_mamm_tg_lg_exp = trex_obj.out_eec_dose_mamm_tg_lg_BL_out_exp
    out_eec_dose_mamm_bp_sm_exp = trex_obj.out_eec_dose_mamm_bp_sm_BL_out_exp
    out_eec_dose_mamm_bp_md_exp = trex_obj.out_eec_dose_mamm_bp_md_BL_out_exp
    out_eec_dose_mamm_bp_lg_exp = trex_obj.out_eec_dose_mamm_bp_lg_BL_out_exp
    out_eec_dose_mamm_fp_sm_exp = trex_obj.out_eec_dose_mamm_fp_sm_BL_out_exp
    out_eec_dose_mamm_fp_md_exp = trex_obj.out_eec_dose_mamm_fp_md_BL_out_exp
    out_eec_dose_mamm_fp_lg_exp = trex_obj.out_eec_dose_mamm_fp_lg_BL_out_exp
    out_eec_dose_mamm_ar_sm_exp = trex_obj.out_eec_dose_mamm_ar_sm_BL_out_exp
    out_eec_dose_mamm_ar_md_exp = trex_obj.out_eec_dose_mamm_ar_md_BL_out_exp
    out_eec_dose_mamm_ar_lg_exp = trex_obj.out_eec_dose_mamm_ar_lg_BL_out_exp
    out_eec_dose_mamm_se_sm_exp = trex_obj.out_eec_dose_mamm_se_sm_BL_out_exp
    out_eec_dose_mamm_se_md_exp = trex_obj.out_eec_dose_mamm_se_md_BL_out_exp
    out_eec_dose_mamm_se_lg_exp = trex_obj.out_eec_dose_mamm_se_lg_BL_out_exp

    t9data_qaqc = gett9data_qaqc(out_eec_dose_mamm_sg_sm, out_eec_dose_mamm_sg_md, out_eec_dose_mamm_sg_lg, out_eec_dose_mamm_tg_sm,
                                 out_eec_dose_mamm_tg_md, out_eec_dose_mamm_tg_lg, out_eec_dose_mamm_bp_sm, out_eec_dose_mamm_bp_md,
                                 out_eec_dose_mamm_bp_lg, out_eec_dose_mamm_fp_sm, out_eec_dose_mamm_fp_md, out_eec_dose_mamm_fp_lg,
                                 out_eec_dose_mamm_ar_sm, out_eec_dose_mamm_ar_md, out_eec_dose_mamm_ar_lg, out_eec_dose_mamm_se_sm,
                                 out_eec_dose_mamm_se_md, out_eec_dose_mamm_se_lg,
                                 out_eec_dose_mamm_sg_sm_exp, out_eec_dose_mamm_sg_md_exp, out_eec_dose_mamm_sg_lg_exp,
                                 out_eec_dose_mamm_tg_sm_exp, out_eec_dose_mamm_tg_md_exp, out_eec_dose_mamm_tg_lg_exp,
                                 out_eec_dose_mamm_bp_sm_exp, out_eec_dose_mamm_bp_md_exp, out_eec_dose_mamm_bp_lg_exp,
                                 out_eec_dose_mamm_fp_sm_exp, out_eec_dose_mamm_fp_md_exp, out_eec_dose_mamm_fp_lg_exp,
                                 out_eec_dose_mamm_ar_sm_exp, out_eec_dose_mamm_ar_md_exp, out_eec_dose_mamm_ar_lg_exp,
                                 out_eec_dose_mamm_se_sm_exp, out_eec_dose_mamm_se_md_exp, out_eec_dose_mamm_se_lg_exp)
    t9rows_qaqc = gethtmlrowsfromcols(t9data_qaqc, pv7headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t9rows_qaqc, headings=pv7headings_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_10_qaqc(trex_obj):
    # pre-table 10_qaqc
    html = """
            <H4 class="out_ collapsible" id="section11"><span></span>Mammalian Dose Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 10_qaqc
    out_arq_dose_mamm_sg_sm = trex_obj.out_arq_dose_mamm_sg_sm
    out_crq_dose_mamm_sg_sm = trex_obj.out_crq_dose_mamm_sg_sm
    out_arq_dose_mamm_sg_md = trex_obj.out_arq_dose_mamm_sg_md
    out_crq_dose_mamm_sg_md = trex_obj.out_crq_dose_mamm_sg_md
    out_arq_dose_mamm_sg_lg = trex_obj.out_arq_dose_mamm_sg_lg
    out_crq_dose_mamm_sg_lg = trex_obj.out_crq_dose_mamm_sg_lg

    out_arq_dose_mamm_tg_sm = trex_obj.out_arq_dose_mamm_tg_sm
    out_crq_dose_mamm_tg_sm = trex_obj.out_crq_dose_mamm_tg_sm
    out_arq_dose_mamm_tg_md = trex_obj.out_arq_dose_mamm_tg_md
    out_crq_dose_mamm_tg_md = trex_obj.out_crq_dose_mamm_tg_md
    out_arq_dose_mamm_tg_lg = trex_obj.out_arq_dose_mamm_tg_lg
    out_crq_dose_mamm_tg_lg = trex_obj.out_crq_dose_mamm_tg_lg

    out_arq_dose_mamm_bp_sm = trex_obj.out_arq_dose_mamm_bp_sm
    out_crq_dose_mamm_bp_sm = trex_obj.out_crq_dose_mamm_bp_sm
    out_arq_dose_mamm_bp_md = trex_obj.out_arq_dose_mamm_bp_md
    out_crq_dose_mamm_bp_md = trex_obj.out_crq_dose_mamm_bp_md
    out_arq_dose_mamm_bp_lg = trex_obj.out_arq_dose_mamm_bp_lg
    out_crq_dose_mamm_bp_lg = trex_obj.out_crq_dose_mamm_bp_lg

    out_arq_dose_mamm_fp_sm = trex_obj.out_arq_dose_mamm_fp_sm
    out_crq_dose_mamm_fp_sm = trex_obj.out_crq_dose_mamm_fp_sm
    out_arq_dose_mamm_fp_md = trex_obj.out_arq_dose_mamm_fp_md
    out_crq_dose_mamm_fp_md = trex_obj.out_crq_dose_mamm_fp_md
    out_arq_dose_mamm_fp_lg = trex_obj.out_arq_dose_mamm_fp_lg
    out_crq_dose_mamm_fp_lg = trex_obj.out_crq_dose_mamm_fp_lg

    out_arq_dose_mamm_ar_sm = trex_obj.out_arq_dose_mamm_ar_sm
    out_crq_dose_mamm_ar_sm = trex_obj.out_crq_dose_mamm_ar_sm
    out_arq_dose_mamm_ar_md = trex_obj.out_arq_dose_mamm_ar_md
    out_crq_dose_mamm_ar_md = trex_obj.out_crq_dose_mamm_ar_md
    out_arq_dose_mamm_ar_lg = trex_obj.out_arq_dose_mamm_ar_lg
    out_crq_dose_mamm_ar_lg = trex_obj.out_crq_dose_mamm_ar_lg

    out_arq_dose_mamm_se_sm = trex_obj.out_arq_dose_mamm_se_sm
    out_crq_dose_mamm_se_sm = trex_obj.out_crq_dose_mamm_se_sm
    out_arq_dose_mamm_se_md = trex_obj.out_arq_dose_mamm_se_md
    out_crq_dose_mamm_se_md = trex_obj.out_crq_dose_mamm_se_md
    out_arq_dose_mamm_se_lg = trex_obj.out_arq_dose_mamm_se_lg
    out_crq_dose_mamm_se_lg = trex_obj.out_crq_dose_mamm_se_lg

    #########
    out_arq_dose_mamm_sg_sm_exp = trex_obj.out_arq_dose_mamm_sg_sm_BL_out_exp
    out_crq_dose_mamm_sg_sm_exp = trex_obj.out_crq_dose_mamm_sg_sm_BL_out_exp
    out_arq_dose_mamm_sg_md_exp = trex_obj.out_arq_dose_mamm_sg_md_BL_out_exp
    out_crq_dose_mamm_sg_md_exp = trex_obj.out_crq_dose_mamm_sg_md_BL_out_exp
    out_arq_dose_mamm_sg_lg_exp = trex_obj.out_arq_dose_mamm_sg_lg_BL_out_exp
    out_crq_dose_mamm_sg_lg_exp = trex_obj.out_crq_dose_mamm_sg_lg_BL_out_exp

    out_arq_dose_mamm_tg_sm_exp = trex_obj.out_arq_dose_mamm_tg_sm_BL_out_exp
    out_crq_dose_mamm_tg_sm_exp = trex_obj.out_crq_dose_mamm_tg_sm_BL_out_exp
    out_arq_dose_mamm_tg_md_exp = trex_obj.out_arq_dose_mamm_tg_md_BL_out_exp
    out_crq_dose_mamm_tg_md_exp = trex_obj.out_crq_dose_mamm_tg_md_BL_out_exp
    out_arq_dose_mamm_tg_lg_exp = trex_obj.out_arq_dose_mamm_tg_lg_BL_out_exp
    out_crq_dose_mamm_tg_lg_exp = trex_obj.out_crq_dose_mamm_tg_lg_BL_out_exp

    out_arq_dose_mamm_bp_sm_exp = trex_obj.out_arq_dose_mamm_bp_sm_BL_out_exp
    out_crq_dose_mamm_bp_sm_exp = trex_obj.out_crq_dose_mamm_bp_sm_BL_out_exp
    out_arq_dose_mamm_bp_md_exp = trex_obj.out_arq_dose_mamm_bp_md_BL_out_exp
    out_crq_dose_mamm_bp_md_exp = trex_obj.out_crq_dose_mamm_bp_md_BL_out_exp
    out_arq_dose_mamm_bp_lg_exp = trex_obj.out_arq_dose_mamm_bp_lg_BL_out_exp
    out_crq_dose_mamm_bp_lg_exp = trex_obj.out_crq_dose_mamm_bp_lg_BL_out_exp

    out_arq_dose_mamm_fp_sm_exp = trex_obj.out_arq_dose_mamm_fp_sm_BL_out_exp
    out_crq_dose_mamm_fp_sm_exp = trex_obj.out_crq_dose_mamm_fp_sm_BL_out_exp
    out_arq_dose_mamm_fp_md_exp = trex_obj.out_arq_dose_mamm_fp_md_BL_out_exp
    out_crq_dose_mamm_fp_md_exp = trex_obj.out_crq_dose_mamm_fp_md_BL_out_exp
    out_arq_dose_mamm_fp_lg_exp = trex_obj.out_arq_dose_mamm_fp_lg_BL_out_exp
    out_crq_dose_mamm_fp_lg_exp = trex_obj.out_crq_dose_mamm_fp_lg_BL_out_exp

    out_arq_dose_mamm_ar_sm_exp = trex_obj.out_arq_dose_mamm_ar_sm_BL_out_exp
    out_crq_dose_mamm_ar_sm_exp = trex_obj.out_crq_dose_mamm_ar_sm_BL_out_exp
    out_arq_dose_mamm_ar_md_exp = trex_obj.out_arq_dose_mamm_ar_md_BL_out_exp
    out_crq_dose_mamm_ar_md_exp = trex_obj.out_crq_dose_mamm_ar_md_BL_out_exp
    out_arq_dose_mamm_ar_lg_exp = trex_obj.out_arq_dose_mamm_ar_lg_BL_out_exp
    out_crq_dose_mamm_ar_lg_exp = trex_obj.out_crq_dose_mamm_ar_lg_BL_out_exp

    out_arq_dose_mamm_se_sm_exp = trex_obj.out_arq_dose_mamm_se_sm_BL_out_exp
    out_crq_dose_mamm_se_sm_exp = trex_obj.out_crq_dose_mamm_se_sm_BL_out_exp
    out_arq_dose_mamm_se_md_exp = trex_obj.out_arq_dose_mamm_se_md_BL_out_exp
    out_crq_dose_mamm_se_md_exp = trex_obj.out_crq_dose_mamm_se_md_BL_out_exp
    out_arq_dose_mamm_se_lg_exp = trex_obj.out_arq_dose_mamm_se_lg_BL_out_exp
    out_crq_dose_mamm_se_lg_exp = trex_obj.out_crq_dose_mamm_se_lg_BL_out_exp

    t10data_qaqc = gett10data_qaqc(out_arq_dose_mamm_sg_sm, out_crq_dose_mamm_sg_sm, out_arq_dose_mamm_sg_md, out_crq_dose_mamm_sg_md,
                                   out_arq_dose_mamm_sg_lg, out_crq_dose_mamm_sg_lg, out_arq_dose_mamm_tg_sm, out_crq_dose_mamm_tg_sm,
                                   out_arq_dose_mamm_tg_md, out_crq_dose_mamm_tg_md, out_arq_dose_mamm_tg_lg, out_crq_dose_mamm_tg_lg,
                                   out_arq_dose_mamm_bp_sm, out_crq_dose_mamm_bp_sm, out_arq_dose_mamm_bp_md, out_crq_dose_mamm_bp_md,
                                   out_arq_dose_mamm_bp_lg, out_crq_dose_mamm_bp_lg, out_arq_dose_mamm_fp_sm, out_crq_dose_mamm_fp_sm,
                                   out_arq_dose_mamm_fp_md, out_crq_dose_mamm_fp_md, out_arq_dose_mamm_fp_lg, out_crq_dose_mamm_fp_lg,
                                   out_arq_dose_mamm_ar_sm, out_crq_dose_mamm_ar_sm, out_arq_dose_mamm_ar_md, out_crq_dose_mamm_ar_md,
                                   out_arq_dose_mamm_ar_lg, out_crq_dose_mamm_ar_lg, out_arq_dose_mamm_se_sm, out_crq_dose_mamm_se_sm,
                                   out_arq_dose_mamm_se_md, out_crq_dose_mamm_se_md, out_arq_dose_mamm_se_lg, out_crq_dose_mamm_se_lg,
                                   out_arq_dose_mamm_sg_sm_exp, out_crq_dose_mamm_sg_sm_exp, out_arq_dose_mamm_sg_md_exp,
                                   out_crq_dose_mamm_sg_md_exp, out_arq_dose_mamm_sg_lg_exp, out_crq_dose_mamm_sg_lg_exp,
                                   out_arq_dose_mamm_tg_sm_exp, out_crq_dose_mamm_tg_sm_exp, out_arq_dose_mamm_tg_md_exp,
                                   out_crq_dose_mamm_tg_md_exp, out_arq_dose_mamm_tg_lg_exp, out_crq_dose_mamm_tg_lg_exp,
                                   out_arq_dose_mamm_bp_sm_exp, out_crq_dose_mamm_bp_sm_exp, out_arq_dose_mamm_bp_md_exp,
                                   out_crq_dose_mamm_bp_md_exp, out_arq_dose_mamm_bp_lg_exp, out_crq_dose_mamm_bp_lg_exp,
                                   out_arq_dose_mamm_fp_sm_exp, out_crq_dose_mamm_fp_sm_exp, out_arq_dose_mamm_fp_md_exp,
                                   out_crq_dose_mamm_fp_md_exp, out_arq_dose_mamm_fp_lg_exp, out_crq_dose_mamm_fp_lg_exp,
                                   out_arq_dose_mamm_ar_sm_exp, out_crq_dose_mamm_ar_sm_exp, out_arq_dose_mamm_ar_md_exp,
                                   out_crq_dose_mamm_ar_md_exp, out_arq_dose_mamm_ar_lg_exp, out_crq_dose_mamm_ar_lg_exp,
                                   out_arq_dose_mamm_se_sm_exp, out_crq_dose_mamm_se_sm_exp, out_arq_dose_mamm_se_md_exp,
                                   out_crq_dose_mamm_se_md_exp, out_arq_dose_mamm_se_lg_exp, out_crq_dose_mamm_se_lg_exp)
    t10rows_qaqc = gethtmlrowsfromcols(t10data_qaqc, pv10headings_qaqc)
    html = html + tmpl_10_qaqc.render(Context(dict(data=t10rows_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_11_qaqc(trex_obj):
    # pre-table 11_qaqc
    html = """
            <H4 class="out_ collapsible" id="section12"><span></span>Mammalian Dietary Based RQs</H4>
                <div class="out_ container_output">
        """
    # table 11_qaqc
    out_arq_diet_mamm_sg = trex_obj.out_arq_diet_mamm_sg
    out_crq_diet_mamm_sg = trex_obj.out_crq_diet_mamm_sg
    out_arq_diet_mamm_tg = trex_obj.out_arq_diet_mamm_tg
    out_crq_diet_mamm_tg = trex_obj.out_crq_diet_mamm_tg
    out_arq_diet_mamm_bp = trex_obj.out_arq_diet_mamm_bp
    out_crq_diet_mamm_bp = trex_obj.out_crq_diet_mamm_bp
    out_arq_diet_mamm_fp = trex_obj.out_arq_diet_mamm_fp
    out_crq_diet_mamm_fp = trex_obj.out_crq_diet_mamm_fp
    out_arq_diet_mamm_ar = trex_obj.out_arq_diet_mamm_ar
    out_crq_diet_mamm_ar = trex_obj.out_crq_diet_mamm_ar

    out_arq_diet_mamm_sg_exp = trex_obj.out_arq_diet_mamm_sg_BL_out_exp
    out_crq_diet_mamm_sg_exp = trex_obj.out_crq_diet_mamm_sg_BL_out_exp
    out_arq_diet_mamm_tg_exp = trex_obj.out_arq_diet_mamm_tg_BL_out_exp
    out_crq_diet_mamm_tg_exp = trex_obj.out_crq_diet_mamm_tg_BL_out_exp
    out_arq_diet_mamm_bp_exp = trex_obj.out_arq_diet_mamm_bp_BL_out_exp
    out_crq_diet_mamm_bp_exp = trex_obj.out_crq_diet_mamm_bp_BL_out_exp
    out_arq_diet_mamm_fp_exp = trex_obj.out_arq_diet_mamm_fp_BL_out_exp
    out_crq_diet_mamm_fp_exp = trex_obj.out_crq_diet_mamm_fp_BL_out_exp
    out_arq_diet_mamm_ar_exp = trex_obj.out_arq_diet_mamm_ar_BL_out_exp
    out_crq_diet_mamm_ar_exp = trex_obj.out_crq_diet_mamm_ar_BL_out_exp

    t11data_qaqc = gett11data_na_qaqc(out_arq_diet_mamm_sg, out_crq_diet_mamm_sg, out_arq_diet_mamm_tg, out_crq_diet_mamm_tg,
                                      out_arq_diet_mamm_bp, out_crq_diet_mamm_bp, out_arq_diet_mamm_fp, out_crq_diet_mamm_fp,
                                      out_arq_diet_mamm_ar, out_crq_diet_mamm_ar,
                                      out_arq_diet_mamm_sg_exp, out_crq_diet_mamm_sg_exp, out_arq_diet_mamm_tg_exp,
                                      out_crq_diet_mamm_tg_exp, out_arq_diet_mamm_bp_exp, out_crq_diet_mamm_bp_exp,
                                      out_arq_diet_mamm_fp_exp, out_crq_diet_mamm_fp_exp, out_arq_diet_mamm_ar_exp,
                                      out_crq_diet_mamm_ar_exp)
    t11rows_qaqc = gethtmlrowsfromcols(t11data_qaqc, pv8headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t11rows_qaqc, headings=pv8headings_qaqc)))
    html = html + """
                </div>
        """
    return html


def table_15_qaqc(trex_obj):
    # pre-table 15_qaqc
    html = """
            <H4 class="out_ collapsible" id="section13"><span></span>LD<sub>50</sub> ft<sup>-2</sup></H4>
                <div class="out_ container_output">
        """
    # table 15_qaqc
    out_ld50_bl_bird_sm = trex_obj.out_ld50_bl_bird_sm
    out_ld50_bl_mamm_sm = trex_obj.out_ld50_bl_mamm_sm
    out_ld50_bl_bird_md = trex_obj.out_ld50_bl_bird_md
    out_ld50_bl_mamm_md = trex_obj.out_ld50_bl_mamm_md
    out_ld50_bl_bird_lg = trex_obj.out_ld50_bl_bird_lg
    out_ld50_bl_mamm_lg = trex_obj.out_ld50_bl_mamm_lg

    out_ld50_bl_bird_sm_exp = trex_obj.out_ld50_bl_bird_sm
    out_ld50_bl_mamm_sm_exp = trex_obj.out_ld50_bl_mamm_sm
    out_ld50_bl_bird_md_exp = trex_obj.out_ld50_bl_bird_md
    out_ld50_bl_mamm_md_exp = trex_obj.out_ld50_bl_mamm_md
    out_ld50_bl_bird_lg_exp = trex_obj.out_ld50_bl_bird_lg
    out_ld50_bl_mamm_lg_exp = trex_obj.out_ld50_bl_mamm_lg

    t15data_qaqc = gett12data_qaqc(out_ld50_bl_bird_sm, out_ld50_bl_mamm_sm, out_ld50_bl_bird_md, out_ld50_bl_mamm_md, out_ld50_bl_bird_lg,
                                   out_ld50_bl_mamm_lg,
                                   out_ld50_bl_bird_sm_exp, out_ld50_bl_mamm_sm_exp, out_ld50_bl_bird_md_exp, out_ld50_bl_mamm_md_exp,
                                   out_ld50_bl_bird_lg_exp, out_ld50_bl_mamm_lg_exp)
    t15rows_qaqc = gethtmlrowsfromcols(t15data_qaqc, pv12headings_qaqc)
    html = html + tmpl.render(Context(dict(data=t15rows_qaqc, headings=pv12headings_qaqc)))
    html = html + """
                </div>
        </div>
        """
    return html
