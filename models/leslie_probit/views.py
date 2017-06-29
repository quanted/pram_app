"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '' \
            '<p>Ideally, individuals\'\ survival and fertility rates can be treated as constants over time:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_1.png"\ alt=\"Leslie Dose_1"\>' \
            '<p>When taking account the reduction of fertility due to the increased population size,</p>' \
            '<p>the fertility is modified into:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_2.png"\ alt=\"Leslie Dose_2"\>' \
            '<p>When considering the impacts from chemical exposure the survival rate is modified into:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_3.png"\ alt=\"Leslie Dose_3"\>' \
            '<p>The logistic dose response model is given::</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_4.png"\ alt=\"Leslie Dose_4"\>' \



#model description html for description page
description = '<p>Developed by Belgian mathematician <a href=\"http://en.wikipedia.org/wiki/Pierre_Fran%C3%A7ois_Verhulst"\ target=\"_blank"\>' \
              'Pierre Verhulst</a> (1804-1849), logistic model assumes that population change rate (r<sub>t</sub>) is not a constant.' \
              'It is related to the maximum population growth rate (r<sub>0</sub>), carrying capacity (K), and current population' \
              '(N<sub>t</sub>), which follows the following relationship: ' \
              '</p>' \
              '<img src = \"/static_qed/images/latex/logistic/logistic_des_1.png"\ alt=\"Logisitic Model"\>' \
              '<ul class="bullet">' \
                '<li> Population growth rate (r<sub>t</sub>) declines with the increase of population size (N<sub>t</sub>) </li>' \
                '<li> Population growth rate (r<sub>t</sub>) is 0 when the population (N<sub>t</sub>) reaches carrying capacity (K) </li>' \
                '<li> If population size (N<sub>t</sub>) exceeds carrying capacity (K), then population declines </li>' \
              '</ul></p>' \

# How model name appears on web page
header = 'Leslie-Probit'

history = '<p>User History</p>'

references = '<p></p>' \



