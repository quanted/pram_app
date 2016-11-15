from django.conf.urls import url
from cts_api import REST, views

# All view functions here must be in '/views/views.py'
# path: serverLocation/jchem/...

# todo: use cts_api.views for every endpoint, which calls cts_rest

urlpatterns = [
    # url(r'^/?$', views.getCTSEndpoints),
    url(r'^$', REST.cts_rest.showSwaggerPage),
    url(r'^swag/?$', views.getSwaggerJsonContent),
    # url(r'^docs/?$', REST.cts_rest.showSwaggerPage),

    url(r'^molecule/?$', REST.cts_rest.getChemicalEditorData),
    # url(r'^speciation/?$', 'cts_rest.getChemicalEditorData),

    url(r'^(?P<calc>.*?)/inputs/?$', views.getCalcInputs),
    url(r'^(?P<calc>.*?)/run/?$', views.runCalc),
    url(r'^(?P<endpoint>.*?)/?$', views.getCalcEndpoints),
]
