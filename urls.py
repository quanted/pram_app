#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()


# All view functions here must be in '/views/views.py'
urlpatterns = patterns('views',
                       url(r'^docs/', include('docs.urls')),
                       url(r'^api/', include('api.urls')),
                       url(r'^api/ubertool/', include('api.urls')),
                       url(r'^api/cts/', include('cts_api.urls')),
                       (r'^rest/', include('REST.urls')),
                       url(r'^hwbi/', include('models.hwbi.urls')),
                       url(r'^ubertool/hwbi/?', include('models.hwbi.urls')),
                       (r'^ubertool/webice/', include('models.webice.urls')),
                       # (r'^eco/test/?$', include('models.test.urls')),
                       (r'^ubertool/login/auth/?$', 'misc.login_auth'),
                       (r'^ubertool/login*', 'misc.login'),
                       (r'^ubertool/ore/', include('models.ore.urls')),
                       (r'^$', 'landing.ubertool_landing_page'),
                       (r'^geoserver/?$', 'geoserver.test_page'),
                       (r'^geoserver/query/(?P<jid>\d{20})$', 'geoserver.sam_huc_query'),
                       (r'^geoserver/sam_done/(?P<jid>\d{20})$', 'geoserver.sam_done_query'),
                       (r'^ubertool/?$', 'landing.eco_landing_page'),
                       (r'^ubertool/(?P<model>.*?)/description/?$', 'description.description_page'),
                       (r'^ubertool/(?P<model>.*?)/input/?$', 'input.input_page'),
                       (r'^ubertool/(?P<model>.*?)/output/?$', 'output.output_page'),
                       (r'^ubertool/(?P<model>.*?)/algorithms/?$', 'algorithms.algorithm_page'),
                       (r'^ubertool/(?P<model>.*?)/references/?$', 'references.references_page'),
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
                       (r'^ubertool/docs/?$', 'misc.docs_redirect'),
                       (r'^ubertool/api/?$', 'misc.api_redirect'),
                       (r'^ubertool/links/?$', 'misc.links'),
                       # (r'^eco/.*?/przm5_intermediate\.html', 'przm5_intermediate.przm5IntermediatePage'),
                       (r'^ubertool/(?P<model>.*?)/?$', 'description.description_page'),
                       (r'^eco_index\.html$', 'landing.eco_landing_page'),  # Legacy links
                       (r'^(?P<model>.*?)_description\.html$', 'description.description_page'),  # Legacy links
                       (r'^(?P<model>.*?)_input\.html$', 'input.input_page'),  # Legacy links
                       (r'^(?P<model>.*?)_output\.html$', 'output.output_page'),  # Legacy links
                       (r'^(?P<model>.*?)_algorithms\.html$', 'algorithms.algorithm_page'),  # Legacy links
                       (r'^(?P<model>.*?)_references\.html$', 'references.references_page'),  # Legacy links
                       (r'^(?P<model>.*?)_batchinput\.html$', 'batch.batchInputPage'),  # Legacy links
                       (r'^(?P<model>.*?)_batchoutput\.html$', 'batch.batchOutputPage'),  # Legacy links
                       (r'^(?P<model>.*?)_qaqc\.html$', 'qaqc.qaqcPage'),  # Legacy links
                       (r'^(?P<model>.*?)_history\.html$', 'history.historyPage'),  # Legacy links
                       # (r'^ubertool/api/', include('rest_framework_swagger.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       )

# 404 Error view (file not found)
handler404 = 'views.misc.file_not_found'
# 500 Error view (server error)
handler500 = 'views.misc.file_not_found'
# 403 Error view (forbidden)
handler403 = 'views.misc.file_not_found'
