"""
.. module:: pfam_tables
   :synopsis: A useful module indeed.
"""

import datetime
import logging

from django.template import Context, Template
from django.utils.safestring import mark_safe

logger = logging.getLogger("PFAM Tables")


def getheaderpvu():
  headings = ["Parameter", "Value", "Units"]
  return headings

def getheaderpvuqaqc():
    headings = ["Parameter", "Value", "Expected Value", "Units"]
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

def gett1data(pfam_obj):
    data = { 
        "Parameter": [mark_safe('Water Column Half life @%s &#8451;') %pfam_obj.wat_t, mark_safe('Benthic Compartment Half Life @%s &#8451;') %pfam_obj.ben_t, mark_safe('Unflooded Soil Half Life @%s &#8451;') %pfam_obj.unf_t, 'Aqueous Near-Surface Photolysis Half Life @%s Degrees Latitude' %pfam_obj.aqu_t,
                      'Hydrolysis Half Life', 'Molecular Weight', 'Vapor Pressure', 'Solubility', 'Koc', 'Heat of Henry', 'Henry Reference Temperature'],
        "Value": ['%s' % pfam_obj.wat_hl, pfam_obj.ben_hl, '%s' % pfam_obj.unf_hl, '%s' % pfam_obj.aqu_hl,
                  '%s' % pfam_obj.hyd_hl, '%s' % pfam_obj.mw, '%s' % pfam_obj.vp, '%s' % pfam_obj.sol, '%s' % pfam_obj.koc, '%s' % pfam_obj.hea_h, '%s' % pfam_obj.hea_r_t],
        "Units": ['days', 'days', 'days', 'days', 'days', 'g/mol', 'torr', 'mg/l', 'ml/g', 'J/mol', mark_safe('&#8451;')],
    }
    return data


pvuheadings = getheaderpvu()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_all(pfam_obj):
    table1_out = table_1(pfam_obj)
    table2_out = table_2(pfam_obj)
    table3_out = table_3(pfam_obj)
    table4_out = table_4(pfam_obj)
    table5_out = table_5(pfam_obj)
    table6_out = table_6(pfam_obj)
    table7_out = table_7(pfam_obj)
    table8_out = table_8(pfam_obj)
    table9_out = table_9(pfam_obj)
    html_all = table1_out + table2_out + table3_out + table4_out + table5_out + table6_out + table7_out + table8_out + table9_out
    return html_all

def timestamp(pfam_obj):
    st = datetime.datetime.strptime(pfam_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A %Y-%m-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>PFAM<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def table_1(pfam_obj):
    html = """
    <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
    <div class="out_">
        <H4 class="out_1 collapsible" id="section1"><span></span>Chemical Properties</H4>
            <div class="out_ container_output">
    """
    t1data = gett1data(pfam_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
            </div>
    """
    return html

def table_2(pfam_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Application Inputs</H4>
            <div class="out_ container_output">
              <table class="out_application_pre" width="604">
                <tr>
                  <td width="50%%">Number of Applications</td>
                  <td id="noa_out" width="50%%">%s</td>
                </tr>
              </table>
              <table class="out_application" width="604">
                <tr>
                  <th scope="col" width="50">App#</th>
                  <th scope="col" width="125">Month</th>                            
                  <th scope="col" width="125">Day</th>
                  <th scope="col" width="125">Mass Applied (kg/hA)</th>
                  <th scope="col" width="125">Slow Release (1/day)</th>
                </tr>
                <tr>
                  <td id="mm_out" data-val='%s' style="display: none"></td>  
                  <td id="dd_out" data-val='%s' style="display: none"></td>  
                  <td id="ma_out" data-val='%s' style="display: none"></td>  
                  <td id="sr_out" data-val='%s' style="display: none"></td>  
                </tr>                               
              </table>
            </div>
       """%(pfam_obj.noa, pfam_obj.mm_out, pfam_obj.dd_out, pfam_obj.ma_out, pfam_obj.sr_out)
    return html

def table_3(pfam_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Location Inputs</H4>
            <div class="out_ container_output">
              <table class="out_location">
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Unit</th>                            
                  <th scope="col">Value</th>
                </tr>                            
                <tr>
                  <td>Weather File</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>                          
                <tr>
                  <td>Latitude (for Photolysis Calculations)</td>
                  <td>degree</td>                            
                  <td>%s</td>
                </tr>                           
              </table>
            </div>
    """%(pfam_obj.weather, pfam_obj.wea_l)    
    return html

def table_4(pfam_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Flood Inputs</H4>
            <div class="out_ container_output">
              <table class="out_floods_pre">
                <tr>
                  <th scope="col">Number of Events</th>
                  <th scope="col">Unit</th>                            
                  <th scope="col">Value</th>
                </tr>                            
                <tr>
                  <td>Number of Events</td>
                  <td></td>
                  <td id="nof_out">%s</td>
                </tr>
                <tr>
                  <td>Date for Event 1</td>
                  <td></td>
                  <td id="noa_out">%s</td>
                </tr>
              </table>
              <table class="out_floods">
                <tr>
                  <th scope="col">Event#</th>
                  <th scope="col">Number of days</th>                            
                  <th scope="col">Fill Level (m)</th>
                  <th scope="col">Wier Level (m)</th>
                  <th scope="col">Min. Level (m)</th>
                  <th scope="col">Turn Over (1/day)</th>                            
                </tr>
                <tr>          
                  <td id="nod_out" data-val='%s' style="display: none"></td>  
                  <td id="fl_out" data-val='%s' style="display: none"></td>  
                  <td id="wl_out" data-val='%s' style="display: none"></td>  
                  <td id="ml_out" data-val='%s' style="display: none"></td>
                  <td id="to_out" data-val='%s' style="display: none"></td>  
                </tr>                               
              </table>
            </div>
      """%(pfam_obj.nof, pfam_obj.date_f1, pfam_obj.nod_out, pfam_obj.fl_out, 
                        pfam_obj.wl_out, pfam_obj.ml_out, pfam_obj.to_out)
    return html

def table_5(pfam_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Crop Inputs</H4>
            <div class="out_ container_output">
              <table class="out_location">
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Unit</th>                            
                  <th scope="col">Value</th>
                </tr>                            
                <tr>
                  <td>Zero Height Reference</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>                          
                <tr>
                  <td>Days from Zero Height to Full Height</td>
                  <td>days</td>                            
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Days from Zero Height to Removal</td>
                  <td>days</td>                            
                  <td>%s</td>
                </tr> 
                <tr>
                  <td>Maximum Fractional Area Coverage</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>                                                                                    
              </table>
            </div>
    """%(pfam_obj.zero_height_ref, pfam_obj.days_zero_full, pfam_obj.days_zero_removal, pfam_obj.max_frac_cov)       
    return html

def table_6(pfam_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Physical Inputs</H4>
            <div class="out_ container_output">
              <table class="out_physical">
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Unit</th>                            
                  <th scope="col">Value</th>
                </tr>                            
                <tr>
                  <td>Mass Transfer Coefficient</td>
                  <td>m</td>                            
                  <td>%s</td>
                </tr>                          
                <tr>
                  <td>Leakage</td>
                  <td>m/d</td>                            
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Reference Depth</td>
                  <td>m</td>                            
                  <td>%s</td>
                </tr> 
                <tr>
                  <td>Benthic Depth</td>
                  <td>m</td>                            
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Benthic Porosity</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>   
                <tr>
                  <td>Dry Bulk Density</td>
                  <td>g/cm<sup>3</sup></td>                            
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Foc Water Column on SS</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>  
                <tr>
                  <td>Foc Benthic</td>
                  <td></td>                            
                  <td>%s</td>
                </tr> 
                <tr>
                  <td>SS</td>
                  <td>mg/L</td>                            
                  <td>%s</td>
                </tr> 
                <tr>
                  <td>Water column DOC</td>
                  <td>mg/L</td>                            
                  <td>%s</td>
                </tr> 
                <tr>
                  <td>Chlorophyll, CHL</td>
                  <td>mg/L</td>                            
                  <td>%s</td>
                </tr> 
                <tr>
                  <td>Dfac</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Q10</td>
                  <td></td>                            
                  <td>%s</td>
                </tr>
              </table>
            </div>
    """%(pfam_obj.mas_tras_cof, pfam_obj.leak, pfam_obj.ref_d, pfam_obj.ben_d, 
         pfam_obj.ben_por, pfam_obj.dry_bkd, pfam_obj.foc_wat, pfam_obj.foc_ben, 
         pfam_obj.ss, pfam_obj.wat_c_doc, pfam_obj.chl, pfam_obj.dfac, pfam_obj.q10)   
    return html

def table_7(pfam_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Area of Application</H4>
            <div class="out_ container_output">
              <table class="out_output">
                <tr>
                  <th scope="col">Variable</th>
                  <th scope="col">Unit</th>                            
                  <th scope="col">Value</th>
                </tr>
                <tr>             
                  <td scope="col">Area of Application</td>
                  <td scope="col">m<sup>2</sup></td>                            
                  <td scope="col">%s</td>
                </tr>
              </table>
            </div>
        </div>
    """%(pfam_obj.area_app)   
    return html

def table_8(pfam_obj):
    html = """
    <br>
    <H3 class="out_1 collapsible" id="section1"><span></span>PFAM Results</H3>
    <div class="out_">
            <div class="out_ container_output">
              <table class="results">
                <tr>
                  <th>Simulation is finished. Please download your file from here</th>
                  <th><a href=%s>Link</a></th>
                </tr>
                <tr style="display: none">
                  <td id="x_date1" data-val='%s'></td>
                  <td id="x_re_v_f" data-val='%s'></td>
                  <td id="x_re_c_f" data-val='%s'></td>
                  <td id="x_date2" data-val='%s'></td>
                  <td id="x_water" data-val='%s'></td>
                  <td id="x_water_level" data-val='%s'></td>
                  <td id="x_ben_tot" data-val='%s'></td>
                  <td id="x_ben_por" data-val='%s'></td>
                </tr>
              </table>
            </div>
      """%(pfam_obj.link, pfam_obj.x_date1, pfam_obj.x_re_v_f, pfam_obj.x_re_c_f, 
           pfam_obj.x_date2, pfam_obj.x_water, pfam_obj.x_water_level, pfam_obj.x_ben_tot, pfam_obj.x_ben_por)  
    return html

def table_9(pfam_obj):
    html = """
    <br>
    <div>
      <h3>Please select the display range:</h3>
    </div>
    <br>
    """

    html = html +"""
    <br>
    <div id="date_range_slider_1"></div>
    <div align="center"><button type="button" id="calc1">Generate</button></div>
    <div id="chart1" style="margin-top:20px; margin-left:90px; width:650px; height:400px;"></div>
    <div id="chart2" style="margin-top:20px; margin-left:90px; width:650px; height:400px;"></div>
    <div id="chart3" style="margin-top:20px; margin-left:90px; width:650px; height:400px;"></div>
    </div>
    """
    return html