from . import rest_funcs
from django.conf.urls import url

urlpatterns = [
    url(r'pram/(?P<model>.*)/(?P<jid>.*)/?$', rest_funcs.rest_proxy),
    url(r'^$', rest_funcs.self_documentation)
    # url(r'pram/(?P<model>.*?/?$)', rest_funcs.rest_proxy),
]
