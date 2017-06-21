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
            '<img src = "/static_qed/images/latex/fellerarley/fellerarley_1.png" alt="Feller-Arley_1">'\
            '<p>In the perspective of probability, the chance of remaining population N at time t + &#916;t</p>'\
            '<p>needs to meet one of the following three conditions:</p>'\
            '<ul class="nobullet">'\
            '<li>N<sub>(t-1)</sub>=N-1, and exactly one birth within the interval (t, t + &#916;):</li>'\
            '<li><img src = "/static_qed/images/latex/fellerarley/fellerarley_2.png" alt="Feller-Arley_2"></li>'\
            '<li>N<sub>(t-1)</sub>=N+1, and exactly one death within the interval (t, t + &#916;):</li>'\
            '<li><img src = "/static_qed/images/latex/fellerarley/fellerarley_3.png" alt="Feller-Arley_3"></li>'\
            '<li>N<sub>(t-1)</sub>=N, and neither birth or death occur within the interval:</li>'\
            '<li><img src = "/static_qed/images/latex/fellerarley/fellerarley_4.png" alt="Feller-Arley_4"></li>'\
            '</ul>'
'<p>Combining the above three probabilities:</p>'\
    '<img src = "/static_qed/images/latex/fellerarley/fellerarley_5.png" alt="Feller-Arley_5">'\
    '<p>The change of probability becomes: </p>'\
    '<img src = "/static_qed/images/latex/fellerarley/fellerarley_6.png" alt="Feller-Arley_6">'\

#model description html for description page
description = '<p>Feller-Arley Markov process is also known as the birth-death process, which assumes:</p>'\
            '<ul class="bullet">'\
              '<li>no internal population structure, each individual can give birth and death</li>'\
              '<li>the birth rate and death rate are constant</li>'\
              '</ul>'' \
              ''<p>As a Markov procees, the future population size is only related to its neighbor state.'\
            'In the below figure, when a birth occurs, the process goes from state n to n + 1.'\
            'When a death occurs, the process goes from state n to state n-1. The possibility of "moving"'\
            'to another state is governed by the birth and death rates.</p>'\
            '<img src = "/static_qed/images/latex/fellerarley/BD-proces.png" alt="Feller-Arley Markov Process">'\

# How model name appears on web page
header = 'Feller-Arley Markov Process'

history = '<p>User History</p>'

references = '<p>Will be populated soon...</p>'


