"""Django settings for scope project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os

from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _
from envparse import env

from .helpers import ss_hosts_parser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", cast=list, subcast=str)

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=False)

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "rest_framework",
    "rest_framework.authtoken",
    "scope.staticfiles.Config",
    "widget_tweaks",
    "compressor",
    "modeltranslation",
    "scope.apps.ScopeConfig",
    "search.apps.SearchConfig",
    "django_cleanup",  # deletes FileFields when objects are deleted
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "scope.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "scope.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Requires MySQL or SQLite, the GROUP_CONCAT() function is being used
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        "OPTIONS": {"timeout": 10},
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTH_USER_MODEL = "scope.User"

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = [("en", _("English")), ("fr", _("French"))]

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

TIME_ZONE = env("DJANGO_TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Messages

# Force cookie storage to reduce the possibility of looking the database
# when using SessionStorage, which saves the data in the database by default.
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
# Fix mismatch with Bootstrap alert classes
MESSAGE_TAGS = {messages.DEBUG: "secondary", messages.ERROR: "danger"}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
    "npm.finders.NpmFinder",
]

# Compress

COMPRESS_OFFLINE = not DEBUG
COMPRESS_PRECOMPILERS = [("text/x-scss", "sassc {infile} {outfile}")]

# NPM

NPM_ROOT_PATH = BASE_DIR
NPM_STATIC_FILES_PREFIX = "lib"
NPM_FILE_PATTERNS = {
    "@fortawesome": ["fontawesome-free/webfonts/fa-solid-900.*"],
    "bootstrap": ["dist/js/bootstrap.bundle.min.*"],
    "bootstrap-datepicker": [
        "dist/css/bootstrap-datepicker3.standalone.min.css",
        "dist/js/bootstrap-datepicker.min.js",
        "dist/locales/bootstrap-datepicker.fr.min.js",
    ],
    "jquery": ["dist/jquery.slim.min.*"],
    "typeface-roboto": ["files/roboto-latin-400.*"],
}

# Media

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
FILE_UPLOAD_PERMISSIONS = 0o640

# Authentication

LOGOUT_REDIRECT_URL = "home"
LOGIN_REDIRECT_URL = "home"

# Fixtures

FIXTURE_DIRS = [os.path.join(BASE_DIR, "scope", "tests", "fixtures")]

# Elasticsearch

# RFC-1738 formatted URLs can be used. E.g.:'https://user:secret@host:443/'
ES_HOSTS = env("ES_HOSTS", cast=list, subcast=str)
ES_TIMEOUT = env.int("ES_TIMEOUT", default=10)
ES_POOL_SIZE = env.int("ES_POOL_SIZE", default=10)
ES_INDEXES_SETTINGS = {
    "number_of_shards": env.int("ES_INDEXES_SHARDS", default=1),
    "number_of_replicas": env.int("ES_INDEXES_REPLICAS", default=0),
}

# Celery

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": env.int("CELERY_BROKER_VISIBILITY_TIMEOUT", default=3600)
}
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

# REST Framework

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# Storage Service

# Allows a list of URLs separated by comma.
# Requires RFC-1738 formatted URLs. E.g.:'https://user:secret@host:443/'.
SS_HOSTS = env(
    "SS_HOSTS", cast=list, subcast=str, postprocessor=ss_hosts_parser, default=[]
)
