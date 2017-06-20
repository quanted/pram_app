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
            '<img src = \"/static_qed/images/latex/foxsurplus/foxsurplus_1.png\" alt=\"Fox Surplus_1\">'

#model description html for description page
description = '<p> Based on Gompertz growth function, William W. Fox established an alternative surplus-yield model which created'\
              'an exponential relationship between fishing effort and population size:'\
              '</p> <img src = \"/static_qed/images/latex/foxsurplus/foxsurplus_des_1.png\" alt=\"Fox Surplus Model\">'\
              '<p>Fox surplus yield model: </p>'\
              '<ul class=\"bullet\">'\
              '<li>considers population as one unit of biomass, without age structure</li>'\
              '<li>assumes people can harvest the surplus production without endangering the population</li>'\
              '</ul>'

# How model name appears on web page
header = 'Fox Surplus Yield'

history = '<p>User History</p>'

references = '<p>Will be populated soon...</p>'