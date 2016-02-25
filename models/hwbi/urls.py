from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hwbi_view, name='hwbi_view'),
    # url(r'^spec/?$', views.api_docs_json)
]
