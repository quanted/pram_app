from django.conf.urls import url
import views
from views_pisces import description, algorithms, input, map, references


urlpatterns = [
    url(r'^$', description.description_page, {'model': "pisces"}),
    url(r'^description$', description.description_page, {'model': "pisces"}),
    url(r'^input$', input.input_page, {'model': "pisces"}),
    url(r'^map$', map.map_page, {'model': "pisces"}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': "pisces"}),
    url(r'^references$', references.references_page, {'model': "pisces"}),
    # TODO: Delete next two endpoints...
    url(r'^api/Baseline$', views.get_default_pisces_values),
    url(r'^api/pisces', views.get_user_pisces_values),
    # url(r'^$', views.pisces_view, name='pisces_view'),  # Shows pisces page without ubertool branding
]
