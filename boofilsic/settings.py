"""
Django settings for boofilsic project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import psycopg2.extensions


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '***REMOVED***'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownx',
    'users.apps.UsersConfig',
    'common.apps.CommonConfig',
    'books.apps.BooksConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boofilsic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'boofilsic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'test',
            'USER': 'donotban',
            'PASSWORD': 'donotbansilvousplait',
            'HOST': '192.168.136.5',
            'OPTIONS': {
                'client_encoding': 'UTF8',
                # 'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_DEFAULT,
            }
        }    
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'boofilsic',
            'USER': 'doubaniux',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'OPTIONS': {
                'client_encoding': 'UTF8',
                # 'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_DEFAULT,
            }
        }    
    }

# Customized auth backend, glue OAuth2 and Django User model together
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#authentication-backends

AUTHENTICATION_BACKENDS = [
    'users.auth.OAuth2Backend',
    # for admin to login admin site
    # 'django.contrib.auth.backends.ModelBackend'
    ]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''

AUTH_USER_MODEL = 'users.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'E:\\temp'

CLIENT_ID = '3U57sjR7uvCu8suyFlp-fiBVj9-pKt3-jd7F2gLF6EE'
CLIENT_SECRET = 'HZohdI-xR8lUyTs_bM0G3l9Na0W6bZ6DfMK3b84_E0g'

# Path to save report related images, ends without slash
REPORT_MEDIA_PATH_ROOT = 'report/'
MARKDOWNX_MEDIA_PATH = 'review/'
BOOK_MEDIA_PATH_ROOT = 'book/'
DEFAULT_BOOK_IMAGE = os.path.join(MEDIA_ROOT, BOOK_MEDIA_PATH_ROOT, 'default.jpg')

# Mastodon domain name
MASTODON_DOMAIN_NAME = 'cmx-im.work'

# Default password for each user. since assword is not used any way,
# any string that is not empty is ok
DEFAULT_PASSWORD = 'eBRM1DETkYgiqPgq'

# Default redirect loaction when access login required view
LOGIN_URL = '/users/login/'

# Admin site root url
ADMIN_URL = 'lpLuTqX72Bt2hLfxxRYKeTZdE59Y2hLfpLuTqX72BtxxResXulIui1ayY2hLfpLuTqX72BtxxRejYKej1aNejYKeTZdE59sXuljYKej1aN1ZdE59sXulINSGMXTY9IIui1ayY2hLfxxRejYKej1aN1ZdE59sXulINSGMXTY9ID4tYEmjrHd'

# https://django-debug-toolbar.readthedocs.io/en/latest/
# maybe benchmarking before deployment