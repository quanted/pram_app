from django.conf.urls import patterns, url

urlpatterns = patterns('',
   (r'^query/category/?$', 'models.ore.ore_rest_calls.category_query'),
   (r'^query/output?$', 'models.ore.ore_rest_calls.output_query')
)
