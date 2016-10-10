#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url
from chemaxon_cts import jchem_rest
# from django.contrib import admin
# admin.autodiscover()
from cts_api.REST import cts_rest
from cts_api import views


# All view functions here must be in '/views/views.py'
# path: serverLocation/jchem/...

# todo: use cts_api.views for every endpoint, which calls cts_rest

urlpatterns = patterns('',
	# (r'^/?$', 'cts_api.views.getCTSEndpoints'),
	(r'^/?$', 'cts_api.REST.cts_rest.showSwaggerPage'),
	(r'^swag/?$', 'cts_api.views.getSwaggerJsonContent'),
	# (r'^docs/?$', 'cts_api.REST.cts_rest.showSwaggerPage'),

	(r'^molecule/?$', 'cts_api.REST.cts_rest.getChemicalEditorData'),
	# (r'^speciation/?$', 'cts_rest.getChemicalEditorData'),

	(r'^(?P<calc>.*?)/inputs/?$', 'cts_api.views.getCalcInputs'),
	(r'^(?P<calc>.*?)/run/?$', 'cts_api.views.runCalc'),
	(r'^(?P<endpoint>.*?)/?$', 'cts_api.views.getCalcEndpoints'),
)

# # 404 Error view (file not found)
# handler404 = 'views.misc.fileNotFound'
# # 500 Error view (server error)
# handler500 = 'views.misc.fileNotFound'
# # 403 Error view (forbidden)
# handler403 = 'views.misc.fileNotFound'

