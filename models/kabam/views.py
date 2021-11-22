"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates

batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>The KABAM model is used to estimate the potential bioaccumulation of hydrophobic organic pesticides in freshwater foodwebs and to estimate the risks to birds and mammals consuming the prey items from these freshwater food webs. The first part of the model calculate the parameters necessary to determine the pesticide concentration in tissues, bioaccumulation factors, bioconcentration factors, biomagnification factors and biota sediment accumulation factors for each trophic level in the aquatic food web. The KABAM model includes a trophic level representation for phytoplankton, zooplankton, benthic invertebrates, filter feeders, small fish, medium fish and large fish. The second part of the model estimates exposure and toxicological effects of a pesticide into risk estimates for mammals and birds consumging contaminated prey. Equations for the bioaccumulation of the food web are below:</p>' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image1.png\">' \
            '<p>Parameters calculated that contribute to trophic level pesticide concentration in tissues:</p>' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image2.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image3.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image4.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image5.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image6.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image7.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image8.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image9.png\">' \
            '<p>These equations are used to determine the dose-based response of mammals and birds feeding on the trophic levels</p>' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image10.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image11.png\">' \
            '<img src = \"/pram/static/images/latex/kabam/kabam_image12.png\">'

#model description html for description page
description = '<p>K<sub>ow</sub> (based) Aquatic BioAccumulation Model (KABAM) ' \
              'links hydrophobic organic pesticide bioaccumulation in aquatic ' \
              'components of a food web to terrestrial exposure in birds and ' \
              'mammals.  Given the dual ecosystem emphasis, KABAM is divided ' \
              'into two portions: 1) an aquatic bioaccumulation model and 2) ' \
              'a terrestrial risk component.  The bioaccumulation model is based ' \
              'off of a widely accepted model by Arnot and Gobas (2004) developed to ' \
              'evaluate PCB and select pesticide transfer through Great Lakes ecosystems.  ' \
              'Dietary and respiratory exposures are estimated using a pesticide\'s ' \
              'octanol-water partition coefficient (KOW).  The terrestrial risk component ' \
              'follows EPA\'s TREX model.  KABAM spans all trophic levels from aquatic ' \
              'primary producers and consumers to aquatic and terrestrial predators ' \
              '(Figure 1).</p>' \
              '<p>To use KABAM effectively, a pesticide must adhere to all 3 of the ' \
              'following characteristics:</p>' \
              '<ul class=\"bullet\">' \
              '<li>Be chemically non-ionic and organic</li>' \
              '<li>Log KOW; range = 4 - 8</li>' \
              '<li>Can reach aquatic habitats</li>' \
              '</ul>'

# How model name appears on web page
header = 'KABAM'

history = '<p>User History</p>'

references = '<p>Specific EPA guidance and the Microsoft Excel version of the model on the KABAM model can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/kabam-version-10-users-guide-and-technical">KABAM Documentation</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/kabam-version-10-users-guide-and-technical">User\'s Guide</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/kabam-version-10-users-guide-and-technical-9\">User\'s Guide (pdf)</a>' \
             '</li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2015-07/kabam_v1_0.xls">KABAM Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/quanted/pram_app/tree/master/models/kabam">pram_src on GitHub (front end)</a></li>' \
             '<li><a href=\"https://github.com/quanted/pram/tree/master/pram/kabam">pram_src on GitHub (back end)</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of KABAM in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://archive.epa.gov/pesticides/reregistration/web/pdf/endosulfan_red.pdf">Endosulfan- Office of Pesticide Programs Environmental Fate and Effects Division</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how KABAM fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/risk/ecological-risk-assessment\">' \
             'EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/ecological-risk-assessment-pesticides-technical\">' \
             'EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"https://nepis.epa.gov/Exe/ZyNET.exe/40000006.TXT?ZyActionD=ZyDocument&Client=EPA&Index=2000+Thru+2005&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C00thru05%5CTxt%5C00000002%5C40000006.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL\">' \
             'Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk">' \
             'EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2016-10/documents/pfam-whitepaper.pdf\">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including KABAM.</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://nctc.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk/risk-tools-and-databases\">Ecological Risk Assessment and Improving Evaluation Tools</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>' \
             '<p>' \
             'Peer-reviewed journal articles and manuscripts on the use of the KABAM model:' \
             '</p>' \
             '<ul>' \
             '<li><a href=\"http://onlinelibrary.wiley.com/doi/10.1897/03-438/abstract;jsessionid=5C0FEBC3E04A35DD2C3E804A8EE523C0.d01t02?deniedAccessCustomisedMessage=&userIsAuthenticated=false\">' \
             'Arnote, J.A. & Gobas, F.A.P. (2004). A food web bioaccumulation model for organic chemicals in aquatic ecosystems. Environmental Toxicology and Chemistry, 23(10), 2343-2355.</a></li>' \
             '<li><a href=\"http://www.sciencedirect.com/science/article/pii/030438009390045T\">' \
             'Gobas, F.A.P.C. (1993). A model for predicting the bioaccumulation of hydrophobic organic chemicals in aquatic food-webs: application to Lake Ontario. Ecological Modelling, 69(1-2), 1-17.</a></li>' \
             '<li><a href=\"http://www.sciencedirect.com/science/article/pii/S0269749100001627\">' \
             'Mackay, D. & Fraser, A. (2000). Bioaccumulation of persistent organic chemicals: mechanisms and models. Environmental Pollution, 110(3), 375-391.</a></li>' \
             '<li><a href=\"http://link.springer.com/article/10.1007%2Fs00216-012-6139-8?LI=true\">' \
             'Wang, J. & Gardinali, P.R. (2012). Analysis of selected pharmaceuticals in fish and the fresh water bodies directly affected by reclaimed water using liquid chromatography-tandem mass spectrometry. Analytical and bioanalytical chemistry.</a></li>' \
             '</ul>'

