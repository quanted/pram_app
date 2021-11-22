"""
.. module:: views
   :synopsis: A useful module indeed.
"""

# these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

# model algorithm html for algorithm page
algorithm = '' \
            '<p>The population change rate is:</p>' \
            '<img src = \"/pram/static/images/latex/maxsus/maxsus_1.png\" alt=\"Maxsus_1\">' \
            '<p>At equilibrium:</p>' \
            '<img src = \"/pram/static/images/latex/maxsus/maxsus_2.png\" alt=\"Maxsus_2\">'

# model description html for description page
description = '<p> The maximum sustainable yield (MSY) model was developed to maintain the population size ' \
              'at the point of maximum growth rate by harvesting the individuals that would normally be added to the population, ' \
              'and allowing the population to continue to be productive indefinitely. It is based on logistic model and adds ' \
              'a term representing the number of individuals being removed from the population (H):</p> ' \
              '<img src = "/pram/static/images/latex/maxsus/maxsus_des_1.png" alt="Maximum Sustainable Yield Model"> ' \
              '<p>When the population size is small, its growth rate is low because there are few organisms to give birth. ' \
              'When the population size is large, still, its growth rate is low because the high mortality rate from competition. ' \
              'When the population growth rate reaches its maximum value, the number of individuals that ' \
              'can be added to a population by natural processes is maximized, which equals the maximum harvest rate. ' \
              'If more individuals than this are removed from the population, the population is at risk for decline to extinction.</p> '

# How model name appears on web page
header = 'Maximum Sustainable Yield'

history = '<p>User History</p>'

references = '<p>Will be populated soon...</p>'
