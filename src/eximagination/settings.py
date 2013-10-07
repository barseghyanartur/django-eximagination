__title__ = 'eximagination.settings'
__version__ = '0.7'
__build__ = 0x000007
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('MEDIA_ROOT', 'MEDIA_URL', 'MEDIA_RELATIVE_ROOT', 'EXPIRATION_INTERVAL', 'DEBUG')

from eximagination.conf import get_setting

MEDIA_ROOT = get_setting('MEDIA_ROOT')
MEDIA_URL = get_setting('MEDIA_URL')
MEDIA_RELATIVE_ROOT = get_setting('MEDIA_RELATIVE_ROOT')
EXPIRATION_INTERVAL = get_setting('EXPIRATION_INTERVAL')
DEBUG = get_setting('DEBUG') # Set back to settings from DEBUG.