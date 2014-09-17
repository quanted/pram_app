from django.conf.urls import patterns, url

urlpatterns = patterns('webice_views',
    #url(r'^$', ),
    url(r'/webiceSSD_out\.html$', 'webiceSSDOutputPage'),
    url(r'/webiceTNE_out\.html$', 'webiceTNEOutputPage'),
    url(r'/ICETable\.html$', 'ICETabletPage'),
)
