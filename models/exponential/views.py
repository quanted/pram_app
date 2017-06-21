"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '' \
            '<p>The population change rate is:</p>' \
            '<img src = \"/static_qed/images/latex/exponential/exp_1.png\" alt=\"Exp_1\">' \
            '<p>If r is constant, the model is known as exponential growth model.</p>' \
            '<p>Integrate both sides of the above equation:</p>' \
            '<img src = \"/static_qed/images/latex/exponential/exp_2.png\" alt=\"Exp_2\">'\
            '<ul class=\"bullet\">' \
            '<li>If r<0, population exponentially declines</li>' \
            '<li>If r>0, population exponentially increases</li>' \
            '<li>If r=0, population does not change</li>' \
            '</ul>'
#model description html for description page
description = '<p> Exponential model (a.k.a. Malthusian growth model) is associated with the name of '\
              '<a href=\"http://en.wikipedia.org/wiki/Thomas_Robert_Malthus\">Thomas Robert Malthus</a> (1766-1834),'\
              'who first realized that any species can potentially increase in numbers according to a geometric series.'\
              'In \'Essay on the Principles of Pupulation\', Malthus argued that in the absence of any constraints, human population will grow in a multiplicative'\
              'manner until the depletion of food.</p>'\
              '<p>Assumptions of Exponential Model:</p>'\
              '<ul class=\"bullet\">'\
              '<li>Continuous reproduction (e.g., no seasonality)</li>'\
              '<li>All organisms are identical (e.g., no age structure)</li>'\
              '<li>Environment is constant in space and time (e.g., resources are unlimited)</li></ul>'\

# How model name appears on web page
header = 'Exponential'

history = '<p>User History</p>'

references = '<p>Will be populated soon...</p>'
