from django.conf.urls import patterns, url

urlpatterns = patterns(
    'REST',
    url(r'ubertool/(?P<model>.*)/(?P<jid>.*)/?$', 'rest_funcs.rest_proxy'),
    # url(r'ubertool/(?P<model>.*?/?$)', 'rest_funcs.rest_proxy'),
)
