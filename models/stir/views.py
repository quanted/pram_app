"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>Saturated air concentration:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image1.png\" alt=\"Stir_1\">' \
            '<p>Avian inhalation rate:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image2.png\" alt=\"stir_2\">' \
            '<p>Maximum avian vapor inhalation dose:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image3.png\" alt=\"stir_3\">' \
            '<p>Mammalian inhalation rate:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image4.png\" alt=\"stir_4\">' \
            '<p>Maximum Mammalian Vapor Inhalation Dose:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image5.png\" alt=\"stir_5\">' \
            '<p>Air column concentration after spray:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image6.png\" alt=\"stir_6\">' \
            '<p>Avian spray droplet inhalation dose:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image7.png\" alt=\"stir_7\">' \
            '<p>Mammalian spray droplet inhalation dose:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image8.png\" alt=\"stir_8\">' \
            '<p>Conversion of mammalian inhalation LC50 to LD50:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image9.png\" alt=\"stir_9\">' \
            '<p>Adjusted mammalian inhalation LD50:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image10.png\" alt=\"stir_10\">' \
            '<p>Estimated avian inhalation LD50:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image11.png\" alt=\"stir_11\">' \
            '<p>Adjusted avian inhalation LD50:</p>' \
            '<img src = \"/static_qed/images/latex/stir/stir_image12.png\" alt=\"stir_12\">'

#model description html for description page
description = '<p>The STIR model was developed as a screening model to estimate ' \
              'inhalation risk of chemicals to birds and mammals.  Chemical ' \
              'specific physical properties are required for executing the model.  ' \
              'Vapor phase and droplet-spray exposure risks are estimated in STIR ' \
              'and then compared to avian inhalation or mammalian inhalation and ' \
              'oral toxicity data.  Inhalation exposure routes addressed by the model ' \
              'include directly applied spray, volatilization of residues on plant ' \
              'canopy and volatilization of residues in soil.</p>' \
              '<p>The exposure estimates are based on the type of application (i.e., ' \
              'air or ground spray, granules, seed treatments) and the quantity of a ' \
              'specified chemical that is to be applied to a field.  The screening tool ' \
              'calculates the theoretical maximum pure product air concentration at ' \
              'standard temperature and pressure based on vapor pressure and molecular ' \
              'weight. STIR also calculates inhalation rates and inhalation dose as a ' \
              'function of saturated air concentration, inhalation rate and animal ' \
              'weight. Toxicity endpoints are estimated using adjusted LD<sub>50</sub> ' \
              'values. Model results are presented as a ratio of the inhalation exposure ' \
              'dose to toxicity.  To determine if inhalation exposure to a particular ' \
              'chemical warrants further investigation, ratios are compared to threshold ' \
              'values.</p>' \
              '<img src = \"/static_qed/images/stir_figure1.gif\" alt=\"STIR Model\">'

# How model name appears on web page
header = 'STIR'

history = '<p>User History</p>'

references = '<p>Specific EPA guidance and the Microsoft Excel version of the model on the STIR Program can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/stir-version-10-users-guide-pesticide-inhalation">STIR Documentation</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/stir-version-10-users-guide-pesticide-inhalation">User\'s Guide</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2015-06/stir_version_1_0.xls\">STIR Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_eco/tree/master/models/stir\">ubertool_src on GitHub (front end)</a></li>' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_ecorest/tree/master/REST_UBER/stir_rest\">ubertool_src on GitHub (back end model)</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of STIR in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2012-0230-0005">Atrazine</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how STIR fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/risk/ecological-risk-assessment\">' \
             'EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/ecological-risk-assessment-pesticides-technical\">' \
             'EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"https://nepis.epa.gov/Exe/ZyNET.exe/40000006.TXT?ZyActionD=ZyDocument&Client=EPA&Index=2000+Thru+2005&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C00thru05%5CTxt%5C00000002%5C40000006.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL\">Science Policy Handbook on Risk Characterization\">' \
             'Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk">' \
             'EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2016-10/documents/pfam-whitepaper.pdf\">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts on the subject of EPA\'s ecological risk assessment models, including STIR.' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://nctc.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk/risk-tools-and-databases">Ecological Risk Assessment and Improving Evaluation Tools</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>'

