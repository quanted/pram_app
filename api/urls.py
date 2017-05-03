from django.conf.urls import url

from . import views

urlpatterns = [
    #this is no more
    url(r'^$', views.api_docs_view, name='api_docs_view'),
    url(r'^spec/?$', views.api_docs_json),
]
