from django.conf.urls import url
from models.webice import output_webice

urlpatterns = [
    url(r'webice_output\.html', output_webice.webiceOutputPage),
    url(r'webiceSSD_out\.html', output_webice.webiceSSDOutputPage),
    url(r'webiceTNE_out\.html', output_webice.webiceTNEOutputPage),
    url(r'ICETable\.html', output_webice.ICETabletPage),
]
