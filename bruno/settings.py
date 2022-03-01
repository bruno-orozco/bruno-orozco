
import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY') #'django-insecure-(b**pz9f_^^%r%+ol0t*gh6j$&&5hkbesogd0jksbppu-i5ql+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mensajes',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bruno.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'bruno.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


#import dj_database_url
#from decouple import config
#DATABASES =  {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')
#    )
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'befkj426p0hdwhrjuz8s',
        'USER': 'uukoels0rzn4xaq0brhl',   
        'PASSWORD': 'AZR9jJyhE8WZzccnjA7A',
        'HOST': 'befkj426p0hdwhrjuz8s-postgresql.services.clever-cloud.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'
#
#
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#
#
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, '/static/'),
#)
#
#if DEBUG:
#        STATICFILES_DIRS = [
#            os.path.join(BASE_DIR, 'static')
#       ]
#else:
#        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Here, they well be accessible at your-domain.onrender.com/static/...
STATIC_URL = '/static/'

# Following settings only make sense on production and may break development environments.
if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'formatters': {
#        'verbose': {
#            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
#                       'pathname=%(pathname)s lineno=%(lineno)s '
#                       'funcname=%(funcName)s %(message)s'),
#            'datefmt': '%Y-%m-%d %H:%M:%S'
#        },
#        'simple': {
#            'format': '%(levelname)s %(message)s'
#        }
#    },
#    'handlers': {
#        'null': {
#            'level': 'DEBUG',
#            'class': 'logging.NullHandler',
#        },
#        'console': {
#            'level': 'INFO',
#            'class': 'logging.StreamHandler',
#            'formatter': 'verbose'
#        }
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['console'],
#            'level': 'DEBUG',
#            'propagate': True,
#        },
#        'django.request': {
#            'handlers': ['console'],    
#            'level': 'DEBUG',
#            'propagate': False,
#        },
#    }
#}

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
#EMAIL_HOST = "smpt.gmail.com"
#
#EMAIL_USE_TLS = True
#
#EMAIL_PORT = 587
#
#EMAIL_HOST_USER = "bruno.pdtlpu@gmail.com"
#
#EMAIL_HOST_PASSWORD = "chabelita2020"