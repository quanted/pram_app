from django.conf.urls import url
import views


urlpatterns = [
    url(r'^api/Baseline$', views.get_default_HWBI_values),
    url(r'^api/HWBI', views.get_user_HWBI_values),
    # url(r'^$', views.hwbi_view, name='hwbi_view'),  # Shows HWBI page without ubertool branding
]
