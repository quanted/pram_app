"""
.. module:: views
   :synopsis: A useful module indeed.
"""

batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>Predictor of chance of individual effect using probit dose-response curve slope ' \
            'and median lethal estimate which is based on the following formula:</p>' \
            '<img src = \"/static_qed/images/latex/iec/iec_image1.png\">'

#model description html for description page
description = '<p>IECV1.1 (Individual Effect Chance Model Version 1.1) estimates potential ' \
              'effects at an individual level. Generally, available toxicity data provides ' \
              'an LC<sub>50</sub> or an EC<sub>50</sub>, (the concentration at which 50% ' \
              'of the test population exhibits the designated endpoint, usually mortality).  ' \
              'The Agency uses the probit dose response relationship as a tool for deriving ' \
              'the probability of effects on a single individual.  The individual effects ' \
              'probability associated with the acute RQ is based on the mean estimate of ' \
              'the probit dose response slope and an assumption that that probit model is ' \
              'appropriate for the data set.  In some cases, probit is not the appropriate ' \
              'model for the data, and EFED has low confidence in extrapolations from these ' \
              'types of data sets.  In addition to a single effects probability estimate ' \
              'based on the mean, upper, and lower estimates of the effects probability are ' \
              'also provided to account for variance in the slope, if available.  The upper ' \
              'and lower bounds of the effects probability are based on available information ' \
              'on the 95% confidence interval of the slope.  </p>'

#these should be in templates
# How model name appears on web page
header = 'IEC'

history = '<p>User History</p>'

references = '<p>Specific EPA guidance and the Microsoft Excel version of the IEC model are not ' \
             'currently available on the Internet:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li>NA</li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/quanted/ubertool_app/tree/master/models/iec">' \
             'ubertool_src on GitHub (front end)</a></li>' \
             '<li><a href=\"https://github.com/quanted/ubertool/tree/master/ubertool/iec">' \
             'ubertool_src on GitHub (back end model)</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of IEC in reregistration eligibility documents and ' \
             'pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.3144&amp;rep=rep1&amp;type=pdf\">' \
             'Metolachlor- Delta Smelt and California Tiger Salamander</a></li>' \
             '<li><a href=\"https://www3.epa.gov/pesticides/endanger/litstatus/effects/redleg-frog/aldicarb/esa_final.pdf\">' \
             'Aldicarb- California Red-legged frog</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.168.6045&rep=rep1&type=pdf\">' \
             'Atrazine- Freshwater Mussel</a></li>' \
             '<li><a href=\"https://archive.epa.gov/pesticides/reregistration/web/pdf/mefluidide_red.pdf\">' \
             'Reregistration Eligibility Decision for Mefluidide</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.168.5654&rep=rep1&type=pdf\">' \
             'Red-legged Frog Dimethoate Pesticide Effects</a></li>' \
             '<li><a href=\"https://www3.epa.gov/pesticides/endanger/litstatus/effects/redleg-frog/carbaryl/determination.pdf\">' \
             'Red-legged Frog Carbaryl Pesticide Effects</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how IEC fits into the overall ecological risk assessment process for ' \
             'pesticides can be found at the following links:' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.epa.gov/sites/production/files/2014-11/documents/ecorisk-overview.pdf\">' \
             'EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"http://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/ecological-risk-assessment-pesticides-technical\">' \
             'EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"http://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=40000006.txt\">' \
             'Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"http://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/technical-overview-ecological-risk-assessment-1\">' \
             'EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"http://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/guidance-development-conceptual-models-problem\">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including IEC. ' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf\">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://training.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf\">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>'
