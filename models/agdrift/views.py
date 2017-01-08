"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in a template loading database

#model algorithm html for algorithm page
algorithm = '<p>The AgDRIFT model is both a mechanistic and empirical model which is ' \
            'used to evaluate off-site deposition of pesticides applied by aerial, ground, ' \
            'and orchard airblast spraying methods. For the aerial application scenarios, ' \
            'AgDRIFT outputs are mathematically based on a Lagrangian approach to the solution ' \
            'of the spray material equations of motion (see Teske et al. 2002). The Tier I ' \
            'aerial analysis curves are based on a user selected drop size classification, ' \
            'standard label assumptions and a default set of model parameters including the ' \
            'aircraft, aircraft operation, nozzle setup, meteorology, test substance and substance ' \
            'application.</p>' \
            '<p>For Tier I ground and orchard application types the deposition curves were ' \
            'created from the Spray Drift Task Force field data. Spray material from aircraft is ' \
            'modelled as a discrete set of droplets, categorized by the drop size. Drop size is ' \
            'defined by volume average diameter and volume fraction of the total sprayed materials. ' \
            'For all droplets the drop flight path is calculated as a function of time after release ' \
            'and includes the interaction with the turbulance in the environment. Equations used ' \
            'for calculation of deposition for ground and orchard application types are below:</p>' \
            '<p>The motion of the spray droplets is modeled using the lagrangian equations governing ' \
            'the behavior of a droplet in motion</p> ' \
            '<img src=\"/static_qed/images/latex/agdrift/agdrift_image1.png\">' \
            '<p>The evaporation model in AgDRIFT is based on the D-aquared law, which describes the ' \
            'time rate of change of drop diamter. This is described by:</p>' \
            '<img src=\"/static_qed/images/latex/agdrift/agdrift_image2.png\">' \
            '<p>Aircraft speed, weight, and thrust are all incorporated into the calculations of drift ' \
            'using flow field modeling.When the sprayed material nears the ground, ground deposition ' \
            'begins and continues until all evaporated material is deposited. Ground deposition is ' \
            'calculated by assuming that the concentration of material around the mean maybe be taken ' \
            'as Gaussian. </p>' \
            '<img src=\"/static_qed/images/latex/agdrift/agdrift_image3.png\">'

#model description html for description page
description = '<p>The primary function of AgDRIFT is to calculate the downward ' \
              'drift and deposition of pesticides and the magnitude of buffer ' \
              'zones needed to protect sensitive aquatic and terrestrial habitats. ' \
              'The Tier I model methodology uses different application type and drop ' \
              'size distributions to yield a conservative exposure estimate. Application ' \
              'type options in AgDRIFT include aerial, ground, and orchard/airblast. ' \
              'The aerial application model of spray drift is based on both mechanistic ' \
              'models and field data. The model outputs for ground and orchard/airblast ' \
              'models are based solely on field data. </p>'

# How model name appears on web page
header = 'AgDrift'

history = '<p>User History</p>'

references = '<p>The web page for the Spray Drift Task Force, specific EPA guidance and the executable ' \
             'version of the model on the AgDrift Program can be found here:</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agdrift.com/\">AgDrift Task Force</a></li>' \
             '<li><a href=\"http://www.epa.gov/oppefed1/models/terrestrial/terrplant/terrplant_user_guide.html\">' \
             'Users Guide</a></li>' \
             '<li><a href=\"http://www.agdrift.com/AgDRIFt2/DownloadAgDrift2_0.htm\">AgDrift Availability</a></li>' \
             '<li><a href=\"http://www.agdrift.com/PDF_FILES/Version%20Control.pdf\">AgDrift Version Changes</a></li>' \
             '</ul>' \
             '<p>Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_eco/tree/master/models/agdrift\">' \
             'ubertool_src on github (front end)</a></li>' \
             '<li><a href=\"https://github.com/puruckertom/ubertool_ecorest/tree/master/REST_UBER/agdrift_rest\">' \
             'ubertool_src on github (back end model)</a></li>' \
             '</ul>' \
             '<p>Example reports documenting the use of TerrPlant in reregistration eligibility documents ' \
             'and pesticide effects determinations for federally threatened and endangered species:</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.3144&rep=rep1&type=pdf\">' \
             'Metolachlor- Delta Smelt and California Tiger Salamander</a></li>' \
             '<li><a href=\"http://epa.gov/espp/litstatus/effects/redleg-frog/aldicarb/esa_final.pdf\">' \
             'Aldicarb- California Red-legged frog</a></li>' \
             '<li><a href=\"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.168.6045&rep=rep1&type=pdf\">' \
             'Atrazine- Freshwater Mussel</a></li>' \
             '<li><a href=\"http://op.bna.com/env.nsf/id/jstn-8van2d/$File/Atrazine%20Report.pdf\">' \
             'Atrazine- FIFRA Scientific Advisory Panel<a></li>' \
             '<li><a href=\"http://www.epa.gov/oppsrrd1/REDs/mefluidide_red.pdf\">' \
             'Reregistration Eligibility Decision for Mefluidide</a></li>' \
             '<li><a href=\"http://www.epa.gov/espp/litstatus/effects/24d/attachment-b.pdf\">' \
             'Reregistration Eligibility Document for 2,4-D</a></li>' \
             '<li><a href=\"http://www.blm.gov/pgdata/etc/medialib/blm/wo/Planning_and_Renewable_Resources/' \
             'veis.Par.99022.File.dat/AgDrift%20Model.pdf\">AgDrift Modeling for Human Health Risk Assessment</a>' \
             '</ul>' \
             '<p>Example reports for the use of PRZM in NOAA consultations with the EPA (Endangered Species ' \
             'Act Section 7 Consultations) concerning the impact of pesticides on listed species:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/consultation/opinions/biop_thiobencarb.pdf\">' \
             'Thiobencarb</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/consultations/pesticides_batch5opinion.pdf\">' \
             'Biological Opinion 5 (Oryzalin,Pendimethalin,Trifluralin)</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/consultations/pesticide_opinion4.pdf\">' \
             'Biological Opinion 4 (2,4-D, Triclopyr BEE, Diuron, Linuron, Captan, Chlorothalonil)</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/final_batch_3_opinion.pdf\">' \
             'Biological Opinion 3 (Azinphos methyl, Bensulide, Dimethoate, Disulfoton, Ethoprop, Fenamiphos, ' \
             'Naled, Methamidophos, Methidathion, Methyl parathion, Phorate and Phosmet)</a>' \
             '<li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/carbamate.pdf\">Biological Opinion 2 (Carbaryl, ' \
             'Carbofuran, and Methomyl)</a><li><a href=\"http://www.nmfs.noaa.gov/pr/pdfs/pesticide_biop.pdf\">' \
             'Biological Opinion 1 (Chlorpyrifos, Diazinon, and Malathion)</a>' \
             '</ul>' \
             '<p>' \
             'General EPA guidance on how AgDrift fits into the overall ecological risk assessment process for ' \
             'pesticides can be found at the following links:' \
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
             '<li><a href=\"http://www.epa.gov/pesticides/science/efed/policy_guidance/team_authors/' \
             'endangered_species_reregistration_workgroup/esa_conceptual_model_pf.htm\">' \
             'EPA Development of Conceptual Models</a></li>' \
             '<li><a href=\"http://www.agdrift.com/PDF_FILES/Ground.pdf\">' \
             'A Summary of Ground Application Studies</a></li>' \
             '</ul>' \
             '<p>' \
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment ' \
             'models, including AgDrift.' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf\">' \
             'Advancements in Endangered Species Act Effects Determination for Pesticide Registration Actions, ' \
             'Ed Odenkirchen (USEPA)</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf\">' \
             'Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/File.ashx?cid=199\">' \
             'Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"http://training.fws.gov/EC/Resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf\">' \
             'EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">' \
             'Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"http://pep.wsu.edu/wrpm/WRPM_11_files/Agenda%20and%20PPT%20pdfs/13Brady5-18-11PM.pdf\">' \
             'Ecological Risk Assessment and Improving Evaluation Tools, Don Brady (USEPA)</a></li><li><a href=\"www.cdpr.ca.gov/docs/enforce/drftinit/confs/2001/esterly.ppt\">AgDrift Training, Dave Easterly, Environmental Focus, Inc\"' \
             '<li><a href=\"http://tpsalliance.org/conference/sessions/2B_Hewitt_Droplet%20Size%20Calculators.pdf\">' \
             'Atomization Models for Actual Tank Mixes, Andrew Hewitt, University of Queensland</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">' \
             'Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a>' \
             '</li></ul>' \
             '<p>' \
             'Peer reviewed literature on AgDrift:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://nctc.fws.gov/EC/Resources/pesticides/Risk%20Assessment/agdispevaluationETC.pdf\">' \
             'Bird, S.L., Perry, S.G., Ray, S.L., & Teske, M.E. 2002. Evaluation of the AgDISP aerial spray algorithms ' \
             'in the AgDRIFT model. Environmental Toxicology and Chemistry. 21(3):672-681.</a></li>' \
             '<li><a href=\"http://training.fws.gov/branchsites/csp/resources/pesticides/risk%20assessment/agdriftestimatesetc.pdf\">' \
             'Teske, M.E., Bird, S.L., Esterly, D.M., Curbishley, T.B., Ray, S.L., Perry, S.G. 2002. ' \
             'AgDrift: A model for estimating near-field spray drift from aerial applications. Environmental Toxicology and Chemistry. 21(3):659-671.</a></li>' \
             '<li>Hewitt, A.J., Johnson, D.R., Fish, J.D., Hermansky, C.G., Valcore, D.L. 2002. Development of the spray drift task force database for aerial applications. Environmental Toxicology and Chemistry. 21(3):648-658.</li>' \
             '<li><a href=\"http://www.ecotox.org.au/aje/archives/vol8no2p3.pdf\">' \
             'Hewitt, A.J., Teske, M.E., Thistle, H.W., 2002. The Development of the AgDrift Model for Aerial Applications from Helicopters and Fixed-Wing Aircraft.' \
             'Australasian Journal of Ecotoxicology, 8:3-6.</a></li>' \
             '<li><a href=\"http://www.ecotox.org.au/aje/archives/vol8no2p7.pdf\">' \
             'Hewitt, A.J., 2002. The Practical Use of Agdrift and other Drift Exposure Models for Aerial, Ground, and Orchard Spray Applications,' \
             'Australasian Journal of Ecotoxicology, 8:7-19.</a></li>' \
             '<li><a href=\"http://www.aab.org.uk/contentok.php?id=183\">' \
             'Birchfield, N. B., 2004. Pesticide spray drift and ecological risk assessment in the US EPA: A comparison between current default spray drift deposition levels and AgDRIFT predictions in screening-level risk assessments.' \
             'Aspects of Applied Biology, 71, 125-132.</a></li>' \
             '</ul>'

