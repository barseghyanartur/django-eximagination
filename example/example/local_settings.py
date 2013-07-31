# Django settings for resato_portal project.
import os
PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

DEBUG = True
DEBUG_TOOLBAR = not True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_DIR('../db/example.db'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR('../tmp')

DEFAULT_FROM_EMAIL = '<no-reply@example.com>'

# eximagination conf follows...

# For testing purposes, files exlire after 10 seconds. Set something like 30 days (2592000) in production
EXIMAGINATION_EXPIRATION_INTERVAL = 10

# Make sure to set this to False in production.
EXIMAGINATION_DEBUG = True