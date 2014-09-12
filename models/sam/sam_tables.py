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
    return "Fake Table"