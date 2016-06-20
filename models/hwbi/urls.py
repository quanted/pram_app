from django.conf.urls import url
import views
import hwbi_qaqc
import hwbi_input


urlpatterns = [
    url(r'^$', views.hwbi_redirect),
    # url(r'^description$', views.descriptionPage),
    # url(r'^input$', hwbi_input.inputPage),
    # url(r'^algorithms$', views.algorithmPage),
    # url(r'^references$', views.referencesPage),
    # url(r'^qaqc$', hwbi_qaqc.qaqcRunView),
    # TODO: Delete next two endpoints...
    url(r'^api/Baseline$', views.get_default_HWBI_values),
    url(r'^api/HWBI', views.get_user_HWBI_values),
    # url(r'^$', views.hwbi_view, name='hwbi_view'),  # Shows HWBI page without ubertool branding
]
