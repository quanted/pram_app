"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates

batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

algorithm = '<p></p>'

#model description html for description page
description = '<p>The Spatial Aquatic Model (SAM) is an exposure model d' \
              'esigned to simulate the magnitude, duration, and location ' \
              'of aquatic exposure concentrations of pesticides. Pesticide ' \
              'concentrations are estimated as a function of chemical properties, ' \
              'environmental factors, and crop/management practices. Outputs include ' \
              'pesticide exposure concentrations in a receiving water body at ' \
              'the watershed or basin level. Concentrations also can be compared to ' \
              'user-defined toxicity thresholds in output tables, maps, and summary ' \
              'histograms to characterize the duration, frequency, and location of ' \
              'exceedances.</p>' \
              '<p>SAM incorporates spatial heterogeneity of assessed drainage ' \
              'areas (soils, land cover, weather), instead of assuming a single, ' \
              'uniform watershed for high-end/protective exposures, as in previous ' \
              'regulatory models. Exposure concentrations are not limited to the ' \
              'standard farm pond or index reservoir, but represent actual water ' \
              'bodies within and across use areas. Output concentrations are ' \
              'aggregated at the outlet of each drainage basin (drinking water ' \
              'basin or HUC12 catchment). For ecological assessments, exposure ' \
              'estimates are based on the main channel within the HUC12. Drinking ' \
              'water exposure estimates are binned as static (lakes, reservoirs) ' \
              'or flowing (streams, rivers) water bodies.</p>' \
              '<p>Due to the national scale of this model, instead of routing ' \
              'flow from fields to stream channels to larger streams, flow is ' \
              'accumulated at the outlet (\"pour point\")  for the catchment of ' \
              'interest (HUC12 or drinking water basin). Daily flow estimates can ' \
              'be compared to stream gauge measurements and daily concentrations to ' \
              'monitoring datasets.</p>' \
              '<p>This is the alpha version of SAM.  Important routines including ' \
              'erosion, spray drift, irrigation, travel times beyond a \"dayshed\", ' \
              'and the application window (as a function of weather and crop stage) are ' \
              'in development.</p>' \
              '<p>Figure 1 shows the data inputs, organization, and model components of SAM.' \
              '</p>' \
              '<p>' \
              '<img src = \"/static_qed/images/sam_figure1.gif\" alt=\"SAM Model\">' \
              '</p>' \
              '<p>' \
              'Many of the data inputs and the hydrology are pre-processed to make exposure ' \
              'concentration calculations at this scale possible in a reasonable amount of ' \
              'time. Spatially, soils are grouped into classes based on important pesticide ' \
              'transport factors, weather data has been regridded to a common grid resolution ' \
              '(~24,000 km grids), land cover captures the prior 5 years of the Cropland ' \
              'Data Layer, crop inputs include a range of crops from an incorporated ' \
              'database, and the hydrology is based on NHD Plus v2 monthly mean flow dataset.' \
              '</p>' \
              '<p> Recipe files are used to create a list of soil-crop-weather units in each ' \
              'basin and the total area of each unit to be simulated. The one-dimensional solute ' \
              'transport routines in SAM are based on PRZM, but are structured differently ' \
              'by separating hydrology and chemical transport to reduce redundancy and increase ' \
              'computational speed. The approach consists of: Scenario Generator, which outputs ' \
              'the hydrology for sub watersheds using the curve number method (to estimate ' \
              'direct runoff and infiltration from rainfall events); Super PRZM Hydro, which ' \
              'sums the runoff (from all soil-crop-weather units) to represent the total ' \
              'daily runoff of an entire watershed; and Pesticide Transport and Water Body ' \
              'Concentration Calculator, which outputs the daily pesticide concentration in ' \
              'the receiving water body based on the transport, degradation, and washout of the ' \
              'pesticide mass.</p>'

# How model name appears on web page
header = 'SAM'

history = '<p>User History</p>'

references = '<p><ul class=\"bullet\">' \
             '<li><a href=\"http://sam-manual.s3-website-us-east-1.amazonaws.com/SAM_ubertool_user_manual_21Apr2015.pdf\">SAM User Manual' \
             '4/21/2015</a>' \
             '<li><a href=\"https://github.com/quanted/static_qed/blob/master/docs/SAM_Developmental_Manual\">' \
             'DEVELOPMENT OF A SPATIAL AQUATIC MODEL (SAM) FOR PESTICIDE ASSESSMENTS</a></li>' \
             '</ul>' \
             '</p>'\
             'Presentations/posters/abstracts/reports on the subject of EPA\'s ecological risk assessment ' \
             'models, including SAM.' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://www.cdpr.ca.gov/docs/emon/surfwtr/presentations/presentation_110.pdf\">' \
             'Spatially distributed modeling for pesticide assessments ' \
             'in surface water, and USEPA Spatial Aquatic Model</a></li>' \
             '<li><a href=\"http://www.agrodiv.org/documents/denver11/Evaluating%20Agrochemical%20Aquatic%20Exposure/19_Parker_Ronald.pdf\">' \
             'Exploring Approaches to Pesticide Aquatic Ecological Exposure Assessment:Issues in Evaluating Risk Across the National Landscape , Ron Parker (USEPA)</a></li>' \
             '<li><a href=\"http://www.complianceservices.com/wp-content/uploads/2013/06/Next-Steps-in-Endangered-Species-Risk-Assessments.pdf\">' \
             'Next Steps in Endangered Species Risk Assessments, Cliff Habig (Compliance Services International)</a></li>' \
             '<li><a href=\"https://nctc.fws.gov/resources/course-resources/pesticides/2011Presentations/Tab%2013%20%20Pesticide%20Risk%20Assessment.pdf\">' \
             'EPA Pesticide Ecological Risk Assessment Methods, Fish and Wildlife Service Training</a></li>' \
             '<li><a href=\"http://www.calcitrusquality.org/wp-content/uploads/2011/07/Prometryncasestudy.pdf\">' \
             'Minor Crop Farm Alliance Endangered Species Assessment Workshop- Prometryn Case Study</a></li>' \
             '<li><a href=\"https://www.epa.gov/risk/risk-tools-and-databases\">' \
             'Ecological Risk Assessment and Improving Evaluation Tools, Don Brady (USEPA)</a></li>' \
             '<li><a href=\"www.cdpr.ca.gov/docs/enforce/drftinit/confs/2001/esterly.ppt">AgDrift Training, Dave Easterly, Environmental Focus, Inc\"' \
             '<li><a href=\"http://tpsalliance.org/pdf/conference/2008/2B_Hewitt_Droplet%20Size%20Calculators.pdf\">' \
             'Atomization Models for Actual Tank Mixes, Andrew Hewitt, University of Queensland</a></li>' \
             '<li><a href=\"http://www.nap.edu/catalog.php?record_id=18344\">' \
             'Assessing Risks to Endangered and Threatened Species From Pesticides (National Academy of Sciences)</a>' \
             '</li></ul>' \
             '<p>'\
             'Peer reviewed literature on SAM:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"https://github.com/quanted/static_qed/blob/master/docs/SAM_ACS_Hoogeweg.pdf\">' \
             'Development of a spatial-temporal cooccurrence index to evaluate relative pesticide risks to threatened and endangered species</a></li>' \
             '</ul>'
