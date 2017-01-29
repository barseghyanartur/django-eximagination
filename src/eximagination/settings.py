from .conf import get_setting

__title__ = 'eximagination.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MEDIA_ROOT',
    'MEDIA_URL',
    'MEDIA_RELATIVE_ROOT',
    'EXPIRATION_INTERVAL',
    'DEBUG'
)

MEDIA_ROOT = get_setting('MEDIA_ROOT')
MEDIA_URL = get_setting('MEDIA_URL')
MEDIA_RELATIVE_ROOT = get_setting('MEDIA_RELATIVE_ROOT')
EXPIRATION_INTERVAL = get_setting('EXPIRATION_INTERVAL')
DEBUG = get_setting('DEBUG')  # Set back to settings from DEBUG.
