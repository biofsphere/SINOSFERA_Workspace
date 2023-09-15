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
from django.contrib import admin

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
    'django.contrib.contenttypes',
    # custom UI choices
    # 'grappelli', # Switch on to use Grappelli (remember to switch off any other admin UI that might be installed)
    'admin_interface', # needed for django-admin-interface
    'colorfield', # needed for django-admin-interface
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.github',
    'bootstrap5',
    'crispy_forms',
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
    'programas',
    'projetos',
    'relatorios',
    'home',
    'blog',
    'support',
    'slick_reporting',
    'categorias',
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

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

AUTH_USER_MODEL = 'pessoas.CustomUser' # for customizing the user model

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
    'TILES': f'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{{z}}/{{x}}/{{y}}?access_token={os.environ.get("MAPBOX_ACCESS_TOKEN")}',
    'DEFAULT_CENTER': (-29.760742, -51.148017),
    'DEFAULT_ZOOM': 10,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 7,
}

BASE_COUNTRY = "BR"

# GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
# RECAPTCHA_KEY = os.environ.get('RECAPTCHA_KEY')
# RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')


USE_DJANGO_JQUERY = True # True means use Jquery from CDN (necessary for using smart_selects)

# Versioning settings:
repo = Repo('D:/HDD_Code/SINOSFERA_Workspace')
commit_count = len(list(repo.iter_commits()))

DJVERSION_VERSION = f'v0.1.{commit_count}' # Aveilable as template context variable {{ VERSION}}
DJVERSION_UPDATED = date
DJVERSION_GIT_REPO_PATH = 'D:/HDD_Code/SINOSFERA_Workspace'
DJVERSION_GIT_USE_TAG = False
DJVERSION_GIT_USE_COMMIT = False

# Grappelli settings:
# GRAPPELLI_ADMIN_TITLE = 'SINOSFERA Admin' # Switch on if Grappelli is in use

# # Customized admin ordering of apps and models:
# ADMIN_ORDERING = (
#     ('auth', (
#         'group', 
#         'permission',
#     )),
#     ('contas', (
#         'emailaddress',
#     )),
#     ('socialaccunt', (
#         'socialaccount',
#         'socialapp',
#         'socialtoken',
#     )),
#     ('pessoas', (
#         'CustomUser', 
#         'Pessoa', 
#     )),
#     ('instituicoes', (
#         'Instituicao',
#     )),
#     ('locais', (
#         'Microbacia',
#         'Municipio',
#         'Unidade_de_referencia',
#     )),
#     ('planos', (
#         'Plano',
#         'Programa_de_acoes_prioritarias',
#         'Acao_prioritaria',
#     )),
#     ('programas', (
#         'Programa',
#         'Diretriz_especifica_de_programa',
#     )),
#     ('projetos', (
#         'Projeto',
#         'Objetivo_especifico_de_projeto',
#         'Etapa',
#         'Atividade',
#     )),
#     ('fundos', (
#         'Requisicao',
#         'Orcamento',
#         'Pedido',
#         'Item',
#     )),
#     ('categorias', (
#         'Profissao',
#         'Categoria_de_plano',
#         'Categoria_de_subprojeto',
#         'Subcategoria_de_subprojeto',
#         'Categoria_de_atividade',
#         'Subcategoria_de_atividade',
#         'Categoria_de_publico_atendido',
#         'Unidade_de_medida',
#         'Fundo',
<<<<<<< HEAD
#         'Categoria_de_despesa'
=======
#         'Categoria_de_despesa',
#     )),
#     ('sites', (
#         'site',
#     )),
#     ('admin_interface', (
#         'theme',
>>>>>>> 7f235b9123fc8524c657c916bfb048063760d43f
#     )),
# )

# def get_app_list(self, request, app_label=None):
#     app_dict = self._build_app_dict(request, app_label)
    
#     if not app_dict:
#         return
        
#     NEW_ADMIN_ORDERING = []
#     if app_label:
#         for ao in ADMIN_ORDERING:
#             if ao[0] == app_label:
#                 NEW_ADMIN_ORDERING.append(ao)
#                 break
    
#     if not app_label:
#         for app_key in list(app_dict.keys()):
#             if not any(app_key in ao_app for ao_app in ADMIN_ORDERING):
#                 app_dict.pop(app_key)
    
#     app_list = sorted(
#         app_dict.values(), 
#         key=lambda x: [ao[0] for ao in ADMIN_ORDERING].index(x['app_label'])
#     )
    
#     for app, ao in zip(app_list, NEW_ADMIN_ORDERING or ADMIN_ORDERING):
#         if app['app_label'] == ao[0]:
#             for model in list(app['models']):
#                 if not model['object_name'] in ao[1]:
#                     app['models'].remove(model)
#         app['models'].sort(key=lambda x: ao[1].index(x['object_name']))
#     return app_list

# admin.AdminSite.get_app_list = get_app_list

