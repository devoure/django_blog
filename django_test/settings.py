"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 3.1b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import django_heroku
from pathlib import Path
import os
#import psycopg2
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'w-uhl8bf56gd_i&=6s#8ve7mj8t2j9s1zax-_7rrr1e))w9oyw'
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition
ADMINS = (('Athman Bakari', 'Disguisedsandwich@gmail.com'),
          )
UPLOAD_FILE_PATTERN = "uploaded_files/%s_%s"
INSTALLED_APPS = [
    'article.apps.ArticleConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'formtools.wizard.views',
    'userprofile.apps.UserprofileConfig',
    'storages'
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

ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/athman/Documents/django/django_test/templates',
                 '/home/athman/Documents/django/django_test/article/templates'],
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

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES ={
    'default':dj_database_url.config()}
#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')



# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers' : False,
    'handlers':{
        'mail_admins':{
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers' : {'django_request':{'handlers' : ['mail_admins'],
                                   'level' : 'ERROR',
                                   'propagate' : True,}
                 },
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR/ 'static']
STATIC_ROOT = BASE_DIR/ 'assets'
MEDIA_URL = '/assets/'
MEDIA_ROOT = BASE_DIR/ 'assets'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "disguisedsandwich@gmail.com"
try:
    from .local_settings import *
except Exception as e:
    print (e)
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']


if not DEBUG:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_PRELOAD_METADATA = True
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
    S3_URL = 'https://%s.s3.amazonaws.com/static/' %AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
django_heroku.settings(locals())
