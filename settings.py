import os
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)

logger.info("PRAM-APP django:settings.py")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, 'templates/')

DEPLOY_ENV = os.getenv("DEPLOY_ENV", "kube-dev")

# logger.info(f"PROJECT_ROOT: {PROJECT_ROOT}")
logger.info(f"TEMPLATE_ROOT: {TEMPLATE_ROOT}")
# logger.info(f"DEPLOY_ENV: {DEPLOY_ENV}")

if DEPLOY_ENV == "kube-dev":
    DEBUG = True
    CORS_ORIGIN_ALLOW_ALL = True
else:
    DEBUG = False
    CORS_ORIGIN_ALLOW_ALL = False

ALLOWED_HOSTS = ['*']
APPEND_SLASH = True

ADMINS = (
    ('Tom Purucker', 'purucker.tom@epa.gov'),
    ('Jeffrey Minucci', 'minucci.jeffrey@epa.gov'),
    ('Deron Smith', 'smith.deron@epa.gov'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(TEMPLATE_ROOT),
            # os.path.join(TEMPLATE_ROOT, 'drupal_2017'),
            # os.path.join(TEMPLATE_ROOT, 'uber2017'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    }
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pram_app',
    'corsheaders'
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, "collected_static/pram")
STATIC_URL = '/pram/static/'

# Define ENVIRONMENTAL VARIABLES
os.environ.update({
    'PROJECT_PATH': PROJECT_ROOT,
    'SITE_SKIN': 'EPA',  # Leave empty ('') for default skin, 'EPA' for EPA skin
    'CONTACT_URL': 'https://www.epa.gov/research/forms/contact-us-about-epa-research',
})

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SECRET_KEY = os.getenv('SECRET_KEY', "needtosetthesecretkey")

WSGI_APPLICATION = 'wsgi.application'
