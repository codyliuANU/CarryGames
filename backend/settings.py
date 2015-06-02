"""
Django settings for backend project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Django settings for backend project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alex L.', 'lanbinaleksey@gmail.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'staticfiles'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = "/home/la0rg/dj-ng-heroku-boilerplate"

# Chose path to Angular.js files according to environment
# ###
# Development SPA
DEV_SPA = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'build'))
# Production SPA
PROD_SPA = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'bin'))
# Chose correct SPA
SPA_INDEX = DEV_SPA if DEBUG else PROD_SPA

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(BASE_DIR, '..', 'static')),
    SPA_INDEX,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zy1j$t&-ufw1h_jcl1in=er-9cytx0k&&-_ymnyq_=hmvyjmqq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    SPA_INDEX,
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Framework for generating REST endpoints
    'rest_framework',
    'rest_framework.authtoken',
    # Extended management commands
    'django_extensions',
    # Custom user model
    'authentication',
    # Django-rest-auth
    'rest_auth',
    'djoser',
    'tournament',
    'TLogger',
    'sslserver',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
   # 'default':
   #     dj_database_url.config(default='postgres://postgres:123@localhost/heroku')
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Customize django user model
AUTH_USER_MODEL = 'authentication.Account'

# Djanro-Rest-Framework configuration

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Djoser App Settings

DJOSER = {
    'DOMAIN': 'localhost:8080',
    'SITE_NAME': 'CarryGames',
    'PASSWORD_RESET_CONFIRM_URL': 'api/auth/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'api/auth/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
}

# BattleNet authentication
BNET_KEY = 'pkbcgy8h99jyhmwvwq9rt9ysqvg5mze7'
BNET_SECRET = '7EqzYtxB427Yb4AAfB3PR2bjMT4vxTwd'

