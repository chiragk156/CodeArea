"""
Django settings for codearea project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&_@v!!ydc=_23ge!612g)p7co2+%x)vd(n^jd7m^6o)krl*2pr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #my apps
    'problems',
    'accounts',
    'oauth',
    'contests',
    'submissions',

    # #third party
    # 'social.apps.django_app.default',
    # 'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]
SITE_ID = 1
LOGIN_REDIRECT_URL = "/"
# # OAUTH
# import json
# with open('google_oauth.key') as keyfile: oauthkey = json.load(keyfile)
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = oauthkey['key']
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = oauthkey['secret']
# AUTHENTICATION_BACKENDS = (
#     'social.backends.google.GoogleOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )
# SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/oauth/login/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # 'social_django.middleware.SocialAuthExceptionMiddleware',  # <--

]

ROOT_URLCONF = 'codearea.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends',  # <- Here
                # 'social_django.context_processors.login_redirect', # <- Here
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


WSGI_APPLICATION = 'codearea.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'codearea',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")