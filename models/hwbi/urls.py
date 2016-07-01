from django.conf.urls import url
import views
from views_hwbi import description, algorithms, input, references


urlpatterns = [
    url(r'^$', views.hwbi_redirect),
    url(r'^description$', description.description_page, {'model': "hwbi"}),
    url(r'^input$', input.input_page, {'model': "hwbi"}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': "hwbi"}),
    url(r'^references$', references.references_page, {'model': "hwbi"}),
    # TODO: Delete next two endpoints...
    url(r'^api/Baseline$', views.get_default_HWBI_values),
    url(r'^api/HWBI', views.get_user_HWBI_values),
    # url(r'^$', views.hwbi_view, name='hwbi_view'),  # Shows HWBI page without ubertool branding
]
