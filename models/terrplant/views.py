"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>TerrPlant derives estimated exposure concentrations (EECs) of pesticide in runoff and in drift. From the derived EECs TerrPlant develops risk quotients (RQs) are developed for non-listed and listed species of monocots and dicots inhabiting dry and semi-aquatic areas adjacent to treatment sites using the equations below.</p>' \
            '<p>Runoff to dry areas:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image1.png\" alt=\"Terrplant_1\">' \
            '<p>Runoff to semi-aquatic areas:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image2.png\" alt=\"Terrplant_2\">' \
            '<p>Spray drift:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image3.png\" alt=\"Terrplant_3\">' \
            '<p>Total for dry areas:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image4.png\" alt=\"Terrplant_4\">' \
            '<p>Total for semi-aquatic areas:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image5.png\" alt=\"Terrplant_5\">' \
            '<p>To calculate RQ values plant survival and growth data (EC<sub>25</sub>, NOAEC) input by the user for seedling emergence and vegetative vigor is divided into the total EEC for each scenario (total dry, total semi-aquatic, total drift) and plant type (monocot and dicot). For the non-listed species the EC<sub>25</sub> values are used and for listed species the NOAEC values are used. For spray drift RQ calculation the most sensitive measure of effect (seedling emergence or vegetative vigor) is used. </p>' \
            '<p>Risk quotient calculation for non-listed species:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image6.png\" alt=\"Terrplant_6\">' \
            '<p>Risk quotient calculation for listed species:</p>' \
            '<img src = \"/static_qed/images/latex/terrplant/terrplant_image7.png\" alt=\"Terrplant_7\">'

#model description html for description page
description = '<p>TerrPLANT provides screening level estimates of exposure to terrestrial plants ' \
              'from single pesticide applications through runoff or drift.  Monocots and dicots ' \
              'found in dry or semi-aquatic habitats can be evaluated using this model.  Exposure ' \
              'estimates can be generated for both listed and non-listed species using TerrPLANT.</p>' \
              '<p>Both dry and semi-aquatic exposure estimates include conceptual models with a ' \
              'target area that is adjacent to a non-target area.  Dry area estimates are determined ' \
              'using pesticide amounts received in the non-target area through sheet runoff from a ' \
              'target area equal in size.  Semi-aquatic estimates are based on pesticide amounts in ' \
              'channel runoff from a target area that is 10 times larger than the non-target area.</p>' \
              '<p>The TerrPLANT model assumes that 1% of the mass of liquid pesticides applied ' \
              'per acre will runoff to the non-target area, 5% for aerial pesticides and 0% for ' \
              'granular applications.  Toxicity of pesticides to non-listed species is based on ' \
              'EC<sub>25</sub> values for the most sensitive monocots and dicots tested.  For ' \
              'listed species, corresponding NOAEC or EC<sub>05</sub> values are used to determine ' \
              'toxicity.  RQ values are generated through comparisons with adverse effects ' \
              'levels measured in seedling emergence studies.</p>'

# How model name appears on web page
header = 'TerrPlant'

history = '<p>User History</p>'

references = '<p>' \
             'Specific EPA guidance and the Microsoft Excel version of the model on the TerrPlant Program can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/terrplant-version-122-users-guide-pesticide-exposure\">TerrPlant Documentation</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/terrplant-version-122-users-guide-pesticide-exposure\">User\'s Guide</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2016-11/terrplant_v1.2.210-29-2009.xls">TerrPlant Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/puruckertom/pram_eco/tree/master/models/terrplant\">pram_src on GitHub (front end)</a></li>' \
             '<li><a href=\"https://github.com/quanted/pram/tree/master/pram/terrplant\">pram_src on GitHub (back end model)</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of TerrPlant in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://pdfs.semanticscholar.org/35ba/0c9682867dc80462eed59e8b3d926549a483.pdf">Diazinon- Delta Smelt and Tidewater Goby</a></li>' \
             '<li><a href=\"https://archive.epa.gov/pesticides/chemicalsearch/chemical/foia/web/pdf/128008/128008-2010-12-23a.pdf">Boscalid</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.3144&amp;rep=rep1&amp;type=pdf">Metolachlor- Delta Smelt and California Tiger Salamander</a></li>' \
             '<li><a href=\"https://www3.epa.gov/pesticides/endanger/litstatus/effects/redleg-frog/aldicarb/esa_final.pdf">Aldicarb- California Red-legged frog</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.168.6045&rep=rep1&type=pdf">Atrazine- Freshwater Mussel</a></li>' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2012-0230-0005">Atrazine- FIFRA Scientific Advisory Panel</a></li>' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2007-0431-0020">Reregistration Eligibility Decision for Mefluidide</a></li>' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2004-0307-0001">Chlorimuron-ethyl</a></li>' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2004-0167-0217">Reregistration Eligibility Document for 2,4-D</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how TerrPlant fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/risk/ecological-risk-assessment\">' \
             'EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/ecological-risk-assessment-pesticides-technical\">' \
             'EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"https://nepis.epa.gov/Exe/ZyNET.exe/40000006.TXT?ZyActionD=ZyDocument&Client=EPA&Index=2000+Thru+2005&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C00thru05%5CTxt%5C00000002%5C40000006.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL\">' \
             'Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk\">' \
             'EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2016-10/documents/pfam-whitepaper.pdf\">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including TerrPlant.' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"https://nctc.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk/risk-tools-and-databases\">Ecological Risk Assessment and Improving Evaluation Tools, Don Brady (USEPA)</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>'

