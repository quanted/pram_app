"""
.. module:: sam_tables
   :synopsis: A useful module indeed.
"""

import time
import datetime


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