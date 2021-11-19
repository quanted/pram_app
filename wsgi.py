from django.core.wsgi import get_wsgi_application
import os

django_settings = os.getenv("DJANGO_SETTINGS_MODULE", "settings")
os.environ.setdefault("DJANGO_SETTINGS_FILE", django_settings)

application = get_wsgi_application()

