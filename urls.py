#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()


# All view functions here must be in '/views/views.py'
urlpatterns = patterns('views.views',
    (r'^$', 'ubertoolLandingPage'),
    (r'^eco/?$', 'ecoLandingPage'),
    (r'^eco/(?P<model>.*?)/description/?$', 'descriptionPage'),
    (r'^eco/(?P<model>.*?)/input/?$', 'inputPage'),
    (r'^eco/(?P<model>.*?)/output/?$', 'outputPage'),
    (r'^eco/(?P<model>.*?)/algorithms/?$', 'algorithmPage'),
    (r'^eco/(?P<model>.*?)/references/?$', 'referencesPage'),
    (r'^eco/(?P<model>.*?)/batchinput/?$', 'batchInputPage'),
    (r'^eco/(?P<model>.*?)/batchoutput/?$', 'batchOutputPage'),
    (r'^eco/(?P<model>.*?)/qaqc/?$', 'qaqcPage'),
    (r'^eco/(?P<model>.*?)/history/?$', 'historyPage'),
    (r'^eco/.*?/history_revisit\.html$', 'historyPageRevist'),
    (r'^eco/(?P<model>.*?)/?$', 'descriptionPage'),
    (r'^eco_index\.html$', 'ecoLandingPage'),                     #Legacy links
    (r'^(?P<model>.*?)_description\.html$', 'descriptionPage'),   #Legacy links
    (r'^(?P<model>.*?)_input\.html$', 'inputPage'),               #Legacy links
    (r'^(?P<model>.*?)_output\.html$', 'outputPage'),             #Legacy links
    (r'^(?P<model>.*?)_algorithms\.html$', 'algorithmPage'),      #Legacy links
    (r'^(?P<model>.*?)_references\.html$', 'referencesPage'),     #Legacy links
    (r'^(?P<model>.*?)_batchinput\.html$', 'batchInputPage'),     #Legacy links
    (r'^(?P<model>.*?)_batchoutput\.html$', 'batchOutputPage'),   #Legacy links
    (r'^(?P<model>.*?)_qaqc\.html$', 'qaqcPage'),                 #Legacy links
    (r'^(?P<model>.*?)_history\.html$', 'historyPage'),           #Legacy links
    # url(r'^admin/', include(admin.site.urls)),
)

# 404 Error view (file not found)
handler404 = 'views.views.fileNotFound'
# 500 Error view (server error)
handler500 = 'views.views.fileNotFound'
# 403 Error view (forbidden)
handler403 = 'views.views.fileNotFound'