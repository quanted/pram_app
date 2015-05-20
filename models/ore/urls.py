from django.conf.urls import patterns, url

urlpatterns = patterns('',
   (r'^query/category/?$', 'models.ore.ore_rest_calls.category_query'),
   (r'^query/assess?$', 'models.ore.ore_rest_calls.category_query')
)
