from django.conf.urls import patterns, url

urlpatterns = patterns('views.output_webice',
    url(r'webice_output\.html', 'webiceOutputPage'),
    url(r'webiceSSD_out\.html', 'webiceSSDOutputPage'),
    url(r'webiceTNE_out\.html', 'webiceTNEOutputPage'),
    url(r'ICETable\.html', 'ICETabletPage'),
)
