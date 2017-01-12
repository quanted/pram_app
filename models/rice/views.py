"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>The formula of the Tier I Rice Model v1.0:</p>' \
            '<img src = \"/static_qed/images/latex/rice/rice.eqn1.gif\">' \
            '<p>The Tier I Rice Conceptual Model:</p>' \
            '<img src = \"/static_qed/images/latex/rice/rice.eqn2.gif\">' \
            '<p>It is more customary to describe a rice paddy in terms of depth rather than volume or mass. Therefore, ' \
            'the following equations are defined:</p>' \
            '<img src = \"/static_qed/images/latex/rice/rice.eqn3.gif\">' \
            '<p>Further, the input mass per unit area as:</p>' \
            '<img src = \"/static_qed/images/latex/rice/rice.eqn4.gif\">' \
            '<p>After substititution, the conceptual model with commonly understood parameters is the following:</p>' \
            '<img src = \"/static_qed/images/latex/rice/rice.eqn5.gif\">'

#model description html for description page
description = '<p>The Tier I Rice Model (Version 1.0) is designed to estimate surface ' \
              'water exposure from the use of pesticide in rice paddies. It is a screening ' \
              'level model that is based on the Interim Rice Model, which has been used ' \
              'by the Environmental Fate and Effects Division for multiple years. The model ' \
              'calculates a single, screening-level concentration that represents both short ' \
              'and long term surface water exposures. The screening-level concentraion can be ' \
              'used for both aquatic ecological risk assessments and drinking water exposure ' \
              'assessments for human health risk assessment. </p>'

# How model name appears on web page
header = 'RICE'

history = '<p>User History</p>'

references = '<p>EPA guidance on the Tier I Rice Program can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.epa.gov/oppefed1/models/water/#rice\">Tier I Rice Documentation</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/models/water/rice_tier_i.htm\">User\'s Guide</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/models/water/rice_tier_i.pdf\">EPA Guidance for Tier I Estimation of Aqueous Pesticide Concentrations in Rice Paddies</a></li>' \
             '<li><a href=\"http://www.cdpr.ca.gov/docs/emon/pubs/ehapreps/report_263.pdf\">California DPR: Review and Evaluation of Pesticide Modeling Approaches in Rice Paddies</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_src/tree/master/rice\">ubertool_src on GitHub</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of the Tier I Rice model in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li>NA</li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how the Tier I Rice model fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.epa.gov/oppfead1/endanger/consultation/ecorisk-overview.pdf\">' \
             'EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/ecorisk_ders/\">' \
             'EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"http://www.epa.gov/OSA/spc/pdfs/rchandbk.pdf\">' \
             'Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/ecorisk_ders/toera_analysis_exp.htm\">' \
             'EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"http://www.epa.gov/pesticides/science/efed/policy_guidance/team_authors/endangered_species_reregistration_workgroup/esa_conceptual_model_pf.htm\">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports for the use of Ricein NOAA consultations with the EPA (Endangered Species Act Section 7 Consultations) concerning the impact of pesticides on listed species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/consultation/opinions/biop_thiobencarb.pdf\">Thiobencarb</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/consultations/pesticides_batch5opinion.pdf\">Biological Opinion 5 (Oryzalin,Pendimethalin,Trifluralin)</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/consultations/pesticide_opinion4.pdf\">Biological Opinion 4 (2,4-D, Triclopyr BEE, Diuron, Linuron, Captan, Chlorothalonil )</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/pesticide_biop.pdf\">Biological Opinion 1 (Chlorpyrifos, Diazinon, and Malathion)</a>' \
             '</ul>' \
             '<p>Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including the Tier I Rice model .' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/File.ashx?cid=199\">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://training.fws.gov/EC/Resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf\">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"http://pep.wsu.edu/wrpm/WRPM_11_files/Agenda%20and%20PPT%20pdfs/13Brady5-18-11PM.pdf\">Ecological Risk Assessment and Improving Evaluation Tools, Don Brady (USEPA)</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>'


