from django.core.exceptions import ImproperlyConfigured
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Secret settings
with open(os.path.join(BASE_DIR, "tmp/secrets.json")) as f:
    secrets_json = json.loads(f.read())


def get_secret(setting, secrets=secrets_json):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable.".format(setting)
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = get_secret('SECRET_KEY')

# Application definition
# https://docs.djangoproject.com/en/dev/ref/applications/
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'apps.users',
    'apps.frontend',
    'apps.applicants',
    'crispy_forms'
]

# Middleware
# https://docs.djangoproject.com/en/dev/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "tmp/db.sqlite3"),
    }
}

# Url conf
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-ROOT_URLCONF
ROOT_URLCONF = 'config.urls'

# Templates
# https://docs.djangoproject.com/en/dev/topics/templates/#configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-WSGI_APPLICATION
WSGI_APPLICATION = 'config.wsgi.application'

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Authentication
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-AUTH_USER_MODEL
AUTH_USER_MODEL = "users.User"

# Login
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-user-model
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/admin/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'tmp/static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp/media')

# mail errors to the admins
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#admins
ADMINS = [('Daniel Mössner', 'bugs@tortuga-webdesign.de')]

# sites framework
# https://docs.djangoproject.com/en/dev/ref/contrib/sites/
SITE_ID = 1
