from django.conf.urls import url
from models.ore import ore_rest_calls

urlpatterns = [
    url(r'^query/category/?$', ore_rest_calls.category_query),
    url(r'^query/output?$', ore_rest_calls.output_query),
    url(r'^export/?$', ore_rest_calls.output_export),
    url(r'^download/?$', ore_rest_calls.output_download)
]
