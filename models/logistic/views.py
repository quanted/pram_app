"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '' \
            '<p>The population change rate of logistic model is:</p>'\
            '<img src = \"/static_qed/images/latex/logistic/logistic_1.png\" alt=\"Logistic_1\">'\
            '<p>whose solution is:</p>'\
            '<img src = \"/static_qed/images/latex/logistic/logistic_2.png\" alt=\"Logistic_2\">'


#model description html for description page
description = '<p>Developed by Belgian mathematician '\
              '<a href=\"http://en.wikipedia.org/wiki/Pierre_Fran%C3%A7ois_Verhulst" target="_blank\"> '\
              'Pierre Verhulst</a> (1804-1849), logistic model assumes that population change rate (r<sub>t</sub>) is not a constant.'\
              'It is related to the maximum population growth rate (r<sub>0</sub>), carrying capacity (K), and current population'\
              '(N<sub>t</sub>), which follows the following relationship: '\
              '</p><img src = \"/static_qed/images/latex/logistic/logistic_des_1.png\" alt=\"Logisitic Model\">'\
              '<ul class=\"bullet\">'\
              '<li> Population growth rate (r<sub>t</sub>) declines with the increase of population size (N<sub>t</sub>) </li>'\
              '<li> Population growth rate (r<sub>t</sub>) is 0 when the population (N<sub>t</sub>) reaches carrying capacity (K) </li>'\
              '<li> If population size (N<sub>t</sub>) exceeds carrying capacity (K), then population declines </li>'\
              '</ul>'


# How model name appears on web page
header = 'Logistic'

history = '<p>User History</p>'

references = '<p>Will be populated soon...</p>'


