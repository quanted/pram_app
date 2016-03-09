# """
# .. module:: views
#    :synopsis: A useful module indeed.
# """
#
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests

hwbi_server = os.environ['REST_SERVER_8']

# ################ How model name appears on web page ################
header = 'HWBI'


# ####################################################################
#

def hwbi_view(request):
    html = render_to_string('index.html', {})
    response = HttpResponse()
    response.write(html)

    return response


def get_default_HWBI_values(request):
    if request.method == 'GET':
        # Django converts GET url arguments into a dictionary available through request.GET
        state = request.GET['State']
        county = request.GET['County']
        try:
            response = requests.get(
                "http://134.67.114.8/hwbi/api/Baseline?State=%s&County=%s" % (state, county)
            )
        except Exception, e:
            print str(e)

        return HttpResponse(response.content, content_type="application/json")

    else:
        return HttpResponse({'error': 'Request must by GET'}, content_type="application/json")


def get_user_HWBI_values(request):
    if request.method == 'GET':
        # Django converts GET url arguments into a dictionary available through request.GET
        capitalinvestmentscore = request.GET['CapitalInvestmentScore']
        consumptionscore = request.GET['ConsumptionScore']
        employmentscore = request.GET['EmploymentScore']
        financescore = request.GET['FinanceScore']
        innovationscore = request.GET['InnovationScore']
        productionscore = request.GET['ProductionScore']
        redistributionscore = request.GET['ReDistributionScore']
        airqualityscore = request.GET['AirQualityScore']
        foodfoberandfuleprovisioningscore = request.GET['FoodFoberAndFuleProvisioningScore']
        greenspacescore = request.GET['GreenspaceScore']
        waterqualityscore = request.GET['WaterQualityScore']
        waterquantityscore = request.GET['WaterQuantityScore']
        activismscore = request.GET['ActivismScore']
        communicationscore = request.GET['CommunicationScore']
        communityandfaithbasedinitiativesscore = request.GET['CommunityAndFaithBasedInitiativesScore']
        educationscore = request.GET['EducationScore']
        emergencypreparednessscore = request.GET['EmergencyPreparednessScore']
        familyservicesscore = request.GET['FamilyServicesScore']
        healthcarescore = request.GET['HealthcareScore']
        justicescore = request.GET['JusticeScore']
        laborscore = request.GET['LaborScore']
        publicworksscore = request.GET['PublicWorksScore']
        connectiontonaturedomainweight = request.GET['ConnectionToNatureDomainWeight']
        culturalfulfillmentdomainweight = request.GET['CulturalFulfillmentDomainWeight']
        educationdomainweight = request.GET['EducationDomainWeight']
        healthdomainweight = request.GET['HealthDomainWeight']
        leisuretimedomainweight = request.GET['LeisureTimeDomainWeight']
        livingstandardsdomainweight = request.GET['LivingStandardsDomainWeight']
        safetyandsecuritydomainweight = request.GET['SafetyAndSecurityDomainWeight']
        socialcohesiondomainweight = request.GET['SocialCohesionDomainWeight']
        response = requests.get(
            "http://134.67.114.8/hwbi/api/HWBI?CapitalInvestmentScore=%s&ConsumptionScore=%s&EmploymentScore=%s&FinanceScore=%s&InnovationScore=%s&ProductionScore=%s&ReDistributionScore=%s&AirQualityScore=%s&FoodFoberAndFuleProvisioningScore=%s&GreenspaceScore=%s&WaterQualityScore=%s&WaterQuantityScore=%s&ActivismScore=%s&CommunicationScore=%s&CommunityAndFaithBasedInitiativesScore=%s&EducationScore=%s&EmergencyPreparednessScore=%s&FamilyServicesScore=%s&HealthcareScore=%s&JusticeScore=%s&LaborScore=%s&PublicWorksScore=%s&ConnectionToNatureDomainWeight=%s&CulturalFulfillmentDomainWeight=%s&EducationDomainWeight=%s&HealthDomainWeight=%s&LeisureTimeDomainWeight=%s&LivingStandardsDomainWeight=%s&SafetyAndSecurityDomainWeight=%s&SocialCohesionDomainWeight=%s"
            % (capitalinvestmentscore, consumptionscore, employmentscore, financescore, innovationscore, productionscore,
              redistributionscore, airqualityscore, foodfoberandfuleprovisioningscore, greenspacescore,
              waterqualityscore, waterquantityscore, activismscore, communicationscore,
              communityandfaithbasedinitiativesscore, educationscore, emergencypreparednessscore, familyservicesscore,
              healthcarescore, justicescore, laborscore, publicworksscore, connectiontonaturedomainweight,
              culturalfulfillmentdomainweight, educationdomainweight, healthdomainweight, leisuretimedomainweight,
              livingstandardsdomainweight, safetyandsecuritydomainweight, socialcohesiondomainweight)
        )

        return HttpResponse(response.content, content_type="application/json")

    else:
        return HttpResponse({'error': 'Request must by GET'}, content_type="application/json")
