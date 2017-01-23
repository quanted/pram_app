"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '' \
            '<p>The daily water intake rates for birds are calculated using allometric equations based on body weight:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image1.png\" alt=\"SIP_1\">' \
            '<p>For mammals the daily water intake rates are calculated below:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image2.png\" alt=\"SIP_2\">' \
            '<p>Dose from drinking water:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image3.png\" alt=\"SIP_3\">' \
            '<p>Adjusted acute toxicity values for birds:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image4.png\" alt=\"SIP_4\">' \
            '<p>Adjusted acute toxicity values for mammals:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image5.png\" alt=\"SIP_5\">' \
            '<p>Daily food intake rate:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image6.png\" alt=\"SIP_6\">' \
            '<p>Dose equivalent toxicity for birds:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image7.png\" alt=\"SIP_7\">' \
            '<p>Dose equivalent toxicity for mammals:</p>' \
            '<img src = \"/static_qed/images/latex/sip/sip_image8.png\" alt=\"SIP_8\">'

#model description html for description page
description = '<p>The SIP model is designed to estimate chemical exposure from ' \
              'drinking water alone in birds and mammals.  Dietary, dermal and ' \
              'respiratory pathways are not considered in this model and cannot ' \
              'be ruled out as additional sources of exposure.  For purposes of ' \
              'risk assessment, it is assumed that 100% of daily water needs are ' \
              'achieved through drinking water and that these needs are equivalent ' \
              'to the daily water flux rate.  The upper bound of exposure is ' \
              'estimated through the use of an allometric equation in daily water ' \
              'intake rate determination (units in mg/kg ? bw).  The equation also ' \
              'considers chemical water solubility.  Acute toxicity values are adjusted ' \
              'using LD<sub>50</sub> values while chronic toxicity is adjusted through ' \
              'NOAEC studies in birds and NOAEL data in mammals.  To determine whether ' \
              'drinking water poses a chemical risk to the study animal, users examine ' \
              'ratios of upper bound exposure estimates relative to either adjusted ' \
              'LD<sub>50</sub>, NOAEC or NOAEL values.</p>'

# How model name appears on web page
header = 'SIP'

history = '<p>User History</p>'

references = '<p>' \
             'Specific EPA guidance and the Microsoft Excel version of the model on the Screening Imbibition Program can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/sip-version-10-users-guide-pesticide-exposure-birds">SIP Documentation</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/sip-version-10-users-guide-pesticide-exposure-birds">User\'s Guide</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2015-06/sip_v_1_0.xls">SIP Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/quanted/ubertool_app/tree/master/models/sip"\">ubertool_src on github (front end)</a></li>' \
             '<li><a href=\"https://github.com/quanted/ubertool/tree/master/ubertool/sip">ubertool_src on github (back end model)</a></li>' \
             '</ul>' \
             '<p>Example reports documenting the use of SIP in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.regulations.gov/document?D=EPA-HQ-OPP-2012-0230-0005\">Atrazine- FIFRA Scientific Advisory Panel</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how SIP fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://www.epa.gov/risk/ecological-risk-assessment\">EPA Ecological Risk Assessment Process Overview</a></li>' \
             '<li><a href=\"https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/ecological-risk-assessment-pesticides-technical\">EPA Ecological Risk Assessment Technical Overview</a></li>' \
             '<li><a href=\"https://nepis.epa.gov/Exe/ZyNET.exe/40000006.TXT?ZyActionD=ZyDocument&Client=EPA&Index=2000+Thru+2005&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C00thru05%5CTxt%5C00000002%5C40000006.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL\">Science Policy Handbook on Risk Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk">EPA Ecological Risk Assessment Exposure Characterization</a></li>' \
             '<li><a href=\"https://www.epa.gov/sites/production/files/2016-10/documents/pfam-whitepaper.pdf">' \
             'EPA Development of Conceptual Models</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including SIP.' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\" target=\"_blank\">Advancements in Endangered Species Act Effects Determination' \
             'for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\" target=\"_blank\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://nctc.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>' \
             '</ul>'


