"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'Bee-REX'

#model description html for description page
description = '<p>The Bee-REX model is a screening level tool that is intended for use in ' \
              'a Tier I risk assessment to assess exposures of bees to pesticides and to calculate ' \
              'risk quotients. This model is individual-based, and is not intended to assess exposures ' \
              'and effects at the colony-level (<i>i.e.,</i> for honeybees).</p>' \
              '<p>The Tier I exposure method is intended to account for the major routes of pesticide ' \
              'exposure that are relevant to bees (<i>i.e.,</i> through diet and contact). Exposure routes ' \
              'for bees differ based on application type. In the model, bees foraging in fields treated ' \
              'with a pesticide through foliar spray could potentially be exposed to the pesticide through ' \
              'direct spray as well through consuming contaminated food. For honeybees foraging in fields ' \
              'treated with a pesticide through direct application to soil (<i>e.g.,</i> drip irrigation), ' \
              'through seed treatments, or through tree injection, direct spray onto bees is not expected. ' \
              'For these application methods, pesticide exposure through consumption of residues in ' \
              'nectar and pollen are expected to be the dominant routes. Foraging honeybees may also be ' \
              'exposed to pesticides via contact with dust from seed treatments or via consumption of ' \
              'water from surface water, puddles, dew droplet formation on leaves and guttation fluid; ' \
              'however, the Bee-REX tool does not include quantification of exposures via these routes.</p>'

#model algorithm html for algorithm page
algorithm = '
<p>The estimated concentrations in pollen and nectar (EECs) are calculated using the following equations:</p>

<p>EEC of foliar spray applications:</p>
<img src = "/static/images/latex/beerex/fs_eec.png" alt="Beerex_1">

<p>EEC of soil applications:</p>
<img src = "/static/images/latex/beerex/soil_eec.png" alt="Beerex_2">

<p>EEC of seed treatment applications:</p>
<img src = "/static/images/latex/beerex/seed_eec.png" alt="Beerex_3">

<p>EEC of tree trunk applications:</p>
<img src = "/static/images/latex/beerex/tree_eec.png" alt="Beerex_4">

<p>where, </p>
<img src = "/static/images/latex/beerex/application_rate.png" alt="App Rate">
<img src = "/static/images/latex/beerex/log_kow.png" alt="Log kow">
<img src = "/static/images/latex/beerex/koc.png" alt="koc">
<img src = "/static/images/latex/beerex/mass_tree.png" alt="Tree mass">

<p>The total dose of individual bees (ug a.i./bee) is calculated using EEC calculations and consumption rates of
individual bees. In the instance when empirical EEC data is provided, the empirical EEC data is used to calculate total
dose of individual bees. Consumption rates of pollen and nectar (mg/day) are derived from Appendix 3, Table 2 of the
2014 Guidance for Assessing Pesticide Risks to Bees document:</p>'

history = '<p>User History</p>'

references = '<p>
Specific EPA guidance and the Microsoft Excel version of the model Bee-REX can be found here:
</p>
<ul class="bullet">
  <li><a href="http://www.epa.gov/oppefed1/models/terrestrial/index.htm#beerex" target="_blank">beerex Documentation</a></li>
  <li><a href="http://www.epa.gov/oppefed1/models/terrestrial/beerex/beerex_user_guide.html" target="_blank">User's Guide</a></li>
  <li><a href="http://www.epa.gov/oppefed1/models/terrestrial/beerex/beerex_v_1_0.xls" target="_blank">beerex Excel Implementation</a></li>
</ul>

<p>
Current github source code:
</p>
<ul class="bullet">
  <li><a href="https://github.com/puruckertom/ubertool_eco/tree/master/models/beerex target="_blank"">ubertool_src on github (front end)</a></li>
  <li><a href="https://github.com/puruckertom/ubertool_ecorest/tree/master/REST_UBER/beerex_rest" target="_blank">ubertool_src on github (back end model)</a></li>
</ul>

<p>
General EPA guidance on how Bee-REX fits into the overall ecological risk assessment process for pesticides can be found at the following links:
</p>
<ul class="bullet">
  <li><a href="http://www.epa.gov/oppfead1/endanger/consultation/ecorisk-overview.pdf" target="_blank">EPA Ecological Risk Assessment Process Overview</a></li>
  <li><a href="http://www.epa.gov/oppefed1/ecorisk_ders/" target="_blank">EPA Ecological Risk Assessment Technical Overview</a></li>
  <li><a href="nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=40000006.TXT" target="_blank">Science Policy Handbook on Risk Characterization</a></li>
  <li><a href="http://www.epa.gov/oppefed1/ecorisk_ders/toera_analysis_exp.htm" target="_blank">
EPA Ecological Risk Assessment Exposure Characterization</a></li>
  <li><a href="http://www.epa.gov/pesticides/science/efed/policy_guidance/team_authors/endangered_species_reregistration_workgroup/esa_conceptual_model_pf.htm" target="_blank">
EPA Development of Conceptual Models</a></li>
</ul>
<p>
Presentations/posters/abstracts/reports on the subject of EPA's ecological risk assessment models, including Bee-REX.
</p>
<ul class="bullet">
  <li><a href="http://www.agrodiv.org/documents/denver11/Endangered%20Species%20Act%20and%20Regulation/AGRO219_Odenkirchen_Edward.pdf" target="_blank">Advancements in Endangered Species Act Effects Determination
	for Pesticide Registration Actions, Ed Odenkirchen (USEPA)</a></li>
  <li><a href="http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/35_Parker_Ronald.pdf" target="_blank">
	Overview of Issues in Aquatic Exposure Modeling in the USEPA Office of Pesticide Programs, Environmental Fate and Effects Division, Don Brady and Ron Parker (USEPA)</a></li>
  <li><a href="http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf" target="_blank">Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>
  <li><a href="http://nctc.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf" target="_blank">EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>
  <li><a href="http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf" target="_blank">Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>
  <li><a href="http://www.nap.edu/catalog.php?record_id=18344" target="_blank">Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a></li>
</ul>'

