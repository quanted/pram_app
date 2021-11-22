"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<img src = \"/pram/static/images/varroapop/varroapop_model_kuan.png\" alt=\"Varroapop_1\">' \
            '<p><a href=\"https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=337175\">' \
            'Kuan <i>et al.</i>, 2018. Sensitivity analysis for simulating pesticide ' \
            'impacts on honey bee colonies. <i>Ecological Modeling</i>. </a>  </p>'

#model description html for description page
description = '<p>VarroaPop + Pesticide is a screening level tool to assess the effects of pesticide exposure on' \
              ' honey bee colonies. This simulation model consider the age and caste structure of the colony (i.e. ' \
              'eggs, larvae, pupae, drones, workers, foragers, queen), the effects of weather and foraging behavior,' \
              ' and (optionally) simultaneous infestation by Varroa destructor mites. Diet-based pesticide exposure' \
              ' occurs through contamination of pollen and nectar as a result of foliar, soil, or seed application' \
              ' of the active ingredient. For foliar application, direct contact of the active ingredient on ' \
              'foragers is also considered. </p>'

# How model name appears on web page
header = 'VarroaPop'

history = '<p>User History</p>'

references = '<p>Peer-reviewed articles describing the use of VarroaPop and VarroaPop+Pesticide:</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=337175\">' \
             'Kuan <i>et al.</i> 2018. Sensitivity analysis for simulating pesticide ' \
             'impacts on honey bee colonies. <i>Ecological Modeling</i>. </a></li>' \
             '<li>DeGrandi-Hoffman, G. and Curry, R., 2005. The population dynamics of varroa mites in honey bee colonies: ' \
             'Part I-The VARROAPOP program. <i>American Bee Journal</i>.</li>' \
             '<li>DeGrandi-Hoffman, G. and Curry, R., 2005. Simulated population dynamics of Varroa mites in honey bee' \
             ' colonies: Part II. What the VARROAPOP model reveals. <i>American Bee Journal</i>.</li>' \
             '</ul>' \
             '<p>' \
             'Source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://github.com/quanted/pram_app/tree/master/models/varroapop">pram_app on GitHub (front end)</a></li>' \
             '<li><a href=\"http://github.com/quanted/flask_qed\">flask_qed on GitHub (back end model)</a></li>' \
             '<li><a href=\"http://github.com/jeffreyminucci/minucci_vp_mcmc\">R wrapper for VarroaPop parameter estimation via MCMC</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including VarroaPop.' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\https://scholarsarchive.byu.edu/iemssconference/2016/Stream-B/27/\">Sobol’ sensitivity analysis for stressor impacts on honeybee colonies</a></li>' \
             '<li><a href=\"https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=337175\">Sensitivity analysis for simulating pesticide impacts on honey bee colonies</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf\">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://training.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf\">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>'

