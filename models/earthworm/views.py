"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>For any particular environmental phase (e.g., water, soil, air, or biota) there ' \
            'is a corresponding \"fugacity capacity\" with units of mol/m<sup>3</sup>-Pa and is denoted ' \
            'by Z. The relationship between fugacity, fugacity capacity and chemical concentration (C) ' \
            'is defined by Equation 1.' \
            '</p>' \
            '<p>Equation 1. <img src = \"/pram/static/images/latex/earthworm/earthworm_image1.png\" ' \
            'alt=\"earthworm_1\"></p>' \
            '<p>' \
            'Fugacity capacities for a given chemical are calculated for the phases of interest as ' \
            'part of the exposure point estimation methodology (Mackay and Paterson 1981). The following ' \
            'calculations of fugacity capacity for water (Z<sub>W</sub>, soil (Z<sub>S</sub>) and ' \
            'earthworms (Z<sub>E</sub>) (Equation 2-4) require several chemical-specific parameters and ' \
            'assumptions of system temperature (25 &#8451;) and steady state equilibrium. Parameter values ' \
            'relevant to Equations 2-4 are defined in Table 1.</p>' \
            '<p>Equation 2. <img src = \"/pram/static/images/latex/earthworm/earthworm_image2.png\" ' \
            'alt=\"earthworm_2\"></p>' \
            '<p>Equation 3. <img src = \"/pram/static/images/latex/earthworm/earthworm_image3.png\" ' \
            'alt=\"earthworm_3\"></p>' \
            '<p>Equation 4. <img src = \"/pram/static/images/latex/earthworm/earthworm_image4.png\" ' \
            'alt=\"earthworm_4\"></p>' \
            '<p>Fugacity capacities for a given chemical are caculated for the phases of interest as part ' \
            'of the exposure point concentration estimation methodology. By definition, the ratio between Z ' \
            'values of different phases (compartments) equals the partitioning coefficient (for example, see ' \
            'Equation 5).' \
            '</p>' \
            '<p>Equation 5. <img src = \"/pram/static/images/latex/earthworm/earthworm_image5.png\" alt=\"earthworm_5\"></p>' \
            '<p>In this approach, it is assumed that a pesticide partitions between the soil, the (pore) water and the ' \
            'air contained within the soil of the treatment site. It is assumed that earthworms dwelling within the soil ' \
            'are exposed to a pesticide via ingestion of contaminated soil and pore-water (Belfroid et. al 1994). The ' \
            'concentration of a pesticide in earthworm tissues can be calculated according to Equation 6. The parameters of ' \
            'Equation 6 are defined in Table 1.' \
            '</p>' \
            '<p>Equation 6. <img src = \"/pram/static/images/latex/earthworm/earthworm_image6.png\" alt=\"earthworm_6\"></p>' \
            '<p>' \
            'Equation 6 can be redefined using equations 2-4 as follows in Equation 7. Equation 7 is used to calculate ' \
            'the concentration of a pesticide in earthworms inhabiting the soil of treatment sites.' \
            '</p>' \
            '<p>Equation 7. <img src = \"/pram/static/images/latex/earthworm/earthworm_image7.png\" alt=\"earthworm_7\"></p>' \
            '<p>L can be based on the lipid content of earthworms, which was assumed to be 0.01 (Cobb et al. 1995). The ' \
            'resulting C<sub>E</sub> value is in units of mol/m<sup>3</sup>. This value is converted to units of g/kg ' \
            'using Equation 8. The density of the earthworm (&#961;<sub>E</sub>) is assumed to be 1000kg/m<sup>3</sup> ' \
            '(equivalent to density of water). The resulting concentration of pesticide in earthworms denotes in ' \
            '(C<sub>E</sub><sup>*</sup>) of Equation 8.' \
            '</p><p>Equation 8. <img src = \"/pram/static/images/latex/earthworm/earthworm_image8.png\" alt=\"earthworm_8\"></p>' \
            '<p>Table 1. Summary of parameters relevant to earthworm fugacity model.</p>' \
            '<table border=\"1\">' \
            '<tr>' \
            '<th>Symbol</th>' \
            '<th>Definition</th>' \
            '<th>Units</th>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>E</SUB></td>' \
            '<td>Chemical concentration in earthworm tissue</td>' \
            '<td>mol/m<SUP>3</SUP></td>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>E</SUB><SUP>*</SUP></td>' \
            '<td>Chemical concentration in earthworm tissue</td>' \
            '<td>k/kg</td>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>S</SUB></td>' \
            '<td>Chemical concentration in soil</td>' \
            '<td>mol/m<SUP>3</SUP></td>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>W</SUB></td>' \
            '<td>Chemical concentration in pore water of soil</td>' \
            '<td>mol/m<SUP>3</SUP></td>' \
            '</tr><tr>' \
            '<td>H</td>' \
            '<td>Henry\'s Law constant</td>' \
            '<td>m<SUP>3</SUP>-Pa/mol</td>' \
            '</tr>' \
            '<tr>' \
            '<td>K<SUB>d</SUB></td>' \
            '<td>Soil partitioning coefficient</td>' \
            '<td>cm<SUP>3</SUP>/g</td>' \
            '</tr>' \
            '<tr>' \
            '<td>K<SUB>OW</SUB></td>' \
            '<td>Octanol to water partition coefficient</td>' \
            '<td>none</td>' \
            '</tr>' \
            '<tr>' \
            '<td>L</td>' \
            '<td>Lipid fraction of earthworm</td>' \
            '<td>none</td>' \
            '</tr>' \
            '<tr>' \
            '<td>MW</td>' \
            '<td>molecular weight of chemical</td>' \
            '<td>g/mol</td>' \
            '</tr>' \
            '<tr>' \
            '<td>Z<SUB>E</SUB></td>' \
            '<td>Fugacity capacity of pesticide in earthworms</td>' \
            '<td>mol/m<SUP>3</SUP>-Pa</td>' \
            '</tr>' \
            '<tr>' \
            '<td>Z<SUB>S</SUB></td>' \
            '<td>Fugacity capacity of pesticide in soil</td>' \
            '<td>mol/m<SUP>3</SUP>-Pa</td>' \
            '</tr>' \
            '<tr>' \
            '<td>Z<SUB>W</SUB></td>' \
            '<td>Fugacity capacity of pesticide in (pore) water</td>' \
            '<td>mol/m<SUP>3</SUP>-Pa</td>' \
            '</tr>' \
            '<tr>' \
            '<td>&#961;<sub>E</sub></td>' \
            '<td>Density of earthworm</td>' \
            '<td>kg/m<SUP>3</SUP></td>' \
            '</tr>' \
            '<tr><td>&#961;<sub>S</sub></td><td>Bulk density of soil</td>' \
            '<td>g/cm<SUP>3</SUP></td>' \
            '</tr>' \
            '</table>'

#model description html for description page
description = '<p>Earthworm Fugacity Modeling is a simple fugacity approach was employed ' \
              'to estimate pesticides concentrations in earthworms. Fugacity is most often r' \
              'egarded as the \"escaping tendency\" of a chemical from a particular phase. ' \
              'Fugacity has units of presure, generally pascals (Pa), and can be related ' \
              'to phase concentratons.</p>' \
              '<p>The T-REX model (USEPA 2008) is useful for assessing exposures of ' \
              'terrestrial animals to pesticide residues on foliar surfaces of crops ' \
              'and seeds. The model cannot be used to assess pesticide exposures to ' \
              'terrestrial animals resulting from consumption of earthworms contaminated ' \
              'with pesticide mass present in the soil of the application site. In order ' \
              'to explore the potential exposures of mammals to pesticides present in the ' \
              'soil and earthworms present on the treatment site, a simple fugacity approach ' \
              'was employed to estimate pesticides concentrations in earthworms. </p>'

# How model name appears on web page
header = 'Earthworm'

history = '<p>User History</p>'

references = '<p> Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://github.com/quanted/pram_app/tree/master/models/earthworm\">pram_app on GitHub' \
             '</a></li>' \
             '<li><a href=\"http://github.com/quanted/pram/tree/master/pram/earthworm\"> pram on GitHub' \
             '</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how Earthworm fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
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
             '</ul>'\
             '<p>' \
             'Peer reviewed literature on Earthworm:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://ac.els-cdn.com/S0147651383710146/1-s2.0-S0147651383710146-main.pdf?_tid=2e556034-e18c-11e6-b151-00000aacb35f&acdnat=1485190467_3330fd664a7b7f22894aacd6c688fb7d">' \
             'Belfroid, A., M. Sikkenk, W. Seinen, K.V. Gestel, J. Hermens. 1994. The toxicokinetic behavior of ' \
             'chlorobenzenes in earthworm (<i>Eisenia andrei</i>) experiments in soil. Environ. Toxicol. Chem. 13: 93-99.</a></li>' \
             '<li><a href=\"http://onlinelibrary.wiley.com/doi/10.1002/etc.5620140213/abstract?systemMessage=WOL+Usage+report+download+page+will+be+unavailable+on+Friday+27th+January+2017+at+23%3A00+GMT%2F+18%3A00+EST%2F+07%3A00+SGT+%28Saturday+28th+Jan+for+SGT%29++for+up+to+2+hours+due+to+essential+server+maintenance.+Apologies+for+the+inconvenience.">Cobb, G.P., E.H. Hol, P.W. Allen, J.A Gagne, R.J. Kendall. 1995. Uptake, metabolism, and toxicity of ' \
             'terbufos in the earthworm (<i>Lumbricus terrestris</i>) exposed to COUNTER-15G in artificial soils. ' \
             'Environ. Toxicol. Chem. 14(2): 279-285. </a></li>' \
             '<li><a href=\"http://pubs.acs.org/doi/pdf/10.1021/es00091a001">Mackay, D. and S. Paterson. 1981. Calculating fugacity. Environ. Sci. Technol. 15: 1006-1014.</a></li>' \
             '</ul>'

