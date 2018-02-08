"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '' \
            '<p>The population change rate is:</p>'\
            '<img src = \"/static_qed/images/latex/gompertz/gompertz_1.png\" alt=\"Gompertz_1\">'

#model description html for description page
description = '<p>The Gompertz model was first introduced to model mortality by'\
              '<a href=\"http://en.wikipedia.org/wiki/Benjamin_Gompertz\" target=\"_blank\"> '\
              'Benjamin Gompertz</a> in 1825. It assumes that population growth rate (r<sub>t</sub>) decays exponentially:</p>'\
              '<img src = \"/static_qed/images/latex/gompertz/gompertz_des_1.png\" alt=\"Gompertz Model\">'\
              '<p>Gompertz model has been used to model the growth of tumors and in fisheries '\
              'ecology in the <a href=\"http://www.pram.org/foxsurplus_description.html\">Fox surplus yield model</a></p></p>'

# How model name appears on web page
header = 'Gompertz'

history = '<p>User History</p>'

references = '<p>Will be populated soon...</p>'