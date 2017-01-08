from django.conf.urls import url
import views
from views_cyan import description, algorithms, input, references


urlpatterns = [
    url(r'^$', description.description_page, {'model': "cyan"}),
    url(r'^description$', description.description_page, {'model': "cyan"}),
    url(r'^input$', input.input_page, {'model': "cyan"}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': "cyan"}),
    url(r'^references$', references.references_page, {'model': "cyan"}),
    # TODO: Delete next two endpoints...
    url(r'^api/Baseline$', views.get_default_cyan_values),
    url(r'^api/cyan', views.get_user_cyan_values),
    # url(r'^$', views.cyan_view, name='cyan_view'),  # Shows cyan page without ubertool branding
]
