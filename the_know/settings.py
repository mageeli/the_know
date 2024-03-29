"""
Django settings for the_know project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
import sys
import dj_database_url
import django_heroku
from decouple import config


import mimetypes
mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "True") == "True"

ALLOWED_HOSTS = ['*']
LOGIN_REDIRECT_URL = '/questions/'
LOGOUT_REDIRECT_URL = '/questions/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'questions',
    'api',
    'goals',
    'journal',
    'accounts.apps.AccountsConfig',
    'crispy_forms',
    'bootstrap5',
    "whitenoise.runserver_nostatic",  # new
    'blog',
    'tinymce',
    'tasks'
]
# CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'the_know.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'the_know.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#

if DEVELOPMENT_MODE is True:
    DATABASES = {
        # "default": {
        #     "ENGINE": "django.db.backends.postgresql_psycopg2",
        #     "NAME": "db",
        #     "USER": "db",
        #     "PASSWORD": "AVNS_v7xYpObqqu_SQq8",
        #     "HOST": "app-d25fe38e-988c-47f3-b4c8-352a12754778-do-user-11298864-0.b.db.ondigitalocean.com",
        #     "PORT": "25060",
        # }
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': BASE_DIR/'db.sqlite3',
        # }
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
        }
    }
    DATABASES['default'] = dj_database_url.config(default='postgres://ribgnldoiyujmf:9ee5f844d6acf42519c35de64a9ac3d1011ef9d8f1dd96e01b877b75498b2c4a@ec2-54-204-56-171.compute-1.amazonaws.com:5432/d51dp2qm840dsk')
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600),
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static/"),
# )
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # new

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
django_heroku.settings(locals())