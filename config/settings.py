"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from environs import Env
from django.urls import reverse_lazy




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

env = Env()
env.read_env()

SECRET_KEY = env("DJANGO_SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'ckeditor',
    'allauth',
    'allauth.account',
    'rosetta',
    'crispy_forms',

    # my_apps
    'accounts',
    'shop',
    'cart',
    'orders',
    'contactus',
    'payments',
]

# crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath("templates"))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # my context processors
                'cart.context_processors.cart',
                'cart.context_processors.favorites',
                'contactus.context_processors.contact',
                'shop.context_processors.admin_awareness',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'POST': 5432,
    }
}

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# language settings

LANGUAGE_CODE = 'fa'

LANGUAGES = (
    ('en', 'english'),
    ('fa', 'persian')
)

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_TZ = True
USE_L10N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC :
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA :
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media/'))

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom user
AUTH_USER_MODEL = 'accounts.CustomUser'

# all_auth settings :
SITE_ID = 1
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("SETTINGS_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("SETTINGS_EMAIL_HOST_PASSWORD")

ACCOUNT_SECTION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_authentication_METHOD = 'email'
ACCOUNTS_EMAIL_REQUIRED = True
ACCOUNTS_UNIQUE_EMAIL = True
ACCOUNT_PASSWORD_HASH = 'bcrypt'

# LOGIN_REDIRECT_URL = 'ShowPackages'
# LOGOUT_REDIRECT_URL = 'ShowPackages'
# ACCOUNT_SIGNUP_REDIRECT_URL = 'aboutme'
# LOGIN_REDIRECT_URL = HttpResponseRedirect('next')
# LOGOUT_REDIRECT_URL = login.HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
# return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# ZARINPAL variables :
ZARINPAL_MERCHANT_ID = env("DJANGO_ZARINPAL_MERCHANT_ID")

