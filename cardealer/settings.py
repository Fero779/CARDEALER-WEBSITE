import dj_database_url
from pathlib import Path  

# BASE_DIR should now be a Path object, using pathlib
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '934nw3r62@!m0^ksgw3#31tntglnr%td+-_b89xpu2@q2zqv=d'

DEBUG = True  # Change to False in production

ALLOWED_HOSTS = ['*']
LOGIN_REDIRECT_URL = 'dashboard'


# Application definition
INSTALLED_APPS = [
    'cars.apps.CarsConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django.contrib.humanize',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',  # Uncomment if using social accounts
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Ensure Whitenoise is installed
]

ROOT_URLCONF = 'cardealer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Ensure this is pointing to the correct templates directory
        ],
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

WSGI_APPLICATION = 'cardealer.wsgi.application'


# Database configuration (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cardealer_db', 
        'USER': 'myuser',       
        'PASSWORD': 'mypassword',  
        'HOST': 'localhost',     
        'PORT': '5432',  
    }
}


# Password validation
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'  # Set to 'UTC' for consistency with PostgreSQL

USE_I18N = True

USE_L10N = True

USE_TZ = True  # Ensure time zone handling is enabled

import os
import django_heroku

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Use 'staticfiles' for Heroku
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)  # Same as your setup, but in tuple form
django_heroku.settings(locals())  # Configure settings for Heroku


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

SITE_ID = 1

# Whitenoise settings for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
