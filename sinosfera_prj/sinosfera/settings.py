"""
Django settings for sinosfera project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from datetime import date
from pathlib import Path
from git import Repo
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.github',
    'bootstrap5',
    'crispy-forms',
    'crispy_bootstrap5',
    'crispy_bootstrap4',
    'leaflet',
    'smart_selects',
    'django_filters',
    'djversion',
    'djgeojson',
    'rest_framework',
    'rest_framework_gis',
    'import_export',
    'django_extensions',
    'dashboards',
    'fundos',
    'instituicoes',
    'locais',
    'mapas',
    'pessoas',
    'planos',
    'projetos',
    'relatorios',
    'slick_reporting',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CRISPY_FAIL_SILENTLY = not DEBUG

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
]

ROOT_URLCONF = 'sinosfera.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sinosfera.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

# AUTH_USER_MODEL = 'accounts.CustomUser' # for customizing the user model

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Allauth settings:
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = 'home'
ACCOUT_LOGOUT_REDIRECT = 'home'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_VALIDATORS = 'autenticacao.validators.custom_username_validators'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [BASE_DIR / 'static'] # directory for storing static files in development
STATIC_ROOT =  BASE_DIR / 'staticfiles' # directory for storing static files to be served in production
STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Mapping configs
VIRTUAL_ENV_BASE = os.environ.get(
    'VIRTUAL_ENV')   # Accessing libraries at .venv

GDAL_LIBRARY_PATH = VIRTUAL_ENV_BASE + r'\Lib\site-packages\osgeo\gdal304.dll'
GEOS_LIBRARY_PATH = VIRTUAL_ENV_BASE + r'\Lib\site-packages\osgeo\geos_c.dll'
PROJ_LIBRARY_PATH = VIRTUAL_ENV_BASE + r'\Lib\site-packages\osgeo\data\proj'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-0.023, 36.87),
    'DEFAULT_ZOOM': 5,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
}

# GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
# RECAPTCHA_KEY = os.environ.get('RECAPTCHA_KEY')
# RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

BASE_COUNTRY = "BR"

USE_DJANGO_JQUERY = True # True means use Jquery from CDN (necessary for using smart_selects)

# Versioning:
repo = Repo('D:/HDD_Code/SINOSFERA_Workspace')
commit_count = len(list(repo.iter_commits()))

DJVERSION_VERSION = f'v0.1.{commit_count}' # Aveilable as template context variable {{ VERSION}}
DJVERSION_UPDATED = date
DJVERSION_GIT_REPO_PATH = 'D:/HDD_Code/SINOSFERA_Workspace'
DJVERSION_GIT_USE_TAG = False
DJVERSION_GIT_USE_COMMIT = False
