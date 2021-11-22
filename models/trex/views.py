"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<img src = \"/pram/static/images/latex/trex/trex_image1.png\">' \
            '<img src = \"/pram/static/images/latex/trex/trex_image2.png\">' \
            '<img src = \"/pram/static/images/latex/trex/trex_image3.png\">'

#model description html for description page
description = '<p>This spreadsheet-based model calculates the residues on ' \
              'avian and mammalian food items (e.g., short or tall grass, ' \
              'seeds, insects, etc) along with the dissipation rate of a ' \
              'chemical applied to foliar surfaces (for single or multiple ' \
              'applications) in order to estimate acute and reproductive ' \
              'risk quotients.  T-REX offers two unique advantages over similar ' \
              'models: 1) the relative body weight of the animal under assessment, ' \
              'as compared to the test animal, is used to adjust acute and chronic ' \
              'toxicity values and 2) risk quotients are calculated for granular ' \
              'applications and seed treatments.  Output for both avian and mammalian ' \
              'diet- and dose-based EEC and RQs are based on upper bound and mean ' \
              'Kenaga values.</p>' \
              '<p>T-REX users enter specified endpoint data obtained from avian or ' \
              'mammal acute oral LD<sub>50</sub>, acute dietary LC<sub>50</sub>, or ' \
              'reproductive NOAEC/L toxicity studies to calculate risk quotients.  ' \
              'Users must also choose a test species from a drop-down menu.  For avian ' \
              'models, bobwhite quail and mallard duck data is commonly used.  If the ' \
              'body weight of a different test species is known, the user can choose ' \
              '\"other\" from the drop-down menu.  For mammalian models, the \"other\" ' \
              'option is not currently available, therefore, test species other than ' \
              'laboratory rats must be done by hand. </p>' \
              '<p>Estimates of LD<sub>50</sub> ft<sup>-2</sup> risk index values can be ' \
              'generated in T-REX for granular formations and row, banded and in-furrow ' \
              'applications.  An adjusted LD<sub>50</sub> toxicity value and EEC are used ' \
              'for the LD<sub>50</sub> ft<sup>-2</sup> calculation which is then compared ' \
              'to a specific level of concern (LOC).</p>'

# How model name appears on web page
header = 'T-REX 1.5.2'

history = '<p>User History</p>'





references = '<p>' \
             'Specific EPA guidance and the Microsoft Excel version of the model on the T-Rex Program can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/t-rex-version-15-users-guide-calculating-pesticide">T-Rex (1.5.1) Documentation</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/t-rex-version-15-users-guide-calculating-pesticide">User\'s Guide</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2015-06/trex_v1_5_2_webversion.xlsm">T-Rex Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/quanted/pram/tree/master/pram/trex">pram_src on GitHub (front end)</a></li>' \
             '<li><a href=\"https://github.com/quanted/pram/tree/master/pram/trex\">pram_src on GitHub (back end model)</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of T-Rex in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://archive.epa.gov/pesticides/chemicalsearch/chemical/foia/web/pdf/128008/128008-2010-12-23a.pdf">Boscalid</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.3144&amp;rep=rep1&amp;type=pdf">Metolachlor- Delta Smelt and California Tiger Salamander</a></li>' \
             '<li><a href=\"https://www3.epa.gov/pesticides/endanger/litstatus/effects/redleg-frog/aldicarb/esa_final.pdf">Aldicarb- California Red-legged frog</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.168.6045&rep=rep1&type=pdf">Atrazine- FIFRA Scientific Advisory Panel</a></li>' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2007-0431-0020">Reregistration Eligibility Decision for Mefluidide</a></li>' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2004-0307-0001">Chlorimuron-ethyl</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how T-Rex fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/risk/ecological-risk-assessment\">' \
             'EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/ecological-risk-assessment-pesticides-technical\">' \
             'EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"https://nepis.epa.gov/Exe/ZyNET.exe/40000006.TXT?ZyActionD=ZyDocument&Client=EPA&Index=2000+Thru+2005&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C00thru05%5CTxt%5C00000002%5C40000006.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL\">Science Policy Handbook on Risk Characterization">' \
             'Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk">' \
             'EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2016-10/documents/pfam-whitepaper.pdf">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including T-Rex.' \
             '</p>' \
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
             '</p>' \
             'References on T-REX:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/t-rex-version-15-users-guide-calculating-pesticide">' \
             'Environmental Protection Agency (2012). User\'s Guide T-REX Version 1.5 (Terrestrial Residue EXposure model</a></li>' \
             '<li><a href=\"https://www.aphis.usda.gov/biotechnology/downloads/alfalfa/gealfalfa_deis_tesanalysis_ovrview.pdf">' \
             'Honegger, J.L., Mortensen, S.R., & Carr, K.H. (2008). Overview of the Analysis of Possible Risk to Threatened and Endangered Species Associated with use of glyphophosphate-containing herbicides in Alfalfa production (pp.1-27)</a></li>' \
             '<li><a href=\"https://www.researchgate.net/publication/46380657_Ecological_risk_of_anthropogenic_pollutants_to_reptiles_Evaluating_assumptions_of_sensitivity_and_exposure">' \
             'Weir, S.M., Suski, J.G., and Salice, C.J. (2010). Ecological risk of anthropogenic pollutants to reptiles: Evaluating assumptions of sensitivity and exposure. Environmental Pollution, 158(12), 3596-606.</a></li>' \
             'Environmental Protection Agency (2008). Risks of Permethrin Use to the Federally Threatened California Red-legged Frog (Rana aurora draytonii) and Bay Checkerspot Butterfly (Euphydryas editha bayensis), and the Federally Endangered California Clapper Rail (Rallus longirostris obsoletus), Salt Marsh Harvest Mouse (Reithrodontomys raviventris), and San Francisco Garter Snake (Thamnophis sirtalis tetrataenia)</a></li>' \
             '<li><a href=\"https://www3.epa.gov/pesticides/endanger/litstatus/effects/redleg-frog/permethrin/determination.pdf">' \
             '</ul>'

# '<h3>References</h3>'
# '<ul class=\"bullet\">' \
# '<li>Environmental Protection Agency (2012). User\'s Guide T-REX Version 1.5 (Terrestrial Residue EXposure model). http://www.epa.gov/oppefed1/models/terrestrial/trex/t_rex_user_guide.htm</li>' \
# '<li>Honegger, J.L., Mortensen, S.R., &amp; Carr, K.H. (2008). Overview of the Analysis of Possible Risk to Threatened and Endangered Species Associated with use of glyphophosphate-containing herbicides in Alfalfa production (pp.1-27). Retrieved from http://www.aphis.usda.gov/biotechnology/downloads/alfalfa/gealfalfa_deis_tesanaysis_ovrview.pdf</li>' \
# '<li>Weir, S.M., Suski, J.G., and Salice, C.J. (2010). Ecological risk of anthropogenic pollutants to reptiles: Evaluating assumptions of sensitivity and exposure. Environmental Pollution, 158(12), 3596-606.</li>' \
# '<li>Environmental Protection Agency (2006). Reregistration Eligibility Decision for Metaldehyde. List A. Case No. 0576. http://www.epa.gov/opp00001/reregistration/REDs/metaldehyde_red.pdf</li>' \
# '<li>Environmental Protection Agency (2010). Risks of Metolachlor and S-Metolachlor Use to Federally Threatened Delta Smelt (<i>Hypomesus transpacificus</i>) and California Tiger Salamander (<i>Ambystoma californiense</i>) (Central California Distinct Population Segment) and Federally Endangered Sonoma County and Santa Barbara County Distinct Population Segments of California Tiger Salamander. 29 June 2010. </li>' \
# '<li>Environmental Protection Agency (2010). Environmental Fate and Ecological Risk Assessment for Boscalid New use on Rapeseed, Including Canola (Seed Treatment). 23 December 2010. http://www.epa.gov/opp00001/chem_search/cleared_reviews/csr_PC-128008_23-Dec-10_a.pdf</li>' \
# '<li>Environmental Protection Agency (2008). Risks of Permethrin Use to the Federally Threatened California Red-legged Frog (<i>Rana aurora draytonii</i>) and Bay Checkerspot Butterfly (<i>Euphydryas editha bayensis</i>), and the Federally Endangered California Clapper Rail (<i>Rallus longirostris obsoletus</i>), Salt Marsh Harvest Mouse (<i>Reithrodontomys raviventris</i>), and San Francisco Garter Snake (<i>Thamnophis sirtalis tetrataenia</i>)' \
# 'http://www.epa.gov/oppfead1/endanger/litstatus/effects/redleg-frog/permethrin/determination.pdf</li>' \
# '<li>Environmental Protection Agency (2008). Risks of Phorate use to Federally Threatened California Red-legged Frog (<i>Rana aurora draytonii</i>) to Federally Threatened Valley Elderberry Loghorn Beetle (<i>Desmocerus californicus dimphorus</i>) to Federally Threatened Bay Checkerspot Butterfly (<i>Euphydryas editha bayensis</i>) to Federally Endangered San Joaquin Kit Fox (<i>Vulpes macrotis mutica</i>). 10 October 2008. http://www.epa.gov/espp/litstatus/effects/redleg-frog/phorate/determination.pdf</li>' \
# '</ul>'