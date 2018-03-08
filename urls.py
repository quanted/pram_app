from django.urls import include, path, re_path
from django.conf.urls import url
from .api import views as api_views
# from .docs import views as docs_views
from .views import description, input, output, algorithms, references, qaqc
from .views import misc, landing
from .views import batch
from .views import sam_watershed
from .models.sam import sam_output_landing
from .views import proxy

print('qed.pram_app.urls')

#model_patterns = [
#    #url(r'^$', description.description_page),
#    url(r'^description$', description.description_page),
#    url(r'^algorithms/?$', algorithms.algorithm_page),
#    url(r'^references/?$', references.references_page),
#    url(r'^qaqc/$', qaqc.qaqc_page),
#]
#url(r'^pram/(?P<model>.*?)/algorithms/?$', algorithms.algorithm_page),

#(?P<name>regex) - Round brackets group the regex between them, we are capturing the model name
#as an argument
#In Python regular expressions, the syntax for named regular-expression
#groups is (?P<name>pattern), where name is the name of the group and pattern is some pattern to match
urlpatterns = [
    # django 2.X
    path('', landing.eco_landing_page),
    path('pop/', landing.pop_landing_page),
    path('unter/', landing.unter_landing_page),
    path('links/', misc.links),
    re_path(r'^rest/(?P<flask_url>.*?)/?$', proxy.flask_proxy),
    path('<slug:model>/', description.description_page),
    path('<slug:model>/algorithms/', algorithms.algorithm_page),
    path('<slug:model>/references/', references.references_page),
    path('<slug:model>/qaqc/', qaqc.qaqc_page),
    path('<slug:model>/input/', input.input_page),
    path('<slug:model>/output', output.output_page),
    path('<slug:model>/batch/', batch.batch_page),
    re_path(r'^sam/output/status/(?P<task_id>.*?)$', sam_output_landing.olanding_page, {'model': 'sam'}),
    re_path(r'^sam/watershed/(?P<task_id>.*?)$', sam_watershed.watershed_page, {'model': 'sam'}),
    re_path(r'^api/$', api_views.api_docs_view, name='api_docs_view'),
    re_path(r'^api/spec/?$', api_views.api_docs_json),

    # #django 1.X
    # url(r'^$', landing.eco_landing_page),
    # url(r'^pop/$', landing.pop_landing_page),
    # url(r'^unter/$', landing.unter_landing_page),
    # url(r'^links/?$', misc.links),
    # url(r'^rest/(?P<flask_url>.*?)/?$', proxy.flask_proxy),
    # #docs
    # #url(r'^docs/$', docs_views.DocsRootView.as_view(), name='docs_root'),
    # #url(r'^(?P<path>.*)$', serve_docs, name='docs_files')
    # #url(r'^docs/', include('ubertool_app.docs.urls')),
    # #/api
    # #url(r'^api/', include('ubertool_app.api.urls')),
    # url(r'^api/$', api_views.api_docs_view, name='api_docs_view'),
    # url(r'^api/spec/?$', api_views.api_docs_json),
    # url(r'^sam/output/status/(?P<task_id>.*?)$', sam_output_landing.olanding_page, {'model': 'sam'}),
    # url(r'^sam/watershed/(?P<task_id>.*?)$', sam_watershed.watershed_page, {'model': 'sam'}),
    # #url(r'^test/$', landing.eco_landing_page_new), #testing before deployment
    # #url(r'^(?P<model>.*?)/?$', description.description_page), #this catches everything...
    # url(r'^(?P<model>.*?)/$', description.description_page),
    # url(r'^(?P<model>.*?)/description/?$', description.description_page),
    # url(r'^(?P<model>.*?)/algorithms/?$', algorithms.algorithm_page),
    # url(r'^(?P<model>.*?)/references/?$', references.references_page),
    # url(r'^(?P<model>.*?)/qaqc/?$', qaqc.qaqc_page),
    # url(r'^(?P<model>.*?)/input/?$', input.input_page),
    # url(r'^(?P<model>.*?)/output/?$', output.output_page),
    # url(r'^(?P<model>.*?)/batch/?$', batch.batch_page),
    # #url(r'^(?P<model>.*?)/?', include(model_patterns)),
]

# 404 Error view (file not found)
handler404 = misc.file_not_found
# 500 Error view (server error)
handler500 = misc.file_not_found
# 403 Error view (forbidden)
handler403 = misc.file_not_found

# #builds list of urlpatterns to pair with python methods to be called
# urlpatterns = [
#     url(r'^$', landing.eco_landing_page),
#     url(r'^(?P<model>)/$', description.description_page),
#     url(r'^(?P<model>)/description/$', description.description_page),
#     url(r'^(?P<model>)/algorithms/$', algorithms.algorithm_page),
#     url(r'^(?P<model>)/references/$', algorithms.algorithm_page),
#     #url(r'^cyan/', include('models.cyan.urls')),
#     #url(r'^pram/cyan/?', include('models.cyan.urls')),
#     #url(r'^pisces/', include('models.pisces.urls')),
#     #url(r'^pram/pisces/?', include('models.pisces.urls')),
#     #url(r'^(?P<model>.*?)/description/?$', description.description_page),
#     #url(r'^api/cts/', include('cts_api.urls')),
#     #url(r'^docs/', include('docs.urls')),
#     #url(r'^api/', include('api.urls')),
#     #url(r'^api/pram/', include('api.urls')),
#     #url(r'^rest/', include('REST.urls')),
#     #url(r'^hwbi/', include('models.hwbi.urls')),
#     #url(r'^pram/hwbi/?', include('models.hwbi.urls')),
#     #url(r'^pram/webice/', include('models.webice.urls')),
#     #url(r'^eco/test/?$', include('models.test.urls')),
#     #url(r'^pram/login/auth/?$', misc.login_auth),
#     #url(r'^pram/login*', misc.login),
#     #url(r'^pram/ore/', include('models.ore.urls')),
#     #url(r'^geoserver/?$', geoserver.test_page),
#     #url(r'^geoserver/query/(?P<jid>\d{20})$', geoserver.sam_huc_query),
#     #url(r'^geoserver/sam_done/(?P<jid>\d{20})$', geoserver.sam_done_query),
#     #url(r'^pram/(?P<model>.*?)/input/?$', input.input_page),
#     #url(r'^pram/(?P<model>.*?)/output/?$', output.output_page),
#     #url(r'^pram/(?P<model>.*?)/algorithms/?$', algorithms.algorithm_page),
#     #url(r'^pram/(?P<model>.*?)/references/?$', references.references_page),
#     #url(r'^pram/(?P<model>.*?)/batchinput/?$', batch.batchInputPage),
#     #url(r'^pram/(?P<model>.*?)/batchoutput/?$', batch.batchOutputPage),
#     #url(r'^pram/(?P<model>.*?)/qaqc/(?P<runID>.*?)/?$', qaqc.qaqcRunView),
#     #url(r'^pram/(?P<model>.*?)/qaqc/?$', qaqc.qaqcPage),
#     #url(r'^pram/(?P<model>.*?)/history/?$', history.historyPage),
#     #url(r'^pram/(?P<model>.*?)/history/query?$', history.historyQueryAjax),
#     #url(r'^pram/(?P<model>.*?)/history/revisit?$', history.historyPageRevist),
#     #url(r'^pram/.*?/history_revisit\.html$', history.historyPageRevist),
#     #url(r'^pram/(?P<model>.*?)/pdf/?$', generateReport.pdfReceiver),
#     #url(r'^pram/(?P<model>.*?)/html/?$', generateReport.htmlReceiver),
#     #url(r'^pram/docs/?$', misc.docs_redirect),
#     #url(r'^pram/api/?$', misc.api_redirect),
#     #url(r'^pram/links/?$', misc.links),
#     #url(r'^eco/.*?/przm5_intermediate\.html', przm5_intermediate.przm5IntermediatePage),
#     #url(r'^eco_index\.html$', landing.eco_landing_page),  # Legacy links
#     #url(r'^(?P<model>.*?)_description\.html$', description.description_page),  # Legacy links
#     #url(r'^(?P<model>.*?)_input\.html$', input.input_page),  # Legacy links
#     #url(r'^(?P<model>.*?)_output\.html$', output.output_page),  # Legacy links
#     #url(r'^(?P<model>.*?)_algorithms\.html$', algorithms.algorithm_page),  # Legacy links
#     #url(r'^(?P<model>.*?)_references\.html$', references.references_page),  # Legacy links
#     #url(r'^(?P<model>.*?)_batchinput\.html$', batch.batchInputPage),  # Legacy links
#     #url(r'^(?P<model>.*?)_batchoutput\.html$', batch.batchOutputPage),  # Legacy links
#     #url(r'^(?P<model>.*?)_qaqc\.html$', qaqc.qaqcPage),  # Legacy links
#     #url(r'^(?P<model>.*?)_history\.html$', history.historyPage),  # Legacy links
#     # url(r'^pram/api/', include('rest_framework_swagger.urls')),
#     # url(r'^admin/', include(admin.site.urls)),
# ]