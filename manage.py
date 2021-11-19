from django.core.management import execute_from_command_line
import os
import sys


if __name__ == "__main__":
    django_settings = os.getenv("DJANGO_SETTINGS_MODULE", "settings")
    print(f"manage.py - DJANGO_SETTINGS_MODULE: {django_settings}")
    os.environ.setdefault("DJANGO_SETTINGS_FILE", django_settings)
    execute_from_command_line(sys.argv)
