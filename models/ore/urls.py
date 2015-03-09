from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^category/?$', 'models.ore.ore_rest_calls.category_query'),
)
