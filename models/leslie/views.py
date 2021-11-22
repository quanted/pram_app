"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '' \
            '<p>To build a Leslie model, one need to know the following inputs:</p>' \
            '<img src = \"/pram/static/images/latex/leslie/leslie_1.png\" alt=\"Leslie Matrix_1"\>' \
            '<p>The fecundiy can be viewed as the number of offspring produced at the next age class</p>' \
            '<p><i>B<sub>k+1</sub></i>weighted by the probability of reaching the next age class.</p>' \
            '<img src = \"/pram/static/images/latex/leslie/leslie_2.png\" alt=\"Leslie Matrix_2\">' \
            '<p>The Leslie model is described by the following two equations:</p>' \
            '<img src = \"/pram/static/images/latex/leslie/leslie_3.png\" alt=\"Leslie Matrix_3\">' \
            '<p>where the first equation estimates the number of offspring produced by each age class,</p>' \
            '<p>and the second equation estimates the number of individuals survived from age class k-1</p>' \
            '<p>to k. Thus we can present Leslie model in terms of system of equations as:</p>' \
            '<img src = \"/pram/static/images/latex/leslie/leslie_4.png\" alt=\"Leslie Matrix_4\">' \
            '<p>more compactly:</p>' \
            '<img src = \"/pram/static/images/latex/leslie/leslie_5.png\" alt=\"Leslie Matrix_5\">' \


#model description html for description page

description = '<p>Leslie matrix (model) is a discrete, non-negative, age-structured model,' \
                'which describes the development, mortality, and reproduction of organisms over a period of time.' \
                'As one of the most popular models in population ecology, it was invented by Patrick H. Leslie in 1945.' \
                '</p>' \
                '<p>' \
                'A typical Leslie model is written as:' \
                '</p>' \
                '<img src = \"/pram/static/images/latex/leslie/leslie_des_1.png"\ alt=\"Leslie Matrix_1\">' \
                '<p>' \
                'which can be expanded into:' \
                '</p>' \
                '<img src = \"/pram/static/images/latex/leslie/leslie_des_2.png\" alt=\"Leslie Matrix_2\">' \
                '<p>' \
                'Thus a Leslie matrix contains:' \
                '</p>' \
                '<ul class=\"bullet\">' \
                  '<li>age-specific fertilities in the first row</li>' \
                  '<li>age-specific survival probabilities in the subdiagonal</li>' \
                  '<li>zeros elsewhere</li>' \
                '</ul>' \

# How model name appears on web page
header = 'Leslie'

history = '<p>User History</p>'

references = '<p></p>' \



