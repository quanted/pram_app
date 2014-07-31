"""
.. module:: agdrift_therps_tables
   :synopsis: A useful module indeed.
"""

import datetime

def timestamp(agdrift_therps_obj):
    st = datetime.datetime.strptime(agdrift_therps_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
    <b>Agdrift-Therps<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

