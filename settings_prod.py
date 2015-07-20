"""
Django settings for redcross project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# JSON secrets module
with open(os.path.join(BASE_DIR, '.redcross_gny_secret.json')) as f:
    secrets=json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """
    get the secret setting or return explicit exception
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable in the secret file".format(setting)
        raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('REDCROSS_GNY_SECRET')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['arcgny.ulstercorps.org',
                 'www.arcgny.ulstercorps.org',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ims',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'redcross_gny.urls'

WSGI_APPLICATION = 'redcross_gny.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('REDCROSS_GNY_DB'),
        'USER': get_secret('REDCROSS_GNY_DB_USER'),
        'PASSWORD': get_secret('REDCROSS_GNY_DB_PASS'),
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL='/accounts/login'

# Paged display defaults
PAGE_SIZE=17

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home3/ulsterc3/public_html/arc/gny/static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home3/ulsterc3/Rob/python27/lib/python2.7/site-packages/ims/static',
)

LOG_FILE=os.path.join(BASE_DIR, 'redcross_gny.log')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates',
                '/home3/ulsterc3/Rob/python27/lib/python2.7/site-packages/ims/templates',)]
# DJANGO_LOG_LEVEL=DEBUG
# # Logging setup
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'redcross.log'),
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'DEBUG',
#         },
#         'rims': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#         },
#     }
# }
