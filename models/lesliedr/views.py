"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>Ideally, individuals\' survival and fertility rates can be treated as constants over time:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_1.png\" alt=\"Leslie Dose_1\">' \
            '<p>When taking account the reduction of fertility due to the increased population size,</p>' \
            '<p>the fertility is modified into:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_2.png\" alt=\"Leslie Dose_2\">' \
            '<p>When considering the impacts from chemical exposure the survival rate is modified into:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_3.png\" alt=\"Leslie Dose_3\">' \
            '<p>The logistic dose response model is given:</p>' \
            '<img src = \"/static_qed/images/latex/lesliedr/lesliedr_4.png\" alt=\"Leslie Dose_4\">' \


#model description html for description page
description = '<p>Traditionally, ecological risk assessment of pesticides is based on the risk, ' \
              'between measured environment concentrations and laboratory tested concentrations ' \
              'which cause biological effects. </p>' \
              '<p>This approach has several drawbacks:</p>'\
              '<ul class=\"bullet\">'\
              '<li>difficult to relate risk ratios to ecological values (e.g., population size)</li>'\
              '<li>safety factors used in estimating risk ratios contain great uncertainty which easily cause over ' \
              'or under protection</li>'\
              '</ul>'\
              '<p>As a solution, adding population models to the ecological risk assessment process can bridge the ' \
              'gap between measurements and protection goals in the following aspects:</p>'\
              '<ul class=\"bullet\">'\
              '<li>reduce uncertainty in extrapolation individual level to population level </li>'\
              '<li>identify worse scenarios with less effort</li>'\
              '<li>integrate the effects of multiple stresses</li>'\
              '<li>reduce the use of laboratory animals</li></ul>'\

# How model name appears on web page
header = 'Leslie Logistic Dose Response'

history = '<p>User History</p>'

references = '<p>Will be back soon.</p>'
