# -*- coding: utf-8 -*-
import os,sys

# The absolute path to this settings.py file
ROOT = os.path.abspath(os.path.dirname(__file__))
# Used to translate every path in settings.py to an absolute path.
path = lambda x: os.path.join(ROOT, x)

MANAGERS = ADMINS
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
SITE_ID = 1
USE_I18N = False

MEDIA_ROOT = path('../media')
MEDIA_URL = '/media'
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'runner.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'runner.urls'

TEMPLATE_DIRS = (
    path('templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'runner',
    'django_extensions',
    'guardian',
)

# ignore django code when we calculate coverage
EXCLUDE_FROM_COVERAGE = ['django']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1
LOGIN_URL="/login/"
LOGIN_EXEMPT_URLS = (
    r'^admin/',
    r'^media/',
    r'^login/',
    r'^logout/',
    r'^auth/',
) 

# the following variables should be overwritten in settings_local.py
ADMINS = ( ('', ''), )
SECRET_KEY = 'yqci=(=-#y#_=-!#rl_9!0z+^n=+c+gb-#w1i6s7!knoc9b1oy'
DATABASES = { 'default': { 'NAME': path('../dev.db'), 'ENGINE': 'django.db.backends.sqlite3', } }
DEBUG = True

# run "python -m smtpd -n -c DebuggingServer localhost:1025" to see outgoing
# messages dumped to the terminal
EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# application specific commands
QUEUE_COMMANDS=False
#QUEUE_COMMANDS = True
#QUEUE_ADDRESS = '127.0.0.1'

# used for the callback
DOMAIN = "http://localhost:8020"

try: from settings_local import *
except: pass

TEMPLATE_DEBUG = DEBUG
