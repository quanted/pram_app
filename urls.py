#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()


# All view functions here must be in '/views/views.py'
urlpatterns = patterns('views',
    url(r'^docs/', include('docs.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^api/ubertool/', include('api.urls')),
    (r'^rest/', include('REST.urls')),
    url(r'^ubertool/hwbi/', include('models.hwbi.urls')),
    (r'^ubertool/webice/', include('models.webice.urls')),
    # (r'^eco/test/?$', include('models.test.urls')),
    (r'^ubertool/login/auth/?$', 'misc.login_auth'),
    (r'^ubertool/login*', 'misc.login'),
    (r'^ubertool/ore/', include('models.ore.urls')),
    (r'^$', 'landing.ubertoolLandingPage'),
    (r'^geoserver/?$', 'geoserver.test_page'),
    (r'^geoserver/query/(?P<jid>\d{20})$', 'geoserver.sam_huc_query'),
    (r'^geoserver/sam_done/(?P<jid>\d{20})$', 'geoserver.sam_done_query'),
    (r'^ubertool/?$', 'landing.ecoLandingPage'),
    (r'^ubertool/(?P<model>.*?)/description/?$', 'description.descriptionPage'),
    (r'^ubertool/(?P<model>.*?)/input/?$', 'input.inputPage'),
    (r'^ubertool/(?P<model>.*?)/output/?$', 'output.outputPage'),
    (r'^ubertool/(?P<model>.*?)/algorithms/?$', 'algorithms.algorithmPage'),
    (r'^ubertool/(?P<model>.*?)/references/?$', 'references.referencesPage'),
    (r'^ubertool/(?P<model>.*?)/batchinput/?$', 'batch.batchInputPage'),
    (r'^ubertool/(?P<model>.*?)/batchoutput/?$', 'batch.batchOutputPage'),
    (r'^ubertool/(?P<model>.*?)/qaqc/(?P<runID>.*?)/?$', 'qaqc.qaqcRunView'),
    (r'^ubertool/(?P<model>.*?)/qaqc/?$', 'qaqc.qaqcPage'),
    (r'^ubertool/(?P<model>.*?)/history/?$', 'history.historyPage'),
    (r'^ubertool/(?P<model>.*?)/history/query?$', 'history.historyQueryAjax'),
    (r'^ubertool/(?P<model>.*?)/history/revisit?$', 'history.historyPageRevist'),
    # (r'^ubertool/.*?/history_revisit\.html$', 'history.historyPageRevist'),
    (r'^ubertool/(?P<model>.*?)/pdf/?$', 'generateReport.pdfReceiver'),
    (r'^ubertool/(?P<model>.*?)/html/?$', 'generateReport.htmlReceiver'),
    (r'^ubertool/docs/?$', 'misc.docsRedirect'),
    (r'^ubertool/api/?$', 'misc.apiRedirect'),
    # (r'^eco/.*?/przm5_intermediate\.html', 'przm5_intermediate.przm5IntermediatePage'),
    (r'^ubertool/(?P<model>.*?)/?$', 'description.descriptionPage'),
    (r'^eco_index\.html$', 'landing.ecoLandingPage'),                        #Legacy links
    (r'^(?P<model>.*?)_description\.html$', 'description.descriptionPage'),  #Legacy links
    (r'^(?P<model>.*?)_input\.html$', 'input.inputPage'),                    #Legacy links
    (r'^(?P<model>.*?)_output\.html$', 'output.outputPage'),                 #Legacy links
    (r'^(?P<model>.*?)_algorithms\.html$', 'algorithms.algorithmPage'),      #Legacy links
    (r'^(?P<model>.*?)_references\.html$', 'references.referencesPage'),     #Legacy links
    (r'^(?P<model>.*?)_batchinput\.html$', 'batch.batchInputPage'),          #Legacy links
    (r'^(?P<model>.*?)_batchoutput\.html$', 'batch.batchOutputPage'),        #Legacy links
    (r'^(?P<model>.*?)_qaqc\.html$', 'qaqc.qaqcPage'),                       #Legacy links
    (r'^(?P<model>.*?)_history\.html$', 'history.historyPage'),              #Legacy links
    # (r'^ubertool/api/', include('rest_framework_swagger.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

# 404 Error view (file not found)
handler404 = 'views.misc.fileNotFound'
# 500 Error view (server error)
handler500 = 'views.misc.fileNotFound'
# 403 Error view (forbidden)
handler403 = 'views.misc.fileNotFound'

