# """
# .. module:: views
#    :synopsis: A useful module indeed.
# """
#
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect
import requests


cyan_server = os.environ['REST_SERVER_8']

# ################ How model name appears on web page ################
header = 'Cyan'
# ####################################################################


def cyan_view(request):
    html = render_to_string('cyan/index.html', {})
    response = HttpResponse()
    response.write(html)

    return response


def get_default_cyan_values(request):
    if request.method == 'GET':
        # Django converts GET url arguments into a dictionary available through request.GET
        state = request.GET['State']
        county = request.GET['County']
        try:
            response = requests.get(
                cyan_server + "/cyan/api/Baseline?State=%s&County=%s" % (state, county)
            )
        except Exception, e:
            response = {'error': str(e)}

        return HttpResponse(response.content, content_type="application/json")

    else:
        return HttpResponse({'error': 'Request must by GET'}, content_type="application/json")


def get_user_cyan_values(request):
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
        foodfiberandfuelprovisioningscore = request.GET['FoodFiberAndFuelProvisioningScore']
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
            cyan_server + "/cyan/api/Cyan?CapitalInvestmentScore=%s&ConsumptionScore=%s&EmploymentScore=%s&FinanceScore=%s&InnovationScore=%s&ProductionScore=%s&ReDistributionScore=%s&AirQualityScore=%s&FoodFiberAndFuelProvisioningScore=%s&GreenspaceScore=%s&WaterQualityScore=%s&WaterQuantityScore=%s&ActivismScore=%s&CommunicationScore=%s&CommunityAndFaithBasedInitiativesScore=%s&EducationScore=%s&EmergencyPreparednessScore=%s&FamilyServicesScore=%s&HealthcareScore=%s&JusticeScore=%s&LaborScore=%s&PublicWorksScore=%s&ConnectionToNatureDomainWeight=%s&CulturalFulfillmentDomainWeight=%s&EducationDomainWeight=%s&HealthDomainWeight=%s&LeisureTimeDomainWeight=%s&LivingStandardsDomainWeight=%s&SafetyAndSecurityDomainWeight=%s&SocialCohesionDomainWeight=%s"
            % (capitalinvestmentscore, consumptionscore, employmentscore, financescore, innovationscore, productionscore,
              redistributionscore, airqualityscore, foodfiberandfuelprovisioningscore, greenspacescore,
              waterqualityscore, waterquantityscore, activismscore, communicationscore,
              communityandfaithbasedinitiativesscore, educationscore, emergencypreparednessscore, familyservicesscore,
              healthcarescore, justicescore, laborscore, publicworksscore, connectiontonaturedomainweight,
              culturalfulfillmentdomainweight, educationdomainweight, healthdomainweight, leisuretimedomainweight,
              livingstandardsdomainweight, safetyandsecuritydomainweight, socialcohesiondomainweight)
        )

        return HttpResponse(response.content, content_type="application/json")

    else:
        return HttpResponse({'error': 'Request must by GET'}, content_type="application/json")


# TODO: Remove all of this after Drupal testing is complete
################################################################
#              TEMPORARY VIEW PAGES                            #
################################################################

# def descriptionPage(request, model='cyan'):
#
#     text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'models/'+model+'/'+model+'_text.txt'), 'r')
#     xx = text_file2.read()
#     html = render_to_string('01uberheader.html', {
#             'site_skin' : os.environ['SITE_SKIN'],
#             'title': header+' Description'})
#     html = html + render_to_string('cyan/02uberintroblock_wmodellinks_cyan.html', {
#             'site_skin' : os.environ['SITE_SKIN'],
#             'model':model,
#             'page':'description'})
#     html = html + linksLeft.linksLeft()
#     html = html + render_to_string('04ubertext_start.html', {
#             'model_attributes': header+' Overview',
#             'text_paragraph':xx})
#     html = html + render_to_string('04ubertext_end.html', {})
#     html = html + render_to_string('05ubertext_links_right.html', {})
#     html = html + render_to_string('06uberfooter.html', {'links': ''})
#
#     response = HttpResponse()
#     response.write(html)
#     return response
#
#
# def algorithmPage(request, model='cyan'):
#
#     text_file1 = open(os.path.join(os.environ['PROJECT_PATH'], 'models/'+model+'/'+model+'_algorithm.txt'),'r')
#     x = text_file1.read()
#     html = render_to_string('01uberheader.html', {
#             'site_skin' : os.environ['SITE_SKIN'],
#             'title': header+' Algorithms'})
#     html = html + render_to_string('cyan/02uberintroblock_wmodellinks_cyan.html', {
#             'site_skin' : os.environ['SITE_SKIN'],
#             'model':model,
#             'page':'algorithm'})
#     html = html + linksLeft.linksLeft()
#     html = html + render_to_string('04uberalgorithm_start.html', {
#             'model_attributes': header+' Algorithms',
#             'text_paragraph':x})
#     html = html + render_to_string('04ubertext_end.html', {})
#     html = html + render_to_string('05ubertext_links_right.html', {})
#     html = html + render_to_string('06uberfooter.html', {'links': ''})
#
#     response = HttpResponse()
#     response.write(html)
#     return response
#
#
# def referencesPage(request, model='cyan'):
#
#     text_file1 = open(os.path.join(os.environ['PROJECT_PATH'], 'models/'+model+'/'+model+'_references.txt'),'r')
#     x = text_file1.read()
#     html = render_to_string('01uberheader.html', {
#             'site_skin' : os.environ['SITE_SKIN'],
#             'title': header+' References'})
#     html = html + render_to_string('cyan/02uberintroblock_wmodellinks_cyan.html', {
#             'site_skin' : os.environ['SITE_SKIN'],
#             'model':model,
#             'page':'references'})
#     html = html + linksLeft.linksLeft()
#     html = html + render_to_string('04uberreferences_start.html', {
#             'model_attributes': header+' References',
#             'text_paragraph':x})
#     html = html + render_to_string('04ubertext_end.html', {})
#     html = html + render_to_string('05ubertext_links_right.html', {})
#     html = html + render_to_string('06uberfooter.html', {'links': ''})
#
#     response = HttpResponse()
#     response.write(html)
#     return response
