from django.conf.urls import url
from cts_api.epi_cts import views


urlpatterns = [
    url(r'^data/$', views.request_manager)
    #  url(r'^api/(?P<path>.*)$', views.simple_proxy),
    #  url(r'^(?P<model>.*?)/table/?$', views.index, name='index'),
    #  url(r'^calc-kow/$', views.calc_kow)
]
