from .base import *

# Debug
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-DEBUG
DEBUG = False

# Allowed Hosts
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_secret("ALLOWED_HOSTS")

# E-Mail
# https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_secret("EMAIL_HOST")
DEFAULT_FROM_EMAIL = get_secret("EMAIL_ADDRESS")
SERVER_EMAIL = get_secret("EMAIL_ADDRESS")
EMAIL_PORT = get_secret("EMAIL_PORT")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Logging
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING_DIR = os.path.join(BASE_DIR, 'tmp/logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'file', 'mail_admins'],
            'propagate': False,
            'level': 'INFO',
        },
    }
}
