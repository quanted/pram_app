from django.urls import include, path, re_path
from django.conf.urls import url
from pram_app.api import views as api_views
# from .docs import views as docs_views
from pram_app.views import description, input, output, algorithms, references, qaqc
from pram_app.views import misc, landing
from pram_app.views import batch
from pram_app.views import sam_watershed
from pram_app.models.sam import sam_output_landing
from pram_app.models.varroapop import varroapop_files
from pram_app.views import proxy

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
    path('links/', misc.links),
    re_path(r'^rest/(?P<flask_url>.*?)/?$', proxy.flask_proxy),
    path('<slug:model>/', description.description_page),
    path('<slug:model>/algorithms/', algorithms.algorithm_page),
    path('<slug:model>/references/', references.references_page),
    path('<slug:model>/qaqc/', qaqc.qaqc_page),
    path('<slug:model>/input/', input.input_page),
    path('<slug:model>/output/', output.output_page, name='output'),
    path('<slug:model>/batch/', batch.batch_page),
    re_path(r'^sam/output/status/(?P<task_id>.*?)$', sam_output_landing.olanding_page, {'model': 'sam'}),
    re_path(r'^sam/watershed/(?P<task_id>.*?)$', sam_watershed.watershed_page, {'model': 'sam'}),
    re_path(r'^api/$', api_views.api_docs_view, name='api_docs_view'),
    re_path(r'^api/spec/?$', api_views.api_docs_json),
    path('varroapop/output/<slug:sessionid>/input/', varroapop_files.files_input_view, name = 'varroapop_input'),
    path('varroapop/output/<slug:sessionid>/log/', varroapop_files.files_log_view, name = 'varroapop_log'),
    path('varroapop/output/<slug:sessionid>/results/', varroapop_files.files_results_view, name = 'varroapop_results'),
    path('github', misc.github)
]

urlpatterns = [path('pram/', include(urlpatterns))]

# 404 Error view (file not found)
handler404 = misc.file_not_found
# 500 Error view (server error)
handler500 = misc.file_not_found
# 403 Error view (forbidden)
handler403 = misc.file_not_found
