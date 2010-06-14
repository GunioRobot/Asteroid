# -*- coding: utf-8 -*-

import os,sys

# The absolute path to this settings.py file
ROOT = os.path.abspath(os.path.dirname(__file__))
# Used to translate every path in settings.py to an absolute path.
path = lambda x: os.path.join(ROOT, x)

ADMINS = ( ('', ''), )
MANAGERS = ADMINS
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
SITE_ID = 1
USE_I18N = False

MEDIA_ROOT = path('media')
MEDIA_URL = '/media'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'yqci=(=-#y#_=-!#rl_9!0z+^n=+c+gb-#w1i6s7!knoc9b1oy'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = { 'default': { 'NAME': path('dev.db'), 'ENGINE': 'django.db.backends.sqlite3', } }

# run "python -m smtpd -n -c DebuggingServer localhost:1025" to see outgoing
# messages dumped to the terminal
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# application specific commands
QUEUE_COMMANDS = True
QUEUE_ADDRESS = '127.0.0.1'

# used for the callback
DOMAIN = "http://localhost:8020"

# ignore django code when we calculate coverage
EXCLUDE_FROM_COVERAGE = ['django']
