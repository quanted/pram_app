"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<h3>1. Introduction</h3>' \
            '<p>' \
            'In conducting ecological risk assessments, EPA currently uses birds as surrogates for terrestrial-phase amphibians and reptiles. However, birds are likely to consume more food than amphibians or reptiles on a daily dietary intake basis, assuming similar caloric content of the food items. This difference is evident by comparing the estimated caloric requirements for free-living iguanid lizards (Iguanidae) to those of passerines (U.S. EPA, 1993):' \
            '</p>' \
            '<img src = \"/pram/static/images/latex/therps/therps_image1.png\">' \
            '<p>' \
            'Given the similar exponents on the allometric functions, the free-living metabolic rate of birds can be 40 times higher than reptiles of similar weight, with differences narrowing as body weight increases. Consequently, use of an avian food intake allometric equation as a surrogate to herptiles is likely to result in an over-estimation of exposure for reptiles and terrestrial-phase amphibians.' \
            '</p>' \
            '<p>' \
            'Because there was a need to evaluate dietary exposure to terrestrial-phase amphibian species (e.g., California red-legged frog, CRLF) and other amphibians and reptiles, EPA developed the terrestrial model T-HERPS. In developing T-HERPS, T-REX (version 1.3.1) was modified to allow for an estimation of food intake for herptiles using the same basic procedure that T-REX uses to estimate avian food intake.' \
            '</p>' \
            '<p>' \
            'Although this version of T-HERPS may be used to evaluate both reptiles and terrestrial-phase amphibians, some of the guidance presented in this document focuses on assessment of the CRLF, given the current need to assess exposures and associated risks to this species.' \
            '</p>' \
            '<h3>2. Summary of Changes in TREX to Allow for Food Intake Estimation for Herptiles</h3>' \
            '<p><b>2.1 Food Intake Allometric Equation</p></b>' \
            '<p>Daily food ingestion for herptiles (Nagy, 1987 as cited in U.S. EPA, 1993):' \
            '</p>' \
            '<img src = \"/pram/static/images/latex/therps/therps_image2.png\">' \
            '<p>' \
            'The insectivore food intake equation was chosen to be consistent with the California red-legged frog diet. Therefore, this version of T-HERPS should not be used to estimate potential exposures to herbivores. Instead, it is used to estimate the food ingestion rate of herpetofauna. It is assumed that since both reptiles and amphibians are poikilothermic, they have similar caloric requirements.' \
            '</p>' \
            '<p><b>2.2 Addition of small mammals and amphibians as potential dietary items</b></p>' \
            '<p>' \
            'There is uncertainty in estimated exposure concentrations (EEC) resulting from consumption of contaminated prey species; therefore, simplifying assumptions were made in T-HERPS that likely result in a conservative estimate of exposure in most cases. EECs resulting from consumption by herpetofauna (e.g., CRLF) of small mammals and herpetofauna (e.g., prey) that have consumed contaminated food items are estimated using procedures outlined below.' \
            '</p>' \
            '<p><b>2.2.1 EECs from Consumption of Prey Herpetofauna</b></p>' \
            '<p>' \
            'In order to assess potential exposures to CRLF via consumption of a pesticide contained in herpetofauna, concentrations of the pesticide in the prey item must first be estimated. The basis for the herpetofaunal prey item EEC is the oral daily dose for the prey item. Daily dose is calculated using methodology in T-REX (v. 1.3.1) with incorporation of the equation in Section 2. The prey herptile is assumed to eat small insects. Then, assuming the entire prey species is consumed, the daily dose calculated for the prey herptile species (mg/kg-bw) is equal to the dietary exposure concentration (mg/kg-food item = ppm). Therefore, the resulting estimated dietary concentration in small prey amphibians (ppm) can be used in the same manner as other standard food items represented in T-REX (plants, insects, fruits, etc., with estimates of residue levels from the Kenaga nomogram) to estimate potential dose-based exposures. In other words, exposure is a function of residue level in the prey item and food intake of the assessed species.' \
            '</p>' \
            '</p>' \
            'For the CRLF assessment, the weight of the prey item was based on data for the Pacific tree frog (Pseudacris regilla), which has been reported to be a dietary item of the CRLF (CA OEHHA, 1999). The user can alter the weight of the prey amphibian as needed for species specific assessments.' \
            '</p>' \
            '<p><b>2.2.2 EECs from Consumption of Prey Mammals</b></p>' \
            '<p>' \
            'For mammals that serve as prey to the CRLF, an alternative method for estimating exposure (EECs) is used. This alternative method is necessary because the weight of a small mammal that may be consumed is larger than the estimated daily food intake, resulting in an underestimation of acute exposures. Two mammalian EECs are calculated by T-HERPS by assuming the prey mammal consumes either' \
            '</p>' \
            '<ol>' \
            '<li>short grass or</li>' \
            '<li>large insects</li>' \
            '</ol>' \
            '<p>' \
            'Potential exposures from consumption of contaminated mammals is calculated in T-HERPS using the following steps:' \
            '</p>' \
            '<ol>' \
            '<li>estimated daily dose for a mammal (mg/kg-bw) of user defined size is calculated using methodology identical to that incorporated into T-REX (version 1.3.1)</li>' \
            '<li>the mass of pesticide consumed (mg) by the assessed species is calculated by multiplying the weight of the prey item (kg-bw) by the dose in the prey item (mg/kg-bw)</li>' \
            '<li>the resulting EEC (mg/kg-bw) for the assessed herpetofaunal species is then calculated as the pesticide mass consumed (mg/bw of assessed species (kg-bw) )</li>' \
            '</ol>' \
            '<p>' \
            'Uncertainties associated with this calculation are discussed in Section 4. The assessor may choose the body weight of the prey item consumed by the assessed species. For the CRLF, prey mammals are assumed to be 35 grams, which is the high-end weight of a deer mouse (U.S. EPA, 1993). However, alternative body weights can be entered to evaluate the potential effect of body weight on EECs and RQs (discussed further in Section 4).' \
            '</p>' \
            '<p><b>2.3 Water content of food items</p></b>' \
            '<p>' \
            'Water content of potential food items is used to convert the dry weight food intake estimate to wet weight for use in equation of Section 2. Water contents of various potential food items of wildlife are reported in Tables 4-1 and 4-2 of U.S. EPA (1993). Given that availability of particular food items will vary across locations and time, the use of the highest mean water content of the taxonomic group (e.g., terrestrial invertebrates) consumed by the assessed species is recommended at this time. For the CRLF, water content of terrestrial-phase insects (69% water; U.S. EPA, 1993) is used in the dose calculation for small terrestrial-phase CRLFs, and a water content of terrestrial herptiles (85% water; U.S. EPA, 1993) is used for the dose-calculation for larger terrestrial-phase CRLFs.' \
            '</p>' \
            '<p><b>2.4 Body Weight of Assessed Animals</p></b>' \
            '<p>' \
            'In the T-HERPS calculation, up to three body weights of herpetofauna can be entered. They are referred to as small, medium, and large animals in T-HERPS; however, any three values may be entered. Fewer than three values may also be entered.' \
            '</p>' \
            '<p>' \
            'For the CRLF, data from Fellers (2007) summarized in Table 1 below were used to define the range of terrestrial-phase red-legged frog body weights that are used as default body weights. Frogs collected by Fellers (2007) were collected from Point Reyes National Seashore and may not be reflective of the range of weights for the species over its entire range. However, these data are considered the best available information for the species.' \
            '</p>' \
            '<table border=\"1\">' \
            '<caption>' \
            '<b>Table 1<br />' \
            '<b>Summary Statistics</b><br />' \
            '<b>for California Red-Legged Frog Size Data</b><br />' \
            '<b>(Fellers (2007))</b>' \
            '</caption>' \
            '<thead>' \
            '<tr>' \
            '<th colspan=\"3\" scope=\"colgroup\">Number of Observations (N) = 545</th>' \
            '</tr>' \
            '<tr>' \
            '<th scope=\"col\">Statistic</th>' \
            '<th scope=\"col\">Length (cm)</th>' \
            '<th scope=\"col\">Weight (g)</th>' \
            '</tr>' \
            '</thead>' \
            '<tbody>' \
            '<tr>' \
            '<th scope=\"row\">Mean</th>' \
            '<td>6.1</td>' \
            '<td>37</td>' \
            '</tr>' \
            '<tr><th scope=\"row\">SD</th>' \
            '<td>3.7</td>' \
            '<td>43</td>' \
            '</tr>' \
            '<tr>' \
            '<th scope=\"row\">Minimum</th>' \
            '<td>2.5</td>' \
            '<td>1.4</td>' \
            '</tr>' \
            '<tr>' \
            '<th scope=\"row\">Median</th>' \
            '<td>4.7</td>' \
            '<td>9.9</td>' \
            '</tr>' \
            '<tr>' \
            '<th scope=\"row\">Maximum</th>' \
            '<td>13</td>' \
            '<td>238</td>' \
            '</tr>' \
            '</tbody>' \
            '</table>' \
            '<p>' \
            'These body weights are also used by the risk assessor to provide insight into the relevance of some ' \
            'food items. For example, terrestrial phase CRLFs reported by Fellers (2007) were as small as ' \
            'approximately 1 gram. It is unlikely that a small mammal will be consumed by a 1 gram frog. ' \
            'Therefore, RQs are not calculated for small terrestrial phase herpetofauna that consume mammals. ' \
            'Therefore, RQs in the summary tables of the' \
            '</p>' \
            '<h3>References</h3>' \
            '<li>' \
            'U.S. EPA (1993). Wildlife Exposure Factors Handbook. EPA/600/R-93/187. Office of Research and Development. December, 1993.' \
            '</li>' \
            '<li>' \
            'Nagy, K. A. (1987). Field metabolic rate and food requirement scaling in mammals and birds. Ecol. Monogr. 57: 111-128.' \
            '</li>' \
            '<li>' \
            'California OEHHA (Office of Environmental Health Hazard Assessment). (1999). The California Wildlife Biology, Exposure Factor, and Toxicity Database (Cal/Ecotox). Exposure Factors for Pacific Treefrog (Hyla regilla).' \
            '</li>' \
            '<li>' \
            'Fellers, G. (2007). Personal communication between Gary Fellers (Western Ecology Research Center of USGS and Thomas Steeger (U.S. EPA) via email' \
            '</li>'

#model description html for description page
description = '<p>Terrestrial Herpetofaunal Exposure Residue Program Simulation ' \
              '(T-HERPS) is designed to estimate dietary exposure and risk to ' \
              'terrestrial-phase amphibians and reptiles from pesticide use.  ' \
              'Historically, risk assessments for terrestrial-phase amphibians ' \
              'and reptiles have been estimated from models using avian toxicity ' \
              'data.  T-HERPS was developed to more accurately estimate amphibian ' \
              'and reptile exposure risk by including lower metabolic rates and ' \
              'dietary requirements that are associated with poikilothermic organisms.  ' \
              'When terrestrial-phase amphibian or reptile data is unavailable, avian ' \
              'toxicity data can be used in T-HERPS although output estimates should be ' \
              'interpreted cautiously.</p>' \
              '<p>An allometric function in T-HERPS allows for food intake to be ' \
              'estimated from the body size of the study animal.  The associated equation ' \
              'is based on food ingestion rates of an iguanid lizard, an insectivorous ' \
              'reptile with dietary habits similar to the California red-legged frog, and ' \
              'therefore should not be used for strictly herbivorous reptiles and amphibians.  ' \
              'For species that consume larger prey, such as other amphibians, reptiles or small ' \
              'mammals, alternative methods for determining EECs are included in T-HERPS.</p>' \
              '<p>Food intake estimates are provided in units of kg-diet/day by size class ' \
              '(small, medium, large).  Daily doses of pesticides to the study animal are ' \
              'given in units of mg/kg - bw by size class and food type.  Using the daily ' \
              'dose estimates, T-HERPS calculates the mass of the pesticide potentially ' \
              'consumed for EEC determinations.  Input estimates of food water content are ' \
              'required for calculation of pesticide intake.</p>'

# How model name appears on web page
header = 'T-HERPS'

history = '<p>User History</p>'

references = '<p>' \
             'Specific EPA guidance and the Microsoft Excel version of the model on the T-Herps Program can be found here:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/models-pesticide-risk-assessment#t-herps\">T-Herps Documentation</a></li>' \
             '<li><a href=\"http://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/t-herps-version-10-users-guide-risk-amphibians-and\">User\'s Guide</a></li>' \
             '<li><a href=\"http://www.epa.gov/sites/production/files/2016-11/t-herps_v._1.0_may_15_2007.xls\">T-Herps Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://github.com/quanted/pram_app/tree/master/models/therps\">pram_app on GitHub</a></li>' \
             '<li><a href=\"http://github.com/quanted/pram/tree/master/pram/therps\">pram on GitHub</a></li>' \
             '</ul>' \
             'Example reports documenting the use of T-Herps in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.3144&amp;rep=rep1&amp;type=pdf\">Metolachlor- Delta Smelt and California Tiger Salamander</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how T-Herps fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
             '</p>' \
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
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including T-Herps.' \
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

