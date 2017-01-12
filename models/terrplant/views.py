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
             '<li><a href=\"http://www.epa.gov/oppefed1/models/terrestrial/#terrplant\">TerrPlant Documentation</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/models/terrestrial/terrplant/terrplant_user_guide.html\">User\'s Guide</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/models/terrestrial/terrplant/terrplant_v1_2_2_oct_29_2009_webversion.xls\">TerrPlant Excel Implementation</a></li>' \
             '</ul>' \
             '<p>' \
             'Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_eco/tree/master/models/terrplant\">ubertool_src on GitHub (front end)</a></li>' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_ecorest/tree/master/REST_UBER/terrplant_rest\">ubertool_src on GitHub (back end model)</a></li>' \
             '</ul>' \
             '<p>' \
             'Example reports documenting the use of TerrPlant in reregistration eligibility documents and pesticide effects determinations for federally threatened and endangered species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.epa.gov/oppfead1/endanger/litstatus/effects/redleg-frog/2012/diazinon/analysis.pdf\">Diazinon- Delta Smelt and Tidewater Goby</a></li>' \
             '<li><a href=\"http://www.epa.gov/opp00001/chem_search/cleared_reviews/csr_PC-128008_23-Dec-10_a.pdf\">Boscalid</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.3144&amp;rep=rep1&amp;type=pdf\">Metolachlor- Delta Smelt and California Tiger Salamander</a></li>' \
             '<li><a href=\"http://epa.gov/espp/litstatus/effects/redleg-frog/aldicarb/esa_final.pdf\">Aldicarb- California Red-legged frog</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.168.6045&amp;rep=rep1&amp;type=pdf\">Atrazine- Freshwater Mussel</a></li>' \
             '<li><a href=\"http://op.bna.com/env.nsf/id/jstn-8van2d/$File/Atrazine%20Report.pdf\">Atrazine- FIFRA Scientific Advisory Panel</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppsrrd1/REDs/mefluidide_red.pdf\">Reregistration Eligibility Decision for Mefluidide</a></li>' \
             '<li><a href=\"http://www.epa.gov/pesticides/chem_search/cleared_reviews/csr_PC-128901_19-Aug-09_a.pdf\">Chlorimuron-ethyl</a></li>' \
             '<li><a href=\"http://www.epa.gov/espp/litstatus/effects/24d/attachment-b.pdf\">Reregistration Eligibility Document for 2,4-D</a></li>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how TerrPlant fits into the overall ecological risk assessment process for pesticides can be found at the following links:' \
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
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment models, including TerrPlant.' \
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

